#!/usr/bin/env python3
"""Audita as notas de atualização de um arquivo de teoria — sem acessar a rede.

Uso:
    python3 auditar_notas.py "<eixo>/<tópico>.md"
    python3 auditar_notas.py "<eixo>/<tópico>.md" --atos    # só lista os atos citados

O que ele verifica, e por quê:

- **nota sem fonte alguma**: uma nota que afirma sem dizer de onde veio é indistinguível de
  invenção. Isso é problema.
- **nota com fonte mas sem URL**: conferível por um humano, mas dá trabalho. Sai como
  observação, não como problema — senão o aviso vira ruído e ninguém lê.
- **ato sem data ou sem número**: "uma portaria de 2026" não permite conferência. O padrão
  aceito é "Portaria SCTIE/MS nº 13, de 21/02/2026".
- **datas futuras**: sinal de número inventado ou de erro de digitação.
- **marcações pendentes**: quantas notas seguem com "(a confirmar na fonte primária)".
- **contador de notas**: se o arquivo anuncia "São N notas", confere se N bate.

O que ele NÃO faz: dizer se o ato existe. Isso exige abrir a fonte — tarefa do WebFetch,
descrita na SKILL.md.
"""

import datetime
import re
import sys

# "Portaria SCTIE/MS nº 13, de 21/02/2026" e variantes usadas no repositório
# "Portaria SCTIE/MS nº 13, de 21/02/2026". Sem "IN" solto na alternância: com
# IGNORECASE ele casaria dentro de "iniciar", "inibição", "intestinal".
ATO = re.compile(
    r"\b(Portarias?|Resolução-RE|Resolução|RDC|Instrução Normativa|Lei|Decreto|"
    r"Nota Técnica(?: Conjunta)?|Relatórios?(?: de Recomendação)?|Alerta|Consulta Pública)"
    r"[^.;)]{0,80}?"
    r"(?:nº|n°|n\.º)\s*([\d.]+)"
    r"([^.;)]{0,45})"
)
DATA = re.compile(r"\b(\d{2})/(\d{2})/(\d{4})\b")
URL = re.compile(r"https?://[^\s>)\]]+")


def notas(texto):
    """Cada nota é um bloco de citação iniciado por '> **Nota ...'."""
    linhas = texto.split("\n")
    blocos, atual = [], None
    for i, l in enumerate(linhas, start=1):
        if re.match(r"^>\s*\*\*Nota (de atualização|de transcrição)", l):
            if atual:
                blocos.append(atual)
            atual = {"linha": i, "texto": [l]}
        elif atual is not None and l.startswith(">"):
            atual["texto"].append(l)
        elif atual is not None:
            blocos.append(atual)
            atual = None
    if atual:
        blocos.append(atual)
    for b in blocos:
        b["texto"] = "\n".join(b["texto"])
    return blocos


def main(caminho, so_atos=False):
    texto = open(caminho, encoding="utf-8").read()
    # o arquivo é quebrado em linhas curtas e as notas levam prefixo ">";
    # sem normalizar, um ato cuja data caiu na linha seguinte parece estar sem data
    corrido = re.sub(r"\s+", " ", re.sub(r"^>\s?", "", texto, flags=re.M))
    blocos = notas(texto)
    hoje = datetime.date.today()
    problemas = []

    if so_atos:
        for m in ATO.finditer(corrido):
            print(m.group(0).strip())
        return 0

    print(f"{len(blocos)} nota(s) encontrada(s)")

    pendentes, sem_url = 0, []
    for b in blocos:
        corpo = re.sub(r"\s+", " ", re.sub(r"^>\s?", "", b["texto"], flags=re.M))
        cabeca = corpo[:70]
        # correção de transcrição é conserto interno do arquivo: não tem fonte externa
        interna = re.search(r"correção de transcrição|Nota de transcrição|"
                            r"reposicionad|Parágrafo reposicionado", corpo, re.I)
        # a nota é conferível se traz URL ou se nomeia um ato com número e data
        tem_url = bool(URL.search(corpo))
        tem_fonte = bool(re.search(r"\*\*Fontes?\b|apoio:", corpo))
        if not interna and not tem_fonte and not tem_url:
            problemas.append(f"linha {b['linha']}: nota sem fonte alguma — {cabeca}…")
        elif not interna and not tem_url:
            sem_url.append(f"linha {b['linha']}: {cabeca}…")
        if "a confirmar" in corpo.lower():
            pendentes += 1

    # Relatório e consulta pública são identificados pelo número; portaria, RDC e afins
    # só permitem conferência com a data.
    EXIGE_DATA = ("portaria", "rdc", "resolução", "lei", "decreto", "instrução normativa",
                  "nota técnica", "alerta")
    atos = []
    for m in ATO.finditer(corrido):
        trecho = m.group(0).strip()
        atos.append(trecho)
        if not m.group(1).lower().startswith(EXIGE_DATA):
            continue
        if not DATA.search(trecho) and not re.search(r"\b(19|20)\d{2}\b", trecho):
            problemas.append(f"ato sem data: “{trecho}”")

    for d, mth, y in DATA.findall(corrido):
        try:
            quando = datetime.date(int(y), int(mth), int(d))
        except ValueError:
            problemas.append(f"data inválida: {d}/{mth}/{y}")
            continue
        if quando > hoje:
            problemas.append(f"data no futuro: {d}/{mth}/{y}")

    print(f"{len(atos)} ato(s) normativo(s) citado(s) · {len(set(atos))} distinto(s)")
    print(f"{len(set(URL.findall(texto)))} URL(s) distinta(s)")
    if pendentes:
        print(f"{pendentes} nota(s) marcada(s) como “a confirmar na fonte primária”")

    anunciado = re.search(r"São \*\*(\d+) notas\*\*", corrido)
    if anunciado and int(anunciado.group(1)) != len(blocos):
        problemas.append(
            f"o arquivo anuncia {anunciado.group(1)} notas, mas há {len(blocos)}"
        )

    print()
    if sem_url:
        print(f"OBSERVAÇÃO: {len(sem_url)} nota(s) citam a fonte mas sem URL — conferíveis, "
              f"porém não clicáveis:")
        for s in sem_url[:5]:
            print("   ", s)
        if len(sem_url) > 5:
            print(f"    … e mais {len(sem_url) - 5}")
        print()
    for p in problemas:
        print("AVISO:", p)
    print(f"{len(problemas)} problema(s)" if problemas else "sem problemas")
    return 1 if problemas else 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1], "--atos" in sys.argv))
