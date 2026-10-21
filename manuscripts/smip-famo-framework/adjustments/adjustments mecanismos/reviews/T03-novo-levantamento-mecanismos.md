# T03 — Novo levantamento de mecanismos (Lens): consolidação dos lotes, teste de mecanismo e vínculo com a mídia social

- **Manuscrito**: smip-famo-framework
- **Versão de referência**: cópia de revisão em Google Docs (ID em `context.md`) no estado
  de 2026-10-16, com os lotes 1–10 da T02 aplicados. A lista dos **39 mecanismos** usada
  para comparação é a tabela consolidada (6.11) de `adjustments/T02-ajustes.md` ("Nova
  tabela"). Esta tarefa ainda **não lê nem altera o texto do paper**.
- **Insumos**: `revisao_mecanismos/` — quatro pastas de lote com os PDFs elegíveis e
  `Mecanismos/` com as cinco listas geradas por IA (`mapeamento-mecanismos-polarizacao-lote-1.pdf`,
  `mecanismos-lote-2.txt`, `mecanismos-lote-3.txt`, `mecanismos-lote4-parte1.txt`,
  `mecanismos-lote4-parte-2.txt`).
- **Data**: 2026-10-17
- **Relatórios anteriores consultados**: T01 (relatório), T02 (Seções 12.1–12.4, 14.3 cluster
  (b), 14.5, 14.6), `adjustments/T02-ajustes.md` (tabela 6.11 e fichas), `backlog.md` (B01–B04),
  `INDEX.md`, `reference-coverage.md`.
- **Status**: roteiro em oito subtarefas (Seção 4, reorganizado em 2026-10-18). As
  **propostas preliminares** de T03.1 a T03.6 estão nas Seções 5 a 11, e **nada nelas está
  aprovado**. T03.1 concluída em 2026-10-18. Próximo passo: **T03.2, passo 2.1**, ou a D11 (estrutura do Apêndice A, 11.1). T03.7 (conferência nos PDFs) e T03.8
  (texto para o paper) não começaram.
- **Nota de roteiro**: o `CLAUDE.md` da raiz manda seguir `.claude/commands/manuscript-review.md`,
  mas a pasta `.claude/` não existe no repositório. Segui `manuscripts/CLAUDE.md` e a
  estrutura da T02. Achados levam o prefixo `T03-F`, achados indiretos `T03-I`.

---

## 1. Pedido do usuário

> Em T02 nós fizemos uma análise dos mecanismos que tinham sido levantados no artigo e
> ajustamos definições, organização, etc. Contudo, um problema é que nós não tínhamos de
> forma clara a maneira como esses mecanismos foram levantados e como chegamos àqueles
> artigos. Nesse sentido, achei melhor realizar um novo levantamento de artigos e por
> conseguinte um novo levantamento de mecanismos.
>
> [Levantamento: string no Lens, 886 resultados; triagem por IA em lotes de ~200, com
> título e ano, pedindo também a leitura do abstract; 51, 54, 44 e 77 elegíveis; extração
> dos mecanismos por outra IA generativa, em batch.]
>
> Agora, eu preciso que você me ajude a consolidar uma lista de mecanismos […]. Aplique o
> "Teste de Mecanismo" […]. Se estamos tratando de "social media-induced polarization",
> então os mecanismos que estamos mapeando no estudo devem ser todos mecanismos de
> polarização INDUZIDA ou empoderada ou pelo menos hospedada POR MÍDIA SOCIAL. Estamos
> verificando isso ao elencar cada mecanismo? Algum mecanismo pode ser induzido/empoderado
> por mídia mas também empoderado de outras formas? A mídia hospeda, empodera e/ou pode
> mitigar também o mecanismo? Implicações? Não quero perder essa discussão.
>
> Não quero que você misture os artigos que foram usados de fonte para fazer a lista de
> mecanismos em T02. Você pode se aproveitar daquela divisão de blocos […], avalie se ela
> ainda é coerente, ou se novos blocos são necessários.
>
> Eu ainda não sei o que será feito na versão final do artigo […]. Me ajude a pensar nisso
> também.

## 2. Por que esta tarefa existe e como se relaciona com a T02

- **A lacuna**: a T02 validou nomes, estrutura e definições dos mecanismos (41 → 39), mas
  não conseguiu documentar **como** eles foram identificados. A T02.4 (processo de
  identificação) foi adiada em 2026-10-16. Os fatos sobre o processo original dependem dos
  autores (T01-P6, T01-D2), e a trilha de auditoria (B01, Table S1) está adiada.
- **O que a T03 faz**: trata o novo levantamento como **um procedimento documentável**.
  Registra o protocolo, consolida os mecanismos extraídos, aplica a mesma régua da T02 (mais
  dois critérios novos, Seção 6) e compara o resultado com os 39.
- **Dois corpora, sem mistura** (pedido do usuário):
  - **Corpus V1**: as fontes dos 39 mecanismos da T02, citadas pela numeração da lista do
    paper (`[n]`).
  - **Corpus L**: os papers elegíveis do levantamento no Lens, citados por *Autor Ano* com o
    lote (`L1`–`L4`). A consolidação da Seção 8 usa **só** o corpus L.
  - **Interseção** (fato, conferido em `reference-coverage.md`): quatro trabalhos estão nos
    dois corpora. Del Vicario et al. 2016 ([52]; L1), Santos et al. 2021 ([59]; L1), Bail et
    al. 2018 ([84]; L2) e Iyengar et al. 2018 (L2; na lista do paper como [28], com data
    2019). Na consolidação, eles contam como corpus L. Ver T03-I04.
- **Regra 7**: este relatório não reescreve a T02. Onde ele afeta uma decisão da T02, isso
  é dito com o ID (ex.: D34).

## 3. Escopo

**Dentro do escopo:**
- o protocolo do levantamento (string, base, triagem, extração) e a qualidade dos insumos;
- as 66 entradas de mecanismo dos cinco arquivos;
- a régua de mecanismo (T02 §12.1), com dois critérios novos sobre o papel da mídia social;
- a consolidação, os blocos (T02 §14.5) e o cruzamento com os 39;
- as opções para o paper.

**Fora do escopo** (por ora):
- ~~as **ligações affordance → mecanismo** propostas nos arquivos da IA (ver T03-F04). A Seção
  7.1 e a Tabela 6 do paper continuam valendo;~~ **Entram no escopo desde 2026-10-18** (decisão
  do usuário sobre T03-F04, Seção 5.5): passos 4.3 e 8.3;
- redigir texto para o paper (vem na T03.8, depois das decisões);
- a leitura integral dos 226 PDFs (T03.7, com escopo a decidir em D9).

## 4. Subtarefas e roteiro

**Modo de trabalho** (o mesmo da T02): uma subtarefa por vez, na ordem abaixo, e um passo por
sessão. Em cada passo, o agente apresenta a proposta e o usuário aprova, ajusta ou rejeita
item a item. As decisões entram numa tabela "Decisões do usuário — T03.x" no fim da seção
correspondente, o passo recebe [x] e o `INDEX.md` é atualizado. As Seções 5 a 11 são a
**proposta inicial** de T03.1 a T03.6. Ao aprovar, a proposta pode mudar, e a mudança fica
registrada na tabela de decisões.

### 4.1 Visão geral

| ID | Subtarefa | Proposta em | Decisões | Depende de | Status |
|---|---|---|---|---|---|
| T03.1 | Protocolo e insumos | Seção 5 | achados F01–F05 | P1–P3 (dados do usuário) | **concluída em 2026-10-18** |
| T03.2 | Régua: Q5, Q6 e a coluna *Claim* | Seção 6 | D4 | — | **concluída em 2026-10-18** |
| T03.3 | Consolidação: 66 entradas → unidades → mecanismos | Seções 7 e 8 | D5, D6, D8 | T03.2 | **concluída em 2026-10-18** (43 mecanismos) |
| T03.4 | Blocos e ligações com affordances | Seção 9; passo 4.3 | D7 | T03.3 | **concluída em 2026-10-18** |
| T03.5 | Cruzamento com os 39 | Seção 10 | D10 | T03.2, T03.3 | **concluída em 2026-10-18** |
| T03.6 | Destino no paper | Seção 11 | D1, D2, D3 | T03.1–T03.5 | **concluída em 2026-10-18** |
| T03.7 | Conferência nos PDFs (regra 4) | Seção 16 | D9 | T03.3, T03.6 | **concluída em 2026-10-18** |
| T03.8 | Texto e ajustes no paper | — | um lote por item | T03.6, T03.7 | não iniciada |
| **T03.9** | **Atores no modelo** (incluída em 2026-10-18, pedido do usuário) | Seção 15 | D13–D17 | T03.3, T03.5 | **concluída em 2026-10-18** |

**Por que esta ordem**: a régua (T03.2) vem antes da consolidação, porque os vereditos
dependem dela. A consolidação e o cruzamento vêm antes do destino (T03.6), porque a decisão
D1 depende do que o corpus sustenta e do que acrescenta. A conferência nos PDFs (T03.7) vem
depois do destino, porque o escopo dela depende da D1. O texto (T03.8) fica por último.
T03.1 pode correr em paralelo com as demais: ela depende de dados que só o usuário tem.

### 4.2 Roteiro

#### T03.1 — Protocolo e insumos (proposta na Seção 5) · concluída em 2026-10-18
- [x] **1.1 Registro do protocolo.** O usuário fornece: a exportação do Lens (886 registros
  com abstract), a data da busca, os campos e os filtros (P1); as listas de elegíveis e de
  excluídos por lote (P2); o nome e a versão das ferramentas de IA e os prompts da triagem e da
  extração (P3). O agente preenche a tabela 5.1 e marca o que ainda faltar.
  *Aprovação*: a tabela 5.1 descreve o que foi feito?
  **Concluído em 2026-10-18** (5.1, 5.4, 5.5). Restam a data da busca, os campos, o modelo do
  Gemini e o prompt da extração.
- [x] ~~**1.2 Limpeza e recontagem dos lotes**~~ **Dispensado pelo usuário em 2026-10-18** (5.5). (T03-F05, P4). O agente propõe as ações, uma por
  linha: tirar a duplicata de Thunga 2026 (L3), tirar o `.txt` da pasta do L2, atualizar
  `lote-02-nao-baixados.md`, decidir sobre o zip do L1 e explicar as diferenças 51/49, 54/52/50
  e 77/38+34. **Nada é apagado sem aprovação.** Produto: tabela 5.2 final, com o número de
  registros em cada etapa (base de um fluxograma, se o paper tiver um).
- [x] **1.3 Achados metodológicos.** Aceitar, ajustar ou contestar T03-F01 a T03-F04, um por
  vez. Eles definem o que o método do paper pode afirmar.
  **Concluído em 2026-10-18** (5.5): F01 opção (a), rebaixado para Menor; F02 registrado; F03
  com critério de inclusão na síntese (147 incluídos, 5.6); F04 contestado pelo usuário,
  reformulado e rebaixado para Menor.
- [x] **1.4 Casos de borda da inclusão** (5.6). **Concluído em 2026-10-18**: (a) não entram;
  (b) considerados descartados. (a) Os 12 papers que só aparecem nos
  quadros-resumo do lote 4 entram ou não? (b) Fazer uma leitura humana dos títulos e abstracts dos
  57 não citados para recuperar os relevantes que o Gemini omitiu (ex.: Halberstam e Knight
  2016, Cota et al. 2019, Roth et al. 2020)?

#### T03.2 — Régua (proposta na Seção 6) · concluída em 2026-10-18
- [x] **2.1 Q5, Q6 e a regra de inclusão** (6.2; itens para aprovação em **6.4**, 2026-10-18). **Concluído em 2026-10-18**: os cinco itens aprovados. Aprovar, ajustar ou rejeitar os dois
  critérios e a regra "entra quem passa em Q1–Q4 e tem via de plataforma em Q5".
- [x] **2.2 Definição de SMIP no paper** (P6; leitura feita em 2026-10-18, itens para aprovação em **6.5**). **Concluído em 2026-10-18**: os cinco itens aprovados; a leitura ampla já é a do paper. O agente lê a Seção 2.1 na cópia de revisão e
  traz o trecho. O usuário escolhe a leitura restritiva ou a ampla (6.3, ponto 4). A escolha
  decide se os itens que a plataforma só hospeda contam como mecanismos.
- [x] **2.3 Discussão induzido × hospedado × mitigado** (6.3, pontos 1 a 4; itens para aprovação em **6.6**, 2026-10-18). **Concluído em 2026-10-18**: seis itens aprovados. Validar ponto a
  ponto. O que for aprovado vira base para a discussão do paper (T03.8, passo 8.5).
- [x] **2.4 Coluna *Claim* em duas dimensões** (papel da plataforma e direção da evidência; itens para aprovação em **6.7**, 2026-10-18). **Concluído em 2026-10-18**: seis itens aprovados; D1 = C.
  Fecha a D4.

#### T03.3 — Consolidação (proposta nas Seções 7 e 8) · concluída em 2026-10-18
- [x] **3.1 Agrupamento das 66 entradas** (Seção 7; lotes aprovados em 7.1–7.5). **Concluído em 2026-10-18.** Aprovar o destino de cada entrada bruta,
  lote a lote: L1 → L2 → L3 → L4a → L4b.
- [x] **3.2 As 15 unidades que já existem na lista atual** (8.1, linhas sem "novo"; itens para aprovação em **8.3**, 2026-10-18). **Concluído em 2026-10-18**: três grupos aprovados. Confirmar a
  correspondência em três grupos: blocos A e B (K01–K08) · bloco C (K12–K17) · blocos D e E
  (K27, K30, K31).
- [ ] **3.3 Candidatos novos, um por vez** (D5; K04, K11 e K10 **aprovados** em 2026-10-18, 8.4–8.6; K18 **não entra**, 8.7; K32 **aprovado**, 8.8; K29 **não entra**, 8.9). **Concluído em 2026-10-18**: entram K04, K11, K10, K32: K04 dissolução seletiva de laços (com a D6) →
  K11 backfire → K10 influência social negativa → K18 sobrecarga cognitiva → K32 retaliação
  por denúncias → K29 efeito terceira pessoa. Para cada um, o agente apresenta o que ele é, a
  fronteira com os mecanismos vizinhos, Q5, a base e o que falta conferir. A entrada fica
  **condicionada à T03.7**.
- [x] **3.4 Unidades que não entram** (8.2, D8; itens para aprovação em **8.10**, 2026-10-18). **Concluído em 2026-10-18**: K21, K22, K23 não entram; K33 fundido em A2. Aprovar em bloco os destinos simples (K09,
  K16, K19, K20, K21, K24, K25, K26, K28) e decidir à parte K22, K23 e K33.

#### T03.4 — Blocos (proposta na Seção 9) · concluída em 2026-10-18
- [x] **4.1 Base e divisão** (D7; itens para aprovação em **9.1**, 2026-10-18). **Concluído em 2026-10-18**: sete blocos; B com três subgrupos: manter os sete blocos com dois subgrupos em B (seleção ×
  influência) ou dividir B.
- [x] **4.2 Bloco de cada candidato** aprovado no passo 3.3. **Concluído em 2026-10-18**: IDs pela opção (a), tabela de correspondência em 9.1.
- [x] **4.3 Ligações affordance → mecanismos novos** (ligações para aprovação em **9.2**; **concluído em 2026-10-18**: 14 aprovadas, 10 rejeitadas; incluído em 2026-10-18; decisão sobre
  T03-F04, 5.5). Para cada candidato aprovado, o agente parte das ligações propostas pelo Gemini
  e as revisa uma a uma, com o mesmo padrão das ligações dos 39: passo causal explícito (o que a
  affordance muda no mecanismo), nomes atuais das affordances (o lote 1 usa os antigos) e fonte
  quando houver. O usuário aprova ligação a ligação. Produto: linhas novas para a Tabela 6 e
  justificativas para a 7.1 (redigidas no passo 8.3).

#### T03.5 — Cruzamento com os 39 (proposta na Seção 10) · concluída em 2026-10-18
- [x] **5.1 Os 16 "sim" e os 9 "parcial"**: validar a leitura, em dois grupos. (Cruzamento atualizado em **10.1**: 16 sim, 7 parcial, 16 não.) **Concluído em 2026-10-18**; K28 removido de D5.
- [x] **5.2 Os 14 "não"** (16 depois do 5.1; itens para aprovação em **10.2**, 2026-10-18). **Concluído em 2026-10-18**: os 16 mantidos; C7 passa a parcial: decidir como o paper justifica a permanência deles (vieram das obras
  âncora, e a string não os alcança, T03-F01).
- [x] **5.3 Q5 aplicado aos 39** (D10; tabela e itens para aprovação em **10.3**, 2026-10-18). **Concluído em 2026-10-18.** Começar pelos quatro classificados só como "Hosts" (C1,
  C2, C4, C5), conforme a escolha do passo 2.2.

#### T03.6 — Destino no paper (proposta na Seção 11) · concluída em 2026-10-18
- [x] **6.1 D1**: opção A, B ou C. **Decidido antecipadamente em 2026-10-18, no passo 2.4: Opção C.**
- [x] **6.2 D2**: string (declarar a limitação ou fazer busca complementar). **Decidido
  antecipadamente em 2026-10-18, no passo 1.3: (a), declarar** (5.5). Uma busca nova vira
  tema próprio em `areas/mestrado/smip-paper/`, com aprovação por item (G4).
- [x] **6.3 D3** (**decidido em 2026-10-18: a conferência já foi feita**, 11.2): conferência humana da triagem (escopo e forma, por exemplo uma planilha com
  os 226 incluídos e uma amostra dos excluídos).
- [x] **6.4 Uso de IA generativa no método** (11.3). **Concluído em 2026-10-18**: política do periódico (P8) e o que declarar.

#### T03.7 — Conferência nos PDFs (regra 4) · concluída em 2026-10-18
- [x] **7.1 D9**: escopo da conferência (16.1). **Concluído em 2026-10-18**: 42 papers confirmados, 2 retirados.
- [x] **7.2 Candidatos aprovados no passo 3.3** (feito no passo 3.3, 8.4–8.9), um por vez: para cada paper citado, o que ele
  diz (com página) e se sustenta, contesta ou não trata o mecanismo.
- [x] **7.3 Evidência contrária** (feito em T03-F03 e 10.1) (5.3 e 6.3), para a discussão.
- [x] **7.4 As 15 unidades já existentes** (feito em 16.1) (antes da submissão, se D9 = (b)).
- [x] **7.5 BibTeX via Crossref** (16.2; `references-T03-novas.bib`, 42 entradas) (G1) de cada obra do corpus L que entrar no paper.

#### T03.9 — Atores no modelo (proposta na Seção 15; incluída em 2026-10-18) · concluída em 2026-10-18
Pedido do usuário: dar mais destaque aos atores, com seis tipos, uma figura nova do framework
(`actors/new_model_famo.jpg`) e o mapeamento mecanismo × ator primário e secundário, feito para
os 41 da v1 e a ajustar à lista de 43. Feita **antes** da T03.8, porque muda a 2.3, a 5 e a tabela.
- [x] **9.1 Conceito** (concluído em 2026-10-18; algoritmo mantido como *Algorithmic system*): definição de *Actor* (2.3), o caso do algoritmo, a fronteira com a
  plataforma (AF10) e com as contingências (D13–D16).
- [x] **9.2 Mapeamento** dos 43 mecanismos × ator primário e secundário (D17). **Concluído em 2026-10-18.**
- [x] **9.3 Figura 2 nova**: setas e rótulos (15.4). **Concluído em 2026-10-18**: PNG em `actors/new_model_famo_v2.png`.
- [x] **9.4 Texto da 5.3 (*Actors*)** (15.5). **Concluído em 2026-10-18**: revisão do rascunho (IDs e nomes atuais, fontes conferidas,
  estilo), com o texto em inglês redigido no passo 8.x.
- [x] **9.5 Forma no paper** (15.6). **Concluído em 2026-10-18**: tabela compacta na 5.3 e colunas na tabela consolidada e na Table A1: tabela compacta na 5.3 e colunas de ator na Table A1.
- [x] **9.6 Propagação** (15.7). **Concluído em 2026-10-18**, com a frase sobre atores na Introdução: 2.3, 5.1, ficha de G3 ("the clearest case of the actors defined in Section
  2.3"), 9.1, 10.2 (jornalismo: veículos e jornalistas como atores organizados em E3).

#### T03.8 — Texto e ajustes no paper
**Organização adotada em 2026-10-18**: seis lotes em `adjustments/T03-ajustes.md` (1 atores; 2 fichas; 3 tabelas e 7.1; 4 Seção 9 e 10.2; 5 método, Apêndice A e *Acknowledgments*; 6 propagação). Lotes 1 (T03-A1 a A9) e 2 (T03-A10 a A39) aplicados em 2026-10-18 e conferidos na releitura.
Um lote de ajustes por passo, como na T02: fonte em `adjustments/T03-ajustes.md`, aplicação
na cópia de revisão só depois de aprovado.
- [ ] **8.1 Método e Apêndice A** (reformulado em 2026-10-18, pedido do usuário; estrutura na
  Seção 11.1). Em ordem: (a) aprovar a estrutura (D11, **aprovada em 2026-10-18**); (b) A.2, segundo levantamento; (c) A.1,
  primeira lista (depende de D12); (d) A.3, relação entre as listas (depende de D1); (e) remissão
  curta na 4.3 e na 6.1 e ajuste da Figura 1. O apêndice absorve T01-A10, T01-A11 e T01-A12 e o
  B01, para não haver dois textos sobre o mesmo processo.
- [ ] **8.2 Fichas dos mecanismos novos**, no modelo de definição da T02 (§12.3).
- [ ] **8.3 Tabelas**: tabela consolidada 6.11 (coluna *Claim* em duas dimensões e itens
  novos), Tabela 6 e Seção 7.1 (ligações aprovadas no passo 4.3, no mesmo padrão das ligações
  dos 39).
- [ ] **8.4 Origem de cada item**: coluna na tabela ou Table S1 (retoma o B01).
- [ ] **8.5 Discussão e limitações**: evidência contrária, causalidade reversa (T03-I03, I05) e
  limites da string e da triagem.
- [ ] **8.6 Propagação**: contagem "39", IDs e figuras.

### 4.3 Nota sobre os IDs

Na primeira versão deste relatório (2026-10-17), a numeração das subtarefas era outra: T03.0
protocolo, T03.1 inventário, T03.2 consolidação, T03.3 blocos, T03.4 cruzamento, T03.5 PDFs,
T03.6 destino. A nova numeração substitui a antiga em todo o relatório e no `INDEX.md`. Os
IDs de achados (T03-F01 a F05, T03-I01 a I05), de decisões (D1–D9) e de unidades (K01–K33) não
mudaram. D10 é novo e separa da D4 a aplicação de Q5 aos 39.

**Ressalva que vale para todo o relatório**: as listas de mecanismos e as atribuições de
papers foram geradas por IA. Pela regra 4, **nenhuma atribuição "paper X sustenta o
mecanismo Y" está verificada**, exceto as nove conferidas no PDF e indicadas com página.
As demais levam **[a verificar]** até a T03.7.

---

## 5. T03.1 — Protocolo e insumos: o levantamento como foi feito

### 5.1 Protocolo reconstruído

Atualizada em 2026-10-18 (passos 1.1 e 1.4), com os filtros, a planilha do Lens, as datas, as
ferramentas de IA e a conferência humana informados pelo usuário.

| Item | O que se sabe | Fonte | Falta |
|---|---|---|---|
| Base | Lens (lens.org) | usuário | campos pesquisados (título, abstract, palavras-chave, texto completo?) |
| Filtros | Tipo de documento: *journal article*, *conference proceedings article* e *book chapter* | usuário (2026-10-18) | outros filtros, se houver (ano, idioma). Os anos dos 886 registros vão de 2006 a 2026 |
| String | `mechanism AND "social media" AND polarization AND (feature OR outcome OR contingencies) AND ("echo chamber" OR "filter bubble" OR "confirmation bias" OR "homophily" OR "news avoidance")` | usuário | se o Lens aplicou *stemming* ("contingencies" pega "contingency"?) |
| Data da busca | **13/10/2026** | usuário (2026-10-18) | — |
| Resultados | **886** registros (conferido) | `revisao_mecanismos/Cópia de polarization-mechanisms-02.xlsx` | — |
| Exportação | Pedida ao Lens com título e abstract. Segundo o usuário, por limitação do próprio Lens, grande parte dos registros veio **sem abstract**. A cópia em `revisao_mecanismos/` tem só *Title* e *Publication Year* (3 registros sem ano) | usuário (2026-10-18); planilha | — |
| Triagem | **Gemini (web)**, em 4 lotes de ~200, a partir da exportação (título e, quando havia, abstract), com o critério colado pelo usuário (Seção 1). O Gemini listou os elegíveis | usuário (2026-10-18) | — |
| Período de uso da IA | Semana de **11/10/2026 a 18/10/2026** (triagem e extração) | usuário (2026-10-18) | — |
| Conferência humana | Os autores avaliaram **os títulos dos elegíveis** e **os mecanismos levantados**, conferindo se eram coerentes com os artigos que a IA indicava e com a pesquisa anterior (a lista de 39 da T02). Os 663 excluídos não foram reavaliados | usuário (2026-10-18) | — |
| Elegíveis | 51 + 54 + 44 + 77 = **226** (usuário). Com PDF nas pastas: **223** registros do Lens (51, 52, 43 e 77), 3 a menos que o declarado (2 no L2, 1 no L3) | usuário; `revisao_mecanismos/triagem-reconstruida.csv` | os 3 elegíveis sem PDF, se existirem |
| Excluídos | **663** (886 − 223), reconstruídos pelo cruzamento dos PDFs das pastas com a planilha | `triagem-reconstruida.csv` | — |
| Extração | **Gemini notebook (web)**, a partir dos **PDFs** dos elegíveis. O lote 1 traz a definição de mecanismo do paper como "Critério teórico de rigor" (p. 1). Os lotes 1–4 mapeiam depois as "11 affordances" | usuário (2026-10-18); arquivos em `Mecanismos/` | confirmar se "Gemini notebook" é o NotebookLM, o produto do Google para análise de documentos; prompt completo da extração |
| Inclusão na síntese | Papers citados como referência de algum mecanismo da lista preliminar (Tabela 8.1): ~~147~~ ~~145~~ **144** (K18 e K29 excluídos, 8.7 e 8.9). Os 12 casos de borda e os 57 não citados foram **descartados** | usuário (2026-10-18); `inclusao-sintese-preliminar.csv` | provisório até a T03.3 e a T03.7 |

### 5.2 Contagens conferidas

| Lote | Elegíveis (usuário) | PDFs na pasta | Artigos analisados (arquivo de mecanismos) | Mecanismos extraídos | Observações |
|---|---|---|---|---|---|
| L1 | 51 | 51 | 49 ("Lote 1 (49 Papers)") | 14 | Todos os autores citados estão na pasta. Papers da pasta não citados em nenhum mecanismo, entre eles Dubois e Blank 2018 e Roth et al. 2020 (ver T03-F03) |
| L2 | 54 | 52 PDFs + 1 `.txt` | "50 papéis" | 11 | `lote-02-nao-baixados.md` diz 23 não baixados, mas a pasta tem 52 PDFs, inclusive itens da lista de não baixados (ex.: Nelimarkka et al. 2018): arquivo desatualizado. A pasta contém `Ukrainian Sentiment Dictionary from Polarized Ukraine 2014.txt`, que não é paper |
| L3 | 44 | 44 (43 únicos) | "primeiro lote de 45 artigos" | 17 | Thunga 2026 está duplicado (dois arquivos). O arquivo se chama de "Lote 1". Cita Wesemael et al. 2026 e van Baar e FeldmanHall 2021, cujos PDFs estão na pasta do **L2** |
| L4 | 77 | 77 | 38 (parte 1) + "39" (parte 2; a tabela da parte 2 lista 34) | 14 + 10 | Parte 2 numera de 1 a 10, sem continuar a parte 1 |
| **Total** | **226** | 224 PDFs, 223 únicos | ~221 | **66** | — |

### 5.3 Achados

| ID | Achado | Severidade |
|---|---|---|
| T03-F01 | A string exige os nomes de cinco mecanismos e o vocabulário do próprio framework | ~~**Crítico**~~ Menor desde 2026-10-18, se declarado no método (5.5) |
| T03-F02 | A triagem por IA não é reproduzível e tem baixa precisão | ~~**Importante**~~ Menor desde 2026-10-18 (5.5) |
| T03-F03 | As listas de "evidência" da IA incluem papers que contestam o mecanismo | **Crítico** |
| T03-F04 | As ligações affordance → mecanismo dos arquivos são especulação forçada a cobrir as 11 affordances. *Reformulado em 2026-10-18*: são rascunho de justificativa teórica, a revisar ligação a ligação (5.5) | ~~**Importante**~~ Menor desde 2026-10-18 |
| T03-F05 | Inconsistências de arquivo entre lotes | Menor |
| T03-F06 | O procedimento de *Claim* da 6.1 não cobre o processo que não existe fora da plataforma (6.5) | Menor |

#### T03-F01 — A string exige os nomes de cinco mecanismos e o vocabulário do próprio framework · **Crítico** · novo
- **Fato**: o último bloco da string é obrigatório (AND) e é composto de nomes de mecanismos:
  *echo chamber*, *filter bubble*, *confirmation bias*, *homophily*, *news avoidance*. O bloco
  anterior, também obrigatório, usa três termos do framework (*feature*, *outcome*,
  *contingencies*). *Affordance*, o termo central do framework, não aparece. No resultado
  (Seção 10), os mecanismos com mais suporte são justamente os vizinhos desses cinco
  termos. Os blocos F (interação) e G (ecossistema) da T02 quase não aparecem.
- **Julgamento**: a busca encontra, sobretudo, o que já nomeou. Um corpus assim não sustenta
  uma afirmação de cobertura da literatura sobre mecanismos, porque um mecanismo que nunca é
  discutido junto com aqueles cinco termos não tem como entrar. Um revisor de método vai
  notar a circularidade. Dois caminhos (D2): (a) declarar a string como **orientada a um
  núcleo de mecanismos conhecidos**, usar o corpus para validar e ampliar a tipologia e
  registrar a limitação; (b) rodar uma string complementar sem o bloco de nomes (ex.: termos
  genéricos como *mechanism\** OR *pathway\** OR *process\**) ou strings dirigidas aos
  blocos que faltam. O termo *contingencies* no plural e a ausência de *affordance* também
  precisam de justificativa ou correção.

#### T03-F02 — A triagem por IA não é reproduzível e tem baixa precisão · **Importante** · novo
- **Fato**: segundo o usuário, a IA recebeu título e ano e foi orientada a considerar também
  o abstract. O critério colado diz "atente à coluna Title". Não há registro da ferramenta,
  da versão, da data nem da origem dos abstracts. Entre os elegíveis há títulos sem relação
  com polarização por mídia social, por exemplo: *Dental caries misinformation on Instagram*
  (Menezes et al. 2026, L4), *Factors Associated With Nurses' Self-Reported Susceptibility to
  Online Health…* (Katsiroumpa et al. 2026, L4), *The polarization of literary censorship in
  the U.S.* (Szetela et al. 2025, L2), *Deep learning for misinformation detection on online
  social networks: a survey* (Islam et al. 2020, L3), *Enhancing Social Media Platforms with
  Machine Learning Algorithms and Neural Networks* (Taherdoost 2023, L1).
- **Julgamento**: o critério ("qualquer mecanismo") é permissivo de propósito, o que explica
  parte da baixa precisão e é defensável. O problema é outro: sem o abstract fornecido à IA,
  não há como saber se ela leu o abstract ou o inferiu. Sem registro, a triagem não pode ser
  reproduzida. Para um artigo, o mínimo é: exportar do Lens os 886 registros com abstract,
  registrar a ferramenta e o prompt, e fazer uma **conferência humana** (todos os 226
  incluídos e uma amostra aleatória dos 660 excluídos, para estimar falsos negativos). O uso
  de IA generativa no método precisa ser declarado. Conferir a política da *Journalism and
  Media* (MDPI) sobre isso **[conferir; ligado à pendência T01-P5]**.

#### T03-F03 — As listas de "evidência" da IA incluem papers que contestam o mecanismo · **Crítico** · novo
- **Fato** (nove PDFs conferidos, primeira página):

| Paper (lote) | Usado pela IA como evidência de | O que o paper diz |
|---|---|---|
| Nordbrandt 2021 (L3) | homofilia/exposição seletiva, câmara de eco, bolha de filtro, *backfire*, contágio moral (L3-01, 02, 03, 07, 09) | "No support was found for the hypothesis that social media use contributed to the level of affective polarization. Instead, the results lend support to the hypothesis that it was the level of affective polarization that affected subsequent use of social media" (p. 3392) |
| Fletcher et al. 2021 (L4) | exposição seletiva, bloqueio partidário (L4a-01, 02) | câmaras de eco partidárias "are real, but only a minority of approximately 5% of internet news users inhabit them", e "more people consume no online news at all than occupy partisan online echo chambers" (p. 1) |
| Liu et al. 2025 (L2) | bolha de filtro (L2-04), com a nota "estudo de teste empírico de curta duração" | "manipulating algorithmic recommendations to create these conditions has limited effects on opinions" (p. 1) |
| Törnberg 2026 (L1) | reestruturação homofílica (L1-01) e cascata de saída (L1-08) | segregação "can arise even without algorithmic personalization and without users preferring homogeneous environments"; "algorithmic personalization can, under some conditions, reduce segregation" (p. 1) |
| Tonin et al. 2025 (L4) | exposição/evitação seletiva (L4b-04) | "offline partisan isolation […] is higher than online segregation" (p. 1) |
| Geiß et al. 2021 (L4) | câmara de eco, espiral do silêncio, assimilação enviesada (L4a-05, 06, 07) | "recent theorizing and evidence has cast doubts on the universal applicability of the echo chamber metaphor" (p. 660) |
| Masip et al. 2020 (L4) | exposição/evitação seletiva (L4b-04) | "high levels of selective exposure that are a characteristic of offline media consumption are being moderated in the online realm" e usuários mais ativos em redes sociais "are more likely to be exposed to news content from different ideological positions" (p. 53) |
| Bail et al. 2018 (L2) | homofilia, câmara de eco, *backfire* | republicanos que seguiram um bot liberal "became substantially more conservative posttreatment" (p. 1). Sustenta o *backfire*, e não a câmara de eco |
| Dubois e Blank 2018 (L1) | **não citado** em nenhum mecanismo | título: "The echo chamber is overstated: the moderating effect of political interest and diverse media" (p. 729) |

  Somam-se as falhas de 5.2: autores de um lote citados em outro, contagens divergentes e
  papers da pasta nunca citados.
- **Acréscimo (2026-10-18, passo 3.3)**: em K18 (8.7), **nenhuma** das quatro fontes citadas
  sustenta a cadeia descrita pelo Gemini, e uma delas (Bo et al. 2025) aponta o contrário. É o caso
  de uma unidade inteira sem base. O mesmo vale para K29 (8.9): a fonte não trata de polarização,
  e os passos que levariam a ela foram acrescentados pelo Gemini.
  Em K28 (10.1), a única fonte (Fang et al. 2024) menciona o processo só como citação de outra
  obra, e não como achado.
- **Julgamento**: a coluna "Evidência na literatura" dos arquivos lista papers **sobre** o
  tema do mecanismo, e não papers **a favor** dele. Em seis dos nove casos conferidos, o sinal
  está trocado ou o paper relativiza o papel da mídia social. Isso tem duas consequências.
  (1) **Nenhuma** dessas listas pode virar coluna *Ref* ou *Evidence* no paper sem a T03.7.
  (2) Essas falhas são, ao mesmo tempo, o material mais valioso do corpus para a discussão
  "induzido × hospedado" da Seção 6.3. O corpus L contém uma literatura que testa e,
  muitas vezes, relativiza o papel causal da mídia social, e a extração por IA a apagou.

#### T03-F04 — As ligações affordance → mecanismo são especulação forçada a cobrir as 11 affordances · **Importante** · novo
- **Fato**: os quatro arquivos fecham com uma variação de "Todas as 11 affordances foram
  contempladas no mapeamento. Nenhuma ficou de fora". As justificativas não citam papers. O
  lote 1 usa os nomes de affordance **anteriores** à T02 (*Connection recommendation*,
  *Context collapse (2nd-order)*), e os lotes 2–4 usam os nomes **posteriores** às decisões
  D21 e D22 (*Network-informed associating*, *Audience segmentation*). Há ligações sem
  sentido técnico, por exemplo *Constraint affordance* como "feeds organizados por
  relevância" (L3, mecanismo 3).
- **Julgamento**: são hipóteses geradas para cumprir a instrução de cobrir todas as
  affordances, e não um achado da literatura. Não devem alimentar a Seção 7.1 nem a Tabela 6.
  Onde uma ligação nova parecer útil, ela entra como hipótese e precisa de fonte.

#### T03-F05 — Inconsistências de arquivo entre lotes · **Menor** · novo
- **Fato**: duplicata de Thunga 2026 (L3); `.txt` de dicionário de sentimentos no L2;
  `lote-02-nao-baixados.md` desatualizado; o arquivo do L3 se chama de "lote 1"; o zip
  `Primeiro Lote-20261017T165419Z-1-001.zip` duplica a pasta do L1.
- **Julgamento**: limpeza simples, mas necessária antes de qualquer contagem que vá para o
  paper (fluxograma do tipo PRISMA, se for o caso).

### 5.4 Cruzamento dos PDFs com a planilha (passo 1.1, 2026-10-18)

Feito para reconstruir a lista de excluídos (P2), comparando o título no nome de cada PDF das
pastas com os 886 títulos da planilha. Resultado em `revisao_mecanismos/triagem-reconstruida.csv`
(886 linhas: linha da planilha, título, ano, elegível/excluído, lote e observação).

- **223 registros do Lens têm PDF** nas pastas, e todos os 223 PDFs únicos estão na planilha.
  Três casos só foram encontrados manualmente:
  - Halida 2020 e Taherdoost 2023 (L1): o título no Lens é diferente do título no nome do
    arquivo (o de Halida começa com "It's Not the Facebook Access…");
  - Madariaga et al. 2022 (L4): no Lens, o registro tem o título em espanhol ("Construyendo
    bloques…") e o ano 2024. O PDF tem os títulos em espanhol e em inglês **[a verificar o
    idioma do texto, regra G7]**.
- **Um PDF está com o nome errado**: `Chen - 2022 - The spreading of misinformation online.pdf`
  (L1) é, pela primeira página, *VisualBubble: Exploring How Reflection-Oriented User Experiences
  Affect Users' Awareness of Their Exposure to Misinformation on Social Media* (Chen, Ciuccarelli
  e Colombo 2022), que está no Lens com esse título. O nome do arquivo copia o título de Del
  Vicario et al. 2016, que também está no L1. Isso importa para a T03.7: uma citação de "Chen
  2022" nas listas da IA pode estar ligada ao paper errado.
- Os 3 elegíveis declarados sem PDF (226 − 223) são, por lote, 2 do L2 e 1 do L3.

### 5.5 Decisões do usuário — T03.1 (2026-10-18)

| Passo | Item | Decisão do usuário | Efeito |
|---|---|---|---|
| 1.1 | Tabela 5.1 | **Aprovada**: descreve o que foi feito. Faltava só o filtro por tipo de documento (*journal article*, *conference proceedings article*, *book chapter*), agora incluído. Planilha do Lens fornecida. Elegíveis = PDFs das pastas. Triagem e extração com o **Gemini (web)**; na extração, os PDFs foram enviados ao Gemini | P1 e P3 parcialmente resolvidas, P2 resolvida (5.4). Ainda faltam: data da busca, campos pesquisados, modelo/versão do Gemini e prompt da extração (P1, P3) |
| 1.2 | Limpeza e recontagem dos lotes | **Não será feita** | T03-F05 fica registrado, sem ação. Consequência para a T03.8: o número de elegíveis no paper precisa vir de uma única fonte. Hoje há duas: 226 (declarado) e 223 (com PDF) |
| 1.3 | T03-F01 (string) | **Opção (a)**: a string partiu de propósito de mecanismos conhecidos, aceitando que outros se perdessem. O paper não é revisão sistemática (é *theoretical review*, Paré et al. [15]), e nem uma revisão sistemática garantiria encontrar todos os mecanismos | **D2 = (a), decidida antecipadamente** (passo 6.2). **T03-F01 rebaixado de Crítico para Menor**, desde que o método declare o propósito da string (T03.8, passo 8.1). O texto deve explicar também o segundo bloco (*feature*, *outcome*, *contingencies*) |
| 1.3 | T03-F02 (triagem por IA) | A IA **auxiliou** o processo. O Gemini triou e levantou os candidatos, e depois recebeu os PDFs para a extração. O paper vai declarar que a IA auxiliou todo o processo, **sempre com conferência humana** | Ver comentário 1 abaixo. T03-F02 continua **Importante** até que o passo 6.3 (D3) defina como a conferência humana da triagem é feita ou foi feita |
| 1.3 | T03-F03 (evidência com sinal trocado) | Nem todos os elegíveis entram no paper final. Os que não apresentam mecanismos nem conteúdo relevante para a discussão são descartados. **Critério de inclusão na síntese** (2026-10-18): **entra o paper citado como referência de algum mecanismo da lista preliminar** (Tabela 8.1) | Etapa nova no fluxo: 886 → 226 elegíveis → **147 incluídos** (5.6). Os papers que contestam um mecanismo (Nordbrandt 2021, Fletcher et al. 2021, Liu et al. 2025 e outros) foram citados e entram. A direção que o Gemini lhes atribuiu continua sendo corrigida na T03.7. T03-F03 continua **Crítico** até a T03.7 |
| 1.3 | T03-F04 (ligações affordance → mecanismo) | **Contestado**: os mecanismos novos devem entrar na discussão das affordances, e a relação entre eles é estabelecida da mesma forma que para os 39 mecanismos da lista atual | **T03-F04 reformulado e rebaixado de Importante para Menor** (ver comentário 3). As ligações entram no escopo da T03 (passo 4.3) e no texto (passo 8.3) |
| 1.1 (complemento) | Fatos do protocolo | O Gemini listou os elegíveis. Foram usados o Gemini e o Gemini notebook (web), na semana de 11 a 18/10/2026. Busca no Lens em 13/10/2026, com exportação de título e abstract, mas grande parte veio sem abstract (limitação do Lens). Conferência humana: avaliação dos títulos dos elegíveis e da coerência dos mecanismos levantados com os artigos indicados e com a pesquisa anterior | Tabela 5.1 completa, salvo a confirmação do nome da ferramenta de extração. **T03-F02 rebaixado de Importante para Menor**: a triagem e a conferência estão descritas, e o que falta são limitações a declarar no apêndice (ver comentário 4) |
| 1.4 (a) | 12 casos de borda (só nos quadros-resumo do lote 4) | **Não entram** | Descartados |
| 1.4 (b) | 57 não citados | **Considerar descartados** (sem nova leitura) | Descartados. Inclusão na síntese: **147**; descartados nesta etapa: **69** (12 + 57), mais 7 que dependem do passo 3.4 |
| — | Apêndice metodológico | **Pedido novo**: um apêndice que descreva a metodologia do segundo levantamento e traga detalhes do processo da primeira lista | Proposta de estrutura na Seção 11.1. Passo 8.1 reformulado |

**Comentário 1 (F02): o que a declaração exige.** Para o método poder dizer "assistido por
IA, com conferência humana", o texto precisa descrever **em que consistiu** a conferência em
cada etapa. Os fatos sobre o que já foi feito só os autores sabem, e entram como placeholder
até serem informados: `[AUTORES: descrever a conferência humana da triagem: quem conferiu,
quais registros (incluídos, excluídos ou amostra) e com que critério]`. Na extração, a
conferência é a T03.7, ainda não feita. Hoje as listas do Gemini trazem atribuições com o sinal
trocado (T03-F03), e é essa conferência que as corrige. A declaração só será verdadeira depois
dela. É preciso registrar também o modelo e o período de uso do Gemini (P3), que as políticas
de periódicos costumam pedir (P8).

**Comentário 2 (F03): elegibilidade não é inclusão.** O critério do usuário resolve uma parte do
achado e deixa outra:
- **resolve**: um paper elegível sem mecanismo ou conteúdo relevante (por exemplo os títulos
  fora do tema citados em T03-F02) não precisa ir para o paper. O fluxo passa a ter três etapas:
  886 registros → 226 elegíveis na triagem → *n* incluídos na síntese (definido na T03.7);
- **não resolve**: os papers que **contestam** um mecanismo (Nordbrandt 2021, Fletcher et al.
  2021, Liu et al. 2025 e outros da tabela de T03-F03) atendem ao critério de "conteúdo relevante
  para a discussão". Eles não devem ser descartados, e sim incluídos **como evidência contrária**.
  O problema do achado é a direção que o Gemini atribuiu a eles, e não a presença deles. Isso
  continua exigindo a T03.7.

**Comentário 3 (F04): o que muda com a decisão do usuário.** O usuário tem razão num ponto que o
achado não considerava. As ligações affordance → mecanismo da lista atual (Seção 7.1, Tabela 6)
também são **justificativas teóricas dos autores**, e não resultados de busca. Tratar as
ligações dos mecanismos novos de outro modo criaria dois padrões no mesmo framework. O achado
fica reformulado assim: as ligações propostas pelo Gemini são **rascunho** de justificativa
teórica e entram na discussão das affordances depois de revistas ligação a ligação, com o mesmo
padrão das ligações dos 39. Três cuidados entram no passo 4.3, porque decorrem dos próprios
arquivos (fatos de T03-F04):
- **cobertura forçada**: o pedido para cobrir as 11 affordances gerou ligações sem sentido
  técnico (ex.: *constraint affordance* como "feeds organizados por relevância", L3). Cada
  ligação precisa do passo causal: o que a affordance muda no mecanismo;
- **nomes antigos no lote 1**: *Connection recommendation* e *Context collapse (2nd-order)*
  precisam ser lidos como *Network-informed associating* e *Audience segmentation* (D21, D22),
  e as ligações devem ser refeitas com as definições atuais;
- **mesmo padrão de fonte**: onde a ligação de um dos 39 cita uma fonte na 7.1, a ligação de um
  mecanismo novo também deve citar, se houver uma. Onde não houver, ela é declarada como
  justificativa teórica, como já acontece na lista atual.

**Comentário 4 (F02): o que a conferência humana cobre e o que não cobre.** Pela descrição do
usuário, a conferência foi feita sobre os **títulos** dos elegíveis e sobre a **coerência** dos
mecanismos com os artigos indicados e com a pesquisa anterior. É uma conferência real e pode ser
declarada como tal. O apêndice deve dizer também o que ela não cobriu, porque um revisor
perguntará: (i) os 663 excluídos não foram reavaliados; (ii) a triagem se apoiou, na maior parte,
só no título, porque faltavam abstracts; (iii) a conferência de coerência não verificou cada
atribuição paper → mecanismo no texto completo, e por isso os erros de direção de T03-F03
passaram. O item (iii) é o que a T03.7 resolve, e o apêndice pode descrevê-la como a etapa final
de verificação.

### 5.6 Inclusão na síntese: aplicação do critério (2026-10-18)

Critério do usuário: entra o paper citado como referência de algum mecanismo da lista preliminar
(Tabela 8.1). Aplicado às listas de evidência dos cinco arquivos do Gemini, considerando só as
entradas que viraram unidades da Tabela 8.1 (Seção 7, coluna "Unidade"), mais os papers que o
agente citou na própria Tabela 8.1. Cada citação foi conferida contra os PDFs das pastas.
Resultado em `revisao_mecanismos/inclusao-sintese-preliminar.csv` (223 linhas: pasta, arquivo,
situação e entradas de origem).

| Situação | PDFs | Observação |
|---|---|---|
| **Incluídos** | ~~147~~ ~~145~~ **144** (2026-10-18, após a exclusão de K18 e K29) | L1 21 · L2 ~~36~~ 34 · L3 ~~32~~ 31 · L4 58. Inclui Dubois e Blank 2018 e Tonin et al. 2025, que o Gemini não citou e o agente citou na Tabela 8.1. Bo et al. 2025 e Clemons et al. 2025 saíram com K18 (8.7), e Yang e Tian 2021 com K29 (8.9) |
| Borda: só nos quadros-resumo do lote 4 (**descartados**, passo 1.4) | 12 | Arcos 2022, Bianchi e Tafuri 2023, Brum 2022, Böttcher e Gersbach 2020, Dykstra 2013, Ertan 2021, Juneja 2023, Katsiroumpa 2026, Miller 2021, Olshannikova 2022, Su 2020, Tsvetkova 2025. Os quadros-resumo os associam a um mecanismo, mas eles não estão nas listas de evidência |
| Citados só em unidades que não entraram | ~~7~~ ~~9~~ 10 | Antinyan 2024, Bozdağ e Koçer 2022, Giese 2023, Kvam 2022, Li e Xu 2025, Yin 2024, Zafeiris 2022. Dependem do passo 3.4: se uma dessas unidades for aceita, os papers dela entram |
| Não citados em nenhum mecanismo (**descartados**, passo 1.4) | 57 | Ficam fora pelo critério, sem nova leitura |

**O número é provisório**: muda com as decisões da T03.3 (unidades aceitas ou rejeitadas) e com
a T03.7 (um paper incluído pode não sustentar nada depois de lido).

**Ponto de atenção**: o critério herda as omissões do Gemini. Entre os 57 não citados há títulos
que tratam diretamente de mecanismos da lista. Por exemplo: Halberstam e Knight 2016
(*Homophily, group size, and the diffusion of political information*), Cota et al. 2019
(*Quantifying echo chamber effects in information spreading*), Brugnoli et al. 2019 (*Recursive
patterns in online echo chambers*), Roth et al. 2020 (*Tubes and bubbles: topological confinement
of YouTube recommendations*), Li et al. 2019 (*Infectivity enhances prediction of viral cascades
in Twitter*), Ibrahim et al. 2026 (*Systematic partisan content skews in TikTok*) e Steiglechner
et al. 2023 (*Social identity bias and communication network clustering*). Uma leitura humana
dos títulos e abstracts dos 57, antes da T03.7, resolveria isso com pouco custo. **Decisão do
usuário (passo 1.4, 2026-10-18): considerar descartados.** A omissão entra nas limitações do
apêndice.

---

## 6. T03.2 — A régua: teste de mecanismo da T02 mais dois critérios

### 6.1 Q1–Q4 (inalterados, T02 §12.1)

| # | Pergunta | Falha típica |
|---|---|---|
| Q1 | O nome designa um **processo**? | Nomeia estado, tipo de conteúdo, grupo, estrutura ou sintoma |
| Q2 | Há cadeia **insumo → passo → mudança** com pelo menos dois passos? | Sem passo, ou guarda-chuva |
| Q3 | A mudança final é um dos **cinco outcomes** (2.2), sem ser o próprio outcome? | Outcome com outro nome |
| Q4 | **Não é** *feature*, *affordance*, contingência ou ator (2.3)? | Natureza de outra camada |

Vereditos: ✅ passa · 🔧 reformular · ❌ não passa como está. Regras de nome R1–R7 (T02 §12.4)
continuam valendo.

### 6.2 Os critérios novos

A T02 não tinha uma pergunta sobre o papel da mídia social. Ela aparecia só depois, na coluna
*Claim* da tabela (*Hosts / Amplifies / Creates*), preenchida item a item e com valores
compostos (ver `context.md`, "Divergências"). A pergunta do usuário pede que isso vire
critério de inclusão.

| # | Pergunta | Valores | Falha típica |
|---|---|---|---|
| **Q5** | **O que a mídia social faz com este processo, e por qual affordance?** | **Cria** (o processo não existe sem um elemento da plataforma) · **Amplifica** (processo humano geral, e a plataforma muda dose, velocidade, escala, custo ou visibilidade) · **Hospeda** (o processo ocorre igual dentro e fora da plataforma, que é só o palco) · e, separado, **Atenua** (há evidência de que a plataforma reduz o processo) | Nenhuma via de plataforma identificável: o processo é cognitivo ou social geral e a mídia social aparece só como contexto do estudo |
| **Q6** | **A evidência no corpus identifica a contribuição da plataforma?** | Experimento ou quase-experimento com manipulação da plataforma · dado observacional de plataforma · survey · simulação (ABM) · teórico | Só simulação ou só teórico: o processo é **possível** na plataforma, e não **demonstrado** nela |

**Regra de decisão proposta**: entra na tipologia de SMIP quem passa em Q1–Q4 **e** tem
Q5 diferente de "nenhuma via". Q6 não exclui. Ela calibra a coluna *Evidence* (simulação
ou teórico → no máximo *Plausible*).

### 6.3 Induzido, empoderado, hospedado ou mitigado: a discussão

Os pontos abaixo respondem às perguntas do usuário, na ordem.

**(1) Estamos verificando o vínculo com a mídia social ao elencar cada mecanismo?** Não de
forma sistemática. Na v1 e na T02, o vínculo aparece na coluna *Claim* e no passo (ii) do
modelo de definição (T02 §12.3, "o que a plataforma muda"), mas não é condição de entrada.
Na extração por IA, também não. Pelos arquivos, a extração aplicou a definição de mecanismo
do paper (lote 1, p. 1), mas nenhum deles registra o papel da plataforma em cada mecanismo
(o prompt completo não está disponível, P3). A IA devolveu vários processos gerais de
dinâmica de opinião, e a mídia social só aparece depois, nas ligações com as affordances
(T03-F04). Três entradas mostram o problema com clareza:
- **L3-08** (viés de confirmação no sistema de recompensa, Lefebvre et al. 2024): o próprio
  arquivo diz que a polarização surge "mesmo sem necessidade de interações sociais";
- **L4b-02** (amostragem sequencial, Kvam et al. 2022): um processo de decisão individual;
- **L1-13 / L4a-10** (confiança limitada): uma regra de modelos de dinâmica de opinião.

Nenhuma delas tem, na fonte, um passo que dependa da plataforma **[a verificar nos PDFs]**.

**(2) Um mecanismo pode ser induzido ou empoderado pela mídia social e também por outras
vias?** Sim, e é o caso da maioria. A exposição seletiva existia com jornais e TV a cabo:
Masip et al. 2020 descrevem a seletividade alta como "a characteristic of offline media
consumption" (p. 53). A segregação partidária é maior fora da rede do que dentro dela (Tonin
et al. 2025, p. 1). O mecanismo é o mesmo, e a mídia social é **uma** das vias que o ativam,
ao lado de mídia partidária, elites, segregação residencial e redes presenciais. Isso tem
três consequências:
- o paper não pode tratar a presença do mecanismo na plataforma como prova de que a
  plataforma o causou. Para isso, é preciso evidência contrafactual (Q6);
