# T05 — Mecanismos, rodada 2: nomes, alternativos e estatuto de 12 itens (plano)

- **Manuscrito**: smip-famo-framework
- **Versão revisada**: cópia de revisão em Google Docs, lida em 2026-10-20 (revisão `AHj4eMR3bP0J…`),
  com a lista de **43 mecanismos** em 7 blocos (A4 · B10 · C9 · D6 · E3 · F5 · G6) aplicada em
  2026-10-18
- **Data**: 2026-10-20
- **Status**: **plano, aguardando decisões** (Seção 6). Nenhum ajuste redigido.
- **Insumos**:
  - `adjustments/adjustments mecanismos/rascunho ajustes.txt` (comentários do usuário, conferidos
    no Google Scholar);
  - relatórios e ajustes da revisão anterior de mecanismos, que estão só no zip
    `adjustments/adjustments mecanismos.zip` (fora do Git): `T02-revisao-mecanismos.md`,
    `T03-novo-levantamento-mecanismos.md` e os dois `*-ajustes.md`. Aqui eles são citados como
    **Mec-T02** e **Mec-T03**, porque a numeração colide com a T02 e a T03 deste INDEX (ver D0).
- **Relatórios anteriores consultados**: Mec-T02 (régua 12.1 e 12.4, lista 14.6, decisões D13–D35),
  Mec-T03 (lista de 43, 9.1; ligações, 9.2), T04 deste repositório (texto inserido na ficha de G1).

## 1. Pedido do usuário

> Temos novos ajustes, ainda sobre os mecanismos, cujo rascunho está em `rascunho ajustes.txt`.
> Avalie o conteúdo desse txt e o contexto dado, proponha um plano de ajuste para cobrir o que é
> abordado no txt, seguindo o mesmo fluxo de estruturação dos outros ajustes já feitos.

