# T02 — Revisão e validação dos 41 mecanismos: nomes, estrutura, definições e processo de identificação

- **Manuscrito**: smip-famo-framework
- **Versão revisada**: cópia de revisão em Google Docs (ID em `context.md`), lida em
  2026-10-10, já com os lotes 1 e 1b da T01 aplicados. Seções 6.1–6.11 e Seção 7
  (nomes das affordances). Na cópia, a tabela consolidada dos mecanismos aparece como
  "Table ~~4~~ 5" (renumeração da T01-A8 em curso). Este relatório a chama de
  **tabela consolidada (6.11)**.
- **Data**: 2026-10-10
- **Relatórios anteriores consultados**: T01 (relatório e ajustes), `backlog.md` (B01).
- **Status**: **T02.1 concluída** (Seção 12, 2026-10-11). A T02.2 aguarda as decisões
  D6–D9 (12.8). Achados da T02.1 levam o prefixo `T02.1-F`.

---

## 1. Pedido do usuário

> 1. Revisar e validar os 41 mecanismos identificados: verificar o nome de cada mecanismo
>    e confirmar se a literatura efetivamente utiliza esse termo, dando preferência a
>    mecanismos que sejam recorrentes na literatura. Verificar se os nomes alternativos
>    usados são coerentes e se há outros nomes alternativos que podem ser adicionados.
> 2. Revisar a lista dos 41 mecanismos e avaliar sua estrutura: verificar se algum
>    mecanismo pode ser excluído, combinado ou reformulado, evitando sobreposições e
>    tornando a tipologia/taxonomia mais consistente. Além disso, avaliar a definição de
>    cada um dos mecanismos, deixando-as mais consistentes, pois alguns mecanismos estão
>    com uma definição pobre e confusa.
> 3. Explicar claramente o processo de identificação dos 41 mecanismos: explicitar a linha
>    de raciocínio, os critérios e as etapas que levaram à sua identificação, de modo a
>    fortalecer a justificativa e apresentar de forma convincente a contribuição do
>    trabalho.

## 2. Escopo

**Dentro do escopo:**
- os 41 mecanismos (Seções 6.2–6.10) e a tabela consolidada (6.11): nome, alternativos,
  definição, bloco e sobreposições;
- os parágrafos de abertura de cada bloco (critério de agrupamento);
- a definição de *mechanism* da Seção 2.3, usada como régua;
- o texto que descreve como os mecanismos foram identificados: Seção 6.1, Seção 4.3 e
  Figura 1;
- a propagação das mudanças (contagem "41", IDs, tabelas, figuras e fechamentos do loop).

**Fora do escopo** (registrados em uma linha nos achados indiretos quando tocados):
- as colunas *Claim* e *Evidence* da tabela consolidada (T01-I01, T01-I02), exceto quando
  uma fusão ou divisão obrigar a reclassificar o item;
- a correção geral da numeração das referências (tarefa própria; ver P3);
- as affordances (Seção 7), exceto onde o nome colide com o de um mecanismo (O01);
- a tradução das Seções 6.1–6.10 (pendência de edição conhecida).

## 3. Subtarefas

| ID | Subtarefa | Parte do pedido | Depende de | Produto |
|---|---|---|---|---|
| T02.1 | Critérios e inventário | 1, 2, 3 | — | Régua (teste de mecanismo, critério de bloco, modelo de definição, regra de nome), inventário dos 41 e mapa de impacto |
| T02.2 | Estrutura da tipologia | 2 | T02.1 | Decisão por mecanismo (manter, dividir, fundir, mover, reformular, excluir) e lista final com N mecanismos |
| T02.3 | Fichas por bloco: nome, alternativos e definição | 1, 2 | T02.2 | Um lote por bloco (M, A, B, C, D, E, F, G, H) com nome verificado, alternativos e definição nova em inglês |
| T02.4 | Processo de identificação | 3 | T02.1, T02.2; relação com T01-A10 (bloqueado por T01-D2) e B01 | Texto para a 6.1 e a 4.3; ajuste da Figura 1 |
| T02.5 | Propagação | — | T02.2–T02.4 | Contagem, IDs, tabelas, figuras e fechamentos do loop coerentes com a lista final |

**Por que a estrutura (T02.2) vem antes das fichas (T02.3):** redigir a definição de um
mecanismo que depois será fundido ou excluído é trabalho perdido. A T02.2 decide **o que
fica**. A T02.3 decide **como cada item se chama e como é definido**.

## 4. Anotações do usuário (hipóteses H01–H14)

Cada hipótese vira um achado `T02-F*n*` quando for avaliada. A coluna "Leitura inicial"
registra o que já se vê no texto. **Não é veredito.** Afirmações sobre o conteúdo das
obras citadas ficam **[a verificar]** até a leitura do PDF (regra 4).

| ID | Mec. | Anotação | Subtarefa | Leitura inicial |
|---|---|---|---|---|
| H01 | M1 | Tratar *echo chamber* e *filter bubble* como mecanismos separados | T02.2 | O próprio texto diz que são "dois processos com causas distintas (escolha social vs. curadoria algorítmica)". Separar faria a divisão coincidir com a fronteira entre os blocos B (rede) e A (curadoria). Verificar também se *epistemic bubble* (alternativo) não é um terceiro conceito. |
| H02 | M2 | *Myside bias* deveria ser alternativo | T02.3 | Hoje está no nome ("Confirmation bias / myside bias"). O alternativo *selective exposure* é discutível: exposição seletiva é comportamento (escolha de fontes), viés de confirmação é processamento. Ver H08. |
| H03 | M3 | Mecanismo confuso: agrupa discurso de ódio, incivilidade e debates improdutivos como "sintomas" e não explica a relação com F1, F2 e F4 | T02.2 | Fato: o texto trata M3 como "sintoma observável mais do que mecanismo causal primário", o que contraria a definição de mecanismo da 2.3 ("a recurring causal process"). M3 e F4 têm a mesma fonte na coluna Ref ([50], Anderson et al.). Acrescentar *hate speech*, *incivility* e *unproductive debate* como alternativos aumentaria a mistura, porque são construtos diferentes. Opções a avaliar: (a) retirar M3 da lista e tratar a toxicidade como manifestação observável dos mecanismos F; (b) reformular M3 com passo causal próprio (exposição à incivilidade → polarização afetiva), decidindo a fronteira com F4. |
| H04 | M4 | *Misinformation* e *disinformation* são coisas diferentes: separar nos alternativos | T02.3 | Procede (diferença de intencionalidade). Há uma questão anterior: M4 nomeia um tipo de conteúdo, não um processo (ver O02). |
| H05 | A3 | A3 deveria estar no bloco A? A abertura do bloco opõe "decisão de exibição" (A) a "estrutura de conexões" (B) | T02.2 | Há um problema maior: A3 tem o mesmo nome da affordance AF2 (ver O01). A4 (*context collapse*) se encaixa ainda menos no critério do bloco A do que A3. |
| H06 | B1 | Não explica o que é homofilia | T02.3 | A entrada só traz a fonte (McPherson et al. [37]), sem definição. |
| H07 | B5 | Mecanismo incompreensível | T02.3 | O nome junta dois processos (tensão interpessoal e ativação da saliência identitária). É o único mecanismo "introduzido neste artigo" e aparece também nas Seções 5.1 e 9.2. Precisa de definição passo a passo. |
| H08 | C1 | Qual a diferença para viés de confirmação? | T02.2 | Cluster M2–C1–C2. Hipótese a conferir nas fontes: *motivated reasoning* é o processo mais amplo (metas direcionais guiando o raciocínio, Kunda [49]); viés de confirmação é a tendência de buscar e avaliar informação a favor da crença prévia (Nickerson [48]); assimilação enviesada é a etapa de avaliação da evidência (Lord et al. [65]). Isso pode justificar manter os três com fronteiras explícitas ou fundi-los. Pergunta associada: M2 é um viés cognitivo, e o bloco C existe para isso. Por que M2 está no bloco M? |
| H09 | D4 | Não explica o que é *social proof* | T02.3 | A entrada só traz o experimento de Muchnik et al. [41]. |
| H10 | E2 | Não fica claro como amplifica a polarização | T02.3 | A entrada descreve o modelo de Van Bavel e Pereira [69], mas não o passo causal até o outcome. |
| H11 | E3 | Explicar melhor a relação | T02.3 | E3 é o único "Creates" da tabela. Possível sobreposição com A1 e E1 (ver O05). |
| H12 | F2 | Não explica o que é *dogpiling* | T02.3 | O texto descreve a fonte como estudo de "tempestades online" (Rost et al. [73]). Verificar qual termo a literatura acadêmica usa (*dogpiling* × *online firestorm*). |
| H13 | G2 | Melhorar a definição | T02.3 | A entrada descreve um achado sobre os EUA, não o mecanismo. |
| H14 | G4 | Melhorar a definição | T02.3 | Nome composto (*deplatforming* e *migration*) e *Claim* "Amplifies or hosts". |

## 5. Observações da leitura inicial (O01–O08)

Pontos que surgiram ao ler as Seções 2.3, 6 e 7 para montar o plano. Serão confirmados
na T02.1 e, se confirmados, viram achados `T02-F*n*` com severidade.

- **O01 — Mecanismos com nome de affordance.** A1 "Engagement-based ranking" é
  alternativo de AF1. A3 "Connection/friend recommendation" coincide com AF2 "Connection
  recommendation (alt.: 'friend/people recommendation')". A4 "Context collapse" tem o mesmo
  nome de AF6. E4 "Social quantification" tem o mesmo nome de AF4. O alternativo de F3,
  "constraint affordance effect", remete a AF7 "Constraint affordance". A Seção 2.3 diz que
  revisões anteriores "conflate affordance with mechanism", e a contribuição 1 do paper é
  separar essas camadas. **Candidato a Crítico**: um revisor que leia a 2.3 e depois a
  tabela vai encontrar a mesma confusão que o paper critica. Isso responde, em parte, à H05.
- **O02 — Itens que podem não passar na definição de mecanismo da 2.3** ("a recurring
  causal process, decomposable into discrete steps"): M3 (o próprio texto o chama de
  sintoma), M4 (tipo de conteúdo), M5 (estratégia de atores, e a 2.3 define *Actor* como
  construto à parte, citando "coordinated manipulation campaigns" como exemplo), M6
  (processo genérico que duplica o *feedback loop* do framework), E3 (estrutura econômica).
- **O03 — Definições sem formato comum.** A maioria das entradas dos blocos A–H não tem
  uma frase de definição própria e começa direto pela evidência (ex.: A1, B1, D4, E2, G2).
  Quase nenhuma diz como o processo leva ao outcome indicado na tabela.
- **O04 — Critério de bloco × membros.** A abertura do bloco C diz que seus mecanismos são
  "predominantemente hospedados (não criados ou amplificados)", mas a tabela classifica C4
  e C5 como "Amplifies". A abertura do bloco A fala em "decisão de exibição", e A4 (*context
  collapse*) não é decisão algorítmica. O critério do bloco M ("transversais") não explica
  por que M2, um viés cognitivo, está fora do bloco C.
- **O05 — Sobreposições candidatas (clusters):**
  (a) cognitivo: M2, C1, C2 (H02, H08);
  (b) isolamento: M1, A3, B1 (H01, H05);
  (c) toxicidade: M3, F1, F2, F4 (H03);
  (d) indignação: C5, E1, A1, E3 (H11);
  (e) radicalização: A2, G3;
  (f) percepção de normas: M7, D1, D2, D3, D4, B3;
  (g) exposição × evitação: M1, M2, H1, H2.
- **O06 — Nomes compostos** ("&" ou "/"): M1, M2, B5, C5, D1, D3, E4, G4, H2. Para cada um,
  testar se é um construto ou dois (mesma lógica de H01).
- **O07 — Coluna Ref e numeração.** A coluna Ref da tabela consolidada diverge da lista de
  referências (T01-I03). Exemplo: no texto de M1, Bakshy et al. é [39], e na Seção 5.2 [39]
  é Ross et al. Verificar o nome de cada mecanismo na fonte definidora exige resolver cada
  fonte **pelo nome do autor**, não pelo número.
- **O08 — Alcance de qualquer mudança estrutural.** "41 mechanisms/mecanismos" aparece 11
  vezes na cópia de revisão. Os IDs aparecem também na Figura 3 e na 5.2 (M7, B1, E1, C5,
  D3), na Figura 4, na matriz de affordances (Tabela ~~5~~ 6), nas Figuras 5–15 e nas
  Seções 9–11. Toda fusão, divisão ou exclusão tem efeito em cascata (T02.5).

## 6. Roteiro

Cada caixa é uma unidade de trabalho que pode ser feita numa sessão. Ao concluir uma
caixa, os achados entram na seção da subtarefa neste relatório, e os ajustes entram em
`adjustments/T02-ajustes.md`, aplicados por lote após aprovação.

### T02.1 — Critérios e inventário (concluída em 2026-10-11; resultado na Seção 12, aguardando D6–D9)
- [x] **1.1 Teste de mecanismo.** Transformar a definição da 2.3 em perguntas
  verificáveis (é um processo? tem passos? leva a qual outcome?) e aplicá-las aos 41.
  Resultado: lista de itens que não passam (O02).
- [x] **1.2 Critério de bloco.** Escrever o critério de cada bloco em uma frase (o insumo
  comum) e conferir os membros (O04, H05).
- [x] **1.3 Modelo de definição.** Proposta inicial: (i) o que é, em uma frase; (ii) como
  leva à polarização, com passo causal até o outcome da tabela; (iii) o que a plataforma
  muda, coerente com o *Claim*; (iv) fonte definidora e evidência.
- [x] **1.4 Regra de nomenclatura.** Nome principal = termo da fonte definidora, recorrente
  na literatura. Alternativos = sinônimos de fato, não construtos vizinhos. Nunca usar nome
  de affordance ou feature (O01).
- [x] **1.5 Inventário.** Tabela de 41 linhas: ID, nome, alternativos, tem definição?,
  passa no teste?, bloco confere?, fonte definidora (pelo nome do autor), hipóteses e
  observações ligadas.
- [x] **1.6 Mapa de impacto.** Onde cada ID e a contagem "41" aparecem no paper (O08).

### T02.2 — Estrutura da tipologia (concluída em 2026-10-13; Seção 14, D6 e D10–D36; 41 → 39 mecanismos em 7 blocos)
- [x] **2.1** Resolver os itens que não passam no teste de mecanismo (O02; H03, H04). Concluída em 2026-10-12: D13–D19, Seção 14.1.
- [x] **2.2** Resolver as colisões de nome com affordances (O01; H05). Concluída em 2026-10-12: D20–D24, Seção 14.2.
- [x] **2.3** Avaliar os clusters de sobreposição, um por vez (O05): (a) cognitivo (H02,
  H08); (b) isolamento (H01, H05); (c) toxicidade (H03); (d) indignação (H11);
  (e) radicalização; (f) percepção de normas; (g) exposição × evitação.
- [x] **2.4** Testar os nomes compostos (O06). Concluída em 2026-10-13: D35, Seção 14.4.
- [x] **2.5** Revisar o critério e a composição de cada bloco à luz de 2.1–2.4. Concluída em 2026-10-13: D6 = (a), Seção 14.5.
- [x] **2.6** Fechar a lista final (N mecanismos) com a tabela de correspondência
  ID antigo → ID novo.

### T02.3 — Fichas por bloco (concluída em 2026-10-16; lotes 1–8, T02-A1 a A78)
Para cada mecanismo: (i) o nome é usado na literatura? é recorrente? (ii) os alternativos
são sinônimos? faltam alternativos? (iii) definição no modelo de 1.3; (iv) ajuste
correspondente.
Blocos e IDs da lista final (14.6, D6, D36). Cada lote inclui a abertura do bloco e as
mudanças estruturais que o afetam (fusões, exclusões, itens que chegam de outros blocos).
- [x] **Bloco A** — curadoria algorítmica (A1–A4). Lote 1 (T02-A1 a A8) aplicado em 2026-10-13
- [x] **Bloco B** — rede, grupo e difusão (B1–B8; H01, H06, H07). Lote 2 (T02-A9 a A22) aplicado em 2026-10-13
- [x] **Bloco C** — seleção e processamento individual da informação (C1–C8; H02, H08). Lote 3 (T02-A23 a A37) aplicado em 2026-10-13; C8 aguarda B02
- [x] **Bloco D** — percepção dos outros (D1–D6; H09). Lote 4 (T02-A38 a A48) aplicado em 2026-10-13; D2 = social proof (alt. social influence bias, herding), confirmado pelo usuário
- [x] **Bloco E** — incentivos (E1–E3; H10, H11). Lote 5 (T02-A49 a A54) aplicado em 2026-10-13; fonte direta para E3 adiada (B04)
- [x] **Bloco F** — interação (F1–F5; H03, H12). Lote 6 (T02-A55 a A63) aplicado em 2026-10-13, com D29 na 7.1
- [x] **Bloco G** — ecossistema e oferta (G1–G5; H04, H13, H14). Lote 7 (T02-A64 a A71) aplicado em 2026-10-13
- [x] **Affordances em conflito** — AF1, AF2, AF4, AF6, AF7 (7.1, 7.2; D20–D25). Lote 8 (T02-A72 a A78) aplicado em 2026-10-16

### T02.4 — Processo de identificação
- [ ] **4.1** Separar o que pode ser declarado sem os autores (os critérios fixados em
  T02.1 e T02.2, como regras de consolidação **aplicadas nesta revisão**) do que só os
  autores sabem (como os candidatos surgiram, em que ordem e quais foram descartados), que
  fica como `[AUTORES: …]`. Não apresentar critérios novos como se tivessem guiado a
  identificação original.
- [ ] **4.2** Redigir o texto: parágrafo novo na 6.1 (identificação e consolidação dos
  mecanismos) e remissão na 4.3.
- [ ] **4.3** Coordenar com T01-A10 e T01-A11 (documentação da 4.3 e Figura 1, bloqueados
  por T01-D2), para não haver dois textos sobre o mesmo processo.
- [ ] **4.4** Decidir a relação com B01 (Table S1, trilha de auditoria).

### T02.5 — Propagação
- [ ] **5.1** Contagem "41" e IDs no texto (mapa de 1.6).
- [ ] **5.2** Tabela consolidada (6.11), matriz de affordances e Figuras 3, 4 e 5–15.
- [ ] **5.3** Fechamentos do *feedback loop* (5.2 e 9.1) que citam mecanismos alterados.

## 7. Decisões necessárias antes de começar

