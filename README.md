# qos-pmmg-farmacia

Tópicos de estudo para o concurso de Farmacêutico do Quadro de Oficiais da Saúde da PMMG (QOS/PMMG). A prova objetiva cobra **Língua Portuguesa**, Direitos Humanos e conhecimentos específicos de Farmácia; este repositório cobre Farmácia (7 eixos), Português e Direitos Humanos.

## Como o repositório está organizado

Uma pasta por **eixo** do conteúdo programático de Farmácia (7 eixos, 67 tópicos) e pastas próprias para **Língua Portuguesa e Interpretação de Textos** (30 tópicos do edital) e para as **matérias extras** (Direitos Humanos). Dentro de cada uma, um arquivo `.md` por **tópico do edital**. Nos eixos de Farmácia, cada arquivo já vem com os números da planilha de análise estatística (em quais editais o tópico foi exigido, em quantos editais, quantas questões gerou e a classificação de incidência). Em Português a incidência foi mapeada a partir do banco de questões das provas de Farmácia (2013, 2017, 2023 e 2024). Nas matérias extras, o corpo dos arquivos é a letra da lei — transcrição verbatim da fonte citada.

```
<pasta>/
├── README.md      índice, com a tabela de incidência
├── <tópico>.md    um arquivo por tópico do edital
├── recursos/      imagens e anexos citados pelos arquivos
└── testes/        afirmativas V/F de cada tópico, com o mesmo nome do arquivo de teoria
```

Os arquivos em `testes/` servem ao estudo por recuperação ativa: você responde blocos de cinco
afirmativas, abre o gabarito recolhido e, para cada erro, segue o link direto para o trecho da
teoria que o explica. São gerados pela skill `gerar-vf` (em `.claude/skills/`) a partir do
arquivo de teoria correspondente — nunca a partir do banco de questões, que serve só de
referência de formato.

Para citar uma imagem dentro de um arquivo de tópico: `![Descrição](recursos/arquivo.png)`.

## Eixos de Farmácia

| Eixo | Tópicos | Questões nas provas | Pasta |
| :---- | :---- | :---- | :---- |
| 1. Legislação e Política Farmacêutica | 9 | 17 | [abrir](1.%20Legisla%C3%A7%C3%A3o%20e%20Pol%C3%ADtica%20Farmac%C3%AAutica/README.md) |
| 2. Farmacotécnica e Manipulação Hospitalar | 8 | 19 | [abrir](2.%20Farmacot%C3%A9cnica%20e%20Manipula%C3%A7%C3%A3o%20Hospitalar/README.md) |
| 3. Gestão e Logística da Farmácia Hospitalar | 14 | 26 | [abrir](3.%20Gest%C3%A3o%20e%20Log%C3%ADstica%20da%20Farm%C3%A1cia%20Hospitalar/README.md) |
| 4. Segurança do Paciente e Controle de Infecção | 6 | 13 | [abrir](4.%20Seguran%C3%A7a%20do%20Paciente%20e%20Controle%20de%20Infec%C3%A7%C3%A3o/README.md) |
| 5. Farmacologia Básica | 4 | 4 | [abrir](5.%20Farmacologia%20B%C3%A1sica/README.md) |
| 6. Farmacoterapia Clínica | 18 | 38 | [abrir](6.%20Farmacoterapia%20Cl%C3%ADnica/README.md) |
| 7. Farmácia Clínica e Cuidado Farmacêutico | 8 | 7 | [abrir](7.%20Farm%C3%A1cia%20Cl%C3%ADnica%20e%20Cuidado%20Farmac%C3%AAutico/README.md) |
| **Total (Farmácia)** | **67** | **124** | |

## Língua Portuguesa e Interpretação de Textos

Matéria da prova objetiva (9 questões em 2013/2017; 10 em 2023/2024), no mesmo formato de arquivo dos eixos de Farmácia. O edital da PMMG numera estes tópicos como 1.1 a 1.30; aqui eles viram **LP.01 a LP.30** para não colidir com o Eixo 1 de legislação. Dois itens do edital são repetição (1.17 = 1.15; 1.23 = 1.18); o LP.30 sintetiza regência, concordância e colocação.