O rascunho comenta 12 dos 43 mecanismos. Os números citados nele (#12, #16, #25, #36) seguem a ordem
sequencial da lista de 43 (B8 Moral contagion = #12, C2 Confirmation bias = #16, D2 Social proof =
#25, F4 Incivility contagion = #36).

## 2. Escopo

**Dentro**: os 12 itens do rascunho, com nome, alternativos, ficha (Seção 6), estatuto de mecanismo
e as linhas correspondentes na Tabela 6 (taxonomia), na Tabela A1 (Apêndice A), na matriz de
affordances e na tabela de atores (5.3), além da propagação dos nomes no texto.

**Fora**: os outros 31 mecanismos; as colunas *Platform role*, *Direction* e *Primary/Secondary
actor*, exceto onde o item muda; as figuras (manuais, com o usuário); a renumeração geral das
referências.

## 3. Régua (herdada da Mec-T02, sem mudança)

**Teste de mecanismo** (Mec-T02, 12.1): Q1 o nome designa um processo? · Q2 há cadeia insumo → passo →
mudança? · Q3 a mudança é um dos cinco outcomes, sem ser o próprio outcome? · Q4 não é *feature*,
*affordance*, contingência nem ator?

**Regra de nomenclatura** (Mec-T02, 12.4): R1 termo da fonte definidora · R2 entre termos correntes, o
mais recorrente (contagem no OpenAlex, título e resumo) · R3 o nome designa o processo, não o estado,
o conteúdo, o ator ou a estrutura · R4 não repete nome de *feature*, *affordance* ou *outcome* · R5 um
nome, um construto · R6 alternativos são sinônimos do mesmo processo; construto vizinho vai para a
definição · R7 inglês, sem aspas.

O rascunho usa o Google Scholar, que busca no texto completo. A R2 usa o OpenAlex, em título e
resumo. As duas medidas podem divergir, e a R2 é a regra adotada.

## 4. Contagens R2 (OpenAlex, título e resumo, 2026-10-20)

Na Mec-T02, as consultas do bloco G foram bloqueadas (HTTP 429) e ficaram pendentes. Foram feitas
agora, só com termos curtos.

| Item | Termo atual | Contagem | Termos candidatos |
|---|---|---|---|
| B4 | interpersonal political tension | 1 | — |
| B7 | negative social influence | 243 | repulsive influence 47 · anticonformity 100 |
| B10 | online community radicalization | 0 | online radicalization 366 · radicalization pathway 82 · radicalization pipeline 17 · alt-right pipeline 5 |
| E1 | social learning of outrage | 0 | moral outrage 1.862 · outrage expression 14 · online moral outrage 12 |
| E3 | metric-driven content | 2 | audience metrics (com news/journalism) 103 |
| F3 | message brevity | 8 | brevity effect 2 |
| F5 | incivility exposure effect | 0 | exposure to incivility 59 · nasty effect 12 |
| G1 | gatekeeping decline | 1 | decline of gatekeeping 4 · disintermediation 3.107 (237 com news, media ou journalism) |
| G2 | propaganda feedback loop | 12 | network propaganda 76 |
| G3 | manufactured consensus | 112 (o OpenAlex junta manufacturing) | astroturfing 850 · coordinated inauthentic behavior 116 · online astroturfing 16 · digital astroturfing 10 |
| G6 | partisan flagging | 2 | mass reporting 419 (sentidos variados) · report brigading 1 · flagging + polarization/partisan + platform/social media 77 |
| C7 | illusory truth effect | 218 (Mec-T02) | truth effect 449 (Mec-T02) |

## 5. Análise por item

Cada item traz o que o rascunho diz, o que foi conferido e o julgamento. Afirmações sobre obras sem
PDF neste repositório levam **[a verificar]** ou **[conhecimento do agente; conferir]**.

### T05-F01 — B4 Interpersonal political tension: nome correto, evidência superestimada na tabela · **Menor**
- **Rascunho**: pouco explorado, há um único par de estudos.
- **Conferido**: o termo é da própria fonte [5] (Tanyel e Windeler), o que satisfaz a R1, e R2 = 1. A
  ficha descreve dois surveys do mesmo grupo. A Tabela 6 dá **Evidence strength = Moderate**. Pela
  régua da 6.1, *moderate* exige "estudos observacionais consistentes entre si". A limitação da 9.3 já
  chama B4 de "the newest and least empirically verified hypothesis".
- **Julgamento**: o nome fica. A divergência está na força da evidência. **Proposta**: Evidence =
  Plausible (ou manter, se os autores tiverem outra base) e uma frase na ficha dizendo que o termo e o
  único teste vêm de [5].

### T05-F02 — B7 Negative social influence: construto nomeado, a crítica do rascunho não se confirma · **Menor**
- **Rascunho**: vago, não é construto distinto, provável sobreposição com Social proof (D2) ou Moral
  contagion (B8).
- **Conferido**: R2 = 243, mais repulsive influence 47 e anticonformity 100. O termo é corrente na
  literatura de dinâmica de opinião **[conhecimento do agente; conferir: Flache et al. 2017, JASSS]**.
  O processo é o afastamento da posição de quem é visto como distante ou do out-group. D2 é o
  alinhamento à aprovação visível, e B8 é a difusão de mensagens com emoção moral. A ficha já distingue
  B7 de C5 (backfire), mas não de D2 nem de B8. A evidência é só de modelos (Tabela 6: Plausible,
  Mixed).
- **Julgamento**: manter. A confusão do rascunho indica o que um leitor pode confundir. **Proposta**:
  uma frase de distinção com D2 e B8 na ficha. Opcional: fonte que define o termo (referência nova,
  D2 da Mec-T02).

### T05-F03 — B10 Online community radicalization: o nome atual não tem uso; "pipeline" já é o guarda-chuva · **Importante**
- **Rascunho**: radicalization pipeline é bem mais usado (e alt-right pipeline, termo de Munn, mais
  ainda, mas com viés à direita). Sugere trocar.
- **Conferido**: R2 = 0 para o nome atual. No OpenAlex, online radicalization 366 · radicalization
  pathway 82 · radicalization pipeline 17 · alt-right pipeline 5, o inverso do que o Scholar indicou
  para "pipeline". A fonte [76] é Munn 2019, "Alt-Right Pipeline". Pela decisão D32 da Mec-T02, o texto
  usa *radicalization pipeline* como **guarda-chuva** de A3 (via algorítmica) e B10 (via comunitária).
- **Julgamento**: dar a B10 o nome do guarda-chuva faria a parte e o todo terem o mesmo nome e
  colidiria com A3 (R5, R6). O nome atual também falha na R2.
- **Opções**: (a) **Community radicalization pathway** (alt. online radicalization; Munn [76]: alt-right
  pipeline), que era o nome provisório da Mec-T02 (14.6) · (b) Online radicalization (366), mas ele
  cobre também a via algorítmica · (c) Radicalization pipeline, como no rascunho, deslocando o
  guarda-chuva. **Recomendação: (a).**

### T05-F04 — C7 Illusory truth effect: atribuição imprecisa à fonte de 1977 · **Menor**
- **Rascunho**: não encontrou paper de Hasher, Goldstein e Toppino sobre o mecanismo.
- **Conferido**: [66] é Hasher, Goldstein e Toppino 1977, "Frequency and the Conference of
  Referential Validity" (J. Verbal Learn. Verbal Behav. 16, 107–112). É a demonstração original do
  efeito, mas o rótulo *illusory truth* (ou *truth effect*) veio depois **[conhecimento do agente;
  conferir]**. O PDF não está em `references/`. R2: illusory truth effect 218, truth effect 449 (mais
  genérico).
- **Julgamento**: o nome fica. A ficha deve dizer que Hasher et al. demonstraram o efeito e que o
  rótulo é posterior, citando uma fonte que define o termo **[conferir dados bibliográficos: Dechêne
  et al. 2010, meta-análise do truth effect; ou Fazio et al. 2015]**.

### T05-F05 — E1 Social learning of outrage: o nome parafraseia a fonte; "online moral outrage" nomeia o fenômeno · **Menor**
- **Rascunho**: termo não encontrado. Sugere online moral outrage, "definido por Brady et al. (2021)".
- **Conferido**: R2 = 0 para o nome atual; online moral outrage 12; moral outrage 1.862 (a emoção).
  A fonte [13] **é** Brady et al. 2021, "How Social Learning Amplifies Moral Outrage Expression in
  Online Social Networks". O nome atual condensa o título da própria fonte.
- **Julgamento**: online moral outrage nomeia a expressão, isto é, o fenômeno, e não o processo de
  aprendizagem (R3). Além disso, ficaria próximo de B8 Moral contagion. **Opções**: (a) manter · (b)
  **Social learning of moral outrage**, mais fiel ao título de [13], com online moral outrage citado na
  definição · (c) Online moral outrage. **Recomendação: (b).** Cuidado: E1 aparece no 2º fechamento do
  *feedback loop* (5.2, Figura 3).

### T05-F06 — E3 Metric-driven content production: estatuto de mecanismo questionado · **Importante**
- **Rascunho**: é prática organizacional ou comportamento de ator (criadores, plataformas); alimenta
  mecanismos, não é um.
- **Conferido**: a Mec-T02 (D18) já reformulou E3 como incentivo do lado da oferta. A ficha descreve um
  processo: produtores aprendem com as métricas o que circula e passam a oferecer mais disso. Esse
  processo passa por Q1–Q3. Q4 é limítrofe, porque o processo é executado por um ator (organizações de
  mídia), como a 5.3 registra (ator primário OA). A base é fraca: Petre [102] só por resenhas, R2 baixo.
  A Seção 10.2 (implicações para o jornalismo) depende de E3.
- **Opções**: (a) **manter**, deixando explícito que o processo é o aprendizado do produtor (paralelo a
  E1, com recompensa econômica) · (b) fundir em E1 como via do produtor (43 → 42) · (c) retirar da lista
  e tratar como comportamento de ator na 5.3 e na 10.2 (43 → 42). **Recomendação: (a).** Um ator que
  executa um processo não torna o processo um ator, e E1 tem a mesma estrutura. Se (b) ou (c), a 10.2
  precisa ser reescrita.

### T05-F07 — F3 Message brevity: o nome designa a característica, não o efeito · **Menor**
- **Rascunho**: é a restrição de design (AF7), não o mecanismo. Depois sugere brevity effect, que nomeia
  o efeito produzido pela restrição.
- **Conferido**: R2 baixo para os dois (message brevity 8, brevity effect 2). A Mec-T02 descartou
  *low-context communication* porque o termo já designa outro construto (Hall). A fonte [9] (Jaidka et
  al.) chama a restrição de *constraint affordance*, que é a AF7.
- **Julgamento**: com R2 empatado, decide a R3. **Proposta**: **Brevity effect (alt. message brevity)**,
  com a primeira frase da ficha descrevendo o efeito. Isso responde também à primeira crítica.

### T05-F08 — F5 Incivility exposure effect: a fonte definidora usa nasty effect · **Menor**
- **Rascunho**: primeiro, redundância com F4. Depois corrige: o *nasty effect* de Anderson et al. é a
  percepção de quem testemunha a incivilidade, distinto do contágio (F4). Sugere nasty effect.
- **Conferido**: [49] é Anderson et al., "The 'Nasty Effect': Online Incivility and Risk Perceptions of
  Emerging Technologies" (R1). R2: nasty effect 12, incivility exposure effect 0. A fronteira com F4 já
  está escrita na ficha de F4.
- **Julgamento**: **Proposta**: **Nasty effect (alt. incivility exposure effect)**. A fronteira F4 × F5
  fica, com os nomes atualizados.

### T05-F09 — G1 Gatekeeping decline: o alternativo é o termo corrente · **Menor**
- **Rascunho**: disintermediation é muito mais usado, e Bennett e Livingston [74] o usam.
- **Conferido**: R2 gatekeeping decline 1, decline of gatekeeping 4, disintermediation 237 (restrito a
  news, media ou journalism). O uso em [74] foi conferido pelo usuário; o PDF não está aqui. A ficha
  tem texto amarelo da T04-A6 ("gatekeeping is better described as redistributed"), e a Introdução tem
  a T04-A1.
- **Julgamento**: **Proposta**: **Disintermediation (alt. gatekeeping decline)**. A frase da T04-A6
  continua válida. Conferir a coerência dos dois textos da T04 com o nome novo.

### T05-F10 — G2 Propaganda feedback loop: nome em conflito com o *feedback loop* do framework · **Importante**
- **Rascunho**: (1) o nome designa o próprio conceito de retroalimentação, que o framework já formaliza
  na 5.2; (2) Benkler, Faris e Roberts descrevem a dinâmica sem esse rótulo; sugere network propaganda.
- **Conferido**: R2 propaganda feedback loop 12, network propaganda 76 (inclui citações do título do
  livro). Quanto a (2), Benkler et al. 2018 usam o rótulo *propaganda feedback loop*, inclusive como
  título de capítulo **[conhecimento do agente; conferir no livro, sem PDF]**. Se isso se confirmar, a
  premissa (2) não procede. *Network propaganda* designa a arquitetura do ecossistema de mídia, que é
  estrutura e não processo (R3). Quanto a (1), G2 é um ciclo específico entre veículos partidários,
  políticos e audiência, distinto do ciclo design → outcome da 5.2, mas o nome convida a confusão.
- **Opções**: (a) manter o nome e acrescentar uma frase que distinga G2 do *feedback loop* da 5.2 ·
  (b) **Network propaganda (alt. propaganda feedback loop)**, que favorece a R2 e viola a R3.
  **Recomendação: conferir o livro primeiro (P2). Se o rótulo se confirmar, (a); se não, (b).**

### T05-F11 — G3 Manufactured consensus × astroturfing · **Menor**
- **Rascunho**: uso real, mas em literatura recente e de menor peso (Mints 2023). O conceito
  estabelecido é *astroturfing* (Kovic et al. 2018). Sugere online astroturfing.
- **Conferido**: R2 manufactured/manufacturing consensus 112, astroturfing 850, coordinated inauthentic
  behavior 116, online astroturfing 16. A fonte que a ficha cita para a definição é [53], Woolley e
  Howard (eds.), *Computational Propaganda* (2018). *Manufacturing consensus* é termo de Woolley
  **[conhecimento do agente; conferir: capítulo de Woolley e Guilbeault em [53]; livro de Woolley,
  2023]**. A premissa de "menor peso" não procede inteira, mas a R2 favorece claramente astroturfing.
- **Opções**: (a) manter (R1, com [53]) · (b) **Astroturfing (alt. manufactured consensus, coordinated
  inauthentic behavior)**, com Kovic et al. 2018 como fonte definidora (referência nova, G1) e [53]
  mantido · (c) Online astroturfing (16). **Recomendação: (b).** O qualificador "online" não é
  necessário, porque a ficha já situa o processo nas plataformas.

### T05-F12 — G6 Partisan flagging: nome sem uso na literatura · **Importante**
- **Rascunho**: é uma instância de viés de confirmação aplicada à moderação; nenhum paper usa o termo.
- **Conferido**: R2 = 2. O nome foi cunhado na Mec-T03 a partir do candidato K32. A única fonte é a
  simulação de Westermann e Coscia [160], cujo título fala em "low tolerance feedback loops in social
  media flagging systems". O termo que eles usam no texto está **[a verificar]**, porque o PDF não está
  aqui. Quanto ao estatuto, G6 passa por Q1–Q4: a saída é uma sanção que muda a oferta de conteúdo, e
  não uma crença individual, o que o distingue de C2. A evidência, porém, é um único modelo, mais uma
  observação de Myers West [78].
- **Opções**: (a) renomear para o termo da fonte, ou o mais recorrente (ex.: biased flagging, mass
  reporting), após conferir o PDF · (b) **retirar como mecanismo próprio** e manter a dinâmica como
  observação em G5 (perceived censorship) e na justificativa de AF10 (43 → 42; reverte parte da
  Mec-T03, K32) · (c) manter, declarando que o termo é adotado neste artigo.
  **Recomendação: conferir o PDF (P4). Se não houver termo estável, (b).** A opção (b) tem o maior
  custo de propagação ("43" aparece 17 vezes, mais as Tabelas 6 e A1, a matriz e a 5.3).

### Observação geral do rascunho — termos alternativos
O rascunho pede que o estudo traga os termos alternativos. Eles já estão nas fichas ("alt. …"). Toda
troca de nome deste plano mantém o nome antigo como alternativo, para não perder a ligação com a v1 e
com os textos anteriores. Levar os alternativos também para a Tabela 6 ou a Tabela A1 é a decisão D8.

## 6. Decisões necessárias

| # | Decisão | Opções | Recomendação |
|---|---|---|---|
| D0 | ID e lugar desta tarefa | (a) T05 neste INDEX, com a revisão anterior de mecanismos citada como Mec-T02/Mec-T03 · (b) continuar a numeração do repositório onde a Mec-T02/T03 foi feita | **(a)**. Opcional: trazer os quatro arquivos do zip para `reviews/` e `adjustments/` com prefixo próprio (ex.: `MEC-T02-…`), para que fiquem versionados |
| D1 | Cor da marcação | (a) **verde** `#00FF00`, como nos ajustes de mecanismos · (b) amarelo, como em `manuscripts/CLAUDE.md` e na T04 | **(a)**. Exige adaptar o `gdocs_apply.py` (P1) |
| D2 | B4 | Evidence = Plausible e frase na ficha · manter Moderate | Plausible |
| D3 | B10 | (a) Community radicalization pathway · (b) Online radicalization · (c) Radicalization pipeline | (a) |
| D4 | E1 | (a) manter · (b) Social learning of moral outrage · (c) Online moral outrage | (b) |
| D5 | E3 | (a) manter e explicitar o processo · (b) fundir em E1 · (c) retirar | (a) |
| D6 | G2 | (a) manter e distinguir da 5.2 · (b) Network propaganda | condicionada à P2 |
| D7 | G6 | (a) renomear · (b) retirar (43 → 42) · (c) manter | condicionada à P4; (b) se não houver termo |
| D8 | Alternativos nas tabelas | (a) só nas fichas · (b) nova coluna na Tabela A1 · (c) na Tabela 6 | (a). A Tabela 6 já tem 9 colunas |
| D9 | Trocas sem opção em aberto | F3 → Brevity effect · F5 → Nasty effect · G1 → Disintermediation · G3 → Astroturfing · C7 atribuição · B7 distinções | Aprovar em bloco ou item a item |
| D10 | Referências novas | Kovic et al. 2018 (G3) · fonte do rótulo *illusory truth* (C7) · opcional Flache et al. 2017 (B7). Pelo fluxo de literatura (G4), com BibTeX do Crossref (G1) | Aprovar a busca dessas três |

## 7. Lotes planejados (depois das decisões)

A estrutura segue a da Mec-T02/T03: fichas primeiro, depois tabelas, depois propagação. A maioria das
fichas é texto verde inserido pelo agente e ainda não incorporado pelos autores. Esses trechos são
revistos com `revisar-insercao`, sem riscar. Onde o texto já tiver sido editado por um humano, o
trecho é riscado e substituído.

| Lote | Conteúdo | Ajustes previstos (aprox.) |
|---|---|---|
| 0 | **Pré-requisito técnico**: `gdocs_apply.py` aceitar o verde (inserção e `revisar-insercao`), com testes (P1) | — |
| 1 | **Fichas** (Seção 6): B4, B7, B10, C7, E1, E3, F3, F5 (e a frase de fronteira em F4), G1, G2, G3, G6 | 12–14 |
| 2 | **Tabelas**: Tabela 6 (nome, *Evidence* de B4), Tabela A1 (nomes), matriz de affordances (Tabela de affordances), tabela de atores (5.3) | 4–8 |
| 3 | **Propagação no texto**: Introdução, 2.3, 5.2 (2º fechamento cita E1), 5.3, 7.1 (justificativas "Why AFn" que citam os 12), 9.x, 10.2 (cita G1 e E3), 11 e Apêndice A. Se D7 = (b): contagem "43" (17 ocorrências) e listas de G | 25–60 |
| 4 | **Referências novas** (D10) no fim da lista, numeração seguinte à atual | 1 |
| — | **Manual, com o usuário**: Figuras 3, 4, 5–15 e A1, onde os nomes aparecem | — |

**Alcance medido no texto atual** (ocorrências fora das tabelas, aproximadas): Interpersonal political
tension 13 · Manufactured consensus 13 · Social learning of outrage 13 · Propaganda feedback loop 10 ·
Gatekeeping decline 8 · Partisan flagging 7 · Negative social influence 7 · Illusory truth 7 · Message
brevity 5 · Online community radicalization 5 · Incivility exposure effect 3 · Metric-driven content
production 3.

## 8. Pendências

| # | Item [a verificar] | Achado | O que falta |
|---|---|---|---|
| P1 | O `gdocs_apply.py` deste repositório só reconhece o amarelo. A versão da outra máquina, que aplicou a Mec-T02/T03, usava o verde | D1 | Portar o suporte ao verde, com testes, antes do lote 1 |
| P2 | O rótulo *propaganda feedback loop* em Benkler, Faris e Roberts (2018) | F10 | Livro sem PDF: conferir no exemplar ou no Google Books |
| P3 | O uso de *disintermediation* em Bennett e Livingston [74] | F09 | Conferido pelo usuário; PDF ausente aqui |
| P4 | O termo que Westermann e Coscia [160] usam para a dinâmica | F12 | PDF de [160] em `references/` |
| P5 | *Manufacturing consensus* em Woolley e Howard [53] | F11 | Livro sem PDF |
| P6 | PDF de Hasher et al. [66] e fonte do rótulo *illusory truth effect* | F04 | PDF e escolha da fonte (D10) |
| P7 | Os PDFs da revisão anterior de mecanismos (53 na outra máquina) não estão em `references/` deste repositório (26 arquivos) | Geral | Sincronizar `references/` entre as máquinas |

## 9. Decisões registradas (2026-10-20)

| # | Decisão do usuário | Consequência |
|---|---|---|
| D0 | T05 neste INDEX; zip fora do Git | Mec-T02/Mec-T03 seguem citados como no plano |
| D1 | **Amarelo** (contra a recomendação de verde) | Não há lote 0 (P1 cai). Os trechos de mecanismos que ainda estão em verde **não são reconhecidos** por `revisar-insercao`: serão riscados e substituídos, ou os autores incorporam antes. Conferir, ficha a ficha, a cor do trecho vigente antes de redigir |
| D2 | B4: Evidence = Plausible + frase na ficha | Ajuste na ficha e na Tabela 6 |
| D3 | B10: Community radicalization pathway | alt. online community radicalization |
| D4 | E1: Social learning of moral outrage | alt. social learning of outrage; cuidado com a 5.2 (Figura 3) |
| D5 | E3: manter e explicitar o processo | 10.2 não muda de estatuto |
| D6 | **Em aberto**: depende de P2 (Benkler et al. 2018, sem PDF) | Usuário confere o livro |
| D7 | **Em aberto**: depende de P4 (PDF de [160] ausente de `references/`) | Usuário deposita o PDF |
| D8 | Alternativos só nas fichas | Tabelas 6 e A1 só com o nome novo |
| D9 | Trocas em bloco: F3 → Brevity effect · F5 → Nasty effect · G1 → Disintermediation · G3 → Astroturfing · C7 atribuição · B7 distinções | Redigir no lote 1 |
| D10 | Buscar as três referências (Kovic 2018, fonte do truth effect, Flache 2017) | Pelo `/literature-review`, G4 por item, BibTeX via Crossref (G1) |

## 10. Fundamentação na literatura (2026-10-20, depois da Seção 9)

O rascunho é do orientador. A pedido do usuário, cada decisão foi fundamentada nas fontes lidas no
PDF, com página. O resultado, escrito para o orientador, está em
[T05-fundamentacao-nomes.md](T05-fundamentacao-nomes.md). PDFs novos no tema
`areas/mestrado/research/mecanismos-nomenclatura` (9 obras, BibTeX via Crossref). PDFs de obras
citadas em `references/`: [13], [49], [52], [56] (versão publicada), [66], [74], [75] (cap. 3), [76], [160].

**Mudanças em relação à Seção 9 e à Seção 5** (a leitura corrigiu o plano):

| Item | Antes | Agora | Motivo |
|---|---|---|---|
| B7 (F02) | manter, com frases de distinção | **Repulsive influence** (alt. negative social influence) | Flache et al. 2017 (¶2.47) usam *repulsive influence* como nome principal; *negative social influence* no OpenAlex é dominado pelo sentido "má influência" (22 dos 50 mais citados na medicina). Corrige a afirmação de F02 de que a crítica do rascunho não se confirmava |
| C7 (F04) | fonte do rótulo: Dechêne 2010 ou Fazio 2015 | Begg et al. 1992 (p. 446), que nomeia o efeito e o atribui a Hasher 1977 | leitura |
| G1 (F09) | uso de *disintermediation* em Bennett e Livingston [74] conferido pelo usuário (P3) | [74] **não** contém o termo; fonte da definição passa a ser Del Vicario et al. [52] (p. 554) | leitura do texto completo de [74]. P3 resolvida |
| G2 (F10), D6 | condicionada à P2 | **(a) manter** e distinguir da 5.2 | Benkler et al. [75], p. 79: "We call this dynamic the 'propaganda feedback loop'". P2 resolvida |
| G3 (F11), D9 | Astroturfing | **Digital astroturfing** (alt. online astroturfing, manufactured consensus) | Kovic et al. 2018 (p. 72) defendem o qualificador *digital*. P5 substituída: *manufacturing consensus* é tese de Woolley 2023 (via resenha) |
| G6 (F12), D7 | condicionada à P4 | **(b) retirar** (43 → 42) | [160] não usa o termo e constrói o modelo sobre viés de confirmação (p. 1). P4 resolvida |

Seguem como na Seção 9: B4, B10, E1, E3, F3, F5. Pendências abertas: PDFs de [5] e [9], capítulo de
*Network Propaganda* que define o termo, livro de Woolley (2023). Nenhum ajuste foi redigido; o
próximo passo é o aval do orientador ao documento de fundamentação.

## T05.1 — Nomes mantidos: reconhecer o termo mais disseminado (2026-10-20)

### 1. Escopo
O orientador comparou, no Google Scholar, quatro nomes com os alternativos: *radicalization pipeline*
(176) × Community radicalization pathway (1); *online moral outrage* (68) × Social learning of moral
outrage (0); Metric-driven content production (0); *network propaganda* (4.666) × Propaganda feedback
loop (199). Ele decidiu manter os nomes da T05 e pediu que o texto diga, em cada um, que a
literatura usa mais o termo alternativo, e por que o artigo escolheu o outro. Fora do escopo: trocar nomes.

### 2. Mapeamento
Fichas B10 (6.3), E1 e E3 (6.6), G2 (6.8) na cópia de revisão lida em 2026-10-20. Fontes: Munn [99],
Ribeiro et al. [67], Brady et al. [13], Crockett [127], Benkler et al. [54] (cap. 3), Tandoc [132]
e Petre [55] (só o título). Numeração da lista atual, renumerada pelos autores depois da T05.

### 3. Avaliação
- **T05.1-F01 — Texto atual não reconhece o termo mais disseminado** · **Menor**. B10 chega perto
  ("forms what the literature calls the radicalization pipeline" e o qualificador *community* "is
  introduced here"). E1 e G2 trazem o alternativo só entre parênteses, e G2 justifica pela fonte ("The
  name is the one Benkler et al. [54] give to this dynamic"). E3 não diz que o rótulo é do artigo.
- **Cuidado com as contagens**: as do Scholar (texto completo) e as do OpenAlex (título e resumo,
  régua da T05) divergem. Em *pathway* × *pipeline*, o OpenAlex dá o inverso (82 × 17). As 4.666
  ocorrências de *network propaganda* devem ser, em boa parte, citações do título do livro. Contagem
  não é citável: as frases nomeiam obras que usam o termo e não trazem números.

### 4. Achados indiretos
Nenhum.

### 5. Sugestões
Quatro inserções no fim das fichas, sem riscar texto, em
[adjustments/T05.1-ajustes.md](../adjustments/T05.1-ajustes.md) (T05.1-A1 a A4), com a página de cada
trecho na justificativa. Simulação em 2026-10-20: as quatro âncoras foram encontradas.

### 6. Pendências
| # | Item [a verificar] | Achado | O que falta |
|---|---|---|---|
| 1 | Aprovação das quatro frases pelo usuário e pelo orientador | F01 | resolvida: aprovadas pelo usuário e aplicadas em 2026-10-20 |
| 2 | Capítulo de *Network Propaganda* que define *network propaganda* | A3 | mesma pendência 3 da T05. A frase se limita ao cap. 3 |
