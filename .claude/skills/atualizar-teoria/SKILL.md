---
name: atualizar-teoria
description: Busca na internet o que mudou desde a edição do livro-texto em um tópico deste repositório de estudo do QOS/PMMG e registra o resultado como notas de atualização no arquivo de teoria, sempre com o ato normativo e a fonte primária. Use quando o usuário pedir para "atualizar o 6.07", "ver o que mudou nesse tópico", "conferir se a teoria está atual", "buscar atualizações da ANVISA/Conitec/PCDT sobre X", ou quando ele desconfiar que o livro está defasado — e também antes de gerar questões sobre um tópico cuja transcrição seja de edição antiga. Roda em **um tópico por vez**.
---

# Atualizar a teoria de um tópico

## Por que existe

A maior parte da teoria deste repositório é transcrição de livro-texto de uma edição específica
— o 6.07, por exemplo, é o Goodman & Gilman de 2012. Em farmácia, boa parte do que a banca
cobra não está no livro: está em portaria de incorporação, PCDT, RDC, nota técnica e diretriz
de sociedade. A seção "Atualizações desde a 12ª edição" do 6.07 é exatamente esse trabalho
feito à mão, e é de onde sai boa parte do material de estudo daquele tópico. Esta skill repete
esse processo em qualquer tópico, com regras que impedem os dois modos de falhar: inventar
número de ato e confundir registro com incorporação.

## Um tópico por vez

Rode em **um arquivo de teoria por vez**, mesmo que o usuário aponte para um eixo inteiro.
Varrer um eixo numa tacada gera resultado inconsistente: o levantamento fica raso onde o
assunto é denso, as buscas se contaminam entre tópicos vizinhos e a checagem de fonte primária
— que é o passo caro — acaba sendo pulada. Se pedirem o eixo todo, faça o primeiro tópico,
mostre o resultado e pergunte se seguem para o próximo.

## O que esta skill não faz

**Não reescreve a transcrição.** O texto do livro fica como está, inclusive onde envelheceu. A
skill só acrescenta blocos `> **Nota de atualização — DD/MM/AAAA.**` e, quando o tópico tiver
uma seção de panorama ("Atualizações desde a …"), atualiza essa seção. A única exceção é o que
já é convenção do repositório: quando uma frase do original virou **incorreta** e a nota
explica a troca, a frase pode ser corrigida no corpo — sempre com a nota registrando o que o
original dizia.

Corrigir erro de transcrição (palavra quebrada, parágrafo fora de lugar) é outra tarefa; não
misture com atualização de conteúdo, e use data e rótulo próprios ("correção de transcrição").

## Se o tópico ainda não tem teoria escrita

Vários arquivos deste repositório são só o template (`Resumo do tópico` e `Pontos-chave` com
`<!-- a preencher -->`, sem nenhuma transcrição). Não há frase alguma para anotar — e mesmo
assim rodar a skill aí tem valor: ela entrega o esqueleto normativo antes mesmo de alguém
escrever a teoria, e evita que a primeira leitura comece de um livro desatualizado sem avisar.

Nesse caso, o passo a passo é o mesmo (base → cabeçalhos do **edital**, já que não há
cabeçalhos de teoria → busca → confirmação), mas o resultado vai em **"Legislação e
referências"**, não em notas espalhadas pelo corpo — porque não há corpo. Estruture como:

- a norma-base do assunto (a portaria ou RDC que qualquer prova vai cobrar);
- o que mudou nela desde a publicação, com o mesmo rigor de fonte das notas comuns;
- pegadinhas conhecidas do assunto (mesmo raciocínio do passo 6, abaixo).

Registre a data do levantamento no topo dessa seção ("Levantamento fechado em …"), do mesmo
jeito que se registraria em "Quando não houver novidade". Isso não substitui escrever a teoria
— é o material que quem for escrevê-la usa como ponto de partida já atualizado.

## Passo a passo

### 1. Estabeleça a linha de base

Antes de buscar qualquer coisa, leia no arquivo de teoria:

- **de que edição e ano** é a transcrição (costuma estar no cabeçalho da seção "Transcrição");
- **quando foi o último levantamento** (a linha "Levantamento fechado em …");
- **quais notas já existem** — para não refazer trabalho nem duplicar nota sobre o mesmo fato.

Sem isso você não sabe o que é novidade. Um tópico já varrido há um mês precisa de uma passada
curta, só do que mudou desde então; um tópico nunca varrido precisa da varredura completa
desde a edição do livro.

### 2. Monte a lista de assuntos a partir dos cabeçalhos

Percorra a árvore de cabeçalhos do arquivo e liste os assuntos concretos — classes de fármacos,
procedimentos, normas citadas. É essa lista que vira consulta, e é ela que garante cobertura;
buscar "atualizações de endocrinologia" devolve manchete, não norma.

Priorize, dentro da lista: o que a banca já cobrou no tópico (o campo "Questões nas provas" e o
banco de questões dizem), o que envolve **número** (dose, prazo, corte laboratorial, critério
de elegibilidade) e o que envolve **disponibilidade no SUS** — as três coisas que mais mudam e
mais caem.

### 3. Busque, restringindo a fontes primárias

Use `WebSearch` com `allowed_domains` apontando para as fontes que decidem o assunto. A lista
por tipo de pergunta está em [references/fontes.md](references/fontes.md) — leia antes de
começar as buscas.

