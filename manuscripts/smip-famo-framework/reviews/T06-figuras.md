# T06 — Figuras: diagnóstico e plano de substituição em lotes

- **Manuscrito**: smip-famo-framework
- **Versão revisada**: cópia de revisão no Google Docs, lida em 2026-10-20 (42 mecanismos em 7 blocos, 11 affordances; texto e imagens extraídos pela API). O PDF `paper/v1-2026-10-08.pdf` está defasado em relação às figuras e não foi usado.
- **Data**: 2026-10-20
- **Relatórios anteriores consultados**: T01 (F07, F11, A10, A11), T02 (I01), T05 (pendência das figuras)

## 1. Escopo

A tarefa pede que todas as figuras do artigo sejam revisadas contra seis hipóteses do usuário:
(H1) estão desatualizadas, (H2) têm problema de estrutura ou diagramação, (H3) têm legenda
incorreta, (H4) são citadas de forma incorreta no texto, (H5) têm resolução ou qualidade ruim e
(H6) são confusas. A tarefa também pede ajustes além desses, quando for o caso, e um plano de
substituição em lotes. **Este relatório traz o diagnóstico e o plano. Nenhuma figura foi
alterada.**

Fora do escopo: as tabelas (só usadas como referência), as imagens do template MDPI (logotipos
e CC BY) e o texto das seções, exceto as legendas e as frases que citam as figuras.

## 2. Mapeamento

São 15 figuras no corpo do texto. A referência do conteúdo atual são as Tabelas 5, 6 e 7 e a
prosa das Seções 4.3, 5, 7, 8 e do Apêndice A.

| Figura | Onde está | Citada em | Conteúdo | Pixels · dpi efetivo · formato |
|---|---|---|---|---|
| 1 | 4.3 | 4.3, 9.3 | processo de identificação da literatura | 292×505 · **168 dpi** · PNG |
| 2 | 5.1 | 5.1, 5.2, 5.3 | framework de 4 camadas + moderadores + atores + loop | 1130×1392 · 285 dpi · **JPEG** |
| 3 | 5.2 | 5.2, 9.1 | três pontos de fechamento do loop | 1166×837 · 247 dpi · PNG |
| 4–14 | 7.1 | 7.1 (cada uma no parágrafo da sua affordance), 9.3 | mecanismos alimentados por AF1…AF11 | 1246 px de largura · 230–430 dpi · PNG |
| 15 | fim da 7.3 | 8 (2×), 10.1 | rede bipartida affordances × blocos | 2048×1687 · 391 dpi · PNG com fundo transparente |
| A1 | Apêndice A.2 | A.2 | fluxo do segundo levantamento (Lens) | 1900×2042 · 529 dpi · PNG |

**Numeração e citação.** A sequência de primeira citação está correta (1 → 2 → 3 → 4…14 → 15
→ A1), e a renumeração feita pelos autores (afordâncias 5–15 → 4–14, rede bipartida 4 → 15) foi
aplicada no texto inteiro, inclusive na 9.3 ("Figures 4 through 14") e na 10.1.

## 3. Avaliação

### Resposta às hipóteses

| Hipótese | Resultado | Figuras afetadas |
|---|---|---|
| H1 Desatualizadas | **Confirmada** em 14 das 15 figuras | todas exceto a 2 (que tem só dois rótulos divergentes) |
| H2 Estrutura ou diagramação | **Confirmada** | 2, 3, 4, 15 |
| H3 Legenda incorreta | **Parcial**: as legendas não estão erradas em relação ao texto, mas as das Figuras 3 e 4–14 não explicam a notação, e a da 15 descreve 7 blocos que a imagem não mostra | 3, 4–14, 15 |
| H4 Citação incorreta | **Em grande parte não confirmada**: números e ordem corretos. Há dois problemas: a 15 está antes da primeira citação, e a 5.2 descreve o loop de um jeito que a Figura 3 não mostra | 3, 15 |
| H5 Resolução ou qualidade | **Parcial**: a Figura 1 está abaixo de 300 dpi, a 2 é JPEG (arte em linha comprimida) e a 15 tem fundo transparente. As demais têm resolução aceitável | 1, 2, 15 |
| H6 Confusas | **Confirmada** | 2, 3, 4–14, 15 |