| # | Decisão | Opções | Recomendação |
|---|---|---|---|
| D1 | Como verificar se a literatura usa cada nome | (a) fonte definidora em PDF + frequência do termo no OpenAlex (só consultas curtas de termos, sem trechos do paper); (b) só as fontes definidoras; (c) conhecimento do agente marcado como [a verificar] | **(a)**. Exige os PDFs das fontes definidoras em `references/` (P2). |
| D2 | Referências novas | (a) só a lista atual do paper; (b) permitir referências novas onde a definição exigir (ex.: *misinformation* × *disinformation*) | **(b)**, via `/literature-review` num tema de `areas/`. Não há tema vinculado: definir onde. |
| D3 | IDs após fusões e divisões | (a) IDs estáveis durante o trabalho (ex.: M1a, M1b) e renumeração única na T02.5; (b) renumerar a cada decisão | **(a)** |
| D4 | Idioma das definições novas | A Seção 6 ainda está em português. Pela política de ajustes, o texto novo é em inglês. | Inglês. Confirmar. |
| D5 | Ordem dos lotes da T02.3 | Ordem do paper (M → H) ou começando pelos blocos com mais anotações | Ordem do paper. Começar pelo M, que concentra H01–H04. |

## 8. Pendências

| # | Item [a verificar] | Ligado a | O que falta |
|---|---|---|---|
| P1 | `paper/v1-2026-10-08.pdf` não está mais na pasta local (estava em 2026-10-10, pela manhã) | Regra 2 (versão revisada) | Restaurar o arquivo ou registrar uma nova versão datada |
| P2 | PDFs das fontes definidoras dos 41 mecanismos (hoje 4 de 106 referências têm PDF) | T02.1, T02.3, D1 | Depósito em `references/` e atualização de `reference-coverage.md` |
| P3 | Numeração das referências (coluna Ref e citações no texto) | O07, T01-I03 | Tarefa própria de verificação de referências; até lá, resolver as fontes pelo nome do autor |
| P4 | Fatos do processo que só os autores conhecem | T02.4, T01-P6 (pausada, T01-D2) | Resposta dos autores |

---

## 9. Decisões do usuário (2026-10-11)

| # | Decisão | Efeito |
|---|---|---|
| D1 | **(a)** Fonte definidora em PDF + frequência do termo no OpenAlex (só consultas curtas de termos) | O usuário está depositando os PDFs em `references/` (cobertura na Seção 10). Sem PDF, o ponto fica [a verificar]. |
| D2 | **(b)** Referências novas permitidas onde a definição exigir | Exceção desta tarefa à regra "só referências da lista" (`manuscripts/CLAUDE.md`). Busca via `/literature-review` num tema de `areas/`, **local ainda a definir**. Obra nova entra na lista do paper com BibTeX pelo G1. |
| D3 | **(a)** IDs estáveis durante o trabalho (ex.: M1a, M1b) e renumeração única na T02.5 | — |
| D4 | Texto novo em inglês | Definições novas substituem o texto em português da Seção 6. |
| D5 | Ordem do paper (M → H) | T02.3 começa pelo bloco M. |
| D-estilo | Regras de redação para todo texto que vai para o paper: inglês; sem travessão (regra fundamental); evitar ponto e vírgula; termos em inglês sem aspas; evitar o padrão de texto gerado por IA | Registrado como regra permanente em `manuscripts/CLAUDE.md` ("Estilo de redação do texto novo"). Citação literal com página mantém as aspas. |
| D-marcação | Ajustes aplicados no documento: texto antigo riscado e mantido, novo texto logo depois com marca-texto **verde** | Substitui o amarelo da T01 (T01-D-marcação) a partir de 2026-10-11, em todas as tarefas. Registrado em `manuscripts/CLAUDE.md` ("Marcação no documento"). Trechos amarelos já aplicados continuam como estão. |
| D-renome | PDFs de `references/` renomeados para `[n]_Ano_Autor_Título.pdf` | 53 arquivos renomeados em 2026-10-11 e duplicata de [59] removida. Convenção atualizada em `manuscripts/CLAUDE.md` e `reference-coverage.md`. O relatório da T01 cita os nomes antigos (ex.: `[15]_Pare_2015.pdf`) e não foi reescrito (regra 7). |
| D-sem-PDF | Para as fontes que o usuário não conseguiu obter (livros, Prentice e Miller [40], Skovsgaard e Andersen [80]), usar o conhecimento do agente e o que estiver disponível na internet | Exceção à regra 4 nesta tarefa. Cada afirmação indica a origem: [abstract OpenAlex], [página da editora] ou [conhecimento do agente]. Resultados na Seção 11. |

## 10. Fontes dos mecanismos: cobertura em `references/` (insumo de D1 e T02.1)

Fontes citadas na entrada de cada mecanismo (Seções 6.2–6.10), resolvidas **pelo nome do
autor** e numeradas pela **lista de referências** (O07). Situação em 2026-10-11, após o
depósito e a renomeação (D-renome). ✅ = PDF na pasta · ◐ = só abstract ou resumo ·
📕 = livro ou capítulo não obtido (D-sem-PDF).

| Mec. | Fontes [n da lista] | Situação |
|---|---|---|
| M1 | Sunstein [43] 📕, Pariser [44] 📕, Bakshy [45] ✅, Cinelli [46] ✅ | livros sem PDF |
| M2 | Festinger [47] 📕, Nickerson [48] ✅ | livro sem PDF |
| M3 | Anderson [49] ✅, Gervais [50] ✅ | completo |
| M4 | Vosoughi [51] ◐, Del Vicario [52] ✅ | [51]: só o *research brief* do MIT IDE |
| M5 | Woolley e Howard [53] 📕, Elmas [54] ✅ | livro sem PDF |
| M6 | Slater [55] ✅ | completo |
| M7 | Noelle-Neumann [24] ✅ | completo |
| A1 | Milli [14] ✅, Rathje 2021 [38] ✅ | completo |
| A2 | Ribeiro [56] ✅, Hosseinmardi [57] ✅ | completo |
| A3 | Chaney [58] ✅, Santos [59] ✅ | completo |
| A4 | Marwick e boyd [60] ✅ | completo |
| A5 | Gillespie [16] 📕 (capítulo) | sem PDF |
| B1 | McPherson [37] ✅ | completo |
| B2 | Sunstein [43] 📕, Isenberg [61] ✅ | livro sem PDF |
| B3 | Vosoughi [51] ◐, Del Vicario [52] ✅ | [51]: só o *research brief* |
| B4 | Mason [62] ✅ | completo |
| B5 | Tanyel e Windeler [5] ✅ | completo |
| C1 | Kunda [63] ✅, Taber e Lodge [64] ✅ | completo |
| C2 | Lord [65] ✅ | completo |
| C3 | Vallone [23] ✅ | completo |
| C4 | Hasher [66] ✅ | completo |
| C5 | Brady 2017 [67] ✅ | completo |
| D1 | Bor e Petersen [68] ✅ | completo |
| D2 | Levendusky e Malhotra [10] ✅, Moore-Berg [11] ✅ | completo |
| D3 | Ross [39] ✅, Prentice e Miller [40] 📕 | [40]: fechado, sem abstract (D-sem-PDF) |
| D4 | Muchnik [41] ✅ | completo |
| E1 | Brady 2021 [13] ✅ | completo |
| E2 | Van Bavel e Pereira [69] ✅ | completo |
| E3 | Munn 2020 [70] ✅ | completo |
| E4 | Lindström [71] ✅ | completo |
| F1 | Suler [72] ✅ | completo |
| F2 | Rost [73] ✅ | completo |
| F3 | Jaidka [9] ✅ | completo |
| F4 | Anderson [49] ✅ | completo |
| G1 | Bennett e Livingston [74] ✅ | completo |
| G2 | Benkler [75] 📕 | sem PDF |
| G3 | Munn 2019 [76] ✅ | completo |
| G4 | Horta Ribeiro [77] ✅ | completo |
| G5 | Myers West [78] ✅ | completo |
| H1 | Toff e Kalogeropoulos [79] ◐ | abstract; PDF aberto na OUP, baixar pelo navegador (ver O09) |
| H2 | Skovsgaard e Andersen [80] ◐, Toff e Kalogeropoulos [79] ◐ | abstracts (ver O09, O10) |

**Resumo**: 52 fontes distintas. **42 com PDF**, 3 só com abstract ou resumo ([51], [79],
[80]) e 7 sem texto ([16], [40], [43], [44], [47], [53], [75]). Ainda vale baixar: **Toff e Kalogeropoulos [79]** (gratuito no site da OUP) e, se
possível, o artigo completo de **Vosoughi et al. [51]** na *Science*.

**Numeração no texto × lista** (amostra que apareceu neste mapeamento, para a tarefa de
referências): no bloco M, Bakshy é citado como [39] (lista: [45]) e Cinelli como [40]
([46]). De Anderson a Mason, o texto cita n+1 (ex.: Anderson [50] → [49]). Kunda é citado
como [49] (lista: [63]).

## 11. Fontes sem PDF: o que foi possível conferir (2026-10-11)

Base: metadados e abstracts do OpenAlex (consulta por título ou DOI, sem trechos do paper).
Pela D-sem-PDF, isso conta como fonte verificável. Os achados abaixo entram como
observações e viram `T02-F*n*` no lote do bloco H (T02.3).

- **O09 — Toff e Kalogeropoulos [79]: subtítulo e conteúdo atribuídos não conferem.**
  - *Fato (lista do paper)*: "All the News That's Fit to Ignore: How the Practice of News
    Use Privileges News That Fits Our Current Beliefs". *Fato (OpenAlex, DOI
    10.1093/poq/nfaa016)*: Public Opinion Quarterly 84(S1), 366–390, 2020. O título em
    repositório (VUB) é "All the News That's Fit to Ignore: How the Information
    Environment Does and Does Not Shape News Avoidance". O abstract descreve um estudo de
    67.000 respondentes em 35 países sobre os preditores da evitação de notícias
    (demografia, atitudes políticas, preferência de gênero noticioso) e mostra que
    liberdade de imprensa, liberdade política e estabilidade reduzem a evitação.
  - *Fato (paper, H1)*: "Toff and Kalogeropoulos [79] documentam como a prática de consumo
    de notícias privilegia o que já se alinha a crenças prévias, inclusive por meio da
    evitação completa". Em H2, o paper atribui à mesma obra uma "assimetria partidária".
  - *Julgamento preliminar*: a afirmação de H1 repete o subtítulo da lista, que não
    corresponde ao publicado, e não aparece no abstract. A "assimetria partidária" também
    não aparece no abstract. Candidato a **Importante**: atribuição e metadado
    incorretos. **[a verificar no PDF]**, que está aberto na OUP.
- **O10 — Skovsgaard e Andersen [80]: a distinção que o artigo faz é outra.**
  - *Fato (OpenAlex, DOI 10.1080/1461670X.2019.1686410, online 2019)*: o artigo propõe
    "a model distinguishing two types of news avoidance, intentional and unintentional,
    depending on the underlying causes leading people to tune out".
  - *Fato (paper, H2)*: "Skovsgaard and Andersen [80] conceituam formalmente a evitação
    seletiva, distinta da evitação geral".
  - *Julgamento preliminar*: no abstract, o eixo é **intencional × não intencional**, não
    **seletiva × geral**, e não há recorte partidário. H2 (*selective/partisan news
    avoidance*) pode estar ancorado na fonte errada ou com o conceito trocado. Sem o texto
    completo, a conferência fica no abstract e no conhecimento do agente.
- **Prentice e Miller [40]**: sem abstract no OpenAlex e fechado na APA. O uso que o paper
  faz (ignorância pluralística como distorção da norma percebida, D3) é coerente com o
  conteúdo conhecido do artigo (conhecimento do agente). Conferir na T02.3, bloco D.
- **Livros** ([16], [43], [44], [47], [53], [75]): conferência pelo conhecimento do agente e
  por páginas de editora ou resenhas, com a origem indicada em cada afirmação, quando o
  bloco correspondente for revisado.

---

## 12. T02.1 — Critérios e inventário (2026-10-11)

Base: cópia de revisão lida em 2026-10-11 (Seções 2.2, 2.3, 5, 6, 7.1, 8–11). Os
julgamentos desta seção vêm do **texto do paper**. A conferência nas fontes é feita na
T02.2 (itens estruturais) e na T02.3 (fichas). Os achados levam o prefixo `T02.1-F`.

### 12.1 Teste de mecanismo (roteiro 1.1)

Régua: a definição da Seção 2.3, "A recurring causal process, decomposable into discrete
steps, through which an input condition produces a measurable increase in polarization",
lida junto com as outras quatro categorias da mesma seção (*feature*, *affordance*,
*contingency*, *actor*) e com os cinco *outcomes* da 2.2.

| # | Pergunta | Falha típica |
|---|---|---|
| Q1 | O nome designa um **processo** (algo que acontece e muda um estado)? | Nomeia um estado, um tipo de conteúdo, um grupo, uma estrutura ou um sintoma |
| Q2 | Dá para escrever a cadeia **insumo → passo → mudança** em pelo menos dois passos? | Não há passo identificável, ou o item é um guarda-chuva de vários processos |
| Q3 | A mudança final é um dos **cinco outcomes** (2.2), sem ser o próprio outcome? | O item é o outcome com outro nome |
| Q4 | O item **não é** uma *feature*, *affordance*, contingência ou ator (2.3)? | Tem nome ou natureza de outra camada |

Veredito: **✅ passa** · **🔧 reformular** (o processo existe, mas o nome ou o recorte está
errado: estado no lugar do processo, dois construtos num nome só) · **❌ não passa como
está** (o item pertence a outra categoria). Resultado: **21 ✅, 9 🔧, 11 ❌** (inventário,
12.5).

### 12.2 Critério de bloco (roteiro 1.2)

Fato: as aberturas dos blocos usam quatro bases de divisão diferentes.

| Base declarada na abertura | Blocos |
|---|---|
| **Insumo comum** ("cujo insumo comum é…") | A (decisão algorítmica de exibição), B (estrutura de conexões), E (estrutura de recompensa), F (interação direta), G (propriedades macro do ecossistema) |
| **Natureza do processo** | C (vieses cognitivos individuais), H (comportamento de fuga) |
| **Outcome** | D ("cujo desfecho primário é a camada perceptiva") |
| **Resíduo** | M ("não se encaixam exclusivamente em nenhuma das demais categorias") |

Membros que não conferem com a abertura do próprio bloco:
- **A4** (*context collapse*) não é decisão algorítmica de exibição.
- **C4 e C5** são "Amplifies" na tabela, mas a abertura do bloco C diz que seus mecanismos são
  "predominantemente hospedados (não criados ou amplificados)". C5 (*contagion*) também é
  um processo de difusão, não um viés individual.
- **M2** é um viés cognitivo (a base do bloco C), e não um item "transversal".
- **B4** (*partisan sorting*) é alinhamento de identidades sociais. Não depende da
  estrutura de conexões que define o bloco B.
- **G3** descreve trajetórias individuais em comunidades fechadas, e não uma propriedade
  macro do ecossistema. Sobrepõe-se a A2.
- **G5** é uma percepção, mais próxima do bloco D.

**Proposta para a T02.2**: adotar uma base única, o **locus do processo** (onde ele
acontece): algoritmo (A), rede (B), cognição individual (C), percepção dos outros (D),
incentivos (E), interação (F), ecossistema (G). O bloco M se dissolve: os itens que passam
no teste vão para o bloco do seu locus. O bloco H vira parte de C ou de um bloco de
exposição seletiva, a decidir junto com o cluster (g). A alternativa é manter os nove
blocos e reescrever as aberturas, declarando que as bases são mistas. É mais barata, mas
um revisor de taxonomia tende a apontar a mistura.

### 12.3 Modelo de definição (roteiro 1.3)

Cada entrada da Seção 6 passa a ter, nesta ordem:
1. **O que é**: uma frase, com a fonte que define o termo.
2. **O que a plataforma muda**: dose, velocidade, escala ou visibilidade, coerente com o
   *Claim* da tabela e com a affordance que alimenta o mecanismo.
3. **Como leva à polarização**: o passo causal até o outcome indicado na tabela.
4. **Evidência** (opcional): o estudo mais direto, com o desenho (experimento, survey,
   auditoria, simulação).

Duas a quatro frases, em inglês, seguindo as regras de estilo de `manuscripts/CLAUDE.md`.

**Exemplo (B1)**, para validar o modelo. A frase 1 vem de McPherson et al. [37], p. 416:
"Homophily is the principle that a contact between similar people occurs at a higher rate
than among dissimilar people".

> Homophily is the tendency of similar people to form ties at a higher rate than
> dissimilar people [37]. On social media, it shapes whom users follow and keep in their
> networks, and connection recommendations based on network similarity can strengthen it
> (AF2, AF3). Repeated homophilous tie formation sorts users into politically homogeneous
> clusters, which is the network segregation measured as structural polarization
> (Section 2.2).

O exemplo mostra a diferença entre o **processo** (formação de laços entre semelhantes) e o
**estado** que ele produz (segregação da rede, que é o outcome). Hoje o alternativo
"network segregation" de B1 nomeia o estado (ver F03).

### 12.4 Regra de nomenclatura (roteiro 1.4)

- **R1** O nome principal é o termo que a fonte definidora usa, conferido no PDF.
- **R2** Havendo mais de um termo corrente, prefere-se o mais recorrente. A recorrência é
  medida pela contagem no OpenAlex (título e resumo), registrada na ficha (D1).
- **R3** O nome designa o **processo**, e não o estado resultante, o tipo de conteúdo, o
  ator, o sintoma ou a estrutura.
- **R4** Nenhum nome repete o nome de uma *feature*, *affordance* (AF1–AF11) ou *outcome*
  (Tabela 1).
- **R5** Um nome, um construto. "&" e "/" só entre sinônimos estritos. Se forem dois
  construtos, dividir ou escolher um.
- **R6** Alternativos são sinônimos ou variantes usadas na literatura **para o mesmo
  processo**. Construto vizinho não entra como alternativo: vai para a definição, como
  distinção ("distinct from…").
- **R7** Nomes e alternativos em inglês, sem aspas (regra de estilo).

### 12.5 Inventário dos 41 (roteiro 1.5)

Legenda. **Def.**: o texto define o mecanismo? S = sim · P = só indiretamente, pelo achado
de uma fonte · N = não. **Passo**: o texto diz como o mecanismo leva ao outcome? S · P · N.
**Fonte no texto**: como o paper usa a fonte (verbo da frase e título da obra): *define*
o termo · *outro termo* (a fonte define um conceito com outro nome) · *só evidência*.
Numeração da lista.

