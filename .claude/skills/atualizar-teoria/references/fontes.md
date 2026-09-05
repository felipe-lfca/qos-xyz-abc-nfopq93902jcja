# Fontes primárias por tipo de pergunta

Cada linha diz **quem decide** aquele assunto. Restrinja a busca ao domínio da fonte que decide;
notícia e portal comercial servem no máximo para localizar o ato, nunca como prova.

## Regulação de medicamentos e produtos para saúde (Brasil)

| Pergunta | Quem decide | Domínio para `allowed_domains` |
| :--- | :--- | :--- |
| Um produto tem registro no Brasil? Qual a bula vigente? | ANVISA — consultas de produto e bulário | `gov.br`, `consultas.anvisa.gov.br` |
| Norma sanitária (RDC, IN, RE) | ANVISA | `gov.br`, `bvsms.saude.gov.br` |
| Alerta, suspensão, recolhimento, cancelamento de registro | ANVISA (Nuvig/Gfarm) | `gov.br` |
| Texto oficial de portaria, RDC, lei | Diário Oficial / Saúde Legis | `in.gov.br`, `bvsms.saude.gov.br`, `planalto.gov.br` |

## O que o SUS oferece

| Pergunta | Quem decide | Domínio |
| :--- | :--- | :--- |
| Foi incorporado ao SUS? Com quais critérios? | Conitec (relatório de recomendação) + portaria SECTICS/SCTIE | `gov.br` |
| Como o SUS trata a doença? | PCDT — Protocolo Clínico e Diretrizes Terapêuticas | `gov.br` |
| Foi **negado**? | Relatório Conitec + portaria de não incorporação | `gov.br` |
| Está em consulta pública? | Conitec | `gov.br` |
| Componente (básico, estratégico, especializado/CEAF) | RENAME e portarias de financiamento | `gov.br` |

Ao citar incorporação, registre **os três dados**: número do relatório Conitec, número e data da
portaria, e os critérios de elegibilidade. É deles que a banca tira a pegadinha.

## Exercício profissional farmacêutico

| Pergunta | Quem decide | Domínio |
| :--- | :--- | :--- |
| Atribuição clínica, prescrição farmacêutica, serviços | CFF (resoluções) | `cff.org.br` |
| Ética profissional | CFF — Código de Ética | `cff.org.br` |
| Regras estaduais | CRF do estado | domínio do CRF |

## Prática clínica e diretrizes

| Assunto | Fonte | Domínio |
| :--- | :--- | :--- |
| Diabetes | SBD (diretriz brasileira) e ADA (*Standards of Care*, anual) | `diabetes.org.br`, `diabetesjournals.org`, `doi.org` |
| Cardiologia | SBC (diretrizes) | `abccardiol.org`, `portal.cardiol.br` |
| Infecção e antimicrobianos | ANVISA (IRAS), MS, IDSA | `gov.br`, `idsociety.org` |
| Oncologia | INCA, SBOC | `gov.br`, `sboc.org.br` |
| Segurança do paciente | ANVISA/Proqualis/ISMP Brasil | `gov.br`, `proqualis.fiocruz.br`, `ismp-brasil.org` |
| Ensaios e revisões | PubMed, DOI | `pubmed.ncbi.nlm.nih.gov`, `doi.org`, `nejm.org`, `thelancet.com` |

## Regulação estrangeira

Serve para **antecipar** o que vem, e para explicar por que um fármaco existe lá e não aqui.
Nunca apresente decisão estrangeira como se valesse no Brasil.

| Fonte | Domínio | Para quê |
| :--- | :--- | :--- |
| FDA | `fda.gov`, `accessdata.fda.gov` | aprovações, tarja preta, mudança de bula |
| EMA | `ema.europa.eu` | aprovações e suspensões na União Europeia |

## Consultas que funcionam

Formule a busca com o **nome do ato ou do fármaco + o órgão**, não com a pergunta clínica:

- bom: `PCDT diabete melito tipo 2 portaria SCTIE incorporação dapagliflozina`
- bom: `relatório Conitec não incorporação empagliflozina diabetes`
- bom: `RDC ANVISA farmácia hospitalar dose unitária`
- ruim: `novidades no tratamento do diabetes` (devolve notícia)
- ruim: `qual o melhor antidiabético` (devolve conteúdo comercial)

Para saber se algo mudou **desde** determinada data, inclua o ano na consulta e confira a data
de cada resultado — busca costuma devolver a versão antiga de um protocolo junto com a nova.

## Armadilhas conhecidas neste assunto

- **Registro ≠ incorporação ≠ PCDT.** Ver a seção correspondente na SKILL.md.
- **Protocolo revogado.** Um PCDT novo revoga o anterior; cite a portaria vigente e, quando
  útil para o estudo, diga qual ela revogou.
- **Bula do FDA × bula brasileira.** Indicação aprovada lá pode não existir aqui.
- **Diretriz de sociedade não é norma.** ADA e SBD orientam a prática; quem define o que o SUS
  paga é a portaria. Um item de prova pode cobrar qualquer um dos dois — deixe claro na nota
  de qual você está falando.
- **Nome comercial × princípio ativo.** Registre os dois na primeira menção; a banca alterna.