### T06-F01 — Figuras 4 a 14 descrevem uma taxonomia que não existe mais · **Crítico**
- **Localização**: Seção 7.1, Figuras 4–14.
- **Fato**: as figuras usam a numeração e os nomes da lista antiga de 9 blocos (M e H incluídos). Nenhuma das 11 coincide com a Tabela 7. Exemplos:
  - Figura 4 (AF1): "A1 — Engagement-based ranking", "A5 — Algorithmic agenda-setting", "C4 — Illusory truth effect", "C5 — Negativity bias & moral contagion", "D2 — False polarization", "G2 — Network propaganda", "H1/H2 — News avoidance", "M1 — Informational isolation", "M5 — Coordinated fake behavior", "M6 — Reinforcing spiral". Pela Tabela 7, AF1 alimenta A1, A2, A3, A4, B2 (−), B8, C3\*, C7, C8, C9, D1, D6, E3\*, G2 e G3 (15 ligações). A figura tem 13, e faltam algorithmic amplification (A2), unfriending (B2, −) e metric-driven content production (E3\*).
  - Mecanismos que já não existem aparecem como alvos: "A3 — Connection recommendation" (Fig. 5), "E4 — Social quantification/vanity metrics" (Fig. 7), "M4 — Information disorder" (Fig. 8), "A4 — Context collapse" (Fig. 9).
  - Os títulos de quatro figuras usam nomes de feature ou de resultado que o próprio artigo rejeita: "AF2 — Friend recommendation", "AF6 — Context collapse", "AF9 — Infinite scroll" e "AF11 — Group formation". A 9.1 diz que "Connection recommendation and infinite scroll are features", que "context collapse is the low end of audience segmentation" e que "community formation is an outcome".
  - Faltam ligações em quase todas: B7 (Fig. 5); B2 e C5 (Fig. 6); E2 (Fig. 7); B2, B7 e C5 (Figs. 9 e 11); A2 (±) e C5 (±) (Fig. 13); B2 (Fig. 14).
  - Nenhuma figura mostra as ligações negativas (−) ou que dependem do desenho (±), que a Tabela 7 e a 9.2–9.3 tratam como achado.
- **Julgamento**: a 9.3 diz que as ligações são "visualized individually in Figures 4 through 14". Um revisor que confira uma figura com a Tabela 7 encontra outra taxonomia, com IDs que não existem. Isso compromete a contribuição central (mecanismos auditáveis). As figuras precisam ser refeitas, não corrigidas pontualmente.
- **Relação com revisões anteriores**: confirma a pendência da T05 ("figuras 3, 5–15 e rede bipartida"). Absorve T02-I01 para as figuras.

### T06-F02 — Figura 15 mostra 9 blocos; legenda e texto falam em 7 · **Crítico**
- **Localização**: fim da 7.3; citada na Seção 8 e na 10.1.
- **Fato**: os nós da direita são "M — spirals, A — algorithm, B — network, C — cognition, D — perception, E — incentives, F — interaction, G — ecosystem, H — avoidance". A legenda diz "the seven blocks of mechanisms". Os rótulos das affordances usam nomes antigos ("AF2 Connections", "AF3 Association", "AF4 Metrics", "AF6 Context collapse", "AF7 Format", "AF9 Infinite scroll", "AF11 Groups"). As arestas seguem o mapeamento antigo.
- **Julgamento**: a Seção 8 tira dois padrões da figura (AF1 liga 6 de 7 blocos; AF4, AF6 e AF8 ligam 4 cada; AF11, AF2 e AF7 ficam na periferia). Esses números conferem com a Tabela 7, mas não com a imagem atual. Há também um problema de diagramação: as linhas pretas finas, todas iguais e sem ordem, se cruzam em massa e não deixam ver a força das ligações. O fundo transparente fica preto em vários visualizadores, inclusive no sistema de submissão.

### T06-F03 — Figura 3 usa IDs e nomes antigos e não mostra a cadeia descrita no texto · **Importante**
- **Localização**: Seção 5.2.
- **Fato**: os três ciclos da figura são "Fewer moderate voices (M7) → Connection recommendation (AF2), reinforces B1", "Rewarded outrage (E1) → Engagement-based ranking (AF1), reinforces C5" e "Apparent consensus (D3) → Public metrics (AF4), reinforces D3". O texto descreve: spiral of silence (D5) → network-informed associating (AF2) → homophily (B1); social learning of moral outrage (E1) → algorithmic content curation (AF1) → moral contagion (B8); false consensus (D3) e pluralistic ignorance (D4) → social quantification (AF4) → apparent consensus.
- **Julgamento**: M7 não existe e C5 hoje é o backfire effect, um mecanismo diferente do citado no texto. Os rótulos das affordances são nomes de feature. A seta curva volta para a caixa de origem, mas o rótulo diz que reforça **outro** mecanismo (B1, C5), então a figura mostra um ciclo de dois nós quando o texto descreve uma cadeia de três passos. D4 está no texto e não na figura. A legenda ("Three concrete points where the feedback loop closes") não explica cores nem setas.