| ID | Nome atual | Alternativos atuais | Def. | Passo | Teste | Fonte no texto | Ligações |
|---|---|---|---|---|---|---|---|
| M1 | Informational isolation/segregation | echo chamber, filter bubble, epistemic bubble | P | N | 🔧 nome designa estado. "Segregation" coincide com a definição de structural (2.2). Funde dois processos | [43], [44] define · [45], [46] evidência | H01, F03 |
| M2 | Confirmation bias / myside bias | selective exposure, motivated dissonance avoidance | S | P | ✅ (bloco errado) | [47], [48] define | H02, H08 |
| M3 | Online toxicity | uncivil discourse, online political hostility | N | N | ❌ sintoma, pelo próprio texto | [49], [50] só evidência | H03 |
| M4 | Information disorder | misinformation/disinformation, fake news | S | N | ❌ tipo de conteúdo | [51], [52] só evidência | H04 |
| M5 | Coordinated inauthentic behavior | astroturfing, computational propaganda | S | N | ❌ estratégia de ator (*Actor*, 2.3) | [53] define · [54] evidência | — |
| M6 | Reinforcing spiral | feedback loop | S | N | ❌ guarda-chuva. Duplica o loop do framework (5.2). Outcome "Varies" | [55] define | — |
| M7 | Spiral of silence | self-censorship, chilling effect | S | S | ✅ (bloco a rever) | [24] define | — |
| A1 | Engagement-based ranking | algorithmic amplification | N | N | ❌ nome de affordance (alternativo de AF1) | [14], [38] só evidência | F01 |
| A2 | Algorithmic radicalization | rabbit hole | S | P | ✅ | [56], [57] só evidência | cluster (e) |
| A3 | Connection/friend recommendation | people-you-may-know | N | N | ❌ nome de affordance (AF2) | [58], [59] só evidência (simulação, modelo) | H05, F01 |
| A4 | Context collapse | context collision, imagined audience | P | N | ❌ nome de affordance (AF6). Fora do critério do bloco A | [60] define | F01, F05 |
| A5 | Algorithmic agenda-setting | trending topics | S | N | ✅ | [16] define | — |
| B1 | Homophily | assortative mixing, network segregation | N | N | ✅ (alternativo "network segregation" nomeia o outcome) | [37] define | H06, F03 |
| B2 | Group polarization | choice shift | S | S | ✅ | [43], [61] define | — |
| B3 | Information cascades | herding, social contagion | S | P | ✅ ("social contagion" é outro construto) | [51], [52] só evidência | cluster (f) |
| B4 | Partisan sorting | social sorting, mega-identity | N | N | ✅ (bloco a rever) | [62] define | F05 |
| B5 | Interpersonal political tension & identity salience activation | — | P | S | 🔧 nome composto | [5] define | H07 |
| C1 | Motivated reasoning | identity-protective cognition | P | N | ✅ | [63] define · [64] evidência | H08 |
| C2 | Biased assimilation | disconfirmation bias | P | S | ✅ | [65] define | H08 |
| C3 | Hostile media effect | — | P | N | ✅ | [23] define | — |
| C4 | Illusory truth effect | truth effect | P | N | ✅ (*Claim* contradiz a abertura do bloco) | [66] define | F05 |
| C5 | Negativity bias & moral-emotional contagion | moral contagion | N | N | 🔧 dois construtos | [67] define (*moral contagion*) | F05 |
| D1 | Vocal minority / extremity bias | sampling bias | N | N | 🔧 nome designa um grupo, não o processo de inferência | [68] só evidência | — |
| D2 | False polarization | perceived polarization, perception gap | P | S | ❌ é o outcome *perceived*. A 2.2 diz que *perceived* e *false polarization* são distintos, e o alternativo usa o nome do outcome | [10] define · [11] evidência | F03 |
| D3 | False consensus & pluralistic ignorance | misperceived norms | N | N | 🔧 dois construtos | [39], [40] define | cluster (f) |
| D4 | Social proof | bandwagon effect, social influence bias | N | N | ✅ | [41] outro termo (*social influence bias*) | H09 |
| E1 | Social learning of outrage | outrage amplification | P | N | ✅ | [13] define | cluster (d) |
| E2 | Identity signaling | partisan expressive behavior | N | N | ✅ | [69] define (modelo) | H10 |
| E3 | Attention economy | outrage industry, rage-bait | N | N | ❌ estrutura econômica (contexto), não processo | [70] outro termo (*angry by design*) | H11, F07 |
| E4 | Social quantification / vanity metrics | gamified reputation | N | N | ❌ nome de affordance (AF4) | [71] só evidência (modelo) | F01 |
| F1 | Online disinhibition effect | deindividuation | P | N | ✅ | [72] define | cluster (c) |
| F2 | Dogpiling | pile-on, online shaming, firestorm | N | N | ✅ | [73] outro termo (*online firestorms*) | H12 |
| F3 | Low-context communication | brevity effect, constraint affordance effect | N | N | 🔧 nome descreve o formato. Alternativo remete a AF7 | [9] outro termo (*constraint affordance*) e evidência | F01 |
| F4 | Incivility contagion | toxicity contagion, nasty effect | P | P | ✅ | [49] define (*nasty effect*) | H03 |
| G1 | Disintermediation / gatekeeping decline | epistemic fragmentation | N | N | ✅ | [74] outro termo (*disinformation order*) | — |
| G2 | Network propaganda | hyperpartisan media ecosystem | N | N | ❌ designa uma estrutura do ecossistema | [75] define | H13 |
| G3 | Radicalization pipeline | fringe community pathway | P | N | ✅ (bloco a rever, sobreposição com A2) | [76] define (*alt-right pipeline*) | cluster (e) |
| G4 | Deplatforming & migration | platform migration | N | N | 🔧 junta ação de governança (AF10) e comportamento dos usuários | [77] só evidência | H14 |
| G5 | Perceived censorship | perceived moderation bias | P | N | 🔧 nome designa percepção (estado) | [78] define (teorias dos usuários) | F05 |
| H1 | News avoidance | news fatigue | N | N | 🔧 caminho até a polarização não explicitado | [79] só evidência, atribuição não confere (O09) | O09 |
| H2 | Selective/partisan news avoidance | checked-out citizens | P | N | ✅ | [80] outro conceito (O10) · [79] | O10, cluster (g) |

Totais: **Def.** S 9 · P 14 · N 18. **Passo** S 5 · P 4 · N 32. **Fonte no texto**: define
25 · outro termo 6 · só evidência 10.

### 12.6 Achados

| ID | Achado | Severidade |
|---|---|---|
| T02.1-F01 | Mecanismos com nome de affordance | **Crítico** |
| T02.1-F02 | Itens que não passam na definição de mecanismo da 2.3 | **Crítico** |
| T02.1-F03 | Mecanismos com nome de outcome | Importante |
| T02.1-F04 | Definições ausentes e sem passo causal | Importante |
| T02.1-F05 | Blocos com bases de divisão diferentes | Importante |
| T02.1-F06 | Mecanismos sem fonte que os defina, contra o critério de inclusão da 4.3 | Importante |
| T02.1-F07 | Mecanismos sem nenhuma affordance ligada | Menor |

#### T02.1-F01 — Mecanismos com nome de affordance · **Crítico** · confirma O01
- **Localização**: Seção 6.3 (A1, A3, A4), 6.7 (E4), 6.8 (F3), tabela consolidada (6.11);
  Seção 7.1 (AF1, AF2, AF4, AF6, AF7); Seção 2.3.
