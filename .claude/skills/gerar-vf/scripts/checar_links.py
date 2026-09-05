#!/usr/bin/env python3
"""Valida links internos (arquivo + âncora) dos .md do repositório.

Uso:
    python3 checar_links.py                      # varre o repo inteiro
    python3 checar_links.py --slug "Título"      # mostra a âncora de um título

Por que existe: o GitHub gera a âncora convertendo CADA espaço em um hífen depois de
remover a pontuação. Um título com travessão ("A — B") vira "#a--b", com hífen duplo.
Calcular isso de cabeça produz links que parecem certos e não levam a lugar nenhum.
"""

import os
import re
import sys
import unicodedata
import urllib.parse

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))


def gh_slug(titulo: str) -> str:
    """Reproduz o github-slugger: minúsculas, sem pontuação, cada espaço vira um hífen."""
    s = titulo.strip().lower()
    s = "".join(c for c in s if unicodedata.category(c)[0] in "LNM" or c in " -_")
    return s.replace(" ", "-")


def ancoras(caminho: str) -> set:
    """Âncoras geradas pelos cabeçalhos de um arquivo (ignora blocos de código)."""
    achadas, cerca = set(), False
    with open(caminho, encoding="utf-8") as fh:
        for linha in fh:
            if linha.lstrip().startswith("```"):
                cerca = not cerca
                continue
            if cerca:
                continue
            m = re.match(r"^#{1,6}\s+(.*?)\s*$", linha)
            if not m:
                continue
            texto = re.sub(r"[*_`]", "", m.group(1))
            texto = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", texto)
            achadas.add(gh_slug(texto))
    return achadas


def sem_codigo(conteudo: str) -> str:
    """Remove blocos cercados e trechos inline de código.

    Exemplos dentro de crase não são links de verdade — sem isso, o template de um
    arquivo de instruções acusa falso positivo.
    """
    conteudo = re.sub(r"^```.*?^```", "", conteudo, flags=re.S | re.M)
    return re.sub(r"`[^`\n]*`", "", conteudo)


def varrer() -> int:
    arquivos = [
        os.path.normpath(os.path.join(raiz, nome))
        for raiz, _dirs, nomes in os.walk(REPO)
        for nome in nomes
        if nome.endswith(".md") and ".git" not in raiz
    ]
    cache = {a: ancoras(a) for a in arquivos}
    problemas = []

    for arq in arquivos:
        with open(arq, encoding="utf-8") as fh:
            conteudo = sem_codigo(fh.read())
        for rotulo, alvo in re.findall(r"\[([^\]]+)\]\(([^)\s]+)\)", conteudo):
            if "#" not in alvo or alvo.startswith(("http", "mailto")):
                continue
            parte_arq, ancora = alvo.split("#", 1)
            ancora = urllib.parse.unquote(ancora)
            destino = arq
            if parte_arq:
                destino = os.path.normpath(
                    os.path.join(os.path.dirname(arq), urllib.parse.unquote(parte_arq))
                )
            if destino not in cache:
                problemas.append((arq, rotulo, alvo, "arquivo não encontrado"))
            elif ancora not in cache[destino]:
                problemas.append((arq, rotulo, "#" + ancora, "âncora inexistente"))

    for arq, rotulo, alvo, motivo in problemas:
        rel = os.path.relpath(arq, REPO)
        print(f"{motivo.upper()}  |  {rel}  |  [{rotulo[:45]}]\n     {alvo}\n")

    print(f"{len(problemas)} link(s) quebrado(s) em {len(arquivos)} arquivos .md verificados")
    return 1 if problemas else 0


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "--slug":
        print("#" + gh_slug(sys.argv[2]))
    else:
        sys.exit(varrer())