### T06-F04 — Loop: a Figura 2 e a 5.2 o desenham de Outcomes para Features, mas os três fechamentos vão de mecanismo para affordance · **Importante**
- **Localização**: Figura 2 (seta "closes the loop"); 5.2, §4 ("connecting the outcomes layer back to the 'Features' layer"); Figura 3.
- **Fato**: na Figura 2, a seta do loop sai de Outcomes e chega a Features. Os três pontos de fechamento detalhados na 5.2 partem de mecanismos (D5, E1, D3/D4) e chegam a affordances (AF2, AF1, AF4), por meio dos dados e sinais que as features usam.
- **Julgamento**: o leitor que passa da Figura 2 para a Figura 3 encontra duas representações do mesmo loop que não se encaixam. Não é erro de desenho: é uma escolha conceitual dos autores. Ela pode ser resolvida de duas formas: (a) manter Outcomes → Features na Figura 2 como representação geral e mostrar na Figura 3 que a volta passa pelos dados que as features usam; ou (b) desenhar o loop a partir da camada de mecanismos. Em qualquer caso, a 5.2 precisa de uma frase que una as duas figuras. **Decisão dos autores (D1 abaixo).**

### T06-F05 — Figura 1 está desatualizada em relação à 4.3 e ao Apêndice A, e tem baixa resolução · **Importante**
- **Localização**: Seção 4.3.
- **Fato**: a primeira caixa diz "4 anchor frameworks / SPIR, Arora, Tölle&Trier" (três nomes, e Tanyel & Windeler não é um framework). O fluxo é linear: anchors → citation chaining → foundational literature → final taxonomy. A 4.3 (último parágrafo) e o Apêndice A descrevem duas fontes: a primeira lista (41 mecanismos em 9 blocos, consolidada em 39 em 7 blocos pelo teste de mecanismo) e o segundo levantamento no Lens (4 mecanismos novos, um deles retirado depois), que resultam em 42. A imagem tem 292 px de largura (168 dpi no tamanho de página).
- **Julgamento**: a figura ilustra só metade do processo que o texto descreve e contradiz o próprio texto da 4.3 ("four anchor works"). A iteração e o critério de parada (T01-F07) continuam dependendo de fatos dos autores (T01-D2): a figura nova não deve inventá-los.
- **Relação com revisões anteriores**: confirma T01-F11. A nota A11 da T01 (rótulo da caixa 1) passa a ser resolvida pela imagem nova. A parte de iteração do A11 continua bloqueada por T01-D2.

### T06-F06 — Figura A1: "n = 43" artigos citados contra "42" no texto; "4 new" sem registrar a retirada de G6 · **Importante**
- **Localização**: Apêndice A.2, Figura A1 e parágrafo que a precede.
- **Fato**: a caixa final diz "Papers cited in this article … n = 43" e a lateral "Included but not cited n = 101" (144 − 43). O texto diz "This article cites 42 of them". A caixa de extração diz "19 mechanisms (15 in the first list, 4 new)". O texto informa que G6 (partisan flagging) foi retirado depois.
- **Julgamento**: uma das duas contagens está errada. Se forem 42, a caixa lateral passa a 102. A divergência não vem da T05, que não alterou esse trecho, então **só os autores podem dizer qual número vale [a verificar]**. A caixa de extração deve mostrar a retirada de G6 (4 aceitos → 3 mantidos), para o fluxo fechar em 42 mecanismos. A diagramação é boa, mas a fonte (DejaVu) difere das demais figuras.

