---
name: gerar-vf
description: Gera blocos de afirmativas Verdadeiro/Falso para treino ativo a partir dos arquivos de teoria deste repositório de estudo do QOS/PMMG, salvando em `<eixo>/testes/`. Use sempre que o usuário pedir questões, afirmativas, itens de treino, "me testa em X", "gerar V/F do 6.07", "quero praticar tal tópico", "criar testes do tópico", ou quando ele quiser transformar teoria em material de autoavaliação — mesmo sem dizer "V/F" explicitamente. Use também para ampliar a cobertura de um arquivo de testes existente, para montar questões no formato da banca (assertivas I-IV) a partir dos itens já gerados, ou para migrar questões antigas para este formato.
---

# Gerar afirmativas V/F

## Por que este formato existe

O objetivo não é produzir questões bonitas: é forçar **recuperação ativa**. Reler texto
corrido dá sensação de domínio sem produzir retenção; tentar responder antes de ver a
resposta produz. Por isso três coisas não são negociáveis no formato:

1. **O gabarito fica escondido** (`<details>`), depois do bloco inteiro. Se a resposta
   estiver visível, virou leitura.
2. **Todo item falso é corrigido no gabarito.** Este é o ponto mais importante. Ler uma
   afirmação falsa cria familiaridade com a versão errada — se o gabarito disser apenas
   "(F)", você acaba de ensinar o erro. O gabarito precisa dizer *o que estava lá* e *o que
   é o certo*.
3. **Todo item aponta para a seção da teoria de onde saiu.** O ganho real vem do erro: em vez
   de reler o capítulo, o usuário abre o link e lê o parágrafo específico.

## Onde o arquivo vive

Espelhe o nome do arquivo de teoria dentro da subpasta `testes/` do mesmo eixo:

```
6. Farmacoterapia Clínica/
├── 6.07 Hormônios e seus antagonistas - distúrbios endocrinológicos.md   ← teoria
└── testes/
    └── 6.07 Hormônios e seus antagonistas - distúrbios endocrinológicos.md   ← itens V/F
```

Mesmo nome, pasta diferente. Isso torna o par óbvio e permite localizar um pelo outro sem
convenção extra. Se o arquivo de testes já existir, **acrescente blocos ao final** e continue
a numeração — não reescreva o que já está lá, porque o usuário pode ter registrado erros nele.

## Regra de ouro: a fonte é o arquivo de teoria, sempre

O conteúdo dos itens sai **do arquivo de teoria do tópico** — é ele que precisa ser coberto de
ponta a ponta. O banco de questões (`QOS_PMMG_Banco_de_Questoes.md`) entra apenas como
referência de **formato** e de **prioridade** (quais assuntos a banca já cobrou naquele tópico);
nunca como fonte dos itens, e nunca como conteúdo a ser reciclado em V/F.

Todo fato de um item — especialmente números, doses, prazos, concentrações, siglas de órgãos,
números de portaria e nomes de fármacos — precisa existir literalmente no arquivo de teoria.
Nunca complete com conhecimento externo, por mais certo que você esteja: o usuário estuda para
uma prova cuja fonte é esse material, e um item "certo pelo mundo" mas ausente do texto
quebra a confiança dele no gabarito.

Confira cada número dígito a dígito contra a fonte antes de escrever. Se um fato do arquivo
parecer errado ou desatualizado, **não conserte dentro do item** — avise o usuário
separadamente, para que ele decida corrigir a teoria primeiro.

## Vigência: a armadilha específica deste repositório

Vários arquivos de teoria são transcrições de edições antigas (o 6.07, por exemplo, é o
Goodman & Gilman de 2012) com blocos *Nota de atualização* inseridos depois. Gerar um item a
partir de um trecho já superado ensina o erro com o selo de "gabarito".

- Gere itens a partir do **texto já corrigido e das notas de atualização**.
- Quando o contraste velho/novo for interessante, faça o *contraste* ser o item
  ("o critério de creatinina foi substituído pela TFGe" → V). É um dos tipos mais valiosos.
- Quando o item vier de trecho da transcrição antiga que ainda não tem nota de atualização,
  marque `[fonte 2012]` no gabarito e registre isso nas pendências do arquivo. É sinal de que
  aquele trecho da teoria ainda precisa ser conferido.

## Estrutura do arquivo

Use este esqueleto. O cabeçalho e as duas tabelas existem para o arquivo funcionar como
registro de estudo, não só como lista de perguntas.