- a definição de cada mecanismo deve dizer **o que a plataforma acrescenta** em relação às
  outras vias. É o passo (ii) do modelo da T02, que passa a ser obrigatório;
- para um periódico de jornalismo, isso abre uma ponte natural: o jornalismo é uma das
  "outras vias" (ver G1, E3, C5 e C7 na T02).

**(3) A mídia social hospeda, empodera e/ou também pode mitigar o mecanismo?** As três
coisas, às vezes **ao mesmo tempo e pela mesma affordance**. O corpus L traz três casos:
- **Mesma affordance, efeitos opostos**: segundo Törnberg 2026, a personalização
  algorítmica "can, under some conditions, reduce segregation by lowering dissatisfaction,
  slowing exit cascades, and stabilizing mixed communities" (p. 1). AF1 alimenta a bolha de
  filtro e, no mesmo modelo, atenua a câmara de eco.
- **Mitigar um mecanismo pode ativar outro**: a exposição ao outro lado é a correção óbvia
  da câmara de eco, e a mídia social a aumenta (Masip et al. 2020, p. 53). Mas, em Bail et
  al. 2018, essa exposição produziu *backfire* (p. 1). A affordance que mitiga B2 ativa o
  candidato K11.
- **Causalidade reversa**: Nordbrandt 2021 encontra polarização → uso de mídia social, e não
  o contrário (p. 3392). Não é mitigação, mas mostra que a seta pode ir no sentido inverso.
  É evidência empírica para o *feedback loop* do framework (5.2), que já prevê esse retorno
  (T03-I03).

**(4) Implicações para o framework**:
- **Critério de inclusão** (Q5): um processo sem via de plataforma não é mecanismo de SMIP.
  Ele pode continuar no paper como **microfundamento**, isto é, a base cognitiva sobre a qual
  os mecanismos de plataforma operam, mas a tabela deve dizer isso.
- **Os itens "Hosts" da T02** (C1, C2, C4, C5): passam em Q5 só se "hospedar" contar como
  vínculo. Há duas leituras possíveis, e a escolha depende de como a Seção 2.1 define SMIP
  "em sentido amplo" (`context.md`) **[a verificar no texto da 2.1; o PDF da v1 está
  ausente, T02-P1]**.
  - **Leitura restritiva**: SMIP = polarização induzida **ou amplificada** pela mídia social.
    Os itens "Hosts" viram microfundamentos (camada de moderadores individuais, Tabela 3) e
    saem da contagem de mecanismos.
  - **Leitura ampla** (provavelmente a do paper): SMIP inclui o que ocorre **na** mídia
    social. Os itens "Hosts" ficam, mas a definição tem de dizer qual affordance lhes dá
    ocasião, sob pena de T02.1-F07 (mecanismos sem affordance) virar objeção de revisor.
- **A coluna *Claim* em duas dimensões**: **papel** (Cria / Amplifica / Hospeda) e **direção
  da evidência** (Reforça / Atenua / Mista). Hoje a direção está embutida em valores
  compostos da coluna *Evidence* ("Strong (phenomenon), weak (induced)", em C2). Separar
  resolve T01-I02 (escalas com valores compostos) de passagem.
- **Ligações affordance → mecanismo com sinal**: a Tabela 6 e a Seção 7.1 tratam toda ligação
  como "alimenta". A Tabela 5 (intervenções) já pressupõe que a mesma affordance pode ser
  redesenhada para atenuar. Marcar o sinal (+/−) onde houver evidência torna as duas tabelas
  coerentes.
- **O título** ("Social Media-Induced Polarization"): continua defensável se a 2.1 disser,
  com todas as letras, que "induced" cobre criar e amplificar, e que a tipologia inclui
  mecanismos que a plataforma só hospeda, marcados como tal. Sem isso, a evidência de
  atenuação e de causalidade reversa do próprio corpus L vira argumento contra o título.

### 6.4 Passo 2.1 — Q5, Q6 e a regra de inclusão: itens para aprovação (2026-10-18)

A proposta de 6.2 foi refinada em cinco itens. As mudanças em relação a 6.2 estão marcadas
como **ajuste**.

| Item | Proposta | Por quê | Recomendação |
|---|---|---|---|
| **2.1-a** Valores de Q5 | Q5 pergunta só o **papel** da plataforma, com três valores e um teste para cada. **Cria**: sem o elemento da plataforma, o processo não ocorre (retire a affordance e o processo desaparece). **Amplifica**: o processo existe fora da plataforma, e ela muda pelo menos um parâmetro dele (dose, velocidade, escala, custo ou visibilidade). **Hospeda**: o processo ocorre igual dentro e fora, e a plataforma só oferece a ocasião. **Ajuste**: *Atenua* sai de Q5 e vai para a direção da evidência (passo 2.4), porque atenuar não é um papel alternativo, e sim o sinal do efeito. A mesma affordance pode amplificar um mecanismo e atenuar outro (Törnberg 2026, p. 1) | Com *Atenua* dentro de Q5, um mecanismo ficaria com dois valores opostos na mesma coluna | Aprovar |
| **2.1-b** Valor único | Cada mecanismo recebe **um** valor de Q5. **Ajuste**: os valores compostos saem. "Hospeda e amplifica" vira **Amplifica**, porque amplificar já pressupõe hospedar. "Cria ou amplifica" vira o valor que a evidência sustenta e, na dúvida, o mais fraco, com a dúvida dita na definição | Resolve parte da T01-I02 (escalas com valores compostos). Atinge os 39 no passo 5.3: B1, C3, C7, D3, D4 ("Hosts & amplifies"), B6 ("Hosts (amplifies)") e G4 ("Amplifies or hosts") | Aprovar |
| **2.1-c** Via obrigatória | Todo valor de Q5 indica a affordance (AF1–AF11) e o parâmetro que ela muda. Sem via identificável, a resposta é **nenhuma via** | Torna Q5 auditável e liga a régua à Seção 7.1 e à Tabela 6 (passo 4.3) | Aprovar |
| **2.1-d** Regra de inclusão | Entra quem passa em Q1–Q4 e tem Q5 = **Cria** ou **Amplifica**. Q5 = **nenhuma via** não entra (já aplicado a K20, K21 e K24). Q5 = **Hospeda** fica para o passo 2.2, porque depende de como a Seção 2.1 define SMIP | Separa o que é consenso do que depende da definição do paper | Aprovar |
| **2.1-e** Q6 e o teto da evidência | A coluna *Evidence* passa a medir a **evidência do papel da plataforma**, e não a existência do fenômeno, que vai para o texto da definição. O desenho mais forte disponível define o teto: experimento ou quase-experimento que manipula um elemento da plataforma → até **Strong**; dados observacionais de plataforma ou survey → até **Moderate**; só simulação ou teoria → **Plausible**. Estudos do fenômeno fora da plataforma (laboratório, offline) não contam para o papel da plataforma. *Mixed* sai desta escala e vai para a direção (passo 2.4) | Resolve valores como "Strong (phenomenon), weak (induced)" (C2) e "Strong (lab), moderate (online)" (B3), que misturam as duas coisas. Torna a coluna conferível pelo leitor | Aprovar, com o destino de *Mixed* fechado no passo 2.4 |

**Aplicação a cinco unidades** (ilustração; o valor de cada uma é decidido no passo 3.2 ou 3.3):

| Unidade | Q5 com a régua refinada | Q6: desenho mais forte no corpus | Teto da evidência | Mudança em relação à Tabela 8.1 |
|---|---|---|---|---|
| K01 Filter bubble | **Cria** (AF1: sem curadoria algorítmica não há bolha de filtro) | experimento que manipula a recomendação (Liu et al. 2025, p. 1) | Strong. Direção **mista**, no passo 2.4 | nenhuma |
| K04 Dissolução seletiva de laços | **Amplifica** (AF3 e ferramentas de bloqueio: **custo** de cortar o laço) | experimento de campo (Martel et al. 2024) **[a verificar]** | Strong | nenhuma |
| K30 Aprendizagem por reforço social da expressão | **Amplifica** (AF4: **visibilidade** e assimetria do sinal de aprovação). A aprovação social existe fora da plataforma, e o contador de *likes* sem contador de rejeição muda o sinal | experimento (Konovalova et al. 2023) **[a verificar]** | Strong | "Cria ou amplifica" → **Amplifica** (2.1-b) |
| K10 Influência social negativa | **Hospeda** (AF8 torna visível o grupo do outro, mas o processo não muda de parâmetro) | só simulações | Plausible | decisão de inclusão adiada para o passo 2.2 (2.1-d) |
| K14 Raciocínio motivado | **Hospeda** | meta-análise sobre suscetibilidade à desinformação (Sultan et al. 2024), sem manipulação da plataforma | Plausible para o papel da plataforma. O fenômeno é forte, e isso vai para a definição | idem |

**Efeito, se tudo for aprovado**: das 21 unidades da Tabela 8.1, as que hoje estão como
"Hospeda" (K10, K14, K15) ficam com a inclusão condicionada ao passo 2.2. As demais seguem para a
T03.3 com a régua definida.

**Decisões do usuário — passo 2.1 (2026-10-18)**

| Item | Decisão | Efeito |
|---|---|---|
| 2.1-a | **Aprovado** | Q5 = papel (Cria / Amplifica / Hospeda), com os testes de 6.4. *Atenua* vai para a direção da evidência (passo 2.4) |
| 2.1-b | **Aprovado** | Valor único por mecanismo; "Hospeda e amplifica" → Amplifica. Vale para os 39 no passo 5.3 |
| 2.1-c | **Aprovado** | Todo valor de Q5 indica a affordance e o parâmetro que ela muda |
| 2.1-d | **Aprovado** | Entra Cria ou Amplifica; "nenhuma via" não entra; Hospeda depende do passo 2.2 |
| 2.1-e | **Aprovado** | *Evidence* mede o papel da plataforma, com teto pelo desenho do estudo; *Mixed* vai para a direção (passo 2.4) |

### 6.5 Passo 2.2 — Definição de SMIP no paper: o que o texto diz (2026-10-18)

**Base**: leitura somente da cópia de revisão em Google Docs (escopo `documents.readonly`), na
revisão vigente em 2026-10-18. Nada foi alterado. Trechos em inglês citados como estão; a Seção
6.1 ainda está em português (pendência de edição conhecida).

**Fato 1 — a definição de SMIP já é a leitura ampla.**
- Seção 2.1, §1: "this article adopts a broader definition aligned with current scholarship in
  political communication and political science, treating SMIP as the totality of processes
  through which social media platform design, usage, and governance generate, amplify, or host
  intergroup social division".
- Introdução: "This article adopts the term in a broader sense, encompassing the full range of
  processes through which social media platforms create, amplify, or host dynamics of social
  division".

**Fato 2 — a Seção 6.1 já tem um procedimento para a coluna *Claim*, e ele é quase o Q5.**
- Seção 6.1, parágrafo "Para 'Claim'": "cada mecanismo foi avaliado por três perguntas em
  sequência: o processo existe fora das plataformas de mídia social, com lógica essencialmente
  idêntica? Em caso afirmativo, algum insumo de design altera a dose, a velocidade, a escala ou a
  visibilidade desse processo? Em caso afirmativo a essa segunda pergunta, o processo deixaria de
  existir, ou se tornaria irrelevante, na ausência desse insumo?" A primeira sem a segunda dá
  'Hosts'; a segunda, 'Amplifies'; a terceira, 'Creates'.
- Seção 6.1, parágrafo "Para 'Evidence'": 'strong' = "replicação experimental ou
  quase-experimental robusta"; 'moderate' = "estudos observacionais consistentes entre si";
  'mixed' = "achados conflitantes entre estudos"; 'plausible' = "teoricamente bem fundamentados
  mas com evidência direta ainda escassa ou indireta".

**Julgamento**:
- A pergunta do passo 2.2 está respondida pelo próprio paper: **"host" faz parte da definição de
  SMIP**. Os mecanismos que a plataforma só hospeda pertencem à tipologia por definição, e não por
  concessão. A ressalva de 6.3, ponto (4), sobre o título também está atendida: a 2.1 já diz, com
  todas as letras, que o termo cobre criar, amplificar e hospedar.
- O Q5 aprovado no passo 2.1 reinventou, sem saber, o procedimento da 6.1. Isso é bom, porque
  confirma o critério. Mas o relatório e o paper não podem ter dois procedimentos. **O Q5 deve ser
  o procedimento da 6.1**, com os ajustes aprovados (via obrigatória, valor único, teto de
  evidência) incorporados ao texto dela na T03.8.
- Há uma lacuna no procedimento da 6.1 (achado T03-F06, abaixo).