### T06-F07 — Figura 2: rótulos divergentes, letras capitulares e JPEG · **Menor**
- **Localização**: Seção 5.1.
- **Fato**: os atores aparecem como "Automated agents" e "Algorithm". A Tabela 5 e a 5.3 usam "Automated or coordinated agents" e "Algorithmic system". Os títulos das camadas usam uma letra num círculo seguida do resto da palavra ("(F) eatures", "(A) ffordances"). A seta Features → Affordances diz "enables", e o texto usa "realize" ("the affordances these features realize"). O arquivo é JPEG.
- **Julgamento**: a estrutura da figura está de acordo com o texto atual (moderadores → Features e Affordances; atores → Mechanisms e Outcomes). As capitulares quebram a leitura da palavra e, reduzidas, leem-se como "eatures". JPEG gera artefatos em arte de linha. A correção é de redesenho, sem mudança de conteúdo, exceto a seta do loop (F04).

### T06-F08 — Notação das Figuras 4–14 sem legenda e rótulos de aresta que contradizem o texto · **Importante**
- **Localização**: Figuras 4–14 e suas legendas.
- **Fato**: linha cheia = direto e tracejada = indireto, mas nenhuma legenda diz isso. Cada aresta tem um rótulo curto que não está no texto. Alguns contradizem a prosa: na Figura 11, AF8 → F2 diz "cheap fake accounts", e a 7.1 diz que nos *firestorms* "non-anonymous individuals are more aggressive than anonymous ones". Na Figura 12, as quatro ligações de AF9 estão marcadas como "direct", e o texto diz "None of these four links is definitional — all follow from the same indirect principle". A Tabela 7 também não marca asterisco nelas.
- **Julgamento**: rótulos de aresta mantidos à mão divergem do texto a cada revisão. A figura nova deve ser gerada a partir da Tabela 7, com a notação dela (\*, −, ±) explicada na legenda. A marcação de AF9 (direto ou indireto) precisa ser decidida pelos autores, porque texto e Tabela 7 divergem [a verificar].

## 4. Achados indiretos

### T06-I01 — Figura 15 posicionada antes da seção que a cita · **Menor**
- **Localização**: a figura está no fim da 7.3, antes do título da Seção 8, e é citada pela primeira vez na Seção 8, §1.
- **Fato**: o template MDPI pede a figura depois da primeira citação.
- **Julgamento**: mover para depois do §1 da Seção 8.

### T06-I02 — Posição das Figuras 4–14 em relação ao parágrafo "Why…" é irregular · **Menor**
- **Localização**: 7.1. As Figuras 4, 5, 6, 8, 9, 11 e 13 vêm logo depois da definição da affordance. As Figuras 7, 10 e 12 vêm depois do parágrafo "Why…", e a 14 vem antes dele.
- **Julgamento**: padronizar (figura logo depois do parágrafo de definição, que é o que a cita).

### T06-I03 — Estilo visual heterogêneo entre figuras · **Menor**
- **Fato**: há quatro famílias de fonte e paleta (Fig. 1; Fig. 2 em Lato; Figs. 3–15 em Arial; Fig. A1 em DejaVu). Os rótulos usam travessão ("AF1 — Algorithmic curation").
- **Julgamento**: um único estilo (fonte, paleta segura para daltonismo, espessuras) para as 15 figuras. Rótulos sem travessão, pela regra de redação do texto novo.

## 5. Sugestões

Diretrizes para todas as figuras novas:
- **Gerar por script a partir dos dados do paper.** As Figuras 4–15 saem da Tabela 7 e dos blocos da Seção 6 (um arquivo de dados + um gerador). Se a tabela mudar, as figuras são regeneradas sem redesenho manual, e o drift que causou F01 e F02 não se repete.
- **Formato**: SVG (vetorial) + PNG a 600 dpi na largura de coluna do template MDPI, com fundo branco.
- **Nomes canônicos**: os da Tabela 6 (mecanismos), da Tabela 7 (affordances) e da Tabela 5 (atores), sem abreviar.
- **Notação única**: direto = linha cheia; indireto (\*) = tracejada; (−) = enfraquece; (±) = depende do desenho. A notação é explicada em toda legenda que a use.
- **Cor por bloco de mecanismo** (7 blocos), igual em todas as figuras, para que o leitor reconheça um bloco da Figura 4 na Figura 15.
- **Legendas**: cada legenda diz o que a figura mostra e como ler a notação. O texto novo das legendas, em inglês, segue a política de ajustes (riscado + amarelo).

## 6. Pendências