```markdown
# Testes V/F — <código e nome do tópico>

> **Teoria:** [<nome do tópico>](../<arquivo>.md) · **Eixo N — <nome do eixo>**
> **Itens:** N (blocos 1-N) · Gerado em DD/MM/AAAA a partir do arquivo de teoria.

Responda o bloco inteiro antes de abrir o gabarito. Para todo item que julgar **falso**, diga
também *qual é o certo* — é isso que transforma reconhecimento em recuperação de verdade.

## Registro de rodadas

| Data | Blocos | Acertos | Errados (nº dos itens) | Próxima revisão |
| :--- | :--- | :--- | :--- | :--- |
|  |  |  |  |  |

## Bloco N — <tema do bloco>

1. <afirmativa>
2. ...

<details>
<summary><strong>GABARITO — bloco N</strong> — clique para revelar</summary>

1. **(V)** — apoio: "<citação curta e literal>" · [seção](../<arquivo>.md#<âncora>)
2. **(F)** — padrão N (<nome>) · consta: "<termo errado>" → correto: "<termo original>" · apoio: "<citação>" · [seção](../<arquivo>.md#<âncora>)

</details>

## Cobertura

| Seção da teoria | Itens |
| :--- | :--- |

## Pendências
```

Blocos de **5 itens**, com numeração contínua ao longo do arquivo (1-5, 6-10, 11-15...). A
numeração contínua é o que permite anotar "errei o 13 e o 17" no registro de rodadas.

**Embaralhe os blocos.** Cada bloco mistura assuntos distintos do capítulo, em vez de agrupar
tudo de um fármaco. Blocos temáticos deixam o estudo cômodo e enganoso: sabendo que o bloco
todo é de metformina, metade do trabalho de recuperação já está feito. Discriminar entre temas
parecidos é exatamente o que a prova cobra. A tabela de cobertura, ao final, é que organiza o
material por seção.

**Use links de referência** para não repetir o caminho longo do arquivo de teoria em cada item:
defina `[rótulo]: ../<arquivo>.md#<âncora>` no fim do arquivo e escreva `[seção][rótulo]` no
gabarito. O validador confere as duas formas.

## Como escrever os itens

**Verdadeiras: paráfrase, nunca cópia.** Reescreva com outra estrutura sintática e outro
vocabulário, preservando o sentido. Se o usuário puder acertar só por reconhecer a frase do
livro, o item não testa conhecimento — testa memória visual da página.

**Falsas: um único ponto alterado.** O resto da frase permanece correto, fluente e plausível.
O erro precisa ser detectável por conhecimento, não por estranheza de redação. Nada de
absurdos: um item que soa esquisito se resolve sem saber o conteúdo.

**Empareie o comprimento.** Falsas tendem a ficar mais longas porque ganham o qualificador
inserido. Se as longas forem sempre as falsas, o usuário aprende a detectar o padrão em vez do
conteúdo. Confira o tamanho médio dos dois grupos antes de fechar o bloco.

**Proporção ~50/50, embaralhada.** Sem alternância regular, sem agrupar as verdadeiras, sem
repetir o mesmo padrão de corrupção em sequência.

