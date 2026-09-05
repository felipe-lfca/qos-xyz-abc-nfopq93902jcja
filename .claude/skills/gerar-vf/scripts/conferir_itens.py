#!/usr/bin/env python3
"""Confere se um arquivo de testes V/F é honesto — isto é, se não dá para acertar
sem saber o conteúdo.

Uso:
    python3 conferir_itens.py "<eixo>/testes/<arquivo>.md"

O que ele mede e por quê:

- **numeração e pareamento**: todo item precisa de gabarito e vice-versa, com numeração
  contínua, porque o registro de rodadas identifica os erros pelo número.
- **equilíbrio V/F**: perto de 50/50. Se pender muito, "chutar V" vira estratégia vencedora.
- **comprimento médio**: se as falsas forem sistematicamente mais longas (ou mais curtas),
  o tamanho denuncia a resposta e o item deixa de testar conhecimento.
- **blocos homogêneos**: um bloco todo V ou todo F entrega a resposta pelo padrão.
- **padrões em sequência**: duas falsas vizinhas com a mesma corrupção ensinam a procurar
  a corrupção, não o conteúdo.
- **concentração de padrões**: troca de número é o padrão mais fácil de gerar e o mais
  fraco pedagogicamente; se passar de ~⅓ das falsas, o material fica raso.
"""

import re
import sys

LIMITE_DESEQUILIBRIO = 0.60      # proporção de V (ou F) a partir da qual avisa
LIMITE_COMPRIMENTO = 0.25        # diferença relativa tolerada entre as médias
LIMITE_PADRAO_3 = 0.35           # fração máxima desejável de "número trocado"

NOMES = {
    "1": "exceção removida", "2": "quantificador", "3": "número trocado",
    "4": "autoridade/norma", "5": "modal trocado", "6": "inversão de direção",
    "7": "atribuição trocada", "8": "via ou tempo", "9": "registro ≠ SUS",
    "10": "critério superado",
}


def carregar(caminho):
    txt = open(caminho, encoding="utf-8").read()
    enun, gab = {}, {}
    for bloco in re.split(r"\n## Bloco ", txt)[1:]:
        corpo, _, resto = bloco.partition("<details>")
        for n, t in re.findall(r"^(\d+)\. (.+?)$", corpo, flags=re.M):
            enun[int(n)] = re.sub(r"\s*`\[fonte \d+\]`", "", t).strip()
        for n, v in re.findall(r"^(\d+)\. \*\*\((V|F)\)\*\*", resto, flags=re.M):
            gab[int(n)] = v
    return txt, enun, gab


def main(caminho):
    txt, enun, gab = carregar(caminho)
    problemas = []

    if not enun:
        print("nenhum bloco encontrado — o arquivo segue o formato da skill?")
        return 1

    faltando = sorted(set(enun) ^ set(gab))
    if faltando:
        problemas.append(f"itens sem par enunciado/gabarito: {faltando}")
    esperado = list(range(1, len(enun) + 1))
    if sorted(enun) != esperado:
        problemas.append("numeração não é contínua a partir de 1")

    V = [len(enun[n]) for n in gab if gab[n] == "V" and n in enun]
    F = [len(enun[n]) for n in gab if gab[n] == "F" and n in enun]
    total = len(V) + len(F)
    print(f"{total} itens · V: {len(V)} ({100*len(V)//total}%) · F: {len(F)} ({100*len(F)//total}%)")
    if max(len(V), len(F)) / total > LIMITE_DESEQUILIBRIO:
        problemas.append(f"proporção V/F desequilibrada ({len(V)}/{len(F)})")

    mv, mf = sum(V) // len(V), sum(F) // len(F)
    dif = abs(mv - mf) / max(mv, mf)
    print(f"comprimento médio — V: {mv} caracteres · F: {mf} ({dif:.0%} de diferença)")
    if dif > LIMITE_COMPRIMENTO:
        mais = "verdadeiras" if mv > mf else "falsas"
        problemas.append(f"as {mais} são bem mais longas: o tamanho denuncia a resposta")

    blocos = (total + 4) // 5
    homog = [i + 1 for i in range(blocos)
             if len({gab[n] for n in range(i*5+1, min(i*5+6, total+1)) if n in gab}) == 1]
    if homog:
        problemas.append(f"blocos com todos os itens do mesmo valor: {homog}")

    seq = re.findall(r"^(\d+)\. \*\*\(F\)\*\* — padrão (\d+)", txt, flags=re.M)
    rep = [seq[i][0] for i in range(1, len(seq))
           if seq[i][1] == seq[i-1][1]
           and int(seq[i][0]) == int(seq[i-1][0]) + 1
           and (int(seq[i][0]) - 1)//5 == (int(seq[i-1][0]) - 1)//5]
    if rep:
        problemas.append(f"falsas vizinhas com o mesmo padrão (mesmo bloco): {rep}")

    pads = re.findall(r"padrão (\d+)", txt)
    if pads:
        print("padrões de corrupção:")
        for p in sorted(set(pads), key=int):
            c = pads.count(p)
            print(f"  {p:>2} {NOMES.get(p, '?'):<20} {c:>3}  {100*c//len(pads):>2}%")
        if pads.count("3") / len(pads) > LIMITE_PADRAO_3:
            problemas.append("mais de um terço das falsas são troca de número — varie os padrões")

    print()
    for p in problemas:
        print("AVISO:", p)
    print(f"{len(problemas)} problema(s)" if problemas else "sem problemas")
    return 1 if problemas else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