#### T03-F06 — O procedimento de *Claim* da 6.1 não cobre o processo que não existe fora da plataforma · **Menor** · novo
- **Localização**: Seção 6.1, parágrafo "Para 'Claim'".
- **Fato**: as três perguntas só levam a um valor quando a primeira é respondida "sim" ("o processo
  existe fora das plataformas…?"). O texto não diz o que acontece quando a resposta é "não".
- **Julgamento**: é justamente o caso dos mecanismos mais específicos da plataforma, como a bolha
  de filtro (K01; A1 na lista atual) e a retaliação por denúncias (K32). A leitura óbvia é
  "Creates", e basta dizê-lo. Além disso, a lista de parâmetros da 6.1 (dose, velocidade, escala,
  visibilidade) não inclui o **custo**, que é o parâmetro de K04 (dissolução de laços: a plataforma
  barateia o corte do laço).

**Itens para aprovação**:

| Item | Proposta | Recomendação |
|---|---|---|
| **2.2-a** Hospeda conta | Completa a regra 2.1-d: **entra quem tem Q5 = Cria, Amplifica ou Hospeda**; "nenhuma via" não entra. Base: a definição de SMIP da 2.1 (Fato 1). K10, K14 e K15 seguem para a T03.3. C1, C2, C4 e C5 da lista atual permanecem como Hospeda | Aprovar |
| **2.2-b** Um procedimento só | O Q5 passa a ser o procedimento de *Claim* da 6.1, e não um critério paralelo. Os itens aprovados em 2.1 entram como ajustes ao texto da 6.1 (T03.8, passo 8.3) | Aprovar |
| **2.2-c** Fechar a lacuna (T03-F06) | Acrescentar à 6.1: "se o processo não existe fora da plataforma, o valor é 'Creates'". Acrescentar **custo** aos parâmetros (dose, velocidade, escala, visibilidade e custo). O teste de "Cria" de 2.1-a passa a usar a formulação da 6.1: o processo "deixaria de existir, ou se tornaria irrelevante" sem o insumo (**ajuste em 2.1-a**, que dizia só "não ocorre") | Aprovar |
| **2.2-d** Via de "Hospeda" | Para Hospeda, a via obrigatória (2.1-c) é a affordance que **oferece a ocasião** para o processo, sem mudar parâmetro dele. A definição da 2.1 fala em "design, usage, and governance": a ocasião costuma vir do uso (exposição a conteúdo político) e é registrada pela affordance que a fornece (ex.: AF1 para o raciocínio motivado) | Aprovar. Isso resolve o caso dos mecanismos sem affordance na Tabela 6 (T02.1-F07; E3 na T02.5) |
| **2.2-e** Vocabulário | A Introdução diz "create", a 2.1 diz "generate", e a tabela usa "Creates". Uniformizar para *create* | Aprovar (Menor; texto na T03.8) |

**Decisões do usuário — passo 2.2 (2026-10-18)**

| Item | Decisão | Efeito |
|---|---|---|
| 2.2-a | **Aprovado** | Regra de inclusão final: entra Q5 = Cria, Amplifica ou Hospeda; "nenhuma via" não entra. K10, K14 e K15 seguem para a T03.3 |
| 2.2-b | **Aprovado** | Q5 = procedimento de *Claim* da 6.1, com os ajustes do passo 2.1 incorporados ao texto da 6.1 na T03.8 (passo 8.3) |
| 2.2-c | **Aprovado** | Na 6.1: "não existe fora da plataforma → Creates" e custo entre os parâmetros. **Ajuste em 2.1-a**: o teste de Cria passa a ser "deixaria de existir, ou se tornaria irrelevante, sem o insumo". Resolve T03-F06 quando aplicado |
| 2.2-d | **Aprovado** | Para Hospeda, a via é a affordance que oferece a ocasião. Vale para os 39 (passo 5.3) e para os novos (passo 4.3) |
| 2.2-e | **Aprovado** | Uniformizar *create* (Introdução, 2.1, Tabela 5) na T03.8 |

**Fora deste passo**: a atenuação. Nem a 2.1 nem a 6.1 dizem que a plataforma também pode atenuar
um mecanismo. Isso entra no passo 2.4 (direção da evidência) e talvez numa frase na 2.1, a decidir
lá.

### 6.6 Passo 2.3 — A discussão induzido × hospedado × mitigado: o que vai para o paper (2026-10-18)

**Base**: os pontos (1) a (4) de 6.3, revistos depois dos passos 2.1 e 2.2, e o texto atual da
cópia de revisão (leitura somente, 2026-10-18).

**O que o paper já diz** (fatos):
- **Bail et al. [84]** já é citado duas vezes: na 7.1, em AF3 ("In a randomized field experiment,
  Bail et al. [84] showed that exposing participants to accounts from the opposing political
  spe[ctrum]…"), e na 7.3, como exemplo de "field studies revealing counter-intuitive directional
  effects".
- **5.2**: o *feedback loop* liga "the outcomes layer back to the 'Features' layer", com três
  pontos de fechamento (D5 → AF2, E1 → AF1, D3/D4 → AF4).
- **9.2, terceira limitação**: menciona "self-report and reverse-causality limitations" a propósito
  de B7.
- **9.2, quarta limitação**: as ligações affordance → mecanismo "denote enabling conditions rather
  than deterministic triggers".
- Nada no texto diz que a mesma affordance pode **atenuar** um mecanismo, nem que os mecanismos
  têm **vias fora da plataforma**.

**Situação dos pontos de 6.3**:

| Ponto de 6.3 | Situação depois dos passos 2.1 e 2.2 |
|---|---|
| (1) O vínculo com a mídia social não era verificado | **Resolvido**: Q5 = procedimento da 6.1, com via obrigatória (2.1, 2.2). No paper, só muda o texto da 6.1 (passo 8.3) |
| (2) Os mecanismos têm outras vias além da plataforma | **Aberto**: itens 2.3-b a 2.3-d |
| (3) A plataforma hospeda, amplifica e também atenua | **Aberto**: itens 2.3-e e 2.3-f |
| (4) Implicações (inclusão, itens Hosts, *Claim*, sinal das ligações, título) | Inclusão e Hosts **resolvidos** (2.1-d, 2.2-a); título **resolvido** (a 2.1 já diz "create, amplify, or host"); *Claim* em duas dimensões e sinal das ligações ficam para o **passo 2.4** e o **passo 4.3** |

**Itens para aprovação** (o texto em inglês é redigido na T03.8, passo 8.5):

| Item | Proposta | Onde no paper | Fontes (corpus L entre os 147 incluídos, salvo indicação) | Recomendação |
|---|---|---|---|---|
| **2.3-a** Uma subseção própria | A discussão ganha um lugar só seu: uma subseção curta na Seção 9 (Discussion), com título provisório *What platforms do to mechanisms: create, amplify, host, or attenuate*. Ela resume a distribuição dos valores de *Claim* (depois da T03.5) e reúne os itens 2.3-b, 2.3-e e 2.3-f. Os demais pontos do paper (6.1, 5.2, 9.2) recebem só remissões ou uma frase | nova 9.x (ou dentro da 9.1) | — | Aprovar: atende ao "não quero perder essa discussão" sem espalhá-la em vários lugares |
| **2.3-b** Outras vias (equifinalidade) | Dizer que a maioria dos mecanismos também opera por vias fora da plataforma (mídia partidária, elites, redes presenciais, segregação residencial) e que *Claim* mede a **contribuição da plataforma** em relação a essas vias. Por isso, observar um mecanismo na plataforma não prova que ela o causou | 9.x; uma frase na 6.1 | Masip et al. 2020 (seletividade alta já no consumo offline, p. 53); Tonin et al. 2025 (segregação offline maior que a online, p. 1); Fletcher et al. 2021 (mais gente sem notícias online do que em câmaras de eco partidárias, p. 1) | Aprovar |
| **2.3-c** O que a plataforma acrescenta, em cada definição | O passo (ii) do modelo de definição da T02 (§12.3, "o que a plataforma muda") passa a ser **obrigatório**: nos mecanismos novos (passo 8.2) e na conferência dos 39 (passo 5.3) | fichas da Seção 6 | — | Aprovar |
| **2.3-d** Ponte com o jornalismo | O jornalismo é uma das vias fora da plataforma e, ao mesmo tempo, um produtor que atua dentro dela (E3, G1, C5, C7). Um parágrafo na 10.2 liga a equifinalidade às implicações para redações | 10.2 | — (mecanismos da lista atual) | Aprovar; decidir a extensão no passo 8.5 |
| **2.3-e** Sinais opostos e mitigação | Generalizar o que hoje aparece só com Bail [84]: a mesma affordance pode atenuar um mecanismo e ativar outro, e uma intervenção que mitiga um mecanismo pode ativar outro. Exemplos: a personalização algorítmica que, em certas condições, reduz a segregação; a exposição ao outro lado que reduz a câmara de eco e pode produzir *backfire* (K11). Liga a discussão à Tabela 6 (intervenções) e ao sinal das ligações (passo 2.4) | 9.x; frase na quarta limitação da 9.2 | Törnberg 2026 (p. 1); Masip et al. 2020 (p. 53); Bail et al. [84], já na lista do paper | Aprovar |
| **2.3-f** Causalidade reversa | A polarização também leva ao uso de mídia social, e não só o contrário. Isso amplia o *feedback loop*: além de fechar em features (5.2), ele fecha pelo **uso**, que a própria 2.1 inclui na definição ("design, usage, and governance"). Também reforça a limitação de desenho da 9.2 | 9.x; uma frase na 5.2; terceira limitação da 9.2 | Nordbrandt 2021 (p. 3392) | Aprovar |

**Referências novas** que estes itens trazem: Törnberg 2026, Masip et al. 2020, Tonin et al. 2025,
Fletcher et al. 2021 e Nordbrandt 2021. Todas estão entre os 147 incluídos e tiveram a primeira
página conferida no PDF (T03-F03). Entram na lista do paper com BibTeX via Crossref (G1), no passo
7.5.

**Decisões do usuário — passo 2.3 (2026-10-18)**: **2.3-a a 2.3-f aprovados**, como recomendado.
Efeito: subseção nova na Seção 9 sobre o que as plataformas fazem com os mecanismos (criar,
amplificar, hospedar, atenuar), com frases de remissão na 6.1, na 5.2 e na 9.2 e um parágrafo na
10.2. O passo (ii) do modelo de definição passa a ser obrigatório. Texto na T03.8 (passos 8.2, 8.5).

### 6.7 Passo 2.4 — A coluna *Claim* em duas dimensões e o destino de *Mixed* (2026-10-18)

**Ponto de partida**: o passo 2.1 decidiu que *Claim* registra só o **papel** da plataforma
(Creates / Amplifies / Hosts, valor único) e que *Evidence* mede a **força** da evidência do papel
da plataforma, com teto pelo desenho do estudo. Falta decidir onde fica a **direção** da evidência
(a plataforma reforça ou atenua o mecanismo?), que hoje aparece misturada à força como *Mixed*.

**Fato — os valores atuais da tabela consolidada** (6.11, conforme `adjustments/T02-ajustes.md`):
- *Evidence* = **Mixed** em 8 dos 39: A1, A3, B2, C3, D5, F1, G3, G4;
- *Evidence* **composta** em 7: A2 ("Moderate–mixed"), B1 ("Strong (existence), moderate (platform
  role)"), B3 ("Strong (lab), moderate (online)"), C1 ("Strong (phenomenon), magnitude debated"),
  C2 ("Strong (phenomenon), weak (induced)"), D6 ("Strong (phenomenon), moderate (platforms)") e
  G2 ("Moderate (strong in the U.S.)");
- *Claim* **composta** em 8: B1, C3, C7, D3, D4 ("Hosts & amplifies"), B6 ("Hosts (amplifies)"),
  E3 ("Creates (incentive)") e G4 ("Amplifies or hosts").

Ou seja, 20 dos 39 itens (A2, B1, B3, C1, C2, D6, G2 e os oito *Mixed*, mais B6, C7, D3, D4, E3)
têm algum valor que mistura dimensões. *Mixed* hoje quer dizer "achados conflitantes entre
estudos" (6.1), o que é **direção**, e não força.

**Itens para aprovação**:

| Item | Proposta | Recomendação |
|---|---|---|
| **2.4-a** Coluna nova *Direction* | A tabela consolidada ganha uma coluna para a direção da evidência sobre o papel da plataforma, com três valores: **Reinforcing** (os estudos indicam que a plataforma aumenta o efeito do mecanismo sobre a polarização) · **Mixed** (há achados em sentidos opostos, ou achados nulos ao lado de positivos) · **Attenuating** (os estudos indicam que a plataforma reduz o efeito). A tabela fica com sete colunas: ID, Mechanism, Outcome, Claim, Direction, Evidence, Ref | Aprovar |
| **2.4-b** *Mixed* muda de coluna | *Mixed* sai de *Evidence* (que fica com Strong / Moderate / Plausible, pelo teto do passo 2.1-e) e passa a ser um valor de *Direction*. Os oito itens hoje *Mixed* ficam com *Direction* = Mixed e recebem uma força de evidência pelo desenho do estudo mais forte (passo 5.3). Os valores compostos de *Evidence* se resolvem pelo 2.1-e: a parte "phenomenon/existence/lab" vai para a definição, e a coluna fica com a parte "platform role/online/induced". Exemplo: C2 "Strong (phenomenon), weak (induced)" → *Evidence* = Plausible | Aprovar |
| **2.4-c** Nomes das colunas | Renomear *Claim* para **Platform role** e *Evidence* para **Evidence strength**. "Claim" não diz ao leitor do que se trata, e as duas colunas novas ficam autoexplicativas. Custo: trocar os nomes na 6.1, na 9.1, na 9.2 e na legenda (passo 8.6) | Aprovar. Se preferir não mexer nos nomes, a alternativa é manter *Claim* e explicar na legenda |
| **2.4-d** Ligações com sinal | Nas ligações affordance → mecanismo (7.1, Tabela 6, Figuras 5–15), o padrão continua "+" (a affordance alimenta o mecanismo). **Marcar "−" ou "±" só onde houver fonte** (ex.: AF1 → B2 com Törnberg 2026, condicional; AF3 → K11 com Bail [84]). Feito no passo 4.3 (mecanismos novos) e no passo 5.3 (os 39) | Aprovar |
| **2.4-e** Atenuação no texto | Uma frase no parágrafo de *Claim* da 6.1: os mesmos elementos de design que criam, amplificam ou hospedam um mecanismo podem atenuá-lo, que é a premissa das intervenções da Tabela 6. **A definição de SMIP da 2.1 não muda**: ela trata dos processos de divisão, e a atenuação não é um deles. Remissão para a subseção nova da Seção 9 (2.3-a) | Aprovar |
| **2.4-f** Fonte da direção para os 39 | A direção dos 39 vem das fontes já citadas nas fichas e da evidência contrária do segundo levantamento (T03-I05: Fletcher et al. 2021, Dubois e Blank 2018, Geiß et al. 2021, Liu et al. 2025 para B2 e A1). **Atenção**: citar o corpus L nas fichas dos 39 combina as duas listas, o que é a lógica da Opção C (D1), ainda não decidida. Se D1 for outra, a direção dos 39 se apoia só nas fontes atuais | Aprovar condicionado a D1 = C, ou decidir já a D1 |

**Efeito na D4**: com 2.1 (papel e força), 2.2 (procedimento único) e 2.4 (direção), a régua fica
fechada e a D4 pode ser registrada como decidida.

**Decisões do usuário — passo 2.4 (2026-10-18)**: **2.4-a a 2.4-f aprovados**. Em 2.4-f, o usuário
decidiu a **D1: Opção C** (dupla origem declarada), o que fecha o passo 6.1 antecipadamente e
permite citar a evidência do segundo levantamento nas fichas dos 39. **D4 decidida**: régua
completa. Tabela consolidada com sete colunas (ID, Mechanism, Outcome, Platform role, Direction,
Evidence strength, Ref). **T03.2 concluída.**

---

## 7. T03.3 (passo 3.1) — Inventário e agrupamento das entradas brutas

ID bruto = lote + número no arquivo (L4a = lote 4, parte 1; L4b = parte 2). "Papers" = número
de papers citados pela IA como evidência (não verificado, T03-F03). "Unidade" = destino na
consolidação (Seção 8).

| ID bruto | Nome no arquivo | Papers | Unidade |
|---|---|---|---|
| L1-01 | Reestruturação homofílica da rede (*homophilic rewiring*) | 7 | K03 (formação) + K04 (dissolução) |
| L1-02 | Assimilação viesada e raciocínio motivado | 6 | K15 + K14 |
| L1-03 | Reação repulsiva / efeito *backfire* | 7 | K11 |
| L1-04 | Reforço social interativo em grupo (*group polarization*) | 5 | K06 |
| L1-05 | Otimização de utilidade entre autenticidade e aversão à extremidade | 1 | K25 |
| L1-06 | Filtragem e recomendação algorítmica de conteúdo | 5 | K01 |
| L1-07 | Recomendação de conexões por similaridade estrutural | 1 | K03 |
| L1-08 | Cascata de saída por limiar de insatisfação local | 1 | K04 |
| L1-09 | Acoplamento inter-tópico | 3 | K09 |
| L1-10 | Rejeição e substituição de sinais por viés de confirmação | 1 | K15 |
| L1-11 | Espiral de reforço cumulativo de mídia e rede (RSM) | 1 | K19 |
| L1-12 | Difusão afetiva por contágio moral-emocional | 2 | K07 |
| L1-13 | Confiança limitada com zonas de repulsão | 3 | K10 |
| L1-14 | Fusão de identidade social e transição de regime | 2 | K08 |
| L2-01 | Homofilia de rede e conexão seletiva | 8 | K03 + K04 (revisto em 7.2) |
| L2-02 | Exposição seletiva e viés de confirmação | 8 | K12 |
| L2-03 | Dinâmica de câmara de eco | 11 | K05 |
| L2-04 | Retroalimentação algorítmica de bolha de filtro | 7 | K01 |
| L2-05 | Efeito ricochete (*backfire*) | 4 | K11 |
| L2-06 | Diferenciação e repulsão interpessoal | 4 | K10 |
| L2-07 | Ordenamento partidário (*partisan sorting*) | 3 | K08 |
| L2-08 | Conformidade intragrupo e anticonformidade intergrupos | 2 | K10 |
| L2-09 | Cascata por animosidade ao exogrupo e linguagem moral-emocional | 4 | K07 (revisto em 7.2) |
| L2-10 | Sobrecarga cognitiva e processamento heurístico | 4 | K18 |
| L2-11 | Pensamento de grupo em grupos homogêneos | 2 | K06 |
| L3-01 | Homofilia e exposição seletiva | 18 | K03 + K12 |
| L3-02 | Câmaras de eco | 23 | K05 |
| L3-03 | Bolha de filtro algorítmica | 15 | K01 |
| L3-04 | Desconexão seletiva (*unfollowing*) | 5 | K04 |
| L3-05 | Influência social de limiar e conformidade intragrupal | 7 | K05 |
| L3-06 | Anticonformidade e animosidade ao out-group | 4 | K10 |
| L3-07 | Raciocínio motivado e *backfire* | 5 | K11 + K14 |
| L3-08 | Viés de confirmação no sistema de recompensa | 1 | K20 |
| L3-09 | Contágio moral-emocional e indignação | 6 | K07 |
| L3-10 | Percepção de normas intragrupais | 1 | K26 → evidência para D4 (7.3) |
| L3-11 | Ordenamento partidário e social | 5 | K08 |
| L3-12 | Equilíbrio social em redes valoradas | 1 | K10 |
| L3-13 | Ciclo de baixa tolerância e retaliação (denúncias) | 1 | K32 |
| L3-14 | Efeito terceira pessoa e ação corretiva | 1 | K29 |
| L3-15 | Narrativas concorrentes | 2 | K24 |
| L3-16 | Centralidade estrutural e bloqueio de consenso | 4 | K33 |
| L3-17 | Reatância opinativa e espiral anti-silêncio | 1 | K28 |
| L4a-01 | Exposição seletiva partidária | 8 | K12 |
| L4a-02 | Esquiva seletiva e bloqueio partidário | 3 | K13 + K04 |
| L4a-03 | Homofilia afetiva e estrutural | 7 | K03 |
| L4a-04 | Retroalimentação algorítmica de personalização | 8 | K01 |
| L4a-05 | Reforço em câmaras de eco | 7 | K05 |
| L4a-06 | Espiral do silêncio e feedback social | 4 | K27 |
| L4a-07 | Assimilação viesada e raciocínio motivado | 6 | K15 + K14 |
| L4a-08 | Modulação afetiva e provocação partidária | 5 | K07 |
| L4a-09 | Engajamento seletivo partidário e sinalização | 2 | K31 |
| L4a-10 | Confiança limitada e julgamento social | 5 | K05 (assimilação) + K10 (contraste) |
| L4a-11 | Inércia cética | 1 | K23 |
| L4a-12 | Efeito de ordem e preferência por crença | 2 | K22 |
| L4a-13 | Amplificação por usuários prioritários | 1 | K33 |
| L4a-14 | Rejeição reativa e *backfire* por exposição cruzada | 4 | K11 |
| L4b-01 | Aprendizado por reforço via feedback social assimétrico | 3 | K30 |
| L4b-02 | Amostragem sequencial e truncamento | 1 | K21, candidato fraco (reteste em 7.5) |
| L4b-03 | Redução de dissonância em sistemas de crenças | 4 | K16 |
| L4b-04 | Exposição seletiva, evitação seletiva e bloqueio ativo | 8 | K12 + K13 + K04 |
| L4b-05 | Assimilação viesada e *backfire* | 6 | K15 + K11 |
| L4b-06 | Raciocínio politicamente motivado | 2 | K14 |
| L4b-07 | Contágio emocional e fronteiras de identidade | 5 | K07 |
| L4b-08 | Loop algorítmico de otimização de engajamento | 6 | K02 |
| L4b-09 | Exposição repetida e verdade ilusória | 1 | K17 |
| L4b-10 | *Echoing* e validação intragrupal | 4 | K05 + K06 |

**Leitura**: metade das 66 entradas (33) são variações de oito processos (homofilia,
exposição seletiva, câmara de eco, bolha de filtro, *backfire*, contágio moral, assimilação
enviesada, *sorting*). Muitos nomes juntam dois construtos com "e" (ex.: L1-02, L3-07, L4b-04), contra
a R5. A saída por lote não deduplicou entre lotes: o mesmo processo recebe nomes diferentes em
cada arquivo.

*Coluna "Unidade" atualizada em 2026-10-18 com as decisões do passo 3.1 (7.1–7.5).*

### 7.1 Passo 3.1, lote L1 — itens para aprovação (2026-10-18)

Régua: Q1–Q4 (6.1), Q5 com os passos 2.1 e 2.2 e as regras R5 (um nome, um construto) e R6
(construtos vizinhos não são sinônimos). As atribuições de papers continuam **[a verificar]** na
T03.7, exceto Törnberg 2026, conferido no PDF.

| Entrada | Nome no arquivo | Destino | Por quê | Observação |
|---|---|---|---|---|
| L1-01 | Reestruturação homofílica da rede (*homophilic rewiring*) | **K03** (formação de laços) + **K04** (dissolução) | O nome junta dois processos (R5). No arquivo, o passo 2 ("desvinculação/unfollow de pares divergentes") é dissolução, e o passo 3 ("criação de novos laços homogêneos") é formação | Törnberg 2026, citado aqui, mostra segregação "without users preferring homogeneous environments" (p. 1). A contribuição dele é para K04 (saída em cascata), e **não** para a homofilia |
| L1-02 | Assimilação viesada e raciocínio motivado | **K15** + **K14** | Dois construtos (R5). Os passos 2 e 3 (aceitar o congruente, hipercriticar o contrário) são assimilação enviesada. O motor é o raciocínio motivado. É a fronteira já fixada na T02 (D26) | — |
| L1-03 | Reação repulsiva / efeito *backfire* | **K11** | O passo 3, "atualização da opinião no sentido oposto" à mensagem do out-group, é o *backfire* | Entre os 7 papers citados há simulações de repulsão entre agentes (ex.: Noorazar et al. 2018), que pertencem a K10. Separar na T03.7. Karlsen et al. 2017 (*trench warfare*) parece o mais próximo do *backfire*, pelo título |
| L1-04 | Reforço social interativo em grupo (*group polarization*) | **K06** | Deslocamento da média do grupo para o extremo depois da troca de argumentos é a definição de polarização de grupo | — |
| L1-05 | Otimização de utilidade entre autenticidade e aversão à extremidade | **K25** → evidência para o bloco D (não é item próprio) | É a calibração da opinião expressa pela norma local percebida: vizinho de D3, D4 e D5. Uma fonte só (Brown et al. 2022) | — |
| L1-06 | Filtragem e recomendação algorítmica de conteúdo | **K01** | Os passos 2 ("ocultação/atenuação de divergências") e 3 ("amostragem afunilada") são a bolha de filtro | O passo 1 ("cálculo do potencial de engajamento") toca K02. Se as fontes tratarem de amplificação por engajamento, elas vão para K02 na T03.7 |
| L1-07 | Recomendação de conexões por similaridade estrutural | **K03** | É a via algorítmica da homofilia (AF2). Mesma solução da T02 (D21: A3 fundido em B1) | Santos et al. 2021 já está na lista do paper ([59]) |
| L1-08 | Cascata de saída por limiar de insatisfação local | **K04** | Saída de comunidades é dissolução de laços no nível do grupo | Única fonte: Törnberg 2026 (p. 1) |
| L1-09 | Acoplamento inter-tópico | **K09** → definição de K08 (não é item próprio) | Q3: o alinhamento de temas é o próprio outcome ideológico. Só simulações | — |
| L1-10 | Rejeição e substituição de sinais por viés de confirmação | **K15** | Rejeitar o sinal incongruente e trocá-lo por uma fonte preferida é assimilação enviesada, num modelo de rede (Sikder et al. 2020) | — |
| L1-11 | Espiral de reforço cumulativo de mídia e rede (RSM) | **K19** → situação de C8 (não é item próprio) | Guarda-chuva (Q2), o mesmo diagnóstico de M6/C8 na T02 | Ohme 2021 alimenta o B02 (T03-I01) |
| L1-12 | Difusão afetiva por contágio moral-emocional | **K07** | Linguagem moral-emocional → mais atenção e repasse → escalada do desprezo ao out-group | — |
| L1-13 | Confiança limitada com zonas de repulsão e contraste | **K10** | A repulsão em distâncias longas é influência social negativa. A assimilação em distâncias curtas, sozinha, não produz polarização | Com o passo 2.2-a, K10 entra (Hospeda conta) |
| L1-14 | Fusão de identidade social e transição de regime | **K08** | O passo 2, "alinhamento (*sorting*) de múltiplas identidades ao partido", é o *sorting* | O *tipping point* é propriedade do modelo, e não etapa do mecanismo |

**Resumo do L1**: 14 entradas → 11 vão para unidades que entram (K01, K03, K04, K06, K07, K08,
K10, K11, K14, K15). As outras 3 vão para unidades que não entram como item próprio (K09, K19,
K25). Duas entradas se dividem (L1-01, L1-02).

**Decisão do usuário — lote L1 (2026-10-18)**: **aprovado** como na tabela.

### 7.2 Passo 3.1, lote L2 — itens para aprovação (2026-10-18)

Duas entradas mudam de destino em relação ao inventário preliminar (Seção 7): **L2-01** passa a
dividir-se como L1-01, e **L2-09** perde a parte algorítmica, que só aparecia nas justificativas
de affordance do Gemini (T03-F04), e não nos passos do mecanismo.

| Entrada | Nome no arquivo | Destino | Por quê | Observação |
|---|---|---|---|---|
| L2-01 | Homofilia de rede e conexão seletiva (*social network homophily & assortative rewiring*) | **K03** + **K04** (**mudou**: era só K03) | O passo 2 junta "estabelece laços com pares congruentes (homofilia)" e "reconecta conexões (*rewiring*) eliminando divergentes": formação e dissolução, como em L1-01 | Bail et al. 2018 ([84]) aparece aqui, mas o PDF trata de exposição ao outro lado e *backfire* (K11) |
| L2-02 | Exposição seletiva e viés de confirmação | **K12** | *Selective exposure* é o alternativo de *confirmation bias* na etapa de busca, como já decidido na T02 (C2, D26 e D35) | O passo 3 ("rejeição de evidências contrárias") é assimilação enviesada (K15). A conferência dos papers (T03.7) diz qual das duas eles sustentam |
| L2-03 | Dinâmica de câmara de eco e retroalimentação endógena | **K05** | Circulação repetida entre pares homogêneos, sem contestação → reforço → dois polos | O passo 3 cita "contágio emocional", que é K07. Entre os 11 papers, Törnberg 2018 (*Echo chambers and viral misinformation: modeling fake news as complex contagion*) toca também as cascatas (B4) |
| L2-04 | Retroalimentação algorítmica de bolha de filtro | **K01** | Perfil de preferência → filtragem do discordante → consumo → novo sinal que estreita o modelo | Liu et al. 2025, citado aqui, encontra efeito limitado (p. 1): é evidência para *Direction* = Mixed |
| L2-05 | Efeito ricochete por raciocínio motivado contraditório | **K11** | Mensagem contra-atitudinal → defesa → posição mais extrema no sentido oposto = *backfire*. O raciocínio motivado (K14) é o motor e entra na definição, como na T02 (C1) | Bail et al. 2018 é a evidência mais direta (p. 1) |
| L2-06 | Diferenciação e repulsão interpessoal | **K10** | Distância acima do limiar de tolerância → força negativa → afastamento = influência social negativa | Quatro simulações |
| L2-07 | Ordenamento partidário global e alinhamento de *cleavages* | **K08** | Interações não locais → alinhamento de atributos à identidade partidária → perda de *cross-cutting cleavages* | É a via de plataforma mais explícita de K08 (Q5 = Amplifica, AF2). Törnberg 2022 é a fonte central, pelo título |
| L2-08 | Conformidade intragrupo e anticonformidade intergrupos | **K10** | O que produz a bipolarização é a anticonformidade ao out-group. A conformidade intragrupo é a parte assimilativa, que sozinha não polariza (mesma lógica de L1-13) | — |
| L2-09 | Cascata por animosidade ao exogrupo e linguagem moral-emocional | **K07** (**mudou**: saiu a parte "+ K02") | Os três passos são emoção → repasse → retaliação, sem etapa algorítmica. A amplificação pelo algoritmo só aparece na justificativa de affordance do Gemini | A ligação com AF1 pode voltar no passo 4.3, com fonte |
| L2-10 | Sobrecarga cognitiva e processamento heurístico | **K18** | Volume e velocidade → sobrecarga da memória de trabalho → processamento heurístico → aceitação acrítica do congruente | Dos 4 papers, só Du et al. 2025 (EEG com vídeos curtos) parece tratar disso. Edinger et al. 2025 (*Cognitive distortions…*) e Clemons et al. 2025 (*Managing disinformation…*) parecem de outro tema, pelo título **[a verificar]**. Se só restar Du, K18 fica com uma fonte |
| L2-11 | Pensamento de grupo e falha de correção factual em grupos homogêneos | **K06** | Deliberação entre semelhantes → só argumentos congruentes → deslocamento para o extremo = polarização de grupo. *Groupthink* (coesão que inibe a crítica) é construto vizinho e **não** vira alternativo (R6) | Sobeh et al. 2025 trata de um fator que **mitiga** o extremismo em câmaras de eco, pelo título: evidência de atenuação, e não de reforço |

**Resumo do L2**: as 11 entradas vão para unidades que entram (K01, K03, K04, K05, K06, K07, K08,
K10, K11, K12, K18). Nenhuma vai para unidade que não entra. Uma se divide (L2-01).

**Decisão do usuário — lote L2 (2026-10-18)**: **aprovado** como na tabela.

### 7.3 Passo 3.1, lote L3 — itens para aprovação (2026-10-18)

**Reteste depois do passo 2.2.** K20 e K24 tinham sido excluídos por Q5 = "nenhuma via" (8.2),
antes de se decidir que Hospeda conta. Com a regra 2.2-d (para Hospeda, a via é a affordance que
oferece a ocasião), o teste foi refeito:
- **K20** (L3-08) continua sem via. A ocasião do processo é fazer escolhas e receber o resultado
  delas, o que qualquer ambiente oferece. Nenhuma affordance a fornece em particular, e a fonte
  mostra o processo sem interação social. O análogo de plataforma é K30 (reforço pelo feedback
  social), que já entra;
- **K24** (L3-15) agora tem via de Hospeda (o feed entrega narrativas, AF1). A exclusão passa a se
  apoiar em **sobreposição** (R6): narrativas concorrentes só polarizam quando a exposição é
  segmentada, e a segmentação já é K12 (busca seletiva) e K01 (bolha de filtro). O efeito de cada
  narrativa sobre a atribuição de causa é enquadramento, que entra na definição de K12.

| Entrada | Nome no arquivo | Destino | Por quê | Observação |
|---|---|---|---|---|
| L3-01 | Homofilia e exposição seletiva atitudinal | **K03** + **K12** | Dois construtos (R5): buscar **pares** alinhados (homofilia) e buscar **conteúdo** alinhado (busca seletiva). "Evitando ou rejeitando fontes dissonantes" toca K13 | 18 papers, entre eles Nordbrandt 2021, que não encontra efeito do uso sobre a polarização afetiva (p. 3392). Cita van Baar e FeldmanHall 2021, cujo PDF está na pasta do L2 |
| L3-02 | Dinâmica de reforço em câmaras de eco | **K05** | Circulação repetida entre pares homogêneos → validação → certeza → blocos distanciados | 23 papers, o maior conjunto do corpus. Vários tratam de detecção ou medição de câmaras de eco (ex.: Villa et al. 2021, *Echo chamber detection and analysis*), e não do processo |
| L3-03 | Personalização e filtragem algorítmica | **K01** | Histórico → entrega do concordante e ocultação do *cross-cutting* | — |
| L3-04 | Reconfiguração da rede por desconexão seletiva (*unfollowing*) | **K04** | Atrito com um laço divergente → corte (*unfollow*, *unfriend*) → perda de pontes | Sasahara et al. 2020 (*Social influence and unfollowing accelerate the emergence of echo chambers*) é a fonte mais direta, pelo título |
| L3-05 | Influência social de limiar e conformidade intragrupal | **K05** | A assimilação entre pares próximos produz núcleos homogêneos: é o reforço intragrupo da câmara de eco. Sozinha, não é mecanismo de polarização à parte (mesma lógica de L1-13 e L2-08) | You e Lee 2024, citado aqui, trata de norma percebida (vai para L3-10). Wesemael et al. 2026 está na pasta do L2 |
| L3-06 | Oposição por anticonformidade e animosidade ao out-group | **K10** | Rejeição sistemática da posição do out-group → repulsão mútua | — |
| L3-07 | Raciocínio motivado e efeito tiro pela culatra | **K11** + **K14** | O *backfire* é o resultado (inversão da posição). O raciocínio motivado é o motor. Ficam nas duas unidades, com a fronteira de L2-05 | Nordbrandt 2021 citado de novo como apoio; ver T03-F03 |
| L3-08 | Viés de confirmação no sistema de recompensa individual | **K20** → não entra | Reteste acima: continua sem via de plataforma | Lefebvre et al. 2024 fica fora da síntese, salvo se citado em outra unidade (está em L3-02 e L3-03, então continua incluído) |
| L3-09 | Difusão por contágio moral-emocional e indignação | **K07** | Conteúdo indignado → atenção e reação → mais compartilhamento → antagonismo | — |
| L3-10 | Assimilação por percepção de normas intragrupais | **K26** → evidência para **D4** (ignorância pluralística) | O processo é: superestimar a hostilidade que o próprio grupo aprova → conformar-se a ela. É o desenho da ignorância pluralística (D4), aplicado à hostilidade ao out-group. Uma fonte | Encaixe a confirmar no PDF de You e Lee 2024 (T03.7). Alternativa: D6 (metapercepções) |
| L3-11 | Ordenamento partidário e integração social | **K08** | Alinhamento de identidades sociais ao eixo político → perda de laços cruzados | — |
| L3-12 | Equilíbrio social em redes valoradas | **K10** | Resolver tríades instáveis (amigo do inimigo) → a rede se divide em dois blocos antagônicos. Equilíbrio estrutural é uma das formas de influência negativa listadas na definição de K10 | Uma simulação (Thurner et al. 2025) |
| L3-13 | Espiral de baixa tolerância e retaliação | **K32** | Denúncias de uma fração dos usuários → retaliação com a mesma ferramenta → equilíbrio de intolerância mútua | Candidato novo (passo 3.3). Uma fonte, um modelo, e o título diz "A potential mechanism" |
| L3-14 | Efeito terceira pessoa e ação corretiva | **K29** | Perceber que a desinformação afeta mais os outros → ação corretiva (censura, ataques, denúncias) | Candidato novo (passo 3.3). Uma fonte (Yang e Tian 2021) |
| L3-15 | Polarização por narrativas concorrentes | **K24** → não entra | Reteste acima: passa em Q5 como Hospeda, mas se sobrepõe a K12 e K01 (R6) | **Motivo de exclusão mudou** em relação a 8.2 |
| L3-16 | Centralidade estrutural e bloqueio de consenso | **K33** → não entra (decisão no passo 3.4) | Q4: *hubs* e líderes de opinião são atores ou estrutura | No passo 3.4 há a alternativa de reformular K33 no bloco A, com L4a-13 |
| L3-17 | Reatância opinativa e espiral anti-silêncio | **K28** → condição de contorno de **D5** (espiral do silêncio) | Descreve quando a espiral do silêncio se inverte: anonimato e incivilidade fazem a minoria se manifestar em vez de calar | Uma fonte (Fang et al. 2024, sobre discurso feminista em mídia social chinesa, pelo título) |

**Resumo do L3**: 12 entradas vão para unidades que entram (K01, K03, K04, K05, K07, K08, K10,
K11, K12, K14, K29, K32). As outras 5 não viram item próprio: K20 e K24 excluídas, K26 como
evidência para D4, K28 como condição de D5 e K33 pendente do passo 3.4. Duas se dividem (L3-01,
L3-07).

**Decisão do usuário — lote L3 (2026-10-18)**: **aprovado** como na tabela, inclusive o reteste de
K20 e K24 e a mudança do motivo de exclusão de K24 (sobreposição, e não falta de via).

### 7.4 Passo 3.1, lote L4a — itens para aprovação (2026-10-18)

| Entrada | Nome no arquivo | Destino | Por quê | Observação |
|---|---|---|---|---|
| L4a-01 | Exposição seletiva partidária | **K12** | Ambiente de alta escolha → seleção do congruente para evitar dissonância → reforço da opinião | Fletcher et al. 2021, citado aqui, mostra que só cerca de 5% vivem em câmaras de eco partidárias (p. 1): evidência para *Direction* = Mixed |
| L4a-02 | Esquiva seletiva e bloqueio partidário | **K04** + **K13** | O núcleo é **cortar o laço** (bloquear, deixar de seguir) com contatos dissimilares: K04. A esquiva do conteúdo é K13 | Kaiser et al. 2022 (*Partisan Blocking*) é a fonte mais direta de K04, pelo título. Kim et al. 2025 trata de rótulos de desinformação e parece pertencer a K11 |
| L4a-03 | Homofilia afetiva e estrutural | **K03** | Atração por semelhança de atitude **ou de afeto** → laços intragrupo → clusters isolados. A homofilia afetiva é uma variante da base da semelhança, e não outro processo | Gu et al. 2025 (*Affective homophily as the dominant organizing principle in online conflict*) |
| L4a-04 | Amplificação e retroalimentação algorítmica de personalização | **K01** | Preferências → personalização → menos discordância → extremização | Cho et al. 2020 (*Do search algorithms endanger democracy?*) parece experimental, pelo título: candidato a evidência forte de K01 |
| L4a-05 | Dinâmica de reforço em câmaras de eco | **K05** | Comunicação em sistema fechado → repetição sem contraponto → certeza e radicalização | Geiß et al. 2021 contesta a metáfora (p. 660). Avin et al. 2024 trata da impossibilidade de romper a câmara de eco, pelo título |
| L4a-06 | Espiral do silêncio e aprendizado por feedback social | **K27** (D5) | Clima de opinião percebido pelas reações → medo do isolamento → silêncio da minoria → distorção da opinião percebida | O nome junta espiral do silêncio e aprendizado por feedback. O aprendizado por feedback é o canal pelo qual a plataforma amplifica (AF4) e não vira outra unidade |
| L4a-07 | Assimilação viesada e raciocínio motivado | **K15** + **K14** | Mesma divisão de L1-02 | — |
| L4a-08 | Modulação afetiva e provocação partidária | **K07** | Mensagem ultrajante → raiva → compartilhamento de ataques → hostilidade ao out-group | O insumo descrito é a mídia partidária e as elites (Hasell e Weeks 2016, *Partisan Provocation*), e não a plataforma. É um exemplo da equifinalidade do item 2.3-b |
| L4a-09 | Engajamento seletivo partidário e sinalização de identidade | **K31** (E2) | Curtir, comentar e compartilhar o congruente para sinalizar lealdade → visibilidade das pautas partidárias | Garz et al. 2019 (*Partisan Selective Engagement: Evidence from Facebook*) |
| L4a-10 | Confiança limitada e julgamento social | **K05** (assimilação) + **K10** (contraste) | Dentro da "latitude de aceitação" há assimilação, que vai para K05. Além do limiar há rejeição e contraste, que é K10. Mesma divisão de L1-13 | Carpentras et al. 2022 deriva o modelo de dados experimentais. Arruda et al. 2024 é a fonte de L4a-13 |
| L4a-11 | Inércia cética | **K23** → decisão no passo 3.4 | Passa em Q1–Q4 e em Q5 (Amplifica: saturação e mistura de fontes no feed). Uma fonte qualitativa, de um país | Candidato fraco. Vizinho de G1 (declínio do *gatekeeping*) |
| L4a-12 | Efeito de ordem e preferência por crença | **K22** → decisão no passo 3.4 | A via de plataforma seria a ordem do feed (AF1). A base é filosófica e de simulação | Candidato fraco |
| L4a-13 | Amplificação por usuários prioritários e ideólogos | **K33** → decisão no passo 3.4 | Fonte única: Arruda et al. 2024 (*Echo chamber formation sharpened by priority users*). Diferente de L3-16: aqui o alcance desigual é **concedido pela plataforma** (verificação, impulsionamento: AF10, AF1) | Reforça a alternativa do passo 3.4: reformular K33 no bloco A como amplificação de contas prioritárias, em vez de tratá-lo como ator |
| L4a-14 | Rejeição reativa e *backfire* por exposição cruzada | **K11** | Mensagem contra-atitudinal ou correção vinda do out-group → reatância → recuo para posição mais extrema | Kim et al. 2025 (rótulos individuais × coletivos de desinformação) e Cole et al. 2023 (revisão) |

**Resumo do L4a**: 11 entradas vão para unidades que entram (K01, K03, K04, K05, K07, K10, K11,
K12, K13, K14, K15, K27, K31). As outras 3 (K22, K23, K33) ficam para o passo 3.4. Três se dividem
(L4a-02, L4a-07, L4a-10).

**Decisão do usuário — lote L4a (2026-10-18)**: **aprovado** como na tabela.

### 7.5 Passo 3.1, lote L4b — itens para aprovação (2026-10-18)

**Reteste de K21 depois do passo 2.2.** K21 (L4b-02) tinha sido excluído por "nenhuma via". Pela
regra 2.2-d, a via de Hospeda é a affordance que oferece a ocasião. Aqui a ocasião é receber
evidências **em sequência** e decidir quando parar, e é exatamente isso que o feed (AF1) e a
rolagem infinita (AF9) fornecem. **K21 passa a ter via (Hospeda)** e não pode mais ser excluído
por Q5. Diferente de K20, cuja ocasião é fazer qualquer escolha, o que nenhuma affordance
fornece em particular. Proposta: K21 sai de "excluído" e vai para **candidato fraco, com decisão
no passo 3.4**, ao lado de K22 e K23. Motivos para não entrar direto: uma fonte só (Kvam et al.
2022), baseada em modelo e laboratório, sem estudo em plataforma.

| Entrada | Nome no arquivo | Destino | Por quê | Observação |
|---|---|---|---|---|
| L4b-01 | Aprendizado por reforço via feedback social assimétrico | **K30** (E1) | Publicação → feedback quantitativo só positivo → reforço → discurso mais extremo para maximizar a recompensa | Konovalova et al. 2023 (*Social media feedback and extreme opinion expression*) é o caso mais claro de efeito de design do corpus |
| L4b-02 | Amostragem sequencial racional e truncamento | **K21** → candidato fraco, decisão no passo 3.4 (**mudou**: era excluído) | Reteste acima | — |
| L4b-03 | Redução de dissonância em sistemas de crenças interconectadas | **K16** → não é item próprio | Busca de coerência → atitudes empurradas para os extremos. Sobrepõe-se a K14 (raciocínio motivado) e ao alinhamento de temas (K09, dentro de K08) | Microfundamento citado nas definições de K14 e K08 |
| L4b-04 | Exposição seletiva, evitação seletiva e bloqueio ativo | **K12** + **K13** + **K04** | Três construtos num nome (R5): buscar o congruente, evitar o contrário e bloquear contas | Martel et al. 2024 (*Blocking of counter-partisan accounts drives political assortment on Twitter*) vai para K04. Masip et al. 2020, também citado, mostra exposição maior ao outro lado entre usuários ativos (p. 53): evidência de atenuação para K12 |
| L4b-05 | Assimilação viesada e efeito rebote / *backfire* | **K15** + **K11** | Escrutínio hipercrítico do contrário (K15) e inversão da posição (K11), como em L1-02 e L2-05 | — |
| L4b-06 | Raciocínio politicamente motivado (PMR) | **K14** | A meta passa da verdade para o pertencimento ao grupo → filtragem pela norma do grupo | Sultan et al. 2024 é meta-análise sobre suscetibilidade à desinformação, pelo título |
| L4b-07 | Contágio emocional e fortalecimento de fronteiras de identidade social | **K07** | Conteúdo moral-emocional → transmissão afetiva → fronteira "nós × eles" → derrogação do out-group. O reforço de fronteiras é o efeito afetivo, e não outro mecanismo | Xu et al. 2026 (*…Consumer Perception of New…*) parece fora do tema, pelo título **[a verificar]** |
| L4b-08 | Loop de reforço algorítmico por otimização de engajamento | **K02** (A2) | Engajamento com o inflamado → o ranking prioriza → as vozes moderadas perdem visibilidade → retroalimentação | É a única entrada do corpus que tem K02 como destino principal |
| L4b-09 | Exposição repetida e fluência de processamento (verdade ilusória) | **K17** (C6) | Repetição → fluência → fluência tomada como sinal de verdade | Uma fonte (Secară e Opre 2026, experimento) |
| L4b-10 | Amplificação por *echoing* e validação intragrupal | **K05** + **K06** | A reiteração entre semelhantes é a câmara de eco (K05). O deslocamento para além da média do grupo é polarização de grupo (K06) | Mølmen e Ravndal 2021 (*Mechanisms of online radicalisation*) e O'Hara e Stevens 2015 tratam de radicalização: relevantes também para B8 da lista atual (Seção 10) |

**Resumo do L4b**: 8 entradas vão para unidades que entram (K02, K04, K05, K06, K07, K11, K12,
K13, K14, K15, K17, K30). L4b-02 (K21) vai para o passo 3.4 e L4b-03 (K16) não é item próprio.
Três se dividem (L4b-04, em três partes; L4b-05; L4b-10).

**Ao aprovar o L4b, o passo 3.1 se fecha** e o agente atualiza a Seção 7 (coluna "Unidade") e a
Tabela 8.1 (coluna "Entradas") com as mudanças aprovadas nos cinco lotes.

**Decisão do usuário — lote L4b (2026-10-18)**: **aprovado** como na tabela, com a mudança de K21
para candidato fraco. **Passo 3.1 concluído**: as 66 entradas têm destino aprovado. A coluna
"Unidade" da Seção 7 e as Tabelas 8.1 e 8.2 foram atualizadas em 2026-10-18.

---

## 8. T03.3 (passos 3.2–3.4) — Consolidação (preliminar)

Nomes provisórios, a conferir pela R1 (termo da fonte definidora) na T03.7. Abreviações de
affordance da T02: AF1 curadoria algorítmica · AF2 *network-informed associating* · AF3
*asymmetric following* · AF4 quantificação social · AF5 replicabilidade · AF6 segmentação de
audiência · AF7 restrição de formato · AF8 identificabilidade · AF9 rolagem infinita · AF10
governança · AF11 formação de grupos. As affordances de Q5 abaixo vêm das fontes ou da
lógica do processo, e não das justificativas da IA (T03-F04).

### 8.1 Unidades que passam e entram como mecanismos de SMIP (passos 3.2 e 3.3)

| K | Nome provisório | Entradas | Q1–Q4 | Q5: papel (via) | Q6: base predominante no corpus L | Bloco | Na T02 |
|---|---|---|---|---|---|---|---|
| K01 | Filter bubble (personalização algorítmica que estreita a exposição) | L1-06, L2-04, L3-03, L4a-04 | 🔧 o nome designa estado (o próprio lote 1 o classifica assim, p. 1). Processo: laço de personalização. Mantido o nome pela D27 | **Cria** (AF1). Direção **mista**: Liu et al. 2025 (efeito limitado, p. 1); Törnberg 2026 (pode reduzir a segregação, p. 1) | experimentos, auditorias, ABMs | A | A1 |
| K02 | Amplificação algorítmica de conteúdo emocional e divisivo | L4b-08 | ✅ | **Cria/Amplifica** (AF1) | revisão (Metzler e García 2023), simulações | A | A2 |
| K03 | Homofilia (formação de laços entre semelhantes, inclusive por recomendação de conexões) | L1-01 (parte), L1-07, L2-01 (parte), L3-01 (parte), L4a-03 | ✅ | **Hospeda e amplifica** (AF2, AF3). Tonin et al. 2025: segregação offline maior que a online (p. 1) | observacional, ABMs | B | B1 |
| **K04** | **Dissolução seletiva de laços** (*unfriending*, *unfollowing*, bloqueio partidário; saída em cascata de comunidades) | L1-01 (parte), L1-08, L2-01 (parte), L3-04, L4a-02 (parte), L4b-04 (parte) | ✅ | **Amplifica** (AF3, ferramentas de bloqueio e silenciamento; baixa o custo de cortar laços) | experimento de campo (Martel et al. 2024), experimento (Kaiser et al. 2022), ABMs (Sasahara et al. 2020; Törnberg 2026) **[a verificar]** | B | **novo** (na T02, parte de C3, D34) |
| K05 | Câmara de eco (reforço da crença por circulação repetida entre pares alinhados) | L2-03, L3-02, L3-05, L4a-05, L4a-10 (assimilação), L4b-10 (parte) | 🔧 nome de estado, mantido pela D27 | **Amplifica** (AF3, AF5, AF11). Direção **mista**: Fletcher et al. 2021 (~5%, p. 1); Dubois e Blank 2018; Geiß et al. 2021 (p. 660) | survey, observacional, ABMs | B | B2 |
| K06 | Polarização de grupo | L1-04, L2-11, L4b-10 (parte) | ✅ | **Hospeda e amplifica** (AF11). Sobeh et al. 2025, pelo título, trata de um fator que **mitiga** o extremismo em câmaras de eco | laboratório, ABMs | B | B3 |
| K07 | Contágio moral (difusão de conteúdo moral-emocional e hostil ao out-group) | L1-12, L2-09, L3-09, L4a-08, L4b-07 | ✅. "Modulação afetiva" (L4a-08) e "fronteiras identitárias" (L4b-07) são etapas do mesmo processo, e não mecanismos à parte | **Amplifica** (AF5, AF4, AF1) | observacional de plataforma | B | B5 |
| K08 | Ordenamento partidário (*partisan sorting*) | L1-14, L2-07, L3-11 | ✅ | **Amplifica** (interações não locais, AF2). Törnberg 2022, pelo título: "How digital media drive affective polarization through partisan sorting" | ABMs, observacional | B | B6 |
| **K10** | **Influência social negativa** (repulsão, diferenciação, anticonformidade ao out-group, equilíbrio estrutural) | L1-13, L2-06, L2-08, L3-06, L3-12, L4a-10 (contraste) | ✅ (processo; outcome ideological/affective). A parte assimilativa da confiança limitada vai para K05: sozinha, ela gera consenso ou fragmentação, e não polarização | **Hospeda** (AF8 torna o grupo do outro visível; AF4) | quase só ABMs (Axelrod et al. 2021; Siedlecki et al. 2016; Krueger et al. 2017; Thurner et al. 2025); Carpentras et al. 2022 deriva o modelo de dados experimentais **[a verificar]** | B | **novo** |
| **K11** | **Efeito backfire** (movimento contrário à mensagem contra-atitudinal ou à correção) | L1-03, L2-05, L3-07 (parte), L4a-14, L4b-05 (parte) | ✅. Fronteiras: K15 é avaliação diferencial; K11 é inversão. K10 é a formulação de influência social (depende do grupo da fonte); K11 é a resposta individual à mensagem | **Amplifica** (exposição incidental ao outro lado; rótulos de checagem, AF10). Evidência **mista** fora do corpus: o *backfire* replica mal **[conhecimento do agente; conferir dados bibliográficos: Wood e Porter 2019]** | experimento de campo (Bail et al. 2018, p. 1), experimento (Kim et al. 2025) | C | **novo** |
| K12 | Viés de confirmação (busca seletiva / exposição seletiva) | L2-02, L3-01 (parte), L4a-01, L4b-04 (parte) | ✅ | **Hospeda e amplifica** (ambiente de alta escolha; AF3, AF11). **Atenuação** documentada: Masip et al. 2020 (p. 53) | survey, observacional | C | C2 |
| K13 | Evitação seletiva | L4a-02 (parte), L4b-04 (parte) | ✅ | **Hospeda e amplifica** | survey | C | C3 |
| K14 | Raciocínio motivado (inclusive politicamente motivado) | L1-02 (parte), L3-07 (parte), L4a-07, L4b-06 | ✅ | **Hospeda** | meta-análise (Sultan et al. 2024), ABM | C | C1 |
| K15 | Assimilação enviesada (viés de desconfirmação) | L1-02, L1-10, L4a-07, L4b-05 | ✅ | **Hospeda** | ABMs, experimentos | C | C4 |
| K17 | Efeito de verdade ilusória | L4b-09 | ✅ | **Amplifica** (repetição por AF5 e AF1) | um experimento (Secară e Opre 2026) | C | C6 |
| **K18** | **Sobrecarga cognitiva e processamento heurístico** | L2-10 | ✅ | **Amplifica** (vídeos curtos, AF9, AF7). Específico de formato | EEG com vídeos curtos (Du et al. 2025); os outros três papers citados parecem tratar de outro tema, pelo título (Edinger et al. 2025, distorções cognitivas; Clemons et al. 2025, gestão de desinformação) **[a verificar]** | C | **novo** |
| K27 | Espiral do silêncio | L4a-06 | ✅ | **Amplifica** (AF4, AF8) | ABMs (Banisch et al. 2022), survey (Cheong et al. 2022) | D | D5 |
| **K29** | **Efeito terceira pessoa** (perceber o efeito da desinformação nos outros → ação corretiva, apoio à censura) | L3-14 | ✅ processo. Q3 fraco: o outcome é behavioral e afetivo, mas o arquivo só diz "conflito intergrupal" | **Amplifica** (visibilidade da desinformação, AF4; denúncia, AF10) | um survey (Yang e Tian 2021) | D | **novo** |
| K30 | Aprendizagem por reforço social da expressão (feedback assimétrico) | L4b-01 | ✅ | **Cria/Amplifica** (AF4: contadores de aprovação sem contadores de rejeição). É o caso mais claro de efeito de design no corpus | experimento (Konovalova et al. 2023), revisão (Metzler e García 2023) | E | E1 |
| K31 | Sinalização identitária (engajamento seletivo partidário) | L4a-09 | ✅ | **Amplifica** (AF8, AF4) | observacional de plataforma (Garz et al. 2019) | E | E2 |
| **K32** | **Retaliação por denúncias** (ciclo de baixa tolerância) | L3-13 | ✅ | **Cria** (só existe com ferramentas de denúncia, AF10) | um modelo; o título diz "A potential mechanism" (Westermann e Coscia 2022) | G | **novo** |

**Totais**: 21 unidades. **15 já estão entre os 39** e **6 são candidatos novos** (K04, K10,
K11, K18, K29, K32).

### 8.2 Unidades que não entram como item próprio (passo 3.4)

| K | Nome provisório | Entradas | Motivo (régua) | Destino proposto |
|---|---|---|---|---|
| K09 | Alinhamento de temas (*issue alignment*) | L1-09 | 🔧 Q3: o alinhamento é o próprio outcome ideológico. Base só em ABMs (Baumann et al. 2021; Chen 2021; Noorazar et al. 2018) | Entra na definição de K08 (B6): *sorting* das identidades e alinhamento das posições |
| K16 | Redução de dissonância em sistemas de crenças | L4b-03 | 🔧 Sobrepõe-se a K14 e a K09. É o motor cognitivo do alinhamento | Microfundamento de K14 e K08, citado na definição |
| K19 | Espiral de reforço (*reinforcing spirals*) | L1-11 | ❌ Q2: guarda-chuva, o mesmo diagnóstico de M6 na T02 | Mantém a situação de C8 e alimenta o B02 (T03-I01) |
| K20 | Viés de confirmação no sistema de recompensa | L3-08 | ❌ **Q5**: o processo opera sem interação social, segundo o próprio arquivo. Reteste depois do passo 2.2 (7.3): continua sem via, porque a ocasião (fazer escolhas) não é fornecida por nenhuma affordance em particular | Excluir. No máximo, microfundamento de K15 |
| K21 | Amostragem sequencial e truncamento | L4b-02 | ✅ em Q1–Q4. **Reteste (7.5)**: Q5 = Hospeda, porque o feed e a rolagem infinita (AF1, AF9) oferecem a sequência de evidências. Uma fonte, de modelo e laboratório | **Candidato fraco, decisão no passo 3.4** (antes: excluir) |
| K22 | Efeito de ordem e preferência por crença | L4a-12 | ✅ em Q1–Q4. Q5 fraco (a via seria a ordenação algorítmica, AF1). Base filosófica e ABM | Registrar como candidato fraco, fora da lista |
| K23 | Inércia cética | L4a-11 | ✅ em Q1–Q4. Uma fonte qualitativa, de um país | Candidato fraco, fora da lista. Vizinho de G1 |
| K24 | Polarização por narrativas concorrentes | L3-15 | **Reteste (7.3)**: passa em Q5 como Hospeda (AF1 entrega narrativas), mas se sobrepõe a K12 e K01 (R6): narrativas concorrentes só polarizam com exposição segmentada | Excluir. O enquadramento entra na definição de K12 |
| K25 | Calibração da expressão por normas locais (autenticidade × aversão à extremidade) | L1-05 | ✅ em Q1–Q4. Uma fonte (Brown et al. 2022) | Evidência para o bloco D (D3, D4, D5), e não item próprio |
| K26 | Percepção de normas do in-group | L3-10 | ✅ em Q1–Q4. Uma fonte (You e Lee 2024) | Evidência para D4 (ignorância pluralística), aprovado em 7.3. Alternativa D6, a conferir na T03.7 |
| K28 | Reatância opinativa / espiral anti-silêncio | L3-17 | ✅ em Q1–Q4. É a condição em que K27 se inverte (anonimato e incivilidade) | Condição de contorno de K27 (D5), na definição |
| K33 | Concentração de influência em hubs e usuários prioritários | L3-16, L4a-13 | ❌ Q4: *hubs* e influenciadores são atores ou estrutura (2.3). O que muda o processo é a plataforma dar alcance desigual (verificação, impulsionamento) | Condição estrutural de K05 e de B4 (cascatas). Alternativa: reformular como "amplificação de contas prioritárias" no bloco A (D8) |

**Contagem do teste nas 33 unidades**: em Q1–Q4, ✅ 27, 🔧 4 (K01, K05, K09, K16) e ❌ 2 (K19,
K33). Q5 exclui K20. Depois dos retestes do passo 3.1, K24 sai por sobreposição (R6) e K21 vira candidato fraco (7.3, 7.5). Resultado: **21 entram e 12 não entram como item
próprio** (K09, K16, K22, K23, K25, K26 e K28 passam na régua, mas são absorvidos por outro
item ou ficam como candidatos fracos).

### 8.3 Passo 3.2 — As 15 unidades que já existem na lista atual (2026-10-18)

**O que se aprova aqui**: (i) a **correspondência** entre a unidade do corpus L e o mecanismo da
lista atual; (ii) o que a unidade **acrescenta à ficha** do mecanismo (material absorvido de outras
unidades, evidência nova, evidência contrária). Com a D1 = C, o corpus L pode ser citado nas fichas
dos 39.

**O que não se decide aqui**: os valores de *Platform role*, *Direction* e *Evidence strength* dos
39. Eles são revistos todos juntos no passo 5.3, com a régua da T03.2. A coluna "Q5 pela régua"
abaixo só sinaliza onde o valor atual vai mudar.

Valores atuais = tabela consolidada (6.11) em `adjustments/T02-ajustes.md`. Papers do corpus L
**[a verificar]** na T03.7, salvo os conferidos (T03-F03).

#### Grupo 1 — Blocos A e B (7 unidades)

| Unidade | Na lista atual | Valores atuais (Claim; Evidence) | Q5 pela régua | O que a unidade acrescenta à ficha |
|---|---|---|---|---|
| K01 Filter bubble | **A1** Filter bubble | Amplifies; Mixed | **Creates** (2.2-c: a personalização algorítmica não existe fora da plataforma). **Muda** | Evidência experimental de efeito limitado (Liu et al. 2025, p. 1) e simulação em que a personalização **reduz** a segregação sob certas condições (Törnberg 2026, p. 1): base para *Direction* = Mixed. Cho et al. 2020 (algoritmos de busca, experimento, pelo título) |
| K02 Amplificação algorítmica | **A2** Algorithmic amplification of divisive content | Amplifies; Moderate–mixed | **Amplifies** (a mídia sensacionalista já privilegiava o conteúdo indignante, e o ranking muda escala e velocidade) | Revisão de Metzler e García 2023 (*Social Drivers and Algorithmic Mechanisms on Digital Media*) e simulação de Ognibene et al. 2023. Pouco acréscimo empírico em relação a Milli [14] e Rathje [38] |
| K03 Homofilia | **B1** Homophily | Hosts & amplifies; Strong (existence), moderate (platform role) | **Amplifies** (2.1-b). **Muda** só o valor composto | Homofilia **afetiva** como variante da base da semelhança (Gu et al. 2025). Recomendação de conexões já estava em B1 (D21), e Santos [59] já é citado. Contra: segregação offline maior que a online (Tonin et al. 2025, p. 1) |
| K05 Câmara de eco | **B2** Echo chamber | Amplifies; Mixed | **Amplifies** | Absorve a **influência assimilativa** dos modelos de confiança limitada como forma do reforço intragrupo (7.1, 7.3, 7.4). Evidência contrária: Fletcher et al. 2021 (~5%, p. 1), Dubois e Blank 2018, Geiß et al. 2021 (p. 660). Törnberg 2026: câmaras de eco sem algoritmo nem preferência por homogeneidade (p. 1) |
| K06 Polarização de grupo | **B3** Group polarization | Amplifies; Strong (lab), moderate (online) | **Amplifies** | *Groupthink* entra como construto vizinho, na definição, e não como alternativo (R6). Sobeh et al. 2025: fator que mitiga o extremismo, pelo título |
| K07 Contágio moral | **B5** Moral contagion | Amplifies; Moderate | **Amplifies** | "Modulação afetiva" e "fronteiras identitárias" entram como etapas do processo (7.4, 7.5). Simchon et al. 2022 (*Troll and divide*). Hasell e Weeks 2016 mostra a mesma cadeia a partir da mídia partidária (via fora da plataforma, item 2.3-b) |
| K08 Ordenamento partidário | **B6** Partisan sorting | Hosts (amplifies); Moderate | **Amplifies** (via: interações não locais, AF2). **Muda** só o valor composto | A via de plataforma que hoje falta na ficha: Törnberg 2022 (*How digital media drive affective polarization through partisan sorting*). Absorve o **alinhamento de temas** (K09) e a **redução de dissonância** (K16) como microfundamento, na definição |

#### Grupo 2 — Bloco C (5 unidades)

| Unidade | Na lista atual | Valores atuais (Claim; Evidence) | Q5 pela régua | O que a unidade acrescenta à ficha |
|---|---|---|---|---|
| K12 Viés de confirmação (busca seletiva) | **C2** Confirmation bias | Hosts; Strong (phenomenon), weak (induced) | **Amplifies** (ambiente de alta escolha, AF3, AF11) ou **Hosts**: a decidir no passo 5.3. **Pode mudar** | O **enquadramento por narrativas concorrentes** (K24) entra na definição. Evidência de **atenuação**: usuários ativos em redes se expõem mais ao outro lado (Masip et al. 2020, p. 53) |
| K13 Evitação seletiva | **C3** Selective avoidance | Hosts & amplifies; Mixed | **Amplifies** (2.1-b) | **Perde** a dissolução de laços (bloqueio, *unfollow*) para K04, se o candidato for aprovado no passo 3.3 (D6). Hoje C3 inclui essa parte (T02, D34) |
| K14 Raciocínio motivado | **C1** Motivated reasoning | Hosts; Strong (phenomenon), magnitude debated | **Hosts** (via: AF1 oferece a ocasião, 2.2-d) | Raciocínio **politicamente** motivado (Sobkowicz 2018) como forma do mesmo processo. Redução de dissonância (K16) como microfundamento. Meta-análise de Sultan et al. 2024 |
| K15 Assimilação enviesada | **C4** Biased assimilation | Hosts; Moderate | **Hosts** | Versão em modelo de rede: rejeição e substituição do sinal incongruente (Sikder et al. 2020) |
| K17 Verdade ilusória | **C6** Illusory truth effect | Amplifies; Strong | **Amplifies** (repetição por AF5, AF1) | Experimento com notícias polarizadas repetidas (Secară e Opre 2026). Atenção para o passo 5.3: o "Strong" atual vem de Hasher [66], que é laboratório fora da plataforma. Pela regra 2.1-e, a força do **papel da plataforma** tende a cair |

#### Grupo 3 — Blocos D e E (3 unidades, mais duas absorções)

| Unidade | Na lista atual | Valores atuais (Claim; Evidence) | Q5 pela régua | O que a unidade acrescenta à ficha |
|---|---|---|---|---|
| K27 Espiral do silêncio | **D5** Spiral of silence | Amplifies; Mixed | **Amplifies** (AF4, AF8) | Feedback das reações como canal (Banisch et al. 2022; Cheong et al. 2022, *algorithm-driven*). **Condição de inversão** (K28): com anonimato e incivilidade, a minoria se manifesta em vez de calar (Fang et al. 2024). Calibração da expressão pela norma local (K25, Brown et al. 2022) |
| K30 Reforço social da expressão | **E1** Social learning of outrage | Amplifies; Moderate | **Amplifies** (AF4: contador de aprovação sem contador de rejeição) | O corpus mostra o mesmo reforço para a **opinião extrema em geral**, e não só para a indignação, e liga o efeito ao **desenho do feedback** (Konovalova et al. 2023). **Proposta**: manter o nome e a fonte definidora de E1 (Brady [13]) e acrescentar a extensão na definição |
| K31 Sinalização identitária | **E2** Identity signaling | Amplifies; Plausible | **Amplifies** (AF8, AF4) | Primeira evidência observacional de plataforma: engajamento seletivo partidário no Facebook (Garz et al. 2019). Pode elevar *Evidence strength* de Plausible para Moderate no passo 5.3 |
| (absorção) K26 | **D4** Pluralistic ignorance | — | — | Superestimação da hostilidade aprovada pelo próprio grupo → conformidade (You e Lee 2024), aprovado em 7.3 |
| (absorção) K25 | **D3**, **D4**, **D5** | — | — | Calibração da opinião expressa pela norma local percebida (Brown et al. 2022) |

**Itens para aprovação** (um por grupo):
- **3.2-G1**: correspondências e acréscimos do Grupo 1. Destaque: A1 deve passar a **Creates**
  (decidido no passo 5.3), e B6 ganha a via de plataforma que hoje falta.
- **3.2-G2**: correspondências e acréscimos do Grupo 2. Destaque: C3 perde a dissolução de laços
  se K04 for aprovado (D6), e o C6 atual "Strong" tende a cair no passo 5.3.
- **3.2-G3**: correspondências, acréscimos e absorções do Grupo 3. Destaque: E1 mantém o nome e
  ganha a extensão para a opinião extrema e o desenho do feedback.

**Decisões do usuário — passo 3.2 (2026-10-18)**: **3.2-G1, G2 e G3 aprovados**. As 15
correspondências estão confirmadas, e os acréscimos entram nas fichas na T03.8 (passo 8.2, para os
39). Os valores de *Platform role*, *Direction* e *Evidence strength* ficam para o passo 5.3.

### 8.4 Passo 3.3 — Candidato K04: dissolução seletiva de laços (2026-10-18)

**Fontes conferidas na primeira página do PDF** (regra 4):
- **Martel et al. 2024** (L4): "There is strong political assortment of Americans on social media
  networks. This is typically attributed to preferential tie formation (i.e. homophily) among those
  with shared partisanship. Here, we demonstrate an additional factor beyond homophily driving
  assorted networks: preferential prevention of social ties." Em dois experimentos de campo no
  Twitter, com contas-robô identificadas como democratas ou republicanas, os usuários foram "12
  times more likely to block counter-partisan accounts compared to copartisan accounts in the first
  experiment, and 4 times more likely […] in the second". Motivo principal do bloqueio, num survey
  experiment: "wanting to avoid seeing any content posted by the blocked user" (p. 1).
- **Kaiser et al. 2022** (L4): dois experimentos 2 × 2 com amostra representativa (n = 968).
  Usuários, sobretudo de esquerda, "are more likely to block and unfollow politically dissimilar
  than similar friends who share misinformation. Partisan blocking contributes to network
  polarization on social media" (p. 214).
- **Sasahara et al. 2020** (L3): modelo de compartilhamento com "the two ingredients of influence
  and unfriending". Mesmo com quantidades mínimas dos dois, "the social network rapidly devolves
  into segregated, homogeneous communities". As previsões são "consistent with empirical data from
  Twitter" (p. 381).
- **Törnberg 2026** (L1): saídas em cascata de comunidades geram segregação "without users
  preferring homogeneous environments". A personalização pode "slowing exit cascades" (p. 1).

**Frequência dos termos no OpenAlex** (título e abstract, consulta de 2026-10-18; a lematização
infla as contagens, por isso valem os exemplos): *unfriending* com *political* traz títulos como
"The politics of 'Unfriending'", "Pruning the news feed: Unfriending and unfollowing political
content…" e "Dividing social networks: Facebook unfriending, unfollowing, and blocking…".
*Unfollowing* com *political*: 36 registros. *Partisan blocking*: 7. *Tie dissolution*: 54, em
geral fora do contexto político. Conclusão (R2): ***unfriending*** é o termo mais corrente, e
*unfollowing* e *blocking* aparecem como variantes da mesma prática.

**Ficha proposta** (conteúdo; o texto em inglês sai no passo 8.2):

| Campo | Proposta |
|---|---|
| Nome | **Unfriending** (alt. unfollowing, partisan blocking) |
| O que é | O corte de laços já existentes (deixar de seguir, desfazer amizade, bloquear, silenciar, sair de uma comunidade) com usuários de posição política oposta ou que compartilham conteúdo considerado inaceitável |
| O que a plataforma muda (Q5) | **Amplifies**: o processo existe fora da plataforma (romper amizades por política), e a plataforma reduz o **custo** do corte a um clique e sem reciprocidade (AF3, cuja definição no paper já inclui "unilaterally disconnect at will"). A saída de comunidades usa AF11 |
| Como leva à polarização | Cortes repetidos de laços com o outro lado removem os laços cruzados, e a rede se reorganiza em grupos homogêneos: polarização **estrutural**. Com menos exposição ao outro lado, a influência dentro dos grupos (B2) fica sem contrapeso |
| Fronteiras | **B1 (homofilia)**: formar laços com semelhantes, enquanto K04 é **cortar** laços existentes. Martel et al. 2024 separa as duas coisas explicitamente. **C3 (evitação seletiva)**: evitar conteúdo e fontes, sem mexer na rede. O motivo do bloqueio pode ser evitar conteúdo (Martel, p. 1), mas o efeito de K04 é estrutural. **G4 (migração de plataforma)**: a comunidade inteira muda de plataforma depois de uma ação de governança, enquanto em K04 o usuário corta laços ou sai de comunidades dentro da plataforma |
| Outcome | Structural (primário) |
| *Direction* | **Reinforcing**. Condição de atenuação registrada: em simulação, a personalização pode desacelerar as saídas em cascata (Törnberg 2026) |
| *Evidence strength* | **Strong**: dois experimentos de campo na plataforma, com replicação em survey experiment (Martel et al. 2024), e dois experimentos de outra equipe (Kaiser et al. 2022). Passa no teto do 2.1-e (manipulação na plataforma) |
| Ref | Martel et al. 2024; Kaiser et al. 2022; Sasahara et al. 2020; Törnberg 2026 (todos do corpus L, entre os 147 incluídos) |
| Bloco | **B**, subgrupo "seleção" (decisão de subgrupos no passo 4.1) |

**Itens para aprovação**:

| Item | Proposta | Recomendação |
|---|---|---|
| **3.3-K04-a** Entra | K04 entra como mecanismo novo | Aprovar. A base já foi conferida no PDF (primeira página das quatro fontes centrais). A T03.7 completa a conferência dos outros papers citados |
| **3.3-K04-b** D6 | **(a)** item próprio em B, e não parte de C3 | Aprovar. **Altera a D34 da T02**: a C3 deixa de incluir o corte de laços. Na ficha atual da C3, saem "and contacts" da definição e a frase "On social media, avoidance can also take the form of cutting ties…", que passa a remeter ao mecanismo novo. O outcome de C3 deixa de ser "Structural" e fica "Ideological" (passo 5.3) |
| **3.3-K04-c** Nome | **Unfriending** (alt. unfollowing, partisan blocking) | Aprovar. Alternativa: *Selective tie dissolution*, mais descritivo e pouco usado (R2) |
| **3.3-K04-d** Valores | Platform role = Amplifies (custo, AF3); Direction = Reinforcing; Evidence strength = Strong; Outcome = Structural | Aprovar |
| **3.3-K04-e** ID | Provisório **B-novo (K04)**. O ID definitivo sai no passo 4.2: logo depois de B1 (ordem lógica, D36), o que renumera os IDs seguintes do bloco B já propagados no paper, ou no fim do bloco (B9), sem renumerar | Decidir no passo 4.2 |

**Decisões do usuário — K04 (2026-10-18)**: **3.3-K04-a a d aprovados**. K04 entra como
**Unfriending** (alt. unfollowing, partisan blocking), no bloco B. **D6 = (a)**: item próprio,
o que **altera a D34 da T02** (C3 deixa de incluir o corte de laços; ajuste da ficha de C3 na
T03.8). Valores: Amplifies (custo, AF3), Reinforcing, Strong, Structural. ID no passo 4.2.

### 8.5 Passo 3.3 — Candidato K11: efeito *backfire* (2026-10-18)

**Fontes conferidas na primeira página do PDF** (regra 4):
- **Bail et al. 2018** (L2; já na lista do paper como [84]): experimento de campo no Twitter;
  republicanos que seguiram por um mês um robô com mensagens liberais "became substantially more
  conservative posttreatment". Entre os democratas, o aumento de atitudes liberais não foi
  estatisticamente significativo (p. 1).
- **Karlsen et al. 2017** (L1): propõem a lógica de *trench warfare*, "in which opinions are
  reinforced through contradiction as well as confirmation". Nos survey experiments, "both
  confirming and contradicting arguments have similar effects on attitude reinforcement", e
  argumentos neutros de dois lados têm efeito menor (p. 257).
- **Kim et al. 2025** (L4): com dados do Twitter, a etiquetagem individual de desinformação "caused
  posters to retreat into information bubbles". O efeito foi suavizado pela verificação coletiva
  (*Community Notes*): "With collective misinformation tagging, posters were less likely to retreat
  from diverse information engagement" (p. 1).
- **Zarouali et al. 2020** (L4): num experimento, as pessoas "agreed more to a counter-attitudinal
  news article when it was delivered by a news chatbot (compared with the website article)" (p. 53).
- **Nordbrandt 2022** (L4): a comunicação cruzada "sometimes elevate[s] polarization—especially
  when individuals also have access to like-minded views and when disagreement is perceived as
  intense" (p. 1).
- O *backfire* replica mal fora dessas condições **[conhecimento do agente; conferir dados
  bibliográficos: Wood e Porter 2019, *Political Behavior*]**. A referência não está no corpus L e
  só entraria pelo fluxo de literatura (G2, G4).

**Ficha proposta** (conteúdo; o texto em inglês sai no passo 8.2):

| Campo | Proposta |
|---|---|
| Nome | **Backfire effect** (alt. boomerang effect, trench warfare) |
| O que é | O reforço da atitude prévia, ou o afastamento da posição defendida, depois da exposição a mensagens contra-atitudinais ou a correções. Inclui a forma **comportamental** documentada por Kim et al. 2025: depois de ser corrigido, o usuário recua para fontes alinhadas |
| O que a plataforma muda (Q5) | **Amplifies**: o processo existe fora da plataforma (persuasão que sai pela culatra). A plataforma aumenta a **dose** de encontros com o outro lado e com correções públicas: exposição incidental (Masip et al. 2020), baixa segmentação de audiência (AF6), seguir contas do outro lado (AF3, Bail [84]) e ferramentas de checagem e etiquetagem (AF10, Kim et al. 2025) |
| Como leva à polarização | A mensagem do outro lado é lida como ameaça à identidade → a pessoa contra-argumenta e desacredita a fonte (o raciocínio motivado, C1, é o motor) → a atitude se reforça ou se desloca para longe da mensagem: polarização **ideológica** |
| Fronteiras | **C4 (assimilação enviesada)**: avaliar de modo desigual a mesma evidência, o que gera divergência sem inversão; em K11, a mensagem contrária **inverte ou reforça** a atitude. **K10 (influência social negativa)**: formulação de influência entre agentes, que depende do grupo da fonte; K11 é a resposta individual à mensagem ou à correção. **C3 (evitação seletiva)**: evitar o contrário por escolha; o recuo de Kim et al. é **reação** a uma correção. **B2 (câmara de eco)**: a exposição ao outro lado que reduziria a câmara de eco pode ativar K11 (item 2.3-e) |
| Outcome | Ideological (primário) |
| *Direction* | **Mixed**: reforço em Bail [84] e Karlsen et al. 2017. **Atenuação pelo desenho**: verificação coletiva no lugar da individual (Kim et al. 2025) e entrega por chatbot (Zarouali et al. 2020). Condição de reforço: discordância percebida como intensa (Nordbrandt 2022) |
| *Evidence strength* | **Moderate**. Há um experimento de campo na plataforma (Bail [84]), mas com efeito significativo só num dos grupos, e uma análise causal observacional (Kim et al. 2025). Os demais são survey experiments. Falta replicação robusta para chegar a Strong (6.1) |
| Ref | Bail et al. [84]; Karlsen et al. 2017; Kim et al. 2025; Zarouali et al. 2020; Nordbrandt 2022 (corpus L, entre os 147 incluídos, salvo [84]) |
| Bloco | **C** (resposta individual à informação) |

**Ganho colateral para a Tabela 6 (intervenções)**: Kim et al. 2025 compara duas formas de
moderação de AF10 (etiquetagem individual × *Community Notes*). É evidência de intervenção que a
Tabela 6 pode usar, a decidir no passo 4.3.

**Itens para aprovação**:

| Item | Proposta | Recomendação |
|---|---|---|
| **3.3-K11-a** Entra | K11 entra como mecanismo novo | Aprovar. As cinco fontes centrais foram conferidas na primeira página |
| **3.3-K11-b** Nome | **Backfire effect** (alt. boomerang effect, trench warfare) | Aprovar. *Trench warfare* é o termo de Karlsen et al. para o reforço pela contradição em debates online. *Attitude polarization* fica fora, porque nomeia o outcome (R4) |
| **3.3-K11-c** Forma comportamental | O recuo para fontes alinhadas depois de uma correção (Kim et al. 2025) entra na definição de K11, e não em C3 | Aprovar. O que une os casos é a reação a uma mensagem ou correção contrária |
| **3.3-K11-d** Valores | Platform role = Amplifies (dose, AF3, AF6, AF10); Direction = Mixed; Evidence strength = Moderate; Outcome = Ideological | Aprovar |
| **3.3-K11-e** ID | Provisório **C-novo (K11)**; posição no bloco C no passo 4.2 | Decidir no passo 4.2 |

**Decisões do usuário — K11 (2026-10-18)**: **3.3-K11-a a d aprovados**. K11 entra como **Backfire
effect** (alt. boomerang effect, trench warfare), no bloco C, incluindo a forma comportamental
(recuo depois de uma correção). Valores: Amplifies (dose, AF3, AF6, AF10), Mixed, Moderate,
Ideological. ID no passo 4.2.

### 8.6 Passo 3.3 — Candidato K10: influência social negativa (2026-10-18)

**Fontes conferidas na primeira página do PDF** (regra 4):
- **Axelrod et al. 2021** (L2): modelo baseado em agentes que separa "the tendency for two actors to
  interact (exposure) and how they respond when interactions occur, positing that interaction
  between similar actors reduces their difference while interaction between dissimilar actors
  increases their difference" (abstract).
- **Krueger et al. 2017** (L3): *q-voter* com conformidade e anticonformidade numa rede de dois
  grupos antagônicos. Abaixo de um número crítico de ligações entre os grupos, o consenso é
  possível; "Above that point the system ends up in a polarized state" (abstract).
- **Thurner et al. 2025** (L3): num modelo com homofilia e equilíbrio estrutural, "above a critical
  social connectivity, an explosive transition toward strong polarization must occur". Os autores
  ligam isso ao aumento observado das conexões sociais nas últimas décadas (p. 1).
- **Nettasinghe et al. 2025** (L3): num modelo de decisão em sociedade afetivamente polarizada,
  "larger out-group animosity compared to in-group favoritism […] is sufficient for polarization",
  e, "counter-intuitively", aumentar as conexões entre partidos favorece a divisão (p. 1).
- **Carpentras et al. 2022** (L4), o único modelo derivado de experimento: influência "very weak,
  but statistically significant", inversão de opinião em cerca de 4% das interações, e menos
  mudança entre os mais extremos (abstract). **Não mostra repulsão.**
- **Keijzer e Mäs 2022** (L4): o efeito da personalização sobre a polarização depende de mecanismos
  nos níveis individual, local e global, e não pode ser decidido sem considerar essa complexidade
  (abstract).

**Termos no OpenAlex** (título e abstract, 2026-10-18): *negative social influence* 243; *repulsive
influence* 47; *anticonformity* 100. Entre os títulos devolvidos há dois contrapontos, **fora do
corpus L** e **[a verificar]**: "Differentiation without Distancing. Explaining Bi-Polarization of
Opinions…", em que a polarização surge sem influência negativa, e "Depolarizing power of
anticonformity".

**Ficha proposta** (conteúdo; o texto em inglês sai no passo 8.2):

| Campo | Proposta |
|---|---|
| Nome | **Negative social influence** (alt. repulsive influence, anticonformity) |
| O que é | A mudança de opinião **para longe** da posição de outra pessoa quando ela é vista como muito distante ou como membro do out-group. Na forma de **anticonformidade**, a pessoa adota o oposto do que o out-group adota. Na forma de **equilíbrio estrutural**, ela se alinha com os amigos e se opõe aos inimigos, e a rede se divide em dois blocos |
| O que a plataforma muda (Q5) | **Amplifies** (**ajuste** em relação à ilustração de 6.4, que dizia Hosts). O processo existe fora da plataforma, e ela aumenta a **dose** de interações com pessoas distantes e com o out-group: conexões não locais (AF2), baixa segmentação de audiência (AF6) e identidade partidária visível (AF8), que torna o grupo do outro reconhecível antes do argumento. Nos modelos, é justamente o aumento dessas interações que dispara a polarização (Thurner et al. 2025; Krueger et al. 2017; Nettasinghe et al. 2025) |
| Como leva à polarização | Interações repetidas com o out-group → cada contato afasta as opiniões → as posições moderadas se esvaziam e a população se divide em dois polos: polarização **ideológica** e, na versão de Nettasinghe et al., **afetiva** |
| Fronteiras | **K11 (*backfire*)**: reação **ao conteúdo** de uma mensagem contrária ou de uma correção; em K10, o afastamento depende **de quem** é a fonte (distância ou grupo), e não do conteúdo. **B2 (câmara de eco)**: a influência **assimilativa** entre semelhantes fica em B2; K10 é só a parte negativa. **B6 (*sorting*)**: alinhamento de identidades; K10 é a mudança de opinião por interação |
| Outcome | Ideological (primário), Affective |
| *Direction* | **Mixed**. Nos modelos do corpus, o efeito é de reforço por construção. Mas o único teste experimental não encontra repulsão (Carpentras et al. 2022), e há modelos fora do corpus em que a anticonformidade despolariza ou em que a polarização surge sem influência negativa (títulos do OpenAlex, [a verificar]) |
| *Evidence strength* | **Plausible**: só simulações, e o teto do 2.1-e para simulação é Plausible |
| Ref | Axelrod et al. 2021; Krueger et al. 2017; Thurner et al. 2025; Nettasinghe et al. 2025; Carpentras et al. 2022 (corpus L, entre os 147 incluídos) |
| Bloco | **B**, subgrupo "influência" |

**Ponto para a discussão do paper (subseção 2.3-a)**: K10 é a versão de rede do mesmo achado de
K11. A exposição ao outro lado, que reduz a câmara de eco, pode aumentar a polarização. Os modelos
mostram isso no agregado, e Bail [84] mostra no indivíduo.

**Itens para aprovação**:

| Item | Proposta | Recomendação |
|---|---|---|
| **3.3-K10-a** Entra como item próprio | K10 entra como mecanismo novo, separado de K11 pela fronteira acima (fonte × conteúdo). **Alternativa**: fundir K10 em K11, tratando os modelos como a versão agregada do *backfire* | Aprovar como item próprio. Anticonformidade e equilíbrio estrutural dependem da identidade ou da relação, e não do conteúdo, e por isso não cabem na definição de K11. Mas, com evidência só de simulação, a fusão é defensável se você preferir uma tipologia mais enxuta |
| **3.3-K10-b** Nome | **Negative social influence** (alt. repulsive influence, anticonformity) | Aprovar |
| **3.3-K10-c** Valores | Platform role = **Amplifies** (dose, AF2, AF6, AF8); Direction = Mixed; Evidence strength = Plausible; Outcome = Ideological, Affective | Aprovar. Muda a ilustração de 6.4 (Hosts → Amplifies) |
| **3.3-K10-d** ID | Provisório **B-novo (K10)**; posição no passo 4.2 | Decidir no passo 4.2 |

**Decisões do usuário — K10 (2026-10-18)**: **3.3-K10-a a c aprovados**. K10 entra como **Negative
social influence** (alt. repulsive influence, anticonformity), **item próprio**, separado de K11,
no bloco B. Valores: Amplifies (dose, AF2, AF6, AF8; ajuste da ilustração de 6.4), Mixed,
Plausible, Ideological e Affective. ID no passo 4.2.

### 8.7 Passo 3.3 — Candidato K18: sobrecarga cognitiva e processamento heurístico (2026-10-18)

**Cadeia descrita pelo Gemini** (L2-10): volume e velocidade da informação → sobrecarga da
memória de trabalho → inibição do processamento analítico (Sistema 2) → aceitação acrítica do
congruente → atitudes mais extremas.

**Fontes conferidas na primeira página do PDF** (regra 4). São as quatro citadas, e só elas:

| Paper (L2) | O que diz | Sustenta a cadeia? |
|---|---|---|
| Du et al. 2025 | "just one week of exposure to polarized content can result in distinct patterns of behavior and brain activity during the perception of videos"; conteúdo negativo baixa o escore de sentimento, e o positivo o eleva (p. 1) | **Não**. Trata do efeito emocional da exposição a conteúdo polarizado em vídeos curtos. Não mede sobrecarga nem processamento heurístico |
| Bo et al. 2025 | Experimento com 132 universitários chineses sobre informação a respeito de IA: cursos estruturados, "marked by high cognitive load and reliability, significantly reduced polarization (β = −0.32, p < 0.01)" (p. 1) | **Não, e aponta o contrário**: carga cognitiva alta associada a **menos** polarização. Sem plataforma |
| Edinger et al. 2025 | Marcadores linguísticos de distorção cognitiva em tweets sobre as eleições de 2016 e 2020: "We find a sharp increase of such markers between these two elections" (p. 1) | **Não**. É um marcador do estilo de pensamento polarizado, e não um mecanismo de sobrecarga |
| Clemons et al. 2025 | Simulação sobre mecanismos para limitar a difusão de desinformação e orientar reguladores (p. 1) | **Não**. Sem relação com o processo |

**Julgamento**: é o caso mais claro de **T03-F03**. A cadeia de K18 é uma síntese do Gemini, e não
um processo descrito pelas fontes que ele citou. A hipótese em si (formatos rápidos favorecendo o
processamento intuitivo) existe na literatura sobre desatenção e desinformação **[conhecimento do
agente; conferir dados bibliográficos: Pennycook e Rand]**, mas não está no corpus L.

**Itens para aprovação**:

| Item | Proposta | Recomendação |
|---|---|---|
| **3.3-K18-a** Não entra | K18 não entra na tipologia: falha na base, e não na régua | Aprovar |
| **3.3-K18-b** Backlog | Registrar a hipótese como **B05** no `backlog.md`: "processamento heurístico induzido pelo formato (vídeos curtos, rolagem infinita)", com Bo et al. 2025 como evidência contrária e a indicação de que uma fonte só entraria por busca nova (fluxo `/literature-review`, G4) | Aprovar |
| **3.3-K18-c** Inclusão na síntese | Bo et al. 2025 e Clemons et al. 2025 só eram citados em L2-10 e **saem dos incluídos**: 147 → **145**. Du et al. 2025 (citado também em L2-04, K01) e Edinger et al. 2025 (também em L2-03, K05) continuam incluídos, e a T03.7 confere se sustentam essas unidades | Aprovar |
| **3.3-K18-d** Registro em T03-F03 | Acrescentar K18 ao achado T03-F03 como exemplo de unidade inteira sem base nas fontes citadas | Aprovar |

**Efeito na contagem**: das 21 unidades da Tabela 8.1, entram 20 se K18 sair. Candidatos novos
aprovados até aqui: K04, K11, K10. Restam K32 e K29.

**Decisões do usuário — K18 (2026-10-18)**: **3.3-K18-a aprovado: K18 não entra.** Consequências
aplicadas: (c) Bo et al. 2025 e Clemons et al. 2025 saem dos incluídos (**147 → 145**;
`inclusao-sintese-preliminar.csv` atualizado); (d) K18 registrado em T03-F03; (b) hipótese
registrada no `backlog.md` como **B05**, como recomendado (o usuário pode retirá-la). Unidades que
entram: **20**.

### 8.8 Passo 3.3 — Candidato K32: retaliação por denúncias (2026-10-18)

**Fonte conferida no PDF** (regra 4). É a única citada:
- **Westermann e Coscia 2022** (L3), *A potential mechanism for low tolerance feedback loops in
  social media flagging*. Simulação: sistemas de denúncia coletiva supõem "that users are impartial
  arbiters of truth", mas os usuários podem ser influenciados "by their own political biases and
  tolerance for opposing points of view". No modelo, as fontes do lado oposto aos usuários
  intolerantes "attract more flags". Com duas extensões (as fontes buscam o caminho de menor
  resistência; os usuários reduzem a tolerância quando percebem menos tolerância do outro lado),
  "intolerance is attractive: news sources are nudged to move their polarity to the side of the
  intolerant users", e os regimes de alta tolerância "will converge towards empirically-supported
  low-tolerance states" (abstract).

**Literatura** (OpenAlex, 2026-10-18): o termo é raro. *Biased flagging* 10, *partisan flagging* 2,
*crowdsourced flagging* 3. Entre os títulos devolvidos há um trabalho anterior do mesmo grupo,
fora do corpus L: "Distortions of political bias in crowdsourced misinformation flagging"
**[a verificar]**. Kim et al. 2025 (corpus L, aprovado em K11) é evidência vizinha: o **desenho**
da verificação (individual × coletiva, *Community Notes*) muda o efeito das etiquetas.

**Ficha proposta** (conteúdo; o texto em inglês sai no passo 8.2):

| Campo | Proposta |
|---|---|
| Nome | **Partisan flagging** (alt. biased crowdsourced flagging). O termo é raro (R2 não decide), e o nome segue o padrão de *partisan blocking* em K04 |
| O que é | O uso das ferramentas de denúncia de forma enviesada pela posição política: usuários denunciam mais o conteúdo do outro lado, o outro lado responde reduzindo a própria tolerância, e as fontes ajustam o que publicam para escapar das denúncias |
| O que a plataforma muda (Q5) | **Creates**: sem um sistema de denúncia que afeta a distribuição do conteúdo, o processo não existe (2.2-c). Via: governança da plataforma (AF10) |
| Como leva à polarização | Denúncia enviesada → o conteúdo do outro lado perde alcance → retaliação com a mesma ferramenta → equilíbrio de baixa tolerância. Do lado da oferta, as fontes se deslocam para o lado dos usuários mais intolerantes: polarização **ideológica** (das fontes) e **afetiva** (intolerância mútua) |
| Fronteiras | **G5 (censura percebida)**: a percepção de viés na moderação; K32 é o uso enviesado da ferramenta pelos usuários. **E3 (produção orientada por métricas)**: as fontes se ajustam ao engajamento; em K32, se ajustam às denúncias. Mesmo lado da oferta, outro sinal. **F2 (*dogpiling*)**: ataque coletivo direto a uma pessoa; a denúncia em massa pode ser uma forma dele, mas K32 opera pelo sistema de moderação. **K11 (*backfire*)**: a reação de quem é corrigido; K32 é o lado de quem denuncia |
| Outcome | Ideological (primário), Affective |
| *Direction* | **Reinforcing** (no modelo). Condição de atenuação possível: o desenho coletivo da verificação (Kim et al. 2025), a conferir se vale para denúncias |
| *Evidence strength* | **Plausible**: uma simulação, e o próprio título fala em "potential mechanism" |
| Ref | Westermann e Coscia 2022 (corpus L, incluído) |
| Bloco | **G** (governança da plataforma), ao lado de G4 e G5, que AF10 também alimenta |

**Itens para aprovação**:

| Item | Proposta | Recomendação |
|---|---|---|
| **3.3-K32-a** Entra | K32 entra como mecanismo novo, com evidência Plausible | Aprovar com ressalva: é o candidato mais fraco em base (uma simulação), mas o mais específico de plataforma e o único que liga a governança à oferta de notícias. Para uma revista de jornalismo, isso pesa. Alternativa: registrar no backlog até haver evidência empírica |
| **3.3-K32-b** Nome | **Partisan flagging** (alt. biased crowdsourced flagging) | Aprovar |
| **3.3-K32-c** Valores | Platform role = Creates (AF10); Direction = Reinforcing; Evidence strength = Plausible; Outcome = Ideological, Affective | Aprovar |
| **3.3-K32-d** ID | Provisório **G-novo (K32)**; posição no passo 4.2 | Decidir no passo 4.2 |

**Decisões do usuário — K32 (2026-10-18)**: **3.3-K32-a a c aprovados: K32 entra agora**, como
**Partisan flagging** (alt. biased crowdsourced flagging), no bloco G. Valores: Creates (AF10),
Reinforcing, Plausible, Ideological e Affective. ID no passo 4.2.

### 8.9 Passo 3.3 — Candidato K29: efeito terceira pessoa (2026-10-18)

**Cadeia descrita pelo Gemini** (L3-14): exposição a desinformação → perceber que ela afeta mais
os outros → ação corretiva (censura, ataques, denúncias) → conflito intergrupal.

**Fonte conferida no PDF** (regra 4). É a única citada:
- **Yang e Tian 2021** (L3): survey online com 871 respondentes (Amazon Mechanical Turk), no
  contexto da COVID-19. O engajamento em mídia social "directly increased TPP [third-person
  perception]" e a aumentou indiretamente pela autoeficácia e pelo conhecimento percebido. Os autores
  concluem que a mídia social pode "cultivate a slanted belief that he or she is fake-news-proof"
  (abstract). Nas três primeiras páginas não há menção a polarização nem a ação contra o out-group.

**Literatura** (OpenAlex, 2026-10-18): *third-person effect* com *polarization*: **0** registros;
com *social media*: 80, sobre percepção de risco, compartilhamento de *fake news* e propaganda.

**Julgamento**:
- **Q3 falha**: a fonte não leva a nenhum dos cinco outcomes. O que ela mede é uma percepção sobre a
  própria vulnerabilidade, e não uma mudança de polarização. Os passos "ação corretiva" e "conflito
  intergrupal" foram acrescentados pelo Gemini, como em K18.
- Existe uma versão **partidária** da hipótese que seria relevante para o bloco D: acreditar que o
  **out-group** é mais vulnerável à desinformação, o que alimentaria a hostilidade e a polarização
  percebida. Mas essa versão não está na fonte nem no corpus L, e fica perto de C5 (efeito da mídia
  hostil) e D6 (metapercepções).

**Itens para aprovação**:

| Item | Proposta | Recomendação |
|---|---|---|
| **3.3-K29-a** Não entra | K29 não entra: Q3 falha e a fonte não sustenta a cadeia | Aprovar |
| **3.3-K29-b** Backlog | Registrar como **B06** a versão partidária ("o out-group é mais enganado que nós"), vizinha de C5 e D6, a buscar no fluxo `/literature-review` | Aprovar, ou descartar se você não quiser acumular hipóteses |
| **3.3-K29-c** Inclusão na síntese | Yang e Tian 2021 só era citado em L3-14 e sai dos incluídos: **145 → 144** | Aprovar |
| **3.3-K29-d** Registro em T03-F03 | Acrescentar K29 ao achado T03-F03, ao lado de K18 | Aprovar |

**Fechamento do passo 3.3, se aprovado**: dos seis candidatos novos, **entram 4** (K04 Unfriending,
K11 Backfire effect, K10 Negative social influence, K32 Partisan flagging) e **não entram 2** (K18,
K29), os dois por falta de base nas fontes citadas. Unidades da lista preliminar que entram:
**19** (15 já existentes + 4 novas). Lista atual: 39 + 4 = **43 mecanismos**, antes do passo 3.4 e
da T03.5.

**Decisões do usuário — K29 (2026-10-18)**: **3.3-K29-a aprovado: K29 não entra.** Consequências
aplicadas: (c) Yang e Tian 2021 sai dos incluídos (**145 → 144**); (d) K29 registrado em T03-F03;
(b) versão partidária registrada no `backlog.md` como **B06**, no mesmo critério de B05 (o usuário
pode retirá-la). **Passo 3.3 concluído**: entram K04, K11, K10 e K32. Lista: **43 mecanismos**.

### 8.10 Passo 3.4 — Unidades que não entram (2026-10-18)

**Parte 1 — destinos já aprovados nos lotes do passo 3.1** (confirmação em bloco):

| Unidade | Destino aprovado | Onde foi aprovado |
|---|---|---|
| K09 Alinhamento de temas | Entra na definição de B6 (*partisan sorting*) | 7.1 (L1-09); 8.3 (G1) |
| K16 Redução de dissonância | Microfundamento nas definições de C1 e B6 | 7.5 (L4b-03); 8.3 |
| K19 Espiral de reforço | Situação de C8 (B02); Ohme 2021 alimenta o B02 | 7.1 (L1-11) |
| K20 Viés no sistema de recompensa | Excluído (sem via de plataforma, reteste) | 7.3 (L3-08) |
| K24 Narrativas concorrentes | Excluído por sobreposição; o enquadramento entra na definição de C2 | 7.3 (L3-15); 8.3 (G2) |
| K25 Calibração da expressão pela norma local | Evidência para D3, D4 e D5 | 7.1 (L1-05); 8.3 (G3) |
| K26 Percepção de normas do in-group | Evidência para D4 | 7.3 (L3-10); 8.3 (G3) |
| K28 Reatância opinativa | Condição de inversão de D5 | 7.3 (L3-17); 8.3 (G3) |

**Parte 2 — os quatro casos pendentes** (fontes conferidas no PDF):

| Unidade | Fonte e o que diz | Julgamento | Proposta |
|---|---|---|---|
| **K21** Amostragem sequencial e truncamento | Kvam et al. 2022 (L4b): "Polarization and extremism are often viewed as the product of psychological biases or social influences, yet they still occur in the absence of any bias or irrational thinking". Evidência extrema faz o decisor parar de amostrar, e a moderada é sub-amostrada. O efeito aparece em experimentos, inclusive com temas políticos, e diminui quando se pede estimativa em vez de decisão (p. 1) | Processo bem demonstrado em laboratório, distinto dos vieses de C1–C4. Q5 = Hosts (o feed oferece a sequência de evidências), mas **nenhuma evidência de plataforma**. Uma ligação plausível com A2 (o ranking põe a evidência extrema primeiro e antecipa a parada) não está na fonte | **Não entra agora**; registrar no backlog (B07) como candidato com base de laboratório, à espera de estudo em plataforma |
| **K22** Efeito de ordem e preferência por crença | Baumgaertner e Justwan 2022 (L4a): "a much weaker mechanism—the preference for belief—can produce issue polarization in epistemic communities with little to no mechanisms of exclusion", num modelo de rede "with an empirically-validated structure". O modelo complementa a assimilação enviesada e o raciocínio motivado (abstract) | Modelo filosófico-computacional que **complementa** C4 e C1. A via de plataforma (ordem do feed) não está na fonte | **Não entra**; citar, se útil, na definição de C4 como explicação alternativa sem exclusão. Registrar no B07 |
| **K23** Inércia cética | Bozdağ e Koçer 2022 (L4a): estudo qualitativo na Turquia (grupos focais, diários, entrevistas) que analisa "how political polarization influences the users' trust in the news and their perceptions about misinformation on social media" (abstract) | A direção é **inversa**: a polarização é a causa, e a desconfiança é o efeito. Não é mecanismo de polarização (Q3). Serviria como exemplo de causalidade reversa (2.3-f), mas Nordbrandt 2021 já cumpre esse papel | **Não entra**. Fica fora da síntese, pelo critério de inclusão |
| **K33** Concentração de influência e usuários prioritários | Arruda et al. 2024 (L4a): "Priority users (e.g., verified profiles on Twitter) are social media users whose content is promoted by recommendation algorithms". Priorizá-los "can inadvertently reduce polarization if they post according to the same rule but sharpen echo chamber formation if they behave heterogeneously", e uma minoria de ideólogos teimosos e priorizados pode levar o sistema do consenso à polarização (abstract). As fontes de L3-16 (Giese 2023; Wang 2022; Yin 2024) tratam de líderes de opinião e *hubs* | Os *hubs* e influenciadores são **atores** (2.3). Mas Arruda mostra outra coisa: a **plataforma** concede alcance desigual (verificação, impulsionamento), o que é decisão de design (AF1, AF10). O efeito depende de quem é priorizado | **Fundir em A2** (*algorithmic amplification*) como segunda via: além do conteúdo que engaja, o ranking amplifica **contas** priorizadas. Direção Mixed (pode reduzir ou acentuar). Alternativas: (a) excluir e tratar como condição de B2 e exemplo de ator; (c) item próprio no bloco A, com uma fonte de simulação |

**Itens para aprovação**:

| Item | Proposta | Recomendação |
|---|---|---|
| **3.4-a** | Confirmar em bloco os destinos da Parte 1 | Aprovar |
| **3.4-b** | K21 não entra agora; registrar no backlog **B07** (candidatos de laboratório ou modelo, sem evidência de plataforma: K21 e K22) | Aprovar |
| **3.4-c** | K22 não entra; Baumgaertner e Justwan 2022 pode ser citado na definição de C4 (já está entre os incluídos, por L4a-05 e L4a-07) | Aprovar |
| **3.4-d** | K23 não entra (direção inversa) | Aprovar |
| **3.4-e** | K33 fundido em A2, como amplificação de contas priorizadas, com Arruda et al. 2024 (já entre os incluídos, por L4a-10) | Aprovar. Giese et al. 2023 e Yin et al. 2024 continuam fora da síntese |

**Efeito na contagem, se aprovado**: nenhuma unidade nova. Lista: **43 mecanismos**. Incluídos na
síntese: **144** (nenhuma mudança, porque Kvam, Bozdağ e Koçer, Giese e Yin já estavam fora).
**Fim da T03.3.**

**Decisões do usuário — passo 3.4 (2026-10-18)**:

| Item | Decisão | Efeito |
|---|---|---|
| 3.4-a | Destinos da Parte 1 **já aprovados** lote a lote no passo 3.1 (7.1–7.5) e nos grupos do passo 3.2 | Confirmados, sem nova decisão |
| 3.4-b | **K21 não entra** | O usuário não pediu o registro no backlog: **B07 não foi criado** |
| 3.4-c | **K22 não entra** | A citação de Baumgaertner e Justwan 2022 na definição de C4 fica como sugestão opcional para o passo 8.2, sem decisão |
| 3.4-d | **K23 não entra** | — |
| 3.4-e | **K33 fundido em A2** | A2 ganha uma segunda via: o ranking amplifica **contas** priorizadas (verificação, impulsionamento), além do conteúdo que engaja. Fonte: Arruda et al. 2024. Direção dessa via: Mixed. Texto no passo 8.2 |

**T03.3 concluída (2026-10-18).** Resultado: **43 mecanismos** (39 + K04, K10, K11, K32);
**144 papers** incluídos na síntese.

---

## 9. T03.4 — Os blocos da T02 ainda servem?

**Base dos blocos** (D6 da T02): o **locus do processo**. Os 21 entram assim: A 2 · B 7 · C 7
· D 2 · E 2 · F 0 · G 1.

**Leitura**:
- **Nenhum candidato novo pede bloco novo.** Os seis cabem no locus: K04 e K10 em B (dependem
  de quem está ligado a quem e de quem é do grupo), K11 e K18 em C (processamento individual),
  K29 em D (percepção dos outros) e K32 em G (governança).
- **O bloco B cresce para 10** (8 da T02 + K04, K10) e mistura dois tipos de processo que a
  literatura de redes separa: **seleção** (quem se liga a quem: B1, K04, B6) e **influência**
  (como as opiniões mudam pelos laços: B2, B3, B4, B5, K10, B8). Há um título no corpus que
  usa exatamente essa distinção: *Social influence and unfollowing accelerate the emergence of
  echo chambers* (Sasahara et al. 2020, L3). A distinção seleção × influência é clássica na
  análise de redes **[conhecimento do agente; conferir dados bibliográficos: Shalizi e Thomas
  2011]**.
- **F e G vazios no corpus L** não indicam problema de bloco. São efeito da string (T03-F01).
- **Não criar bloco pelo papel da plataforma** (Cria/Amplifica/Hospeda): misturaria de novo as
  bases de divisão (T02.1-F05). O papel vai numa coluna (6.3).

**Opções** (D7):
- **(a) Manter os sete blocos** e abrir B com dois subgrupos declarados (seleção e influência).
  Não muda IDs já propagados no paper (T02.5). **Recomendada.**
- **(b) Dividir B** em B (seleção de laços) e um bloco novo de influência social. Mais limpo,
  mas exige renumerar IDs, figuras e tabelas que a T02.5 acabou de propagar.

### 9.1 Passos 4.1 e 4.2 — Blocos e IDs com a lista de 43 (2026-10-18)

**Composição com os candidatos aprovados**:

| Bloco | Mecanismos | Total |
|---|---|---|
| A — Curadoria algorítmica | A1 Filter bubble · A2 Algorithmic amplification (com a via de contas priorizadas, 3.4-e) · A3 Algorithmic rabbit hole · A4 Algorithmic agenda-setting | 4 |
| B — Rede, grupo e difusão | B1 Homophily · B2 Echo chamber · B3 Group polarization · B4 Information cascades · B5 Moral contagion · B6 Partisan sorting · B7 Interpersonal political tension · B8 Online community radicalization · **Unfriending** (K04) · **Negative social influence** (K10) | 10 |
| C — Seleção e processamento individual da informação | C1–C8 · **Backfire effect** (K11) | 9 |
| D — Percepção dos outros | D1–D6 | 6 |
| E — Incentivos | E1–E3 | 3 |
| F — Interação | F1–F5 | 5 |
| G — Ecossistema e oferta | G1–G5 · **Partisan flagging** (K32) | 6 |
| **Total** | | **43** |

**Passo 4.1 — subgrupos no bloco B.** O critério do bloco B na T02 (14.5) já tem três partes: "o
processo depende de **quem está ligado a quem**, das **identidades de grupo** ou da **difusão
entre usuários**". Com 10 itens, a proposta é tornar essas três partes explícitas como subgrupos:

| Subgrupo | Pergunta | Mecanismos |
|---|---|---|
| **Seleção de laços** | Quem se liga a quem? | Homophily (B1); Unfriending (K04) |
| **Identidade de grupo** | Como as identidades se alinham e ganham saliência? | Partisan sorting (B6); Interpersonal political tension (B7) |
| **Influência e difusão** | Como as opiniões e os conteúdos mudam e circulam pelos laços? | Echo chamber (B2); Group polarization (B3); Negative social influence (K10); Moral contagion (B5); Information cascades (B4); Online community radicalization (B8) |

A divisão segue a distinção entre seleção e influência, clássica na análise de redes
**[conhecimento do agente; conferir dados bibliográficos: Shalizi e Thomas 2011]**, que o corpus
também usa (Sasahara et al. 2020: "Social influence and unfollowing"; Martel et al. 2024: "beyond
homophily"). Os outros blocos (A, C–G, com 3 a 9 itens) não precisam de subgrupos.

**Passo 4.2 — IDs.** A T02 numerou por ordem lógica dentro de cada bloco (D36, opção a), e os IDs já
foram propagados no texto e nas tabelas (T02.5, lotes 10b e 10c). As figuras (3, 4, 5–15) ainda não
foram atualizadas. Duas opções:

| | (a) Renumerar uma vez, em ordem lógica | (b) Acrescentar no fim, sem renumerar |
|---|---|---|
| Bloco A | sem mudança | sem mudança |
| Bloco B | por subgrupo: **B1** Homophily · **B2** Unfriending · **B3** Partisan sorting · **B4** Interpersonal political tension · **B5** Echo chamber · **B6** Group polarization · **B7** Negative social influence · **B8** Moral contagion · **B9** Information cascades · **B10** Online community radicalization (só B1 mantém o ID) | **B9** Unfriending · **B10** Negative social influence. Nos subgrupos, os IDs ficam fora de ordem (ex.: B1 e B9 em "seleção") |
| Bloco C | **C5** Backfire effect, logo depois de C4 (assimilação enviesada), de que é vizinho; C5–C8 atuais passam a C6–C9 | **C9** Backfire effect |
| Bloco G | **G6** Partisan flagging, no fim, ao lado de G4 e G5 (governança): sem renumerar | **G6** Partisan flagging |
| Custo | Renumerar B2–B8 e C5–C8 no texto, nas Tabelas 5 e 6, na 7.1, na 5.2 (*feedback loop*: B1 e B5 atuais) e nas Seções 9–11. É mecânico e pode ser feito de uma vez no passo 8.6, com tabela de correspondência, como a T02 fez (D3). As figuras ainda precisam ser refeitas de qualquer forma | Nenhum para os 39 |
| Leitura | Ordem lógica e subgrupos contíguos | Os novos ficam no fim, fora da lógica do bloco |

**Itens para aprovação**:

| Item | Proposta | Recomendação |
|---|---|---|
| **4.1-a** | **D7 = (a)**: manter os sete blocos (nenhum candidato pede bloco novo, 9) | Aprovar |
| **4.1-b** | Bloco B com três subgrupos (seleção de laços · identidade de grupo · influência e difusão), anunciados na abertura do bloco | Aprovar |
| **4.2** | IDs: **(a)** renumerar uma vez, em ordem lógica, no passo 8.6; ou **(b)** acrescentar no fim | **(a)**. Como as figuras ainda vão ser refeitas, o custo extra fica no texto e nas tabelas, e a renumeração é mecânica. Se você preferir não tocar de novo nos IDs já propagados, (b) é aceitável |

**Decisões do usuário — passos 4.1 e 4.2 (2026-10-18)**: **4.1-a aprovado** (D7 = a, sete blocos);
**4.1-b aprovado** (bloco B com três subgrupos); **4.2 = (a)**, renumerar uma vez, em ordem lógica,
no passo 8.6.

**Tabela de correspondência de IDs** (aplicada no passo 8.6; até lá, o relatório usa os IDs atuais,
com o novo entre parênteses quando houver risco de confusão):

| ID atual | Mecanismo | ID novo | Subgrupo (B) |
|---|---|---|---|
| A1–A4 | (sem mudança) | A1–A4 | — |
| B1 | Homophily | **B1** | Seleção de laços |
| — | Unfriending (K04) | **B2** | Seleção de laços |
| B6 | Partisan sorting | **B3** | Identidade de grupo |
| B7 | Interpersonal political tension | **B4** | Identidade de grupo |
| B2 | Echo chamber | **B5** | Influência e difusão |
| B3 | Group polarization | **B6** | Influência e difusão |
| — | Negative social influence (K10) | **B7** | Influência e difusão |
| B5 | Moral contagion | **B8** | Influência e difusão |
| B4 | Information cascades | **B9** | Influência e difusão |
| B8 | Online community radicalization | **B10** | Influência e difusão |
| C1–C4 | (sem mudança) | C1–C4 | — |
| — | Backfire effect (K11) | **C5** | — |
| C5 | Hostile media effect | **C6** | — |
| C6 | Illusory truth effect | **C7** | — |
| C7 | News avoidance | **C8** | — |
| C8 | Reinforcing spiral | **C9** | — |
| D1–D6, E1–E3, F1–F5 | (sem mudança) | idem | — |
| G1–G5 | (sem mudança) | G1–G5 | — |
| — | Partisan flagging (K32) | **G6** | — |

**Pontos sensíveis da renumeração** (passo 8.6): o segundo fechamento do *feedback loop* (5.2,
Figura 3) cita B5 (*moral contagion*), que passa a **B8**; o primeiro cita B1, que não muda. A
Seção 9.2 cita B7 (*interpersonal political tension*), que passa a **B4**, e G2, que não muda.

### 9.2 Passo 4.3 — Ligações affordance → mecanismos novos (2026-10-18)

**Regras** (decisão sobre T03-F04 e item 2.4-d): o ponto de partida são as ligações que o Gemini
propôs para as entradas que formam cada mecanismo. Cada uma é revista assim: (i) há um **passo
causal** (o que a affordance muda no mecanismo)? (ii) o nome da affordance é o **atual** (o lote 1
usa *Connection recommendation* = AF2 e *Context collapse* = AF6)? (iii) há **fonte** no corpus? Se
não houver, a ligação pode entrar como **justificativa teórica**, como já acontece na 7.1. (iv) O
**sinal** é "+" por padrão; "−" ou "±" só com fonte. Ligações que duplicam a de outro mecanismo, ou
que descrevem uma *feature* de outra affordance, são rejeitadas.

Affordances: AF1 Algorithmic content curation · AF2 Network-informed associating · AF3 Asymmetric
following · AF4 Social quantification · AF5 Replicability · AF6 Audience segmentation · AF7
Constraint affordance · AF8 Identifiability · AF9 Infinite scroll · AF10 Platform governance · AF11
Group/community formation.

#### Unfriending (K04 → B2)

| Ligação | Sinal | Passo causal | Base | Proposta |
|---|---|---|---|---|
| **AF3 → B2** | + | Cortar o laço é unilateral e custa um clique; sem reciprocidade, o corte não tem custo social. A definição de AF3 no paper já inclui "unilaterally disconnect at will" | Martel et al. 2024; Kaiser et al. 2022 | **Aprovar** (ligação central) |
| **AF8 → B2** | + | A identidade partidária visível no perfil revela o lado do outro antes de qualquer conversa e dispara o bloqueio | Martel et al. 2024: as contas-robô "identified as Democrats or Republicans" foram bloqueadas conforme o partido | **Aprovar** |
| **AF11 → B2** | + | Comunidades oferecem destinos para onde sair quando a insatisfação local passa do limiar, o que alimenta as saídas em cascata | Törnberg 2026 (simulação) | **Aprovar** |
| **AF6 → B2** | + | Com baixa segmentação, o usuário vê as postagens políticas de todos os contatos, inclusive as que considera inaceitáveis, o que é a ocasião do corte | Justificativa teórica. O cenário de Kaiser et al. 2022 (desinformação compartilhada por amigos) é compatível | Aprovar como justificativa teórica |
| **AF1 → B2** | **−** (condicional) | A personalização pode reduzir a insatisfação e desacelerar as saídas em cascata | Törnberg 2026: "slowing exit cascades" (p. 1) | **Aprovar**. Primeira ligação com sinal negativo |
| AF2 → B2 | + | (Gemini) a recomendação de contatos substitui o laço cortado por outro semelhante | Sem fonte; o passo é formação de laço, que já é AF2 → B1 | **Rejeitar** (duplica B1) |
| AF10 → B2 | + | (Gemini) banimentos e mudanças de regra provocam saídas em massa | É a migração de plataforma (G4), que já tem AF10 | **Rejeitar** (duplica G4) |

#### Negative social influence (K10 → B7)

| Ligação | Sinal | Passo causal | Base | Proposta |
|---|---|---|---|---|
| **AF2 → B7** | + | Conexões além da rede local aumentam o número de contatos com pessoas distantes, que é a condição da repulsão | Thurner et al. 2025 (mais conectividade → transição para a polarização, simulação) | **Aprovar** |
| **AF6 → B7** | + | A baixa segmentação mistura audiências e aumenta a dose de contato com o out-group | Krueger et al. 2017 (mais ligações entre os grupos → polarização, simulação) | **Aprovar** |
| **AF8 → B7** | + | A identidade visível marca o outro como out-group antes do argumento, e o afastamento depende de quem é a fonte | Nettasinghe et al. 2025 (animosidade ao out-group, simulação) | **Aprovar** |
| AF4 → B7 | + | (Gemini) contadores mostram a popularidade do out-group e provocam anticonformidade | Sem fonte e sem passo claro | **Rejeitar** |
| AF7 → B7 | + | (Gemini) mensagens curtas fazem as distâncias parecerem maiores | Especulativo. O efeito de brevidade é F3 (Jaidka [9]) | **Rejeitar** |
| AF11 → B7 | + | (Gemini) grupos delimitam fronteiras e provocam anticonformidade nas bordas | Duplica a câmara de eco (B5 novo) | **Rejeitar** |
| AF10 → B7 | + | (Gemini) denúncias como laços negativos no equilíbrio estrutural | É Partisan flagging (G6) | **Rejeitar** |

#### Backfire effect (K11 → C5)

| Ligação | Sinal | Passo causal | Base | Proposta |
|---|---|---|---|---|
| **AF3 → C5** | + | Seguir contas do outro lado traz mensagens contra-atitudinais regulares, que reforçam a posição prévia | Bail et al. [84] (experimento de campo), já citado em AF3 na 7.1 | **Aprovar** |
| **AF10 → C5** | **±** | Correções e etiquetas da plataforma acionam a reação. A forma muda o sinal: a etiquetagem individual leva ao recuo (+), e a verificação coletiva o reduz (−) | Kim et al. 2025 | **Aprovar** |
| **AF6 → C5** | + | A baixa segmentação gera exposição incidental ao outro lado, que é a ocasião do *backfire* | Masip et al. 2020 (exposição incidental maior entre usuários ativos) | **Aprovar** |
| AF8 → C5 | + | A identidade visível da fonte faz a mensagem ser lida como ataque do out-group | Justificativa teórica (Nordbrandt 2022: discordância percebida como intensa) | Aprovar como justificativa teórica |
| AF1 → C5 | + | (Gemini) o algoritmo insere conteúdo provocativo do outro lado | Sem fonte | **Rejeitar** |
| AF7 → C5 | + | (Gemini) a brevidade tira as nuances e faz a mensagem contrária parecer agressiva | Duplica F3 (Jaidka [9]) | **Rejeitar** |

#### Partisan flagging (K32 → G6)

| Ligação | Sinal | Passo causal | Base | Proposta |
|---|---|---|---|---|
| **AF10 → G6** | + | Sistemas de denúncia que afetam a distribuição são a condição do mecanismo (Creates) | Westermann e Coscia 2022 (simulação) | **Aprovar** (ligação central) |
| AF4 → G6 | + | (Gemini) contagens visíveis de remoções ou votos negativos confirmam a hostilidade do outro lado | Sem fonte; votos negativos não são denúncias | **Rejeitar** |
| AF7 → G6 | + | (Gemini) menus simplificados de denúncia baixam o custo da punição | É uma *feature* da ferramenta de denúncia, que pertence a AF10, e não a AF7 (restrição de formato) | **Rejeitar** (incorporar à justificativa de AF10) |

#### A2 com a via de contas priorizadas (fusão de K33, 3.4-e)

| Ligação | Sinal | Passo causal | Base | Proposta |
|---|---|---|---|---|
| **AF10 → A2** | **±** | A política de priorização (verificação, impulsionamento) concede alcance desigual a algumas contas. Se elas se comportam como as demais, a polarização pode cair; se são ideólogos teimosos, as câmaras de eco se acentuam | Arruda et al. 2024 (simulação) | **Aprovar**. A ligação AF1 → A2 já existe e não muda |

**Resumo**: **14** ligações recomendadas para aprovação (12 com fonte no corpus e 2 como
justificativa teórica). Três têm sinal diferente de "+": AF1 → B2 (−, condicional), AF10 → C5 (±) e
AF10 → A2 (±). **10** ligações do Gemini recomendadas para rejeição. As aprovadas viram linhas da
Tabela 6 e justificativas na 7.1, redigidas no passo 8.3.

**Item para aprovação**: **4.3**, aprovar as ligações marcadas "Aprovar" e rejeitar as marcadas
"Rejeitar", ou indicar as que quer mudar.

**Decisão do usuário — passo 4.3 (2026-10-18)**: **aprovadas as 14 ligações recomendadas e
rejeitadas as 10 marcadas "Rejeitar"**. As aprovadas entram na Tabela 6 e na 7.1 no passo 8.3. **T03.4
concluída.**

---

## 10. T03.5 — Cruzamento com os 39 da T02

| ID T02 | Mecanismo | No corpus L | Unidade | Observação |
|---|---|---|---|---|
| A1 | Filter bubble | **sim** | K01 | evidência mista no próprio corpus |
| A2 | Algorithmic amplification of divisive content | **sim** | K02 | — |
| A3 | Algorithmic rabbit hole | parcial | — | Liu et al. 2025 testa *rabbit holes* (p. 1), mas a IA não extraiu. É evidência **contra** |
| A4 | Algorithmic agenda-setting | não | — | — |
| B1 | Homophily | **sim** | K03 | — |
| B2 | Echo chamber | **sim** | K05 | evidência mista no próprio corpus |
| B3 | Group polarization | **sim** | K06 | — |
| B4 | Information cascades | parcial | — | Törnberg 2018 (contágio complexo) e Li et al. 2019 (cascatas virais) estão no L2, mas não foram extraídos como cascata |
| B5 | Moral contagion | **sim** | K07 | — |
| B6 | Partisan sorting | **sim** | K08 | — |
| B7 | Interpersonal political tension | não | — | — |
| B8 | Online community radicalization | parcial | — | Mølmen e Ravndal 2021 e O'Hara e Stevens 2015 (L4) foram extraídos como *echoing* (K05/K06) |
| C1 | Motivated reasoning | **sim** | K14 | — |
| C2 | Confirmation bias | **sim** | K12 | — |
| C3 | Selective avoidance | **sim** | K13 | o bloqueio vai para K04 se D6 = (a) |
| C4 | Biased assimilation | **sim** | K15 | — |
| C5 | Hostile media effect | não | — | — |
| C6 | Illusory truth effect | **sim** | K17 | uma fonte |
| C7 | News avoidance | não | — | estava na string e nenhum arquivo o extraiu |
| C8 | Reinforcing spiral | **sim** | K19 | Ohme 2021; mesmo problema de guarda-chuva (B02) |
| D1 | Vocal minority | não | — | — |
| D2 | Social proof | não | — | aparece só nas justificativas de affordance da IA |
| D3 | False consensus | parcial | K25 | "ilusão de consenso" em L2-11 |
| D4 | Pluralistic ignorance | parcial | K26 | — |
| D5 | Spiral of silence | **sim** | K27 | — |
| D6 | Exaggerated meta-perceptions | parcial | K26 | — |
| E1 | Social learning of outrage | **sim** | K30 | — |
| E2 | Identity signaling | **sim** | K31 | — |
| E3 | Metric-driven content production | não | — | B04 continua aberto |
| F1 | Online disinhibition effect | parcial | K28 | anonimato em Fang et al. 2024 |
| F2 | Dogpiling | não | — | — |
| F3 | Message brevity | não | — | — |
| F4 | Incivility contagion | não | — | — |
| F5 | Incivility exposure effect | parcial | — | Kobellarz et al. 2024 (*uncivil discourse*, L4) está só no resumo do arquivo, sem mecanismo |
| G1 | Gatekeeping decline | não | — | — |
| G2 | Propaganda feedback loop | não | — | — |
| G3 | Manufactured consensus | não | — | — |
| G4 | Platform migration | parcial | K04 | a cascata de saída (L1-08) é análoga; a migração só aparece nas justificativas de affordance |
| G5 | Perceived censorship | não | — | idem |

**Totais**: **16 sim · 9 parcial · 14 não**. **Candidatos novos**: K04, K10, K11, K18, K29, K32.

**Leitura**: o corpus L confirma o **núcleo** da tipologia (curadoria, rede, cognição) e não
alcança a **periferia** (interação, ecossistema, percepção dos outros). Pela T03-F01, a
ausência é esperada e não é evidência contra esses 14 mecanismos. Entre eles estão os mais
ligados ao jornalismo (G1, E3, C5, C7), o que pesa na decisão D1.


### 10.1 Passo 5.1 — Cruzamento atualizado depois da T03.3 (2026-10-18)

A tabela acima é a versão de 2026-10-17. As decisões da T03.3 mudam três status, e a leitura da
primeira página dos papers que sustentariam os itens "parcial" (regra 4) muda outros dois.

**Mudanças de status**:

| ID atual | Mecanismo | Antes | Agora | Motivo |
|---|---|---|---|---|
| D6 | Exaggerated meta-perceptions | parcial (K26) | **parcial**, com evidência que **qualifica** | K26 foi para D4 (7.3). Mas You e Lee 2024 compara as duas coisas: a percepção da norma do próprio grupo explica "8.4 times the variance explained by outgroup meta-perception" na polarização afetiva, e, no apoio à violência partidária, a metapercepção explica "0%" (abstract) |
| F1 | Online disinhibition effect | parcial (K28, anonimato) | **não** | Fang et al. 2024 só menciona o anonimato e o "anti-silence spiral" como citação de outra obra ([53] do artigo), e não como achado. O estudo trata da difusão de discursos feministas no Weibo (abstract; busca no texto completo) |
| F5 | Incivility exposure effect | parcial | **parcial (tangencial)** | Kobellarz et al. 2024 estuda se os *bubble reachers* (contas que alcançam públicos dos dois lados) geram discurso mais civil, no Brasil e no Canadá (abstract). Trata da civilidade em torno da exposição cruzada, e não do efeito da incivilidade sobre quem lê. Serve melhor para a discussão (2.3-e) |
| G4 | Platform migration | parcial (cascata de saída) | **não** | A cascata de saída de Törnberg 2026 ocorre dentro da plataforma e sem ação de governança. Foi para o Unfriending (B2 novo, 7.1) |

**Correção de uma decisão anterior (regra 7)**: a unidade **K28** (reatância opinativa / "espiral
anti-silêncio") foi aprovada no passo 3.1 (7.3, L3-17) e no passo 3.2 (8.3, Grupo 3) como **condição
de inversão de D5** (espiral do silêncio). A única fonte, Fang et al. 2024, não sustenta isso: a
expressão aparece numa frase de revisão de literatura, citando outra obra. **Proposta 5.1-c**: retirar
a condição de inversão da ficha de D5. Se os autores quiserem mantê-la, ela precisa da obra original
(a referência [53] de Fang et al.), que entraria pelo fluxo de literatura. O caso entra em T03-F03.
Fang et al. 2024 continua entre os incluídos, porque também é citado em L3-03 (K01), e a T03.7
confere se sustenta K01.

**Cruzamento atualizado**:

| Situação | Mecanismos (IDs atuais) | Total |
|---|---|---|
| **Sim** (unidade do corpus L corresponde) | A1, A2, B1, B2, B3, B5, B6, C1, C2, C3, C4, C6, C8, D5, E1, E2 | 16 |
| **Parcial** (papers do corpus servem às fichas, sem unidade própria) | A3 (Liu et al. 2025, evidência **contrária**: efeitos limitados de *rabbit holes*, p. 1) · B4 (Törnberg 2018: câmaras de eco facilitam a difusão viral de desinformação como contágio complexo, simulação) · B8 (Mølmen e Ravndal 2021: a internet facilitou a radicalização por "information provision, as well as amplifying group polarisation and legitimising extreme ideology and violence through echoing", com fatores offline também decisivos) · D3 (Brown et al. 2022, simulação) · D4 (You e Lee 2024: norma do próprio grupo "exaggerated", três estudos e experimento-piloto; Brown et al. 2022) · D6 (You e Lee 2024, evidência que qualifica) · F5 (Kobellarz et al. 2024, tangencial) | 7 |
| **Não** | A4, B7, C5, C7, D1, D2, E3, F1, F2, F3, F4, G1, G2, G3, G4, G5 | 16 |

**Itens para aprovação**:

| Item | Proposta | Recomendação |
|---|---|---|
| **5.1-a** | Validar os 16 "sim" (as correspondências já aprovadas no passo 3.2) | Aprovar |
| **5.1-b** | Validar os 7 "parcial" e citar os papers indicados nas fichas desses mecanismos (Opção C), com a direção indicada (contrária em A3; qualificadora em D6) | Aprovar |
| **5.1-c** | Corrigir a decisão do passo 3.1/3.2 sobre K28: retirar a condição de inversão da ficha de D5 | Aprovar |
| **5.1-d** | F1 e G4 passam de "parcial" para "não" | Aprovar |

**Decisões do usuário — passo 5.1 (2026-10-18)**: **5.1-a, b e d aprovados**; **5.1-c: K28 removido
de D5**. A ficha de D5 não terá a condição de inversão ("espiral anti-silêncio"). Correção registrada
no `INDEX.md`. Cruzamento final: **16 sim, 7 parcial, 16 não**.

### 10.2 Passo 5.2 — Os 16 mecanismos sem suporte no segundo levantamento (2026-10-18)

**Quais são, por bloco**:

| Bloco | Mecanismos sem suporte (IDs atuais) | No bloco |
|---|---|---|
| A | A4 Algorithmic agenda-setting | 1 de 4 |
| B | B7 Interpersonal political tension | 1 de 8 |
| C | C5 Hostile media effect · C7 News avoidance | 2 de 8 |
| D | D1 Vocal minority · D2 Social proof | 2 de 6 |
| E | E3 Metric-driven content production | 1 de 3 |
| F | F1 Online disinhibition · F2 Dogpiling · F3 Message brevity · F4 Incivility contagion | **4 de 5** |
| G | G1 Gatekeeping decline · G2 Propaganda feedback loop · G3 Manufactured consensus · G4 Platform migration · G5 Perceived censorship | **5 de 5** |

**Leitura**: a ausência se concentra nos blocos **F (interação)** e **G (ecossistema e oferta)**,
justamente os que a string não alcança (T03-F01: o bloco obrigatório tem nomes de mecanismos de rede
e de cognição). No bloco G, o único mecanismo com base no segundo levantamento é o novo, G6 (Partisan
flagging). Quatro dos 16 são os mais ligados ao jornalismo (C5, C7, E3, G1). Pela D1 (Opção C), todos
continuam: a ausência é efeito do recorte da busca, e não evidência contra eles. As fontes de cada um
já foram conferidas nos PDFs na T02.

**Um caso a reexaminar: C7 (news avoidance)**. O termo estava na string, e nenhuma lista do Gemini o
extraiu. Mas Fletcher et al. 2021, entre os incluídos, mostra que "in every country covered, more
people consume no online news at all than occupy partisan online echo chambers" (p. 1). Isso não
sustenta C7 como mecanismo de polarização, mas dá o tamanho da evitação de notícias online e serve à
ficha de C7 como contexto. Se aprovado, C7 passa de "não" para **"parcial"** (cruzamento: 16 sim, 8
parcial, 15 não).

**Itens para aprovação**:

| Item | Proposta | Recomendação |
|---|---|---|
| **5.2-a** | Manter os 16 mecanismos (D1 = C), com as fontes atuais | Aprovar |
| **5.2-b** | No Apêndice A (A.3) e na Table A1, cada mecanismo traz a **origem** (primeira lista / segundo levantamento / ambos) e o **suporte no segundo levantamento** (sim / parcial / não). Os 16 aparecem como "primeira lista; não" | Aprovar |
| **5.2-c** | No A.3, uma frase de leitura: a ausência se concentra nos blocos F e G, que a string não alcança, o que é coerente com o recorte declarado (T03-F01). Na limitação correspondente (A.4 ou 9.2), apontar uma busca dirigida a esses blocos como trabalho futuro | Aprovar |
| **5.2-d** | C7: citar Fletcher et al. 2021 como contexto na ficha (prevalência da não exposição a notícias online) e passar C7 a "parcial" | Aprovar |

**Decisões do usuário — passo 5.2 (2026-10-18)**: **5.2-a** (manter os 16, com as fontes atuais), **5.2-b**, **5.2-c** e **5.2-d aprovados**. Cruzamento final: **16 sim, 8 parcial (com C7), 15 não**.

### 10.3 Passo 5.3 — Régua aplicada aos 39 (D10) (2026-10-18)

**Base**: as fichas atuais da Seção 6 (cópia de revisão, leitura de 2026-10-18), as fontes já
conferidas na T02 e os papers do segundo levantamento aprovados para as fichas (8.3, 10.1, 10.2).
IDs atuais, com o novo entre parênteses quando muda (9.1).

**Regra operacional proposta para *Evidence strength*** (detalha o 2.1-e, que diz "estudos do
fenômeno fora da plataforma não contam"): conta como evidência do papel da plataforma o estudo com
**dados de uso real de plataforma**: experimento de campo ou quase-experimento numa plataforma, dados
de rastro ou de conteúdo de plataforma, ou survey sobre o uso de plataforma. **Não contam**:
experimento de laboratório com estímulos fora de plataforma, estudo de mídia tradicional e
simulação (que só dá Plausible). Teto: **Strong** = experimento ou quase-experimento em plataforma,
com replicação por mais de um estudo; **Moderate** = um experimento em plataforma, ou dados
observacionais ou surveys de plataforma consistentes; **Plausible** = só simulação, teoria ou
evidência do fenômeno fora da plataforma.

**Consequência esperada**: os mecanismos que a plataforma só **hospeda** (C1, C4, C5) ficam com
*Plausible*, o que é coerente: por definição, não há evidência de que a plataforma mude o processo,
só de que ela oferece a ocasião. O mesmo ocorre com mecanismos cujo fenômeno é forte fora da
plataforma, mas sem estudo em plataforma (B3, C6, D3, D4, D6). A força do fenômeno vai para o texto
da definição (2.1-e).

**Tabela proposta** (atual → proposto; "=" quando não muda):

| ID | Mecanismo | Platform role | Direction | Evidence strength | Base da proposta |
|---|---|---|---|---|---|
| A1 | Filter bubble | Amplifies → **Creates** | **Mixed** | Mixed → **Strong** | Personalização não existe fora da plataforma (2.2-c). Experimentos que manipulam recomendações (Liu et al. 2025) e dados do Facebook (Bakshy [45]), com resultados que não confirmam efeito forte |
| A2 | Algorithmic amplification | = Amplifies | **Reinforcing** | Moderate–mixed → **Moderate** | Auditoria pré-registrada (Milli [14]); dados de Rathje [38]. A via de contas priorizadas (Arruda et al. 2024, simulação) é Mixed e fica dita no texto |
| A3 | Algorithmic radicalization | Amplifies → **Creates** | **Mixed** | Mixed → **Strong** | A sequência de recomendações exige o sistema de recomendação (mesma lógica de A1). Auditoria (Ribeiro [56]), painel (Hosseinmardi [57]) e experimento (Liu et al. 2025), com resultados opostos |
| A4 | Algorithmic agenda-setting | = Amplifies | **Reinforcing** | = Plausible | Agenda-setting existe na mídia tradicional. Elmas [54] mostra a manipulação dos *trends*, mas não o efeito na percepção |
| B1 (B1) | Homophily | Hosts & amplifies → **Amplifies** | **Reinforcing** | composto → **Moderate** | Dados de redes (Cinelli [46]) e experimento de campo sobre *follow-back* (Martel et al. 2024). O efeito da recomendação vem de simulação (Santos [59]) |
| B2 (B5) | Echo chamber | = Amplifies | **Mixed** | Mixed → **Moderate** | Dados de plataforma (Cinelli [46]) × surveys que encontram câmaras de eco pequenas (Fletcher et al. 2021; Dubois e Blank 2018; Geiß et al. 2021) |
| B3 (B6) | Group polarization | = Amplifies | **Reinforcing** | composto → **Plausible** | Fenômeno forte em laboratório ([61]); online, só estudos de caso qualitativos (Mølmen e Ravndal 2021). A ficha já diz "more limited online" |
| B4 (B9) | Information cascades | = Amplifies | **Reinforcing** | = Moderate | Dados de plataforma (Vosoughi [51]; Del Vicario [52]); simulação (Törnberg 2018) |
| B5 (B8) | Moral contagion | = Amplifies | **Reinforcing** | = Moderate | Dados de plataforma (Brady [67]; Rathje [38]) |
| B6 (B3) | Partisan sorting | Hosts (amplifies) → **Amplifies** | **Reinforcing** | Moderate → **Plausible** | O *sorting* é forte fora da plataforma (Mason [62]); a via de plataforma vem de modelo (Törnberg 2022). A ficha já diz "direct evidence of this amplification is limited" |
| B7 (B4) | Interpersonal political tension | = Amplifies | **Reinforcing** | = Moderate | Dois surveys com usuários de Facebook e Twitter (Tanyel e Windeler [5]) |
| B8 (B10) | Online community radicalization | = Amplifies | **Reinforcing** | = Moderate | Testemunhos e registros de chat (Munn [76]); estudos de caso (Mølmen e Ravndal 2021), que também apontam fatores offline |
| C1 | Motivated reasoning | = Hosts | **Reinforcing** | composto → **Plausible** | Hospeda (2.2-a). Evidência do fenômeno fora da plataforma ([63], [64]) |
| C2 | Confirmation bias | Hosts → **Amplifies** | **Mixed** | composto → **Moderate** | A plataforma amplia a seleção (Garrett [107], survey sobre fontes online). Atenuação: usuários ativos mais expostos ao outro lado (Masip et al. 2020) |
| C3 | Selective avoidance | Hosts & amplifies → **Hosts** | **Mixed** | Mixed → **Plausible** | Sem o corte de laços (que foi para B2 novo, D6), não resta via de plataforma demonstrada. Heseltine [108] é navegação em sites de notícias; a ficha já diz que o vínculo é teórico. **Outcome**: Structural, Ideological → **Ideological** |
| C4 | Biased assimilation | = Hosts | **Reinforcing** | Moderate → **Plausible** | Hospeda. Evidência de laboratório (Lord [65]); Bakshy [45] mostra só que há ocasião (exposição cruzada) |
| C5 (C6) | Hostile media effect | = Hosts | **Reinforcing** | Moderate → **Plausible** | Hospeda. Estudo com TV (Vallone [23]) |
| C6 (C7) | Illusory truth effect | = Amplifies | **Reinforcing** | Strong → **Plausible** | O "Strong" era do fenômeno (Hasher [66], laboratório). Nenhum estudo em plataforma (Secară e Opre 2026 é experimento com notícias, fora de plataforma) |
| C7 (C8) | News avoidance | Hosts & amplifies → **Amplifies** | **Reinforcing** | = Plausible | Ambiente fragmentado facilita evitar (Toff e Kalogeropoulos [79]; Urman [109]; Fletcher et al. 2021). Vínculo com a polarização indireto |
| C8 (C9) | Reinforcing spiral | = Amplifies | **Reinforcing** | = Plausible | Sem mudança até o B02. Ohme 2021 entra como evidência |
| D1 | Vocal minority | = Amplifies | **Reinforcing** | = Moderate | Oito estudos de survey (Bor e Petersen [68]) |
| D2 | Social proof | = Amplifies | **Reinforcing** | = Moderate | Experimento de campo randomizado numa plataforma (Muchnik [41]), um só estudo |
| D3 | False consensus | Hosts & amplifies → **Amplifies** | **Reinforcing** | Moderate → **Plausible** | Fenômeno de laboratório (Ross [39]); simulação (Brown et al. 2022) |
| D4 | Pluralistic ignorance | Hosts & amplifies → **Amplifies** | **Reinforcing** | Moderate → **Plausible** | Estudo em campus ([40]); surveys sem recorte de plataforma (You e Lee 2024); simulação (Brown et al. 2022) |
| D5 | Spiral of silence | = Amplifies | **Mixed** | Mixed → **Moderate** | Surveys e dados sobre expressão online (Cheong et al. 2022; Geiß et al. 2021); simulação (Banisch et al. 2022). A ficha já diz "evidence for its operation online is mixed" |
| D6 | Exaggerated meta-perceptions | = Amplifies | **Reinforcing** | composto → **Plausible** | Surveys sem recorte de plataforma (Moore-Berg [11]). You e Lee 2024 qualifica a importância do mecanismo (8.4 vezes menos variância que a norma do in-group) |
| E1 | Social learning of outrage | = Amplifies | **Reinforcing** | Moderate → **Strong** | Estudos observacionais pré-registrados e experimentos (Brady [13]); dados de mais de um milhão de posts (Lindström [71]); experimento sobre o desenho do feedback (Konovalova et al. 2023). Mais de uma equipe |
| E2 | Identity signaling | = Amplifies | **Reinforcing** | Plausible → **Moderate** | Dados do Facebook sobre engajamento seletivo partidário (Garz et al. 2019) |
| E3 | Metric-driven content production | Creates (incentive) → **Amplifies** | **Reinforcing** | = Plausible | Pela 6.1, o processo existe fora da plataforma com lógica essencialmente idêntica: redações já se ajustavam a audiência, tiragem e índices de audiência. A plataforma muda a velocidade e a visibilidade do sinal (métricas em tempo real). B04 continua aberto |
| F1 | Online disinhibition effect | = Amplifies | **Mixed** | Mixed → **Moderate** | Oito estudos de survey (Bor e Petersen [68]) com apoio limitado à tese |
| F2 | Dogpiling | = Amplifies | **Reinforcing** | Plausible → **Moderate** | Dados de 532.197 comentários numa plataforma de petições (Rost [73]) |
| F3 | Message brevity | = Amplifies | **Reinforcing** | Plausible → **Moderate** | Experimento natural no Twitter (Jaidka [9]), um só estudo. Resolve a pendência da 9.1 (AF7/F3 × Tabela 5) |
| F4 | Incivility contagion | = Amplifies | **Reinforcing** | = Moderate | Experimento num fórum online (Gervais [50]) |
| F5 | Incivility exposure effect | = Amplifies | **Reinforcing** | = Moderate | Experimento online com amostra representativa (Anderson [49]) |
| G1 | Gatekeeping decline | = Amplifies | **Mixed** | = Plausible | A ficha diz que o *gatekeeping* é "redistributed" e não perdido ([115], [116]) |
| G2 | Propaganda feedback loop | = Amplifies | **Reinforcing** | composto → **Moderate** | Análise em larga escala do ecossistema de mídia dos EUA (Benkler [75]). O recorte nacional vai para o texto |
| G3 | Manufactured consensus | = Amplifies | **Reinforcing** | Mixed → **Moderate** | Dados de plataforma sobre *trends* falsos (Elmas [54]). Nenhum achado contrário citado |
| G4 | Platform migration | Amplifies or hosts → **Amplifies** | **Mixed** | Mixed → **Moderate** | Dados de plataforma (Horta Ribeiro [77]): menos atividade, mas mais toxicidade em quem migrou |
| G5 | Perceived censorship | = Amplifies | **Reinforcing** | = Plausible | Survey com usuários moderados (Myers West [78]), que documenta as crenças e não o efeito |
| **B2 novo** | Unfriending | Amplifies | Reinforcing | Strong | Decidido em 8.4 |
| **B7 novo** | Negative social influence | Amplifies | Mixed | Plausible | Decidido em 8.6 |
| **C5 novo** | Backfire effect | Amplifies | Mixed | Moderate | Decidido em 8.5 |
| **G6** | Partisan flagging | Creates | Reinforcing | Plausible | Decidido em 8.8 |

**Resumo das mudanças nos 39**:
- *Platform role*: 11 mudam. **Creates**: A1, A3 (e G6, novo). **Hosts**: C1, C3, C4, C5. O resto é
  **Amplifies**. E3 deixa de ser o único "Creates".
- *Direction* (coluna nova): **Mixed** em 9 dos 39 (A1, A3, B2, C2, C3, D5, F1, G1, G4), mais B7 e
  C5 novos; **Reinforcing** nos demais; nenhum **Attenuating**.
- *Evidence strength* (39): **Strong** 3 (A1, A3, E1; mais B2 novo), **Moderate** 20, **Plausible**
  16 (os itens Hosts e os de fenômeno forte fora da plataforma). Antes, só C6 era Strong.

**Efeitos fora da tabela** (para o passo 8.3): a frase da 9.1 sobre "only a single mechanism […]
robust, direct causal evidence" deixa de valer (pendência aberta no INDEX); a terceira limitação da
9.2 ganha a regra operacional; a ficha de E3 muda a frase "creates an incentive that did not exist in
this form"; a ficha de C6 deixa de chamar a evidência de forte para o papel da plataforma.

**Itens para aprovação**:

| Item | Proposta | Recomendação |
|---|---|---|
| **5.3-a** | A regra operacional de *Evidence strength* (o que conta como evidência de plataforma) | Aprovar |
| **5.3-b** | A coluna *Platform role* (11 mudanças) | Aprovar. Pontos que pedem atenção: A1 e A3 → Creates; C2 → Amplifies; C3 → Hosts; E3 → Amplifies |
| **5.3-c** | A coluna *Direction* | Aprovar |
| **5.3-d** | A coluna *Evidence strength* | Aprovar. Pontos que pedem atenção: os rebaixamentos de C6 (Strong → Plausible), B3, B6, C4, C5, D3, D4 e D6, e as elevações de A1, A3, E1, E2, F2 e F3 |
| **5.3-e** | Outcome de C3: Structural, Ideological → Ideological (consequência da D6) | Aprovar |

**Decisões do usuário — passo 5.3 (2026-10-18)**: **5.3-a a e aprovados**. Regra operacional de *Evidence strength* adotada; as colunas *Platform role*, *Direction* e *Evidence strength* dos 39 ficam como na tabela; C3 passa a outcome Ideological. **D10 decidida. T03.5 concluída.**


---

## 11. T03.6 — O que fazer na versão final do paper

A pergunta do usuário: descartar os 39 e adotar a lista nova, o que obrigaria a remover os
artigos e as passagens em que são citados, ou há outra opção?

**Uma distinção que muda a resposta**: o problema da v1 **não está nas obras citadas**. As
fontes dos 39 existem e foram conferidas nos PDFs na T02. O problema é que o paper não diz
**como** elas foram escolhidas. São coisas diferentes:
- a **fonte definidora** de um mecanismo (Noelle-Neumann para a espiral do silêncio, Kunda
  para o raciocínio motivado) não precisa vir de busca. Ela é escolhida por definir o termo
  (R1), e quase sempre é anterior à mídia social;
- a **evidência de que a mídia social atua sobre o mecanismo** (Q5, Q6) é que precisa de um
  procedimento declarado. É esse o papel que o corpus L pode cumprir.

Por isso, remover citações só faz sentido para os mecanismos que saírem da tipologia.

| | Opção A — Substituir | Opção B — Validação mínima | **Opção C — Dupla origem declarada** |
|---|---|---|---|
| O que é | A lista do corpus L vira a tipologia | Os 39 ficam; o levantamento entra no método só como checagem | Os 39 ficam; os candidatos novos aprovados entram; cada item declara de onde veio (âncoras, corpus L, ambos) e o que o corpus diz sobre o papel da plataforma |
| Mecanismos | 21 (perdem-se 14, entre eles G1, E3, C5, C7) | 39 | 39 + até 6 |
| Citações da v1 | remover as dos 14 que saem; reescrever 5–11 | nenhuma mudança | nenhuma remoção; acréscimo de fontes do corpus L (BibTeX via Crossref, G1) |
| Rastreabilidade | total para o que fica, mas apoiada num corpus circular (F01) e numa extração com erros (F03) | fraca: o método continua sem dizer como os 39 surgiram | **cada item tem trilha**: fonte definidora + suporte no corpus L, ou a declaração de que veio só das âncoras |
| Custo | muito alto: refaz T02.3–T02.5 (199 ajustes), Tabelas 5–6, Figuras 3–15, e exige conferir os 226 PDFs | baixo | médio: método (4.3, 6.1, Figura 1), fichas novas, coluna de origem ou Table S1, conferência dos PDFs que sustentam cada item |
| Risco com revisor | alto: string circular e corpus dominado por modelos | alto: "por que a busca não gerou a lista?" | baixo, se as limitações forem declaradas |
| Para *Journalism and Media* | perde os mecanismos ligados ao jornalismo | — | mantém e ainda ganha a discussão sobre a contribuição da plataforma |

**Recomendação: Opção C.** Ela responde ao problema do usuário (rastreabilidade) sem
depender da memória dos autores (T01-D2), aproveita a T02 e transforma as falhas do
levantamento em conteúdo: a evidência de atenuação e de causalidade reversa vai para a
discussão (6.3). Ela também resolve a T02.4 e o B01. A Table S1 deixa de precisar da coluna
"como a fonte foi encontrada", que dependia dos autores, e passa a ter uma coluna "suporte no
corpus L" (sim / parcial / não, com os papers), que é verificável.

**O que a Opção C exige** (antes de redigir):
1. **Registrar o protocolo** (P1–P3): exportação do Lens, data, ferramentas, prompts.
2. **Conferência humana da triagem** (T03-F02): os 226 incluídos e uma amostra dos excluídos.
3. **T03.7**: conferir nos PDFs os papers que sustentam cada unidade, com prioridade para os
   seis candidatos novos e para a evidência contrária.
4. **Decidir a string** (D2): declarar a limitação ou complementar a busca.
5. **Um fato que só os autores sabem**: como os 41 da v1 foram reunidos. A Opção C precisa só
   de uma frase honesta, por exemplo "a tipologia foi montada a partir das obras âncora e do
   conhecimento dos autores, e depois testada contra um levantamento estruturado". Ela fica
   como `[AUTORES: confirmar]`.

### 11.1 Proposta: Apêndice A, identificação dos mecanismos (pedido do usuário, 2026-10-18)

**Pedido**: um apêndice que descreva a metodologia do segundo levantamento e traga detalhes do
processo de levantamento da primeira lista.

**Por que um apêndice resolve mais de um problema**: hoje há três textos previstos sobre o mesmo
processo, todos parados: T01-A10 (documentar o *chaining* na 4.3), T01-A11 (Figura 1) e a Table
S1 do B01 (trilha de auditoria). A T02.4 (processo de identificação) foi adiada. Um único
apêndice pode absorver os quatro. Na 4.3 e na 6.1 fica só um resumo de duas ou três frases, com
remissão ao apêndice. No template MDPI, os apêndices entram como "Appendix A", com tabelas e
figuras próprias (Table A1, Figure A1) **[conferir no template]**.

**Estrutura proposta** (conteúdo em português aqui; o texto do paper sai em inglês no passo 8.1):

| Parte | Conteúdo | O que já está documentado | O que falta |
|---|---|---|---|
| **A.1 Primeira lista (v1)** | Como os 41 mecanismos da v1 foram identificados e como chegaram aos 39 atuais | (i) O que o paper declara: *theoretical review* (Paré et al. [15]), *citation chaining* a partir de quatro obras âncora (Harris et al. [2], Arora et al. [3], Tölle e Trier [4], Tanyel e Windeler [5]) e o critério de inclusão por item, "anchored in at least one primary source with an explicit operational definition" (4.3; T01 §4). (ii) A **consolidação** feita nesta revisão: teste de mecanismo (Q1–Q4), regras de nome (R1–R7), base única dos blocos (locus do processo) e o resultado 41 → 39, com fusões (M4 → B4, A3 → B1, E4 → E1), exclusão (A4) e divisões (M1, D3), em 9 → 7 blocos (T02, Seções 12–14) | Os fatos de T01-P6, que só os autores sabem: direção do *chaining* (para trás, para frente), iterações, critério de parada, janela temporal, exclusões, regras de fusão na v1, como entraram as obras de 2023–2025, quem conduziu e se houve uso de IA. Sem eles, A.1 fica com placeholders `[AUTORES: …]` |
| **A.2 Segundo levantamento** | Objetivo, busca, triagem, extração, conferência, consolidação e inclusão | Tudo o que está na tabela 5.1 e nas Seções 5.5–5.6, 6 e 8: Lens, 13/10/2026, string e filtros, 886 registros; Gemini (web) na triagem e Gemini notebook (web) na extração, de 11 a 18/10/2026; conferência humana; 226 elegíveis; 66 entradas → 33 unidades → 21 mecanismos (teste Q1–Q6); 147 papers incluídos na síntese. Fluxograma (Figure A1): 886 → 226 → 147 | Os números finais (dependem da T03.3 e da T03.7); a fonte única para os elegíveis (226 declarados × 223 com PDF); a confirmação do nome da ferramenta de extração |
| **A.3 Relação entre as duas listas** | O que o segundo levantamento confirma, acrescenta e não alcança | Cruzamento da Seção 10 (16 sim, 9 parcial, 14 não) e os candidatos novos | Depende de D1 (passo 6.1) e da T03.3. Pode virar a **Table A1**: cada mecanismo × fonte definidora × suporte no segundo levantamento, que é o que o B01 queria |
| **A.4 Uso de IA e limitações do procedimento** | Declaração do uso de IA e o que a conferência humana cobre | Comentário 4 (5.5): o que foi conferido e o que não foi; string orientada a mecanismos conhecidos (T03-F01); abstracts ausentes; omissões do Gemini (5.6) | A política do periódico sobre IA (P8). Parte disso pode ir para a 9.2 (limitações) em vez do apêndice |

**Duas formas de dar "detalhes do processo da primeira lista"** (D12):
- **(a) Perguntar aos autores** (retomar a T01-D2, pausada): é a única forma de afirmar como os
  41 foram de fato encontrados. As perguntas já estão prontas na T01-P6.
- **(b) Rastreabilidade reconstruída** (método do B01, opção 2): para cada fonte dos 39,
  conferir se ela está nas referências das quatro âncoras (um passo de *chaining*), nas de outra
  fonte já incluída (dois passos) ou em nenhuma ("fora da cadeia"). Isso mostra que **existe** um
  caminho, e não que foi **o** caminho usado, e o texto teria de dizer "rastreabilidade
  reconstruída". Um dado já disponível ajuda aqui: só 4 das 106 referências do paper apareceram no
  segundo levantamento (T03-I04), o que é coerente com uma primeira lista montada por *chaining*,
  e não por busca.
- **Recomendação**: **(a) + (b)**. A reconstrução (b) dá ao apêndice uma tabela verificável sem
  depender da memória dos autores. As respostas (a) confirmam ou corrigem cada linha.

**Cuidado que vem da T02.4** (roteiro 4.1 da T02): os critérios de consolidação da revisão de
2026-10 (Q1–Q4, R1–R7, locus) não podem ser apresentados como se tivessem guiado a identificação
original. Em A.1, eles aparecem como uma **etapa posterior de consolidação**.

**Decisões do usuário — Apêndice A (2026-10-18)**

| # | Decisão | Efeito |
|---|---|---|
| D11 | **Estrutura aprovada** (A.1 a A.4) | Passo 8.1 (a) concluído. A redação fica para a T03.8 |
| D12 | **(a) confirmada**: os autores darão os detalhes do processo da primeira lista mais tarde. **(b) não será feita**. Fato informado pelo usuário: a primeira lista foi montada **inicialmente com o auxílio de uma IA generativa, o Claude (web)** | A.1 declara o uso do Claude (web) na montagem inicial. Os demais fatos de T01-P6 (direção do *chaining*, iterações, critério de parada, janela temporal, exclusões, fusões, quem conduziu, período e forma de uso da IA) ficam como `[AUTORES: …]` até a resposta. Sem a reconstrução (b), A.1 não terá tabela de trilha. A Table A1 (A.3) continua possível, porque vem do cruzamento com o segundo levantamento. **Interpretação do agente, a confirmar**: "já foi feito inicialmente com o auxílio de uma IA generativa" se refere à montagem da primeira lista |


### 11.2 Passo 6.3 — Conferência humana da triagem (2026-10-18)

**Decisão do usuário**: a conferência **já foi feita**, na forma descrita no passo 1.1 (5.5): avaliação
dos títulos dos elegíveis e da coerência dos mecanismos com os artigos indicados e com a pesquisa
anterior. **D3 decidida**: nenhuma conferência adicional. O que ela não cobriu (os 663 excluídos não
reavaliados; triagem sobretudo por título) entra nas limitações do Apêndice A (A.4), como aprovado no
comentário 4 de 5.5.

### 11.3 Passo 6.4 — Declaração do uso de IA generativa (2026-10-18)

**Política da MDPI** (P8). As páginas da MDPI recusaram o acesso automático (HTTP 403:
`mdpi.com/ethics`, o anúncio 5687 e o blog de 2025-03-19). O que segue vem dos trechos devolvidos
pela busca e precisa ser conferido na página de ética **[conferir]**:
- modelos de linguagem **não podem ser autores**;
- o uso deve ser declarado nos **Acknowledgments**, com as ferramentas e o modo de uso, e o
  procedimento deve ser descrito em detalhe em **Materials and Methods**;
- uso só para formatar, revisar ou editar texto não precisa ser declarado (blog de 2025, citando a
  orientação da STM). Usos além disso precisam;
- os autores respondem integralmente pela originalidade, validade e integridade do conteúdo.

**O que precisa ser declarado neste paper** (fatos do relatório):

| Uso | Ferramenta | Etapa | Fonte do fato |
|---|---|---|---|
| Montagem inicial da primeira lista de mecanismos | Claude (Anthropic), web | primeira lista | usuário, D12 (11.1) |
| Triagem dos 886 registros do Lens | Gemini (Google), web | segundo levantamento, 11 a 18/10/2026 | usuário, 5.5 |
| Extração dos mecanismos a partir dos PDFs | **Gemini Notebook** (web), nome atual do NotebookLM, segundo o usuário (2026-10-18) | segundo levantamento, 11 a 18/10/2026 | usuário, 5.5 |
| Consolidação dos mecanismos, conferência das atribuições nos PDFs e revisão e redação de trechos do texto (definições, Seção 5.3, ajustes) | Claude (Anthropic), via Claude Code. Modelo desta sessão: Claude Opus 5.5 | revisão do manuscrito (T01 a T03) | relatórios T01–T03 |

O último uso vai além de editar texto: inclui análise (consolidação, aplicação da régua) e redação de
trechos novos. Pela política, deve ser declarado.

**Decisões do usuário — passo 6.4 (2026-10-18)**: **6.4-a a c aprovados**. Produto de extração: **Gemini
Notebook** (nome atual do NotebookLM, segundo o usuário). Continua em aberto o *placeholder* sobre o
período e o modelo do Claude usado na primeira lista. **T03.6 concluída.**

**Itens para aprovação**:

| Item | Proposta | Recomendação |
|---|---|---|
| **6.4-a** | **Onde**: nos *Acknowledgments*, as ferramentas e o uso; no método, o procedimento (uma frase na 4.3 e o detalhe no Apêndice A, partes A.1, A.2 e A.4) | Aprovar |
| **6.4-b** | **O quê**: os quatro usos da tabela acima, com a conferência humana de cada etapa | Aprovar. O quarto uso (Claude Code na revisão) depende de você concordar que ele seja declarado |
| **6.4-c** | **Texto dos *Acknowledgments*** (abaixo), com *placeholders* para o que só os autores sabem | Aprovar ou ajustar |
| **6.4-d** | Conferir a política na página de ética da MDPI e nas instruções da *Journalism and Media* antes da submissão (P8) | O usuário confere, porque o agente não conseguiu abrir as páginas |

**Texto proposto para os *Acknowledgments*** (em inglês):

> During the preparation of this study, the authors used generative AI tools as follows. Claude
> (Anthropic, web interface) assisted in the initial compilation of the first list of mechanisms
> [AUTORES: período e modelo, se disponíveis]. Gemini (Google, web interface) was used to screen the
> records retrieved from Lens, and Gemini Notebook (Google, web interface) was used to extract candidate
> mechanisms from the full texts of the eligible papers, between 11 and 18 October 2026. Claude
> (Anthropic), through Claude Code, assisted in consolidating the extracted mechanisms, checking their
> attributions against the full texts, and revising and drafting parts of the manuscript. The
> procedure and the human verification applied at each stage are described in Section 4.3 and
> Appendix A. The authors reviewed and edited all output and take full responsibility for the
> content of this publication.

---

## 12. Decisões necessárias

Em ordem de roteiro. Cada decisão é tomada no passo indicado (Seção 4.2).

| # | Passo | Decisão | Opções | Recomendação |
|---|---|---|---|---|
| D4 | 2.1, 2.4 | Régua: Q5 e Q6 (6.2) e coluna *Claim* em duas dimensões (papel e direção) | aprovar · ajustar · rejeitar | **Decidida em 2026-10-18: aprovada** (6.4–6.7) |
| D5 | 3.3 | Candidatos novos K04, K10, K11, K18, K29, K32 (**decidida em 2026-10-18**: entram K04, K10, K11, K32; não entram K18, K29) | item a item. O B03 vetava mecanismos novos "até terminar a revisão dos 41", e essa revisão terminou (T02.3) | Entrar, **condicionado à T03.7**: K04, K11, K10. Entrar como *Plausible*: K18, K32. Avaliar: K29 (Q3 fraco) |
| D6 | 3.3 (com K04) | Dissolução de laços (K04) (**decidida em 2026-10-18: (a)**) | (a) item próprio em B · (b) manter dentro de C3, como decidido na T02 (D34, 14.5) | **(a)**: o corpus L dá base própria (Kaiser et al. 2022; Martel et al. 2024), e o outcome (estrutural) difere do de C3. Altera D34 |
| D8 | 3.4 | Destinos da 8.2 (K09, K16, K19–K26, K28, K33) (**decidida em 2026-10-18**, 8.10) | aprovar em bloco ou item a item | Aprovar como na tabela. K33: excluir, ou reformular no bloco A |
| D7 | 4.1 | Blocos (Seção 9) | (a) sete blocos com subgrupos em B · (b) dividir B | **Decidida em 2026-10-18: (a)**, com três subgrupos em B |
| D10 | 5.3 | Aplicar Q5 aos 39 da T02 | (a) aos 39, começando pelos quatro só "Hosts" (C1, C2, C4, C5) · (b) só aos candidatos novos | **(a)**, conforme a escolha do passo 2.2 |
| D1 | 6.1 | Destino do novo levantamento no paper | A substituir · B validação mínima · C dupla origem declarada (Seção 11) | **Decidida em 2026-10-18: C** |
| D2 | 6.2 | String (T03-F01) | (a) declarar como orientada ao núcleo e registrar a limitação · (b) rodar uma string complementar sem o bloco de nomes de mecanismos · (c) strings dirigidas aos blocos D, F e G | **Decidida em 2026-10-18 (passo 1.3): (a).** Recomendação original: **(a)** se D1 = C. **(b)** se o corpus L tiver de sustentar a tipologia inteira. A busca nova roda pelo fluxo `/literature-review`, num tema de `areas/mestrado/smip-paper/` (regra comum do `CLAUDE.md`) |
| D3 | 6.3 | Triagem (T03-F02) (**decidida em 2026-10-18: conferência já feita**, 11.2) | (a) conferência humana dos 226 + amostra aleatória dos 660 excluídos · (b) só dos 226 · (c) nenhuma | **(a)**. Ver também P1–P3 |
| D11 | 8.1 (a) | Estrutura do Apêndice A (11.1) | aprovar · ajustar | **Decidida em 2026-10-18: aprovada** |
| D12 | 8.1 (c) | Detalhes do processo da primeira lista (A.1) | (a) perguntar aos autores (retomar T01-D2) · (b) rastreabilidade reconstruída (B01) · (a) + (b) | **Decidida em 2026-10-18: (a)**, com resposta dos autores mais tarde; (b) não será feita. Primeira lista montada inicialmente com o Claude (web) |
| D9 | 7.1 | Escopo da T03.7 (conferência nos PDFs) | (a) papers dos 21 itens · (b) só dos 6 novos + evidência contrária · (c) todos os 226 | **(b)** agora, (a) antes da submissão |

## 13. Pendências

| # | Item [a verificar] | Ligado a | O que falta |
|---|---|---|---|
| P1 | Data da busca e campos pesquisados no Lens. Filtros (tipo de documento) e planilha (886, só título e ano) recebidos em 2026-10-18 | T03-F01, F02 | Usuário: **parcialmente resolvida** |
| P2 | Listas de elegíveis e excluídos por lote | T03-F02 | **Resolvida em 2026-10-18**: elegíveis = PDFs das pastas; excluídos reconstruídos em `triagem-reconstruida.csv` (5.4). Os 3 elegíveis declarados sem PDF continuam sem identificação |
| P3 | Modelo/versão e período de uso do Gemini (web), prompt completo da extração e descrição da conferência humana da triagem | T03-F02, F03 | Usuário: **parcialmente resolvida** (ferramenta informada em 2026-10-18) |
| P4 | Divergências de contagem (5.2) | T03-F05 | **Dispensada pelo usuário em 2026-10-18** (passo 1.2). Fica só a escolha da fonte única do número de elegíveis no paper (226 declarados × 223 com PDF), na T03.8 |
| P5 | Atribuições paper → mecanismo (regra 4) | T03-F03, D9 | T03.7 |
| P6 | Definição de SMIP na Seção 2.1 ("sentido amplo") | 6.3 (4), D4 | **Resolvida em 2026-10-18**: lida na cópia de revisão (6.5). SMIP = processos pelos quais design, uso e governança das plataformas "generate, amplify, or host" divisão social |
| P7 | Idiomas dos elegíveis (G7: só en/pt). A planilha do Lens não tem idioma. Caso a conferir: Madariaga et al. 2022 (título do registro em espanhol, 5.4) | regra comum | T03.7 |
| P8 | Política da *Journalism and Media* sobre uso de IA generativa no método | T03-F02, T01-P5 | Usuário ou consulta às instruções do periódico |

## 14. Achados indiretos

- **T03-I01** — **B02 (C8, *reinforcing spiral*)**: o corpus L traz Ohme 2021, *Algorithmic
  social media use and its relationship to attitude reinforcement…* (L1), sobre espirais de
  reforço no uso algorítmico. É insumo para retomar o B02. Não altera o diagnóstico de
  guarda-chuva.
- **T03-I02** — **B04 (E3)**: o corpus L não traz fonte para a produção orientada por métricas.
  Li et al. 2023, *Journalists' networks: Homophily and peering over the shoulder of other…*
  (L4), trata de homofilia entre jornalistas, pelo título. Pode interessar à Seção 10.2
  (implicações para o jornalismo) **[a verificar]**.
- **T03-I03** — **Feedback loop (5.2)**: Nordbrandt 2021 (p. 3392) dá evidência empírica para o
  retorno polarização → uso de mídia social, que o loop já prevê. Candidato a citação na 5.2 ou
  na 9.2.
- **T03-I04** — **Sobreposição V1 ∩ L**: só 4 das 106 referências do paper foram recuperadas
  pela string ([28], [52], [59], [84]), e só [52] e [59] são fontes de algum dos 39 (B4 e B1).
  Isso é coerente com a declaração de *citation chaining* da v1 e mostra que os 39 não saíram
  de uma busca desse tipo. O dado é útil no texto do método (Opção C).
- **T03-I05** — **Seção 9 (limitações) e B2/A1**: Fletcher et al. 2021, Dubois e Blank 2018,
  Geiß et al. 2021 e Liu et al. 2025 sustentam a ressalva de evidência mista que a tabela 6.11 já
  atribui a B2 e A1 ("Mixed"). Hoje essa avaliação não cita nenhuma fonte contrária.

---

## 15. T03.9 — Atores no modelo (2026-10-18)

**Pedido do usuário**: dar mais destaque aos atores. Insumos em `actors/`: a figura nova do
framework (`new_model_famo.jpg`), a tabela de ator primário e secundário para os 41 mecanismos da
v1 (`Tabela SMIP_ Mechanism-Actors (Claude) - Table 4 - Actors.pdf`) e um rascunho em inglês de uma
Seção 5.3, *Actors*, com seis parágrafos e uma síntese (`actors.txt`, gerado com o Claude).

**Os seis tipos** (figura e rascunho): *Ordinary users* · *Social groups* · *Organized (political
or commercial) actors* · *Automated or coordinated agents* · *Algorithm* (ator emergente) ·
*Platform* (ator institucional). Na figura, a caixa *Actors* liga-se a *Mechanisms* ("exploits") e a
*Outcomes* ("shapes"); a caixa *Moderators* (individual, contextual, structural, cultural) liga-se a
*Features* e *Affordances* ("affects").

### 15.1 Achados sobre o material

#### T03-F07 — O rascunho atribui a Rost et al. [73] campanhas organizadas que a obra não descreve · **Importante** · novo
- **Fato**: o parágrafo revisado de *Organized actors* diz que Rost et al. [73] "document
  coordinated harassment campaigns — F2 (Dogpiling) — organized deliberately rather than arising
  from spontaneous individual pile-on". No PDF, as *firestorms* são "crowd-based outrage", com
  críticas e insultos que "may be formed by, and propagated via, thousands or millions of people
  within hours" (Introdução), explicadas como imposição de norma social, e não como efeito do anonimato
  (abstract). A palavra "campaign" não aparece nas 26 páginas; "coordinate" aparece só numa citação
  sobre anonimato e interação de grupo.
- **Julgamento**: o exemplo de comportamento ligado a atores organizados fica sem base. Em F2, o
  ator primário sustentado pela fonte é o usuário comum, agindo como grupo que pune uma transgressão.
  A síntese final do rascunho ("behavioral (organized actors, via F2)") cai junto.
- **Outros problemas do rascunho** (para o passo 9.4): usa os IDs e nomes da v1 (A1 *Engagement-based
  ranking*, A2, M5, M6, E3 *Attention economy*, G2 *Network propaganda*, B4) e fala em "41
  mechanisms"; cita Mason como [63] (na lista é [62]); traz uma referência nova sem dados conferidos
  ("Seaver [NEW]", G1); usa travessões, proibidos pela regra de estilo; e atribui a Munn [70] que as
  arquiteturas são "constitutive business choices", quando o artigo fala de **arquiteturas de
  design** ("Facebook's Feed drives views but also privileges incendiary content", p. 1), sem esse
  enquadramento econômico.

#### T03-F08 — A definição de *Actor* da 2.3 não cobre dois dos seis tipos, e o algoritmo já é exemplo de *feature* · **Importante** · novo
- **Fato**: a 2.3 define *Actor* como "An agent, whether human, institutional, or automated, that
  **deliberately** triggers or exploits a mechanism, such as in coordinated manipulation campaigns".
  O rascunho diz que *Ordinary users* "enact mechanisms **without deliberate exploitation**" e trata o
  algoritmo como agência "not fully reducible to the intentions of whoever built the system". Na
  mesma 2.3, *Feature* é "The concrete, platform-specific technical element, such as a named button,
  **a recommendation algorithm**, or a numerical character limit".
- **Julgamento**: com a definição atual, usuários comuns, grupos e o algoritmo não são atores. E o
  algoritmo passaria a ser, ao mesmo tempo, *feature* e *actor*. A contribuição 1 do paper é
  justamente separar as camadas ("treating feature and affordance as distinct, sequential layers
  that are never merged", 2.3). Um revisor vai notar. Resolve-se com uma definição nova e uma frase
  de fronteira (itens 9.1-a e 9.1-b).

#### T03-F09 — Na figura nova, as setas não seguem as definições de contingência e de ator · **Menor** · novo
- **Fato**: a figura liga *Moderators* a *Features* e *Affordances*. A 2.3 define *Contingency* como
  a condição "that moderates the magnitude of a **mechanism**", e a 5.2 diz que o moderador "alters
  the strength with which a mechanism operates". A seta *Actors* → *Mechanisms* diz "exploits", verbo
  que não cabe a usuários comuns nem ao algoritmo. A seta *Actors* → *Outcomes* ("shapes") sugere que
  os atores produzem outcomes sem passar pelos mecanismos, enquanto o rascunho descreve outcomes
  moldados **por meio** de um mecanismo.
- **Julgamento**: três ajustes simples na figura (item 9.3). A separação entre *Moderators* e
  *Actors* resolve uma divergência antiga do `context.md` (a Figura 2 antiga rotulava a camada como
  "context, actors").

### 15.2 Passo 9.1 — Conceito: itens para aprovação

| Item | Proposta | Recomendação |
|---|---|---|
| **9.1-a** (D13) Definição de *Actor* | Nova definição na 2.3, em substância: o agente (individual, coletivo, institucional ou automatizado) cujo comportamento **realiza, dispara ou explora** um mecanismo. Alguns o fazem deliberadamente (atores organizados, agentes coordenados); outros, sem intenção estratégica (usuários comuns, grupos sociais, o algoritmo). O texto em inglês sai na T03.8 | Aprovar. Sem isso, a seção nova contradiz a 2.3 |
| **9.1-b** (D14) O algoritmo como ator | (a) **Manter**, com o nome *Algorithmic system* e uma frase de fronteira na 2.3: como *feature*, o algoritmo é o elemento técnico especificado; como ator, é o sistema em operação, cujo comportamento agregado (o que ele aprende a priorizar) ninguém decide diretamente. Restrito ao bloco A como primário. A fonte nova (Seaver 2019, ou outra sobre comportamento de máquinas) **[conhecimento do agente; conferir dados bibliográficos]** entra pelo G1. (b) **Retirar** o algoritmo dos atores e tratar a agência algorítmica pela *Platform* (que define o objetivo) e por AF1 | **(a)**, que preserva o modelo do usuário, desde que a frase de fronteira entre na 2.3. (b) é a opção mais segura para a contribuição 1 |
| **9.1-c** (D15) *Platform* × AF10 | Frase de fronteira: AF10 (*platform governance*) é a affordance, isto é, o que as regras da plataforma tornam possível para os usuários. *Platform* como ator é a organização que define essas regras e o objetivo que o algoritmo otimiza | Aprovar |
| **9.1-d** (D16) Fonte do exemplo de cada ator | Cada exemplo da 5.3 usa uma fonte já conferida e a ficha atual do mecanismo. Saem os exemplos sem base (F2 com atores organizados, T03-F07). A síntese "the six actor types span all five outcome types" é refeita com o mapeamento novo (15.3) | Aprovar |

### 15.3 Passo 9.2 — Mapeamento dos 43 mecanismos × atores (D17)

**Método**: parte da tabela da v1 (41 mecanismos). Cada linha foi levada ao mecanismo atual pela
correspondência da T02 (14.6) e da T03 (9.1). Mantém-se o mapeamento da v1 quando o mecanismo não
mudou de conteúdo. Muda quando a T02 ou a T03 mudaram o que o mecanismo é. Os quatro novos recebem
ator a partir das fontes aprovadas. IDs **novos** (9.1), com o atual entre parênteses quando muda.

Abreviações: **OU** *Ordinary users* · **SG** *Social groups* · **OA** *Organized actors* · **AC**
*Automated or coordinated agents* · **AL** *Algorithm* · **PL** *Platform*.

| ID novo (atual) | Mecanismo | Na v1 | Primário | Secundário | Mudança e motivo |
|---|---|---|---|---|---|
| A1 | Filter bubble | M1 (parte): OU, — | **AL** | OU | A1 é a via algorítmica de M1 (D27). A escolha do usuário (Bakshy [45]) fica como secundária |
| A2 | Algorithmic amplification | A1: AL, PL | AL | PL | = v1. PL também pela política de contas priorizadas (fusão de K33) |
| A3 | Algorithmic radicalization | A2: AL, OU | AL | OU | = v1 |
| A4 | Algorithmic agenda-setting | A5: OU, — | **AL** | **AC** | Os *trending topics* são agregação algorítmica (bloco A). Elmas [54] mostra a manipulação por contas coordenadas |
| B1 | Homophily | B1: OU, —; A3: OU, — | OU | **AL** | Absorveu A3 (recomendação de conexões, D21): Santos [59] |
| B2 (novo) | Unfriending | — | OU | — | Corte de laços por usuários (Martel et al. 2024; Kaiser et al. 2022) |
| B3 (B6) | Partisan sorting | B4: SG, OU | SG | OU | = v1 |
| B4 (B7) | Interpersonal political tension | B5: OU, — | OU | — | = v1 |
| B5 (B2) | Echo chamber | M1 (parte): OU, — | OU | **SG** | Reforço entre pares de um mesmo grupo (Cinelli [46]) |
| B6 (B3) | Group polarization | B2: OU, SG | OU | SG | = v1 |
| B7 (novo) | Negative social influence | — | OU | SG | O afastamento depende do grupo da fonte (8.6) |
| B8 (B5) | Moral contagion | C5: OU, — | OU | **OA** | Rathje [38]: o efeito mais forte está nos posts de veículos e congressistas |
| B9 (B4) | Information cascades | B3: OU, AC; M4: OU, AC | OU | AC | = v1 |
| B10 (B8) | Online community radicalization | G3: SG, OA | SG | OA | = v1 |
| C1 | Motivated reasoning | C1: OU, — | OU | — | = v1 |
| C2 | Confirmation bias | M2: OU, — | OU | — | = v1 |
| C3 | Selective avoidance | H2: OU, — | OU | — | = v1 |
| C4 | Biased assimilation | C2: OU, — | OU | — | = v1 |
| C5 (novo) | Backfire effect | — | OU | PL | Correções e etiquetas da plataforma mudam o efeito (Kim et al. 2025) |
| C6 (C5) | Hostile media effect | C3: OU, — | OU | — | = v1 |
| C7 (C6) | Illusory truth effect | C4: OU, — | OU | — | = v1 |
| C8 (C7) | News avoidance | H1: OU, — | OU | — | = v1 |
| C9 (C8) | Reinforcing spiral | M6: AL, OU | **OU** | **AL** | Inversão: na T02, o mecanismo foi para o bloco C como espiral individual identidade ↔ consumo de mídia (Slater [55]). Fica sujeito ao B02 |
| D1 | Vocal minority | D1: OU, — | OU | — | = v1 |
| D2 | Social proof | D4: OU, AC | OU | AC | = v1 |
| D3 | False consensus | D3 (parte): OU, — | OU | — | = v1 |
| D4 | Pluralistic ignorance | D3 (parte): OU, — | OU | **SG** | Norma percebida do próprio grupo (You e Lee 2024, aprovado em 10.1) |
| D5 | Spiral of silence | M7: OU, — | OU | — | = v1 |
| D6 | Exaggerated meta-perceptions | D2: OU, — | OU | — | = v1 |
| E1 | Social learning of outrage | E1: OU, —; E4: OU, PL | OU | **PL** | Herda o secundário de E4, fundido em E1 (D23): a plataforma desenha os contadores de recompensa |
| E2 | Identity signaling | E2: OU, — | OU | **SG** | A sinalização é dirigida ao próprio grupo (Van Bavel e Pereira [69]) |
| E3 | Metric-driven content production | E3: PL, OA | **OA** | **PL** | Inversão: E3 foi redefinido (D18) como ajuste de veículos, jornalistas e criadores às métricas. Quem age são os produtores; a plataforma define as métricas |
| F1 | Online disinhibition effect | F1: OU, — | OU | — | = v1 |
| F2 | Dogpiling | F2: OU, OA | OU | **— (ou OA como justificativa teórica)** | Rost [73] não sustenta a ação organizada (T03-F07) |
| F3 | Message brevity | F3: OU, — | OU | — | = v1 |
| F4 | Incivility contagion | F4: OU, — | OU | — | = v1 |
| F5 | Incivility exposure effect | M3: OU, — | OU | — | = v1 (M3 reformulado como F5) |
| G1 | Gatekeeping decline | G1: OU, PL | **PL** | **OA** | O processo é a substituição do filtro editorial pela distribuição da plataforma; quem passa pelo portão são veículos partidários e atores políticos (Bennett e Livingston [74]) |
| G2 | Propaganda feedback loop | G2: OA, OU | OA | OU | = v1 |
| G3 | Manufactured consensus | M5: AC, OA | AC | OA | = v1 |
| G4 | Platform migration | G4: PL, SG | PL | SG | = v1 |
| G5 | Perceived censorship | G5: OU, OA | OU | OA | = v1. Myers West [78]: usuários atribuem remoções a "coordinated reporting by their opponents" |
| G6 (novo) | Partisan flagging | — | OU | OA | Usuários denunciam (Westermann e Coscia 2022); a denúncia coordinada é a forma organizada (percepção registrada por Myers West [78]) |

**Itens da v1 que deixam de existir**: A4 *Context collapse* (excluído na T02, D22), M4 (→ B9), M3 (→
F5), A3 (→ B1), E4 (→ E1).

**Distribuição dos primários (43)**: OU 32 · AL 4 (A1–A4) · SG 2 (B3, B10) · OA 2 (E3, G2) · PL 2
(G1, G4) · AC 1 (G3).

**Outcomes alcançados por cada tipo de ator, como primário** (outcomes da tabela 6.11 e das fichas
aprovadas):

| Ator (primário) | Outcomes | Exemplo |
|---|---|---|
| OU | Structural, Ideological, Affective, Perceived, **Behavioral** | B1 (structural); D5 e F2 (behavioral) |
| SG | Affective, Ideological | B3 (affective) |
| OA | Affective, Ideological, Perceived | G2 (ideological, perceived) |
| AC | Perceived, Affective | G3 |
| AL | Ideological, Affective, Perceived | A3 (ideological); A4 (perceived) |
| PL | Ideological, Perceived, Structural, Affective | G4 (structural, affective) |

**Leitura**: a síntese do rascunho ("no outcome type is reachable by only one actor") **não se
sustenta** com o mapeamento: como ator primário, só o usuário comum alcança o outcome
**behavioral**. É um resultado em si: a polarização comportamental (autocensura, sanção coletiva,
denúncia) aparece como efeito agregado de ações individuais, e não como estratégia de atores
organizados, ao menos no que as fontes do paper sustentam.

**Itens para aprovação**:

| Item | Proposta | Recomendação |
|---|---|---|
| **9.2-a** | Aprovar o mapeamento das linhas "= v1" (sem mudança) | Aprovar |
| **9.2-b** | Aprovar as mudanças: A1 e A4 (AL primário), B1, B5, B8, D4, E1 e E2 (novos secundários), C9 (OU primário), E3 (OA primário), G1 (PL primário) | Aprovar. Destaques: E3 e G1, que mudam o primário |
| **9.2-c** | F2: secundário **—** (sem fonte) ou **OA** como justificativa teórica | **—**, coerente com T03-F07 |
| **9.2-d** | Atores dos quatro novos (B2, B7, C5, G6) | Aprovar |
| **9.2-e** | Refazer a síntese do rascunho: em vez de "no outcome reachable by only one actor", dizer que o outcome behavioral só aparece com usuários comuns como primário | Aprovar |

**Decisões do usuário — passos 9.1 e 9.2 (2026-10-18)**: **9.1-a, c e d aprovados**; **9.1-b = (a)**:
o algoritmo continua ator, com o nome *Algorithmic system* e a frase de fronteira na 2.3. **9.2-a a e
aprovados**: mapeamento dos 43 como na tabela, F2 sem secundário e síntese refeita. **D13–D17
decididas.**

### 15.4 Passo 9.3 — Figura 2 nova: correções propostas (2026-10-18)

Esboço em Mermaid para o redesenho: `actors/new_model_famo_proposta.mmd` (não substitui o JPG).

| Item | Na figura atual | Proposta | Por quê |
|---|---|---|---|
| **9.3-a** | *Moderators* → *Features* e → *Affordances* ("affects") | Uma seta *Moderators* → *Mechanisms*, com o rótulo **"moderate"** | A 2.3 define a contingência como a condição que "moderates the magnitude of a mechanism", e a 5.2 diz que o moderador "alters the strength with which a mechanism operates" (T03-F09) |
| **9.3-b** | *Actors* → *Mechanisms* ("exploits") | Rótulo **"enact or exploit"** | A definição aprovada (9.1-a) inclui atores que agem sem intenção estratégica |
| **9.3-c** | *Actors* → *Outcomes* ("shapes") | **Retirar** a seta direta | Os atores moldam os outcomes por meio dos mecanismos, como o próprio rascunho descreve. A seta direta sugere uma via sem mecanismo |
| **9.3-d** | *Algorithm* | ***Algorithmic system*** | Decisão 9.1-b |
| **9.3-e** (opcional) | — | Seta tracejada *Platform* → *Features* ("designs") | Torna visível o papel institucional da plataforma (9.1-c): ela define as *features* e o objetivo que o algoritmo otimiza |
| **9.3-f** (opcional) | — | Seta tracejada *Outcomes* → *Actors* ("changes use") | Mostra o fechamento do loop pelo **uso**, aprovado no item 2.3-f (Nordbrandt 2021: a polarização muda o uso de mídia social). Complementa a seta que já fecha em *Features* |

**Item para aprovação**: 9.3-a a d (correções) e a decisão sobre os opcionais 9.3-e e 9.3-f.

**Decisões do usuário — passo 9.3 (2026-10-18)**: **9.3-a a d aprovados**; **9.3-e e 9.3-f
recusados**. PNG gerado: `actors/new_model_famo_v2.png` (fonte: `actors/new_model_famo_v2_fonte.py`;
esboço: `actors/new_model_famo_proposta.mmd`). Substitui a Figura 2 do paper no passo 8.3.

### 15.5 Passo 9.4 — Texto da Seção 5.3, *Actors* (2026-10-18)

**Base**: o rascunho de `actors/actors.txt`, refeito com as decisões 9.1 e 9.2. IDs na **numeração
nova** (9.1), que entra no paper no passo 8.6. Cada afirmação sobre uma obra vem da ficha atual do
mecanismo, já conferida no PDF na T02 ou na T03, ou da primeira página do PDF (Munn [70]). Benkler
[75] e Woolley e Howard [53] são livros sem PDF (D-sem-PDF da T02), usados como já estão nas fichas.

**O que mudou em relação ao rascunho**: IDs e nomes atuais (saem A1 *Engagement-based ranking*, M5,
M6, E3 *Attention economy*, G2 *Network propaganda*); 43 mecanismos, e não 41; Mason [62], e não
[63]; sai a citação nova sem dados conferidos (Seaver); sai o dogpiling organizado atribuído a Rost
[73] (T03-F07); sai "constitutive business choices" (Munn [70] fala de arquiteturas de design);
exemplos novos para o algoritmo (A2, Milli [14]) e para a plataforma (G4, Horta Ribeiro [77]); um
parágrafo sobre o jornalismo como ator (E3, Petre [102]); a síntese é refeita (9.2-e); sem
travessões, sem ponto e vírgula, sem aspas em termos em inglês.

**Texto proposto** (inserir como Seção 5.3, depois da 5.2):

> **5.3. Actors**
>
> Actors are the agents whose behavior enacts, triggers, or exploits the mechanisms catalogued in
> Section 6 (Section 2.3). Some act with strategic intent and others without it. Figure 2
> distinguishes six types, and Table [N] assigns a primary and, where relevant, a secondary actor to
> each of the 43 mechanisms. Each type is illustrated below through one mechanism and the outcome it
> most directly shapes.
>
> Ordinary users enact most mechanisms without any intention to polarize, and they are the primary
> actor for 32 of the 43 mechanisms. Homophily (B1) is the clearest case. Similar people form ties at
> a higher rate than dissimilar people [37], and on social media the sum of these individually
> unremarkable choices sorts users into homogeneous clusters, which is structural polarization.
> Ordinary users are also the only primary actor of the mechanisms with behavioral outcomes. In
> online firestorms (F2), large numbers of users sanction a perceived transgression as a form of
> social norm enforcement, and in the data analyzed by Rost et al. [73], non-anonymous users were more
> aggressive than anonymous ones. In the spiral of silence (D5), people who perceive their opinion as
> losing ground become less willing to express it [24].
>
> Social groups act as collective units. In the mechanisms they drive, a shared identity matters more
> than the choice of any member or leader. Partisan sorting (B3) shows this. When partisan and
> ideological identities align, each party becomes a more homogeneous social group, and partisan
> bias, activism, and anger increase even when issue positions do not polarize to the same degree
> [62]. The outcome is mainly affective.
>
> Organized political or commercial actors exploit mechanisms toward a strategic goal. In the
> propaganda feedback loop (G2), partisan media outlets, political figures, and audiences reward
> stories that confirm the group's identity and penalize outlets and journalists that check them, so
> that the media ecosystem becomes insular and resistant to correction [75]. The outcome is
> ideological and perceived polarization. News organizations belong to this type as well when they
> adjust what they publish to engagement metrics (E3) [102]. Journalism therefore appears in the
> framework as an actor, in addition to being one of the fields affected by polarization.
>
> Automated or coordinated agents depend on cheap and scalable activity rather than on individual
> conviction. In manufactured consensus (G3), coordinated accounts, often automated, fabricate
> signals of popularity [53]. Elmas et al. [54] detected over 19,000 fake trends on Twitter promoted
> by over 108,000 accounts, and these attacks accounted for at least 20% of the top ten global
> trends. The outcome is mainly perceived polarization, since observers misjudge how widely a
> position is held.
>
> The algorithmic system is treated as an actor in a restricted sense. As a feature, a recommendation
> algorithm is a technical element specified by the platform (Section 2.3). As an actor, it is the
> system in operation, whose aggregate behavior, such as the kind of content it learns to
> prioritize, is not decided directly by anyone. It is the primary actor of the four mechanisms in
> Block A. In algorithmic amplification (A2), Milli et al. [14] found that the engagement-based
> ranking of Twitter amplified emotionally charged and out-group hostile content that users said made
> them feel worse about their political out-group, and that users did not prefer the political posts
> it selected. The outcome is mainly affective.
>
> The platform acts as an institution. It sets the rules of governance (AF10), the design of
> features, and the objective that its ranking systems optimize. Munn [70] argues that design
> architectures such as the Facebook Feed privilege incendiary content and set up a stimulus-response
> loop that promotes outrage expression. Platform migration (G4) shows the platform as primary actor.
> After Reddit banned two communities, both moved to standalone websites, where posting activity
> fell but users of one of them showed more signals of toxicity and radicalization [77]. The outcome
> is structural, through the separation of communities across platforms, and affective.
>
> Two patterns emerge from Table [N]. Organized and automated actors appear as primary actors only in
> Block G and in metric-driven content production (E3), while ordinary users are the primary actor in
> every block except Block A. Behavioral polarization appears only with ordinary users as the primary
> actor, which suggests that self-censorship and collective sanctioning arise from aggregated
> individual action rather than from strategy, at least in the evidence reviewed here. As with the
> links between affordances and mechanisms (Section 5.1), the mapping indicates which actors can
> enact or exploit a mechanism. It does not predict the outcome of a specific case.

**Conferência das regras de estilo** (`manuscripts/CLAUDE.md`): sem travessão; sem ponto e vírgula;
sem aspas em termos em inglês; sem vocabulário inflado nem fórmulas de contraste. As listas de três
itens que restam são listas reais (governança, *features* e objetivo; viés, ativismo e raiva, que é a
formulação de Mason na ficha de B3).

**Pontos que dependem de outros passos**:
- **Table [N]**: número e forma da tabela de atores (passo 9.5).
- **Munn [70]**: está na lista de referências, mas não é citado no texto atual. Volta a ser citado
  aqui.
- **Petre [102]**: base indireta de E3 (resenhas, D18 da T02; B04 aberto). A frase sobre jornalismo
  se apoia na definição de E3, e não em evidência sobre polarização.

**Itens para aprovação**:

| Item | Proposta | Recomendação |
|---|---|---|
| **9.4-a** | O texto acima como Seção 5.3 | Aprovar ou indicar mudanças por parágrafo |
| **9.4-b** | Posição: nova Seção 5.3, depois da 5.2 (*Moderators and the Feedback Loop*) | Aprovar. Segue o pedido original do rascunho e a ordem da figura (moderadores, depois atores) |

**Decisões do usuário — passo 9.4 (2026-10-18)**: **9.4-a e 9.4-b aprovados**. O texto entra como
Seção 5.3 no passo 8.x, com "Table [N]" resolvido no passo 9.5.

### 15.6 Passo 9.5 — Forma da tabela de atores no paper (2026-10-18)

**Opções**:
- **(a) Tabela compacta na 5.3**, com uma linha por tipo de ator (6 linhas). Mostra o padrão sem
  repetir os 43 mecanismos.
- **(b) Duas colunas novas na tabela consolidada** (6.11). Ela já tem sete colunas (ID, Mechanism,
  Outcome, Platform role, Direction, Evidence strength, Ref) e passaria a nove, largo demais para o
  template MDPI.
- **(c) Mapeamento completo na Table A1** do Apêndice A, que já vai ter, para cada mecanismo, a
  origem e o suporte no segundo levantamento (5.2-b). Entram duas colunas: *Primary actor* e
  *Secondary actor*.

**Recomendação: (a) + (c).** A 5.3 traz a tabela compacta, e a Table A1 traz o mapeamento linha a
linha. A tabela consolidada não muda.

**Tabela compacta proposta** (em inglês; IDs na numeração nova):

| Actor type | Mode of action | Primary actor of | Secondary actor of | Outcomes reached as primary actor |
|---|---|---|---|---|
| Ordinary users | Enact mechanisms without strategic intent | 32 mechanisms: B1, B2, B4–B9, C1–C9, D1–D6, E1, E2, F1–F5, G5, G6 | A1, A3, B3, G2 | Structural, ideological, affective, perceived, behavioral |
| Social groups | Shared identity drives the mechanism | B3, B10 | B5, B6, B7, D4, E2, G4 | Affective, ideological |
| Organized actors | Exploit mechanisms strategically | E3, G2 | B8, B10, G1, G3, G5, G6 | Affective, ideological, perceived |
| Automated or coordinated agents | Exploit mechanisms strategically, at scale | G3 | A4, B9, D2 | Perceived, affective |
| Algorithmic system | Emergent behavior of a system in operation | A1–A4 | B1, C9 | Ideological, affective, perceived |
| Platform | Institutional choices of rules, design, and objectives | G1, G4 | A2, C5, E1, E3 | Ideological, perceived, structural, affective |

**Numeração**: a tabela nova entra na 5.3, depois da Tabela 4 (moderadores, 5.2). Vira a **Tabela 5**,
e as atuais 5 (mecanismos, 6.11) e 6 (affordances × mecanismos × intervenções) passam a **6 e 7**.
A renumeração entra no passo 8.6, junto com a dos IDs.

**Itens para aprovação**:

| Item | Proposta | Recomendação |
|---|---|---|
| **9.5-a** | Tabela compacta na 5.3, como acima | Aprovar |
| **9.5-b** | Colunas *Primary actor* e *Secondary actor* na Table A1 | Aprovar |
| **9.5-c** | Renumerar as tabelas 5 e 6 para 6 e 7 no passo 8.6 | Aprovar |

**Decisões do usuário — passo 9.5 (2026-10-18)**: **9.5-a = (a) e (b)**: a tabela compacta entra na
5.3 **e** a tabela consolidada ganha as colunas *Primary actor* e *Secondary actor* (nove colunas no
total). **9.5-b aprovado** (colunas também na Table A1). **9.5-c aprovado** (tabela nova = Tabela 5;
as atuais 5 e 6 passam a 6 e 7, no passo 8.6). Para caber no template, a proposta de formato está em
15.7 (9.6-f).

### 15.7 Passo 9.6 — Propagação: textos para aprovação (2026-10-18)

**Base**: texto atual da cópia de revisão (leitura de 2026-10-18). Os trechos "atual" são citados
como estão; os "novos" seguem as regras de estilo e foram conferidos (sem travessão, sem ponto e
vírgula, sem aspas em termos em inglês). Tabelas na numeração nova (9.5-c).

| Item | Onde | Texto atual | Texto novo |
|---|---|---|---|
| **9.6-a** | 2.3, definição de *Actor* | "Actor: An agent, whether human, institutional, or automated, that deliberately triggers or exploits a mechanism, such as in coordinated manipulation campaigns." | Actor: An agent, whether individual, collective, institutional, or automated, whose behavior enacts, triggers, or exploits a mechanism. Some actors do so deliberately, as in coordinated manipulation campaigns. Others do so without strategic intent, as ordinary users and the algorithmic systems of platforms do (Section 5.3). |
| **9.6-b** | 2.3, parágrafo novo logo depois da lista das cinco categorias | — | Two elements of social media can appear under more than one of these categories, and the framework keeps their roles apart. A recommendation algorithm can appear in two roles. As a feature, it is the technical element that the platform specifies. As an actor, it is the system in operation, whose aggregate behavior, such as the content it learns to prioritize, no one decides directly. The platform also appears in two roles. As an actor, it is the organization that sets the rules, the design of features, and the objective that its ranking systems optimize. Platform governance (AF10) is the affordance, that is, what those rules make possible for users. |
| **9.6-c** | 5.1, legenda da Figura 2 | "A four-layer framework: features, affordances, mechanisms, and outcomes." | The framework: four layers (features, affordances, mechanisms, and outcomes), with moderators and actors acting on the mechanisms layer and a feedback loop from outcomes to features. |
| **9.6-d** | 5.1, frase nova no fim do primeiro parágrafo depois da figura (o que termina em "represented in Figure 2.") | — | Two further elements act on the mechanisms layer without forming part of the chain: moderators, which change the strength with which a mechanism operates (Section 5.2), and actors, which enact or exploit mechanisms (Section 5.3). |
| **9.6-e** | 5.2, primeira frase | "A moderators layer, represented on the left side of Figure 2, cuts across the four layers without forming part of the main causal chain." | A moderators layer, represented on the left side of Figure 2, acts on the mechanisms layer without forming part of the main causal chain. |
| **9.6-f** | Tabela consolidada (nova Tabela 6), formato das colunas de ator | — | Nas colunas *Primary actor* e *Secondary actor*, usar abreviações com legenda na nota da tabela: OU (ordinary users), SG (social groups), OA (organized actors), CA (automated or coordinated agents), AS (algorithmic system), PL (platform). Nas colunas *Platform role* e *Direction*, valores curtos (Creates, Amplifies, Hosts; Reinf., Mixed). Se ainda faltar espaço, a tabela vai em página paisagem, que o template MDPI admite **[conferir no template]** |
| **9.6-g** | G3, última frase da ficha | "It is the clearest case of the actors defined in Section 2.3, who deliberately trigger or exploit mechanisms." | Its primary actors are automated or coordinated agents, the clearest case of actors who exploit mechanisms deliberately (Section 5.3). |
| **9.6-h** | 9.1, parágrafo novo depois do parágrafo sobre *perceived polarization* | — | The actor mapping (Section 5.3, Table 5) adds a further finding. Behavioral polarization appears only with ordinary users as the primary actor, and organized and automated actors are primary actors only in Block G and in metric-driven content production (E3). Strategic exploitation is therefore concentrated in the supply of information, while the mechanisms that change behavior depend on the aggregated action of ordinary users. |
| **9.6-i** | 10.2, primeiro item, depois da frase que termina em "a testable hypothesis." | — | In the actor typology of Section 5.3, news organizations that adapt their output to engagement metrics are organized actors and the primary actor of E3. |

**Fora da tabela** (para localizar no passo 8.x): a Introdução descreve o framework e as contribuições
sem mencionar os atores. Uma oração ("with moderators and actors acting on the mechanisms layer")
basta, se você quiser que eles apareçam já na Introdução.

**Efeito colateral resolvido**: a divergência registrada no `context.md` ("a Figura 2 rotula a camada
como 'context, actors'; a Tabela 3 só traz contingências") deixa de existir com a figura nova.

**Item para aprovação**: **9.6-a a i**, um por um ou em bloco, e a decisão sobre a Introdução.

**Decisões do usuário — passo 9.6 (2026-10-18)**: **9.6-a a i aprovados**. **Introdução: acrescentar
a observação sobre os atores.** Texto (a inserir no parágrafo que começa com "This article proposes a
four-layer framework", logo depois da primeira frase):

> Around these layers, the framework places moderators, which change how strongly a mechanism
> operates, and six types of actors, which enact or exploit mechanisms (Section 5).

O mesmo parágrafo diz "forty-one distinct mechanisms", que passa a "forty-three" no passo 8.6.
**T03.9 concluída.**

---

## 16. T03.7 — Conferência nos PDFs (2026-10-18)

### 16.1 Passo 7.1 — Escopo (D9)

**Proposta e execução**: conferir **todos os papers do segundo levantamento que vão ser citados no
paper**, e não os 144 incluídos na síntese. A Table A1 lista só os papers citados, e o número de
incluídos aparece no fluxo do Apêndice A. Profundidade: abstract e primeira página, e o trecho que
sustenta a afirmação da ficha quando o abstract não basta.

**Situação**:
- **27 já conferidos** nas etapas anteriores (T03-F03, 3.3, 10.1): Martel et al. 2024; Kaiser et al.
  2022; Sasahara et al. 2020; Törnberg 2026; Karlsen et al. 2017; Kim et al. 2025; Zarouali et al.
  2020; Nordbrandt 2022; Axelrod et al. 2021; Krueger et al. 2017; Thurner et al. 2025; Nettasinghe et
  al. 2025; Carpentras et al. 2022; Westermann e Coscia 2022; Liu et al. 2025; Arruda et al. 2024;
  Tonin et al. 2025; Fletcher et al. 2021; Dubois e Blank 2018; Geiß et al. 2021; Törnberg 2018;
  Mølmen e Ravndal 2021; Masip et al. 2020; Brown et al. 2022; You e Lee 2024; Kobellarz et al. 2024;
  Nordbrandt 2021.
- **17 conferidos agora**, que eram citados nas fichas dos 39 (passos 3.2 e 5.3) sem leitura:

| Paper | Ficha | O que o PDF diz | Resultado |
|---|---|---|---|
| Cho et al. 2020 | A1 | Experimento de laboratório com o recomendador real do YouTube, manipulando o histórico: "political self-reinforcement […] and affective polarization are heightened by political videos – selected by the YouTube recommender algorithm" (abstract) | **Confirma**, com direção de reforço. A1 = Mixed (Cho × Liu) |
| Metzler e García 2023 | A2, E1 | Revisão: "Existing evidence suggests that algorithms mostly reinforce existing social drivers" (abstract) | **Confirma**; também sustenta o valor *Amplifies* |
| Ognibene et al. 2023 | A2 | Artigo de "Hypothesis and Theory": propõe um sistema de recomendação orientado ao bem-estar coletivo e um assistente educacional | **Não sustenta A2.** O Gemini o descreveu como simulação da recomendação por engajamento. **Sai da ficha de A2.** Pode servir como intervenção para AF1 na Tabela 7 (opcional) |
| Gu et al. 2025 | B1 | Em redes de discurso de conflito, o modelo "learns to overwhelmingly prioritize affective homophily" (*emotional fortresses*) (abstract) | **Confirma** |
| Sobeh et al. 2025 | B6 (*group polarization*) | 188 participantes em grupos de quatro, com fNIRS: grupos homogêneos levaram a visões mais extremas, e a sincronia entre cérebros no DLPFC "diminishes this effect" (abstract) | **Confirma** o fenômeno, em laboratório (não conta como evidência de plataforma, regra 5.3-a) |
| Simchon et al. 2022 | B8 (*moral contagion*) | Trolls russos usam mais linguagem polarizada que usuários comuns, e a linguagem polarizada se associa a mais engajamento entre usuários politicamente engajados (abstract) | **Confirma**. Serve também para G3 e para a seção de atores (agentes coordenados) |
| Hasell e Weeks 2016 | B8 | Painel de 2012: o uso de notícias partidárias online "is associated with increased anger […] directed at the opposing party's presidential candidate", e a raiva facilitou o compartilhamento em mídia social (abstract) | **Confirma**; exemplo de via fora da plataforma (2.3-b) |
| Törnberg 2022 | B3 (*partisan sorting*) | Modelo: "it is not isolation from opposing views that drives polarization but precisely the fact that digital media bring us to interact outside our local bubble", o que produz *sorting* (abstract) | **Confirma**; também é evidência contrária à hipótese da câmara de eco |
| Sobkowicz 2018 | C1 | Modelo baseado em agentes que compara "confirmation bias and politically motivated reasoning" (abstract) | **Confirma** (simulação) |
| Sultan et al. 2024 | C1 | Meta-análise de 31 experimentos (11.561 participantes): "ideological congruency […] [and] motivated reflection […] are associated with a true-news bias" (abstract) | **Confirma** |
| Sikder et al. 2020 | C4 | Modelo em que uma minoria rejeita informação incongruente; o mecanismo "generates permanent opinion polarization and cascade dynamics", com teste em dados de condados dos EUA (abstract) | **Confirma** |
| Secară e Opre 2026 | C7 (*illusory truth*) | Experimento pré-registrado: duas semanas de artigos completos sobre suplementos, com valência positiva, negativa ou mista (abstract) | **Confirma** o fenômeno, fora de plataforma, coerente com *Plausible* (5.3) |
| Ohme 2021 | C9 (*reinforcing spiral*) | Painel com 847 dinamarqueses: "frequent social media usage reinforces existing attitudes and mobilizes political participation" (abstract) | **Confirma**; alimenta o B02 |
| Banisch et al. 2022 | D5 | Modelo teórico: "Even strong majorities can be forced into silence if a minority acts as a cohesive whole", mas a organização em torno de opiniões que as plataformas permitem também favorece regimes em que vozes opostas se expressam (abstract) | **Confirma** a direção *Mixed* (simulação) |
| Cheong et al. 2022 | D5 | "The aim of this **conceptual study**" é propor como os princípios da espiral do silêncio operam com conteúdo sugerido por algoritmos (abstract) | **Corrige a descrição** de 10.3, que o chamava de survey. Não é evidência empírica. A base de *Moderate* em D5 passa a ser Geiß et al. 2021: com diários móveis, "SM reliance does not generally stimulate opinion expression" (abstract) |
| Konovalova et al. 2023 | E1 | Simulações de um modelo de aprendizagem, análises de dados do Twitter e "several online experiments": opiniões expressas mais extremas quando não há contagem de reações negativas (abstract) | **Confirma**; sustenta *Strong* em E1, com Brady [13] |
| Garz et al. 2019 | E2 | Posts de 84 veículos alemães no Facebook (2012–2017): "users engaged with congenial posts more than with uncongenial ones, especially in terms of likes" (abstract) | **Confirma**; sustenta *Moderate* em E2. É *working paper* (CESifo): conferir se há versão publicada no passo 7.5 |

**Resultado**: **42 papers do segundo levantamento confirmados** para citação (27 + 15). **Dois saem
como evidência**: Ognibene et al. 2023 (A2) e Cheong et al. 2022 (D5). Nenhum valor da tabela de
10.3 muda: em D5, o *Moderate* se apoia em Geiß et al. 2021.

**Itens para aprovação**:

| Item | Proposta | Recomendação |
|---|---|---|
| **7.1-a** (D9) | Escopo: todos os papers citados (42), e não os 144 | Aprovar (já executado) |
| **7.1-b** | Retirar Ognibene et al. 2023 da ficha de A2 e Cheong et al. 2022 da base empírica de D5 | Aprovar |
| **7.1-c** | Ognibene et al. 2023 como intervenção de AF1 na Tabela 7 | Opcional. Recomendo não incluir: é proposta sem teste |
| **7.5** | Próximo passo: BibTeX dos 42 via Crossref (G1), por DOI ou título, num arquivo novo `manuscripts/smip-famo-framework/references-T03-novas.bib`, com a versão publicada de Garz et al. 2019, se existir. Só metadados: nenhum trecho do paper é enviado | Aprovar |

**Efeito na lista de referências**: de 106 para cerca de **148** obras. Nenhuma das 42 está hoje na
lista. Bail [84] e Santos [59], que também estão no corpus, já estão nela.

**Decisões do usuário — passo 7.1 (2026-10-18)**: **7.1-a aprovado** (escopo: os 42 citados);
**7.1-b aprovado** (Ognibene et al. 2023 e Cheong et al. 2022 saem como evidência); **7.1-c: não
incluir** Ognibene et al. 2023 na Tabela 7. **D9 decidida.**

### 16.2 Passo 7.5 — BibTeX via Crossref (2026-10-18)

- **Arquivo**: `manuscripts/smip-famo-framework/references-T03-novas.bib`, com **42 entradas**, todas
  obtidas do Crossref pelo DOI (G1): 31 pelo DOI impresso no próprio PDF, com o título conferido no
  Crossref, e 11 por busca de título, com similaridade de título acima de 0,75. Conferência linha a
  linha em `revisao_mecanismos/references-T03-novas-conferencia.csv`.
- **Garz et al.**: o PDF do corpus é o *working paper* (CESifo/SSRN, 2019). A versão publicada é
  *Journal of Economic Behavior & Organization* 177 (2020), DOI 10.1016/j.jebo.2020.06.016, que
  substitui a do SSRN no .bib. O conteúdo citado foi conferido no *working paper* (16.1).
- **Ohme**: o Crossref registra 2020 (publicação online), e o arquivo do corpus diz 2021 (volume).
  Usar o ano do registro na lista do paper.
- **Chaves de citação** únicas; 5 entidade(s) HTML "&amp;" convertida(s) em "\&" (ajuste de
  formato, sem mudança de conteúdo).
- **Na lista do paper**: as 42 obras entram no estilo MDPI, numeradas no passo 8.6, junto com a
  renumeração das citações.

**T03.7 concluída (2026-10-18)**: os passos 7.2 (candidatos, 8.4–8.9), 7.3 (evidência contrária,
T03-F03 e 10.1) e 7.4 (unidades existentes, 16.1) foram cumpridos dentro do escopo da D9.