- **Fato**: A1 "Engagement-based ranking" é alternativo de AF1 ("alt.: engagement-based
  ranking"). A3 "Connection/friend recommendation" coincide com AF2 "Connection
  recommendation (alt.: 'friend/people recommendation')". A4 e AF6 se chamam "Context
  collapse". E4 e AF4 se chamam "Social quantification". O alternativo de F3, "constraint
  affordance effect", remete a AF7 "Constraint affordance". A 2.3 afirma que revisões
  anteriores "conflate affordance with mechanism at specific points in their syntheses".
- **Julgamento**: o paper comete, em cinco itens, a confusão que apresenta como problema
  dos trabalhos anteriores, e que a contribuição 1 promete resolver. Um revisor que leia a
  2.3 e depois a tabela consolidada nota de imediato. Em cada caso existe um processo por
  trás da affordance, e é ele que deve dar nome ao mecanismo (T02.2).

#### T02.1-F02 — Itens que não passam na definição de mecanismo da 2.3 · **Crítico** · confirma e amplia O02
- **Localização**: Seção 6, M3, M4, M5, M6, D2, E3, G2 (além dos quatro de F01).
- **Fato**: pelo teste de 12.1, 11 dos 41 itens não são processos causais. M3 é chamado
  pelo próprio texto de "sintoma observável mais do que mecanismo causal primário". M4
  ("circulação de conteúdo falso ou enganoso") é tipo de conteúdo. M5 é estratégia de
  atores, e a 2.3 define *Actor* como construto à parte, com "coordinated manipulation
  campaigns" como exemplo. M6 é um "processo genérico", guarda-chuva, com outcome "Varies",
  e duplica o loop da 5.2. D2 é o outcome *perceived* (ver F03). E3 é uma estrutura
  econômica. G2 é uma estrutura do ecossistema de mídia.
- **Julgamento**: um quarto da taxonomia não cumpre a definição que o próprio paper dá. É
  o ponto mais exposto da contribuição 2 ("41 mecanismos tratados como unidades
  auditáveis"). Para cada item, a T02.2 decide entre excluir, reformular como processo
  ou mover para outra camada (Actor, contingência).

#### T02.1-F03 — Mecanismos com nome de outcome · **Importante** · novo
- **Localização**: Seção 2.2, §2; Seção 6, M1, B1 e D2.
- **Fato**: a 2.2 diz que "Structural polarization corresponds directly to the metrics of
  network segregation and homophily" e que "Perceived polarization, closely related to
  but distinct from false polarization, is formalized here as an independent category".
  M1 se chama "Informational isolation/**segregation**". B1 tem "network segregation" como
  alternativo. D2 se chama "False polarization" e tem "perceived polarization" como
  alternativo.
- **Julgamento**: quando mecanismo e outcome têm o mesmo nome, a cadeia mecanismo →
  outcome fica circular. Em D2, o alternativo contradiz a 2.2 diretamente. No caso de B1,
  o problema é só o alternativo: o processo (formação de laços entre semelhantes) é
  distinto do estado (segregação). Ver o exemplo de 12.3.

#### T02.1-F04 — Definições ausentes e sem passo causal · **Importante** · confirma O03, H06–H14
- **Fato**: das 41 entradas, 18 não têm frase de definição e 14 só definem indiretamente,
  pelo achado de uma fonte. Só 5 dizem como o mecanismo leva ao outcome indicado na tabela
  (M7, B2, B5, C2, D2).
- **Julgamento**: sem o passo causal, as colunas *Outcome* e *Claim* da tabela não podem
  ser conferidas pelo leitor. O modelo de 12.3 resolve as duas coisas. As anotações H06,
  H07 e H09–H14 são casos particulares deste achado.

#### T02.1-F05 — Blocos com bases de divisão diferentes · **Importante** · confirma e amplia O04
- **Fato**: ver 12.2. Cinco blocos são definidos por insumo, dois pela natureza do
  processo, um pelo outcome e um é residual. Sete membros contradizem a abertura do
  próprio bloco (A4, C4, C5, M2, B4, G3, G5).
- **Julgamento**: uma tipologia com bases mistas não garante exclusividade mútua, e cada
  sobreposição apontada pelo usuário (H05, H08) nasce dessa mistura. Proposta em 12.2.

#### T02.1-F06 — Mecanismos sem fonte que os defina, contra o critério de inclusão da 4.3 · **Importante** · novo
- **Localização**: Seção 4.3, §1; Seção 6.
- **Fato**: a 4.3 define como critério de inclusão "that each item of the taxonomy […] be
  anchored in at least one primary source with an explicit operational definition". Pelo
  uso no texto, 10 mecanismos só citam estudos de evidência (M3, M4, A1, A2, A3, B3, D1,
  E4, G4, H1). Outros 6 citam uma fonte que define o conceito com **outro nome** (D4, E3,
  F2, F3, G1, H2).
- **Julgamento**: esses 16 itens, como estão, não cumprem o critério que o paper declara.
  É preliminar: a T02.3 confere nos PDFs se as fontes trazem uma definição operacional.
  Onde não trouxerem, a solução é achar a fonte definidora (D2: referência nova) ou
  adotar o termo da fonte (R1). Isso alimenta a T02.4: o critério da 4.3 só se sustenta
  se valer para os 41.

#### T02.1-F07 — Mecanismos sem nenhuma affordance ligada · **Menor** · novo
- **Fato**: M2, M3, C1, C2, C3 e E3 não aparecem na Seção 7.1 nem na matriz da Tabela 6.
  E3 é o único mecanismo classificado como "Creates".
- **Julgamento**: para os vieses hospedados (M2, C1–C3), a ausência é coerente, mas
  precisa ser dita no texto. Para E3, é contraditório: um mecanismo que a plataforma
  "cria" deveria ter um insumo de design identificável. Fica para a T02.2.

### 12.7 Mapa de impacto (roteiro 1.6)

Ocorrências fora da Seção 6, no texto da cópia de revisão. Figuras são imagens e não
entram na busca: as Figuras 3, 4 e 5–15 precisam de conferência visual na T02.5.

| Onde | Mecanismos citados |
|---|---|
| 5.1 | B1, B5 |
| 5.2 (e Figura 3) | M7, B1 por ID. E1 e D3 citados pelo conceito, sem o ID |
| 7.1 (affordances) e Tabela 6 (Seção 8) | os 35 mecanismos com affordance (todos menos M2, M3, C1, C2, C3, E3) |
| 9.1 | M5, A5, B4, D1, D2, D3, D4, E2, F3, G4, G5 |
| 9.2 | B1, B5, G2 |
| 10.2 | M6, C5, E1, E4, G1, G2, H1, H2 |
| 11 | M7, E1, E4, F2, G2 |
| "41 mechanisms" (contagem) | 12 vezes: 3.4 (2), 5.1, 6.1 (2), 6.11 (legenda), 8, 9.1, 9.2, 11 (3) |

Consequência: excluir, fundir ou dividir um mecanismo afeta, no mínimo, a 7.1, a Tabela 6
e as figuras por affordance. Os mais citados fora da Seção 6 (B1, E1, E4, G2, M7) pedem
cuidado extra.

### 12.8 Decisões para iniciar a T02.2

| # | Decisão | Recomendação |
|---|---|---|
| D6 | Base única dos blocos (12.2) | **Locus do processo**, com a dissolução do bloco M |
| D7 | Modelo de definição (12.3) e exemplo B1 | Aprovar ou ajustar |
| D8 | Regra de nomenclatura R1–R7 (12.4) | Aprovar ou ajustar |
| D9 | Destino padrão dos 11 itens ❌ | Reformular como processo quando houver um processo claro por trás (A1, A3, A4, E4, M4, D2, G2, E3). Excluir ou mover de camada quando não houver (M3 → manifestação dos mecanismos F; M5 → camada *Actor*; M6 → loop da 5.2). Cada caso se confirma nas fontes, na T02.2 |

---

## 13. Discurso de ódio, incivilidade e debates improdutivos são mecanismos? (T02.2, cluster c; 2026-10-11)

**Pedido do usuário**: avaliar criticamente se discurso de ódio, incivilidade e debates
improdutivos, que o texto de M3 trata como "sintomas", podem entrar na taxonomia como
mecanismos, e incluí-los se for o caso.

**Bases desta análise**:
- PDFs lidos: Anderson et al. [49], Gervais [50], Bor e Petersen [68] e o artigo dos
  autores aceito no CHIRA 2026 (inédito, confidencial; nenhum trecho foi enviado a
  serviços externos).
- Busca exploratória no OpenAlex, registrada no tema
  `areas/mestrado/smip-paper/mecanismos-interacao/` (27 candidatos em
  `deliverables/candidates.md`, **aguardando aprovação por item**). Até os PDFs chegarem,
  o que se diz sobre esses candidatos vem **só do abstract** e leva a marca [abstract].

### 13.1 O teste de mecanismo aplicado aos três fenômenos

| Fenômeno | Q1: o nome designa um processo? | Q2–Q3: há processo documentado até um outcome? | Leitura |
|---|---|---|---|
| **Incivilidade** | Não. É uma propriedade do discurso (tom, desrespeito a normas de conversa). A literatura separa a impolidez da falta de deliberação e de reciprocidade (Muddiman 2017 [abstract]) e a civilidade da polidez (Papacharissi 2004 [abstract]) | Sim, e mais de um: exposição → percepção e afeto (13.2, P1) · exposição → mais incivilidade (P2) | **Insumo** de processos, e também **produto** de outros (F1, E1, F2) |
| **Discurso de ódio** | Não. É um tipo de conteúdo: ataque a grupos. Rossini 2020 [abstract] separa a **intolerância** (ataque a grupos e direitos) da incivilidade (tom) | Sim: exposição frequente → dessensibilização → preconceito (P3) · normas percebidas → expressão de ódio (P4) | **Insumo** de processos. Mesmo caso de M4 (tipo de conteúdo) |
| **Debate improdutivo** | Parcialmente. É uma propriedade da interação (baixa qualidade deliberativa), mas o artigo CHIRA descreve, a partir de Angenot, duas dinâmicas que são processos: a **retórica da incompreensão** ("refusal or inability to recognize the adversary as a rational being", Seção 3.1) e a **ilusão de racionalidade** ("individuals argue more to justify themselves before their own audience", Seção 3.1) | Fraco e misto: discussão com o outro lado reduz hostilidade em Amsalem et al. 2021 [abstract] e aumenta a polarização afetiva via *unfriending*, condicionada à incivilidade, em Lin et al. 2023 [abstract] | Melhor como **condição** (moderador) do efeito da exposição ao outro lado. A deslegitimação do adversário é o processo candidato |

**Conclusão do teste**: nenhum dos três passa **com esse nome**, pela mesma razão que M3 e
M4 não passam. Eles designam **o que circula ou o estado da conversa**, e não **como** a
polarização é produzida. A literatura, porém, documenta processos com passos em que eles
são o insumo. O texto atual de M3 acerta em parte ao chamá-los de sintomas: eles são
produto de mecanismos como F1 (desinibição) e E1 (aprendizagem social da indignação). Mas
não diz que também são **gatilho** de outros processos, e é aí que estão os mecanismos que
faltam na taxonomia.

### 13.2 Processos encontrados (candidatos a mecanismo)

| # | Processo (nome provisório, a conferir pela R1) | Cadeia | Outcome | Base | Relação com a taxonomia atual |
|---|---|---|---|---|---|
| P1 | **Efeito da exposição à incivilidade** (*incivility exposure effect*; *nasty effect*) | Exposição a discussão incivil → reação afetiva (raiva, aversão) e julgamento pelos valores prévios → polarização da percepção do tema e da percepção do público | perceived, affective (ideological nas percepções de tema) | Anderson [49], p. 374: "to examine how uncivil online interpersonal discussion may contribute to polarization of perceptions about an issue". Gervais [50], p. 167: discordância incivil "induces feelings of anger and aversion". Hwang et al. 2014 [abstract]: sem efeito sobre atitudes, com efeito sobre a polarização percebida do público. Druckman et al. 2018 [abstract]: a incivilidade do out-party polariza afetivamente, e a do in-party despolariza. Skytte 2020 [abstract] separa incivilidade e distância ideológica | **Não existe hoje.** O *nasty effect* aparece como alternativo de F4, mas é este processo, não contágio (ver T02.2-F01) |
| P2 | **Contágio da incivilidade** (*incivility contagion*) | Exposição à incivilidade, sobretudo do próprio lado → normas da conversa mudam → mais comentários incivis | behavioral (e realimenta P1) | Gervais [50], p. 167: "exposure to like-minded incivility increases the use of uncivil behavior". Kim et al. 2021 [abstract] | **É F4**, que precisa de definição nova e sem o alternativo *nasty effect* |
| P3 | **Dessensibilização ao discurso de ódio** (*desensitization to hate speech*) | Exposição frequente → menor sensibilidade à violência verbal → avaliação pior do grupo-alvo e distanciamento → preconceito. Desprezo no lugar de empatia | affective | Soral et al. 2017 [abstract], dois surveys e um experimento. Bilewicz e Soral 2020 [abstract] | **Não existe hoje** |
| P4 | **Erosão de normas contra o discurso de ódio** (*normative change*) | Usuários inferem a aceitabilidade pelo que veem os outros fazendo (norma descritiva) e pelas sanções → mais expressão de ódio | behavioral | Álvarez-Benjumea e Winter 2018 e 2020 [abstract] | Sobrepõe-se a F4 (contágio) e a D3/D4 (normas percebidas, prova social). Candidato a **entrar na definição de F4**, e não a item próprio |
| P5 | **Deslegitimação do adversário** (*out-group delegitimization*; retórica da incompreensão) | Na discussão, o adversário é tratado como irracional ou de má-fé → o desacordo vira juízo sobre a pessoa → hostilidade ao out-group | affective | Artigo CHIRA (Angenot, ensaio teórico). Marchal 2021 [abstract]: interações entre usuários opostos no Reddit são mais negativas | **Não existe hoje.** Evidência ainda "Plausible". A "ilusão de racionalidade" (falar para a própria plateia) já está perto de E2 (*identity signaling*) |

### 13.3 Recomendação preliminar

1. **Não acrescentar** discurso de ódio, incivilidade e debate improdutivo como mecanismos
   com esses nomes, nem como alternativos de M3. Pela R6, eles são construtos distintos
   entre si (Rossini 2020 [abstract]) e distintos dos processos que desencadeiam.
2. **Retirar M3** como mecanismo, o que confirma a recomendação D9. Incivilidade,
   intolerância e discurso de ódio passam a ser definidos na abertura do bloco F como
   **manifestações observáveis**: produzidas por F1, E1 e F2, e insumo de P1–P4. Isso
   responde à anotação H03, porque deixa explícita a relação com F1, F2 e F4.
3. **Acrescentar P1 e P3** como mecanismos novos, se os PDFs confirmarem o que dizem os
   abstracts. Os dois têm cadeia causal, desenho experimental e outcome do paper.
4. **Reformular F4 (= P2)** e incorporar P4 à definição dele (o contágio opera por normas
   percebidas). Tirar *nasty effect* dos alternativos de F4.
5. **Debate improdutivo** entra como **contingência**: a qualidade da interação modera o
   efeito da exposição ao outro lado (Amsalem et al. × Lin et al. [abstract]). P5
   (deslegitimação) só entra como mecanismo se a leitura dos candidatos 15, 25 e 26 trouxer
   evidência além do ensaio teórico. Até lá, fica como candidato "Plausible".

Efeito líquido na contagem: −M3, +P1, +P3, e +P5 se aprovado (de 41 para 42 ou 43, antes
das demais decisões da T02.2).

### 13.4 Achado novo

#### T02.2-F01 — O alternativo *nasty effect* de F4 nomeia outro processo · **Importante** · novo
- **Localização**: Seção 6.8, F4; tabela consolidada (6.11).
- **Fato**: F4 se chama *Incivility contagion* e tem *nasty effect* como alternativo. A
  fonte do *nasty effect*, Anderson et al. [49], estuda como a incivilidade "may contribute
  to polarization of perceptions about an issue" (p. 374). Ou seja, estuda o efeito da
  exposição sobre a percepção de quem lê, e não a propagação da incivilidade. O contágio
  propriamente dito aparece em Gervais [50], p. 167 ("exposure to like-minded incivility
  increases the use of uncivil behavior").
- **Julgamento**: F4 junta dois processos com outcomes diferentes: perceived/ideological
  no *nasty effect* e behavioral no contágio. A tabela atribui a F4 o outcome "Affective",
  que não corresponde a nenhum dos dois com precisão. A separação proposta em 13.2 (P1 ×
  P2) resolve o problema.

### 13.5 Para fechar o cluster (c)

- **Aprovar os candidatos** em `areas/mestrado/smip-paper/mecanismos-interacao/deliverables/candidates.md`
  (marcar `[x]`). Prioridade para a decisão: 3 (Rossini), 4 (Hwang), 5 (Druckman),
  7 (Kim), 15 (Marchal), 17 (Soral), 18 (Bilewicz e Soral), 19 (Álvarez-Benjumea e
  Winter), 25 (Amsalem), 26 (Lin).
- Depois do download, reler P1–P5 contra os PDFs e fechar as decisões D10–D12.

| # | Decisão | Recomendação |
|---|---|---|
| D10 | Os três fenômenos entram como mecanismos com esses nomes? | **Não.** Entram como manifestações observáveis na abertura do bloco F |
| D11 | P1 (exposição à incivilidade) e P3 (dessensibilização ao ódio) entram como mecanismos novos? | **Sim**, condicionado à leitura dos PDFs |
| D12 | Debate improdutivo: contingência ou mecanismo (P5, deslegitimação)? | **Contingência** agora. P5 fica como candidato "Plausible" até a leitura |

### 13.6 Decisões do usuário (2026-10-12)

| # | Decisão | Efeito |
|---|---|---|
| D10 | **Não**: discurso de ódio, incivilidade e debate improdutivo não entram como mecanismos | Confirma a recomendação |
| D11 | **Não**: nenhum mecanismo novo por ora. Prioridade: terminar a revisão dos 41 | P1 e P3 ficam registrados como candidatos para o futuro, fora da T02 |
| D12 | **Não mexer** em debate improdutivo por enquanto (nem contingência, nem mecanismo) | P5 fica registrado, fora da T02 |

O achado T02.2-F01 (F4 × *nasty effect*) continua válido e será resolvido na ficha de F4
(T02.3, bloco F) ou na 2.1 abaixo, conforme a decisão sobre M3.

---

## 14. T02.2 — Estrutura da tipologia (2026-10-12)

Modo de trabalho (pedido do usuário): uma subtarefa por vez. O agente sugere, o usuário
aprova item a item. Restrição vigente (D11): não acrescentar mecanismos. Só excluir,
fundir, mover ou reformular os 41.

### 14.1 Subtarefa 2.1 — Itens que não passam no teste de mecanismo

Escopo: os 7 itens ❌ de 12.5 que **não** têm nome de affordance (M3, M4, M5, M6, D2, E3,
G2). Os quatro com nome de affordance (A1, A3, A4, E4) são a subtarefa 2.2.
"Reformular" mantém o ID e a posição na contagem, e o nome final sai na T02.3, pela R1.

#### M3 — Online toxicity
- **Fato**: o texto chama M3 de "sintoma observável mais do que mecanismo causal primário".
  As duas fontes ([49], [50]) são estudos de efeito, e [49] é também a única fonte de F4.
  M3 não aparece fora da Seção 6 (12.7).
- **Opções**:
  (a) **excluir** M3 e descrever incivilidade, intolerância e discurso de ódio na abertura do
  bloco F como manifestações observáveis, produzidas por F1, E1 e F2 e insumo de F4. Isso
  responde à H03 e segue a D10.
  (b) **reformular** M3 no mesmo lugar como o efeito da exposição à incivilidade (P1 da Seção
  13), com Anderson [49] e Gervais [50]. Mantém a contagem, mas na prática é o P1 que a D11
  deixou de fora.
- **Recomendação**: **(a)**, coerente com D10 e D11. Consequência na T02.3: F4 passa a citar
  Gervais [50] (contágio) e perde o alternativo *nasty effect* (T02.2-F01).
- **Contagem**: −1.

#### M4 — Information disorder
- **Fato**: M4 e B3 (*Information cascades*) citam **as mesmas duas fontes**, Vosoughi et al.
  [51] e Del Vicario et al. [52]. Del Vicario [52] (p. 554) estuda "the determinants
  governing misinformation spreading" e conclui que "cascade dynamics differ" entre
  narrativas. Ou seja, o processo que as fontes de M4 descrevem **é** o de B3.
- **Opções**: (a) **fundir M4 em B3**: B3 passa a cobrir a difusão em cascata, inclusive de
  conteúdo falso. A distinção *misinformation* × *disinformation* (H04) entra na definição
  de B3, e a desinformação intencional fica com os atores (ver M5). (b) reformular M4 como
  difusão de desinformação, separada de B3, com o risco de duplicar B3. (c) excluir.
- **Recomendação**: **(a)**.
- **Contagem**: −1. **Impacto**: 7.1 e Tabela 6 (M4 → B3).

#### M5 — Coordinated inauthentic behavior
- **Fato**: a 2.3 define *Actor* como "an agent […] that deliberately triggers or exploits a
  mechanism, such as in coordinated manipulation campaigns". Elmas et al. [54] (p. 1)
  descrevem um ataque "on the popularity mechanisms of social media platforms", em que um
  tema "is artificially promoted by coordinated and inauthentic activity to appear
  popular". O processo explorado é o de A5 (*trending*) e o de D4 (prova social).
- **Opções**: (a) **excluir** M5 da lista e tratá-lo como o exemplo de *Actor* que a 2.3 já
  usa. Elmas [54] passa a ilustrar, em A5 e D4, como atores exploram esses mecanismos.
  (b) reformular como "consenso fabricado", com sobreposição forte a A5, D3 e D4.
- **Recomendação**: **(a)**. É a solução que o próprio paper prevê na 2.3.
- **Contagem**: −1. **Impacto**: 7.1, Tabela 6, 9.1.

#### M6 — Reinforcing spiral
- **Fato**: o texto chama M6 de "processo genérico de retroalimentação […] que funciona como
  guarda-chuva para instâncias específicas discutidas na Seção 5.2". O outcome na tabela é
  "Varies". O PDF em `references/` descreve o modelo como "a dynamic and recursive process"
  que integra a seletividade (M2, H2) e os efeitos da mídia, ou seja, um metamodelo.
  **Atenção**: esse PDF não é Slater 2007 [55], o artigo citado. É um texto posterior de
  Slater, Shehata e Strömbäck sobre o mesmo modelo.
- **Opções**: (a) **excluir** M6 e citar Slater [55] na 5.2 como base teórica do *feedback
  loop*. (b) manter, redefinido como a espiral individual identidade ↔ consumo de mídia,
  distinta do loop sistêmico da Figura 2. Ainda assim, ficaria sobreposto a M2 e H2.
- **Recomendação**: **(a)**.
- **Contagem**: −1. **Impacto**: 7.1, Tabela 6, 10.2, 5.2.

#### D2 — False polarization
- **Fato**: Levendusky e Malhotra [10] definem *false polarization* como perceber "more
  polarization with respect to policy issues than actually exists" (abstract, p. 378). É o
  outcome *perceived* da Tabela 1. A segunda fonte, Moore-Berg et al. [11] (p. 14864),
  trata de outra coisa: **metapercepções** (o que achamos que o outro grupo pensa de nós),
  que são exageradas "approximately twice" e predizem hostilidade.
- **Opções**: (a) **reformular** D2 como o efeito das metapercepções exageradas: perceber
  o out-group como mais hostil do que é → hostilidade recíproca (perceived → affective).
  É um processo distinto de D1 (por que a percepção se distorce) e de D3 (normas). *False
  polarization* passa a ser descrita na 2.2, junto do outcome *perceived*, e o alternativo
  "perceived polarization" sai (T02.1-F03). (b) fundir D2 em D1. (c) excluir.
- **Recomendação**: **(a)**. Fonte já na lista, com PDF.
- **Contagem**: 0. **Impacto**: 7.1, Tabela 6, 9.1, 2.2.

#### E3 — Attention economy
- **Fato**: Munn [70] não define "attention economy". O argumento dele (p. 1) é que o Feed
  do Facebook "privileges incendiary content, setting up a stimulus-response loop that
  promotes outrage expression" e que a recomendação do YouTube leva a "more extreme
  content". Esses processos já são A1, E1 e A2. E3 é o único "Creates" e não tem affordance
  ligada (T02.1-F07).
- **Opções**: (a) **excluir** E3 e redistribuir Munn [70] como evidência em A1 e E1.
  (b) **reformular** E3 como o incentivo do lado da **oferta**: veículos, jornalistas e
  criadores ajustam o conteúdo às métricas de engajamento. Nenhum outro mecanismo cobre os
  produtores, o que é relevante para um periódico de jornalismo. A fonte natural já está
  na lista: Petre [102], *All the News That's Fit to Click: How Metrics Are Transforming
  the Work of Journalists* (sem PDF; [conhecimento do agente; conferir]).
- **Recomendação**: **(b)**, se você conseguir o livro de Petre ou aceitar a D-sem-PDF para
  ele. Se não, **(a)**.
- **Contagem**: 0 em (b), −1 em (a).

#### G2 — Network propaganda
- **Fato**: o texto descreve um achado sobre os EUA ("o ecossistema de mídia da direita se
  mostrou historicamente mais insular e menos autocorretivo"), que é uma estrutura. No livro
  de Benkler et al. [75], o processo que produz essa estrutura se chama *propaganda feedback
  loop*: veículos, políticos e audiência recompensam histórias que confirmam a identidade e
  punem quem as checa [conhecimento do agente; conferir, livro sem PDF].
- **Opções**: (a) **reformular** G2 como esse ciclo (processo → ecossistema insular →
  ideological, perceived). (b) fundir em G1 (*disintermediation*). (c) excluir.
- **Recomendação**: **(a)**. G2 é citado na 9.2, na 10.2 e na 11, então excluí-lo custa
  caro.
- **Contagem**: 0.

#### Resumo da 2.1

| Item | Recomendação | Contagem |
|---|---|---|
| M3 | Excluir. Manifestações descritas na abertura do bloco F | −1 |
| M4 | Fundir em B3 | −1 |
| M5 | Excluir. Vira o exemplo de *Actor* (2.3); Elmas [54] vai para A5 e D4 | −1 |
| M6 | Excluir. Slater [55] vai para a 5.2 como base do loop | −1 |
| D2 | Reformular: metapercepções exageradas (perceived → affective) | 0 |
| E3 | Reformular: incentivo de métricas do lado da oferta (Petre [102]), ou excluir | 0 ou −1 |
| G2 | Reformular: *propaganda feedback loop* | 0 |

Se tudo for aprovado como recomendado: **41 → 37**. O bloco M ficaria com M1, M2 e M7, o
que pesa na decisão D6 (dissolver o bloco M), na subtarefa 2.5.

**Status**: aguardando aprovação item a item.

#### Decisões do usuário — 2.1 (2026-10-12)

| # | Item | Decisão | Efeito |
|---|---|---|---|
| D13 | M3 | **(b) reformular no mesmo lugar** como o efeito da exposição à incivilidade (P1 da 13.2) | Contagem 0. Fontes: Anderson [49], Gervais [50]. Resolve T02.2-F01: o *nasty effect* sai de F4 e vai para M3. F4 fica só com o contágio, que passa a citar Gervais [50] |
| D14 | M4 | **(a) fundir em B3** | −1. B3 recebe Vosoughi [51] e Del Vicario [52] e a distinção *misinformation* × *disinformation* (H04). Na 7.1 e na Tabela 6, M4 → B3 |
| D15 | M5 | **(b) reformular** como consenso fabricado | Contagem 0. A definição deve separar M5 de A5, D3 e D4: M5 é o processo de fabricar sinais de popularidade, e A5/D4 são os processos que esses sinais acionam. Elmas [54] continua em M5. Termo a conferir na T02.3 (*manufactured consensus*, usado na literatura de propaganda computacional [conhecimento do agente; conferir]) |
| D16 | M6 | **Manter como está** por enquanto | Contagem 0. Registrado em `backlog.md` (B02) para revisão futura |
| D17 | D2 | **(a) reformular** como o efeito das metapercepções exageradas | Contagem 0. *False polarization* vai para a 2.2, junto do outcome *perceived*. Sai o alternativo "perceived polarization" (T02.1-F03) |
| D18 | E3 | **(b) reformular** como incentivo de métricas do lado da oferta | Contagem 0. Fonte: Petre [102]. **O arquivo obtido é só a resenha** de Holton (2024), fonte secundária (D-sem-PDF). Pela resenha, o livro trata de como as métricas mudam "the stories they choose to cover", e as plataformas criam "a feedback loop where sensational stories and vitriolic content thrive" (Holton, p. 315). A ligação com a polarização é indireta ("deepening audience fragmentation and siloing", p. 315): a evidência de E3 deve continuar "Plausible" |
| D19 | G2 | **(a) reformular** como *propaganda feedback loop* | Contagem 0. Benkler [75] sem PDF (D-sem-PDF) |

**Contagem após a 2.1: 41 → 40** (só M4 sai, fundido em B3).

**Ajustes decorrentes** (texto redigido na T02.3, no lote do bloco de cada item):
M3 (bloco M), M5 (bloco M), D2 (bloco D), E3 (bloco E), G2 (bloco G) e F4 (bloco F,
sem *nasty effect*). A fusão de M4 em B3 entra no lote do bloco B, com a retirada da
entrada M4 (6.2), da linha M4 da tabela consolidada e a troca M4 → B3 na 7.1 e na
Tabela 6.

### 14.2 Subtarefa 2.2 — Colisões de nome entre mecanismos e affordances (2026-10-12)

**Pergunta do usuário**: em cada colisão, basta trocar o nome ou o problema é mais
profundo, isto é, a affordance não é affordance ou o mecanismo não é mecanismo?

**Réguas**:
- **Affordance**: os três critérios de Evans et al. [34], a fonte que a 2.3 cita para
  definir affordance. **C1**: não é o objeto nem uma *feature* do objeto (pp. 39–40).
  **C2**: não é um outcome. Affordances "invite behaviors and other outcomes […] but are
  not the outcome itself" (p. 40). **C3**: tem variabilidade, "gradations of affordances"
  (p. 40). Evans dá "filtering" como exemplo de *feature* tratada indevidamente como
  affordance (p. 36), e conclui que *privacy* é "an outcome resulting from affordances such
  as visibility or editability" (p. 44).
- **Feature**, pela 2.3 do próprio paper: "The concrete, platform-specific technical
  element, such as a named button, **a recommendation algorithm**, or **a numerical
  character limit**".
- **Mecanismo**: o teste de 12.1.

Escopo: só as affordances envolvidas nas colisões (AF1, AF2, AF4, AF6, AF7), como pedido.

#### Resumo

| Par | Affordance passa em Evans? | Mecanismo passa no teste? | Diagnóstico |
|---|---|---|---|
| A1 × AF1 | **Não (C1)**: definida como operação do sistema, uma *feature* | **Não**: "engagement-based ranking" é o critério de ordenação de uma *feature* | **Profundo, nas duas camadas** |
| A3 × AF2 | **Não com esse nome (C1)**: "connection recommendation" é *feature*. O alternativo *network-informed associating* passa | **Não**: é a mesma *feature* | **Profundo, nas duas camadas** |
| A4 × AF6 | **Não (C2)**: o próprio paper a descreve como consequência de outras affordances | **Não**: o texto diz que A4 é "the behavioral instance of the affordance itself" | **Profundo, nas duas camadas** |
| E4 × AF4 | **Não como definida (C1)**: "publicly visible counters" são *features* | **Não**: tem o nome da affordance. O processo das fontes é a aprendizagem por recompensa, que já é E1 | **Profundo, nas duas camadas** |
| F3 × AF7 | **Sim**: *constraint affordance* é o termo da fonte e tem variabilidade | **Sim**: brevidade → discussão menos civil | **Só de nome**: tirar o alternativo de F3 |

#### A1 × AF1 — Engagement-based ranking × Algorithmic content curation
- **Fato (affordance)**: AF1 é "the affordance through which content visible to the user is
  selected and ordered by an automated system based on predictive engagement signals". A
  definição descreve o que o **sistema** faz, e não uma possibilidade de ação na relação
  usuário–tecnologia. É o que a 2.3 chama de *feature* ("a recommendation algorithm") e o
  que Evans dá como exemplo de *feature* ("filtering", p. 36). O alternativo de AF1,
  "engagement-based ranking", é ainda mais claramente uma *feature*: o critério de
  ordenação. Bossetta [35] chama esse tipo de "algorithmic affordance". A posição tem
  apoio na literatura, mas não sobrevive ao C1 de Evans, que é a régua que o paper declara.
- **Fato (mecanismo)**: A1 tem o nome do critério de ordenação. O processo está nas fontes:
  - Milli et al. [14] (abstract, p. 1): "Twitter's engagement-based ranking algorithm
    amplifies emotionally charged, out-group hostile content that users say makes them
    feel worse about their political out-group";
  - Rathje et al. [38] (p. 1): termos sobre o out-group são "the strongest predictor of
    shares and retweets".
- **Diagnóstico**: profundo. A1 é uma *feature* com nome de mecanismo, e AF1 é uma
  *feature* com nome de affordance.
- **Opções**:
  (a) **reformular A1** como o processo: a otimização por engajamento amplifica conteúdo de
  animosidade ao out-group, que é o que mais gera engajamento. **Redefinir AF1** em termos
  relacionais (o que o usuário vê e o que consegue tornar visível depende do engajamento
  previsto) e tirar "engagement-based ranking" dos alternativos de AF1. Esse alternativo
  passa a ser citado como exemplo de *feature*.
  (b) só renomear A1, sem mexer em AF1.
- **Recomendação**: **(a)**. Contagem: 0.

#### A3 × AF2 — Connection/friend recommendation × Connection recommendation
- **Fato (affordance)**: AF2 é "the affordance through which a platform suggests connections
  based on network similarity and proximity". O sujeito é a plataforma, e "people you may
  know" é uma *feature* (2.3: "a recommendation algorithm"). O alternativo de AF2,
  *network-informed associating* (Majchrzak et al. [8]), está entre as affordances que
  Evans reconhece (p. 40) e é relacional: o usuário se associa a outros a partir de
  informação sobre a rede.
- **Fato (mecanismo)**: A3 é a mesma *feature*. O processo está nas fontes:
  - Chaney et al. [58] (abstract): sistemas treinados "with data from users already exposed
    to algorithmic recommendations; this creates a pernicious feedback loop", que
    "homogenizes user behavior";
  - Santos et al. [59] (p. 1): as conexões online são "intermediated by link recommendation
    algorithms", em redes que já tendem à homofilia.
- **Fato (coerência interna)**: a 5.1 ("The connection recommendation affordance […] makes
  it more likely that the homophily and clustering mechanism (Section 6.3) operates") e o
  primeiro fechamento do loop (5.2: AF2 → reforça B1) ligam AF2 **direto a B1**, sem passar
  por A3.
- **Diagnóstico**: profundo. A3 não tem processo próprio separado de B1. O processo que
  suas fontes descrevem é a recomendação reforçando a homofilia.
- **Opções**:
  (a) **fundir A3 em B1** (Chaney [58] e Santos [59] viram a evidência do papel da
  plataforma em B1, que já é "Hosts & amplifies") e **renomear AF2** como *network-informed
  associating*, com "connection recommendation" citado como *feature* exemplar;
  (b) reformular A3 como o ciclo de retroalimentação do recomendador (*algorithmic
  confounding*, termo de Chaney [58]). Mantém a contagem, mas Chaney trata de recomendação
  em geral (Netflix, Amazon), não de polarização.
- **Recomendação**: **(a)**. Contagem: −1. Resolve também a H05 (A3 no bloco A).

#### A4 × AF6 — Context collapse × Context collapse
- **Fato (affordance)**: a 7.2 diz que AF6 "does not correspond to the presence of a
  specific design feature, but rather to the absence of an audience segmentation
  affordance", e que boyd [7] trata as audiências invisíveis "as an emergent consequence of
  persistence, searchability, and replicability". Para Evans, o que resulta de outras
  affordances é outcome, não affordance (C2; é o caso de *privacy*, p. 44). Marwick e boyd
  [60] também tratam o colapso como efeito: "Social media technologies collapse multiple
  audiences into single contexts" (abstract).
- **Fato (mecanismo)**: a 7.1 afirma que "the link to A4 (Context collapse) is definitional:
  the mechanism is the behavioral instance of the affordance itself". O processo descrito
  por Marwick e boyd [60] é a gestão da audiência imaginada, com técnicas como "concealing
  subjects". Isso é autocensura (M7) e, na política, a tensão com laços existentes (B5).
  AF6 já alimenta F2, F4, M7 e B5.
- **Diagnóstico**: profundo. AF6 é um outcome, e A4 é o mesmo outcome repetido.
- **Opções**:
  (a) **reformular AF6** como a affordance relacional de **segmentação de audiência**
  (*audience segmentation*), que varia de audiências segmentadas a colapsadas (C3). O
  colapso de contexto passa a ser o polo baixo dessa affordance. A 7.2 já aponta nessa
  direção: AF6 "can only be mitigated by introducing a new affordance, namely segmentation
  tools". **Excluir A4**: seus efeitos já estão mapeados em M7, B5, F2 e F4;
  (b) manter AF6 como "affordance de segunda ordem" e reformular A4 como autocensura pela
  audiência imaginada. Sobreposição forte com M7.
- **Recomendação**: **(a)**. Contagem: −1. A 7.2 precisa ser reescrita.

#### E4 × AF4 — Social quantification / vanity metrics × Social quantification
- **Fato (affordance)**: AF4 é "the affordance through which reactions and reach are converted
  into publicly visible counters". Contadores são *features*: Evans trata assim os alertas
  e notificações (p. 45). A "metrification of sociality" de Van Dijck [42] descreve uma
  lógica cultural, mais próxima de processo ou outcome. Uma formulação relacional existe na
  própria fonte da AF2: *metavoicing* (Majchrzak et al. [8]), reconhecida por Evans (p. 40),
  isto é, reagir publicamente à presença e ao conteúdo dos outros [o conteúdo de Majchrzak
  vem do conhecimento do agente; conferir, sem PDF].
- **Fato (mecanismo)**: E4 tem o nome da affordance. A fonte, Lindström et al. [71] (p. 1),
  mostra que "social media users spaced their posts to maximize the average rate of
  accrued social rewards", ou seja, aprendizagem por recompensa social. Isso não é, em si,
  polarizador. Fica polarizador quando o conteúdo recompensado é a indignação, e esse caso
  já é **E1** (Brady et al. [13]: "social learning processes amplify online moral outrage
  expressions").
- **Diagnóstico**: profundo. E4 é o processo geral de que E1 é o caso polarizador. AF4
  descreve *features*.
- **Opções**:
  (a) **fundir E4 em E1**: Lindström [71] vira a base geral de E1. **Redefinir AF4** em
  termos relacionais (dar e ver feedback quantificado sobre o conteúdo; nome a definir,
  com *metavoicing* como candidato);
  (b) reformular E4 como aprendizagem por recompensa social, geral, separada de E1. Fica
  sobreposto a E1 e sem ligação direta com a polarização.
- **Recomendação**: **(a)**. Contagem: −1. E4 é citado na 10.2 e na 11, que precisam de
  ajuste.

#### F3 × AF7 — Low-context communication × Constraint affordance
- **Fato (affordance)**: *constraint affordance* é o termo de Jaidka et al. [9] (título:
  "Brevity Is the Soul of Twitter: The Constraint Affordance and Political Discussion").
  O limite numérico é a *feature* (2.3). A affordance é o quanto o usuário pode elaborar a
  expressão, e isso tem gradação (C3). Passa, desde que a definição de AF7 seja relacional
  e não fale só do limite.
- **Fato (mecanismo)**: F3 tem processo nas fontes. Jaidka et al. [9] (abstract): "doubling
  the permissible length of a Tweet led to less uncivil, more polite and more constructive
  discussions online". A colisão está só no alternativo "constraint affordance effect".
- **Diagnóstico**: só de nome.
- **Recomendação**: tirar o alternativo "constraint affordance effect" de F3. O nome "Low-
  context communication" será conferido na T02.3, pela R1. Contagem: 0.

#### Achado

##### T02.2-F02 — Quatro das cinco affordances em colisão não passam nos critérios de Evans et al. [34] · **Crítico** · novo
- **Fato**: AF1 e AF2 são definidas pelo que o sistema faz e correspondem aos exemplos de
  *feature* que a 2.3 dá ("a recommendation algorithm"). AF4 é definida como contadores
  (*feature*). AF6 é descrita na 7.2 como consequência emergente de outras affordances
  (outcome). Só AF7 passa.
- **Julgamento**: a contribuição 1 do paper é a separação entre *feature* e affordance, e a
  2.3 cita Evans [34] como base. Um revisor que aplique os três critérios de Evans vai
  encontrar *features* e um outcome na camada de affordances. As colisões de nome com
  mecanismos são o sintoma visível desse problema, e não a causa. A correção é redefinir
  essas affordances em termos relacionais, o que é possível em todos os casos sem trocar a
  numeração AF1–AF11.
- **Ressalva**: os critérios de Evans são exigentes, e parte da literatura (Bossetta [35])
  aceita "algorithmic affordances". O paper pode adotar essa posição, mas então precisa
  dizê-lo e justificar o desvio em relação a Evans, que é a referência declarada.

#### Resumo das recomendações

| Item | Recomendação | Contagem |
|---|---|---|
| A1 | Reformular como amplificação de conteúdo hostil ao out-group pela otimização por engajamento | 0 |
| AF1 | Redefinir em termos relacionais. "Engagement-based ranking" sai dos alternativos (vira *feature* exemplar) | — |
| A3 | Fundir em B1 | −1 |
| AF2 | Renomear como *network-informed associating* | — |
| A4 | Excluir. Efeitos já mapeados em M7, B5, F2, F4 | −1 |
| AF6 | Reformular como segmentação de audiência. O colapso é o polo baixo | — |
| E4 | Fundir em E1 | −1 |
| AF4 | Redefinir em termos relacionais (candidato: *metavoicing*) | — |
| F3 | Tirar o alternativo "constraint affordance effect" | 0 |
| AF7 | Manter. Ajustar a definição para que seja relacional | — |

Se tudo for aprovado: **40 → 37**.

**Decisão de escopo (D25)**: as mudanças nas affordances vão além da revisão dos
mecanismos. Proposta: (i) na T02, só o necessário para desfazer as colisões (as linhas AF
da tabela acima); (ii) abrir uma **T03 — revisão das 11 affordances pelos critérios de
Evans**, para as outras seis (AF3, AF5, AF8, AF9, AF10, AF11), que não foram avaliadas.

**Status**: aguardando aprovação item a item.

#### Decisões do usuário — 2.2 (2026-10-12)

| # | Par | Decisão | Efeito |
|---|---|---|---|
| D20 | A1 × AF1 | **(a)** | A1 é reformulado como a amplificação de conteúdo hostil ao out-group pela otimização por engajamento (Milli [14], Rathje [38]). AF1 é redefinida em termos relacionais, e "engagement-based ranking" sai dos alternativos de AF1 para virar exemplo de *feature*. Contagem 0 |
| D21 | A3 × AF2 | **(a)** | A3 é fundido em B1, com Chaney [58] e Santos [59] como evidência do papel da plataforma. AF2 passa a se chamar *network-informed associating* (Majchrzak [8]), e "connection recommendation" vira exemplo de *feature*. Resolve H05. Contagem −1 |
| D22 | A4 × AF6 | **(a)** | A4 é excluído (efeitos em M7, B5, F2, F4). AF6 é reformulada como segmentação de audiência, com o colapso de contexto como polo baixo. A 7.2 é reescrita. Contagem −1 |
| D23 | E4 × AF4 | **(a)** | E4 é fundido em E1, com Lindström [71] como base geral. AF4 é redefinida em termos relacionais (candidato: *metavoicing*). Ajustes na 10.2 e na 11. Contagem −1 |
| D24 | F3 × AF7 | **Recomendação** | Sai o alternativo "constraint affordance effect" de F3. AF7 é mantida, com definição relacional. Nome de F3 conferido na T02.3. Contagem 0 |

**Contagem após a 2.2: 40 → 37.**

**Ajustes decorrentes**:
- Mecanismos, na T02.3, no lote de cada bloco: A1 (bloco A); A3 → B1 e E4 → E1 (blocos
  B e E); remoção das entradas e das linhas de A3, A4 e E4 da tabela consolidada; F3
  (bloco F).
- Affordances (AF1, AF2, AF4, AF6, AF7): definições na 7.1, a 7.2 e os alternativos. A
  lista "Feeds" de cada affordance, a Tabela 6 e as Figuras 5, 6, 8 e 10 precisam trocar
  A3 → B1, E4 → E1 e retirar A4. O lote depende da D25.

**D25 (2026-10-12)**: **(i)**. Na T02, corrigir só as cinco affordances em conflito (AF1,
AF2, AF4, AF6, AF7). As outras seis não serão revisadas agora (sem T03 por enquanto).

### 14.3 Subtarefa 2.3 — Sobreposições (clusters), uma por vez (2026-10-12)

Clusters de O05, atualizados pelas decisões da 2.1 e da 2.2:

| Cluster | Itens (após D13–D24) | Situação |
|---|---|---|
| (a) cognitivo | M2, C1, C2 | **em análise** (abaixo) |
| (b) isolamento | M1, B1 (já com A3) | a analisar (H01) |
| (c) toxicidade | M3 (exposição à incivilidade), F1, F2, F4 | em grande parte resolvido por D13. Falta conferir a fronteira M3 × F4 e o bloco de M3 |
| (d) indignação | C5, E1 (já com E4), A1, E3 | a analisar |
| (e) radicalização | A2, G3 | a analisar |
| (f) percepção de normas | M7, D1, D2, D3, D4, B3, M5 | a analisar |
| (g) exposição × evitação | M1, M2, H1, H2 | a analisar |

#### Cluster (a) — M2 Confirmation bias × C1 Motivated reasoning × C2 Biased assimilation

**O que as fontes dizem** (PDFs):
- **Kunda [63]**, p. 480: "motivation may affect reasoning through reliance on a biased set
  of cognitive processes: strategies for **accessing, constructing, and evaluating
  beliefs**". O motivo pode ser de precisão ("to be accurate") ou direcional ("to arrive at
  particular conclusions"). Raciocínio motivado é, portanto, o **porquê**: um objetivo
  enviesa todas as etapas do processamento.
- **Nickerson [48]**, p. 175: confirmation bias "refers usually to **unwitting
  selectivity** in the acquisition and use of evidence". Na p. 176, o autor distingue
  "motivated and unmotivated forms of confirmation bias". Ou seja, o viés de confirmação
  pode existir sem motivação, e por isso não é o mesmo que raciocínio motivado. A
  definição de Nickerson cobre tanto a **busca** quanto o **uso** da evidência.
- **Lord, Ross e Lepper [65]**, p. 2098: quem tem opinião forte tende "to accept
  'confirming' evidence at face value while subjecting 'disconfirming' evidence to critical
  evaluation", e o efeito líquido é "the postulated increase in attitude polarization". É
  a etapa de **avaliação** da evidência, e é ela que produz a polarização a partir da
  **mesma** evidência.
- **Taber e Lodge [64]**, p. 755 (abstract), separam as etapas no mesmo modelo de
  *motivated skepticism*: (1) "a **disconfirmation bias**": os participantes
  "counterargue the contrary arguments and uncritically accept supporting arguments"; (2)
  "a **confirmation bias**, the seeking out of confirmatory evidence when Ps are free to
  self-select the source". E "Both the confirmation and disconfirmation biases lead to
  attitude polarization".

**Resposta à H08 (diferença entre C1 e viés de confirmação)**: o raciocínio motivado (C1) é
o **motivo** que enviesa o processamento. O viés de confirmação (M2) é uma das **etapas** em
que esse viés aparece: a busca seletiva pela evidência. A outra etapa é a avaliação
enviesada, que é C2. Nickerson acrescenta que o viés de confirmação também ocorre sem
motivação. Na taxonomia atual, os três itens se sobrepõem porque C1 contém M2 e C2.

**Fato no paper**: M2 traz "selective exposure" e "motivated dissonance avoidance" como
alternativos, cita Festinger [47] e Nickerson [48] e está no bloco M. C1 cita Kunda [63] e
Taber e Lodge [64]. C2 cita Lord [65] e tem "disconfirmation bias" como alternativo. Nenhum
dos três aparece fora da Seção 6 (12.7), então a mudança é barata.

**Opções**:
- **(a) Manter os três**, com fronteiras explícitas: C1 = o motivo; M2 = a busca seletiva;
  C2 = a avaliação enviesada. Contagem 0. Continua havendo um item que contém os outros
  dois, e um revisor de taxonomia tende a apontar isso.
- **(b) Fundir os três** num único mecanismo, *motivated reasoning*, com duas componentes
  (busca e avaliação). Contagem −2. Perde a distinção que mais importa para o paper, que é
  a da busca (ligada à exposição e à estrutura) e a da avaliação (ligada às atitudes).
- **(c) Dois mecanismos, por etapa, e C1 vira a explicação comum**:
  - **M2 → viés de confirmação, restrito à busca seletiva** da evidência (o sentido de Taber
    e Lodge). Vai para o bloco C, junto dos outros vieses cognitivos (decisão final na 2.5);
  - **C2 → assimilação enviesada**, a avaliação enviesada da evidência ("disconfirmation
    bias" continua como alternativo, que é o termo de Taber e Lodge para essa etapa);
  - **C1 é fundido**: Kunda [63] e Taber e Lodge [64] passam a explicar, nas definições de
    M2 e C2, que as duas etapas costumam ser movidas por objetivos direcionais, sem que isso
    seja condição (Nickerson, p. 176).

  Contagem −1.

**Recomendação**: **(c)**. Separa os itens pelo ponto do processamento em que atuam, sem um
item guarda-chuva, e cada um fica com uma fonte que o define.

**Consequência para os alternativos de M2 (H02, a conferir na T02.3)**:
- "selective exposure" é o **comportamento** que resulta da busca seletiva. Pela R6, sai dos
  alternativos e entra na definição como manifestação. Isso também ajuda a separar M2 de H2,
  no cluster (g);
- "motivated dissonance avoidance" sai: é o motivo de Festinger [47], que passa a ser citado
  na definição;
- "myside bias" (sugestão da H02) entra como alternativo **se** a literatura o usar como
  sinônimo da busca seletiva. Não aparece em Nickerson [48]. Conferir pela R2 (contagem no
  OpenAlex) na T02.3.

**Status**: aguardando aprovação.

**D26 (2026-10-12) — cluster (a)**: **opção (a)**, manter M2, C1 e C2 com fronteiras
explícitas. C1 = o motivo (objetivos direcionais que enviesam o processamento, Kunda [63]);
M2 = a busca seletiva da evidência (Nickerson [48], Taber e Lodge [64]); C2 = a avaliação
enviesada (Lord [65]; *disconfirmation bias*, Taber e Lodge [64]). As definições da T02.3
devem dizer explicitamente como cada um se distingue dos outros dois e que C1 atua nas
etapas de M2 e C2. Os alternativos de M2 (H02) seguem para a T02.3. Contagem: 37 (sem
mudança).

#### Cluster (b) — M1 Informational isolation/segregation × B1 Homophily (H01)

**Fato no paper**: M1 é a "fusão de câmara de eco e bolha de filtro, dois processos com
causas distintas (escolha social vs. curadoria algorítmica) mas efeito convergente de
isolamento informacional [Sunstein, 43; Pariser, 44]". Alternativos: echo chamber, filter
bubble, epistemic bubble. Outcome: Structural, Ideological. O nome contém "segregation",
que a 2.2 usa para definir o outcome *structural* (T02.1-F03). B1 (Homophily) já absorveu
A3 (D21).

**O que as fontes dizem** (PDFs):
- **Bakshy et al. [45]**, p. 1130, definem os dois conceitos separadamente: "echo chambers
  (in which individuals are exposed only to information from like-minded individuals)" e
  "filter bubbles (in which content is selected by algorithms according to a viewer's
  previous behaviors)". O estudo decompõe a exposição em três etapas: a rede de amigos
  ("ideological homophily in friend networks"), o ranqueamento algorítmico do News Feed e
  a escolha do usuário. Conclusão: "Compared with algorithmic ranking, individuals'
  choices played a stronger role in limiting exposure to cross-cutting content".
- **Cinelli et al. [46]**, p. 1: "We can broadly define echo chambers as environments in
  which the opinion, political leaning, or belief of users about a topic gets reinforced due
  to repeated interactions with peers or sources having similar tendencies and attitudes".
- Sunstein [43] e Pariser [44] são livros sem PDF (D-sem-PDF). Pariser cunhou *filter
  bubble* para a personalização algorítmica, e Sunstein trata dos *echo chambers* e da
  polarização de grupo [conhecimento do agente; conferir].

**Leitura**: as fontes confirmam a anotação H01. São dois processos, com insumos distintos e
pontos diferentes da cadeia de exposição que Bakshy [45] decompõe:

| Etapa da exposição (Bakshy [45]) | Processo | Onde está hoje |
|---|---|---|
| Com quem o usuário está ligado | Formação de laços entre semelhantes | **B1** (com A3) |
| O que circula e se repete entre os semelhantes | **Câmara de eco**: reforço da crença por interação repetida com pares e fontes alinhados (Cinelli [46]) | dentro de M1 |
| O que o algoritmo seleciona a partir do comportamento anterior | **Bolha de filtro**: personalização algorítmica que estreita a exposição (Pariser [44]) | dentro de M1 |
| O que o usuário escolhe abrir | Busca seletiva | **M2** (D26) |

A fusão em M1 esconde exatamente a distinção que o estudo mais citado do item (Bakshy [45])
testa, ou seja, se o estreitamento vem da rede, do algoritmo ou da escolha.

**Fronteiras a cuidar** (se houver divisão):
- câmara de eco × **B1**: B1 é a formação dos laços (estrutura). A câmara de eco é o reforço
  da crença pelo que circula nesses laços (exposição);
- câmara de eco × **B2** (*group polarization*): B2 é o deslocamento para posições extremas
  depois da deliberação entre semelhantes. A câmara de eco é a exposição repetida que
  reforça a crença, mesmo sem deliberação;
- bolha de filtro × **A1** (D20): A1 amplifica o conteúdo que gera mais engajamento, em
  geral hostil ao out-group. A bolha de filtro estreita a exposição ao que o usuário já
  consumia;
- "epistemic bubble" (alternativo atual): na literatura filosófica, distingue-se de *echo
  chamber* (omissão de vozes × descrédito ativo das fontes de fora) [conhecimento do agente;
  conferir]. Não é sinônimo de nenhum dos dois. Decidir na T02.3.

**Opções**:
- **(a) Dividir M1 em dois** (H01): **M1a, câmara de eco** (processo de rede; bloco B na 2.5)
  e **M1b, bolha de filtro** (processo algorítmico; bloco A na 2.5). Resolve também o nome
  com "segregation" (T02.1-F03). Contagem **+1** (37 → 38). Não é tema novo: é a separação de
  dois processos que o próprio texto de M1 já descreve. Mesmo assim, aumenta a contagem, o
  que esbarra no espírito da D11.
- **(b) Manter M1 fundido**, renomeado como processo (estreitamento da exposição), com as duas
  vias explicitadas na definição. Contagem 0. Mantém um item com dois insumos, o que
  contraria a R5 e a lógica de blocos por insumo.
- **(c) M1 vira só a bolha de filtro**, e a câmara de eco entra na definição de B1 (como
  consequência informacional da homofilia). Contagem 0. Perde o termo mais recorrente da
  literatura como mecanismo nomeado, o que um revisor pode estranhar.

**Recomendação**: **(a)**. É a solução que as fontes sustentam e a que você propôs na H01.
Se a D11 deve valer de forma estrita (não aumentar a contagem), a segunda melhor é **(c)**.

**Impacto**: M1 aparece na 7.1 (AF1 e AF2, "indirect") e na Tabela 6. Na divisão, M1a vai
para a lista de AF2 e AF3 (rede), e M1b para a de AF1 (algoritmo).

**Status**: aguardando aprovação.

**D27 (2026-10-12) — cluster (b)**: **opção (a)**, dividir M1 em **M1a, câmara de eco**
(reforço da crença por interação repetida com pares e fontes alinhados, Cinelli [46]; bloco
B na 2.5) e **M1b, bolha de filtro** (personalização algorítmica que estreita a exposição,
Pariser [44]; bloco A na 2.5). Bakshy [45] fica como evidência comparativa das duas vias e
de M2. As fronteiras com B1, B2 e A1 descritas acima entram nas definições (T02.3). "Epistemic
bubble" é decidido na T02.3. 7.1 e Tabela 6: M1a em AF2 e AF3, M1b em AF1. Contagem:
**37 → 38**.

#### Cluster (c) — M3 (exposição à incivilidade) × F1 Online disinhibition × F2 Dogpiling × F4 Incivility contagion

**Situação após a D13**: M3 virou o efeito da exposição à incivilidade (Anderson [49],
Gervais [50]), e F4 ficou só com o contágio. Falta definir as fronteiras entre os quatro e
conferir as fontes de F1 e F2.

**O que as fontes dizem** (PDFs):
- **Suler [72]**, p. 321: o efeito tem "six factors that interact with each other […]:
  dissociative anonymity, invisibility, asynchronicity, solipsistic introjection,
  dissociative imagination, and minimization of authority", e opera em duas direções,
  "benign disinhibition" e "toxic disinhibition". Só a direção tóxica interessa ao paper. O
  texto de F1 cita só três fatores e não faz a distinção.
- **Bor e Petersen [68]** (hoje fonte de D1), abstract: testam a "mismatch hypothesis",
  segundo a qual o ambiente online piora o comportamento, e "only find evidence for limited
  selection effects. Instead, hostile political discussions are the result of status-driven
  individuals who are drawn to politics and are equally hostile both online and offline".
  É evidência contrária a F1 na política, e F1 não a cita.
- **Rost et al. [73]**, p. 1: *firestorms* são "storms of emotional and aggressive outrage"
  contra alvos públicos, explicados por "social norm theory". O resultado: "in the context
  of online firestorms, non-anonymous individuals are more aggressive compared to anonymous
  individuals", o que contraria "the popular assumption that online anonymity" explica a
  agressão.

**Proposta de fronteiras**: os quatro itens ocupam pontos diferentes de uma mesma cadeia, e
podem continuar separados se as definições disserem isso:

| Ponto da cadeia | Item | Processo | Outcome |
|---|---|---|---|
| Produção individual | **F1** | Características da interação online (anonimato, invisibilidade, assincronia) reduzem a inibição → mais expressão hostil | behavioral (→ affective) |
| Produção coletiva | **F2** | Uma transgressão percebida desencadeia uma onda de sanções agressivas contra um alvo, como aplicação de norma do grupo | behavioral, affective |
| Circulação | **F4** | A incivilidade vista, sobretudo do próprio lado, muda a norma da conversa → mais comentários incivis | behavioral |
| Recepção | **M3** | Quem lê a discussão incivil reage com raiva ou aversão e julga pelos valores prévios → polarização percebida e afetiva | perceived, affective |

Essa cadeia também resolve a H03 e a D10. Incivilidade, intolerância e discurso de ódio são
descritos na abertura do bloco F como o que essa cadeia produz e faz circular, e não como
mecanismos.

**Recomendação**: **manter os quatro**, com as fronteiras da tabela nas definições (T02.3).
**M3 vai para o bloco F**, ao lado dos outros três (decisão de bloco na 2.5). Contagem 0.

#### Achado

##### T02.2-F03 — A justificativa de AF8 → F2 contradiz a fonte de F2 · **Importante** · novo
- **Localização**: Seção 7.1, parágrafo "Why AF8 (Identifiability) feeds each of these
  mechanisms"; Tabela 6, linha AF8.
- **Fato**: o texto diz que "The link to F2 (Dogpiling) follows from the same reduced
  reputational cost applied to coordinated attacks: an attacker operating under a
  disposable identity risks no nominal reputation in the process". A única fonte de F2,
  Rost et al. [73], conclui que "non-anonymous individuals are more aggressive compared to
  anonymous individuals" em *firestorms* (p. 1) e explica isso por aplicação de normas,
  não por perda de inibição.
- **Julgamento**: o paper usa a fonte de F2 de um jeito e justifica a ligação AF8 → F2 com o
  argumento que essa fonte refuta. Um revisor que conheça Rost et al. aponta de imediato.
  Duas saídas: (a) inverter a justificativa (a identificabilidade **aumenta** o ganho de
  reputação de quem sanciona, o que é o argumento de Rost [73]); ou (b) tirar F2 da lista
  de AF8 e manter só a ligação AF6 → F2. Decisão na T02.3 (bloco F), junto da ficha de F2.
- **Relacionado**: F1 deve citar Bor e Petersen [68] como evidência contrária, o que
  sustenta o rating "Mixed" de F1.

**Status**: aguardando aprovação.

**Decisões do usuário — cluster (c) (2026-10-12)**

| # | Decisão | Efeito |
|---|---|---|
| D28 | **Manter M3, F1, F2 e F4**, com as fronteiras da cadeia produção individual → produção coletiva → circulação → recepção | Definições na T02.3 (bloco F). A ida de M3 para o bloco F será decidida na 2.5. Contagem: 38 |
| D29 | T02.2-F03: **inverter a justificativa** de AF8 → F2 | Na 7.1 ("Why AF8 (Identifiability) feeds…"), a ligação com F2 passa a seguir Rost et al. [73]: a identificabilidade aumenta o ganho de reputação de quem sanciona, e os não anônimos são mais agressivos em *firestorms* (p. 1). Ajuste no lote do bloco F |
| D30 | F1 passa a citar **Bor e Petersen [68]** como evidência contrária | Sustenta o rating "Mixed". A definição de F1 também passa a mencionar os seis fatores de Suler [72] e a distinção *benign* × *toxic* (p. 321). Ajuste no lote do bloco F |

#### Cluster (d) — C5 Negativity bias & moral-emotional contagion × E1 Social learning of outrage × A1 (amplificação algorítmica) × E3 (incentivo de métricas na oferta)

**Situação após D18, D20 e D23**: A1 é a amplificação de conteúdo hostil ao out-group pela
otimização por engajamento (Milli [14], Rathje [38]). E1 absorveu E4 (Lindström [71]). E3 é
o incentivo de métricas do lado da oferta (Petre [102], via resenha).

**O que as fontes dizem** (PDFs):
- **Brady et al. 2017 [67]**, p. 7313: "the expression of moral emotion is key for the spread
  of moral and political ideas in online social networks, a process we call 'moral
  contagion'". Cada palavra moral-emocional aumentou a difusão "by a factor of 20%", e o
  contágio "was bounded by group membership", ou seja, foi mais forte dentro das redes
  liberal e conservadora do que entre elas. É um processo de **difusão por compartilhamento
  humano**.
- **Rathje et al. [38]**, p. 1: "Out-group language consistently emerged as the strongest
  predictor of shares and retweets: the average effect size of out-group language was about
  4.8 times as strong as that of negative affect language and about 6.7 times as strong as
  that of moral-emotional language". Também é engajamento **humano** (compartilhamento), e
  não um efeito do algoritmo.
- **Brady et al. 2021 [13]**, p. 1: "positive social feedback for outrage expressions
  increases the likelihood of future outrage expressions, consistent with principles of
  reinforcement learning", e "users conform their outrage expressions to the expressive
  norms of their social networks". É **aprendizagem de quem escreve**.
- **Milli et al. [14]** (abstract): o algoritmo amplifica esse conteúdo "relative to a
  reverse-chronological baseline". É o **multiplicador algorítmico**.

**Leitura**: os quatro itens descrevem um ciclo, e cada um corresponde a um ator diferente.
É o segundo fechamento do loop que a 5.2 já descreve (E1 → AF1).

| Ator | Item | Processo |
|---|---|---|
| Quem compartilha | **C5** | O conteúdo moral-emocional e hostil ao out-group se espalha mais por compartilhamento, sobretudo dentro do grupo (Brady [67], Rathje [38]) |
| O algoritmo | **A1** | A otimização por engajamento aprende essa preferência e amplifica esse conteúdo além do que o feed cronológico mostraria (Milli [14]) |
| Quem escreve | **E1** | O feedback positivo e as normas da rede ensinam o usuário a expressar mais indignação (Brady [13], Lindström [71]) |
| Quem produz conteúdo profissional | **E3** | Veículos, jornalistas e criadores ajustam o que publicam às métricas de engajamento (Petre [102]) |

**Problemas no C5**:
1. **Nome composto (R5, O06)**: "negativity bias" e "moral-emotional contagion" são dois
   construtos. Nenhuma fonte da lista define *negativity bias*, e Rathje [38] mostra que o
   afeto negativo pesa bem menos que a linguagem sobre o out-group.
2. **Fonte mal distribuída**: Rathje [38] descreve o que **os usuários** compartilham, que é o
   processo de C5, mas o paper o cita em A1.
3. **Bloco**: contágio é difusão, e não viés cognitivo individual (T02.1-F05). Decisão na 2.5.

**Fronteiras a cuidar**:
- **C5 × A1**: C5 é a preferência humana de compartilhamento. A1 é o algoritmo que aprende e
  multiplica essa preferência. Milli [14] separa os dois com a linha de base cronológica.
- **E1 × F4**: Brady [13] mostra que a aprendizagem também é de **normas**, como em F4. A
  diferença é o conteúdo e o resultado: E1 é a expressão de indignação moral recompensada; F4
  é a difusão da incivilidade (tom) na conversa.
- **E1 × E3**: E1 é o usuário comum aprendendo por feedback social. E3 é o produtor
  profissional respondendo a métricas com consequência econômica.

**Recomendação**:
- **Manter os quatro**, com as fronteiras por ator nas definições (T02.3). Contagem 0.
- **Reformular C5** como um construto só: *moral contagion* (termo de Brady [67], R1).
  "Negativity bias" sai do nome. A definição pode mencioná-lo como base atencional, sem
  tratá-lo como mecanismo.
- **Rathje [38] passa a ser citado em C5**, e A1 fica com Milli [14] como evidência própria do
  efeito algorítmico. Rathje pode continuar em A1, mas como insumo: é o que o algoritmo
  aprende a amplificar.

**Status**: aguardando aprovação.

**D31 (2026-10-12) — cluster (d)**: **manter C5, E1, A1 e E3**, com as fronteiras por ator
(quem compartilha, o algoritmo, quem escreve, o produtor profissional) explícitas nas
definições: C5 × A1 (preferência humana × multiplicador algorítmico, separados pela linha de
base cronológica de Milli [14]); E1 × F4 (indignação moral recompensada × tom incivil da
conversa); E1 × E3 (usuário comum por feedback social × produtor profissional por métricas
com consequência econômica). **C5 reformulado como *moral contagion*** (Brady [67], R1);
"negativity bias" sai do nome e pode aparecer na definição como base atencional. **Rathje
[38] passa para C5**; em A1, fica só como o insumo que o algoritmo aprende a amplificar.
Bloco de C5 decidido na 2.5. Contagem: 38.

#### Cluster (e) — A2 Algorithmic radicalization × G3 Radicalization pipeline

**Fato no paper**: A2 é o "deslocamento gradual para conteúdo mais extremo via recomendações
sucessivas" (alternativo: *rabbit hole*), com Ribeiro et al. [56] e Hosseinmardi et al.
[57]. G3 descreve "trajetórias individuais graduais para o extremismo em comunidades online
fechadas" (alternativo: *fringe community pathway*), com Munn 2019 [76], no bloco G
(ecossistema). Os dois têm outcome Ideological.

**O que as fontes dizem** (PDFs):
- **Ribeiro et al. [56]**, abstract: auditam a hipótese de um "**radicalization pipeline** on
  YouTube", segundo a qual "users systematically progress towards more extreme content".
  Pelos comentários, encontram que "users consistently migrate from milder to more extreme
  content". Sobre o algoritmo, o achado é limitado: "Alt-lite content is easily reachable
  from I.D.W. channels, while Alt-right videos are reachable only through channel
  recommendations".
- **Hosseinmardi et al. [57]** (o PDF na pasta é a versão arXiv v2, de 2022), p. 1: testam a
  hipótese de que usuários "are being radicalized via a combination of biased
  recommendations and ostensibly apolitical 'anti-woke' channels". Encontram que o consumo
  é "dominated by mainstream and largely centrist sources" e que os consumidores de extrema
  direita são "a small and stable percentage". É evidência **contra** o papel central do
  algoritmo.
- **Munn [76]**, p. 1: "Alt-righters are not instantly converted, but rather incrementally
  nudged along a particular medial pathway". O artigo descreve "three overlapping cognitive
  phases that occur within this journey: **normalization, acclimation, and
  dehumanization**". O processo é de **socialização** num ambiente midiático (vídeos,
  chats, comunidades), não só de recomendação.

**Leitura**: como em M1 (D27), há um fenômeno (a trajetória gradual para o extremismo) com
duas vias distintas. O paper já separa as vias, mas com nomes e fontes cruzados:

| Via | Item | Processo | Fontes | Problema |
|---|---|---|---|---|
| Algoritmo | **A2** | Recomendações sucessivas deslocam o usuário para conteúdo mais extremo (*rabbit hole*) | Ribeiro [56] (parcial), Hosseinmardi [57] (contrária) | Evidência fraca ou contrária. O rating "Mixed" está correto, mas o texto precisa dizê-lo |
| Comunidade | **G3** | Socialização em comunidades e ambientes marginais: normalização → aclimatação → desumanização | Munn [76] | O nome "radicalization pipeline" é o termo-guarda-chuva de Ribeiro para a hipótese inteira (as duas vias). O bloco G (macro) não combina com um processo individual |

**Opções**:
- **(a) Manter os dois, separados pela via**: A2 = via algorítmica (nome: *algorithmic
  rabbit hole*, a conferir pela R2); G3 = via comunitária, renomeado pelo processo de Munn
  [76] (socialização gradual em comunidades extremistas, com as três fases). "Radicalization
  pipeline" passa a ser o guarda-chuva citado nas duas definições. G3 sai do bloco G (2.5;
  candidato: bloco B, dinâmica de grupo, que é onde AF11, *group/community formation*, já
  o liga). Contagem 0.
- **(b) Fundir** num único "radicalization pipeline" com as duas vias. Contagem −1. Vai na
  direção oposta à D27, que separou as vias de M1.
- **(c) Manter como está**. Os nomes cruzados continuam.

**Recomendação**: **(a)**, coerente com a D27. Na definição de A2, deixar explícito que
a evidência é mista (Ribeiro [56] × Hosseinmardi [57]). Na de G3, a fase de desumanização
liga G3 também ao outcome **affective** (hoje só Ideological).

**Status**: aguardando aprovação.

**D32 (2026-10-12) — cluster (e)**: **opção (a)**. A2 = via algorítmica (nome a conferir
pela R2, candidato *algorithmic rabbit hole*), com a evidência mista explícita (Ribeiro [56]
× Hosseinmardi [57]). G3 = via comunitária, renomeado pelo processo de Munn [76]
(normalização → aclimatação → desumanização), com outcome affective acrescentado. "Radicalization
pipeline" vira o guarda-chuva citado nas duas definições. G3 sai do bloco G (decisão na 2.5;
candidato: bloco B). Contagem: 38.

#### Cluster (f) — Percepção de normas: M7, D1, D2, D3, D4, B3, M5

**Situação após D14, D15 e D17**: B3 absorveu M4 (difusão de desinformação). M5 virou o
consenso fabricado. D2 virou o efeito das metapercepções exageradas.

**O que as fontes dizem** (PDFs, salvo indicação):
- **Noelle-Neumann [24]**, p. 45: a disposição de se expor depende do "individual's fear of
  isolation and of his self-confidence being shaken if his own view is not confirmed by the
  majority opinion or by the trend of opinion". O texto não usa o termo *pluralistic
  ignorance*.
- **Ross et al. [39]**, p. 279: "social observers tend to perceive a 'false consensus' with
  respect to the relative commonness of their own responses". É superestimar o quanto **a
  própria** posição é comum.
- **Prentice e Miller [40]** (sem PDF; D-sem-PDF, conhecimento do agente; conferir):
  *pluralistic ignorance* é quando a maioria rejeita uma norma em privado, mas acredita que
  os outros a aceitam. É **o oposto** do falso consenso: subestimar o quanto a própria
  posição é comum.
- **Muchnik et al. [41]**, p. 647 (abstract): os termos dos autores são "**social influence
  bias**" e "**herding**". Uma avaliação positiva prévia "increased the likelihood of
  positive ratings by 32% and created accumulating positive herding that increased final
  ratings by 25% on average". "Social proof", o nome de D4, não aparece. É o termo de
  Cialdini, que não está na lista.
- **Bor e Petersen [68]**, abstract: as discussões online "feel more hostile, in part,
  because the behavior of such individuals [status-driven] is more visible than offline".
- **Elmas et al. [54]**, p. 1: atores coordenados fazem um tema "appear popular".

**Leitura**: os sete itens se organizam numa cadeia (sinais → leitura dos sinais → percepção
da distribuição de opiniões → resposta). Só um deles junta dois construtos opostos:

| Etapa | Item | Processo | Observação |
|---|---|---|---|
| Fabricação dos sinais | **M5** | Atores coordenados fabricam sinais de popularidade | Fronteira: M5 produz os sinais; D4, D3 e A5 são os processos que esses sinais acionam |
| Leitura individual dos sinais | **D4** | A aprovação visível dos outros muda a avaliação do conteúdo (*social influence bias*, *herding*) | Nome a conferir pela R1, porque a fonte usa outros termos |
| Difusão em rede | **B3** | Cada compartilhamento segue os anteriores, e a cascata espalha o conteúdo, inclusive o falso | Fronteira com D4: D4 é a decisão individual; B3 é a dinâmica da rede. *Herding* sai de B3 e vai para D4 |
| Quem fica visível | **D1** | Uma minoria extrema e mais ativa domina o que se vê, e o observador generaliza a partir dessa amostra | — |
| Percepção da distribuição | **D3** | **Dois construtos opostos**: falso consenso (superestimar a própria posição) e ignorância pluralística (subestimar a própria posição) | **Problema (R5, O06)** |
| Resposta: silêncio | **M7** | Medo do isolamento → quem se vê como minoria se cala → o clima de opinião se distorce mais | A 5.2 já liga a ignorância pluralística ao silêncio ("the pluralistic ignorance that keeps dissenters silent") |
| Resposta: hostilidade | **D2** | Metapercepções exageradas (achar que o outro grupo nos odeia mais do que odeia) → hostilidade recíproca | — |

**Opções para D3**:
- **(a) Dividir** em D3a (falso consenso) e D3b (ignorância pluralística). Contagem +1 (38 →
  39).
- **(b) Manter junto** sob o nome "misperceived norms" (o alternativo atual), com os dois como
  direções opostas do mesmo erro. Contagem 0. Fica um item guarda-chuva, contra a R5.
- **(c) D3 fica só com o falso consenso** (Ross [39]), e **a ignorância pluralística entra na
  definição de M7** como o estado de percepção que a espiral produz e do qual se alimenta.
  É a ligação que a própria 5.2 já faz. Prentice e Miller [40] passa a ser citado em M7.
  Contagem 0. Ajuste correspondente no terceiro fechamento do loop (5.2), que hoje cita D3
  com os dois construtos.

**Recomendação**: **(c)**. Resolve o nome composto sem aumentar a contagem e alinha a
taxonomia com o que a 5.2 já diz. Se preferir manter a ignorância pluralística como item
próprio, a alternativa é **(a)**.

**Os outros seis**: **manter**, com as fronteiras da tabela nas definições (T02.3). Mudanças
de nome: D4 (conferir *social influence bias* × *social proof*) e o alternativo *herding*,
que sai de B3 e vai para D4. M7 ainda está no bloco M (2.5; candidato: bloco D).

**Status**: aguardando aprovação.

**D33 (2026-10-12) — cluster (f)**: **D3, opção (a)**: dividir em **D3a, falso consenso**
(superestimar o quanto a própria posição é comum; Ross [39]) e **D3b, ignorância
pluralística** (a maioria rejeita a norma em privado, mas acredita que os outros a aceitam;
Prentice e Miller [40], D-sem-PDF). Fronteira D3b × M7, explícita nas definições: D3b é o
erro de percepção da norma; M7 é o silêncio por medo do isolamento, que alimenta esse erro
(5.2). O terceiro fechamento do loop (5.2) passa a citar D3a e D3b. **Os outros seis (M5,
D4, B3, D1, M7, D2) ficam**, com as fronteiras da tabela. Na T02.3: conferir o nome de D4
(*social influence bias* × *social proof*) e levar *herding* de B3 para D4. Contagem:
**38 → 39**.

#### Cluster (g) — Exposição × evitação: M1a (câmara de eco), M2 (busca seletiva), H1 News avoidance, H2 Selective/partisan news avoidance

**Fato no paper**: H1, "News avoidance" (alternativo: news fatigue): "Toff and Kalogeropoulos
[79] documentam como a prática de consumo de notícias privilegia o que já se alinha a crenças
prévias, inclusive por meio da evitação completa". H2, "Selective/partisan news avoidance"
(alternativo: checked-out citizens): "Skovsgaard and Andersen [80] conceituam formalmente a
evitação seletiva, distinta da evitação geral, com assimetria partidária documentada por Toff
and Kalogeropoulos [79]". A abertura do bloco H o apresenta como "o espelho dos mecanismos de
exposição seletiva do Bloco M", e justifica o bloco próprio "em vez de subsumi-los sob
Confirmation bias / myside bias (M2)".

**O que as fontes dizem**:
- **Toff e Kalogeropoulos [79]** (PDF depositado em 2026-10-12):
  - o título publicado é "All the News That's Fit to Ignore: How the Information Environment
    Does and Does Not Shape News Avoidance" (p. 366), e não o subtítulo da lista do paper;
  - o estudo mede a **evitação geral** de notícias em 35 países e encontra que "levels of press
    freedom and political freedom and stability are shown to negatively predict rates of news
    avoidance" (abstract, p. 366);
  - a ideologia tem efeito pequeno: "right-leaning individuals somewhat less likely to avoid
    news than those on the left", com d = −0,09, menor que o da eficácia política interna
    (p. 379). Não há "assimetria partidária" de evitação **seletiva**;
  - a exposição seletiva partidária aparece só como literatura de fundo (Stroud; Garrett e
    Stroud), e o artigo observa que, na mídia social, "the effect of partisan selective
    exposure may be reduced" (p. 369).
- **Skovsgaard e Andersen [80]** (abstract, D-sem-PDF): o modelo distingue "two types of news
  avoidance, intentional and unintentional, depending on the underlying causes". É uma
  conceituação da evitação **em geral**, não da evitação seletiva ou partidária (O10).
- **Taber e Lodge [64]**, p. 755: o viés de confirmação é "the seeking out of confirmatory
  evidence when Ps are free to self-select the source". Buscar o que confirma e evitar o que
  contraria são os dois lados da mesma escolha de fontes.

**Leitura**:
- **H2** descreve evitar fontes contrárias à própria posição. É o outro lado da escolha
  seletiva de fontes, que a D26 deixou em M2 (busca seletiva). As duas fontes de H2 não
  sustentam o que o texto atribui a elas (F04, F05 abaixo).
- **H1** descreve a evitação geral de notícias. Essa é a conceituação que Skovsgaard e
  Andersen [80] de fato fazem (intencional × não intencional), e é o que Toff e
  Kalogeropoulos [79] de fato estudam. As fontes de H1 e H2 estão trocadas. O caminho de H1
  até a polarização não está nas fontes: a hipótese plausível é que, quando os menos
  interessados se afastam, o público que continua atento é mais partidário e mais visível
  (liga H1 a D1) [conhecimento do agente; a literatura de referência não está na lista].
- **M1a** (câmara de eco) não se sobrepõe a H1 nem a H2: é reforço pela rede, não escolha
  individual de fontes.

**Opções**:
- **H2**:
  (a) **fundir em M2**, que passa a cobrir a escolha seletiva de fontes nos dois sentidos
  (buscar o que confirma, evitar o que contraria). Fontes: Taber e Lodge [64] e Nickerson
  [48]. Contagem −1. Resolve a falta de fonte de H2 sem procurar referência nova;
  (b) manter H2 e buscar uma fonte que defina a evitação seletiva partidária (referência nova,
  pela D2; há literatura sobre o tema, mas fora da lista [conhecimento do agente]).
  Contagem 0.
- **H1**:
  (a) **manter, reancorado**: Skovsgaard e Andersen [80] definem (intencional × não
  intencional), Toff e Kalogeropoulos [79] trazem os preditores, e o caminho até a
  polarização é declarado como plausível, com evidência "Plausible" (já é o rating da
  tabela). Contagem 0;
  (b) excluir, porque nenhuma fonte da lista liga a evitação geral à polarização. Contagem −1.

**Recomendação**: **H2 (a)** e **H1 (a)**. Contagem final: **39 → 38**. O bloco H fica só com
H1, o que pesa na 2.5 (o bloco tende a se dissolver).

#### Achados

##### T02.2-F04 — Toff e Kalogeropoulos [79]: subtítulo errado na lista e conteúdo atribuído que a obra não sustenta · **Importante** · confirma O09
- **Localização**: lista de referências, item 79; Seção 6.10, H1 e H2.
- **Fato**: a lista traz "How the Practice of News Use Privileges News That Fits Our Current
  Beliefs". O título publicado é "How the Information Environment Does and Does Not Shape
  News Avoidance" (p. 366). O paper atribui à obra (i) que o consumo "privilegia o que já se
  alinha a crenças prévias" (H1) e (ii) uma "assimetria partidária" da evitação seletiva
  (H2). A obra estuda a evitação **geral**, encontra efeito pequeno da ideologia (d = −0,09,
  p. 379) e trata a exposição seletiva partidária só como literatura de fundo, que pode estar
  **reduzida** na mídia social (p. 369).
- **Julgamento**: o subtítulo errado parece ter gerado a própria afirmação de H1. As duas
  atribuições precisam sair. O G1 vale para corrigir o item da lista: dados via Crossref (DOI
  10.1093/poq/nfaa016). Fica registrado também para a tarefa de verificação de referências.

##### T02.2-F05 — Skovsgaard e Andersen [80] conceituam outra distinção · **Importante** · confirma O10
- **Localização**: Seção 6.10, H2.
- **Fato**: o paper diz que [80] "conceituam formalmente a evitação seletiva, distinta da
  evitação geral". O abstract de [80] distingue evitação **intencional e não intencional**,
  sem recorte seletivo nem partidário.
- **Julgamento**: [80] é a fonte certa para definir **H1** (evitação geral), não H2. A ressalva
  é que a conferência foi feita só pelo abstract (D-sem-PDF).

**Status**: aguardando aprovação.

#### Cluster (g), complemento: busca sobre evitação seletiva partidária (2026-10-12)

**Pedido do usuário**: buscar referências novas para avaliar se vale manter H2.
Busca exploratória no OpenAlex, registrada no tema `areas/mestrado/smip-paper/exposicao-seletiva/`
(22 candidatos em `deliverables/candidates.md`, **aguardando aprovação por item**). Tudo abaixo
vem **só dos abstracts** [abstract], até os PDFs chegarem.

**O que a literatura indica**:
- **A evitação é um fenômeno distinto da aproximação.** Garrett e Stroud 2014 (candidato 3):
  "attraction to proattitudinal information and aversion to counterattitudinal information are
  distinct phenomena". Song 2016 (7) usa a mesma distinção ("selective approach" ×
  "selective avoidance"). Heseltine et al. 2025 (6) medem a "partisan temporal selective
  avoidance" em 27 milhões de visitas a sites de notícias.
- **Há assimetria partidária, com fonte.** Garrett e Stroud 2014 (3): "Republicans are
  significantly more likely to engage in selective avoidance of predominantly
  counterattitudinal information". É a afirmação que o paper atribuía, sem respaldo, a Toff e
  Kalogeropoulos [79] (T02.2-F04).
- **A evidência é mista.** Garrett 2009 (1): as pessoas preferem o reforço "without
  systematically avoiding opinion challenges". Chaffee et al. 2001 (8) vão na mesma linha.
- **Na mídia social, a evitação vira desconexão**, e é aí que a plataforma pesa: unfriending,
  unfollowing e remoção de conteúdo (Bode 2016, 10; Škorić et al. 2021, 4; Zhu e Škorić 2021,
  12 e 13; Goyanes et al. 2021, 15). Bode (10) mostra que o unfriending político é raro
  ("fewer than 10%") e se concentra nos mais ideológicos. Zhu e Škorić (13) tratam o
  unfriending como "selective avoidance through tie dissolution", ligado ao colapso de
  contexto.
- **Consequência estrutural**: Sasahara et al. 2020 (14), em modelo, mostram que influência
  social mais unfollowing "accelerate the emergence of echo chambers", o que liga H2 a M1a.
- **H1**: Urman 2019 (22) encontra "a politically apathetic majority and news-interested
  minority", e os assinantes de notícias "are polarized along political lines". Isso dá
  base ao caminho de H1 até a polarização, que estava sem fonte.

**Opções revistas para H2**:
- **(a) Manter H2, reformulado como evitação seletiva**, com fontes novas (D2). Definição:
  evitar conteúdo, fontes e contatos contrários à própria posição, o que nas plataformas
  inclui a dissolução de laços (unfriending, unfollowing). Fronteiras: M2 é a aproximação ao
  que confirma (fenômeno distinto, Garrett e Stroud); B1 é a formação de laços entre
  semelhantes, e H2 é o corte reativo de laços depois da discordância; M1a é o resultado em
  rede (Sasahara). A affordance AF3 (seguir e desfazer sem reciprocidade) já alimenta essa
  via. Evidência "Mixed" (Garrett 2009 × Garrett e Stroud 2014). Contagem 0.
- **(b) Fundir H2 em M2** (recomendação anterior). Perde a distinção que a literatura faz
  entre aproximação e evitação, e a via de desconexão, que é a mais específica da mídia
  social.

**Recomendação revista**: **(a)**. A literatura trata a evitação seletiva como fenômeno
próprio, documenta a assimetria partidária e mostra uma forma típica das plataformas
(dissolução de laços). A decisão final depende da leitura dos candidatos 1, 3, 4, 6, 10 e
13. **H1**: manter, reancorado (Skovsgaard e Andersen [80] para a definição, Toff e
Kalogeropoulos [79] para os preditores, Urman 2019 para o caminho até a polarização).

**Status**: aguardando decisão sobre H2 e H1 (e aprovação dos candidatos).

**D34 (2026-10-12) — cluster (g)**: **H2, opção (a)**. Manter H2, reformulado como
**evitação seletiva**: evitar conteúdo, fontes e contatos contrários à própria posição, o que
nas plataformas inclui a dissolução de laços (unfriending, unfollowing). Fronteiras nas
definições: M2 = aproximação ao que confirma; B1 = formação de laços entre semelhantes (H2 é
o corte reativo depois da discordância); M1a = resultado em rede. Saem de H2 as atribuições
a Toff e Kalogeropoulos [79] e a Skovsgaard e Andersen [80] (T02.2-F04, F05). Fontes novas
(D2), via tema `areas/mestrado/smip-paper/exposicao-seletiva/`. Contagem: 39.

**Leitura dos PDFs obtidos (candidatos 1 e 6 do tema)**:
- **Garrett 2009** (*J. Commun.* 59, 676–699): "people exhibit a preference for
  opinion-reinforcing political information without systematically avoiding opinion
  challenges", o que contradiz "the common assumption that reinforcement seeking and
  challenge avoidance are intrinsically linked aspects of the selective exposure phenomenon"
  (p. 676). O artigo **sustenta a distinção** entre aproximação (M2) e evitação (H2) e é a
  principal **evidência contrária** à prevalência da evitação. Também afirma que a evitação,
  quando ocorre, é "significantly more harmful to democratic deliberation" (p. 676).
- **Heseltine et al. 2025** (*AJPS* 69, 1541–1558): com 27,6 milhões de visitas, encontram
  "support for partisan temporal selective news avoidance" e assimetria partidária no nível
  macro (p. 1541). Quando a cobertura do próprio partido fica negativa, republicanos migram
  para veículos alinhados, e democratas ajustam quanto consomem (pp. 1550–1551, 1554). O
  efeito sobre a polarização é **proposto, não testado**: "likely one of the contributing
  factors of attitudinal, affective, or perceived polarization" (p. 1556).
- **Consequência para H2**: a existência e a assimetria partidária têm fonte. O elo com a
  polarização é teórico nas duas leituras. Rating sugerido: **"Mixed"** (Garrett × Heseltine).
  Os candidatos 3, 4, 10 e 13 (Garrett e Stroud; unfriending) seguem pendentes e reforçariam
  a via da desconexão, que é a mais específica da mídia social.
- **H1**: mantido, reancorado (Skovsgaard e Andersen [80], Toff e Kalogeropoulos [79], Urman
  2019), conforme a recomendação. Aguarda confirmação explícita do usuário.

**Nota sobre E3 (D18)**: o usuário obteve uma segunda resenha de Petre [102] (Hua 2023,
*Qualitative Sociology Review* 19(2), 118–121). Segundo ela, o livro trata do controle
gerencial do trabalho jornalístico por métricas (Chartbeat), sem tratar de polarização. A
ligação entre métricas e conteúdo "vitriolic" aparece só na resenha de Holton (p. 315). A
base de E3 reformulado continua fraca: evidência "Plausible", e talvez seja preciso uma fonte
que ligue métricas de engajamento ao conteúdo polarizador (D2). Decidir na ficha de E3
(T02.3, bloco E).

**Subtarefa 2.3 concluída (2026-10-13)**: D26–D34. H1 mantido e reancorado (recomendação
aceita pelo usuário ao seguir para a 2.4). Contagem: **39**.

### 14.4 Subtarefa 2.4 — Nomes compostos (2026-10-13)

Régua: **R5** (um nome, um construto; "&" e "/" só entre sinônimos estritos). Dos nove
nomes de O06, já resolvidos: M1 (dividido, D27), C5 (*moral contagion*, D31), D3 (dividido,
D33), E4 (fundido em E1, D23), H2 (evitação seletiva, D34). Restam M2, B5, D1 e G4, e
acrescento G1, que também usa "/". O nome final de cada um sai na T02.3, pela R1 e pela R2
(contagem no OpenAlex). Aqui se decide **se o item tem um ou dois construtos** e **qual
termo é o principal**.

| Item | Nome atual | Diagnóstico | Proposta |
|---|---|---|---|
| **M2** | Confirmation bias / myside bias | Um construto. "Myside bias" é um termo vizinho, não usado por Nickerson [48] | Nome principal: **confirmation bias**. *Myside bias* vai para os alternativos se a R2 confirmar o uso como sinônimo (pedido da H02) |
| **B5** | Interpersonal political tension & identity salience activation | **Um** processo em duas etapas. Tanyel e Windeler [5] (abstract): "the mechanisms that link social media use to polarization: interpersonal political tension and political identity salience". No texto, a tensão "heightens the salience of a person's political identity" (Study 1). É uma cadeia, não dois mecanismos paralelos | Nome principal pela etapa inicial: **interpersonal political tension**. A ativação da saliência identitária entra na definição como o passo seguinte (resolve parte da H07) |
| **D1** | Vocal minority / extremity bias | O "/" junta um **grupo** (a minoria ruidosa) e um **viés de percepção**. A fonte, Bor e Petersen [68], não usa nenhum dos dois termos. Fala na "perception hypothesis" e mostra que a hostilidade online "is more visible" por causa da natureza pública das plataformas | Um construto: a **sobrerrepresentação** dos poucos usuários mais ativos e extremos no que fica visível, e a generalização que o observador faz a partir dela. Nome principal: **vocal minority** (a conferir pela R2). "Extremity bias" e "sampling bias" saem, salvo se a R2 mostrar uso como sinônimo |
| **G4** | Deplatforming & migration | Dois elementos de naturezas diferentes. *Deplatforming* é uma ação de governança: está na Tabela 6 como **intervenção** de AF10. A migração é o processo. Horta Ribeiro et al. [77] (abstract): comunidades que sofrem "moderation measures, such as bans, […] may migrate to other platforms with laxer policies" | Nome principal: **platform migration** (o termo do título de [77]). O banimento entra na definição como gatilho |
| **G1** | Disintermediation / gatekeeping decline | Quase sinônimos: os dois nomeiam o enfraquecimento do filtro editorial. Bennett e Livingston [74] usam outro termo, "disinformation order", que nomeia a **ordem resultante** (estado), e descrevem um "amplifier effect" para histórias "that would be dismissed as absurd in earlier eras of more effective press gatekeeping" (p. 124). O alternativo "epistemic fragmentation" é um outcome (R6) | Nome principal: **gatekeeping decline**, com *disintermediation* como alternativo. Sai "epistemic fragmentation". Fonte definidora candidata já na lista: Barzilai-Nahon [17], *Toward a Theory of Network Gatekeeping* (sem PDF) |

**Notas sobre as versões dos PDFs** (para `reference-coverage.md`): o arquivo de Bor e
Petersen [68] é o manuscrito aceito (post-print), e o de Horta Ribeiro et al. [77] é a
versão arXiv v3. Os dois têm conteúdo equivalente ao publicado. A paginação citada é a
do arquivo.

**Contagem**: 39, sem mudança. A 2.4 só mexe em nomes.

**Status**: aguardando aprovação item a item.

**D35 (2026-10-13) — subtarefa 2.4**: **todas as propostas aprovadas**. Nomes principais
(definitivos na T02.3, pela R1 e pela R2): M2 = *confirmation bias* (*myside bias* como
alternativo se a R2 confirmar); B5 = *interpersonal political tension* (a saliência
identitária entra como passo seguinte na definição); D1 = *vocal minority* (saem *extremity
bias* e *sampling bias*, salvo se a R2 indicar uso como sinônimo); G4 = *platform migration*
(o banimento entra como gatilho); G1 = *gatekeeping decline* (*disintermediation* como
alternativo; sai *epistemic fragmentation*; Barzilai-Nahon [17] como fonte definidora
candidata). **Subtarefa 2.4 concluída.** Contagem: 39.

### 14.5 Subtarefa 2.5 — Critério e composição dos blocos (2026-10-13)

**Ponto de partida**: T02.1-F05. Os nove blocos usam quatro bases de divisão (insumo,
natureza do processo, outcome, resíduo), e sete membros contradiziam a abertura do próprio
bloco. As decisões da 2.1–2.4 tiraram itens de lugar (M1a, M1b, G3, C5, M3, H2) e deixaram o
bloco M com itens heterogêneos e o bloco H com dois itens.

**Os 39 mecanismos atuais** (IDs estáveis até a T02.5, D3):
M1a câmara de eco · M1b bolha de filtro · M2 viés de confirmação (busca) · M3 exposição à
incivilidade · M5 consenso fabricado · M6 reinforcing spiral (B02) · M7 espiral do silêncio ·
A1 amplificação algorítmica de conteúdo hostil · A2 *rabbit hole* algorítmico · A5 agenda
algorítmica · B1 homofilia (com A3) · B2 polarização de grupo · B3 cascatas (com M4) · B4
*partisan sorting* · B5 tensão política interpessoal · C1 raciocínio motivado · C2 assimilação
enviesada · C3 efeito da mídia hostil · C4 efeito de verdade ilusória · C5 *moral contagion* ·
D1 minoria ruidosa · D2 metapercepções exageradas · D3a falso consenso · D3b ignorância
pluralística · D4 influência social na avaliação · E1 aprendizagem social da indignação (com
E4) · E2 sinalização identitária · E3 incentivo de métricas na oferta · F1 desinibição · F2
*firestorm*/*dogpiling* · F3 comunicação breve · F4 contágio da incivilidade · G1 declínio do
gatekeeping · G2 *propaganda feedback loop* · G3 radicalização comunitária · G4 migração de
plataforma · G5 censura percebida · H1 evitação de notícias · H2 evitação seletiva.

#### D6 — Base dos blocos

- **(a) Base única: o locus do processo** (onde ele acontece). Sete blocos. Os blocos M
  (resíduo) e H (dois itens) se dissolvem. **Recomendado.**
- **(b) Manter os nove blocos**, reescrevendo as aberturas para declarar que as bases são
  mistas. Mais barato, mas um revisor de taxonomia tende a apontar a falta de um princípio
  único de divisão e as sobreposições entre M e os outros blocos.

#### Composição proposta com (a)

| Bloco (locus) | Critério em uma frase | Membros | Origem das mudanças |
|---|---|---|---|
| **A — Curadoria algorítmica** | O sistema decide o que é exibido ou recomendado | A1, A2, A5, **M1b** | M1b vem de M (D27). A3 e A4 saíram (D21, D22) |
| **B — Rede, grupo e difusão** | O processo depende de quem está ligado a quem, das identidades de grupo ou da difusão entre usuários | B1, B2, B3, B4, B5, **M1a**, **G3**, **C5** | M1a (D27), G3 (D32: socialização em comunidades), C5 (D31: difusão por compartilhamento, "bounded by group membership") |
| **C — Seleção e processamento individual da informação** | O processo acontece na escolha ou no julgamento do indivíduo diante da informação | C1, C2, C3, C4, **M2**, **H1**, **H2**, **M6** (provisório) | M2 (D26), H1 e H2 (D34; o bloco H se dissolve). M6 fica aqui até a revisão do B02: o modelo de Slater é individual (identidade ↔ consumo de mídia) |
| **D — Percepção dos outros** | O processo muda o que se acredita que os outros pensam, sentem ou fazem | D1, D2, D3a, D3b, D4, **M7** | M7 (D33: o silêncio alimenta a ignorância pluralística) |
| **E — Incentivos** | O processo é movido por recompensa social ou econômica | E1, E2, E3 | E4 saiu (D23) |
| **F — Interação** | O processo acontece na troca direta entre usuários | F1, F2, F3, F4, **M3** | M3 (D28: recepção da incivilidade) |
| **G — Ecossistema e oferta** | O processo envolve a oferta de informação ou a governança no nível do sistema de mídia | G1, G2, G4, G5, **M5** | M5 (D15: atores coordenados que fabricam sinais, lado da oferta). G3 saiu para B |

Totais: A 4 · B 8 · C 8 · D 6 · E 3 · F 5 · G 5 = **39**.

**Casos de fronteira** (a confirmar):
- **B4** (*partisan sorting*): alinhamento de identidades sociais, e não estrutura de laços.
  Cabe em B se o critério de B incluir **identidades de grupo**, como na tabela acima. A
  alternativa seria G (processo societal de longo prazo).
- **G5** (censura percebida): é uma percepção, mas sobre a **governança da plataforma**, não
  sobre os outros usuários. Por isso fica em G, junto de G1 e G4, que AF10 (*platform
  governance*) também alimenta.
- **M5**: o alvo é a percepção (D), mas o processo é de quem produz os sinais. Fica em G
  (oferta), coerente com a fronteira M5 × D4 da D33.
- **H2**: inclui a dissolução de laços, que mexe na rede (B). O processo, porém, é a escolha
  individual de evitar. A consequência em rede já é M1a.
- **M6**: provisório em C, até a decisão do B02.

**Efeitos colaterais**:
- **Aberturas dos blocos**: todas reescritas na T02.3, uma por lote. A abertura de C não pode
  mais dizer que seus mecanismos são "hospedados (não criados ou amplificados)", porque C4 é
  "Amplifies" (T02.1-F05).
- **Nomes dos blocos** em todo o paper: Seções 6.2–6.10, legenda da Figura 4 (rede bipartida
  affordance ↔ bloco), Figuras 5–15 (agrupam por bloco), 7.1 (listas "It feeds mechanisms in
  … blocks") e Tabela 6. Entra na T02.5.
- **IDs**: com M e H dissolvidos, a renumeração única da T02.5 (D3) passa a seguir os sete
  blocos (A1…G5).
- **Ordem dos lotes da T02.3** (D5: ordem do paper): passa a ser A → G.

**Status**: aguardando D6 e a aprovação da composição.

**D6 (2026-10-13) — subtarefa 2.5**: **(a), base única pelo locus do processo**, com a
composição da tabela acima aprovada, incluindo os casos de fronteira como propostos (B4 em B,
G5 e M5 em G, H2 em C, M6 provisório em C). Blocos M e H dissolvidos. Sete blocos: A
(curadoria algorítmica), B (rede, grupo e difusão), C (seleção e processamento individual da
informação), D (percepção dos outros), E (incentivos), F (interação), G (ecossistema e
oferta). **Subtarefa 2.5 concluída.** Contagem: 39.

### 14.6 Subtarefa 2.6 — Lista final e correspondência de IDs (2026-10-13)

**Regra de numeração (D36, a decidir)**:
- **(a) Ordem lógica dentro de cada bloco** (a cadeia do processo, como nas análises da
  2.3). Melhor para quem lê o paper pela primeira vez, que é o caso dos revisores.
  **Recomendada.**
- **(b) Mudança mínima**: quem fica no bloco mantém o ID, e os que chegam vão para o fim.
  Facilita para os autores comparar com a v1, mas deixa a ordem dos blocos sem lógica.

A tabela abaixo segue a (a). Os nomes são **provisórios**: os definitivos saem na T02.3
(R1, R2). Os novos IDs só entram no paper na T02.5 (D3).

| Novo | Nome provisório | ID na v1 | Decisões |
|---|---|---|---|
| **A — Curadoria algorítmica** | | | |
| A1 | Filter bubble | M1 (parte) | D27 |
| A2 | Algorithmic amplification of divisive content | A1 | D20 |
| A3 | Algorithmic rabbit hole | A2 | D32 |
| A4 | Algorithmic agenda-setting | A5 | — |
| **B — Rede, grupo e difusão** | | | |
| B1 | Homophily | B1 + A3 | D21 |
| B2 | Echo chamber | M1 (parte) | D27 |
| B3 | Group polarization | B2 | — |
| B4 | Information cascades | B3 + M4 | D14 |
| B5 | Moral contagion | C5 | D31 |
| B6 | Partisan sorting | B4 | D6 |
| B7 | Interpersonal political tension | B5 | D35 |
| B8 | Community radicalization pathway | G3 | D32 |
| **C — Seleção e processamento individual da informação** | | | |
| C1 | Motivated reasoning | C1 | D26 |
| C2 | Confirmation bias (busca seletiva) | M2 | D26, D35 |
| C3 | Selective avoidance | H2 | D34 |
| C4 | Biased assimilation | C2 | D26 |
| C5 | Hostile media effect | C3 | — |
| C6 | Illusory truth effect | C4 | — |
| C7 | News avoidance | H1 | D34 |
| C8 | Reinforcing spiral (provisório; B02) | M6 | D16 |
| **D — Percepção dos outros** | | | |
| D1 | Vocal minority | D1 | D35 |
| D2 | Social influence bias (nome a conferir) | D4 | D33 |
| D3 | False consensus | D3 (parte) | D33 |
| D4 | Pluralistic ignorance | D3 (parte) | D33 |
| D5 | Spiral of silence | M7 | D33 |
| D6 | Exaggerated meta-perceptions | D2 | D17 |
| **E — Incentivos** | | | |
| E1 | Social learning of outrage | E1 + E4 | D23 |
| E2 | Identity signaling | E2 | — |
| E3 | Metric-driven content production (nome a definir) | E3 | D18 |
| **F — Interação** | | | |
| F1 | Online disinhibition effect | F1 | D30 |
| F2 | Online firestorm / dogpiling (nome a conferir, H12) | F2 | D29 |
| F3 | Low-context communication (nome a conferir) | F3 | D24 |
| F4 | Incivility contagion | F4 | D28 |
| F5 | Incivility exposure effect | M3 | D13 |
| **G — Ecossistema e oferta** | | | |
| G1 | Gatekeeping decline | G1 | D35 |
| G2 | Propaganda feedback loop | G2 | D19 |
| G3 | Manufactured consensus | M5 | D15 |
| G4 | Platform migration | G4 | D35 |
| G5 | Perceived censorship | G5 | — |

**Total: 39** (A 4 · B 8 · C 8 · D 6 · E 3 · F 5 · G 5).

**IDs da v1 que deixam de existir**: M4 (→ B4), A3 (→ B1), A4 (excluído; efeitos em D5, B7,
F2 e F4), E4 (→ E1). **Saldo**: −4 (fusões e exclusão) e +2 (divisões de M1 e D3), de 41
para 39.

**Fechamentos do *feedback loop* (5.2, Figura 3) com os novos IDs**:
1. D5 (espiral do silêncio) → AF2 → reforça B1 (homofilia);
2. E1 (aprendizagem social da indignação) → AF1 → reforça B5 (*moral contagion*);
3. D3 e D4 (falso consenso e ignorância pluralística) → AF4 → reforçam D3.

**Itens com nome ainda em aberto** (resolver na T02.3): D2, E3, F2, F3, e a conferência pela R2
de todos os nomes provisórios.

**Status**: aguardando D36 e a aprovação da lista.

**D36 (2026-10-13) — subtarefa 2.6**: **(a), ordem lógica dentro de cada bloco**. Lista
final de **39 mecanismos** aprovada, conforme a tabela acima. Os novos IDs entram no paper na
T02.5. Até lá, o relatório e os ajustes usam os novos IDs com o ID da v1 entre parênteses
quando houver risco de confusão.

**Subtarefa 2.6 e T02.2 concluídas (2026-10-13).** Decisões da T02.2: D6, D10–D36. Achados:
T02.2-F01 a F05. Próximo passo: T02.3, fichas por bloco (A → G).