A incidência foi mapeada nas provas de Farmácia de 2013, 2017, 2023 e 2024 (38 questões de Português, inclusive a #Q2023-06 anulada). As provas de 2022 (Psiquiatria) e 2026 (Psicologia) entram só como aproveitamento, listadas em «Questões relacionadas» de cada tópico. Além do recorte das provas, cada tópico canônico tem a seção **Cobertura extra — casos ainda não cobrados**, para extinguir o edital se a banca inovar.

| Matéria | Tópicos | Questões nas provas | Pasta |
| :---- | :---- | :---- | :---- |
| LP. Língua Portuguesa e Interpretação de Textos | 30 | 38 | [abrir](LP.%20L%C3%ADngua%20Portuguesa%20e%20Interpreta%C3%A7%C3%A3o%20de%20Textos/README.md) |

## Matérias extras

| Matéria | Tópicos | Pasta |
| :---- | :---- | :---- |
| Direitos Humanos | 2 | [abrir](Direitos%20Humanos/README.md) |

## Índice completo dos tópicos

### Eixo 1 — Legislação e Política Farmacêutica

| # | Tópico do edital | Exigido em | Editais | Questões | Incidência |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 1.01 | [Código de ética da profissão farmacêutica](1.%20Legisla%C3%A7%C3%A3o%20e%20Pol%C3%ADtica%20Farmac%C3%AAutica/1.01%20C%C3%B3digo%20de%20%C3%A9tica%20da%20profiss%C3%A3o%20farmac%C3%AAutica.md) | 2013, 2017, 2023 | 3 de 4 | 1 | Baixa incidência |
| 1.02 | [Política nacional de medicamentos e de assistência farmacêutica](1.%20Legisla%C3%A7%C3%A3o%20e%20Pol%C3%ADtica%20Farmac%C3%AAutica/1.02%20Pol%C3%ADtica%20nacional%20de%20medicamentos%20e%20de%20assist%C3%AAncia%20farmac%C3%AAutica.md) | 2013, 2017, 2023 | 3 de 4 | 1 | Baixa incidência |
| 1.03 | [Medicamentos genéricos, similares e de referência](1.%20Legisla%C3%A7%C3%A3o%20e%20Pol%C3%ADtica%20Farmac%C3%AAutica/1.03%20Medicamentos%20gen%C3%A9ricos%2C%20similares%20e%20de%20refer%C3%AAncia.md) | 2013, 2017, 2023 | 3 de 4 | 2 | Média incidência |
| 1.04 | [Medicamentos sujeitos a controle especial](1.%20Legisla%C3%A7%C3%A3o%20e%20Pol%C3%ADtica%20Farmac%C3%AAutica/1.04%20Medicamentos%20sujeitos%20a%20controle%20especial.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 4 | Alta incidência |
| 1.05 | [Vigilância sanitária de medicamentos, correlatos, saneantes e produtos de saúde](1.%20Legisla%C3%A7%C3%A3o%20e%20Pol%C3%ADtica%20Farmac%C3%AAutica/1.05%20Vigil%C3%A2ncia%20sanit%C3%A1ria%20de%20medicamentos%2C%20correlatos%2C%20saneantes%20e%20produtos%20de%20sa%C3%BAde.md) | 2023 | 1 de 4 | 3 | Média incidência |
| 1.06 | [Boas práticas de funcionamento de serviços de saúde e farmacêuticos](1.%20Legisla%C3%A7%C3%A3o%20e%20Pol%C3%ADtica%20Farmac%C3%AAutica/1.06%20Boas%20pr%C3%A1ticas%20de%20funcionamento%20de%20servi%C3%A7os%20de%20sa%C3%BAde%20e%20farmac%C3%AAuticos.md) | 2023 | 1 de 4 | 1 | Baixa incidência |
| 1.07 | [Atribuições do farmacêutico na gestão de produtos para a saúde](1.%20Legisla%C3%A7%C3%A3o%20e%20Pol%C3%ADtica%20Farmac%C3%AAutica/1.07%20Atribui%C3%A7%C3%B5es%20do%20farmac%C3%AAutico%20na%20gest%C3%A3o%20de%20produtos%20para%20a%20sa%C3%BAde.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 3 | Média incidência |
| 1.08 | [Registro, rotulagem e reprocessamento de produtos médicos](1.%20Legisla%C3%A7%C3%A3o%20e%20Pol%C3%ADtica%20Farmac%C3%AAutica/1.08%20Registro%2C%20rotulagem%20e%20reprocessamento%20de%20produtos%20m%C3%A9dicos.md) | 2013, 2017 | 2 de 4 | 2 | Média incidência |
| 1.09 | [Reprocessamento e reesterilização de materiais médico-hospitalares](1.%20Legisla%C3%A7%C3%A3o%20e%20Pol%C3%ADtica%20Farmac%C3%AAutica/1.09%20Reprocessamento%20e%20reesteriliza%C3%A7%C3%A3o%20de%20materiais%20m%C3%A9dico-hospitalares.md) | 2013, 2017 | 2 de 4 | 0 | Nunca caiu |

### Eixo 2 — Farmacotécnica e Manipulação Hospitalar

| # | Tópico do edital | Exigido em | Editais | Questões | Incidência |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 2.01 | [Formas farmacêuticas (sólidas, líquidas, semissólidas, injetáveis) e vias de administração](2.%20Farmacot%C3%A9cnica%20e%20Manipula%C3%A7%C3%A3o%20Hospitalar/2.01%20Formas%20farmac%C3%AAuticas%20%28s%C3%B3lidas%2C%20l%C3%ADquidas%2C%20semiss%C3%B3lidas%2C%20injet%C3%A1veis%29%20e%20vias%20de%20administra%C3%A7%C3%A3o.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 3 | Média incidência |
| 2.02 | [Boas práticas de manipulação de magistrais, oficinais e produtos estéreis e não estéreis](2.%20Farmacot%C3%A9cnica%20e%20Manipula%C3%A7%C3%A3o%20Hospitalar/2.02%20Boas%20pr%C3%A1ticas%20de%20manipula%C3%A7%C3%A3o%20de%20magistrais%2C%20oficinais%20e%20produtos%20est%C3%A9reis%20e%20n%C3%A3o%20est%C3%A9reis.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 2 | Média incidência |
| 2.03 | [Preparação de dose unitária e unitarização de doses](2.%20Farmacot%C3%A9cnica%20e%20Manipula%C3%A7%C3%A3o%20Hospitalar/2.03%20Prepara%C3%A7%C3%A3o%20de%20dose%20unit%C3%A1ria%20e%20unitariza%C3%A7%C3%A3o%20de%20doses.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 3 | Média incidência |
| 2.04 | [Preparação e dispensação de terapia antineoplásica](2.%20Farmacot%C3%A9cnica%20e%20Manipula%C3%A7%C3%A3o%20Hospitalar/2.04%20Prepara%C3%A7%C3%A3o%20e%20dispensa%C3%A7%C3%A3o%20de%20terapia%20antineopl%C3%A1sica.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 4 | Alta incidência |
| 2.05 | [Controle de qualidade e estabilidade de insumos e medicamentos](2.%20Farmacot%C3%A9cnica%20e%20Manipula%C3%A7%C3%A3o%20Hospitalar/2.05%20Controle%20de%20qualidade%20e%20estabilidade%20de%20insumos%20e%20medicamentos.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 2 | Média incidência |
| 2.06 | [Cálculos aplicados à farmácia hospitalar](2.%20Farmacot%C3%A9cnica%20e%20Manipula%C3%A7%C3%A3o%20Hospitalar/2.06%20C%C3%A1lculos%20aplicados%20%C3%A0%20farm%C3%A1cia%20hospitalar.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 5 | Alta incidência |
| 2.07 | [Controle de qualidade de matérias-primas; emissão e análise de laudos](2.%20Farmacot%C3%A9cnica%20e%20Manipula%C3%A7%C3%A3o%20Hospitalar/2.07%20Controle%20de%20qualidade%20de%20mat%C3%A9rias-primas%3B%20emiss%C3%A3o%20e%20an%C3%A1lise%20de%20laudos.md) | 2013, 2017 | 2 de 4 | 0 | Nunca caiu |
| 2.08 | [Adequação de dosagens e formulações extemporâneas para pacientes hospitalizados](2.%20Farmacot%C3%A9cnica%20e%20Manipula%C3%A7%C3%A3o%20Hospitalar/2.08%20Adequa%C3%A7%C3%A3o%20de%20dosagens%20e%20formula%C3%A7%C3%B5es%20extempor%C3%A2neas%20para%20pacientes%20hospitalizados.md) | 2013, 2017 | 2 de 4 | 0 | Nunca caiu |

### Eixo 3 — Gestão e Logística da Farmácia Hospitalar

| # | Tópico do edital | Exigido em | Editais | Questões | Incidência |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 3.01 | [Organização hospitalar, estrutura da farmácia e farmácias satélites](3.%20Gest%C3%A3o%20e%20Log%C3%ADstica%20da%20Farm%C3%A1cia%20Hospitalar/3.01%20Organiza%C3%A7%C3%A3o%20hospitalar%2C%20estrutura%20da%20farm%C3%A1cia%20e%20farm%C3%A1cias%20sat%C3%A9lites.md) | 2017, 2023 | 2 de 4 | 1 | Baixa incidência |
| 3.02 | [Seleção e padronização de medicamentos](3.%20Gest%C3%A3o%20e%20Log%C3%ADstica%20da%20Farm%C3%A1cia%20Hospitalar/3.02%20Sele%C3%A7%C3%A3o%20e%20padroniza%C3%A7%C3%A3o%20de%20medicamentos.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 2 | Média incidência |
| 3.03 | [Programação e aquisição de medicamentos e produtos para saúde](3.%20Gest%C3%A3o%20e%20Log%C3%ADstica%20da%20Farm%C3%A1cia%20Hospitalar/3.03%20Programa%C3%A7%C3%A3o%20e%20aquisi%C3%A7%C3%A3o%20de%20medicamentos%20e%20produtos%20para%20sa%C3%BAde.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 3 | Média incidência |
| 3.04 | [Armazenamento, dimensionamento e gestão de estoques](3.%20Gest%C3%A3o%20e%20Log%C3%ADstica%20da%20Farm%C3%A1cia%20Hospitalar/3.04%20Armazenamento%2C%20dimensionamento%20e%20gest%C3%A3o%20de%20estoques.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 3 | Média incidência |
| 3.05 | [Sistemas de distribuição e boas práticas de dispensação](3.%20Gest%C3%A3o%20e%20Log%C3%ADstica%20da%20Farm%C3%A1cia%20Hospitalar/3.05%20Sistemas%20de%20distribui%C3%A7%C3%A3o%20e%20boas%20pr%C3%A1ticas%20de%20dispensa%C3%A7%C3%A3o.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 5 | Alta incidência |
| 3.06 | [Noções de licitações e contratos administrativos](3.%20Gest%C3%A3o%20e%20Log%C3%ADstica%20da%20Farm%C3%A1cia%20Hospitalar/3.06%20No%C3%A7%C3%B5es%20de%20licita%C3%A7%C3%B5es%20e%20contratos%20administrativos.md) | 2013, 2023, 2024 | 3 de 4 | 3 | Média incidência |
| 3.07 | [Gestão de qualidade em farmácia hospitalar e acreditação](3.%20Gest%C3%A3o%20e%20Log%C3%ADstica%20da%20Farm%C3%A1cia%20Hospitalar/3.07%20Gest%C3%A3o%20de%20qualidade%20em%20farm%C3%A1cia%20hospitalar%20e%20acredita%C3%A7%C3%A3o.md) | 2023, 2024 | 2 de 4 | 2 | Média incidência |
| 3.08 | [Avaliação de tecnologias em saúde e farmacoeconomia](3.%20Gest%C3%A3o%20e%20Log%C3%ADstica%20da%20Farm%C3%A1cia%20Hospitalar/3.08%20Avalia%C3%A7%C3%A3o%20de%20tecnologias%20em%20sa%C3%BAde%20e%20farmacoeconomia.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 3 | Média incidência |
| 3.09 | [Rastreabilidade de medicamentos e produtos para saúde](3.%20Gest%C3%A3o%20e%20Log%C3%ADstica%20da%20Farm%C3%A1cia%20Hospitalar/3.09%20Rastreabilidade%20de%20medicamentos%20e%20produtos%20para%20sa%C3%BAde.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 1 | Baixa incidência |
| 3.10 | [Gerenciamento dos resíduos de serviços de saúde (RSS)](3.%20Gest%C3%A3o%20e%20Log%C3%ADstica%20da%20Farm%C3%A1cia%20Hospitalar/3.10%20Gerenciamento%20dos%20res%C3%ADduos%20de%20servi%C3%A7os%20de%20sa%C3%BAde%20%28RSS%29.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 3 | Média incidência |
| 3.11 | [Noções sobre gestão orçamentária e financeira](3.%20Gest%C3%A3o%20e%20Log%C3%ADstica%20da%20Farm%C3%A1cia%20Hospitalar/3.11%20No%C3%A7%C3%B5es%20sobre%20gest%C3%A3o%20or%C3%A7ament%C3%A1ria%20e%20financeira.md) | 2023, 2024 | 2 de 4 | 0 | Nunca caiu |
| 3.12 | [Gestão de recursos humanos](3.%20Gest%C3%A3o%20e%20Log%C3%ADstica%20da%20Farm%C3%A1cia%20Hospitalar/3.12%20Gest%C3%A3o%20de%20recursos%20humanos.md) | 2023 | 1 de 4 | 0 | Nunca caiu |
| 3.13 | [Participação do farmacêutico em comissões hospitalares](3.%20Gest%C3%A3o%20e%20Log%C3%ADstica%20da%20Farm%C3%A1cia%20Hospitalar/3.13%20Participa%C3%A7%C3%A3o%20do%20farmac%C3%AAutico%20em%20comiss%C3%B5es%20hospitalares.md) | 2023, 2024 | 2 de 4 | 0 | Nunca caiu |
| 3.14 | [Cadeia de suprimentos: seleção de fornecedores e redes de distribuição](3.%20Gest%C3%A3o%20e%20Log%C3%ADstica%20da%20Farm%C3%A1cia%20Hospitalar/3.14%20Cadeia%20de%20suprimentos%20-%20sele%C3%A7%C3%A3o%20de%20fornecedores%20e%20redes%20de%20distribui%C3%A7%C3%A3o.md) | 2023, 2024 | 2 de 4 | 0 | Nunca caiu |

### Eixo 4 — Segurança do Paciente e Controle de Infecção

| # | Tópico do edital | Exigido em | Editais | Questões | Incidência |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 4.01 | [Segurança do paciente, erros de medicação e protocolos básicos](4.%20Seguran%C3%A7a%20do%20Paciente%20e%20Controle%20de%20Infec%C3%A7%C3%A3o/4.01%20Seguran%C3%A7a%20do%20paciente%2C%20erros%20de%20medica%C3%A7%C3%A3o%20e%20protocolos%20b%C3%A1sicos.md) | 2023, 2024 | 2 de 4 | 6 | Alta incidência |
| 4.02 | [Farmacovigilância](4.%20Seguran%C3%A7a%20do%20Paciente%20e%20Controle%20de%20Infec%C3%A7%C3%A3o/4.02%20Farmacovigil%C3%A2ncia.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 2 | Média incidência |
| 4.03 | [Tecnovigilância](4.%20Seguran%C3%A7a%20do%20Paciente%20e%20Controle%20de%20Infec%C3%A7%C3%A3o/4.03%20Tecnovigil%C3%A2ncia.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 0 | Nunca caiu |
| 4.04 | [Controle das infecções hospitalares e IRAS](4.%20Seguran%C3%A7a%20do%20Paciente%20e%20Controle%20de%20Infec%C3%A7%C3%A3o/4.04%20Controle%20das%20infec%C3%A7%C3%B5es%20hospitalares%20e%20IRAS.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 4 | Alta incidência |
| 4.05 | [Antibioticoterapia, antibioticoprofilaxia e uso correto de antimicrobianos](4.%20Seguran%C3%A7a%20do%20Paciente%20e%20Controle%20de%20Infec%C3%A7%C3%A3o/4.05%20Antibioticoterapia%2C%20antibioticoprofilaxia%20e%20uso%20correto%20de%20antimicrobianos.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 1 | Baixa incidência |
| 4.06 | [Precauções, isolamento e prevenção de infecções relacionadas à assistência](4.%20Seguran%C3%A7a%20do%20Paciente%20e%20Controle%20de%20Infec%C3%A7%C3%A3o/4.06%20Precau%C3%A7%C3%B5es%2C%20isolamento%20e%20preven%C3%A7%C3%A3o%20de%20infec%C3%A7%C3%B5es%20relacionadas%20%C3%A0%20assist%C3%AAncia.md) | 2023, 2024 | 2 de 4 | 0 | Nunca caiu |

### Eixo 5 — Farmacologia Básica

| # | Tópico do edital | Exigido em | Editais | Questões | Incidência |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 5.01 | [Conceitos em farmacocinética, biodisponibilidade e bioequivalência](5.%20Farmacologia%20B%C3%A1sica/5.01%20Conceitos%20em%20farmacocin%C3%A9tica%2C%20biodisponibilidade%20e%20bioequival%C3%AAncia.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 3 | Média incidência |
| 5.02 | [Mecanismos gerais de ação e efeitos de fármacos](5.%20Farmacologia%20B%C3%A1sica/5.02%20Mecanismos%20gerais%20de%20a%C3%A7%C3%A3o%20e%20efeitos%20de%20f%C3%A1rmacos.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 0 | Nunca caiu |
| 5.03 | [Reações adversas a medicamentos](5.%20Farmacologia%20B%C3%A1sica/5.03%20Rea%C3%A7%C3%B5es%20adversas%20a%20medicamentos.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 1 | Baixa incidência |
| 5.04 | [Fatores que afetam a resposta farmacológica](5.%20Farmacologia%20B%C3%A1sica/5.04%20Fatores%20que%20afetam%20a%20resposta%20farmacol%C3%B3gica.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 0 | Nunca caiu |

### Eixo 6 — Farmacoterapia Clínica

| # | Tópico do edital | Exigido em | Editais | Questões | Incidência |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 6.01 | [Farmacoterapia das doenças infecciosas / quimioterapia das doenças microbianas](6.%20Farmacoterapia%20Cl%C3%ADnica/6.01%20Farmacoterapia%20das%20doen%C3%A7as%20infecciosas%20-%20quimioterapia%20das%20doen%C3%A7as%20microbianas.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 9 | Alta incidência |
| 6.02 | [Farmacoterapia cardiovascular (funções renal e cardiovascular)](6.%20Farmacoterapia%20Cl%C3%ADnica/6.02%20Farmacoterapia%20cardiovascular%20%28fun%C3%A7%C3%B5es%20renal%20e%20cardiovascular%29.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 6 | Alta incidência |
| 6.03 | [Farmacoterapia em distúrbios neurológicos e transtornos psiquiátricos (SNC)](6.%20Farmacoterapia%20Cl%C3%ADnica/6.03%20Farmacoterapia%20em%20dist%C3%BArbios%20neurol%C3%B3gicos%20e%20transtornos%20psiqui%C3%A1tricos%20%28SNC%29.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 4 | Alta incidência |
| 6.04 | [Quimioterapia das doenças neoplásicas / distúrbios oncológicos](6.%20Farmacoterapia%20Cl%C3%ADnica/6.04%20Quimioterapia%20das%20doen%C3%A7as%20neopl%C3%A1sicas%20-%20dist%C3%BArbios%20oncol%C3%B3gicos.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 5 | Alta incidência |
| 6.05 | [Sangue e órgãos hematopoiéticos / distúrbios hematológicos](6.%20Farmacoterapia%20Cl%C3%ADnica/6.05%20Sangue%20e%20%C3%B3rg%C3%A3os%20hematopoi%C3%A9ticos%20-%20dist%C3%BArbios%20hematol%C3%B3gicos.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 5 | Alta incidência |
| 6.06 | [Terapia farmacológica da inflamação e da dor](6.%20Farmacoterapia%20Cl%C3%ADnica/6.06%20Terapia%20farmacol%C3%B3gica%20da%20inflama%C3%A7%C3%A3o%20e%20da%20dor.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 3 | Média incidência |
| 6.07 | [Hormônios e seus antagonistas / distúrbios endocrinológicos](6.%20Farmacoterapia%20Cl%C3%ADnica/6.07%20Horm%C3%B4nios%20e%20seus%20antagonistas%20-%20dist%C3%BArbios%20endocrinol%C3%B3gicos.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 3 | Média incidência |
| 6.08 | [Função gastrintestinal / distúrbios gastrointestinais](6.%20Farmacoterapia%20Cl%C3%ADnica/6.08%20Fun%C3%A7%C3%A3o%20gastrintestinal%20-%20dist%C3%BArbios%20gastrointestinais.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 1 | Baixa incidência |
| 6.09 | [Distúrbios respiratórios](6.%20Farmacoterapia%20Cl%C3%ADnica/6.09%20Dist%C3%BArbios%20respirat%C3%B3rios.md) | 2023, 2024 | 2 de 4 | 1 | Baixa incidência |
| 6.10 | [Farmacoterapia em terapia intensiva (sedação e analgesia)](6.%20Farmacoterapia%20Cl%C3%ADnica/6.10%20Farmacoterapia%20em%20terapia%20intensiva%20%28seda%C3%A7%C3%A3o%20e%20analgesia%29.md) | 2017 | 1 de 4 | 1 | Baixa incidência |
| 6.11 | [Distúrbios articulares e ósseos](6.%20Farmacoterapia%20Cl%C3%ADnica/6.11%20Dist%C3%BArbios%20articulares%20e%20%C3%B3sseos.md) | 2023, 2024 | 2 de 4 | 0 | Nunca caiu |
| 6.12 | [Distúrbios renais](6.%20Farmacoterapia%20Cl%C3%ADnica/6.12%20Dist%C3%BArbios%20renais.md) | 2013, 2023, 2024 | 3 de 4 | 0 | Nunca caiu |
| 6.13 | [Distúrbios urológicos](6.%20Farmacoterapia%20Cl%C3%ADnica/6.13%20Dist%C3%BArbios%20urol%C3%B3gicos.md) | 2023, 2024 | 2 de 4 | 0 | Nunca caiu |
| 6.14 | [Distúrbios nutricionais e terapia nutricional](6.%20Farmacoterapia%20Cl%C3%ADnica/6.14%20Dist%C3%BArbios%20nutricionais%20e%20terapia%20nutricional.md) | 2023, 2024 | 2 de 4 | 0 | Nunca caiu |
| 6.15 | [Dermatologia / distúrbios dermatológicos](6.%20Farmacoterapia%20Cl%C3%ADnica/6.15%20Dermatologia%20-%20dist%C3%BArbios%20dermatol%C3%B3gicos.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 0 | Nunca caiu |
| 6.16 | [Oftalmologia / distúrbios oftalmológicos](6.%20Farmacoterapia%20Cl%C3%ADnica/6.16%20Oftalmologia%20-%20dist%C3%BArbios%20oftalmol%C3%B3gicos.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 0 | Nunca caiu |
| 6.17 | [Quimioterapia das infecções parasitárias](6.%20Farmacoterapia%20Cl%C3%ADnica/6.17%20Quimioterapia%20das%20infec%C3%A7%C3%B5es%20parasit%C3%A1rias.md) | 2013, 2017 | 2 de 4 | 0 | Nunca caiu |
| 6.18 | [Imunomoduladores](6.%20Farmacoterapia%20Cl%C3%ADnica/6.18%20Imunomoduladores.md) | 2013, 2017 | 2 de 4 | 0 | Nunca caiu |

### Eixo 7 — Farmácia Clínica e Cuidado Farmacêutico

| # | Tópico do edital | Exigido em | Editais | Questões | Incidência |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 7.01 | [Processo de cuidado do paciente, raciocínio clínico e decisão em farmacoterapia](7.%20Farm%C3%A1cia%20Cl%C3%ADnica%20e%20Cuidado%20Farmac%C3%AAutico/7.01%20Processo%20de%20cuidado%20do%20paciente%2C%20racioc%C3%ADnio%20cl%C3%ADnico%20e%20decis%C3%A3o%20em%20farmacoterapia.md) | 2023, 2024 | 2 de 4 | 2 | Média incidência |
| 7.02 | [Problemas relacionados ao uso de medicamentos (PRM)](7.%20Farm%C3%A1cia%20Cl%C3%ADnica%20e%20Cuidado%20Farmac%C3%AAutico/7.02%20Problemas%20relacionados%20ao%20uso%20de%20medicamentos%20%28PRM%29.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 1 | Baixa incidência |
| 7.03 | [Uso racional de medicamentos](7.%20Farm%C3%A1cia%20Cl%C3%ADnica%20e%20Cuidado%20Farmac%C3%AAutico/7.03%20Uso%20racional%20de%20medicamentos.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 1 | Baixa incidência |
| 7.04 | [Atribuições clínicas do farmacêutico e serviços clínicos](7.%20Farm%C3%A1cia%20Cl%C3%ADnica%20e%20Cuidado%20Farmac%C3%AAutico/7.04%20Atribui%C3%A7%C3%B5es%20cl%C3%ADnicas%20do%20farmac%C3%AAutico%20e%20servi%C3%A7os%20cl%C3%ADnicos.md) | 2023, 2024 | 2 de 4 | 1 | Baixa incidência |
| 7.05 | [Avaliação da prescrição e atuação em equipe multiprofissional](7.%20Farm%C3%A1cia%20Cl%C3%ADnica%20e%20Cuidado%20Farmac%C3%AAutico/7.05%20Avalia%C3%A7%C3%A3o%20da%20prescri%C3%A7%C3%A3o%20e%20atua%C3%A7%C3%A3o%20em%20equipe%20multiprofissional.md) | 2023, 2024 | 2 de 4 | 1 | Baixa incidência |
| 7.06 | [Farmacoterapia no idoso e desprescrição](7.%20Farm%C3%A1cia%20Cl%C3%ADnica%20e%20Cuidado%20Farmac%C3%AAutico/7.06%20Farmacoterapia%20no%20idoso%20e%20desprescri%C3%A7%C3%A3o.md) | — (fora do edital) | 0 de 4 | 1 | Baixa incidência |
| 7.07 | [Gestão da prática clínica](7.%20Farm%C3%A1cia%20Cl%C3%ADnica%20e%20Cuidado%20Farmac%C3%AAutico/7.07%20Gest%C3%A3o%20da%20pr%C3%A1tica%20cl%C3%ADnica.md) | 2023, 2024 | 2 de 4 | 0 | Nunca caiu |
| 7.08 | [Cuidados farmacêuticos na atenção primária à saúde](7.%20Farm%C3%A1cia%20Cl%C3%ADnica%20e%20Cuidado%20Farmac%C3%AAutico/7.08%20Cuidados%20farmac%C3%AAuticos%20na%20aten%C3%A7%C3%A3o%20prim%C3%A1ria%20%C3%A0%20sa%C3%BAde.md) | 2013, 2017 | 2 de 4 | 0 | Nunca caiu |

### Língua Portuguesa e Interpretação de Textos

| # | Tópico do edital | Exigido em | Editais | Questões | Incidência |
| :---- | :---- | :---- | :---- | :---- | :---- |
| LP.01 | [Domínio da Expressão Escrita (redação)](LP.%20L%C3%ADngua%20Portuguesa%20e%20Interpreta%C3%A7%C3%A3o%20de%20Textos/LP.01%20Dom%C3%ADnio%20da%20Express%C3%A3o%20Escrita%20%28reda%C3%A7%C3%A3o%29.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 0 | Nunca caiu |
| LP.02 | [Adequação conceitual](LP.%20L%C3%ADngua%20Portuguesa%20e%20Interpreta%C3%A7%C3%A3o%20de%20Textos/LP.02%20Adequa%C3%A7%C3%A3o%20conceitual.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 0 | Nunca caiu |
| LP.03 | [Pertinência, relevância e articulação dos argumentos](LP.%20L%C3%ADngua%20Portuguesa%20e%20Interpreta%C3%A7%C3%A3o%20de%20Textos/LP.03%20Pertin%C3%AAncia%2C%20relev%C3%A2ncia%20e%20articula%C3%A7%C3%A3o%20dos%20argumentos.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 0 | Nunca caiu |
| LP.04 | [Seleção vocabular](LP.%20L%C3%ADngua%20Portuguesa%20e%20Interpreta%C3%A7%C3%A3o%20de%20Textos/LP.04%20Sele%C3%A7%C3%A3o%20vocabular.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 0 | Nunca caiu |
| LP.05 | [Estudo de texto (questões objetivas sobre textos)](LP.%20L%C3%ADngua%20Portuguesa%20e%20Interpreta%C3%A7%C3%A3o%20de%20Textos/LP.05%20Estudo%20de%20texto%20%28quest%C3%B5es%20objetivas%20sobre%20textos%29.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 12 | Alta incidência |
| LP.06 | [Tipologia textual e Gêneros textuais](LP.%20L%C3%ADngua%20Portuguesa%20e%20Interpreta%C3%A7%C3%A3o%20de%20Textos/LP.06%20Tipologia%20textual%20e%20G%C3%AAneros%20textuais.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 3 | Média incidência |
| LP.07 | [Ortografia oficial](LP.%20L%C3%ADngua%20Portuguesa%20e%20Interpreta%C3%A7%C3%A3o%20de%20Textos/LP.07%20Ortografia%20oficial.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 1 | Baixa incidência |
| LP.08 | [Acentuação gráfica](LP.%20L%C3%ADngua%20Portuguesa%20e%20Interpreta%C3%A7%C3%A3o%20de%20Textos/LP.08%20Acentua%C3%A7%C3%A3o%20gr%C3%A1fica.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 1 | Baixa incidência |
| LP.09 | [Emprego dos sinais de pontuação](LP.%20L%C3%ADngua%20Portuguesa%20e%20Interpreta%C3%A7%C3%A3o%20de%20Textos/LP.09%20Emprego%20dos%20sinais%20de%20pontua%C3%A7%C3%A3o.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 0 | Nunca caiu |
| LP.10 | [Estrutura e formação de palavras](LP.%20L%C3%ADngua%20Portuguesa%20e%20Interpreta%C3%A7%C3%A3o%20de%20Textos/LP.10%20Estrutura%20e%20forma%C3%A7%C3%A3o%20de%20palavras.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 3 | Média incidência |
| LP.11 | [Classes de palavras](LP.%20L%C3%ADngua%20Portuguesa%20e%20Interpreta%C3%A7%C3%A3o%20de%20Textos/LP.11%20Classes%20de%20palavras.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 0 | Nunca caiu |
| LP.12 | [Frase, oração e período](LP.%20L%C3%ADngua%20Portuguesa%20e%20Interpreta%C3%A7%C3%A3o%20de%20Textos/LP.12%20Frase%2C%20ora%C3%A7%C3%A3o%20e%20per%C3%ADodo.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 1 | Baixa incidência |
| LP.13 | [Termos da oração](LP.%20L%C3%ADngua%20Portuguesa%20e%20Interpreta%C3%A7%C3%A3o%20de%20Textos/LP.13%20Termos%20da%20ora%C3%A7%C3%A3o.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 0 | Nunca caiu |
| LP.14 | [Período composto por coordenação e subordinação](LP.%20L%C3%ADngua%20Portuguesa%20e%20Interpreta%C3%A7%C3%A3o%20de%20Textos/LP.14%20Per%C3%ADodo%20composto%20por%20coordena%C3%A7%C3%A3o%20e%20subordina%C3%A7%C3%A3o.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 2 | Média incidência |
| LP.15 | [Funções sintáticas dos pronomes relativos](LP.%20L%C3%ADngua%20Portuguesa%20e%20Interpreta%C3%A7%C3%A3o%20de%20Textos/LP.15%20Fun%C3%A7%C3%B5es%20sint%C3%A1ticas%20dos%20pronomes%20relativos.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 1 | Baixa incidência |
| LP.16 | [Emprego de nomes e pronomes](LP.%20L%C3%ADngua%20Portuguesa%20e%20Interpreta%C3%A7%C3%A3o%20de%20Textos/LP.16%20Emprego%20de%20nomes%20e%20pronomes.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 2 | Média incidência |
| LP.17 | [Funções sintáticas dos pronomes relativos](LP.%20L%C3%ADngua%20Portuguesa%20e%20Interpreta%C3%A7%C3%A3o%20de%20Textos/LP.17%20Fun%C3%A7%C3%B5es%20sint%C3%A1ticas%20dos%20pronomes%20relativos.md) *(= LP.15)* | 2013, 2017, 2023, 2024 | 4 de 4 | 0 | Nunca caiu |
| LP.18 | [Colocação pronominal](LP.%20L%C3%ADngua%20Portuguesa%20e%20Interpreta%C3%A7%C3%A3o%20de%20Textos/LP.18%20Coloca%C3%A7%C3%A3o%20pronominal.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 0 | Nunca caiu |
| LP.19 | [Emprego de tempos e modos verbais](LP.%20L%C3%ADngua%20Portuguesa%20e%20Interpreta%C3%A7%C3%A3o%20de%20Textos/LP.19%20Emprego%20de%20tempos%20e%20modos%20verbais.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 2 | Média incidência |
| LP.20 | [Regência verbal e nominal](LP.%20L%C3%ADngua%20Portuguesa%20e%20Interpreta%C3%A7%C3%A3o%20de%20Textos/LP.20%20Reg%C3%AAncia%20verbal%20e%20nominal.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 1 | Baixa incidência |
| LP.21 | [Concordância verbal e nominal](LP.%20L%C3%ADngua%20Portuguesa%20e%20Interpreta%C3%A7%C3%A3o%20de%20Textos/LP.21%20Concord%C3%A2ncia%20verbal%20e%20nominal.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 2 | Média incidência |
| LP.22 | [Orações reduzidas](LP.%20L%C3%ADngua%20Portuguesa%20e%20Interpreta%C3%A7%C3%A3o%20de%20Textos/LP.22%20Ora%C3%A7%C3%B5es%20reduzidas.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 0 | Nunca caiu |
| LP.23 | [Colocação pronominal](LP.%20L%C3%ADngua%20Portuguesa%20e%20Interpreta%C3%A7%C3%A3o%20de%20Textos/LP.23%20Coloca%C3%A7%C3%A3o%20pronominal.md) *(= LP.18)* | 2013, 2017, 2023, 2024 | 4 de 4 | 0 | Nunca caiu |
| LP.24 | [Estilística](LP.%20L%C3%ADngua%20Portuguesa%20e%20Interpreta%C3%A7%C3%A3o%20de%20Textos/LP.24%20Estil%C3%ADstica.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 1 | Baixa incidência |
| LP.25 | [Figuras de linguagem](LP.%20L%C3%ADngua%20Portuguesa%20e%20Interpreta%C3%A7%C3%A3o%20de%20Textos/LP.25%20Figuras%20de%20linguagem.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 2 | Média incidência |
| LP.26 | [Vícios de linguagem e qualidade da boa linguagem](LP.%20L%C3%ADngua%20Portuguesa%20e%20Interpreta%C3%A7%C3%A3o%20de%20Textos/LP.26%20V%C3%ADcios%20de%20linguagem%20e%20qualidade%20da%20boa%20linguagem.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 0 | Nunca caiu |
| LP.27 | [Fonemas](LP.%20L%C3%ADngua%20Portuguesa%20e%20Interpreta%C3%A7%C3%A3o%20de%20Textos/LP.27%20Fonemas.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 0 | Nunca caiu |
| LP.28 | [Semântica](LP.%20L%C3%ADngua%20Portuguesa%20e%20Interpreta%C3%A7%C3%A3o%20de%20Textos/LP.28%20Sem%C3%A2ntica.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 2 | Média incidência |
| LP.29 | [Emprego da crase](LP.%20L%C3%ADngua%20Portuguesa%20e%20Interpreta%C3%A7%C3%A3o%20de%20Textos/LP.29%20Emprego%20da%20crase.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 1 | Baixa incidência |
| LP.30 | [Sintaxe (regência, concordância e colocação)](LP.%20L%C3%ADngua%20Portuguesa%20e%20Interpreta%C3%A7%C3%A3o%20de%20Textos/LP.30%20Sintaxe%20%28reg%C3%AAncia%2C%20concord%C3%A2ncia%20e%20coloca%C3%A7%C3%A3o%29.md) | 2013, 2017, 2023, 2024 | 4 de 4 | 1 | Baixa incidência |

### Direitos Humanos

A numeração **2.1** e **2.2** é a do edital desta matéria — não se confunde com o eixo 2 (Farmacotécnica). O corpo de cada arquivo é a letra da lei da fonte citada.

| # | Tópico do edital | Fonte citada |
| :---- | :---- | :---- |
| 2.1 | [Declaração Universal dos Direitos Humanos](Direitos%20Humanos/2.1%20Declara%C3%A7%C3%A3o%20Universal%20dos%20Direitos%20Humanos.md) | Adotada pela Assembleia Geral das Nações Unidas em 10 de dezembro de 1948 |
| 2.2 | [Convenção Americana sobre Direitos Humanos](Direitos%20Humanos/2.2%20Conven%C3%A7%C3%A3o%20Americana%20sobre%20Direitos%20Humanos.md) | Assinada na Conferência Especializada Interamericana sobre Direitos Humanos (San José da Costa Rica), em 22 de novembro de 1969 |

## Outros arquivos

- `QOS_PMMG_Banco_de_Questoes.md` — banco de questões comentado das provas de 2013, 2017, 2022, 2023, 2024 e 2026. Os gabaritos e comentários ficam em blocos recolhíveis (`Gabarito oficial — clique para revelar`), para dar para responder antes de ver a resposta.
- `livros/` — material de apoio em markdown.

*Os números de editais, questões e incidência dos eixos de Farmácia vêm da planilha `QOS_PMMG_Analise_Estatistica`, abas «6. Cobertura do edital» e «7. Lacunas» (editais e provas de 2013, 2017, 2023 e 2024). Em Língua Portuguesa, a incidência foi mapeada no banco `QOS_PMMG_Banco_de_Questoes.md` sobre as mesmas quatro provas.*