| # | Item [a verificar] | Achado | O que falta |
|---|---|---|---|
| 1 | Artigos citados no segundo levantamento: 42 (texto) ou 43 (Fig. A1)? | F06 | confirmação dos autores |
| 2 | Ligações de AF9: diretas (Tabela 7) ou indiretas (texto da 7.1)? | F08 | decisão dos autores |
| 3 | Iteração e critério de parada do *citation chaining* | F05 | T01-D2 (pausada pelo usuário) |
| 4 | Representação do loop na Figura 2 × Figura 3 | F04 | decisão D1 |

## 7. Plano de substituição em lotes

Cada lote: (1) gero as figuras e as mostro para aprovação; (2) redijo as legendas e as frases
de citação afetadas em `adjustments/T06-ajustes.md`; (3) com o lote aprovado, aplico as
legendas na cópia de revisão e entrego as imagens para a troca (ver D3).

| Lote | Figuras | O que muda | Achados | Depende de |
|---|---|---|---|---|
| 1 | **2 e 3** (núcleo do framework) | Fig. 2: redesenho sem capitulares, rótulos de atores da Tabela 5, "realizes", vetorial; seta do loop conforme D1. Fig. 3: três cadeias de três passos (mecanismo de origem → affordance → mecanismo reforçado), com IDs e nomes atuais, D4 incluído; legenda com a notação. Frase de ligação na 5.2, se D1 pedir | F03, F04, F07 | D1 |
| 2 | **4 a 9** (AF1 a AF6) | Regeneradas da Tabela 7: título com o nome canônico da affordance, mecanismos agrupados e coloridos por bloco, notação \*/−/±, sem rótulos de aresta; legendas com a notação; posição padronizada (I02) | F01, F08 | D2 |
| 3 | **10 a 14** (AF7 a AF11) e **15** | O mesmo para AF7–AF11 (AF9 conforme a pendência 2). Fig. 15 regenerada da Tabela 7: 11 affordances × 7 blocos, espessura da aresta = número de mecanismos, ordem que reduz cruzamentos, fundo branco; mover para depois do §1 da Seção 8 (I01) | F01, F02, F08, I01 | D2, pendência 2 |
| 4 | **1 e A1** (método) | Fig. 1: duas fontes (primeira lista: 4 obras âncora [2–5] → *chaining* → 41 em 9 blocos → teste de mecanismo → 39 em 7 blocos; segundo levantamento → +4, G6 retirado) convergindo em 42 mecanismos e 11 affordances, sem iteração inventada. Fig. A1: número final conforme a pendência 1, retirada de G6 na caixa de extração, estilo unificado | F05, F06, I03 | pendência 1 (A1) |

A ordem segue o peso para o leitor: o framework (lote 1) é lido antes de tudo, e as
Figuras 4–15 (lotes 2 e 3) compartilham o gerador. O lote 4 fica por último porque a Figura A1
depende de uma resposta dos autores.

### Decisões antes do lote 1

- **D1 — Loop (F04)**: (a) manter Outcomes → Features na Figura 2 e mostrar, na Figura 3, que a volta passa pelos dados e sinais que as features usam, com uma frase na 5.2 que ligue as duas (**recomendado**, porque não muda o modelo, só explicita a passagem); (b) desenhar o loop a partir da camada de mecanismos, o que muda a Figura 2 e a 5.2.
- **D2 — Formato das Figuras 4–14**: (a) manter 11 figuras, regeneradas e compactas (**recomendado**: o texto cita cada uma no parágrafo da sua affordance); (b) uma figura composta com 11 painéis (4a–4k), o que exige renumerar as citações; (c) substituir as 11 por uma única matriz affordance × mecanismo, o que duplicaria a Tabela 7.
- **D3 — Como as imagens entram no documento**: a API do Google Docs só insere imagem a partir de uma URL pública, o que exporia figuras de um manuscrito inédito (Confidencialidade, `manuscripts/CLAUDE.md`). Proposta: gerar SVG/PNG localmente, aplicar pela API as legendas e uma nota amarela junto a cada figura ("[AJUSTE T06-A…: substituir pela imagem fig02.png]") e deixar a troca da imagem com você ou com os autores. A figura antiga fica no documento até a troca, como pede a política de ajustes.
- **D4 — Onde ficam os arquivos**: gerador e dados em `adjustments/T06-figuras/` (versionados, como os `.md` de ajustes); SVG/PNG gerados fora do Git (acrescentar ao `.gitignore`), pela mesma razão de `paper/`.