**Inclua itens de aplicação, não só de recall.** Um item que dá um caso concreto e exige
aplicar um critério ("paciente de 58 anos, homem, hipertenso, sem DCV estabelecida — cumpre o
critério etário?") vale mais que três de repetição de número, e é assim que a banca cobra.

## Padrões de corrupção

Varie entre eles e não repita o mesmo tipo em sequência. Os sete primeiros vêm do uso já
consolidado no banco de questões; os três últimos são recorrentes nesta banca em específico.

| Nº | Padrão | Como se faz |
| :--- | :--- | :--- |
| 1 | Exceção removida ou acrescentada | "salvo em casos excepcionais" → "em nenhuma hipótese" |
| 2 | Quantificador absoluto | inserir "apenas", "todos", "sempre", "nunca" |
| 3 | Número trocado | dose, prazo, concentração, mandato, percentual |
| 4 | Autoridade ou órgão invertido | quem executa, quem autoriza, quem julga |
| 5 | Modal trocado | "pode" ↔ "deve", "é facultado" ↔ "é obrigatório" |
| 6 | Inversão de direção | aumenta ↔ diminui, inibe ↔ induz, superior ↔ inferior |
| 7 | Atribuição trocada | o fato está correto, mas colado no fármaco, classe ou artigo errado |
| 8 | Via ou tempo trocado | via de administração, frequência, jejum × com alimento |
| 9 | Registro ≠ incorporação | ter registro na ANVISA tratado como estar no SUS/PCDT |
| 10 | Critério superado como vigente | apresentar o valor da edição antiga como conduta atual |

O padrão 10 é o de maior rendimento neste repositório e o mais perigoso: use-o, mas o gabarito
precisa deixar explícito qual é o critério que vale hoje e desde quando.

## Links de seção: cuidado com o travessão

O GitHub monta a âncora assim: minúsculas, remove a pontuação e converte **cada espaço** em um
hífen. Como o travessão é removido mas os dois espaços ao redor dele não, um título com `—`
gera **hífen duplo**:

```
"Inibidores do SGLT2 — a lacuna mais grave"  →  #inibidores-do-sglt2--a-lacuna-mais-grave
```

Errar isso produz um link que parece certo e não vai a lugar nenhum. Não calcule de cabeça:

```bash
python3 .claude/skills/gerar-vf/scripts/checar_links.py --slug "Título da seção"
```

E depois de escrever o arquivo, valide tudo de uma vez (varre o repo inteiro):

```bash
python3 .claude/skills/gerar-vf/scripts/checar_links.py
```

O caminho relativo de `<eixo>/testes/` até a teoria começa com `../`, e espaços e acentos vão
percent-encoded, como já se faz nos READMEs dos eixos.

**Aponte para o cabeçalho do fármaco ou do assunto**, não para subtítulos genéricos. Um arquivo
de teoria repete "Mecanismo de ação" e "Efeitos adversos e interações medicamentosas" a cada
classe, e o GitHub resolve duplicatas anexando `-1`, `-2`, `-3` conforme a ordem — âncora
frágil, que quebra assim que alguém insere uma seção. Prefira `#metformina`, `#tiazolidinedionas`,
`#inibidores-da-dpp-4`.

## Antes de fechar o arquivo, meça

Um conjunto de V/F pode estar todo correto e ainda assim ser inútil, se der para acertar sem
saber o conteúdo. Rode:

```bash
python3 .claude/skills/gerar-vf/scripts/conferir_itens.py "<eixo>/testes/<arquivo>.md"
```

Ele mede o que a intuição não pega: proporção V/F, comprimento médio de cada grupo, blocos
homogêneos, padrões repetidos em sequência e concentração de "número trocado". As três
armadilhas que mais aparecem — todas invisíveis a olho nu e todas fatais para o valor do
material:

- **Um grupo mais longo que o outro.** Ao escrever, a tendência é justificar mais as
  verdadeiras (ou enfeitar mais as falsas). Se a diferença passa de ~25%, o comprimento vira
  a resposta.
- **Conversões concentradas.** Ao corrigir a proporção V/F no fim, é fácil converter vários
  itens seguidos e criar um bloco inteiramente falso. Distribua as correções entre os blocos.
- **Excesso de troca de número.** É o padrão mais fácil de gerar e o que menos ensina. Se
  passar de um terço, converta alguns em inversão de direção, atribuição trocada ou modal.

## Cobertura

O pedido de fundo é "pegar todos os cantos", então gere **percorrendo a árvore de cabeçalhos do
arquivo de teoria**, seção por seção — não "de memória" sobre o tópico, que concentra tudo no
começo do arquivo. Feche o arquivo com a tabela de cobertura (seção → nº de itens) para que a
próxima passada saiba onde continuar.

Prioridade dentro de um tópico:

1. O que a banca já cobrou ali (o banco de questões e o campo "Questões nas provas" dizem).
2. Seções "Pontos-chave" e "Atualizações desde a…" — maior densidade por linha.
3. Tudo que é falsificável: números, prazos, contraindicações, competências, quem faz o quê.

Não force volume: bibliografia, notas de transcrição e legendas de figura não rendem itens.
Um tópico grande como o 6.07 comporta 120-160 itens; um tópico curto de legislação, 40-60.

## Ao terminar

1. Rode os dois scripts: `checar_links.py` (sem argumento, varre o repo) e `conferir_itens.py`
   no arquivo gerado. Corrija o que aparecer antes de entregar.
2. Confira as citações do gabarito contra o arquivo de teoria. Como o texto é quebrado em
   linhas e há prefixo `>` nas notas, compare com espaços normalizados em vez de `grep` cru.
3. No arquivo de **teoria**, preencha a seção "Questões relacionadas" com o link para o arquivo
   de testes e os códigos das questões reais do banco sobre aquele tópico.
4. No "Controle de revisão" da teoria, acrescente o que fizer sentido (`[ ] Testes V/F gerados`).
5. Diga ao usuário quantos itens saíram, que seções ficaram cobertas e o que ficou de fora.
6. **Relate os defeitos que encontrou no arquivo de teoria** (erro de transcrição, parágrafo
   partido, número que contradiz outra passagem) em vez de gerar item em cima deles. O usuário
   decide se corrige a teoria antes de estudar — e essa lista costuma ser um dos subprodutos
   mais úteis da geração.

## Dois modos a partir do mesmo pool

Quando o usuário quiser treinar o **formato da prova**, monte questões de assertivas a partir
de itens já existentes no arquivo: escolha quatro (misturando V e F), apresente como I-IV e
peça "estão corretas:" com alternativas A-D. Não escreva conteúdo novo para isso — a graça é
que o mesmo item serve para os dois modos, e o gabarito já está pronto.