Duas cautelas sobre a ferramenta: `allowed_domains` é filtro **frouxo** (pedir `gov.br` também
traz `saude.sc.gov.br` e às vezes um resultado de fora), então confira o domínio de cada
resultado que você for usar; e o resumo que a busca devolve é texto de terceiros — serve para
localizar o ato, não como prova de que ele existe.

### 4. Confirme na fonte primária

Para cada mudança que você pretende registrar, abra a fonte com `WebFetch` e confirme **número
do ato, data e conteúdo**. Se a fonte confirmar, a nota afirma. Três desfechos possíveis:

| Situação | Como registrar |
| :--- | :--- |
| Fonte primária aberta e confirmada | Afirme, citando o ato e a data |
| Só fonte secundária (notícia, portal comercial, sociedade) | Afirme com ressalva e escreva **(a confirmar na fonte primária)** |
| `WebFetch` bloqueado pelo ambiente (`EGRESS_BLOCKED`) | Registre com **(a confirmar na fonte primária)** e diga ao usuário quais URLs ele precisa abrir |

O último caso é comum: em sessão remota a saída de rede costuma ser restrita a uma allowlist, e
`WebFetch` falha em `gov.br` e afins, embora `WebSearch` funcione. Isso **não** é motivo para
afirmar assim mesmo — é motivo para marcar. Na máquina do usuário o `WebFetch` normalmente
funciona e a mesma nota pode ser promovida a confirmada.

### 5. Nunca invente ato normativo

É o modo de falhar mais perigoso desta skill, porque um número de portaria plausível é
indistinguível de um verdadeiro para quem está estudando. Regras:

- Todo ato citado precisa vir **de um resultado de busca que você leu**, nunca de memória.
- Todo ato citado precisa aparecer com **número e data completos** ("Portaria SCTIE/MS nº 13,
  de 21/02/2026"), não "uma portaria de 2026".
- Toda nota precisa terminar com uma linha `> **Fonte:**` ou `> **Fontes:**` contendo pelo
  menos **uma URL**, para que o usuário possa conferir.
- Se você lembra de uma mudança mas não achou a fonte, **diga isso ao usuário** em vez de
  escrever a nota.

**Quando a busca confirma que o ato existe mas não devolve a data exata** (comum com RDC muito
recente, onde só a notícia circula e a página do Diário Oficial ainda não indexou): cite o
número tal como as fontes o deram e escreva **"(data de publicação não localizada — a
confirmar)"** no lugar da data. Isso é diferente de "a confirmar na fonte primária" — aqui o
que falta não é abrir a fonte, é a própria data não ter aparecido em nenhum resultado. Não
arredonde para o mês nem invente o dia só para preencher o formato "nº X, de DD/MM/AAAA".

### 6. Separe registro de incorporação

Erro clássico do assunto e pegadinha recorrente da banca brasileira. Três estados diferentes,
que a nota precisa distinguir com todas as letras:

- **Registro na ANVISA** — o produto pode ser comercializado no país;
- **Incorporação ao SUS** (Conitec + portaria SECTICS/SCTIE) — o SUS fornece, e sob quais
  critérios;
- **Constar em PCDT / protocolo** — como e para quem o SUS fornece.

Um fármaco pode ter registro e não estar no SUS (é o caso de todos os agonistas de GLP-1), ou
ter sido recusado pela Conitec com relatório e portaria de não incorporação — que também são
fonte citável.

## Formato da nota

Siga o que o repositório já usa, para o arquivo continuar homogêneo:

```markdown
> **Nota de atualização — DD/MM/AAAA.** <o que mudou, em uma frase>. <detalhe: número do ato,
> data, critério, valor novo × valor antigo>. Quando o trecho do livro ficou incorreto,
> comece com "Trecho alterado. O original dizia: …".
> **Fontes:** <órgão, ato, data> <URL>
```

Coloque a nota **imediatamente após o parágrafo ou quadro a que ela se refere** — é o que
permite estudar o trecho já sabendo o que mudou. Nota solta no fim do arquivo não é lida.

Se o tópico tiver seção de panorama ("Atualizações desde a …"), acrescente lá o resumo e
mantenha a lista de fontes daquela seção em dia. Se não tiver e as mudanças forem muitas, crie
a seção seguindo o modelo do 6.07.

## Quando não houver novidade

Diga isso explicitamente e **registre a data do levantamento** no arquivo ("Levantamento
fechado em <mês/ano>"). Um tópico conferido e sem mudanças é informação valiosa: evita a
próxima varredura e dá segurança para estudar o texto como está. Não invente atualização para
justificar a rodada.

## Ao terminar

1. Rode a auditoria estrutural das notas:
   ```bash
   python3 .claude/skills/atualizar-teoria/scripts/auditar_notas.py "<caminho do arquivo de teoria>"
   ```
   Ela não acessa a rede: confere se toda nota tem linha de fonte, se todo ato citado tem
   número e data, quais notas ficaram sem URL e quais marcações "a confirmar" seguem pendentes.
2. Rode `python3 .claude/skills/gerar-vf/scripts/checar_links.py` (varre o repo) se você tiver
   mexido em links internos.
3. Atualize o contador de notas do arquivo, se ele existir ("São N notas ao longo do capítulo").
4. Relate ao usuário: o que mudou, o que ficou "a confirmar" e **com quais URLs**, e o que você
   procurou e não encontrou mudança — essa última parte é o que dá confiança no resultado.
5. Se o tópico já tiver arquivo em `testes/`, avise que as notas novas podem render itens e
   ofereça rodar a skill `gerar-vf` sobre elas. Não gere itens por conta própria: são tarefas
   separadas, e o usuário pode querer revisar as notas antes.
