# Ajustes T02 — Revisão dos mecanismos

- **Manuscrito**: smip-famo-framework · **Versão de referência**: cópia de revisão em Google Docs, lida em 2026-10-10 (ver P1 do relatório)
- **Relatório**: [`reviews/T02-revisao-mecanismos.md`](../reviews/T02-revisao-mecanismos.md) (roteiro na Seção 6, decisões na Seção 7)
- **Destino**: cópia de revisão em Google Docs (ID em `context.md`)
- **Marcação**: texto substituído fica riscado, sem ser apagado; novo texto logo depois, em preto com marca-texto verde (`#00FF00`).
- **Aplicação**: `uv run scripts/gdocs_apply.py apply <doc> manuscripts/smip-famo-framework/adjustments/T02-ajustes.md --ids A1,A2` (simulação; `--apply` grava)

## Lotes

| Lote | Subtarefa | Ajustes | Estado |
|---|---|---|---|
| 1 | T02.3 — bloco A, curadoria algorítmica (A1–A4) | T02-A1 a T02-A8 | **aplicado em 2026-10-13** |
| 2 | T02.3 — bloco B, rede, grupo e difusão (B1–B8) | T02-A9 a T02-A22 | **aplicado em 2026-10-13** |
| 3 | T02.3 — bloco C, seleção e processamento individual (C1–C7; C8 aguarda B02) | T02-A23 a T02-A37 | **aplicado em 2026-10-13** |
| 4 | T02.3 — bloco D, percepção dos outros (D1–D6) | T02-A38 a T02-A48 | **aplicado em 2026-10-13** |
| 5 | T02.3 — bloco E, incentivos (E1–E3) | T02-A49 a T02-A54 | **aplicado em 2026-10-13** |
| 6 | T02.3 — bloco F, interação (F1–F5), com D29 (AF8 → F2 na 7.1) | T02-A55 a T02-A63 | **aplicado em 2026-10-13** |
| 7 | T02.3 — bloco G, ecossistema e oferta (G1–G5) | T02-A64 a T02-A71 | **aplicado em 2026-10-13** |
| 8 | T02.3 — affordances em conflito: AF1, AF2, AF4, AF6, AF7 (7.1, 7.2; D20–D25) | T02-A72 a T02-A78 | **aplicado em 2026-10-16** |
| 9 | T02.4 — processo de identificação (6.1, 4.3, Figura 1) | a definir | depende de T01-D2 |
| 10 | T02.5 — propagação: 10a contagem, 10c tabelas, 10b IDs no texto e loop, 10d Seção 7.1 (figuras depois) | 10a: T02-A79 a A89; 10c: T02-A90, A91 | **10a e 10c aplicados em 2026-10-16**; 10b e 10d a redigir |

A estrutura foi decidida na T02.2 (relatório, Seção 14; D6, D10–D36): 41 → 39 mecanismos em
sete blocos. Cada lote de bloco inclui a abertura do bloco e as mudanças estruturais que o
afetam (fusões, exclusões, itens que chegam de outros blocos). Os ajustes usam os **novos
IDs** (14.6), com o ID da v1 entre parênteses quando necessário.

Cada ajuste segue a estrutura de `T01-ajustes.md`: ID,
lote, achados, decisões, localização (seção, parágrafo e primeiras palavras), ação,
estado, texto original, novo texto (inglês) e justificativa (português).

---

# Lote 1 — Bloco A, curadoria algorítmica (aplicado em 2026-10-13)

**Base**: relatório, Seções 12.3 (modelo de definição), 12.4 (R1–R7), 14.1–14.6 (D13–D36).
**Contagem R2 (OpenAlex, título e resumo, 2026-10-13)**: *filter bubble* 2.545 · *algorithmic
amplification* 1.053 (*engagement-based ranking* 19) · *algorithmic radicalization* 30 +
*radicalisation* 9 (*algorithmic rabbit hole* 1; *YouTube rabbit hole* 6) · *algorithmic
agenda-setting* 16 (*trending topics* 5.421, mas é *feature*, R4).
**Numeração das referências**: o texto novo usa a numeração da **lista**. No trecho original,
Ribeiro et al. e Hosseinmardi et al. aparecem como [57] e [58]; na lista, são [56] e [57]
(pendência P3).
**IDs**: o texto novo usa os IDs da lista final (14.6). Até a T02.5, outras seções do paper
ainda usam os IDs da v1.
**Fontes sem PDF neste lote**: Pariser [44] e Gillespie [16] (livro e capítulo, D-sem-PDF);
McCombs e Shaw [21] foi obtido em 2026-10-13 e conferido (p. 176).

| ID | Localização (âncora) | Ação | Objetivo | Decisões |
|---|---|---|---|---|
| T02-A1 | Título da Seção 6.3, "Bloco A — Curadoria algorítmica e arquitetura" | substituir | Novo nome do bloco | D6 |
| T02-A2 | 6.3, parágrafo de abertura, "Este bloco reúne mecanismos cujo insumo comum é a decisão algorítmica…" | substituir-paragrafo | Critério do bloco pelo locus | D6, T02.1-F05 |
| T02-A3 | 6.3, depois da abertura | inserir-apos | Nova entrada A1, *filter bubble* (vinda de M1) | D27 |
| T02-A4 | 6.3, "A1 — Engagement-based ranking…" | substituir-paragrafo | Entrada A2, *algorithmic amplification* | D20, D31 |
| T02-A5 | 6.3, "A2 — Algorithmic radicalization…" | substituir-paragrafo | Entrada A3, com evidência mista explícita | D32 |
| T02-A6 | 6.3, "A3 — Connection/friend recommendation…" | remover | A3 da v1 fundido em B1 | D21 |
| T02-A7 | 6.3, "A4 — Context collapse…" | remover | A4 da v1 excluído | D22 |
| T02-A8 | 6.3, "A5 — Algorithmic agenda-setting…" | substituir-paragrafo | Entrada A4, *algorithmic agenda-setting* | D15, D35 |

A entrada M1 da Seção 6.2 (de onde sai a bolha de filtro) é tratada no lote 2, junto da
câmara de eco (B2).

---

## T02-A1 — Título do bloco A

| Campo | Valor |
|---|---|
| Lote | 1 |
| Achados | T02.1-F05 |
| Decisões | D6 |
| Localização | Seção 6.3, título: "6.3. Bloco A — Curadoria algorítmica e arquitetura" (só o texto depois de "6.3. "; a numeração da seção muda na T02.5) |
| Ação | substituir |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
Bloco A — Curadoria algorítmica e arquitetura
```

**Novo texto**

```novo
Block A. Algorithmic curation
```

**Justificativa**: "arquitetura" deixa de fazer parte do critério (D6, locus do processo). O
travessão sai pela regra de estilo.

---

## T02-A2 — Abertura do bloco A

| Campo | Valor |
|---|---|
| Lote | 1 |
| Achados | T02.1-F05 |
| Decisões | D6 |
| Localização | Seção 6.3, parágrafo 1, começa com "Este bloco reúne mecanismos cujo insumo comum é a decisão algorítmica" |
| Ação | substituir-paragrafo |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
Este bloco reúne mecanismos cujo insumo comum é a decisão algorítmica sobre o que é exibido, recomendado ou priorizado — justificando agrupá-los separadamente dos mecanismos de rede (Bloco B), que dependem de estrutura de conexões, não de decisão de exibição.
```

**Novo texto**

```novo
This block groups the mechanisms that originate in automated decisions about what each user sees: which posts are ranked first, which videos are recommended next, and which topics are displayed as trending. In all of them the selection is made by the platform's system, not by the user or by the structure of the user's network. This criterion separates them from the mechanisms of Block B, which depend on who is connected to whom and on how content spreads among users.
```

**Justificativa**: o critério do bloco passa a ser o locus do processo (D6). A frase final
deixa explícita a fronteira com o bloco B, que a abertura atual já fazia, sem travessão.

---

## T02-A3 — Nova entrada A1, *filter bubble*

| Campo | Valor |
|---|---|
| Lote | 1 |
| Achados | T02.1-F03 (M1 com nome de outcome), H01 |
| Decisões | D27, D35 (R5) |
| Localização | Seção 6.3, logo depois do parágrafo de abertura reescrito por T02-A2 (aplicar T02-A2 antes) |
| Ação | inserir-apos |
| Estado | aplicado em 2026-10-13 |

**Âncora** (fim do texto novo de T02-A2)

```ancora
and on how content spreads among users.
```

**Novo texto**

```novo
A1. Filter bubble. The narrowing of a user's information exposure produced by algorithmic personalization, in which content is selected according to the user's previous behavior [44,45]. Ranking and recommendation systems (AF1) learn from past clicks and reactions, so congenial content gains space and cross-cutting content loses it without any deliberate choice by the user. Prolonged exposure to a narrower range of views can reinforce existing attitudes and contribute to ideological polarization. The evidence is mixed: on Facebook, individual choices limited exposure to cross-cutting content more than algorithmic ranking did [45]. Unlike the echo chamber (B2), where reinforcement comes from repeated interaction with like-minded peers, the filter bubble originates in the selection made by the system.
```

**Justificativa**: é a metade algorítmica de M1, separada pela D27. A definição segue Bakshy et
al. [45] (p. 1130: "filter bubbles (in which content is selected by algorithms according to a
viewer's previous behaviors)"), e o achado sobre as escolhas individuais é da mesma página.
Pariser [44] cunhou o termo (livro, D-sem-PDF). "Epistemic bubble" não entra como
alternativo, porque não é sinônimo (R6; Seção 14.3, cluster b). O outcome é ideological, e o
rating continua "Mixed".

---

## T02-A4 — Entrada A2, *algorithmic amplification*

| Campo | Valor |
|---|---|
| Lote | 1 |
| Achados | T02.1-F01, T02.2-F02 |
| Decisões | D20, D31 |
| Localização | Seção 6.3, parágrafo que começa com "A1 — Engagement-based ranking (alt.: 'algorithmic amplification')." |
| Ação | substituir-paragrafo |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
A1 — Engagement-based ranking (alt.: 'algorithmic amplification'). Milli et al. [14] demonstram, em auditoria do algoritmo do Twitter, que o ranqueamento por engajamento privilegia conteúdo hostil ao exogrupo; Rathje et al. [38] mostram que animosidade intergrupal é o preditor mais robusto de engajamento político.
```

**Novo texto**

```novo
A2. Algorithmic amplification. The increase in the reach of emotionally charged and out-group hostile content produced by ranking systems that optimize for predicted engagement. Posts about the political out-group attract more shares than other political posts [38], so a system trained on engagement signals (AF1) learns to give them more visibility than a chronological feed would. In a preregistered audit of Twitter, Milli et al. [14] found that the engagement-based algorithm amplified emotionally charged, out-group hostile content that users said made them feel worse about their political out-group, and that users did not prefer the political posts it selected. The mechanism raises exposure to hostile portrayals of the out-group and acts mainly on affective polarization. It differs from moral contagion (B5), the human sharing preference that the algorithm learns, and from the social learning of outrage (E1), which concerns the authors rewarded for producing such content.
```

**Justificativa**: o nome antigo era o critério de ordenação de uma *feature* (T02.1-F01). O
novo nome designa o processo e é o termo mais recorrente (R2). As afirmações sobre Milli et
al. [14] vêm do abstract (linha de base cronológica; usuários dizem se sentir pior sobre o
out-group; não preferem os posts escolhidos). Rathje et al. [38] entra só como o insumo que o
algoritmo aprende (D31). As fronteiras com B5 e E1 são as da D31.

---

## T02-A5 — Entrada A3, *algorithmic radicalization*

| Campo | Valor |
|---|---|
| Lote | 1 |
| Achados | — (cluster e) |
| Decisões | D32 |
| Localização | Seção 6.3, parágrafo que começa com "A2 — Algorithmic radicalization (alt.: 'rabbit hole')." |
| Ação | substituir-paragrafo |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
A2 — Algorithmic radicalization (alt.: 'rabbit hole'). Deslocamento gradual para conteúdo mais extremo via recomendações sucessivas. Ribeiro et al. [57] auditam esse padrão no YouTube; Hosseinmardi et al. [58] mostram que o consumo de conteúdo radical é em boa parte guiado por preferências prévias, não apenas pela recomendação.
```

**Novo texto**

```novo
A3. Algorithmic radicalization (alt. rabbit hole). The gradual shift of a user toward more extreme content through a sequence of recommendations that lead from milder to more radical material. Recommendation systems (AF1) place the next item one click away and can connect mainstream, borderline, and fringe channels. Ribeiro et al. [56] found that YouTube users consistently migrated from milder to more extreme content and that milder far-right channels were easily reachable from more moderate ones, while the most extreme videos were reachable only through channel recommendations. Using a representative panel, Hosseinmardi et al. [57] found instead that news consumption on YouTube was dominated by mainstream sources and that consumers of far-right content formed a small and stable group, which points to prior preferences rather than recommendations. The evidence is therefore mixed. Together with the community radicalization pathway (B8), this mechanism makes up what the literature calls the radicalization pipeline, here divided into an algorithmic route and a community route.
```

**Justificativa**: o nome atual é o mais recorrente na forma específica (R2). *Rabbit hole*
fica como alternativo. A evidência mista fica explícita, como decidido na D32. Ribeiro et al.
[56] (abstract): "users consistently migrate from milder to more extreme content"; "Alt-lite
content is easily reachable from I.D.W. channels, while Alt-right videos are reachable only
through channel recommendations". Hosseinmardi et al. [57] (p. 1): consumo "dominated by
mainstream and largely centrist sources"; consumidores de extrema direita são "a small and
stable percentage". "Radicalization pipeline" é o termo de Ribeiro et al. para a hipótese
geral (D32). Corrige também a numeração das duas citações.

---

## T02-A6 — Remoção da entrada A3 da v1 (*connection/friend recommendation*)

| Campo | Valor |
|---|---|
| Lote | 1 |
| Achados | T02.1-F01, T02.2-F02 |
| Decisões | D21 |
| Localização | Seção 6.3, parágrafo que começa com "A3 — Connection/friend recommendation (alt.: 'people-you-may-know')." |
| Ação | remover |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
A3 — Connection/friend recommendation (alt.: 'people-you-may-know'). Chaney et al. [59] mostram, por simulação, que recomendações treinadas em dados já moldados por recomendações anteriores aceleram a homogeneização comportamental; Santos et al. [60] formalizam o efeito para recomendação de links especificamente.
```

**Justificativa**: o item tinha o nome de uma *feature* e da affordance AF2, e foi fundido em B1
(D21). Chaney et al. [58] e Santos et al. [59] (numeração da lista) passam para a entrada B1,
no lote 2. Pela política de ajustes, o texto fica riscado no documento.

---

## T02-A7 — Remoção da entrada A4 da v1 (*context collapse*)

| Campo | Valor |
|---|---|
| Lote | 1 |
| Achados | T02.1-F01, T02.2-F02 |
| Decisões | D22 |
| Localização | Seção 6.3, parágrafo que começa com "A4 — Context collapse (alt.: 'context collision', 'imagined audience')." |
| Ação | remover |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
A4 — Context collapse (alt.: 'context collision', 'imagined audience'). Unificação de audiências normalmente separadas, documentada por Marwick and boyd [61] a partir de entrevistas com usuários do Twitter.
```

**Justificativa**: o item repetia a affordance AF6 e não era um processo (D22). Seus efeitos já
estão em D5 (espiral do silêncio), B7 (tensão política interpessoal), F2 e F4. Marwick e boyd
[60] passam para a redefinição de AF6, no lote 8.

---

## T02-A8 — Entrada A4, *algorithmic agenda-setting*

| Campo | Valor |
|---|---|
| Lote | 1 |
| Achados | T02.1-F04 |
| Decisões | D15 (fronteira com G3), D35 |
| Localização | Seção 6.3, parágrafo que começa com "A5 — Algorithmic agenda-setting (alt.: 'trending topics')." |
| Ação | substituir-paragrafo |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
A5 — Algorithmic agenda-setting (alt.: 'trending topics'). Agregação de atividade em massa exibida como pauta coletiva [Gillespie, 16].
```

**Novo texto**

```novo
A4. Algorithmic agenda-setting. The process by which the automated aggregation of user activity, displayed as trending topics, shapes users' perception of which issues the public considers important [16,21]. Agenda-setting research shows that the emphasis an issue receives raises its perceived salience among audiences [21]. On platforms, that emphasis is produced by an algorithm that counts and ranks activity (AF1), and the resulting list is presented as a reflection of collective attention. The list can diverge from what most users actually discuss: Elmas et al. [54] found that coordinated attacks making topics appear popular accounted for at least 20% of the top ten global trends on Twitter in their data. When divisive topics dominate the displayed agenda, users can overestimate how central conflict is to public conversation, which points to perceived polarization. The fabrication of these popularity signals is treated separately as manufactured consensus (G3).
```

**Justificativa**: a entrada atual tinha uma frase sem processo nem caminho até o outcome
(T02.1-F04). "Trending topics" sai dos alternativos porque é *feature* (R4) e entra na
definição como o que é exibido. McCombs e Shaw [21] (já na lista) dá a base do
agenda-setting, p. 176: "Readers learn not only about a given issue, but also how much importance
to attach to that issue from the amount of information in a news story and its position". Elmas et al. [54], abstract: "Trends astroturfed by these
attacks account for at least 20% of the top 10 global trends". A fronteira com G3 segue a D15.
O outcome continua perceived e o rating "Plausible".

---

### Conferência das regras de estilo (lote 1)

Travessão: nenhum no texto novo. Ponto e vírgula: nenhum. Aspas em termos em inglês: nenhuma
(as aspas da v1 em *alt.* saíram). Texto em inglês. Conferido contra a lista de marcas de
texto gerado por IA de `manuscripts/CLAUDE.md`.

# Lote 2 — Bloco B, rede, grupo e difusão (aplicado em 2026-10-13)

**Contagem R2 (OpenAlex, 2026-10-13)**: *homophily* 8.314 (*assortative mixing* 488) · *echo
chamber* 2.442 · *group polarization* 999 (*choice shift* 400) · *information cascade* 1.796
(*social contagion* 1.983, outro construto) · *moral contagion* 133 · *partisan sorting* 163
(*social sorting* 392; *mega-identity* 19) · *interpersonal political tension* 1 (termo da fonte,
R1) · *online radicalization* 365 (*radicalization pathway* 82; *alt-right pipeline* 5).
**Numeração das referências**: no trecho original, Isenberg, Vosoughi et al., Del Vicario et al.
e Mason aparecem como [62], [52], [53] e [63]; na lista, são [61], [51], [52] e [62] (P3). O
texto novo usa a numeração da lista.
**Fontes sem PDF**: Sunstein [43] (livro, D-sem-PDF). Vosoughi et al. [51]: só o resumo do MIT
IDE, escrito pelos próprios autores.
**Rótulos em negrito**: aplicados pelo script nas entradas inseridas.

| ID | Localização (âncora) | Ação | Objetivo | Decisões |
|---|---|---|---|---|
| T02-A9 | Título da 6.4, "Bloco B — Estrutura de rede e dinâmica de grupo" | substituir | Novo nome do bloco | D6 |
| T02-A10 | 6.4, abertura, "Este bloco reúne mecanismos cujo insumo comum é a estrutura de conexões…" | substituir-paragrafo | Critério do bloco | D6 |
| T02-A11 | 6.4, "B1 — Homophily…" | substituir-paragrafo | B1, com A3 da v1 incorporado | D21 |
| T02-A12 | 6.4, depois do novo B1 | inserir-apos | B2, câmara de eco (vinda de M1) | D27 |
| T02-A13 | 6.4, "B2 — Group polarization…" | substituir-paragrafo | B3, polarização de grupo | — |
| T02-A14 | 6.4, "B3 — Information cascades…" | substituir-paragrafo | B4, com M4 da v1 incorporado | D14 |
| T02-A15 | 6.4, depois do novo B4 | inserir-apos | B5, *moral contagion* (vinda de C5) | D31 |
| T02-A16 | 6.4, "B4 — Partisan sorting…" | substituir-paragrafo | B6 | D6 |
| T02-A17 | 6.4, "B5 — Interpersonal political tension…" | substituir-paragrafo | B7 | D35 |
| T02-A18 | 6.4, depois do novo B7 | inserir-apos | B8, radicalização em comunidades (vinda de G3) | D32 |
| T02-A19 | 6.2, "M1 — Informational isolation/segregation…" | remover | M1 dividido em A1 e B2 | D27 |
| T02-A20 | 6.2, "M4 — Information disorder…" | remover | M4 fundido em B4 | D14 |
| T02-A21 | 6.5, "C5 — Negativity bias & moral-emotional contagion…" | remover | C5 movido para B5 | D31 |
| T02-A22 | 6.9, "G3 — Radicalization pipeline…" | remover | G3 movido para B8 | D32 |

---

## T02-A9 — Título do bloco B

| Campo | Valor |
|---|---|
| Lote | 2 |
| Achados | T02.1-F05 |
| Decisões | D6 |
| Localização | Seção 6.4, título (só o texto depois de "6.4. ") |
| Ação | substituir |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
Bloco B — Estrutura de rede e dinâmica de grupo
```

**Novo texto**

```novo
Block B. Networks, groups, and diffusion
```

**Justificativa**: o bloco passa a reunir também identidades de grupo e difusão entre usuários
(D6).

---

## T02-A10 — Abertura do bloco B

| Campo | Valor |
|---|---|
| Lote | 2 |
| Achados | T02.1-F05 |
| Decisões | D6 |
| Localização | Seção 6.4, parágrafo 1, começa com "Este bloco reúne mecanismos cujo insumo comum é a estrutura de conexões" |
| Ação | substituir-paragrafo |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
Este bloco reúne mecanismos cujo insumo comum é a estrutura de conexões entre usuários, não a decisão algorítmica individual de exibição — a distinção que justifica separá-lo do Bloco A (Curadoria algorítmica e arquitetura), mesmo quando os dois blocos interagem (como no caso de Connection/friend recommendation (A3) alimentando Homophily (B1)).
```

**Novo texto**

```novo
This block groups the mechanisms that depend on the social structure in which users are embedded: who is connected to whom, which group identities those connections carry, and how content spreads from one user to another. Algorithms can strengthen these processes, as when recommendations favor ties between similar users, but their locus is the network and the groups formed in it rather than an automated selection of content, which separates them from Block A. They also differ from Block C, where the process takes place in the individual's own choice or judgment of information.
```

**Justificativa**: critério pelo locus (D6), com as fronteiras com os blocos A e C. O exemplo da
v1 (A3 alimentando B1) deixa de existir, porque A3 foi fundido em B1 (D21).

---

## T02-A11 — Entrada B1, *homophily*

| Campo | Valor |
|---|---|
| Lote | 2 |
| Achados | T02.1-F03 (alternativo com nome de outcome), T02.1-F04, H06 |
| Decisões | D7 (exemplo de 12.3), D21 |
| Localização | Seção 6.4, parágrafo que começa com "B1 — Homophily (alt.: 'assortative mixing', 'network segregation')." |
| Ação | substituir-paragrafo |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
B1 — Homophily (alt.: 'assortative mixing', 'network segregation'). McPherson et al. [37] estabelecem a homofilia como um dos princípios mais robustos de formação de redes sociais.
```

**Novo texto**

```novo
B1. Homophily (alt. assortative mixing). The tendency of similar people to form ties at a higher rate than dissimilar people [37]. On social media, it shapes whom users follow and keep in their networks, and connection recommendations based on network similarity can strengthen it (AF2, AF3). In simulations, Santos et al. [59] found that preferentially linking structurally similar users promotes opinion polarization by producing networks with well-defined communities, even without any opinion-based choice, while connecting dissimilar users moderates opinions. Recommenders retrained on data already shaped by earlier recommendations form a feedback loop that homogenizes user behavior [58]. Repeated homophilous tie formation sorts users into politically homogeneous clusters, which is the network segregation measured as structural polarization (Section 2.2).
```

**Justificativa**: responde à H06 (faltava dizer o que é homofilia). Definição de McPherson et al.
[37], p. 416: "Homophily is the principle that a contact between similar people occurs at a
higher rate than among dissimilar people". Incorpora A3 da v1 (D21): Santos et al. [59], p. 1
(abstract): "preferentially establishing links with structurally similar nodes potentiates
opinion polarization by stimulating network topologies with well-defined communities (even in
the absence of opinion-based rewiring)" e "connecting structurally dissimilar nodes enhances
moderate opinions"; Chaney et al. [58] (abstract): "this creates a pernicious feedback loop" que
"homogenizes user behavior". "Network segregation" sai dos alternativos (nome do outcome,
T02.1-F03).

---

## T02-A12 — Nova entrada B2, *echo chamber*

| Campo | Valor |
|---|---|
| Lote | 2 |
| Achados | H01, T02.1-F03 |
| Decisões | D27 |
| Localização | Seção 6.4, logo depois do novo B1 (aplicar T02-A11 antes) |
| Ação | inserir-apos |
| Estado | aplicado em 2026-10-13 |

**Âncora** (fim do texto novo de T02-A11)

```ancora
which is the network segregation measured as structural polarization (Section 2.2).
```

**Novo texto**

```novo
B2. Echo chamber. The reinforcement of users' opinions through repeated interaction with peers and sources that share them [43,46]. Echo chambers form inside homophilous networks (B1) and are sustained by the bias of information diffusion toward like-minded users. Comparing Facebook, Twitter, Reddit, and Gab, Cinelli et al. [46] found that the aggregation of users in homophilic clusters dominates online dynamics, with higher segregation on Facebook than on Reddit. Inside such clusters, users mostly meet content that confirms what they already believe, which can harden positions and deepen the separation between groups, with effects on ideological and structural polarization. The echo chamber differs from the filter bubble (A1), where the narrowing comes from algorithmic selection, and from group polarization (B3), which concerns the shift of positions after discussion among like-minded people.
```

**Justificativa**: metade de M1 que fica no bloco B (D27). Definição de Cinelli et al. [46], p. 1:
"environments in which the opinion, political leaning, or belief of users about a topic gets
reinforced due to repeated interactions with peers or sources having similar tendencies and
attitudes". Resultado, mesma página: "the aggregation in homophilic clusters of users dominates
online dynamics. However, a direct comparison of news consumption on Facebook and Reddit shows
higher segregation on Facebook". Sunstein [43] popularizou o termo (livro, D-sem-PDF). As
fronteiras com A1 e B3 são as da D27.

---

## T02-A13 — Entrada B3, *group polarization*

| Campo | Valor |
|---|---|
| Lote | 2 |
| Achados | T02.1-F04 |
| Decisões | — |
| Localização | Seção 6.4, parágrafo que começa com "B2 — Group polarization (alt.: 'choice shift')." |
| Ação | substituir-paragrafo |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
B2 — Group polarization (alt.: 'choice shift'). Deslocamento de posições para mais extremas após deliberação entre semelhantes [Sunstein, 43; Isenberg, 62].
```

**Novo texto**

```novo
B3. Group polarization. The process by which an initial tendency shared by the members of a group is enhanced after group discussion, so that the group ends up more extreme than its members were before [61]. Two explanations dominate the literature: social comparison, in which members shift to match or exceed the position they perceive as valued in the group, and persuasive argumentation, in which discussion exposes members to more arguments for the side already favored. A meta-analysis found that both operate together, with larger effects for persuasive argumentation [61]. Online groups and threads formed around shared views provide the conditions the process needs, namely like-minded members and a steady flow of arguments for one side [43]. The process moves positions toward the extremes and acts on ideological polarization. The evidence is strong in laboratory settings and more limited online.
```

**Justificativa**: definição de Isenberg [61], p. 1141: "Group polarization is said to occur when
an initial tendency of individual group members toward a given direction is enhanced following
group discussion". Mesma página: os dois mecanismos explicativos e o resultado da meta-análise,
"social comparison and persuasive argumentation occur in combination to produce polarization,
although the persuasive argumentation effects tend to be larger". "Choice shift" sai dos
alternativos: Isenberg trata os *shifts* como "special cases" do fenômeno (R6). A última frase
reproduz o rating da tabela ("Strong (lab); moderate (online)"). Sunstein [43]: D-sem-PDF.

---

## T02-A14 — Entrada B4, *information cascades*

| Campo | Valor |
|---|---|
| Lote | 2 |
| Achados | T02.1-F02 (M4), H04 |
| Decisões | D14, D33 (*herding* vai para D2) |
| Localização | Seção 6.4, parágrafo que começa com "B3 — Information cascades (alt.: 'herding', 'social contagion')." |
| Ação | substituir-paragrafo |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
B3 — Information cascades (alt.: 'herding', 'social contagion'). Repasse de informação sem checagem individual, baseado na inferência de credibilidade a partir do volume de compartilhamento prévio [Vosoughi et al., 52; Del Vicario et al., 53].
```

**Novo texto**

```novo
B4. Information cascades. The spread of content through chains of sharing in which each user passes information on because others have already shared it, rather than after an independent check of its accuracy. Sharing takes a single action and share counts are visible (AF4, AF5), so cascades can reach large audiences quickly, and false content travels as easily as true content. Vosoughi et al. [51] found that false news on Twitter diffused significantly farther, faster, deeper, and more broadly than true news, with the strongest effects for false political news. On Facebook, Del Vicario et al. [52] found that selective exposure drives diffusion within homogeneous clusters, each with its own cascade dynamics. The cascades of misinformation described here, false content shared without intent to deceive, differ from disinformation spread deliberately by coordinated actors, which is treated as manufactured consensus (G3). By circulating unverified claims within like-minded clusters, the mechanism acts on ideological and perceived polarization.
```

**Justificativa**: incorpora M4 da v1 (D14), com a distinção *misinformation* × *disinformation*
pedida na H04. Vosoughi et al. [51], pelo resumo dos autores (MIT IDE): "Falsehood diffused
significantly farther, faster, deeper, and more broadly than the truth in all categories. The
effects were most pronounced for false political news". Del Vicario et al. [52], p. 554:
"Selective exposure to content is the primary driver of content diffusion and generates the
formation of homogeneous clusters", e "each echo chamber has its own cascade dynamics". *Herding*
vai para D2 (Muchnik, D33). *Social contagion* sai: é outro construto (R6).

---

## T02-A15 — Nova entrada B5, *moral contagion*

| Campo | Valor |
|---|---|
| Lote | 2 |
| Achados | T02.1-F05 (C5 fora do bloco), O06 |
| Decisões | D31 |
| Localização | Seção 6.4, logo depois do novo B4 (aplicar T02-A14 antes) |
| Ação | inserir-apos |
| Estado | aplicado em 2026-10-13 |

**Âncora** (fim do texto novo de T02-A14)

```ancora
the mechanism acts on ideological and perceived polarization.
```

**Novo texto**

```novo
B5. Moral contagion. The greater spread of messages that express moral emotions. Brady et al. [67] named the process after finding that each additional moral-emotional word in a message increased its diffusion by about 20%, an effect bounded by group membership: moral-emotional language increased diffusion more within liberal and within conservative networks than between them. Content about the political out-group spreads even further. In posts by news media and members of the U.S. Congress, out-group language was the strongest predictor of shares, about 4.8 times as strong as negative affect language and 6.7 times as strong as moral-emotional language [38]. The mechanism describes a human sharing preference that keeps moralized and hostile content circulating inside each camp, and it acts mainly on affective polarization. It is the preference that engagement-based ranking learns and amplifies (A2), and it differs from the social learning of outrage (E1), which concerns the authors rewarded for expressing it.
```

**Justificativa**: C5 da v1, reformulado como *moral contagion* e movido para o bloco B (D31).
Brady et al. [67], p. 7313: "a process we call 'moral contagion'", "increased their diffusion by
a factor of 20% for each additional word" e "moral contagion was bounded by group membership".
Rathje et al. [38], p. 1: "the average effect size of out-group language was about 4.8 times as
strong as that of negative affect language and about 6.7 times as strong as that of
moral-emotional language", em posts de "news media accounts and US congressional members"
(D31: Rathje passa para esta entrada). Fronteiras com A2 e E1 da D31.

---

## T02-A16 — Entrada B6, *partisan sorting*

| Campo | Valor |
|---|---|
| Lote | 2 |
| Achados | T02.1-F04, T02.1-F05 |
| Decisões | D6 (B4 da v1 fica em B) |
| Localização | Seção 6.4, parágrafo que começa com "B4 — Partisan sorting (alt.: 'social sorting', 'mega-identity')." |
| Ação | substituir-paragrafo |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
B4 — Partisan sorting (alt.: 'social sorting', 'mega-identity'). Mason [63] mostra que o alinhamento de múltiplas identidades sociais (partido, religião, estilo de vida) aumenta a polarização afetiva mesmo sem extremismo de posições.
```

**Novo texto**

```novo
B6. Partisan sorting (alt. partisan-ideological sorting). The alignment of partisan and ideological identities, through which each party becomes a more homogeneous social group [62]. Mason [62] found that this alignment strengthens partisan identity and increases partisan bias, activism, and anger even when issue positions do not polarize to the same degree. Platforms can make the alignment more visible, since profiles, communities, and shared content bundle political and cultural cues (AF11), although direct evidence of this amplification is limited. The mechanism acts on affective polarization: the other party comes to be seen as a distinct social group rather than as people who disagree on some issues.
```

**Justificativa**: Mason [62], p. 128 (abstract): "Social polarization, characterized by increased
levels of partisan bias, activism, and anger, is increasing, driven by partisan identity and
political identity alignment, and does not require the same magnitude of issue position
polarization", e "The partisan-ideological sorting that has occurred in recent decades has
caused the nation as a whole to hold more aligned political identities". A v1 atribuía a Mason
[62] o alinhamento de "partido, religião, estilo de vida" e o termo *mega-identity*, que não
estão neste artigo (são de trabalhos posteriores da autora, fora da lista [conhecimento do agente; conferir]). Por isso saem
*social sorting* e *mega-identity*, e entra o termo do artigo, *partisan-ideological sorting*.
O papel da plataforma é declarado como plausível (Claim "Hosts (amplifies)").

---

## T02-A17 — Entrada B7, *interpersonal political tension*

| Campo | Valor |
|---|---|
| Lote | 2 |
| Achados | H07, O06 |
| Decisões | D35 |
| Localização | Seção 6.4, parágrafo que começa com "B5 — Interpersonal political tension & identity salience activation." |
| Ação | substituir-paragrafo |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
B5 — Interpersonal political tension & identity salience activation. Mecanismo introduzido neste artigo com base em Tanyel and Windeler [5], que demonstram, em dois levantamentos (N = 2.820 e N = 492), que a visibilidade de desacordo político em conexões existentes gera tensão interpessoal que eleva a saliência da identidade política, contribuindo para polarização afetiva independentemente de mudança na posição ideológica substantiva.
```

**Novo texto**

```novo
B7. Interpersonal political tension. The strain that visible political disagreement places on existing relationships, which in turn raises the salience of political identity [5]. Tanyel and Windeler [5] proposed and tested this sequence with a survey of 2,820 Facebook and Twitter users and a second survey of 492 users: tension around differences in values triggers an us-versus-them awareness that leads to more positive attitudes toward the in-group and more negative attitudes toward the out-group. On social media, the low segmentation of audiences (AF6) keeps the political views of friends, relatives, and colleagues visible and recurrent, and asymmetric following (AF3) shapes which disagreeing ties stay in view. The mechanism acts on affective polarization. It differs from homophily (B1), which concerns which ties are formed, because here the disagreeing ties already exist and are kept.
```

**Justificativa**: responde à H07 (mecanismo incompreensível) com a cadeia passo a passo (D35).
Tanyel e Windeler [5], abstract: "the mechanisms that link social media use to polarization:
interpersonal political tension and political identity salience", com 2.820 e 492
respondentes; Study 1: "These differences trigger an 'us versus them' awareness through
heightened identity salience, leading to more positive ingroup and more negative outgroup
attitudes". A afirmação da v1 de que o efeito ocorre "independentemente de mudança na posição
ideológica substantiva" sai, porque não foi localizada no PDF. A relação com AF6 segue a
redefinição da D22 (segmentação de audiência).

---

## T02-A18 — Nova entrada B8, radicalização em comunidades online

| Campo | Valor |
|---|---|
| Lote | 2 |
| Achados | T02.1-F05 (G3 fora do bloco) |
| Decisões | D32 |
| Localização | Seção 6.4, logo depois do novo B7 (aplicar T02-A17 antes) |
| Ação | inserir-apos |
| Estado | aplicado em 2026-10-13 |

**Âncora** (fim do texto novo de T02-A17)

```ancora
because here the disagreeing ties already exist and are kept.
```

**Novo texto**

```novo
B8. Online community radicalization. The gradual movement of individuals toward extremist views through participation in online communities and media environments that progressively normalize those views [76]. Drawing on video testimonies and chat logs, Munn [76] argued that people are not converted at once but incrementally nudged along a pathway, and described three overlapping cognitive phases in this journey: normalization, acclimation, and dehumanization. Platforms enable the process through group and community formation (AF11), which gives fringe communities persistent spaces with their own norms. The mechanism acts on ideological polarization and, through dehumanization, on affective polarization. Together with algorithmic radicalization (A3), it forms what the literature calls the radicalization pipeline, here split into a community route and an algorithmic route.
```

**Justificativa**: G3 da v1, renomeado pelo processo e movido para o bloco B (D32). Munn [76], p. 1:
"Alt-righters are not instantly converted, but rather incrementally nudged along a particular
medial pathway", e "three overlapping cognitive phases that occur within this journey:
normalization, acclimation, and dehumanization". Nome pela R2: *online radicalization* é o termo
corrente (365), e o qualificador *community* marca a via (D32). O outcome affective é
acrescentado (D32).

---

## T02-A19 — Remoção da entrada M1 da v1

| Campo | Valor |
|---|---|
| Lote | 2 |
| Achados | T02.1-F03, H01 |
| Decisões | D27 |
| Localização | Seção 6.2, parágrafo que começa com "M1 — Informational isolation/segregation" |
| Ação | remover |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
M1 — Informational isolation/segregation (alt.: 'echo chamber', 'filter bubble', 'epistemic bubble'). Fusão de câmara de eco e bolha de filtro — dois processos com causas distintas (escolha social vs. curadoria algorítmica) mas efeito convergente de isolamento informacional [Sunstein, 43; Pariser, 44]. Bakshy et al. [39] encontram que, no Facebook, as escolhas individuais pesam mais que o algoritmo na redução de exposição cruzada; Cinelli et al. [40] documentam o efeito em múltiplas plataformas, com intensidade variável.
```

**Justificativa**: M1 foi dividido em A1 (bolha de filtro, lote 1) e B2 (câmara de eco, T02-A12). O
texto fica riscado.

---

## T02-A20 — Remoção da entrada M4 da v1

| Campo | Valor |
|---|---|
| Lote | 2 |
| Achados | T02.1-F02 |
| Decisões | D14 |
| Localização | Seção 6.2, parágrafo que começa com "M4 — Information disorder" |
| Ação | remover |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
M4 — Information disorder (alt.: 'misinformation/disinformation', 'fake news'). Circulação de conteúdo falso ou enganoso. Vosoughi et al. [52] mostram que notícias falsas se difundem mais rápido e mais amplamente que notícias verdadeiras no Twitter; Del Vicario et al. [53] mostram que essa difusão ocorre predominantemente dentro de clusters homogêneos.
```

**Justificativa**: fundido em B4 (T02-A14).

---

## T02-A21 — Remoção da entrada C5 da v1

| Campo | Valor |
|---|---|
| Lote | 2 |
| Achados | T02.1-F05 |
| Decisões | D31 |
| Localização | Seção 6.5, parágrafo que começa com "C5 — Negativity bias & moral-emotional contagion" |
| Ação | remover |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
C5 — Negativity bias & moral-emotional contagion (alt.: 'moral contagion'). Brady et al. [67] mostram que palavras moral-emocionais aumentam a difusão de mensagens, sobretudo dentro do mesmo grupo ideológico.
```

**Justificativa**: movido para B5 (T02-A15).

---

## T02-A22 — Remoção da entrada G3 da v1

| Campo | Valor |
|---|---|
| Lote | 2 |
| Achados | T02.1-F05 |
| Decisões | D32 |
| Localização | Seção 6.9, parágrafo que começa com "G3 — Radicalization pipeline" |
| Ação | remover |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
G3 — Radicalization pipeline (alt.: 'fringe community pathway'). Munn [76] descreve trajetórias individuais graduais para o extremismo em comunidades online fechadas.
```

**Justificativa**: movido para B8 (T02-A18).

---

### Conferência das regras de estilo (lote 2)

Feita pelo script de conferência antes do registro (travessão, ponto e vírgula, aspas em termos,
marcas de texto gerado por IA).

# Lote 3 — Bloco C, seleção e processamento individual da informação (aplicado em 2026-10-13)

**Contagem R2 (OpenAlex, 2026-10-13)**: *motivated reasoning* 2.322 (*identity-protective
cognition* 89) · *confirmation bias* 5.919 (*myside bias* 157) · *selective avoidance* 239
(*selective exposure* 2.350) · *biased assimilation* 145 (*disconfirmation bias* 43) · *hostile
media effect* 129 (*hostile media phenomenon* 34) · *illusory truth effect* 218 (*truth effect*
449, mais genérico) · *news avoidance* 315 (*news fatigue* 54, uma causa, não sinônimo).
**Referências novas (D2; aprovação do usuário em 2026-10-13)**: Garrett 2009 [107], Heseltine et
al. 2025 [108] e Urman 2019 [109], acrescentadas ao fim da lista (T02-A37). PDFs em
`references/` e no tema `areas/mestrado/smip-paper/exposicao-seletiva/`.
**Numeração**: no trecho original, Kunda aparece como [49]; na lista, é [63] (P3).
**Fontes sem PDF**: Festinger [47] (livro, D-sem-PDF); Skovsgaard e Andersen [80] (só abstract,
D-sem-PDF).
**C8 (reinforcing spiral, M6 da v1)**: não entra neste lote. Fica como está na Seção 6.2 até a
revisão do backlog B02 (D16).

| ID | Localização (âncora) | Ação | Objetivo | Decisões |
|---|---|---|---|---|
| T02-A23 | Título da 6.5, "Bloco C — Micro-fundamentos cognitivos" | substituir | Novo nome do bloco | D6 |
| T02-A24 | 6.5, abertura, "Este bloco reúne vieses cognitivos individuais…" | substituir-paragrafo | Critério do bloco | D6, T02.1-F05 |
| T02-A25 | 6.5, "C1 — Motivated reasoning…" | substituir-paragrafo | C1, o motivo | D26 |
| T02-A26 | 6.5, depois do novo C1 | inserir-apos | C2, viés de confirmação (vindo de M2) | D26, D35, H02 |
| T02-A27 | 6.5, depois do novo C2 | inserir-apos | C3, evitação seletiva (vinda de H2) | D34 |
| T02-A28 | 6.5, "C2 — Biased assimilation…" | substituir-paragrafo | C4, a avaliação | D26 |
| T02-A29 | 6.5, "C3 — Hostile media effect…" | substituir-paragrafo | C5 | — |
| T02-A30 | 6.5, "C4 — Illusory truth effect…" | substituir-paragrafo | C6 | — |
| T02-A31 | 6.5, depois do novo C6 | inserir-apos | C7, evitação de notícias (vinda de H1) | D34 |
| T02-A32 | 6.2, "M2 — Confirmation bias / myside bias…" | remover | M2 movido para C2 | D26 |
| T02-A33 | Título da 6.10, "Bloco H — Evitação e desengajamento informacional" | remover | Bloco H dissolvido | D6 |
| T02-A34 | 6.10, abertura, "Este bloco reúne mecanismos comportamentais de fuga…" | remover | Bloco H dissolvido | D6 |
| T02-A35 | 6.10, "H1 — News avoidance…" | remover | H1 movido para C7 | D34 |
| T02-A36 | 6.10, "H2 — Selective/partisan news avoidance…" | remover | H2 movido para C3 | D34 |
| T02-A37 | Referências, depois do item 106 (Napoli) | inserir-apos | Itens 107–109 | D2 |

---

## T02-A23 — Título do bloco C

| Campo | Valor |
|---|---|
| Lote | 3 |
| Achados | T02.1-F05 |
| Decisões | D6 |
| Localização | Seção 6.5, título (só o texto depois de "6.5. ") |
| Ação | substituir |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
Bloco C — Micro-fundamentos cognitivos
```

**Novo texto**

```novo
Block C. Individual selection and processing of information
```

**Justificativa**: o bloco passa a reunir a escolha e o julgamento individual da informação, o que
inclui a evitação (D6, D34).

---

## T02-A24 — Abertura do bloco C

| Campo | Valor |
|---|---|
| Lote | 3 |
| Achados | T02.1-F05 |
| Decisões | D6 |
| Localização | Seção 6.5, parágrafo 1, começa com "Este bloco reúne vieses cognitivos individuais" |
| Ação | substituir-paragrafo |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
Este bloco reúne vieses cognitivos individuais que antecedem a mídia social e são, por definição, predominantemente hospedados (não criados ou amplificados) por ela — a justificativa para tratá-los separadamente dos mecanismos de design.
```

**Novo texto**

```novo
This block groups the mechanisms that take place in the individual's own choice or judgment of information: the motive behind processing, the selection of sources, the avoidance of news, and the evaluation and memory of what is encountered. Most of these processes predate social media, and platforms mainly change how often they are triggered rather than how they work, although repetition and choice at scale can amplify some of them. The block differs from Block D, which concerns beliefs about what others think, and from Block B, where the process depends on the network rather than on the individual.
```

**Justificativa**: a abertura da v1 dizia que esses mecanismos são "hospedados (não criados ou
amplificados)", o que contradizia o *Claim* "Amplifies" de C4 da v1 (T02.1-F05). O critério
passa a ser o locus (D6), com as fronteiras com os blocos B e D.

---

## T02-A25 — Entrada C1, *motivated reasoning*

| Campo | Valor |
|---|---|
| Lote | 3 |
| Achados | H08, T02.1-F04 |
| Decisões | D26 |
| Localização | Seção 6.5, parágrafo que começa com "C1 — Motivated reasoning (alt.: 'identity-protective cognition')." |
| Ação | substituir-paragrafo |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
C1 — Motivated reasoning (alt.: 'identity-protective cognition'). Kunda [49] descreve como a motivação por conclusões desejadas leva a uso seletivo da razão; Taber and Lodge [64] documentam ceticismo motivado no domínio político.
```

**Novo texto**

```novo
C1. Motivated reasoning. The influence of a desired conclusion on how people access, construct, and evaluate beliefs [63]. Kunda [63] distinguished accuracy goals from directional goals and argued that directional goals bias reasoning, within the limits of the justifications people can construct for the conclusions they want. In the political domain, Taber and Lodge [64] found that people rate congruent arguments as stronger, counterargue contrary ones, and seek out confirming sources, and that these biases strengthen attitudes, especially among those with the strongest priors and the highest political sophistication. Motivated reasoning is the motive that drives the search stage (C2) and the evaluation stage (C4). These stages are listed separately because they act at different points of processing and because confirmation bias can also occur without motivation [48]. Platforms host the process: they do not create the motive, but their constant supply of political claims gives it frequent occasions to operate. The main effect is on ideological polarization.
```

**Justificativa**: responde à H08 (diferença entre C1 e viés de confirmação), conforme a D26.
Kunda [63], p. 480: "motivation may affect reasoning through reliance on a biased set of
cognitive processes: strategies for accessing, constructing, and evaluating beliefs", e a
capacidade de chegar à conclusão desejada "is constrained by their ability to construct
seemingly reasonable justifications". Taber e Lodge [64], p. 755: "prior attitude effect",
"disconfirmation bias", "confirmation bias" e polarização de atitudes "especially among those
with the strongest priors and highest levels of political sophistication". Nickerson [48], p.
176: "motivated and unmotivated forms of confirmation bias". *Identity-protective cognition* sai
dos alternativos: é um caso particular, de fonte fora da lista (R6). Corrige a numeração de
Kunda.

---

## T02-A26 — Nova entrada C2, *confirmation bias*

| Campo | Valor |
|---|---|
| Lote | 3 |
| Achados | H02, H08, T02.1-F05 (M2 fora do bloco) |
| Decisões | D26, D35 |
| Localização | Seção 6.5, logo depois do novo C1 (aplicar T02-A25 antes) |
| Ação | inserir-apos |
| Estado | aplicado em 2026-10-13 |

**Âncora** (fim do texto novo de T02-A25)

```ancora
The main effect is on ideological polarization.
```

**Novo texto**

```novo
C2. Confirmation bias (alt. myside bias). The tendency to seek out evidence that supports existing beliefs, which Nickerson [48] describes as a usually unwitting selectivity in the acquisition and use of evidence. In this taxonomy, the term covers the search stage, that is, which sources and arguments a person chooses to consult. Its behavioral manifestation is selective exposure to congenial information, classically explained by the wish to avoid the discomfort of cognitive dissonance [47]. Taber and Lodge [64] observed the bias when participants were free to choose the sources they read, and Garrett [107] found that Americans used the control afforded by online sources to increase their exposure to views consistent with their own. Platforms widen the room for this selection by offering many sources and easy ways to filter them. Confirmation bias differs from motivated reasoning (C1), which is the motive, from biased assimilation (C4), which concerns how evidence already encountered is weighed, and from selective avoidance (C3), the avoidance of challenging content.
```

**Justificativa**: M2 da v1, movido para o bloco C e restrito à busca (D26). Nickerson [48], p.
175: "unwitting selectivity in the acquisition and use of evidence". Taber e Lodge [64], p. 755:
"a confirmation bias, the seeking out of confirmatory evidence when Ps are free to self-select
the source". Garrett [107], p. 676: "Americans use the control afforded by online information
sources to increase their exposure to opinions consistent with their own views". *Myside bias*
entra como alternativo (H02; R2: 157 trabalhos). *Selective exposure* passa para a definição como
manifestação comportamental, e *motivated dissonance avoidance* sai, com Festinger [47] citado
na definição (D-sem-PDF).

---

## T02-A27 — Nova entrada C3, *selective avoidance*

| Campo | Valor |
|---|---|
| Lote | 3 |
| Achados | T02.2-F04, T02.2-F05 |
| Decisões | D34 |
| Localização | Seção 6.5, logo depois do novo C2 (aplicar T02-A26 antes) |
| Ação | inserir-apos |
| Estado | aplicado em 2026-10-13 |

**Âncora** (fim do texto novo de T02-A26)

```ancora
and from selective avoidance (C3), the avoidance of challenging content.
```

**Novo texto**

```novo
C3. Selective avoidance (alt. partisan selective avoidance). The avoidance of content, sources, and contacts that challenge one's political views. It is distinct from confirmation bias (C2): Garrett [107] found that people seek opinion-reinforcing information without systematically avoiding opinion challenges, so that seeking and avoiding are not two sides of the same behavior. Avoidance does occur and varies over time. Using about 27.6 million visits to news sites, Heseltine et al. [108] found that partisans change the volume, type, and source of the news they consume when news sentiment toward their own or the other party changes, with asymmetries between parties. On social media, avoidance can also take the form of cutting ties, since asymmetric following (AF3) lets users unfollow or unfriend disagreeing contacts at low cost. The evidence is mixed, and the link to polarization remains theoretical: by narrowing exposure and removing disagreeing ties, avoidance can reinforce attitudes and feed the network separation described by the echo chamber (B2).
```

**Justificativa**: H2 da v1, reformulado como evitação seletiva (D34) e com as fontes corretas. As
atribuições a Toff e Kalogeropoulos [79] e a Skovsgaard e Andersen [80] saem (T02.2-F04, F05).
Garrett [107], p. 676: "people exhibit a preference for opinion-reinforcing political
information without systematically avoiding opinion challenges", o que "contradicts the common
assumption that reinforcement seeking and challenge avoidance are intrinsically linked".
Heseltine et al. [108], p. 1541: "partisans alter the volume, type, and source of news because of
changing news sentiment" e "partisan asymmetries emerge", com 27.648.770 visitas; o elo com a
polarização é proposto, não testado (p. 1556). A ligação com AF3 é a que a Seção 5.1 já faz
("exploits low-friction disconnection to prune disagreement").

---

## T02-A28 — Entrada C4, *biased assimilation*

| Campo | Valor |
|---|---|
| Lote | 3 |
| Achados | H08 |
| Decisões | D26 |
| Localização | Seção 6.5, parágrafo que começa com "C2 — Biased assimilation (alt.: 'disconfirmation bias')." |
| Ação | substituir-paragrafo |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
C2 — Biased assimilation (alt.: 'disconfirmation bias'). Lord et al. [65] mostram que a mesma evidência mista reforça crenças opostas em grupos opostos.
```

**Novo texto**

```novo
C4. Biased assimilation (alt. disconfirmation bias). The tendency to accept evidence that supports one's position at face value while subjecting contrary evidence to critical scrutiny [65]. Lord et al. [65] showed that when proponents and opponents of a policy read the same mixed evidence, their evaluations and beliefs shifted in opposite directions, so that the net effect was an increase in attitude polarization. Taber and Lodge [64] call the counterarguing of contrary arguments a disconfirmation bias and found that it, too, leads to attitude polarization. Social media supply this bias with material, since users do meet cross-cutting content: on Facebook, between about a quarter and a third of the hard news shared by users' friends came from the other side [45]. The mechanism acts on ideological polarization. It differs from confirmation bias (C2), which concerns which evidence is sought, because it concerns how evidence already encountered is weighed.
```

**Justificativa**: Lord et al. [65], p. 2098: "They are apt to accept 'confirming' evidence at face
value while subjecting 'disconfirming' evidence to critical evaluation", e "The net effect of such
evaluations and opinion shifts was the postulated increase in attitude polarization". Taber e
Lodge [64], p. 755: "disconfirmation bias" e "Both the confirmation and disconfirmation biases
lead to attitude polarization". Bakshy et al. [45], p. 1130: "24% are cross-cutting" para os
liberais e "35% for conservatives". Fronteira com C2 conforme a D26.

---

## T02-A29 — Entrada C5, *hostile media effect*

| Campo | Valor |
|---|---|
| Lote | 3 |
| Achados | T02.1-F04 |
| Decisões | — |
| Localização | Seção 6.5, parágrafo que começa com "C3 — Hostile media effect." |
| Ação | substituir-paragrafo |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
C3 — Hostile media effect. Vallone et al. [23] mostram que partidários de lados opostos percebem a mesma cobertura como enviesada contra si.
```

**Novo texto**

```novo
C5. Hostile media effect (alt. hostile media phenomenon). The tendency of partisans on opposite sides to perceive the same news coverage as biased against their own side [23]. After viewing identical television coverage of the Beirut massacre, both pro-Israeli and pro-Arab partisans rated it as biased against them, reported more negative references to their side, and predicted that it would sway neutral viewers in a hostile direction. Greater knowledge of the issue was associated with stronger perceptions of bias [23]. The effect predates social media, which host it rather than create it. By leading each side to see mainstream coverage as favoring the other, the mechanism can feed distrust of the media and resentment toward the out-group, with effects on affective polarization.
```

**Justificativa**: Vallone et al. [23], p. 577: "both pro-Israeli and pro-Arab partisans rated these
programs […] as being biased against their side"; "each group reported more negative references
to their side than positive ones, and each predicted that the coverage would sway nonpartisans in
a hostile direction"; "greater knowledge of the crisis was associated with stronger perceptions of
media bias". *Hostile media phenomenon*, o termo da fonte, entra como alternativo (R1); o nome
principal fica com o termo mais recorrente (R2).

---

## T02-A30 — Entrada C6, *illusory truth effect*

| Campo | Valor |
|---|---|
| Lote | 3 |
| Achados | T02.1-F04 |
| Decisões | — |
| Localização | Seção 6.5, parágrafo que começa com "C4 — Illusory truth effect (alt.: 'truth effect')." |
| Ação | substituir-paragrafo |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
C4 — Illusory truth effect (alt.: 'truth effect'). Hasher et al. [66] mostram que afirmações repetidas parecem mais verdadeiras, independentemente de sua veracidade.
```

**Novo texto**

```novo
C6. Illusory truth effect (alt. truth effect). The increase in the perceived truth of a statement that comes from repeated exposure to it, regardless of whether it is true. Hasher et al. [66] found that statements repeated across sessions received higher validity ratings, for both true and false statements, while ratings of nonrepeated statements did not change, and concluded that frequency of occurrence is used as a criterion of validity. Social media can amplify the effect, because reshares, cascades (B4), and repeated recommendations expose users to the same claims many times. Repeated partisan claims, false ones included, can then come to seem true to those who see them most often, with effects on ideological and perceived polarization.
```

**Justificativa**: Hasher et al. [66], p. 107: "For both true and false statements, there was a
significant increase in the validity judgments for the repeated statements and no change in the
validity judgments for the nonrepeated statements. Frequency of occurrence is apparently a
criterion used to establish the referential validity of plausible statements". O *Claim*
"Amplifies" da v1 passa a ter o mecanismo explícito (repetição por compartilhamento, cascatas e
recomendação).

---

## T02-A31 — Nova entrada C7, *news avoidance*

| Campo | Valor |
|---|---|
| Lote | 3 |
| Achados | T02.2-F04, T02.2-F05, O09, O10 |
| Decisões | D34 |
| Localização | Seção 6.5, logo depois do novo C6 (aplicar T02-A30 antes) |
| Ação | inserir-apos |
| Estado | aplicado em 2026-10-13 |

**Âncora** (fim do texto novo de T02-A30)

```ancora
with effects on ideological and perceived polarization.
```

**Novo texto**

```novo
C7. News avoidance. The avoidance of news in general, which can be intentional, when people tune out because of how news is selected and presented, or unintentional, when the media environment offers few chances for inadvertent exposure [80]. In a fragmented digital environment where news is often met passively in feeds, active avoidance gains weight in shaping who stays informed [79]. Across more than 67,000 respondents in 35 countries, Toff and Kalogeropoulos [79] found that avoidance is predicted by individual factors, with only a small effect of ideology, and that press freedom, political freedom, and stability reduce it. The link to polarization is indirect and plausible rather than demonstrated: when most users avoid news, the attentive public that remains is smaller and more partisan. On the Russian platform Vkontakte, Urman [109] found a politically apathetic majority and a news-interested minority polarized along political lines.
```

**Justificativa**: H1 da v1, com as fontes reancoradas (D34). Skovsgaard e Andersen [80], abstract
(D-sem-PDF): "a model distinguishing two types of news avoidance, intentional and
unintentional", com soluções na "news selection and news presentation" e nas "opportunity
structures provided in the media system" para a exposição inadvertida. Toff e Kalogeropoulos
[79], p. 366: o ambiente em que a notícia é "encountered passively in social media feeds" e o
efeito negativo de "press freedom and political freedom and stability"; p. 379: efeito da
ideologia d = −0,09. Urman [109], p. 5158: "a politically apathetic majority and news-interested
minority" e "news subscribers are polarized along political lines" (contexto autoritário,
desenho transversal: apoio de plausibilidade). A afirmação da v1 de que Toff e Kalogeropoulos
mostram o privilégio de notícias alinhadas às crenças sai (T02.2-F04). *News fatigue* sai dos
alternativos (é uma causa, R6).

---

## T02-A32 — Remoção da entrada M2 da v1

| Campo | Valor |
|---|---|
| Lote | 3 |
| Achados | T02.1-F05 |
| Decisões | D26 |
| Localização | Seção 6.2, parágrafo que começa com "M2 — Confirmation bias / myside bias" |
| Ação | remover |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
M2 — Confirmation bias / myside bias (alt.: 'selective exposure', 'motivated dissonance avoidance'). Tendência a buscar e privilegiar informação que confirma crenças prévias, reduzindo o desconforto da dissonância cognitiva [Festinger, 47; Nickerson, 48]. É predominantemente hospedado, não criado, pelas plataformas — o fenômeno antecede a mídia social em décadas de pesquisa psicológica.
```

**Justificativa**: movido para C2 (T02-A26).

---

## T02-A33 — Remoção do título do bloco H

| Campo | Valor |
|---|---|
| Lote | 3 |
| Achados | T02.1-F05 |
| Decisões | D6 |
| Localização | Seção 6.10, título (só o texto depois de "6.10. "; a numeração muda na T02.5) |
| Ação | remover |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
Bloco H — Evitação e desengajamento informacional
```

**Justificativa**: o bloco H foi dissolvido (D6). H1 e H2 foram para C7 e C3.

---

## T02-A34 — Remoção da abertura do bloco H

| Campo | Valor |
|---|---|
| Lote | 3 |
| Achados | T02.1-F05 |
| Decisões | D6 |
| Localização | Seção 6.10, parágrafo 1, começa com "Este bloco reúne mecanismos comportamentais de fuga" |
| Ação | remover |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
Este bloco reúne mecanismos comportamentais de fuga, não de exposição — o espelho dos mecanismos de exposição seletiva do Bloco M (Mecanismos transversais), justificando tratamento como bloco próprio em vez de subsumi-los sob Confirmation bias / myside bias (M2).
```

**Justificativa**: bloco dissolvido (D6).

---

## T02-A35 — Remoção da entrada H1 da v1

| Campo | Valor |
|---|---|
| Lote | 3 |
| Achados | T02.2-F04 |
| Decisões | D34 |
| Localização | Seção 6.10, parágrafo que começa com "H1 — News avoidance" |
| Ação | remover |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
H1 — News avoidance (alt.: 'news fatigue'). Toff and Kalogeropoulos [79] documentam como a prática de consumo de notícias privilegia o que já se alinha a crenças prévias, inclusive por meio da evitação completa.
```

**Justificativa**: movido para C7 (T02-A31), com as fontes corrigidas.

---

## T02-A36 — Remoção da entrada H2 da v1

| Campo | Valor |
|---|---|
| Lote | 3 |
| Achados | T02.2-F04, T02.2-F05 |
| Decisões | D34 |
| Localização | Seção 6.10, parágrafo que começa com "H2 — Selective/partisan news avoidance" |
| Ação | remover |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
H2 — Selective/partisan news avoidance (alt.: 'checked-out citizens'). Skovsgaard and Andersen [80] conceituam formalmente a evitação seletiva, distinta da evitação geral, com assimetria partidária documentada por Toff and Kalogeropoulos [79].
```

**Justificativa**: movido para C3 (T02-A27), com as fontes corrigidas.

---

## T02-A37 — Referências 107–109

| Campo | Valor |
|---|---|
| Lote | 3 |
| Achados | — |
| Decisões | D2 (aprovação das referências novas em 2026-10-13) |
| Localização | Lista de referências, logo depois do item 106 (Napoli) |
| Ação | inserir-apos |
| Estado | aplicado em 2026-10-13 |

**Âncora** (fim do item 106)

```ancora
Media Regulation in the Disinformation Age; Columbia University Press: New York, NY, USA, 2019.
```

**Novo texto**

```novo
Garrett, R.K. Politically Motivated Reinforcement Seeking: Reframing the Selective Exposure Debate. J. Commun. 2009, 59, 676–699.
Heseltine, M.; Barnehl, H.; Wojcieszak, M. Partisan Temporal Selective News Avoidance: Evidence from Online Trace Data. Am. J. Polit. Sci. 2025, 69, 1541–1558.
Urman, A. News Consumption of Russian Vkontakte Users: Polarization and News Avoidance. Int. J. Commun. 2019, 13, 5158–5182.
```

**Justificativa**: formato MDPI, como o restante da lista. Dados conferidos no Crossref (Garrett,
Heseltine: DOIs 10.1111/j.1460-2466.2009.01452.x e 10.1111/ajps.12944) e no PDF (Urman, sem DOI
do periódico). O ponto e vírgula entre autores é o padrão MDPI da lista e fica, como exceção à regra de estilo. A lista do Docs é numerada automaticamente, então os itens recebem 107, 108 e 109.

# Lote 4 — Bloco D, percepção dos outros (aplicado em 2026-10-13)

**Contagem R2 (OpenAlex, 2026-10-13)**: *vocal minority* 435 (*extremity bias* 26) · *social
proof* 2.048 (*social influence bias* 39; *bandwagon effect* 918; *herding* 164.982, termo de
vários campos) · *false consensus* 677 · *pluralistic ignorance* 654 · *spiral of silence* 1.245 ·
*meta-perceptions* 332 + *metaperceptions* 285 (*false polarization* 100; *perceived
polarization* 135).
**D2, conflito entre R1 e R2**: o termo da fonte (Muchnik et al. [41]) é *social influence bias*,
com *herding*; o mais recorrente é *social proof* (Cialdini, fora da lista), que também é o termo
da anotação H09. Proposta: nome principal *social proof* (R2), com os termos da fonte como
alternativos (R1). *Bandwagon effect* sai: é a adoção de uma posição por ser popular, vizinha mas
não idêntica (R6).
**Ordem física**: as entradas novas seguem a ordem D1–D6. As entradas D2 (*false polarization*) e
D4 (*social proof*) da v1 ficam riscadas no lugar, e seu conteúdo reaparece em D6 e D2.
**Fontes sem PDF**: Prentice e Miller [40] (D-sem-PDF; o que se diz do estudo vem do
conhecimento do agente, a conferir).

| ID | Localização (âncora) | Ação | Objetivo | Decisões |
|---|---|---|---|---|
| T02-A38 | Título da 6.6, "Bloco D — Distorção perceptiva" | substituir | Novo nome do bloco | D6 |
| T02-A39 | 6.6, abertura, "Este bloco agrupa mecanismos cujo desfecho primário…" | substituir-paragrafo | Critério do bloco pelo locus | D6, T02.1-F05 |
| T02-A40 | 6.6, "D1 — Vocal minority / extremity bias…" | substituir-paragrafo | D1 | D35 |
| T02-A41 | 6.6, depois do novo D1 | inserir-apos | D2, *social proof* (conteúdo de D4 da v1) | D33, H09 |
| T02-A42 | 6.6, "D2 — False polarization…" | remover | Conteúdo vai para D6 | D17 |
| T02-A43 | 6.6, "D3 — False consensus & pluralistic ignorance…" | substituir-paragrafo | D3, falso consenso | D33 |
| T02-A44 | 6.6, depois do novo D3 | inserir-apos | D4, ignorância pluralística | D33 |
| T02-A45 | 6.6, depois do novo D4 | inserir-apos | D5, espiral do silêncio (vinda de M7) | D33, D6 |
| T02-A46 | 6.6, depois do novo D5 | inserir-apos | D6, metapercepções exageradas (D2 da v1) | D17 |
| T02-A47 | 6.6, "D4 — Social proof…" | remover | Conteúdo vai para D2 | D33 |
| T02-A48 | 6.2, "M7 — Spiral of silence…" | remover | M7 movido para D5 | D6 |

---

## T02-A38 — Título do bloco D

| Campo | Valor |
|---|---|
| Lote | 4 |
| Achados | T02.1-F05 |
| Decisões | D6 |
| Localização | Seção 6.6, título (só o texto depois de "6.6. ") |
| Ação | substituir |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
Bloco D — Distorção perceptiva
```

**Novo texto**

```novo
Block D. Perceptions of others
```

**Justificativa**: o bloco passa a ser definido pelo locus do processo (a inferência sobre os
outros), e não pelo outcome (D6).

---

## T02-A39 — Abertura do bloco D

| Campo | Valor |
|---|---|
| Lote | 4 |
| Achados | T02.1-F05 |
| Decisões | D6 |
| Localização | Seção 6.6, parágrafo 1, começa com "Este bloco agrupa mecanismos cujo desfecho primário" |
| Ação | substituir-paragrafo |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
Este bloco agrupa mecanismos cujo desfecho primário é a camada perceptiva definida na Seção 2.2 — a distinção de nível de análise (percepção sobre o outro, não atitude própria) que justifica separá-lo tanto do Bloco C (vieses de processamento da própria informação) quanto dos desfechos afetivo/ideológico.
```

**Novo texto**

```novo
This block groups the mechanisms that change what people believe others think, feel, or do: how common an opinion is, how hostile the other side is, and which positions can be voiced without social cost. The process takes place in the inferences people draw from the visible behavior of others, which on social media is filtered by who posts, what is counted, and what remains unsaid. These mechanisms act first on perceived polarization (Section 2.2) and can then affect attitudes and behavior. They differ from Block C, which concerns how individuals select and judge information, and from Block A, where an algorithm decides what becomes visible.
```

**Justificativa**: na v1, o critério do bloco era o outcome (T02.1-F05). Passa a ser o locus (D6),
mantendo a ligação com o outcome *perceived* e as fronteiras com os blocos A e C.

---

## T02-A40 — Entrada D1, *vocal minority*

| Campo | Valor |
|---|---|
| Lote | 4 |
| Achados | O06, T02.1-F04 |
| Decisões | D35 |
| Localização | Seção 6.6, parágrafo que começa com "D1 — Vocal minority / extremity bias (alt.: 'sampling bias')." |
| Ação | substituir-paragrafo |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
D1 — Vocal minority / extremity bias (alt.: 'sampling bias'). Bor and Petersen [68] mostram que a hostilidade política online é produzida por uma pequena minoria de usuários orientados a status.
```

**Novo texto**

```novo
D1. Vocal minority. The overrepresentation, in what users see, of a small minority of highly active and extreme participants, from which observers generalize about the whole group. Bor and Petersen [68] found that hostile political discussion online is produced mainly by status-driven individuals who are drawn to politics and are just as hostile offline, and that online discussions feel more hostile in part because the behavior of these individuals is more visible than offline. When the most visible voices of the other side are its most hostile ones, users overestimate how extreme and hostile that side is, which acts on perceived and affective polarization. The mechanism describes who becomes visible. The inference that users then draw about how the other side feels toward them is treated as exaggerated meta-perceptions (D6).
```

**Justificativa**: Bor e Petersen [68], abstract: "hostile political discussions are the result
of status-driven individuals who are drawn to politics and are equally hostile both online and
offline", e "online discussions feel more hostile, in part, because the behavior of such
individuals is more visible than offline". Um construto só (D35); saem *extremity bias* e
*sampling bias* (R2, R6).

---

## T02-A41 — Nova entrada D2, *social proof*

| Campo | Valor |
|---|---|
| Lote | 4 |
| Achados | H09, T02.1-F06 (fonte com outro termo) |
| Decisões | D33 |
| Localização | Seção 6.6, logo depois do novo D1 (aplicar T02-A40 antes) |
| Ação | inserir-apos |
| Estado | aplicado em 2026-10-13 |

**Âncora** (fim do texto novo de T02-A40)

```ancora
is treated as exaggerated meta-perceptions (D6).
```

**Novo texto**

```novo
D2. Social proof (alt. social influence bias, herding). The inference that content is valuable or correct because others have visibly approved of it, which leads people to align their own evaluations with the earlier ones. In a randomized experiment on a social news site, Muchnik et al. [41] gave comments a single artificial up-vote at creation and found that this positive manipulation increased the likelihood of further positive ratings by 32% and produced accumulating herding that raised final ratings by 25% on average, while users tended to correct negative manipulations. Public counts of likes, shares, and votes (AF4) make this signal constant on social media. When approval is concentrated within one camp, social proof can make partisan claims look more widely endorsed than they are, which acts on perceived and ideological polarization. Social proof concerns the individual judgment made in the face of visible approval. The network-level spread that results from many such judgments is treated as information cascades (B4).
```

**Justificativa**: responde à H09 (faltava explicar o que é *social proof*). Muchnik et al. [41],
p. 647: comentários "were artificially given an up-vote (a +1 rating) upon the comment's
creation"; "positive social influence increased the likelihood of positive ratings by 32% and
created accumulating positive herding that increased final ratings by 25% on average", e
"negative social influence inspired users to correct manipulated ratings". Nome pela R2, com os
termos da fonte como alternativos. *Herding* vem de B4 (D33). Fronteira com B4 da D33.

---

## T02-A42 — Remoção da entrada D2 da v1 (*false polarization*)

| Campo | Valor |
|---|---|
| Lote | 4 |
| Achados | T02.1-F02, T02.1-F03 |
| Decisões | D17 |
| Localização | Seção 6.6, parágrafo que começa com "D2 — False polarization" |
| Ação | remover |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
D2 — False polarization (alt.: 'perceived polarization', 'perception gap'). Levendusky and Malhotra [10] documentam a superestimação sistemática de quão polarizados os concidadãos são; Moore-Berg et al. [11] mostram que essas meta-percepções exageradas predizem hostilidade intergrupal real.
```

**Justificativa**: o item era o próprio outcome *perceived* (T02.1-F03). Foi reformulado como D6,
metapercepções exageradas (T02-A46), e *false polarization* passa a ser mencionado lá como
equivalente do outcome *perceived*.

---

## T02-A43 — Entrada D3, *false consensus*

| Campo | Valor |
|---|---|
| Lote | 4 |
| Achados | O06 |
| Decisões | D33 |
| Localização | Seção 6.6, parágrafo que começa com "D3 — False consensus & pluralistic ignorance (alt.: 'misperceived norms')." |
| Ação | substituir-paragrafo |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
D3 — False consensus & pluralistic ignorance (alt.: 'misperceived norms'). Ross et al. [39] descrevem o falso consenso; Prentice and Miller [40] descrevem a ignorância pluralística — as duas faces complementares da distorção de norma percebida.
```

**Novo texto**

```novo
D3. False consensus. The tendency to overestimate how common one's own opinions and choices are among others. Ross et al. [39] showed in four studies that social observers perceive a false consensus about the relative commonness of their own responses. On social media, homophilous networks (B1) and echo chambers (B2) surround users with people who agree with them, which supplies apparent evidence for this overestimate. Users can then overestimate the support for their own side, which acts on perceived polarization. False consensus is the opposite error of pluralistic ignorance (D4), in which people underestimate how common their private views are.
```

**Justificativa**: metade de D3 da v1 (D33). Ross et al. [39], p. 279: "Evidence from four studies
demonstrates that social observers tend to perceive a 'false consensus' with respect to the
relative commonness of their own responses". *Misperceived norms* sai: cobre os dois construtos.

---

## T02-A44 — Nova entrada D4, *pluralistic ignorance*

| Campo | Valor |
|---|---|
| Lote | 4 |
| Achados | O06 |
| Decisões | D33 |
| Localização | Seção 6.6, logo depois do novo D3 (aplicar T02-A43 antes) |
| Ação | inserir-apos |
| Estado | aplicado em 2026-10-13 |

**Âncora** (fim do texto novo de T02-A43)

```ancora
in which people underestimate how common their private views are.
```

**Novo texto**

```novo
D4. Pluralistic ignorance. The situation in which most members of a group privately reject a norm but believe that most others accept it, and act in line with that belief [40]. Prentice and Miller [40] documented this pattern for alcohol use on campus, where students believed that their peers were more comfortable with drinking practices than they themselves were. On social media, the norm that users infer is drawn from what is posted and counted, so the silence of those who disagree (D5) and the visibility of a vocal minority (D1) can make an extreme position look like the majority view. The mechanism acts on perceived polarization and, by discouraging dissent within each side, can push public expression toward the extremes. It is the opposite error of false consensus (D3).
```

**Justificativa**: metade de D3 da v1 (D33). Prentice e Miller [40] (sem PDF; D-sem-PDF): o resultado
sobre o consumo de álcool no campus vem do conhecimento do agente e precisa ser conferido. A
fronteira com D5 (o erro de percepção × o silêncio que o alimenta) é a da D33.

---

## T02-A45 — Nova entrada D5, *spiral of silence*

| Campo | Valor |
|---|---|
| Lote | 4 |
| Achados | T02.1-F05 (M7 no bloco M) |
| Decisões | D6, D33 |
| Localização | Seção 6.6, logo depois do novo D4 (aplicar T02-A44 antes) |
| Ação | inserir-apos |
| Estado | aplicado em 2026-10-13 |

**Âncora** (fim do texto novo de T02-A44)

```ancora
It is the opposite error of false consensus (D3).
```

**Novo texto**

```novo
D5. Spiral of silence. The process by which people who perceive their opinion to be in the minority, or losing ground, become less willing to express it for fear of isolation, which makes the opinion even less visible and further discourages its expression [24]. Noelle-Neumann [24] linked the willingness to speak out to the individual's assessment of the climate of opinion and its trend, and to the fear of isolation when one's view is not confirmed by the majority. On social media, that assessment is made from what is visible in feeds and counts, and the public and persistent character of posts can raise the perceived cost of voicing a minority view. The silence of moderates also changes the behavioral data on which connection recommendation (AF2) is trained, which reinforces homophily (B1), one of the closures of the feedback loop (Section 5.2). The mechanism acts on perceived polarization and, through self-censorship, on behavioral polarization. The evidence for its operation online is mixed.
```

**Justificativa**: M7 da v1, movido para o bloco D (D6). Noelle-Neumann [24], p. 45: a disposição de
se expor depende do "individual's fear of isolation and of his self-confidence being shaken if
his own view is not confirmed by the majority opinion or by the trend of opinion". O fechamento do
loop é o primeiro da Seção 5.2. O rating "Mixed" da v1 fica explícito. *Self-censorship* e
*chilling effect* saem dos alternativos (o primeiro é o comportamento, citado na definição; o
segundo é um conceito jurídico distinto).

---

## T02-A46 — Nova entrada D6, *exaggerated meta-perceptions*

| Campo | Valor |
|---|---|
| Lote | 4 |
| Achados | T02.1-F02, T02.1-F03 |
| Decisões | D17 |
| Localização | Seção 6.6, logo depois do novo D5 (aplicar T02-A45 antes) |
| Ação | inserir-apos |
| Estado | aplicado em 2026-10-13 |

**Âncora** (fim do texto novo de T02-A45)

```ancora
The evidence for its operation online is mixed.
```

**Novo texto**

```novo
D6. Exaggerated meta-perceptions. The overestimation of how negatively the other side views one's own side, and the hostility that this overestimation produces. Moore-Berg et al. [11] found that Democrats and Republicans dislike and dehumanize each other about equally, but believe the other party's prejudice and dehumanization toward them to be about twice as strong as reported. These exaggerated meta-perceptions were independently associated with the desire for social distance from the other party and with support for policies that harm the country and flout democratic norms to favor one's own party. They are related to false polarization, the overestimation of how divided the public is on issues [10], which this framework treats as perceived polarization (Section 2.2). On social media, the visibility of a hostile vocal minority (D1) supplies the evidence from which such meta-perceptions are formed. The mechanism turns perceived polarization into affective polarization.
```

**Justificativa**: D2 da v1, reformulado (D17). Moore-Berg et al. [11], p. 14864: os partidários
"equally dislike and dehumanize each other but think that the levels of prejudice and
dehumanization held by the outgroup party are approximately twice as strong as actually
reported", e "meta-prejudice and meta-dehumanization are independently associated with the
desire for social distance from members of the outgroup party and support for policies that harm
the country and flout democratic norms to favor the ingroup political party". Levendusky e
Malhotra [10], p. 378: "Americans perceive more polarization with respect to policy issues than
actually exists, a phenomenon known as false polarization". Saem os alternativos *perceived
polarization* (nome do outcome, T02.1-F03) e *perception gap*.

---

## T02-A47 — Remoção da entrada D4 da v1 (*social proof*)

| Campo | Valor |
|---|---|
| Lote | 4 |
| Achados | H09 |
| Decisões | D33 |
| Localização | Seção 6.6, parágrafo que começa com "D4 — Social proof" |
| Ação | remover |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
D4 — Social proof (alt.: 'bandwagon effect', 'social influence bias'). Muchnik et al. [41], em experimento randomizado, mostram que um voto positivo inicial altera avaliações subsequentes.
```

**Justificativa**: o conteúdo foi para D2 (T02-A41), na ordem lógica do bloco.

---

## T02-A48 — Remoção da entrada M7 da v1

| Campo | Valor |
|---|---|
| Lote | 4 |
| Achados | T02.1-F05 |
| Decisões | D6 |
| Localização | Seção 6.2, parágrafo que começa com "M7 — Spiral of silence" |
| Ação | remover |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
M7 — Spiral of silence (alt.: 'self-censorship', 'chilling effect'). Autocensura de posições percebidas como minoritárias por medo de isolamento social [Noelle-Neumann, 24], com efeito líquido de distorcer a norma percebida de opinião — mecanismo central ao primeiro ponto de fechamento do circuito de retroalimentação (Seção 5.2).
```

**Justificativa**: movido para D5 (T02-A45).

# Lote 5 — Bloco E, incentivos (aplicado em 2026-10-13)

**Contagem R2 (OpenAlex, 2026-10-13)**: *moral outrage* 1.856 (*outrage expression* 14; *social
reward learning* 46) · *identity signaling* 690 (*partisan expressive* 7; *expressive responding*
44) · *attention economy* 2.403 (estrutura, não processo; T02.1-F02) · *metric-driven* 1.074 ·
*audience metrics* 230 (*feature*, R4) · *clickbait* 1.805 e *rage-bait* 74 (tipos de conteúdo,
não processos) · *outrage industry* 20.
**E3, base fraca**: Petre [102] só está disponível por duas resenhas (Holton 2024; Hua 2023).
Segundo elas, o livro trata de como as métricas mudam o trabalho e as decisões nas redações, e
não de polarização. A ligação com a polarização vem de Rathje et al. [38] (posts sobre o
out-group, inclusive de veículos de imprensa, são mais compartilhados) e fica declarada como
plausível.
**Fontes sem PDF**: Petre [102] (D-sem-PDF, via resenhas).

| ID | Localização (âncora) | Ação | Objetivo | Decisões |
|---|---|---|---|---|
| T02-A49 | Título da 6.7, "Bloco E — Incentivos e economia da atenção" | substituir | Novo nome do bloco | D6 |
| T02-A50 | 6.7, abertura, "Este bloco reúne mecanismos cujo insumo comum é a estrutura de recompensa…" | substituir-paragrafo | Critério do bloco | D6 |
| T02-A51 | 6.7, "E1 — Social learning of outrage…" | substituir-paragrafo | E1, com E4 da v1 incorporado | D23, D31 |
| T02-A52 | 6.7, "E2 — Identity signaling…" | substituir-paragrafo | E2 | H10 |
| T02-A53 | 6.7, "E3 — Attention economy…" | substituir-paragrafo | E3, incentivo de métricas na produção | D18, H11 |
| T02-A54 | 6.7, "E4 — Social quantification / vanity metrics…" | remover | E4 fundido em E1 | D23 |

---

## T02-A49 — Título do bloco E

| Campo | Valor |
|---|---|
| Lote | 5 |
| Achados | T02.1-F02 (E3 como estrutura) |
| Decisões | D6 |
| Localização | Seção 6.7, título (só o texto depois de "6.7. ") |
| Ação | substituir |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
Bloco E — Incentivos e economia da atenção
```

**Novo texto**

```novo
Block E. Incentives
```

**Justificativa**: "economia da atenção" é uma estrutura (contexto), não o critério do bloco
(T02.1-F02). Passa a ser citada na definição de E3.

---

## T02-A50 — Abertura do bloco E

| Campo | Valor |
|---|---|
| Lote | 5 |
| Achados | T02.1-F05 |
| Decisões | D6, D31 |
| Localização | Seção 6.7, parágrafo 1, começa com "Este bloco reúne mecanismos cujo insumo comum é a estrutura de recompensa" |
| Ação | substituir-paragrafo |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
Este bloco reúne mecanismos cujo insumo comum é a estrutura de recompensa — social ou financeira — e não o design de interface em si, o que o distingue do Bloco A (Curadoria algorítmica e arquitetura) mesmo quando operam sobre o mesmo substrato técnico.
```

**Novo texto**

```novo
This block groups the mechanisms driven by rewards: the social approval that posts receive and the economic return that attention brings to those who produce content. What changes behavior here is the expectation of reward, not the interface or the selection made by an algorithm, although both supply and display the rewards. The mechanisms differ in who responds to the incentive: ordinary users who learn from feedback (E1), users who express group loyalty (E2), and professional producers who adjust their output to audience metrics (E3).
```

**Justificativa**: critério pelo locus (D6). A última frase registra as fronteiras por ator da D31
(E1 × E3) e acrescenta E2.

---

## T02-A51 — Entrada E1, *social learning of outrage*

| Campo | Valor |
|---|---|
| Lote | 5 |
| Achados | T02.1-F01 (E4 com nome de affordance) |
| Decisões | D23, D31 |
| Localização | Seção 6.7, parágrafo que começa com "E1 — Social learning of outrage (alt.: 'outrage amplification')." |
| Ação | substituir-paragrafo |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
E1 — Social learning of outrage (alt.: 'outrage amplification'). Brady et al. [13] mostram que feedback social positivo aumenta a probabilidade de expressões futuras de indignação moral, por aprendizagem de reforço.
```

**Novo texto**

```novo
E1. Social learning of outrage. The increase in expressions of moral outrage that results from the social rewards those expressions receive. In two preregistered observational studies on Twitter and two behavioral experiments, Brady et al. [13] found that positive social feedback for outrage expressions increases the likelihood of future outrage expressions, consistent with reinforcement learning, and that users also conform their outrage expressions to the expressive norms of their networks. More generally, Lindström et al. [71] showed with over one million posts from more than 4,000 users that social media behavior follows the principles of reward learning, with users spacing their posts to maximize the rate of social rewards they receive. Likes and shares (AF4) make these rewards immediate and countable, and algorithmic amplification (A2) extends the reach of the rewarded posts. The mechanism raises the volume of hostile moral expression in public discussion, which acts on affective polarization. It concerns the authors who learn from feedback, whereas moral contagion (B5) concerns the users who share such content.
```

**Justificativa**: incorpora E4 da v1 (D23). Brady et al. [13], p. 1: "positive social feedback for
outrage expressions increases the likelihood of future outrage expressions, consistent with
principles of reinforcement learning", e "users conform their outrage expressions to the
expressive norms of their social networks". Lindström et al. [71], p. 1: "We analyze over one
million posts from over 4000 individuals", e "social media users spaced their posts to maximize
the average rate of accrued social rewards". *Outrage amplification* sai dos alternativos: nomeia
o resultado, não o processo (R3). Fronteiras com B5 e A2 da D31.

---

## T02-A52 — Entrada E2, *identity signaling*

| Campo | Valor |
|---|---|
| Lote | 5 |
| Achados | H10, T02.1-F04 |
| Decisões | — |
| Localização | Seção 6.7, parágrafo que começa com "E2 — Identity signaling (alt.: 'partisan expressive behavior')." |
| Ação | substituir-paragrafo |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
E2 — Identity signaling (alt.: 'partisan expressive behavior'). Van Bavel and Pereira [69] propõem um modelo em que a identidade partidária molda percepção e expressão de crença.
```

**Novo texto**

```novo
E2. Identity signaling. The public expression of beliefs and content that marks a person as a loyal member of a political group. Van Bavel and Pereira [69] propose that partisan identities fulfill social goals such as belonging, distinctiveness, and status, and that these identity goals can take precedence over accuracy goals, which helps explain why people place party loyalty over policy and even truth. On social media, political expression is public, attached to a profile, and answered with visible approval from the in-group (AF4), so taking the group's side becomes a way of showing membership. When the expressions that best signal loyalty are the most partisan or the most hostile to the out-group, signaling pushes public positions toward the poles and acts on affective polarization. The evidence comes mainly from theoretical models of partisan identity, with less direct evidence on platform behavior.
```

**Justificativa**: responde à H10 (não ficava claro como o mecanismo polariza): a cadeia vai dos
objetivos identitários à expressão pública e ao deslocamento para os polos. Van Bavel e Pereira
[69] (manuscrito aceito): "This framework helps explain why people place party loyalty over
policy, and even truth" (abstract, p. 2); grupos atendem necessidades como "belonging",
"distinctiveness" e acesso a "power and resources", e "electoral success confers status and
power"; quando as identidades atendem a esses objetivos, "they can generate a powerful incentive
to distort beliefs"; "Although people often possess accuracy goals, in some situations other
goals might take precedence" (p. 7). O termo *signaling* não é dos autores; o nome segue a R2
(690 trabalhos). *Partisan expressive behavior* sai (7 trabalhos). A frase final declara o tipo
de evidência, que é sobretudo teórica.

---

## T02-A53 — Entrada E3, *metric-driven content production*

| Campo | Valor |
|---|---|
| Lote | 5 |
| Achados | H11, T02.1-F02, T02.1-F07 |
| Decisões | D18 |
| Localização | Seção 6.7, parágrafo que começa com "E3 — Attention economy (alt.: 'outrage industry', 'rage-bait')." |
| Ação | substituir-paragrafo |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
E3 — Attention economy (alt.: 'outrage industry', 'rage-bait'). Munn [70] argumenta que arquiteturas técnicas constitutivas favorecem comunicação tóxica por design, independentemente de intenção.
```

**Novo texto**

```novo
E3. Metric-driven content production. The adjustment of what news organizations, journalists, and other content producers publish to the engagement metrics that determine their reach and revenue in an attention economy. Petre [102] examined how real-time analytics tools came to shape newsroom decisions and the daily work of journalists. In posts by news media and members of the U.S. Congress, posts about the political out-group were shared about twice as often as posts about the in-group [38], so metrics reward producers who emphasize conflict and hostility toward the other side. The mechanism creates an incentive that did not exist in this form before platform metrics: producers learn which content travels and supply more of it. Its effect on polarization is plausible rather than demonstrated, since the evidence on newsroom metrics concerns editorial practice more than audience attitudes. It differs from the social learning of outrage (E1), which concerns ordinary users rewarded by social feedback, because here the reward is economic and the producer is professional.
```

**Justificativa**: responde à H11 (explicar melhor a relação), com a reformulação aprovada na D18.
Petre [102], via resenhas: Holton (p. 314–315) descreve como as métricas orientam "the stories they
choose to cover, the angles they adopt, the platforms they distribute on", e Hua (p. 118–119)
trata das ferramentas de analítica em tempo real (Chartbeat) nas redações. Rathje et al. [38],
p. 1: em posts de "news media accounts and US congressional members", "posts about the political
out-group were shared or retweeted about twice as often as posts about the in-group". Munn [70]
sai desta entrada: descreve o desenho das plataformas, que já está em A2 e E1 (D18). *Rage-bait*
e *outrage industry* saem dos alternativos (tipo de conteúdo e indústria, não processos). O
*Claim* "Creates (incentive)" fica explícito e o rating "Plausible" é declarado no texto.

---

## T02-A54 — Remoção da entrada E4 da v1

| Campo | Valor |
|---|---|
| Lote | 5 |
| Achados | T02.1-F01 |
| Decisões | D23 |
| Localização | Seção 6.7, parágrafo que começa com "E4 — Social quantification / vanity metrics" |
| Ação | remover |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
E4 — Social quantification / vanity metrics (alt.: 'gamified reputation'). Lindström et al. [71] formalizam, por modelo computacional de recompensa, como a frequência de postagem se ajusta a reforço social recebido.
```

**Justificativa**: fundido em E1 (T02-A51). O nome repetia a affordance AF4 (T02.1-F01).

# Lote 6 — Bloco F, interação (aplicado em 2026-10-13)

**Contagem R2 (OpenAlex, 2026-10-13)**: *online disinhibition* 548 (*toxic disinhibition* 77) ·
*dogpiling* 110 · *online firestorm(s)* 95 · *online shaming* 154 (mais amplo) · *low-context
communication* 250, **mas no sentido de Edward Hall** (comunicação explícita e direta, o contrário
do que o paper quer dizer) · *message brevity* 7, *brevity effect* 2 · *incivility contagion* 0,
*contagion of incivility* 1, *toxicity contagion* 5 · *exposure to incivility* 59 · *nasty effect*
12. Parte das consultas foi bloqueada pelo limite de requisições do OpenAlex (429); as que
faltaram não alteram as escolhas.
**F3, troca de nome**: *low-context communication* colide com o conceito de Hall (R4, por
analogia: nome que já designa outro construto). Proposta: *message brevity*, com *brevity effect*
como alternativo.
**F5, só fontes da lista**: Anderson et al. [49] e Gervais [50]. Hwang et al. 2014 (candidato do
tema `mecanismos-interacao`, sem PDF) não foi incluído.
**Fora do bloco**: T02-A63 aplica a D29 na Seção 7.1 (justificativa de AF8 → F2).

| ID | Localização (âncora) | Ação | Objetivo | Decisões |
|---|---|---|---|---|
| T02-A55 | Título da 6.8, "Bloco F — Interação e comunicação" | substituir | Novo nome do bloco | D6 |
| T02-A56 | 6.8, abertura, "Este bloco reúne mecanismos que operam no nível da interação direta…" | substituir-paragrafo | Critério do bloco e lugar da incivilidade e do discurso de ódio | D6, D10, D28, H03 |
| T02-A57 | 6.8, "F1 — Online disinhibition effect…" | substituir-paragrafo | F1 | D30 |
| T02-A58 | 6.8, "F2 — Dogpiling…" | substituir-paragrafo | F2 | D28, D29, H12 |
| T02-A59 | 6.8, "F3 — Low-context communication…" | substituir-paragrafo | F3, *message brevity* | D24 |
| T02-A60 | 6.8, "F4 — Incivility contagion…" | substituir-paragrafo | F4, só o contágio | D13, D28, T02.2-F01 |
| T02-A61 | 6.8, depois do novo F4 | inserir-apos | F5, efeito da exposição à incivilidade (M3 da v1) | D13, D28 |
| T02-A62 | 6.2, "M3 — Online toxicity…" | remover | M3 movido para F5 | D13 |
| T02-A63 | 7.1, "Why AF8 (Identifiability) feeds…", frase sobre F2 | substituir | Inverter a justificativa, conforme Rost et al. [73] | D29, T02.2-F03 |

---

## T02-A55 — Título do bloco F

| Campo | Valor |
|---|---|
| Lote | 6 |
| Achados | T02.1-F05 |
| Decisões | D6 |
| Localização | Seção 6.8, título (só o texto depois de "6.8. ") |
| Ação | substituir |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
Bloco F — Interação e comunicação
```

**Novo texto**

```novo
Block F. Interaction
```

**Justificativa**: nome pelo locus (D6).

---

## T02-A56 — Abertura do bloco F

| Campo | Valor |
|---|---|
| Lote | 6 |
| Achados | H03, T02.1-F02 (M3 como sintoma) |
| Decisões | D6, D10, D28 |
| Localização | Seção 6.8, parágrafo 1, começa com "Este bloco reúne mecanismos que operam no nível da interação direta" |
| Ação | substituir-paragrafo |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
Este bloco reúne mecanismos que operam no nível da interação direta entre usuários — a distinção que o separa do Bloco E (incentivo estrutural) e do Bloco D (distorção perceptiva sem interação direta).
```

**Novo texto**

```novo
This block groups the mechanisms that operate in direct exchanges between users: how people express themselves when they talk to strangers, how groups react to a perceived transgression, how the format of a message shapes the conversation, and how the tone of a discussion spreads and affects those who read it. Incivility and hate speech are treated here as observable features of discourse rather than as mechanisms. They are produced by disinhibition (F1) and collective sanctioning (F2), they spread through contagion (F4), and they affect readers through exposure (F5). The block differs from Block E, where behavior is driven by rewards, and from Block D, which concerns inferences about others rather than the interaction itself.
```

**Justificativa**: responde à H03 (relação de M3 com F1, F2 e F4) e aplica a D10: incivilidade e
discurso de ódio não são mecanismos, mas o que a cadeia produção → circulação → recepção (D28)
produz e faz circular.

---

## T02-A57 — Entrada F1, *online disinhibition effect*

| Campo | Valor |
|---|---|
| Lote | 6 |
| Achados | T02.1-F04 |
| Decisões | D30 |
| Localização | Seção 6.8, parágrafo que começa com "F1 — Online disinhibition effect (alt.: 'deindividuation')." |
| Ação | substituir-paragrafo |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
F1 — Online disinhibition effect (alt.: 'deindividuation'). Suler [72] descreve como anonimato, assincronia e invisibilidade reduzem inibições sociais.
```

**Novo texto**

```novo
F1. Online disinhibition effect. The loosening of the social restraints that normally govern how people express themselves, produced by features of online interaction. Suler [72] identified six interacting factors: dissociative anonymity, invisibility, asynchronicity, solipsistic introjection, dissociative imagination, and minimization of authority. Disinhibition can be benign, as in greater openness and self-disclosure, or toxic, as in rude language, harsh criticism, anger, hatred, and threats, and only the toxic form matters for polarization. Identifiability settings (AF8) shape several of these factors. The evidence for a role in political hostility is mixed: across eight studies, Bor and Petersen [68] found that hostile political discussion is produced mainly by people who are just as hostile offline, with only limited support for the claim that online environments make people more hostile. Where it operates, the mechanism raises the amount of hostile expression in political talk, which acts on affective polarization.
```

**Justificativa**: aplica a D30. Suler [72], p. 321: "six factors that interact with each other in
creating this online disinhibition effect: dissociative anonymity, invisibility, asynchronicity,
solipsistic introjection, dissociative imagination, and minimization of authority"; a forma tóxica
inclui "rude language, harsh criticisms, anger, hatred, even threats". Bor e Petersen [68],
abstract: "Across eight studies", "we test the mismatch hypothesis but only find evidence for
limited selection effects. Instead, hostile political discussions are the result of status-driven
individuals who are drawn to politics and are equally hostile both online and offline".
*Deindividuation* sai dos alternativos: é um construto vizinho, da psicologia de multidões (R6).

---

## T02-A58 — Entrada F2, *dogpiling*

| Campo | Valor |
|---|---|
| Lote | 6 |
| Achados | H12, T02.2-F03 |
| Decisões | D28, D29 |
| Localização | Seção 6.8, parágrafo que começa com "F2 — Dogpiling (alt.: 'pile-on', 'online shaming', 'firestorm')." |
| Ação | substituir-paragrafo |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
F2 — Dogpiling (alt.: 'pile-on', 'online shaming', 'firestorm'). Rost et al. [73] analisam tempestades online como aplicação desproporcional de normas sociais.
```

**Novo texto**

```novo
F2. Dogpiling (alt. online firestorm, pile-on). A sudden wave of hostile messages from many users directed at a person or organization after a perceived transgression. Analyzing 532,197 comments on 1,612 online petitions, Rost et al. [73] explained such firestorms as the digital enforcement of social norms rather than as a product of anonymity: in this context, non-anonymous individuals were more aggressive than anonymous ones. Low audience segmentation (AF6) exposes posts to readers the author never anticipated, so a single post can reach many hostile users at once. Because attackers act to enforce the norms of their own group, dogpiling deepens the divide between groups and shows potential speakers that voicing a contested view carries a high cost, which links it to the spiral of silence (D5). The mechanism acts on behavioral and affective polarization.
```

**Justificativa**: responde à H12 (faltava explicar o que é *dogpiling*). Nome pela R2 (*dogpiling*
110, *online firestorm* 95), com o termo da fonte como alternativo (R1). Rost et al. [73], p. 1:
"532,197 comments on 1,612 online petitions"; "This article introduces social norm theory to
understand online aggression"; "non-anonymous individuals are more aggressive compared to
anonymous individuals". A ligação com D5 é a que a 7.1 já faz para AF6 ("staying silent becomes
the rational response"). *Online shaming* sai: é mais amplo (R6).

---

## T02-A59 — Entrada F3, *message brevity*

| Campo | Valor |
|---|---|
| Lote | 6 |
| Achados | T02.1-F01 (alternativo com nome de affordance) |
| Decisões | D24 |
| Localização | Seção 6.8, parágrafo que começa com "F3 — Low-context communication (alt.: 'brevity effect', 'constraint affordance effect')." |
| Ação | substituir-paragrafo |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
F3 — Low-context communication (alt.: 'brevity effect', 'constraint affordance effect'). Jaidka et al. [9] mostram, em quase-experimento, que a ampliação do limite de caracteres do Twitter produziu discussões políticas mais civis.
```

**Novo texto**

```novo
F3. Message brevity (alt. brevity effect). The loss of nuance, politeness, and constructive argument that occurs when the format of a platform forces political messages to be short. Limits on message length (AF7) make it harder to qualify claims, explain reasoning, and acknowledge the other side, which pushes discussion toward blunt and uncivil statements. Using the 2017 doubling of Twitter's character limit as a natural experiment, Jaidka et al. [9] found that longer permitted messages led to less uncivil, more polite, and more constructive replies to politicians, although empathy and respectfulness kept declining over the period. The mechanism lowers the quality of political talk and acts on affective polarization.
```

**Justificativa**: aplica a D24 (sai o alternativo *constraint affordance effect*, que remetia a
AF7) e troca o nome: *low-context communication* é o conceito de Hall para comunicação explícita e
direta [conhecimento do agente; o uso confirma-se pelas 250 ocorrências no OpenAlex], o oposto do
sentido pretendido. Jaidka et al. [9] (versão SSRN), abstract: "doubling the permissible length of
a Tweet led to less uncivil, more polite and more constructive discussions online. However, the
declining trend in the empathy and respectfulness of these tweets raises concerns", com "358,242
Tweet replies to U.S. politicians".

---

## T02-A60 — Entrada F4, *incivility contagion*

| Campo | Valor |
|---|---|
| Lote | 6 |
| Achados | T02.2-F01 |
| Decisões | D13, D28 |
| Localização | Seção 6.8, parágrafo que começa com "F4 — Incivility contagion (alt.: 'toxicity contagion', 'nasty effect')." |
| Ação | substituir-paragrafo |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
F4 — Incivility contagion (alt.: 'toxicity contagion', 'nasty effect'). Anderson et al. [50] mostram que comentários incivis de terceiros alteram a percepção do tema discutido, mesmo quando o conteúdo original é neutro.
```

**Novo texto**

```novo
F4. Incivility contagion (alt. toxicity contagion). The spread of an uncivil tone through a discussion, as people exposed to uncivil comments, especially from their own side, become more likely to write uncivil comments themselves. In an experiment with an online discussion forum, Gervais [50] found that exposure to like-minded incivility increased the use of uncivil language in participants' own political comments, mainly when the incivility was histrionic and emotional. Comment threads make each message visible to the next participant, so the tone set by the first messages shapes the norms of the conversation. The mechanism raises the share of uncivil discourse in political talk, which acts on behavioral and affective polarization. It differs from the exposure effect (F5), which concerns how readers' perceptions and emotions change, and from the social learning of outrage (E1), which concerns rewarded moral outrage rather than tone.
```

**Justificativa**: resolve o T02.2-F01: o *nasty effect* sai (vai para F5), e F4 fica só com o
contágio. Gervais [50], p. 167: "exposure to like-minded incivility increases the use of uncivil
behavior in political comments by message board posters. Notably, these effects mainly occur when
histrionic, emotional incivility is present". Fronteira com E1 da D31. Corrige a fonte (a v1
citava Anderson et al. como [50]; na lista, Anderson é [49] e Gervais é [50]).

---

## T02-A61 — Nova entrada F5, *incivility exposure effect*

| Campo | Valor |
|---|---|
| Lote | 6 |
| Achados | H03, T02.2-F01 |
| Decisões | D13, D28 |
| Localização | Seção 6.8, logo depois do novo F4 (aplicar T02-A60 antes) |
| Ação | inserir-apos |
| Estado | aplicado em 2026-10-13 |

**Âncora** (fim do texto novo de T02-A60)

```ancora
which concerns rewarded moral outrage rather than tone.
```

**Novo texto**

```novo
F5. Incivility exposure effect (alt. nasty effect). The change in readers' perceptions and emotions that follows exposure to uncivil discussion. In an experiment with a sample representative of the U.S. population, Anderson et al. [49] found that uncivil comments under a blog post polarized readers' perceptions of the risks of the technology discussed along the lines of their religiosity and prior support, as readers fell back on their own values. Gervais [50] found that exposure to uncivil disagreement induced anger and aversion, which reduced satisfaction with the discussion. On social media, comments are shown next to news and posts, so readers who never take part in an exchange still absorb its tone. The mechanism acts on ideological polarization, by polarizing perceptions of the issue discussed, and on affective polarization, through anger and aversion toward the other side.
```

**Justificativa**: é M3 da v1, reformulado como processo (D13; o P1 da Seção 13). Anderson et al.
[49], p. 373: "exposure to uncivil blog comments can polarize risk perceptions of nanotechnology
along the lines of religiosity and issue support", com amostra "representative of the U.S.
population"; p. 374: os leitores podem "make judgments about the issue based on their own
preexisting values". Gervais [50], p. 167: "exposure to disagreeable uncivil political talk induces
feelings of anger and aversion, which in turn reduces satisfaction with the message board
discourse". *Nasty effect*, termo de Anderson et al., entra como alternativo.

---

## T02-A62 — Remoção da entrada M3 da v1

| Campo | Valor |
|---|---|
| Lote | 6 |
| Achados | H03, T02.1-F02 |
| Decisões | D13 |
| Localização | Seção 6.2, parágrafo que começa com "M3 — Online toxicity" |
| Ação | remover |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
M3 — Online toxicity (alt.: 'uncivil discourse', 'online political hostility'). Manifestações de discurso de ódio, incivilidade e debates improdutivos, tratadas aqui como sintoma observável mais do que mecanismo causal primário — o mecanismo por trás é melhor capturado por F1, F2 e F4 três mecanismos do Bloco F (Interação e comunicação): Online disinhibition effect (F1), Dogpiling (F2) e Incivility contagion (F4) (Seção 6.8). Anderson et al. [50] demonstram que comentários incivis alteram a percepção do próprio tema discutido; Gervais [51] documenta reações afetivas e comportamentais a posts politicamente incivis.
```

**Justificativa**: movido para F5 (T02-A61). O tratamento da incivilidade como manifestação
observável passa para a abertura do bloco F (T02-A56).

---

## T02-A63 — Seção 7.1, justificativa de AF8 → F2

| Campo | Valor |
|---|---|
| Lote | 6 |
| Achados | T02.2-F03 |
| Decisões | D29 |
| Localização | Seção 7.1, parágrafo "Why AF8 (Identifiability) feeds each of these mechanisms.", segunda frase, começa com "The link to F2 (Dogpiling) follows from the same reduced reputational cost" |
| Ação | substituir |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
The link to F2 (Dogpiling) follows from the same reduced reputational cost applied to coordinated attacks: an attacker operating under a disposable identity risks no nominal reputation in the process.
```

**Novo texto**

```novo
The link to F2 (Dogpiling) runs in the opposite direction to what is often assumed. In online firestorms, non-anonymous individuals are more aggressive than anonymous ones, because the aggression works as the enforcement of social norms, which people have reasons to carry out under their own name [73].
```

**Justificativa**: aplica a D29 e resolve o T02.2-F03. Rost et al. [73], p. 1: "challenging the
popular assumption that online anonymity is" a causa da agressão; "non-anonymous individuals are
more aggressive compared to anonymous individuals"; p. 2: "Individuals have a strong motivation for
being non-anonymous when being aggressive in social media. We explain this behavior pattern by
social norm theory".

# Lote 7 — Bloco G, ecossistema e oferta (aplicado em 2026-10-13)

**Contagem R2**: **não obtida**. O OpenAlex recusou as consultas por limite de requisições (HTTP 429) em duas tentativas, em 2026-10-13. Os nomes seguem as decisões D15 (G3), D19 (G2) e D35 (G1, G4). A contagem fica pendente e não bloqueia o lote: em todos os casos o nome escolhido é o termo da fonte (R1) ou o já decidido.
**Fontes**: Barzilai-Nahon [17] obtido em 2026-10-13 (PDF). Benkler et al. [75] e Woolley e Howard
[53] são livros sem PDF (D-sem-PDF; o que se diz deles vem do conhecimento do agente, a conferir).
**Depois deste lote**, a Seção 6.2 (bloco M) fica só com M6, que aguarda o backlog B02.

| ID | Localização (âncora) | Ação | Objetivo | Decisões |
|---|---|---|---|---|
| T02-A64 | Título da 6.9, "Bloco G — Ecossistema informacional e oferta" | substituir | Novo nome do bloco | D6 |
| T02-A65 | 6.9, abertura, "Este bloco reúne mecanismos de nível macro…" | substituir-paragrafo | Critério do bloco | D6 |
| T02-A66 | 6.9, "G1 — Disintermediation / gatekeeping decline…" | substituir-paragrafo | G1 | D35 |
| T02-A67 | 6.9, "G2 — Network propaganda…" | substituir-paragrafo | G2, *propaganda feedback loop* | D19, H13 |
| T02-A68 | 6.9, depois do novo G2 | inserir-apos | G3, consenso fabricado (M5 da v1) | D15 |
| T02-A69 | 6.9, "G4 — Deplatforming & migration…" | substituir-paragrafo | G4, *platform migration* | D35, H14 |
| T02-A70 | 6.9, "G5 — Perceived censorship…" | substituir-paragrafo | G5 | — |
| T02-A71 | 6.2, "M5 — Coordinated inauthentic behavior…" | remover | M5 movido para G3 | D15 |

---

## T02-A64 — Título do bloco G

| Campo | Valor |
|---|---|
| Lote | 7 |
| Achados | T02.1-F05 |
| Decisões | D6 |
| Localização | Seção 6.9, título (só o texto depois de "6.9. ") |
| Ação | substituir |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
Bloco G — Ecossistema informacional e oferta
```

**Novo texto**

```novo
Block G. Information ecosystem and supply
```

**Justificativa**: o nome se mantém, traduzido e sem travessão (D6).

---

## T02-A65 — Abertura do bloco G

| Campo | Valor |
|---|---|
| Lote | 7 |
| Achados | T02.1-F05 |
| Decisões | D6 |
| Localização | Seção 6.9, parágrafo 1, começa com "Este bloco reúne mecanismos de nível macro" |
| Ação | substituir-paragrafo |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
Este bloco reúne mecanismos de nível macro — propriedades do ecossistema de mídia como um todo, não de uma interação ou decisão algorítmica isolada —, justificando tratá-lo separadamente mesmo quando a evidência disponível é mais contingente e dependente de contexto nacional (Seção 3.4, Tabela 4).
```

**Novo texto**

```novo
This block groups the mechanisms that operate at the level of the information ecosystem: who controls which information reaches the public, how partisan media and political actors supply and reinforce it, how coordinated actors fabricate signals of popularity, and how platform governance moves communities and shapes their trust. The locus of these processes is the supply of information and the rules of the system, not the individual user, the network of contacts, or a single interaction, which separates this block from Blocks B to F. Because they depend on media systems and institutions, the evidence for them is more contingent on national context.
```

**Justificativa**: critério pelo locus (D6). Mantém a ressalva da v1 sobre a dependência do contexto
nacional. A remissão à "Tabela 4" da v1 sai: era a tabela de moderadores, renumerada pela T01.

---

## T02-A66 — Entrada G1, *gatekeeping decline*

| Campo | Valor |
|---|---|
| Lote | 7 |
| Achados | O06, T02.1-F06 (fonte com outro termo) |
| Decisões | D35 |
| Localização | Seção 6.9, parágrafo que começa com "G1 — Disintermediation / gatekeeping decline (alt.: 'epistemic fragmentation')." |
| Ação | substituir-paragrafo |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
G1 — Disintermediation / gatekeeping decline (alt.: 'epistemic fragmentation'). Bennett and Livingston [74] argumentam que a comunicação disruptiva e o declínio institucional formam uma nova "ordem de desinformação".
```

**Novo texto**

```novo
G1. Gatekeeping decline (alt. disintermediation). The weakening of the editorial filters that once decided which information reached the public, as platforms let content reach audiences without passing through professional gatekeepers. Barzilai-Nahon [17] defines gatekeeping as the process of controlling information as it moves through a gate and proposes a theory of network gatekeeping in which the gated gain influence through their political power, their ability to produce information, and their alternatives. As traditional gatekeeping loses force, disinformation can pass through the gates of legacy media and receive an amplifier effect that stories dismissed as absurd would not have received in eras of more effective press gatekeeping [74]. The mechanism widens the circulation of unvetted and partisan claims, which acts on ideological and perceived polarization.
```

**Justificativa**: nome principal pela D35. Barzilai-Nahon [17], p. 1495: "Gatekeeping is defined here
as the process of controlling information as it moves through a gate"; abstract (p. 1493): os
"gated" e sua saliência por "(a) their political power in relation to the gatekeeper, (b) their
information production ability, (c) their relationship with the gatekeeper, and (d) their
alternatives". Bennett e Livingston [74], p. 124: disinformation "often passes through the gates of
the legacy media, resulting in an 'amplifier effect' for stories that would be dismissed as absurd
in earlier eras of more effective press gatekeeping". *Epistemic fragmentation* sai (outcome, R6).

---

## T02-A67 — Entrada G2, *propaganda feedback loop*

| Campo | Valor |
|---|---|
| Lote | 7 |
| Achados | H13, T02.1-F02 |
| Decisões | D19 |
| Localização | Seção 6.9, parágrafo que começa com "G2 — Network propaganda (alt.: 'hyperpartisan media ecosystem')." |
| Ação | substituir-paragrafo |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
G2 — Network propaganda (alt.: 'hyperpartisan media ecosystem'). Benkler et al. [75] argumentam que, nos EUA, o ecossistema de mídia da direita se mostrou historicamente mais insular e menos autocorretivo.
```

**Novo texto**

```novo
G2. Propaganda feedback loop (alt. network propaganda). A self-reinforcing cycle in which partisan media outlets, political figures, and audiences reward stories that confirm the group's identity and penalize outlets and journalists that check them, so that the media ecosystem becomes insular and resistant to correction [75]. Benkler et al. [75] describe this dynamic in the right-wing media ecosystem of the United States, which they found more insular and less self-correcting than the rest of the American media system. Bennett and Livingston [74] place such dynamics within a broader disinformation order linked to disruptive communication and the decline of democratic institutions. Social media accelerate the loop by letting partisan content circulate without editorial filters (G1) and by rewarding content that confirms group identity (E1, E2). The mechanism acts on ideological and perceived polarization. Its evidence is moderate and stronger for the United States than for other countries.
```

**Justificativa**: responde à H13 (melhorar a definição) e aplica a D19: o item passa a nomear o
processo, e *network propaganda*, título do livro, vira alternativo. Benkler et al. [75] (livro sem
PDF; D-sem-PDF): o ciclo e a assimetria do ecossistema de direita vêm do conhecimento do agente, a
conferir. Bennett e Livingston [74]: título do artigo ("The disinformation order: Disruptive
communication and the decline of democratic institutions"). A última frase reproduz o rating da v1,
"Moderate (strong in the U.S.)".

---

## T02-A68 — Nova entrada G3, *manufactured consensus*

| Campo | Valor |
|---|---|
| Lote | 7 |
| Achados | T02.1-F02 (M5 como estratégia de ator) |
| Decisões | D15 |
| Localização | Seção 6.9, logo depois do novo G2 (aplicar T02-A67 antes) |
| Ação | inserir-apos |
| Estado | aplicado em 2026-10-13 |

**Âncora** (fim do texto novo de T02-A67)

```ancora
Its evidence is moderate and stronger for the United States than for other countries.
```

**Novo texto**

```novo
G3. Manufactured consensus (alt. astroturfing, coordinated inauthentic behavior). The fabrication of signals of popularity by coordinated actors, often with automated or compromised accounts, to make a topic, claim, or position look more widely supported than it is [53]. Elmas et al. [54] uncovered ephemeral astroturfing attacks on Twitter, in which a chosen keyword was promoted by coordinated inauthentic activity to appear popular and the activity was then removed. They detected over 19,000 fake trends promoted by over 108,000 accounts and found that these attacks accounted for at least 20% of the top ten global trends. The mechanism sits on the supply side: it produces the signals that other mechanisms then act upon, such as social proof (D2), algorithmic agenda-setting (A4), and information cascades (B4). Its effects are mainly on perceived polarization, through distorted impressions of what others support, and on affective polarization when the fabricated content targets the out-group. It is the clearest case of the actors defined in Section 2.3, who deliberately trigger or exploit mechanisms.
```

**Justificativa**: M5 da v1, reformulado como processo e movido para o bloco G (D15). Elmas et al.
[54], abstract: "a chosen keyword or topic is artificially promoted by coordinated and inauthentic
activity to appear popular, and, crucially, this activity is removed as part of the attack";
"We detected over 19,000 unique fake trends promoted by over 108,000 accounts"; "Trends astroturfed
by these attacks account for at least 20% of the top 10 global trends". Woolley e Howard [53] (livro,
D-sem-PDF). As fronteiras com D2, A4 e B4 são as da D15 e da D33. A última frase liga G3 ao
construto *Actor* da 2.3 (T02.1-F02). *Computational propaganda* sai: é mais amplo (R6).

---

## T02-A69 — Entrada G4, *platform migration*

| Campo | Valor |
|---|---|
| Lote | 7 |
| Achados | H14, O06 |
| Decisões | D35 |
| Localização | Seção 6.9, parágrafo que começa com "G4 — Deplatforming & migration (alt.: 'platform migration')." |
| Ação | substituir-paragrafo |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
G4 — Deplatforming & migration (alt.: 'platform migration'). Horta Ribeiro et al. [77] mostram que a moderação de duas comunidades do Reddit reduziu atividade, mas, em um caso, aumentou sinais de toxicidade na plataforma de destino.
```

**Novo texto**

```novo
G4. Platform migration. The movement of a community to another platform, often one with laxer rules or a website of its own, after moderation measures such as bans on a mainstream platform. Horta Ribeiro et al. [77] followed r/The_Donald and r/Incels, two communities banned from Reddit that migrated to standalone websites. In both cases, moderation significantly decreased posting activity on the new platform, with fewer posts, active users, and newcomers, but users of r/The_Donald showed increases in signals associated with toxicity and radicalization. Moderation decisions made under platform governance (AF10) act as the trigger, and the migration concentrates the most committed members in more homogeneous and less moderated spaces. The mechanism acts on structural polarization, by separating communities across platforms, and on affective polarization, through the radicalization of those who remain. Its evidence is mixed.
```

**Justificativa**: responde à H14 (melhorar a definição) e aplica a D35: o nome passa a ser o
processo, e o banimento entra como gatilho. Horta Ribeiro et al. [77] (versão arXiv), abstract:
"two communities that were banned from Reddit and subsequently migrated to their own standalone
websites"; "moderation measures significantly decreased posting activity on the new platform,
reducing the number of posts, active users, and newcomers. In spite of that, users in one of the
studied communities (r/The_Donald) showed increases in signals associated with toxicity and
radicalization". O rating da v1, "Mixed", fica explícito.

---

## T02-A70 — Entrada G5, *perceived censorship*

| Campo | Valor |
|---|---|
| Lote | 7 |
| Achados | T02.1-F04, T02.1-F05 |
| Decisões | D6 (G5 fica em G) |
| Localização | Seção 6.9, parágrafo que começa com "G5 — Perceived censorship (alt.: 'perceived moderation bias')." |
| Ação | substituir-paragrafo |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
G5 — Perceived censorship (alt.: 'perceived moderation bias'). Myers West [78] documenta como usuários formam teorias próprias sobre critérios de moderação diante de remoções pouco explicadas.
```

**Novo texto**

```novo
G5. Perceived censorship (alt. perceived moderation bias). The belief, formed after content is removed or accounts are restricted with little explanation, that platform moderation is biased against one's views or group. In a survey of 519 users who had experienced content moderation, Myers West [78] found that users build folk theories about how moderation works, and several attributed takedowns to political bias on the part of the company or to coordinated reporting by their opponents. Opaque moderation under platform governance (AF10) leaves room for these theories. When each side comes to see the platform as an ally of the other, the mechanism feeds grievance and distrust, which acts on affective polarization. The evidence is plausible rather than demonstrated, since the available work documents the beliefs more than their effect on attitudes toward the out-group.
```

**Justificativa**: Myers West [78], abstract (p. 4366): "Through a survey of users (n=519) who have
experienced content moderation, I explore users' folk theories of how content moderation systems
work"; p. 4373: "Several users attributed the reason for the content takedown to perceived political
bias on the part of the company", e relatos de denúncias feitas por adversários ("attacked by
transphobes who reported my picture"). O rating da v1, "Plausible", fica explícito. G5 fica em G
pela D6 (percepção sobre a governança, não sobre os outros usuários).

---

## T02-A71 — Remoção da entrada M5 da v1

| Campo | Valor |
|---|---|
| Lote | 7 |
| Achados | T02.1-F02 |
| Decisões | D15 |
| Localização | Seção 6.2, parágrafo que começa com "M5 — Coordinated inauthentic behavior" |
| Ação | remover |
| Estado | aplicado em 2026-10-13 |

**Texto original**

```original
M5 — Coordinated inauthentic behavior (alt.: 'astroturfing', 'computational propaganda'). Manipulação deliberada de percepção de consenso por atores coordenados, incluindo contas automatizadas [Woolley and Howard, 54]. Elmas et al. [55] documentam ataques efêmeros de astroturfing capazes de fabricar tendências no Twitter.
```

**Justificativa**: movido para G3 (T02-A68).

# Lote 8 — Affordances em conflito: AF1, AF2, AF4, AF6, AF7 e Seção 7.2 (aplicado em 2026-10-16)

**Base**: relatório, Seção 14.2 (D20–D25; achado T02.2-F02); critérios de Evans et al. [34], pp.
39–40. Conforme a D25, só as cinco affordances em conflito.
**Escopo**: só a frase de nome e definição de cada affordance (substituição dentro do parágrafo). As
frases seguintes de cada entrada (fontes, listas *Feeds*, blocos) ficam para o lote 10 (T02.5), junto
da Tabela 6 e das Figuras 5, 6, 8, 10 e 11.
**Fontes sem PDF**: Majchrzak et al. [8] (termos *network-informed associating* e *metavoicing*:
reconhecidos como affordances por Evans et al. [34], p. 40; as definições vêm do conhecimento do
agente, a conferir) e boyd [7] (D-sem-PDF, a conferir).
**Texto original**: tirado da cópia de revisão lida em 2026-10-13. A credencial da conta de serviço
foi recusada em 2026-10-16 ("Invalid JWT Signature"); a simulação depende de uma chave nova.
**Numeração**: no trecho original, Marwick e boyd aparecem como [61]; na lista, são [60] (P3).

| ID | Localização (âncora) | Ação | Objetivo | Decisões |
|---|---|---|---|---|
| T02-A72 | 7.1, "AF1 — Algorithmic content curation…", nome e 1ª frase | substituir | Definição relacional | D20 |
| T02-A73 | 7.1, "AF2 — Connection recommendation…", nome e 2 primeiras frases | substituir | Renomear: *network-informed associating* | D21 |
| T02-A74 | 7.1, "AF4 — Social quantification…", nome e 1ª frase | substituir | Definição relacional (*metavoicing*) | D23 |
| T02-A75 | 7.1, "AF6 — Context collapse…", nome e 2 primeiras frases | substituir | Renomear: segmentação de audiência | D22 |
| T02-A76 | 7.1, "AF7 — Constraint affordance.", nome e 1ª frase | substituir | Definição relacional | D24 |
| T02-A77 | Título da 7.2, "Conceptualizing AF6 as a second-order affordance" | substituir | Novo título | D22 |
| T02-A78 | 7.2, parágrafo único, "Unlike the other ten affordances…" | substituir-paragrafo | Reescrever pela D22 | D22 |

---

## T02-A72 — AF1, *algorithmic content curation*

| Campo | Valor |
|---|---|
| Lote | 8 |
| Achados | T02.2-F02 |
| Decisões | D20 |
| Localização | Seção 7.1, entrada AF1, do início até o fim da primeira frase de definição |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

**Texto original**

```original
AF1 — Algorithmic content curation (alt.: engagement-based ranking, algorithmic selection). The affordance through which content visible to the user is selected and ordered by an automated system based on predictive engagement signals.
```

**Novo texto**

```novo
AF1. Algorithmic content curation (alt. algorithmic selection). The degree to which what users see, and how visible their own posts become, is decided by an automated system that ranks content by predicted engagement rather than by the user's own choices or by chronology. Engagement-based ranking is the feature through which most platforms realize this affordance, which varies from chronological feeds to fully algorithmic ones.
```

**Justificativa**: a definição da v1 descrevia o que o sistema faz, isto é, uma *feature* (Evans et
al. [34], critério 1, pp. 39–40; a 2.3 do próprio paper dá "a recommendation algorithm" como exemplo
de *feature*). A nova define a relação usuário–sistema e a variabilidade (critério 3, p. 40).
*Engagement-based ranking* sai dos alternativos e passa a ser citado como a *feature* (D20).

---

## T02-A73 — AF2, *network-informed associating*

| Campo | Valor |
|---|---|
| Lote | 8 |
| Achados | T02.2-F02 |
| Decisões | D21 |
| Localização | Seção 7.1, entrada AF2, do início até "specifically designate this mechanism network-informed associating." |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

**Texto original**

```original
AF2 — Connection recommendation (alt.: 'friend/people recommendation', 'network-informed associating'). The affordance through which a platform suggests connections based on network similarity and proximity. Majchrzak et al. [8] specifically designate this mechanism network-informed associating.
```

**Novo texto**

```novo
AF2. Network-informed associating (alt. connection recommendation). The possibility of forming ties with other users on the basis of information about one's own network and the relations of others [8], which platforms realize through features such as people-you-may-know suggestions. It varies with how prominently such suggestions are offered and how far they rely on network similarity.
```

**Justificativa**: renomeação da D21. *Network-informed associating* é o termo de Majchrzak et al. [8]
e consta entre as affordances que Evans et al. [34] reconhecem (p. 40). A frase da v1 chamava a
affordance de "mechanism", o que confundia as camadas (T02.1-F01). *Connection recommendation*
passa a alternativo e a *feature* exemplar. Definição de Majchrzak: conhecimento do agente, a
conferir.

---

## T02-A74 — AF4, *social quantification*

| Campo | Valor |
|---|---|
| Lote | 8 |
| Achados | T02.2-F02 |
| Decisões | D23 |
| Localização | Seção 7.1, entrada AF4, do início até o fim da primeira frase de definição |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

**Texto original**

```original
AF4 — Social quantification (alt.: 'metrification of sociality'). The affordance through which reactions and reach are converted into publicly visible counters.
```

**Novo texto**

```novo
AF4. Social quantification (alt. metavoicing, metrification of sociality). The possibility of reacting to others' content with lightweight public signals, such as likes, shares, and votes, and of seeing these reactions aggregated for each post and profile. Majchrzak et al. [8] call the first part of this possibility metavoicing. The counters themselves are features, and the affordance varies with how visible and prominent the aggregated reactions are.
```

**Justificativa**: a v1 definia a affordance pelos contadores, que são *features* (Evans et al. [34]
tratam alertas e notificações da mesma forma, p. 45). O nome se mantém, porque a colisão com E4 já
foi resolvida pela fusão de E4 em E1 (D23). *Metavoicing* (Majchrzak et al. [8]; reconhecido por
Evans et al., p. 40) entra como alternativo; definição a conferir no PDF de [8].

---

## T02-A75 — AF6, *audience segmentation*

| Campo | Valor |
|---|---|
| Lote | 8 |
| Achados | T02.2-F02 |
| Decisões | D22 |
| Localização | Seção 7.1, entrada AF6, do início até "Marwick and boyd [61] coined the term." |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

**Texto original**

```original
AF6 — Context collapse (second-order affordance; see Section 7.2 for discussion). The affordance, defined negatively, through which audiences typically segmented offline are collapsed into a single channel. Marwick and boyd [61] coined the term.
```

**Novo texto**

```novo
AF6. Audience segmentation. The possibility of directing content to distinct audiences instead of a single undifferentiated one. When segmentation is low, audiences that are kept apart offline are collapsed into a single context, which Marwick and boyd [60] call context collapse and which makes it hard for users to manage the different audiences they imagine for each post. Context collapse is therefore the low end of this affordance rather than an affordance in itself (Section 7.2).
```

**Justificativa**: aplica a D22. Pelo critério 2 de Evans et al. [34] (p. 40), o colapso de contexto é
um outcome, e não uma affordance. Marwick e boyd [60], p. 114: "Social media technologies collapse
multiple audiences into single contexts, making it difficult for people to use the same techniques
online that they do to handle multiplicity in face-to-face conversation", e "imagined audiences".
Corrige a numeração ([61] → [60]).

---

## T02-A76 — AF7, *constraint affordance*

| Campo | Valor |
|---|---|
| Lote | 8 |
| Achados | T02.2-F02 |
| Decisões | D24 |
| Localização | Seção 7.1, entrada AF7, do início até o fim da primeira frase de definição |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

**Texto original**

```original
AF7 — Constraint affordance. The affordance (or deliberate restriction) imposing limits on the length, duration, or structure of expression.
```

**Novo texto**

```novo
AF7. Constraint affordance. The extent to which users can elaborate a message within the limits a platform sets on its length, duration, or structure [9]. The limit itself, such as a character count, is the feature, and the affordance varies from tightly constrained formats to open ones.
```

**Justificativa**: AF7 passa nos critérios de Evans et al. [34] e é o termo da fonte (Jaidka et al.
[9], que tratam de "constraints on message length"). Só a definição fica relacional, separando o
limite (a *feature*, como na 2.3 do paper: "a numerical character limit") da affordance (D24).

---

## T02-A77 — Título da Seção 7.2

| Campo | Valor |
|---|---|
| Lote | 8 |
| Achados | T02.2-F02 |
| Decisões | D22 |
| Localização | Seção 7.2, título (só o texto depois de "7.2. ") |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

**Texto original**

```original
Conceptualizing AF6 as a second-order affordance
```

**Novo texto**

```novo
Audience segmentation and context collapse
```

**Justificativa**: AF6 deixa de ser tratada como affordance de segunda ordem (D22).

---

## T02-A78 — Seção 7.2, parágrafo único

| Campo | Valor |
|---|---|
| Lote | 8 |
| Achados | T02.2-F02 |
| Decisões | D22 |
| Localização | Seção 7.2, parágrafo único, começa com "Unlike the other ten affordances" |
| Ação | substituir-paragrafo |
| Estado | aplicado em 2026-10-16 |

**Texto original**

```original
Unlike the other ten affordances, the context collapse affordance (AF6) does not correspond to the presence of a specific design feature, but rather to the absence of an audience segmentation affordance. boyd [7] treats “invisible audiences” as an emergent consequence of persistence, searchability, and replicability, three of the four properties she identifies as primary, rather than as a fourth property of equal logical status. This distinction is preserved in this article because it directly informs intervention design (Section 7.3). Unlike other affordances, which can be removed or attenuated through product decisions, AF6 can only be mitigated by introducing a new affordance, namely segmentation tools, rather than by stripping away an existing feature.
```

**Novo texto**

```novo
Context collapse could be read as an affordance defined negatively, as the absence of audience segmentation. The threshold criteria of Evans et al. [34] point the other way: affordances invite outcomes but are not outcomes themselves, and context collapse is what results when audiences cannot be segmented. boyd [7] likewise treats invisible audiences as a consequence of persistence, searchability, and replicability rather than as a property of equal status. This article therefore defines AF6 as audience segmentation, an affordance that ranges from fully segmented to fully collapsed audiences, and treats context collapse as its low end. The distinction matters for intervention design (Section 7.3): context collapse is not mitigated by removing a feature but by adding segmentation tools, such as lists, circles, and audience selectors, that move users up this range.
```

**Justificativa**: aplica a D22. Evans et al. [34], p. 40: "Affordances invite behaviors and other
outcomes […] but are not the outcome itself". Mantém a leitura que a v1 faz de boyd [7] (sem PDF) e a
consequência para as intervenções, que já era o argumento da v1. As aspas curvas da v1 em
"invisible audiences" saem (regra de estilo).

# Lote 10 — T02.5, propagação (proposto em 2026-10-16)

Escopo definido pelo usuário em 2026-10-16: 5.1 (contagem e IDs no texto), 5.2 só nas duas
tabelas (consolidada dos mecanismos e matriz de affordances; as figuras ficam para depois) e 5.3
(fechamentos do *feedback loop*). A T02.4 foi adiada. O lote se divide em quatro partes, cada uma
com aprovação própria:

| Parte | Conteúdo | Ajustes | Estado |
|---|---|---|---|
| 10a | Contagem "41" → "39" (12 ocorrências; 11 ajustes) | T02-A79 a T02-A89 | aplicado em 2026-10-16 |
| 10c | Tabela 5 (consolidada, 6.11) e Tabela 6 (matriz de affordances, Seção 8) | T02-A90, T02-A91 | aplicado em 2026-10-16 |
| 10b | IDs antigos no texto corrido fora da 7.1 (5.1, 5.2, 9.1, 9.2, 10.2, 11), com os fechamentos do loop (5.3) | T02-A92 a T02-A118 | aplicado em 2026-10-16 |
| 10d | Seção 7.1: listas "It feeds…" e parágrafos "Why AFx feeds…" | T02-A148 a T02-A199 | aplicado em 2026-10-18 (re-simulado antes; A165 e A166 revisados para tirar AF3 → C3, decisão 3a-1 da T03) |
| 10e | Numeração das citações no texto (deslocamento +2 e +1) | T02-A119 a T02-A147 | aplicado em 2026-10-16 |

**Ações novas no script** (2026-10-16): `revisar-insercao` (troca direta de texto ainda destacado,
inserido por ajuste anterior; recusa se o trecho não estiver todo em verde ou amarelo) e
`substituir-tabela` (risca todo o texto da tabela antiga, achada por uma célula-âncora, e insere a
tabela nova logo abaixo, em verde, com o cabeçalho em negrito).

---

## Parte 10a — Contagem "41" → "39"

Cada ajuste troca só o trecho mínimo que identifica a ocorrência. A Seção 6.1 ainda está em
português (pendência conhecida dos autores; a reescrita da 6.1 é parte da T02.4, adiada): ali a
troca mantém o idioma do trecho.

## T02-A79 — Tabela 2, "41 mechanisms"

| Campo | Valor |
|---|---|
| Lote | 10a |
| Decisões | D36 (lista final de 39) |
| Localização | Tabela 2, linha "Intermediate processes", coluna "Proposed framework" |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
41 mechanisms, each with an ID
```

```novo
39 mechanisms, each with an ID
```

**Justificativa**: contagem da lista final (14.6).

---

## T02-A80 — Seção 3.4, "41 mechanisms as its own unit"

| Campo | Valor |
|---|---|
| Lote | 10a |
| Decisões | D36 |
| Localização | Seção 3.4, parágrafo que contém "treats each of the 41 mechanisms as its own unit" |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
41 mechanisms as its own unit
```

```novo
39 mechanisms as its own unit
```

**Justificativa**: contagem da lista final.

---

## T02-A81 — Seção 5.1, "41 mechanisms in Table"

| Campo | Valor |
|---|---|
| Lote | 10a |
| Decisões | D36 |
| Localização | Seção 5.1, último parágrafo ("A terminological caution applies…"), última frase |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
41 mechanisms in Table
```

```novo
39 mechanisms in Table
```

**Justificativa**: contagem da lista final.

---

## T02-A82 — Seção 6.1, "os 41 mecanismos, cabe"

| Campo | Valor |
|---|---|
| Lote | 10a |
| Decisões | D36 |
| Localização | Seção 6.1, parágrafo 1 ("Antes de apresentar os 41 mecanismos…") |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
os 41 mecanismos, cabe
```

```novo
os 39 mecanismos, cabe
```

**Justificativa**: contagem da lista final. A seção ainda está em português (pendência dos
autores), e a troca mantém o idioma do trecho.

---

## T02-A83 — Seção 6.1, "dos 41 mecanismos foi classificada"

| Campo | Valor |
|---|---|
| Lote | 10a |
| Decisões | D36 |
| Localização | Seção 6.1, parágrafo sobre *Claim* ("A maioria dos 41 mecanismos…") |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
dos 41 mecanismos foi classificada
```

```novo
dos 39 mecanismos foi classificada
```

**Justificativa**: idem T02-A82.

---

## T02-A84 — Legenda da tabela consolidada

| Campo | Valor |
|---|---|
| Lote | 10a |
| Decisões | D36 |
| Localização | Seção 6.11, legenda "Table 5. Complete mechanism taxonomy (41 mechanisms)." |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
(41 mechanisms).
```

```novo
(39 mechanisms).
```

**Justificativa**: contagem da lista final.

---

## T02-A85 — Seção 8, "all 41 individual mechanisms"

| Campo | Valor |
|---|---|
| Lote | 10a |
| Decisões | D36 |
| Localização | Seção 8, parágrafo sobre a Figura 4 ("Figure 4 illustrates, as a bipartite network…") |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
all 41 individual mechanisms
```

```novo
all 39 individual mechanisms
```

**Justificativa**: contagem da lista final. O texto também diz que a Figura 4 agrupa os mecanismos
em "nine families", o que muda para sete blocos (D6); fica para a revisão das figuras.

---

## T02-A86 — Seção 9.1, "all 41 mechanisms (Section 6.11"

| Campo | Valor |
|---|---|
| Lote | 10a |
| Decisões | D36 |
| Localização | Seção 9.1, parágrafo "The individual evidentiary assessment of all 41 mechanisms…" |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
all 41 mechanisms (Section 6.11
```

```novo
all 39 mechanisms (Section 6.11
```

**Justificativa**: contagem da lista final.

---

## T02-A87 — Seção 9.2, "the 41 mechanisms concentrates"

| Campo | Valor |
|---|---|
| Lote | 10a |
| Decisões | D36 |
| Localização | Seção 9.2, segunda limitação ("The second limitation concerns the composition…") |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
the 41 mechanisms concentrates
```

```novo
the 39 mechanisms concentrates
```

**Justificativa**: contagem da lista final.

---

## T02-A88 — Seção 11, "identified 41 mechanisms and 11 affordances"

| Campo | Valor |
|---|---|
| Lote | 10a |
| Decisões | D36 |
| Localização | Seção 11, parágrafo 1 ("This article proposed a four-tier framework…") |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
identified 41 mechanisms and 11 affordances
```

```novo
identified 39 mechanisms and 11 affordances
```

**Justificativa**: contagem da lista final.

---

## T02-A89 — Seção 11, item 1, texto inserido pela T01 (revisão direta)

| Campo | Valor |
|---|---|
| Lote | 10a |
| Decisões | D36; política de ajustes (revisão de texto ainda destacado) |
| Localização | Seção 11, item 1, texto em amarelo inserido por T01-A14 ("As discussed in Sections 4.1 and 9.2…") |
| Ação | revisar-insercao |
| Estado | aplicado em 2026-10-16 |

```original
whether the 41 mechanisms and 11 affordances cover
```

```novo
whether the 39 mechanisms and 11 affordances cover
```

**Justificativa**: o trecho é texto inserido pela T01 e ainda destacado em amarelo. Pela política de
ajustes, é trocado diretamente, sem riscar. A ocorrência equivalente no texto original dos autores
já está riscada (T01-A14).

---

## Parte 10c — Tabelas

## T02-A90 — Tabela 5, taxonomia consolidada dos mecanismos

| Campo | Valor |
|---|---|
| Lote | 10c |
| Achados | T01-I03 (coluna Ref com a numeração do texto), T02.1-F02 a F06 |
| Decisões | D6, D13–D36 |
| Localização | Seção 6.11, tabela logo abaixo da legenda "Table 5. Complete mechanism taxonomy" |
| Ação | substituir-tabela |
| Estado | aplicado em 2026-10-16 |

**Âncora** (célula da tabela antiga)

```ancora
Informational isolation/segregation
```

**Nova tabela**

```tabela
| ID | Mechanism | Outcome | Claim | Evidence | Ref |
|---|---|---|---|---|---|
| A1 | Filter bubble | Ideological | Amplifies | Mixed | [44,45] |
| A2 | Algorithmic amplification | Affective, Ideological | Amplifies | Moderate–mixed | [14] |
| A3 | Algorithmic radicalization | Ideological | Amplifies | Mixed | [56,57] |
| A4 | Algorithmic agenda-setting | Perceived | Amplifies | Plausible | [16,21] |
| B1 | Homophily | Structural | Hosts & amplifies | Strong (existence), moderate (platform role) | [37] |
| B2 | Echo chamber | Ideological, Structural | Amplifies | Mixed | [46] |
| B3 | Group polarization | Ideological | Amplifies | Strong (lab), moderate (online) | [61] |
| B4 | Information cascades | Ideological, Perceived | Amplifies | Moderate | [51,52] |
| B5 | Moral contagion | Affective | Amplifies | Moderate | [67] |
| B6 | Partisan sorting | Affective | Hosts (amplifies) | Moderate | [62] |
| B7 | Interpersonal political tension | Affective, Perceived | Amplifies | Moderate | [5] |
| B8 | Online community radicalization | Ideological, Affective | Amplifies | Moderate | [76] |
| C1 | Motivated reasoning | Ideological, Affective | Hosts | Strong (phenomenon), magnitude debated | [63] |
| C2 | Confirmation bias | Ideological, Affective | Hosts | Strong (phenomenon), weak (induced) | [48] |
| C3 | Selective avoidance | Structural, Ideological | Hosts & amplifies | Mixed | [107,108] |
| C4 | Biased assimilation | Ideological | Hosts | Moderate | [65] |
| C5 | Hostile media effect | Affective | Hosts | Moderate | [23] |
| C6 | Illusory truth effect | Ideological, Perceived | Amplifies | Strong | [66] |
| C7 | News avoidance | Structural (indirect), Behavioral | Hosts & amplifies | Plausible | [79,80] |
| C8 | Reinforcing spiral | Varies | Amplifies | Plausible | [55] |
| D1 | Vocal minority | Perceived, Affective | Amplifies | Moderate | [68] |
| D2 | Social proof | Perceived, Ideological | Amplifies | Moderate | [41] |
| D3 | False consensus | Perceived | Hosts & amplifies | Moderate | [39] |
| D4 | Pluralistic ignorance | Perceived | Hosts & amplifies | Moderate | [40] |
| D5 | Spiral of silence | Perceived, Behavioral | Amplifies | Mixed | [24] |
| D6 | Exaggerated meta-perceptions | Affective, Perceived | Amplifies | Strong (phenomenon), moderate (platforms) | [10,11] |
| E1 | Social learning of outrage | Affective | Amplifies | Moderate | [13,71] |
| E2 | Identity signaling | Affective | Amplifies | Plausible | [69] |
| E3 | Metric-driven content production | Affective | Creates (incentive) | Plausible | [102] |
| F1 | Online disinhibition effect | Affective | Amplifies | Mixed | [72] |
| F2 | Dogpiling | Behavioral, Affective | Amplifies | Plausible | [73] |
| F3 | Message brevity | Affective | Amplifies | Plausible | [9] |
| F4 | Incivility contagion | Behavioral, Affective | Amplifies | Moderate | [50] |
| F5 | Incivility exposure effect | Ideological, Affective | Amplifies | Moderate | [49,50] |
| G1 | Gatekeeping decline | Ideological, Perceived | Amplifies | Plausible | [17,74] |
| G2 | Propaganda feedback loop | Ideological, Perceived | Amplifies | Moderate (strong in the U.S.) | [75] |
| G3 | Manufactured consensus | Perceived, Affective | Amplifies | Mixed | [54] |
| G4 | Platform migration | Structural, Affective | Amplifies or hosts | Mixed | [77] |
| G5 | Perceived censorship | Affective | Amplifies | Plausible | [78] |
```

**Justificativa**: lista final da 14.6 (D36), com os nomes das fichas aplicadas nos lotes 1–7.
- **Coluna Ref**: passa a usar a **numeração da lista** de referências (resolve T01-I03 e O07 nesta
  tabela; ex.: na v1, M1 → "[39]", que na lista é Ross et al.). Cada célula traz a(s) fonte(s)
  definidora(s) citada(s) na ficha.
- **Valores mantidos da v1** para *Claim* e *Evidence* sempre que o item não mudou de conteúdo. A
  revisão geral das escalas (valores compostos, T01-I02) segue fora do escopo.
- **Valores alterados para ficar coerentes com as fichas**: A1 (de M1; outcome só Ideological, a
  via algorítmica), B2 (de M1; Ideological, Structural), B8 (+Affective, D32), C3 (evidência Mixed,
  D34), D6 (Affective, Perceived: o mecanismo leva da percepção ao afeto, D17), E2 (evidência
  Plausible: a ficha declara base sobretudo teórica), F3 (Affective: civilidade, Jaidka et al.),
  F4 (Behavioral, Affective: o contágio é comportamento), F5 (Ideological, Affective, de M3:
  Anderson et al.), G2 (Ideological, Perceived).
- **Fusões**: B1 (A3), B4 (M4), E1 (E4) mantêm os valores do item principal. A4 da v1 sai.
- **C8** fica com os valores de M6, provisório até o backlog B02.

---

## T02-A91 — Tabela 6, matriz de affordances

| Campo | Valor |
|---|---|
| Lote | 10c |
| Achados | T02.2-F02; T01-I03 (numeração das citações) |
| Decisões | D20–D25, D36 |
| Localização | Seção 8, tabela logo abaixo da legenda "Table 6. Complete affordance matrix." |
| Ação | substituir-tabela |
| Estado | aplicado em 2026-10-16 |

**Âncora** (célula do cabeçalho da tabela antiga)

```ancora
Mechanisms fed
```

**Nova tabela**

```tabela
| ID | Affordance | Alt. nomenclature | Mechanisms fed | Known intervention(s) |
|---|---|---|---|---|
| AF1 | Algorithmic content curation | algorithmic selection | A1, A2, A3, A4, B5, C3*, C6, C7, C8, D1, D6, G2, G3 | Chronological feed, tested, no detected attitude effect [94] |
| AF2 | Network-informed associating | connection recommendation, friend recommendation | B1, B2*, B3*, D3*, D4* | Diversity-weighted recommendation, tested by simulation [59] |
| AF3 | Asymmetric following | directed association | B1, B2*, B3*, B7*, C3, D3*, D4* | Paid cross-cutting exposure, tested in the field, reverse effect [84] |
| AF4 | Social quantification | metavoicing, metrification of sociality | B4, B7*, D2, E1, E2, G3 | Hiding public counters, industry practice, not peer-reviewed |
| AF5 | Replicability | n/a | B4, D6, E2 | Forward limits and accuracy nudges, tested [98] |
| AF6 | Audience segmentation | context collapse (low end) | B7, D5, F2, F4 | Audience segmentation tools, under-tested |
| AF7 | Constraint affordance | n/a | A4, F3 | Character limit expansion, tested, robust [9] |
| AF8 | Identifiability | anonymity–identifiability spectrum | F1, F2, G3 | Revise-before-post prompts, tested [95] |
| AF9 | Infinite scroll | absence of stopping cues | A2, B5, C6, C7 | Autoplay removal, open question |
| AF10 | Platform governance | n/a | G1, G4, G5 | Deplatforming, tested, heterogeneous [77]. Transparency, tested [97] |
| AF11 | Group/community formation | n/a | B6, B8 | Community quarantine, under-tested |
```

**Justificativa**:
- **Nomes e alternativos**: AF1 (sai *engagement-based ranking*, D20), AF2 (*network-informed
  associating*, D21), AF4 (+*metavoicing*, D23), AF6 (*audience segmentation*, D22; sai
  "(2nd-order)").
- **Mecanismos alimentados**: os IDs da v1 convertidos pela correspondência da 14.6 (ex.: AF1: A1 →
  A2, A2 → A3, A5 → A4, C4 → C6, C5 → B5, D2 → D6, H1 → C7, H2* → C3*, M5 → G3, M6 → C8). M1*
  vira A1 (direto, porque a ficha de A1 liga a bolha de filtro a AF1) e B2* (em AF2 e AF3). A4 da
  v1 sai de AF6. D3* da v1 vira D3* e D4*. Ligações acrescentadas porque as fichas novas as
  declaram: C3 em AF3 (T02-A27) e E2 em AF4 (T02-A52). O asterisco continua indicando ligação
  indireta.
- **Coluna de intervenções**: texto mantido, com as citações convertidas para a numeração da lista
  (no trecho, o texto estava deslocado em +2 a partir de [94], e em +1 em [60] e [86]): Guess et
  al. [94], Santos et al. [59], Bail et al. [84], Rathje et al. 2022 [98], Jaidka et al. [9],
  Katsaros et al. [95], Horta Ribeiro et al. [77], Jhaver et al. [97]. A correspondência foi feita
  pelo tema de cada intervenção e confere com o deslocamento observado (P3); vale conferir na
  tarefa de verificação de referências.
- **Estilo**: os ";" que vinham da v1 dentro das células viram vírgula (ou ponto, na coluna de
  intervenções de AF10), e o "—" das células vazias de nomes alternativos vira "n/a".

## Parte 10b — IDs e nomes no texto corrido, fechamentos do loop (5.3) e recontagem da 9.1

Escopo: Seções 5.1, 5.2, 9.1, 9.2, 10.2 e 11. Ficam de fora a Seção 7 (parte 10d) e os
parágrafos da Seção 8 que descrevem a Figura 4 ("nine families", hubs), porque dependem da revisão
das figuras. Os números de seção citados seguem a numeração atual (Bloco A = 6.3 … Bloco G = 6.9).
Quando o título do Bloco M (6.2) sair, todas as referências "Section 6.x" do texto deslocam uma
posição (anotado no backlog, B05). Os trechos em amarelo nestes parágrafos são revisões dos
próprios autores, não inserções da T01, e por isso são riscados como texto original.

## T02-A92 — Seção 5.1, exemplo da cadeia de três elos

| Campo | Valor |
|---|---|
| Lote | 10b |
| Decisões | D21 (AF2 = network-informed associating, A3 fundido em B1) |
| Localização | Seção 5.1, parágrafo "The connection recommendation affordance, for instance…" |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
The connection recommendation affordance, for instance, does not directly produce structural polarization — it makes it more likely that the homophily and clustering mechanism (Section 6.3) operates
```

```novo
The network-informed associating affordance (AF2), for instance, does not directly produce structural polarization. It makes it more likely that the homophily mechanism (B1, Section 6.4) operates
```

**Justificativa**: nome novo de AF2 e de B1, com os IDs, e seção do Bloco B.

---

## T02-A93 — Seção 5.1, bifurcação de AF3

| Campo | Valor |
|---|---|
| Lote | 10b |
| Decisões | D36 (B5 v1 → B7) |
| Localização | Seção 5.1, parágrafo "A terminological caution applies…" |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
B5 (Interpersonal tension & identity salience activation) — two mechanisms
```

```novo
B7 (Interpersonal political tension), two mechanisms
```

**Justificativa**: ID e nome novos. O par B1/B7 continua sendo o exemplo de enactments opostos da
mesma affordance (a ligação AF3 → B7 aparece como indireta na Tabela 6).

---

## T02-A94 — Seção 5.2, primeiro fechamento do loop

| Campo | Valor |
|---|---|
| Lote | 10b |
| Decisões | D36 (fechamento 1: D5 → AF2 → B1), D21 |
| Localização | Seção 5.2, parágrafo "At the first point…" |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
the spiral of silence (mechanism M7, Section 6.2) — the self-censorship of moderate voices in an environment perceived as hostile [Noelle-Neumann, 24] — alters the behavioral data on which connection-recommendation systems (AF2) are trained
```

```novo
the spiral of silence (D5, Section 6.6), the self-censorship of moderate voices in an environment perceived as hostile [Noelle-Neumann, 24], alters the behavioral data on which the recommendation systems behind network-informed associating (AF2) are trained
```

**Justificativa**: M7 virou D5 (Bloco D, Seção 6.6). AF2 com o nome novo.

---

## T02-A95 — Seção 5.2, segundo fechamento do loop

| Campo | Valor |
|---|---|
| Lote | 10b |
| Decisões | D36 (fechamento 2: E1 → AF1 → B5), D20 |
| Localização | Seção 5.2, parágrafo "At the second point…" |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
socially rewarded expression of moral outrage — a mechanism that Brady et al. [13] show operates through reinforcement learning in social networks — feeds back into engagement-based ranking (AF1): content hostile to the out-group generates more engagement [Rathje et al., 38], which the algorithm learns to prioritize [Milli et al., 14], which in turn exposes more users to that type of content, closing the loop.
```

```novo
the social learning of outrage (E1, Section 6.7), which Brady et al. [13] show operates through reinforcement learning in social networks, feeds back into algorithmic content curation (AF1). Content hostile to the out-group generates more engagement [Rathje et al., 38], which the algorithm learns to prioritize [Milli et al., 14]. More users are then exposed to moralized content, which spreads further through moral contagion (B5, Section 6.4) and closes the loop.
```

**Justificativa**: o fechamento passa a nomear os dois mecanismos da lista final (E1 na origem, B5
no reforço) e AF1 pelo nome da matriz (D20 tirou *engagement-based ranking* dos alternativos).

---

## T02-A96 — Seção 5.2, terceiro fechamento do loop

| Campo | Valor |
|---|---|
| Lote | 10b |
| Decisões | D36 (fechamento 3: D3/D4 → AF4), D33 (D3 v1 dividido em D3 e D4) |
| Localização | Seção 5.2, parágrafo "At the third point…" |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
false consensus within homogeneous clusters [Ross et al., 39] and the pluralistic ignorance that keeps dissenters silent [Prentice and Miller, 40]
```

```novo
false consensus (D3) within homogeneous clusters [Ross et al., 39] and the pluralistic ignorance (D4) that keeps dissenters silent [Prentice and Miller, 40], both in Section 6.6,
```

**Justificativa**: acrescenta os IDs dos dois mecanismos, agora separados.

---

## T02-A97 — Seção 9.1, nome de AF2

| Campo | Valor |
|---|---|
| Lote | 10b |
| Decisões | D21 |
| Localização | Seção 9.1, parágrafo "The distinction between features and affordances…" |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
affordances, Connection recommendation (AF2)
```

```novo
affordances, Network-informed associating (AF2)
```

**Justificativa**: nome novo. Ver a ressalva na apresentação do lote: o argumento desse parágrafo
(quatro affordances cujo rótulo mais citado é amplo demais) precisa ser reavaliado depois de D21–D23.

---

## T02-A98 — Seção 9.1, F3

| Campo | Valor |
|---|---|
| Lote | 10b |
| Decisões | D35/F3 (Message brevity) |
| Localização | Seção 9.1, parágrafo "The individual evidentiary assessment…" |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
via Low-context communication (F3)
```

```novo
via Message brevity (F3)
```

**Justificativa**: nome novo de F3.

---

## T02-A99 — Seção 9.1, mecanismos ligados à polarização percebida e recontagem

| Campo | Valor |
|---|---|
| Lote | 10b |
| Decisões | D6, D17, D33, D36; Tabela 5 nova (T02-A90) |
| Localização | Seção 9.1, parágrafo "Furthermore, formalizing perceived polarization…" |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
The four mechanisms of Block D (Perceptual distortion), namely Vocal minority / extremity bias (D1), False polarization (D2), False consensus & pluralistic ignorance (D3), and Social proof (D4), as well as two additional mechanisms, Algorithmic agenda-setting (A5) and Coordinated inauthentic behavior (M5), feature perceived polarization as a primary or secondary outcome. This represents the second highest concentration of mechanisms after affective polarization (fifteen mechanisms) and ahead of structural polarization (six mechanisms),
```

```novo
The six mechanisms of Block D (Perceptions of others), namely Vocal minority (D1), Social proof (D2), False consensus (D3), Pluralistic ignorance (D4), Spiral of silence (D5), and Exaggerated meta-perceptions (D6), together with seven mechanisms from other blocks, Algorithmic agenda-setting (A4), Information cascades (B4), Interpersonal political tension (B7), Illusory truth effect (C6), Gatekeeping decline (G1), Propaganda feedback loop (G2), and Manufactured consensus (G3), feature perceived polarization as a primary or secondary outcome. These thirteen mechanisms form the third largest group, after those tied to affective polarization (twenty-one) and ideological polarization (sixteen), and well ahead of structural (five) and behavioral polarization (four), since a mechanism can feed more than one outcome,
```

**Justificativa**: recontagem pela coluna Outcome da Tabela 5 nova. Afetiva 21, ideológica 16,
percebida 13, estrutural 5, comportamental 4 (C8, "Varies", fica fora). A v1 dizia que a percebida
era a segunda, atrás só da afetiva. Com a lista nova, a ideológica passa à frente, e o texto diz
isso. A conclusão do parágrafo ("one of the framework's most generative dimensions") continua
sustentada por 13 de 39.

---

## T02-A100 — Seção 9.1, seção da Figura 3

| Campo | Valor |
|---|---|
| Lote | 10b |
| Decisões | correção factual |
| Localização | Seção 9.1, parágrafo "Finally, while the feedback loop illustrated in Figure 3…" |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
Figure 3 (Section 2)
```

```novo
Figure 3 (Section 5.2)
```

**Justificativa**: a Figura 3 está na Seção 5.2.

---

## T02-A101 — Seção 9.1, G4

| Campo | Valor |
|---|---|
| Lote | 10b |
| Decisões | lote 7 (G4 Platform migration) |
| Localização | mesmo parágrafo |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
G4 (deplatforming and migration)
```

```novo
G4 (platform migration)
```

**Justificativa**: nome novo.

---

## T02-A102 — Seção 9.1, B4 v1 → B6

| Campo | Valor |
|---|---|
| Lote | 10b |
| Decisões | D36 (B4 v1 → B6 Partisan sorting) |
| Localização | mesmo parágrafo |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
B4 (sorting)
```

```novo
B6 (partisan sorting)
```

**Justificativa**: ID e nome novos.

---

## T02-A103 — Seção 9.2, G2

| Campo | Valor |
|---|---|
| Lote | 10b |
| Decisões | G2 Propaganda feedback loop (lote 7) |
| Localização | Seção 9.2, segunda limitação |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
Mechanism G2 (Network propaganda)
```

```novo
Mechanism G2 (Propaganda feedback loop)
```

**Justificativa**: nome novo.

---

## T02-A104 — Seção 9.2, B5 v1 → B7 (1/2)

| Campo | Valor |
|---|---|
| Lote | 10b |
| Decisões | D36 |
| Localização | Seção 9.2, terceira limitação |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
Mechanism B5 (Interpersonal tension and identity salience activation)
```

```novo
Mechanism B7 (Interpersonal political tension)
```

**Justificativa**: ID e nome novos.

---

## T02-A105 — Seção 9.2, B5 v1 → B7 (2/2)

| Campo | Valor |
|---|---|
| Lote | 10b |
| Decisões | D36 |
| Localização | mesmo parágrafo, última frase |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
Consequently, B5 should be
```

```novo
Consequently, B7 should be
```

**Justificativa**: ID novo.

---

## T02-A106 — Seção 9.2, quarta limitação

| Campo | Valor |
|---|---|
| Lote | 10b |
| Decisões | D36 |
| Localização | Seção 9.2, quarta limitação, última frase |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
feeds Interpersonal tension & identity salience (B5)
```

```novo
feeds Interpersonal political tension (B7)
```

**Justificativa**: ID e nome novos.

---

## T02-A107 — Seção 10.2, primeiro item, mecanismos de AF1

| Campo | Valor |
|---|---|
| Lote | 10b |
| Decisões | D36 (C5 v1 → B5, M6 → C8) |
| Localização | Seção 10.2, parágrafo "First, newsrooms distributing content…" |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
C5 (negativity bias and moral-emotional contagion) and M6 (reinforcement spirals)
```

```novo
B5 (moral contagion) and C8 (reinforcing spiral)
```

**Justificativa**: IDs e nomes novos.

---

## T02-A108 — Seção 10.2, primeiro item, métricas na redação

| Campo | Valor |
|---|---|
| Lote | 10b |
| Decisões | D36 (E4 fundido em E1), E3 (lote 5) |
| Localização | mesmo parágrafo, duas últimas frases |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
[Petre, 104] documents how the internal visibility of engagement performance shapes editorial decision-making in a manner directly analogous to how E4 (social quantification and status metrics) influences individual users. This framework elevates that parallel from an intuitive observation to a theoretical foundation.
```

```novo
[Petre, 102] documents how the internal visibility of engagement performance shapes editorial decision-making. The framework treats this process as a mechanism of its own, E3 (metric-driven content production), which turns an intuitive observation about newsrooms into a testable hypothesis.
```

**Justificativa**: E4 não existe mais (fundido em E1). A analogia com usuários comuns perdeu o
objeto, e o próprio processo descrito por Petre virou o mecanismo E3, cuja ficha cita Petre e
nomeia as redações. A citação passa a usar o número da lista (Petre é [102]).

---

## T02-A109 — Seção 10.2, segundo item, G1

| Campo | Valor |
|---|---|
| Lote | 10b |
| Decisões | G1 Gatekeeping decline (lote 7) |
| Localização | Seção 10.2, parágrafo "Second, the erosion of traditional editorial gatekeeping…" |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
G1 (disintermediation and gatekeeping erosion, Section 6.9)
```

```novo
G1 (gatekeeping decline, Section 6.9)
```

**Justificativa**: nome novo.

---

## T02-A110 — Seção 10.2, segundo item, G2

| Campo | Valor |
|---|---|
| Lote | 10b |
| Decisões | G2 (lote 7) |
| Localização | mesmo parágrafo, última frase |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
Network propaganda (G2) in Section 6.9
```

```novo
the Propaganda feedback loop (G2) in Section 6.9
```

**Justificativa**: nome novo.

---

## T02-A111 — Seção 10.2, terceiro item, os dois mecanismos de evitação

| Campo | Valor |
|---|---|
| Lote | 10b |
| Decisões | D34, D36 (H1 → C7, H2 → C3) |
| Localização | Seção 10.2, parágrafo "Third, the two avoidance mechanisms…" |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
News avoidance (H1) and Selective/partisan news avoidance (H2)
```

```novo
News avoidance (C7) and Selective avoidance (C3)
```

**Justificativa**: IDs e nomes novos.

---

## T02-A112 — Seção 10.2, terceiro item, seção

| Campo | Valor |
|---|---|
| Lote | 10b |
| Decisões | D36 |
| Localização | mesmo parágrafo |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
(Section 6.10)
```

```novo
(Section 6.5)
```

**Justificativa**: os dois mecanismos estão agora no Bloco C (Seção 6.5).

---

## T02-A113 — Seção 10.2, terceiro item, fonte da assimetria partidária

| Campo | Valor |
|---|---|
| Lote | 10b |
| Achados | T02.1 (atribuição de assimetria partidária a Skovsgaard e Andersen) |
| Decisões | D34 |
| Localização | mesmo parágrafo |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
[Skovsgaard and Andersen, 80] operates asymmetrically
```

```novo
[Heseltine et al., 108] operates asymmetrically
```

**Justificativa**: Skovsgaard e Andersen [80] conceituam a evitação de notícias e não testam
assimetria partidária. Heseltine et al. [108] encontram assimetrias partidárias no nível macro
("partisan asymmetries emerge", p. 1541): com cobertura negativa do próprio partido, republicanos
migram para veículos alinhados e democratas reduzem o volume de notícias (pp. 1550–1551, 1554).

---

## T02-A114 — Seção 10.2, terceiro item, IDs na última comparação

| Campo | Valor |
|---|---|
| Lote | 10b |
| Decisões | D36 |
| Localização | mesmo parágrafo |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
general news avoidance (H1) and selective partisan avoidance (H2)
```

```novo
general news avoidance (C7) and selective avoidance (C3)
```

**Justificativa**: IDs e nome novos.

---

## T02-A115 — Seção 11, AF6

| Campo | Valor |
|---|---|
| Lote | 10b |
| Decisões | D22 (AF6 = audience segmentation) |
| Localização | Seção 11, item "Systematic comparisons between mainstream and alternative platforms" |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
the absence of audience collapse (AF6)
```

```novo
finer audience segmentation (AF6)
```

**Justificativa**: AF6 passou a ser a segmentação de audiência, e o colapso de contexto é o extremo
baixo dela. A frase diz o mesmo pelo lado positivo.

---

## T02-A116 — Seção 11, M7 → D5

| Campo | Valor |
|---|---|
| Lote | 10b |
| Decisões | D36 |
| Localização | mesmo parágrafo |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
Dogpiling (F2) and Spiral of silence (M7)
```

```novo
Dogpiling (F2) and Spiral of silence (D5)
```

**Justificativa**: ID novo.

---

## T02-A117 — Seção 11, mecanismos de AF4

| Campo | Valor |
|---|---|
| Lote | 10b |
| Decisões | D36 (E4 fundido em E1), Tabela 6 nova |
| Localização | mesmo parágrafo |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
Social learning of outrage (E1) and Social quantification / vanity metrics (E4). These propositions
```

```novo
Social learning of outrage (E1) and Identity signaling (E2). These propositions
```

**Justificativa**: E4 foi fundido em E1. O segundo exemplo passa a ser E2, que AF4 também alimenta
na matriz nova.

---

## T02-A118 — Seção 11, G2

| Campo | Valor |
|---|---|
| Lote | 10b |
| Decisões | G2 (lote 7) |
| Localização | Seção 11, item "Geographical and institutional extension…" |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
G2 (network propaganda)
```

```novo
G2 (propaganda feedback loop)
```

**Justificativa**: nome novo.

## Parte 10e — Numeração das citações no texto

Pedida pelo usuário em 2026-10-16. Cruzamento automático de todas as citações com autor do texto
("Autor [n]", "[Autor, n]" e listas com ";") contra a lista de referências, mais conferência manual
das citações só numéricas. Achados: de Kwak et al. a Bak-Coleman et al. o texto está deslocado +2
em relação à lista (Seções 7.1, 7.3, 9.1, 10.1 e 10.2), exceto Henrich [99] e Munger [100], que estão
certas. Chaney et al. e Mason estão deslocados +1 na Seção 7.1. Diakopoulos [107] e Napoli [108]
colidiam com Garrett [107] e Heseltine [108]. As citações só numéricas (Seção 6) conferem. Todos os
trechos são texto dos autores (riscar e inserir em verde). As colunas Ref e de intervenções das
Tabelas 5 e 6 já foram corrigidas em T02-A90 e A91.

## T02-A119 — 7.1, AF2, Chaney et al. [59 → [58]

| Campo | Valor |
|---|---|
| Lote | 10e |
| Achados | T01-I03, T02 (P3) |
| Localização | Seção 7.1, AF2, parágrafo P204 do dump |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
Chaney et al. [59]
```

```novo
Chaney et al. [58]
```

**Justificativa**: número da lista de referências (entrada [58]).

---

## T02-A120 — 7.1, AF3, Kwak et al. [85 → [83]

| Campo | Valor |
|---|---|
| Lote | 10e |
| Achados | T01-I03, T02 (P3) |
| Localização | Seção 7.1, AF3, parágrafo P205 do dump |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
will. Kwak et al. [85]
```

```novo
will. Kwak et al. [83]
```

**Justificativa**: número da lista de referências (entrada [83]).

---

## T02-A121 — 7.1, AF3, Bail et al. [86 → [84]

| Campo | Valor |
|---|---|
| Lote | 10e |
| Achados | T01-I03, T02 (P3) |
| Localização | Seção 7.1, AF3, parágrafo P205 do dump |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
experiment, Bail et al. [86]
```

```novo
experiment, Bail et al. [84]
```

**Justificativa**: número da lista de referências (entrada [84]).

---

## T02-A122 — 7.1, AF3, Bail et al. [86 → [84]

| Campo | Valor |
|---|---|
| Lote | 10e |
| Achados | T01-I03, T02 (P3) |
| Localização | Seção 7.1, AF3, parágrafo P208 do dump |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
by Bail et al. [86]
```

```novo
by Bail et al. [84]
```

**Justificativa**: número da lista de referências (entrada [84]).

---

## T02-A123 — 7.1, AF4, Gerlitz and Helmond [87 → [85]

| Campo | Valor |
|---|---|
| Lote | 10e |
| Achados | T01-I03, T02 (P3) |
| Localização | Seção 7.1, AF4, parágrafo P209 do dump |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
Gerlitz and Helmond [87]
```

```novo
Gerlitz and Helmond [85]
```

**Justificativa**: número da lista de referências (entrada [85]).

---

## T02-A124 — 7.1, AF5, Fatima Oliveira [88 → [86]

| Campo | Valor |
|---|---|
| Lote | 10e |
| Achados | T01-I03, T02 (P3) |
| Localização | Seção 7.1, AF5, parágrafo P213 do dump |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
Fatima Oliveira [88]
```

```novo
Fatima Oliveira [86]
```

**Justificativa**: número da lista de referências (entrada [86]).

---

## T02-A125 — 7.1, AF5, Fatima Oliveira, 88 → [86]

| Campo | Valor |
|---|---|
| Lote | 10e |
| Achados | T01-I03, T02 (P3) |
| Localização | Seção 7.1, AF5, parágrafo P216 do dump |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
Fatima Oliveira, 88]
```

```novo
Fatima Oliveira, 86]
```

**Justificativa**: número da lista de referências (entrada [86]).

---

## T02-A126 — 7.1, AF8, Marx [89 → [87]

| Campo | Valor |
|---|---|
| Lote | 10e |
| Achados | T01-I03, T02 (P3) |
| Localização | Seção 7.1, AF8, parágrafo P225 do dump |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
pseudonymity. Marx [89]
```

```novo
pseudonymity. Marx [87]
```

**Justificativa**: número da lista de referências (entrada [87]).

---

## T02-A127 — 7.1, AF8, Hogan [90 → [88]

| Campo | Valor |
|---|---|
| Lote | 10e |
| Achados | T01-I03, T02 (P3) |
| Localização | Seção 7.1, AF8, parágrafo P225 do dump |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
Hogan [90]
```

```novo
Hogan [88]
```

**Justificativa**: número da lista de referências (entrada [88]).

---

## T02-A128 — 7.1, AF8, Lapidot-Lefler and Barak [91 → [89]

| Campo | Valor |
|---|---|
| Lote | 10e |
| Achados | T01-I03, T02 (P3) |
| Localização | Seção 7.1, AF8, parágrafo P228 do dump |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
Lapidot-Lefler and Barak [91]
```

```novo
Lapidot-Lefler and Barak [89]
```

**Justificativa**: número da lista de referências (entrada [89]).

---

## T02-A129 — 7.1, AF9, Monge Roffarello et al. [92 → [90]

| Campo | Valor |
|---|---|
| Lote | 10e |
| Achados | T01-I03, T02 (P3) |
| Localização | Seção 7.1, AF9, parágrafo P229 do dump |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
Monge Roffarello et al. [92]
```

```novo
Monge Roffarello et al. [90]
```

**Justificativa**: número da lista de referências (entrada [90]).

---

## T02-A130 — 7.1, AF9, Lukoff et al. [93 → [91]

| Campo | Valor |
|---|---|
| Lote | 10e |
| Achados | T01-I03, T02 (P3) |
| Localização | Seção 7.1, AF9, parágrafo P229 do dump |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
Lukoff et al. [93]
```

```novo
Lukoff et al. [91]
```

**Justificativa**: número da lista de referências (entrada [91]).

---

## T02-A131 — 7.1, AF10, Gillespie [94 → [92]

| Campo | Valor |
|---|---|
| Lote | 10e |
| Achados | T01-I03, T02 (P3) |
| Localização | Seção 7.1, AF10, parágrafo P233 do dump |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
Gillespie [94]
```

```novo
Gillespie [92]
```

**Justificativa**: número da lista de referências (entrada [92]).

---

## T02-A132 — 7.1, AF10, Klonick [95 → [93]

| Campo | Valor |
|---|---|
| Lote | 10e |
| Achados | T01-I03, T02 (P3) |
| Localização | Seção 7.1, AF10, parágrafo P233 do dump |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
Klonick [95]
```

```novo
Klonick [93]
```

**Justificativa**: número da lista de referências (entrada [93]).

---

## T02-A133 — 7.1, AF11, Mason [63 → [62]

| Campo | Valor |
|---|---|
| Lote | 10e |
| Achados | T01-I03, T02 (P3) |
| Localização | Seção 7.1, AF11, parágrafo P237 do dump |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
individual ties. Mason [63]
```

```novo
individual ties. Mason [62]
```

**Justificativa**: número da lista de referências (entrada [62]).

---

## T02-A134 — 7.1, AF11, Mason, 63 → [62]

| Campo | Valor |
|---|---|
| Lote | 10e |
| Achados | T01-I03, T02 (P3) |
| Localização | Seção 7.1, AF11, parágrafo P240 do dump |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
[Mason, 63]
```

```novo
[Mason, 62]
```

**Justificativa**: número da lista de referências (entrada [62]).

---

## T02-A135 — 7.3, Guess et al. [96 → [94]

| Campo | Valor |
|---|---|
| Lote | 10e |
| Achados | T01-I03, T02 (P3) |
| Localização | Seção 7.3, parágrafo P246 do dump |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
Guess et al. [96]
```

```novo
Guess et al. [94]
```

**Justificativa**: número da lista de referências (entrada [94]).

---

## T02-A136 — 7.3, Bail et al. [86 → [84]

| Campo | Valor |
|---|---|
| Lote | 10e |
| Achados | T01-I03, T02 (P3) |
| Localização | Seção 7.3, parágrafo P246 do dump |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
in Bail et al. [86]
```

```novo
in Bail et al. [84]
```

**Justificativa**: número da lista de referências (entrada [84]).

---

## T02-A137 — 7.3, Katsaros et al. [97 → [95]

| Campo | Valor |
|---|---|
| Lote | 10e |
| Achados | T01-I03, T02 (P3) |
| Localização | Seção 7.3, parágrafo P246 do dump |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
Katsaros et al. [97]
```

```novo
Katsaros et al. [95]
```

**Justificativa**: número da lista de referências (entrada [95]).

---

## T02-A138 — 7.3, Yildirim et al. [98 → [96]

| Campo | Valor |
|---|---|
| Lote | 10e |
| Achados | T01-I03, T02 (P3) |
| Localização | Seção 7.3, parágrafo P246 do dump |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
Yildirim et al. [98]
```

```novo
Yildirim et al. [96]
```

**Justificativa**: número da lista de referências (entrada [96]).

---

## T02-A139 — 7.3, Jhaver et al. [99 → [97]

| Campo | Valor |
|---|---|
| Lote | 10e |
| Achados | T01-I03, T02 (P3) |
| Localização | Seção 7.3, parágrafo P246 do dump |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
Jhaver et al. [99]
```

```novo
Jhaver et al. [97]
```

**Justificativa**: número da lista de referências (entrada [97]).

---

## T02-A140 — 7.3, Roozenbeek et al. [100 → [98]

| Campo | Valor |
|---|---|
| Lote | 10e |
| Achados | T01-I03, T02 (P3) |
| Localização | Seção 7.3, parágrafo P246 do dump |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
Roozenbeek et al. [100]
```

```novo
Roozenbeek et al. [98]
```

**Justificativa**: número da lista de referências (entrada [98]).

---

## T02-A141 — 9.1, Kwak et al. [85 → [83]

| Campo | Valor |
|---|---|
| Lote | 10e |
| Achados | T01-I03, T02 (P3) |
| Localização | Seção 9.1, parágrafo P260 do dump |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
(Kwak et al. [85]
```

```novo
(Kwak et al. [83]
```

**Justificativa**: número da lista de referências (entrada [83]).

---

## T02-A142 — 9.1, Marx [89 → [87]

| Campo | Valor |
|---|---|
| Lote | 10e |
| Achados | T01-I03, T02 (P3) |
| Localização | Seção 9.1, parágrafo P260 do dump |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
AF4; Marx [89]
```

```novo
AF4; Marx [87]
```

**Justificativa**: número da lista de referências (entrada [87]).

---

## T02-A143 — 10.1, Bak-Coleman et al., 103 → [101]

| Campo | Valor |
|---|---|
| Lote | 10e |
| Achados | T01-I03, T02 (P3) |
| Localização | Seção 10.1, parágrafo P276 do dump |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
Bak-Coleman et al., 103]
```

```novo
Bak-Coleman et al., 101]
```

**Justificativa**: número da lista de referências (entrada [101]).

---

## T02-A144 — 10.2, Nielsen and Ganter, 105 → [103]

| Campo | Valor |
|---|---|
| Lote | 10e |
| Achados | T01-I03, T02 (P3) |
| Localização | Seção 10.2, parágrafo P281 do dump |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
Nielsen and Ganter, 105
```

```novo
Nielsen and Ganter, 103
```

**Justificativa**: número da lista de referências (entrada [103]).

---

## T02-A145 — 10.2, Bell and Owen, 106 → [104]

| Campo | Valor |
|---|---|
| Lote | 10e |
| Achados | T01-I03, T02 (P3) |
| Localização | Seção 10.2, parágrafo P281 do dump |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
Bell and Owen, 106]
```

```novo
Bell and Owen, 104]
```

**Justificativa**: número da lista de referências (entrada [104]).

---

## T02-A146 — 10.2, Diakopoulos, 107 → [105]

| Campo | Valor |
|---|---|
| Lote | 10e |
| Achados | T01-I03, T02 (P3) |
| Localização | Seção 10.2, parágrafo P283 do dump |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
[Diakopoulos, 107]
```

```novo
[Diakopoulos, 105]
```

**Justificativa**: número da lista de referências (entrada [105]).

---

## T02-A147 — 10.2, Napoli, 108 → [106]

| Campo | Valor |
|---|---|
| Lote | 10e |
| Achados | T01-I03, T02 (P3) |
| Localização | Seção 10.2, parágrafo P283 do dump |
| Ação | substituir |
| Estado | aplicado em 2026-10-16 |

```original
[Napoli, 108]
```

```novo
[Napoli, 106]
```

**Justificativa**: número da lista de referências (entrada [106]).

## Parte 10d — Seção 7.1: listas "It feeds…" e parágrafos "Why AFx feeds…"

As listas "It feeds…" são revisão dos autores (amarelo), e os parágrafos "Why…" são texto dos
autores: tudo é riscado e reinserido em verde. Cada lista é refeita pela linha da affordance na
Tabela 6 nova, com os nomes de bloco da lista final. Nos parágrafos "Why…", as trocas são pontuais
(ID e nome), exceto onde a ligação mudou de natureza (fusões, divisões e ligações novas). As
legendas das Figuras 5–15 e os cabeçalhos AF3, AF5, AF8–AF11 (que ainda usam travessão e aspas)
ficam para a revisão das figuras e das fichas de affordance.

## T02-A148 — Seção 7.1, AF1, lista It feeds… (revisão dos autores, em amarelo)

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF1, lista "It feeds…" (revisão dos autores, em amarelo) |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
It feeds mechanisms in six blocks (Figure 5). Block A (Algorithmic curation and architecture): Engagement-based ranking (A1), Algorithmic radicalization (A2), and Algorithmic agenda-setting (A5). Block C (Cognitive micro-foundations): Illusory truth effect (C4) and Negativity bias & moral contagion (C5). Block D (Perceptual distortion): Vocal minority / extremity bias (D1) and False polarization (D2). Block G (Information ecosystem and supply): Network propaganda (G2). Block H (Information avoidance and disengagement): News avoidance (H1) and Selective/partisan news avoidance (H2, indirect). Block M (Cross-cutting mechanisms): Informational isolation/segregation (M1, indirect), Coordinated inauthentic behavior (M5), and Reinforcing spiral (M6).
```

```novo
It feeds mechanisms in five blocks (Figure 5). Block A (Algorithmic curation): Filter bubble (A1), Algorithmic amplification (A2), Algorithmic radicalization (A3), and Algorithmic agenda-setting (A4). Block B (Networks, groups, and diffusion): Moral contagion (B5). Block C (Individual selection and processing of information): Selective avoidance (C3, indirect), Illusory truth effect (C6), News avoidance (C7), and Reinforcing spiral (C8). Block D (Perceptions of others): Vocal minority (D1) and Exaggerated meta-perceptions (D6). Block G (Information ecosystem and supply): Propaganda feedback loop (G2) and Manufactured consensus (G3).
```

**Justificativa**: Lista refeita pela linha da affordance na Tabela 6 nova (T02-A91), com os IDs, nomes e blocos da lista final (D6, D36), em ordem de bloco. M1* da v1 vira A1 direto (a ficha de A1 liga a bolha de filtro a AF1).

---

## T02-A149 — Seção 7.1, AF1, Why AF1…, A1 v1 → A2

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF1, "Why AF1…", A1 v1 → A2 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The link to A1 (Engagement-based ranking) is near-definitional — engagement-based ranking is the most direct instance of the affordance itself.
```

```novo
The link to A2 (Algorithmic amplification) is near-definitional, since ranking by predicted engagement is the most direct use of the affordance itself.
```

**Justificativa**: A1 v1 virou A2 (D20). Sai o travessão.

---

## T02-A150 — Seção 7.1, AF1, Why AF1…, A2 v1 → A3

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF1, "Why AF1…", A2 v1 → A3 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The link to A2 (Algorithmic radicalization)
```

```novo
The link to A3 (Algorithmic radicalization)
```

**Justificativa**: ID e nome da lista final (correspondência da 14.6).

---

## T02-A151 — Seção 7.1, AF1, Why AF1…, A5 v1 → A4

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF1, "Why AF1…", A5 v1 → A4 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The link to A5 (Algorithmic agenda-setting) follows the same selection logic
```

```novo
The link to A4 (Algorithmic agenda-setting) follows the same selection logic
```

**Justificativa**: ID e nome da lista final (correspondência da 14.6).

---

## T02-A152 — Seção 7.1, AF1, Why AF1…, C4/C5 v1 → C6/B5

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF1, "Why AF1…", C4/C5 v1 → C6/B5 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The links to C4 (Illusory truth effect) and C5 (Negativity bias & moral contagion) follow from
```

```novo
The links to C6 (Illusory truth effect) and B5 (Moral contagion) follow from
```

**Justificativa**: ID e nome da lista final (correspondência da 14.6).

---

## T02-A153 — Seção 7.1, AF1, Why AF1…, C4/C5 v1 → C6/B5 (fim da frase)

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF1, "Why AF1…", C4/C5 v1 → C6/B5 (fim da frase) |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
(feeding C4) and cumulative exposure to moralized content (feeding C5)
```

```novo
(feeding C6) and cumulative exposure to moralized content (feeding B5)
```

**Justificativa**: ID e nome da lista final (correspondência da 14.6).

---

## T02-A154 — Seção 7.1, AF1, Why AF1…, D1 e D2 v1 → D6

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF1, "Why AF1…", D1 e D2 v1 → D6 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The links to D1 (Vocal minority/extremity bias) and D2 (False polarization)
```

```novo
The links to D1 (Vocal minority) and D6 (Exaggerated meta-perceptions)
```

**Justificativa**: ID e nome da lista final (correspondência da 14.6).

---

## T02-A155 — Seção 7.1, AF1, Why AF1…, G2

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF1, "Why AF1…", G2 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The link to G2 (Network propaganda) follows
```

```novo
The link to G2 (Propaganda feedback loop) follows
```

**Justificativa**: ID e nome da lista final (correspondência da 14.6).

---

## T02-A156 — Seção 7.1, AF1, Why AF1…, H1/H2 → C7/C3

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF1, "Why AF1…", H1/H2 → C7/C3 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The links to H1 (News avoidance) and H2 (Selective/partisan news avoidance, indirect)
```

```novo
The links to C7 (News avoidance) and C3 (Selective avoidance, indirect)
```

**Justificativa**: ID e nome da lista final (correspondência da 14.6).

---

## T02-A157 — Seção 7.1, AF1, Why AF1…, M1 → A1

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF1, "Why AF1…", M1 → A1 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The link to M1 (Informational isolation/segregation) is indirect because algorithmic curation is one of two channels — the other being social, via AF2 (Connection recommendation) and AF3 (Asymmetric following) — that jointly constitute informational isolation.
```

```novo
The link to A1 (Filter bubble) is direct, because the filter bubble is the algorithmic channel of informational isolation. Its social channel is the echo chamber (B2), which AF2 (Network-informed associating) and AF3 (Asymmetric following) feed indirectly.
```

**Justificativa**: M1 foi dividido em A1 (canal algorítmico) e B2 (canal social) (D27). A ligação com AF1 passa a ser direta, e a frase mantém o argumento dos dois canais.

---

## T02-A158 — Seção 7.1, AF1, Why AF1…, M5 → G3

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF1, "Why AF1…", M5 → G3 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The link to M5 (Coordinated inauthentic behavior) follows from the fact that the same space
```

```novo
The link to G3 (Manufactured consensus) follows from the fact that the same space
```

**Justificativa**: ID e nome da lista final (correspondência da 14.6).

---

## T02-A159 — Seção 7.1, AF1, Why AF1…, M6 → C8

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF1, "Why AF1…", M6 → C8 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The link to M6 (Reinforcing spiral) is the most structural
```

```novo
The link to C8 (Reinforcing spiral) is the most structural
```

**Justificativa**: ID e nome da lista final (correspondência da 14.6).

---

## T02-A160 — Seção 7.1, AF2, lista It feeds… (revisão dos autores, em amarelo)

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF2, lista "It feeds…" (revisão dos autores, em amarelo) |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
It feeds mechanisms in four blocks (Figure 6). Block A (Algorithmic curation and architecture): Connection/friend recommendation (A3). Block B (Network structure and group dynamics): Homophily (B1) and Group polarization (B2, indirect). Block M (Cross-cutting mechanisms): Informational isolation/segregation (M1, indirect). Block D (Perceptual distortion): False consensus & pluralistic ignorance (D3, indirect).
```

```novo
It feeds mechanisms in two blocks (Figure 6). Block B (Networks, groups, and diffusion): Homophily (B1), Echo chamber (B2, indirect), and Group polarization (B3, indirect). Block D (Perceptions of others): False consensus (D3, indirect) and Pluralistic ignorance (D4, indirect).
```

**Justificativa**: Lista refeita pela linha da affordance na Tabela 6 nova (T02-A91), com os IDs, nomes e blocos da lista final (D6, D36), em ordem de bloco. A3 v1 foi fundido em B1.

---

## T02-A161 — Seção 7.1, AF2, Why AF2…, abertura e A3 v1

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF2, "Why AF2…", abertura e A3 v1 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
Why AF2 (Connection recommendation) feeds each of these mechanisms. The link to A3 (Connection/friend recommendation) is definitional. The link to B1 (Homophily) follows directly
```

```novo
Why AF2 (Network-informed associating) feeds each of these mechanisms. The link to B1 (Homophily) follows directly
```

**Justificativa**: Nome novo de AF2 (D21). A frase sobre A3 sai porque A3 foi fundido em B1.

---

## T02-A162 — Seção 7.1, AF2, Why AF2…, M1 → B2

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF2, "Why AF2…", M1 → B2 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The link to M1 (Informational isolation/segregation) runs parallel to
```

```novo
The indirect link to B2 (Echo chamber) runs parallel to
```

**Justificativa**: M1 dividido em A1 e B2 (D27).

---

## T02-A163 — Seção 7.1, AF2, Why AF2…, ligações indiretas

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF2, "Why AF2…", ligações indiretas |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The links to B2 (Group polarization) and D3 (False consensus & pluralistic ignorance), both indirect, follow from the fact that the denser, more homogeneous network that connection recommendation produces is the structural condition under which group polarization [Sunstein, 43] and false consensus [Ross et al., 39] operate — the affordance does not trigger these two mechanisms directly, it sets the stage on which they find room to function.
```

```novo
The links to B3 (Group polarization), D3 (False consensus), and D4 (Pluralistic ignorance), all indirect, follow from the fact that the denser, more homogeneous network these suggestions produce is the structural condition under which group polarization [Sunstein, 43], false consensus [Ross et al., 39], and pluralistic ignorance [Prentice and Miller, 40] operate. The affordance does not trigger these mechanisms directly. It sets the stage on which they can function.
```

**Justificativa**: B2 v1 → B3. D3 v1 dividido em D3 e D4 (D33), com a fonte de D4. Sai o travessão.

---

## T02-A164 — Seção 7.1, AF3, parágrafo de abertura, B5 v1 → B7

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF3, parágrafo de abertura, B5 v1 → B7 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
Interpersonal tension & identity salience (B5) helps explain
```

```novo
Interpersonal political tension (B7) helps explain
```

**Justificativa**: ID e nome da lista final (correspondência da 14.6).

---

## T02-A165 — Seção 7.1, AF3, lista It feeds… (revisão dos autores, em amarelo)

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF3, lista "It feeds…" (revisão dos autores, em amarelo) |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
It feeds mechanisms in three blocks (Figure 7). Block B (Network structure and group dynamics): Homophily (B1), Group polarization (B2, indirect), and Interpersonal tension & identity salience (B5, indirect). Block M (Cross-cutting mechanisms): Informational isolation/segregation (M1, indirect). Block D (Perceptual distortion): False consensus & pluralistic ignorance (D3, indirect).
```

```novo
It feeds mechanisms in two blocks (Figure 7). Block B (Networks, groups, and diffusion): Homophily (B1), Echo chamber (B2, indirect), Group polarization (B3, indirect), and Interpersonal political tension (B7, indirect). Block D (Perceptions of others): False consensus (D3, indirect) and Pluralistic ignorance (D4, indirect).
```

**Justificativa**: Lista refeita pela linha da affordance na Tabela 6 nova (T02-A91), com os IDs, nomes e blocos da lista final (D6, D36), em ordem de bloco. C3 entra porque a ficha nova de C3 (T02-A27) liga a evitação ao corte de laços via AF3. **Revisado em 2026-10-18, antes da aplicação** (T03, decisão 3a-1): C3 sai da lista, porque o corte de laços passou ao *Unfriending* (D6 da T03) e a ligação AF3 → C3 foi retirada.

---

## T02-A166 — Seção 7.1, AF3, Why AF3…, ligação nova com C3 e ligações indiretas

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF3, "Why AF3…", ligação nova com C3 e ligações indiretas |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
[McPherson et al., 37]. The indirect links to M1 (Informational isolation/segregation), B2 (Group polarization), and D3 (False consensus & pluralistic ignorance) follow the same logic as
```

```novo
[McPherson et al., 37]. The indirect links to B2 (Echo chamber), B3 (Group polarization), D3 (False consensus), and D4 (Pluralistic ignorance) follow the same logic as
```

**Justificativa**: Justificativa da ligação AF3 → C3, no mesmo argumento da ficha de C3 (sem fonte nova), e IDs das ligações indiretas. **Revisado em 2026-10-18, antes da aplicação** (T03, decisão 3a-1): a frase sobre C3 sai, e o ajuste fica só com os IDs das ligações indiretas.

---

## T02-A167 — Seção 7.1, AF3, Why AF3…, contagem

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF3, "Why AF3…", contagem |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
for these three mechanisms to operate
```

```novo
for these four mechanisms to operate
```

**Justificativa**: Agora são quatro ligações indiretas (B2, B3, D3, D4).

---

## T02-A168 — Seção 7.1, AF3, Why AF3…, B5 v1 → B7

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF3, "Why AF3…", B5 v1 → B7 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The link to B5 (Interpersonal tension & identity salience activation), also indirect,
```

```novo
The link to B7 (Interpersonal political tension), also indirect,
```

**Justificativa**: ID e nome da lista final (correspondência da 14.6).

---

## T02-A169 — Seção 7.1, AF4, lista It feeds… (revisão dos autores, em amarelo)

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF4, lista "It feeds…" (revisão dos autores, em amarelo) |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
It feeds mechanisms in four blocks (Figure 8). Block B (Network structure and group dynamics): Information cascades (B3) and Interpersonal tension & identity salience (B5, secondary). Block D (Perceptual distortion): Social proof (D4). Block E (Incentives and attention economy): Social learning of outrage (E1) and Social quantification / vanity metrics (E4). Block M (Cross-cutting mechanisms): Coordinated inauthentic behavior (M5).
```

```novo
It feeds mechanisms in four blocks (Figure 8). Block B (Networks, groups, and diffusion): Information cascades (B4) and Interpersonal political tension (B7, indirect). Block D (Perceptions of others): Social proof (D2). Block E (Incentives): Social learning of outrage (E1) and Identity signaling (E2). Block G (Information ecosystem and supply): Manufactured consensus (G3).
```

**Justificativa**: Lista refeita pela linha da affordance na Tabela 6 nova (T02-A91), com os IDs, nomes e blocos da lista final (D6, D36), em ordem de bloco. E4 foi fundido em E1. E2 entra porque a ficha nova de E2 (T02-A52) cita AF4.

---

## T02-A170 — Seção 7.1, AF4, Why AF4…, B3 v1 → B4

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF4, "Why AF4…", B3 v1 → B4 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The link to B3 (Information cascades) follows from the fact that a visible counter
```

```novo
The link to B4 (Information cascades) follows from the fact that a visible counter
```

**Justificativa**: ID e nome da lista final (correspondência da 14.6).

---

## T02-A171 — Seção 7.1, AF4, Why AF4…, D4 v1 → D2

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF4, "Why AF4…", D4 v1 → D2 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The link to D4 (Social proof) is the same logic
```

```novo
The link to D2 (Social proof) is the same logic
```

**Justificativa**: ID e nome da lista final (correspondência da 14.6).

---

## T02-A172 — Seção 7.1, AF4, Why AF4…, E4 → E2

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF4, "Why AF4…", E4 → E2 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The link to E4 (Social quantification/vanity metrics) is definitional — the affordance is literally what makes social quantification possible.
```

```novo
The link to E2 (Identity signaling) follows from the public and visible character of these reactions: approval from the in-group rewards the expressions that best mark loyalty to it [Van Bavel and Pereira, 69].
```

**Justificativa**: E4 foi fundido em E1 e a frase definicional perde o objeto. Entra a justificativa da ligação AF4 → E2, com a fonte e o argumento da ficha de E2.

---

## T02-A173 — Seção 7.1, AF4, Why AF4…, M5 → G3

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF4, "Why AF4…", M5 → G3 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The link to M5 (Coordinated inauthentic behavior) follows from the adversarial flip side
```

```novo
The link to G3 (Manufactured consensus) follows from the adversarial flip side
```

**Justificativa**: ID e nome da lista final (correspondência da 14.6).

---

## T02-A174 — Seção 7.1, AF4, Why AF4…, B5 v1 → B7

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF4, "Why AF4…", B5 v1 → B7 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The secondary, indirect link to B5 (Interpersonal tension & identity salience activation)
```

```novo
The secondary, indirect link to B7 (Interpersonal political tension)
```

**Justificativa**: ID e nome da lista final (correspondência da 14.6).

---

## T02-A175 — Seção 7.1, AF5, lista It feeds… (revisão dos autores, em amarelo)

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF5, lista "It feeds…" (revisão dos autores, em amarelo) |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
It feeds mechanisms in four blocks (Figure 9). Block B (Network structure and group dynamics): Information cascades (B3). Block D (Perceptual distortion): False polarization (D2). Block E (Incentives and attention economy): Identity signaling (E2). Block M (Cross-cutting mechanisms): Information disorder (M4).
```

```novo
It feeds mechanisms in three blocks (Figure 9). Block B (Networks, groups, and diffusion): Information cascades (B4). Block D (Perceptions of others): Exaggerated meta-perceptions (D6). Block E (Incentives): Identity signaling (E2).
```

**Justificativa**: Lista refeita pela linha da affordance na Tabela 6 nova (T02-A91), com os IDs, nomes e blocos da lista final (D6, D36), em ordem de bloco. M4 foi fundido em B4.

---

## T02-A176 — Seção 7.1, AF5, Why AF5…, B3 v1 → B4

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF5, "Why AF5…", B3 v1 → B4 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The link to B3 (Information cascades) is the most direct
```

```novo
The link to B4 (Information cascades) is the most direct
```

**Justificativa**: ID e nome da lista final (correspondência da 14.6).

---

## T02-A177 — Seção 7.1, AF5, Why AF5…, D2 v1 → D6

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF5, "Why AF5…", D2 v1 → D6 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The link to D2 (False polarization) follows from the fact that the out-group
```

```novo
The link to D6 (Exaggerated meta-perceptions) follows from the fact that the out-group
```

**Justificativa**: ID e nome da lista final (correspondência da 14.6).

---

## T02-A178 — Seção 7.1, AF5, Why AF5…, M4 fundido em B4

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF5, "Why AF5…", M4 fundido em B4 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The link to M4 (Information disorder) is definitional: the same low friction that accelerates B3 is the most efficient channel for misleading information to circulate at volume.
```

```novo
Since B4 also covers the spread of misleading content, the same low friction is also the most efficient channel for misinformation to circulate at volume.
```

**Justificativa**: M4 foi fundido em B4 (D14). O argumento fica, agora como parte da ligação com B4.

---

## T02-A179 — Seção 7.1, AF6, lista It feeds… (revisão dos autores, em amarelo)

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF6, lista "It feeds…" (revisão dos autores, em amarelo) |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
It feeds mechanisms in four blocks (Figure 10). Block A (Algorithmic curation and architecture): Context collapse (A4). Block F (Interaction and communication): Dogpiling (F2) and Incivility contagion (F4). Block M (Cross-cutting mechanisms): Spiral of silence (M7). Block B (Network structure and group dynamics): Interpersonal tension & identity salience (B5).
```

```novo
It feeds mechanisms in three blocks (Figure 10). Block B (Networks, groups, and diffusion): Interpersonal political tension (B7). Block D (Perceptions of others): Spiral of silence (D5). Block F (Interaction): Dogpiling (F2) and Incivility contagion (F4).
```

**Justificativa**: Lista refeita pela linha da affordance na Tabela 6 nova (T02-A91), com os IDs, nomes e blocos da lista final (D6, D36), em ordem de bloco. A4 da v1 (Context collapse) foi removido (D22).

---

## T02-A180 — Seção 7.1, AF6, Why AF6…, abertura e A4 v1

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF6, "Why AF6…", abertura e A4 v1 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
Why AF6 (Context collapse) feeds each of these mechanisms. The link to A4 (Context collapse) is definitional — the mechanism is the behavioral instance of the affordance itself (the more cautious self-presentation strategy forced by an unpredictable audience). The link to F2
```

```novo
Why AF6 (Audience segmentation) feeds each of these mechanisms. All four links come from the low end of the affordance, context collapse. The link to F2
```

**Justificativa**: Nome novo de AF6 (D22). A frase sobre A4 sai com o mecanismo. A frase nova diz de que extremo da affordance vêm as ligações.

---

## T02-A181 — Seção 7.1, AF6, Why AF6…, ligação com F4

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF6, "Why AF6…", ligação com F4 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
hostile comments from strangers, visible under any post for lack of a segmented audience, alter perceptions of the very topic being discussed [Anderson et al., 49].
```

```novo
hostile comments from strangers, visible under any post for lack of a segmented audience, set an uncivil tone that later participants tend to adopt [Gervais, 50].
```

**Justificativa**: A justificativa descrevia o efeito de exposição (F5, Anderson et al.), não o contágio (F4). Passa a descrever o contágio, com a fonte da ficha de F4 (Gervais). Ver a pergunta sobre F5 na apresentação do lote.

---

## T02-A182 — Seção 7.1, AF6, Why AF6…, M7 → D5

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF6, "Why AF6…", M7 → D5 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The link to M7 (Spiral of silence)
```

```novo
The link to D5 (Spiral of silence)
```

**Justificativa**: ID e nome da lista final (correspondência da 14.6).

---

## T02-A183 — Seção 7.1, AF6, Why AF6…, B5 v1 → B7

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF6, "Why AF6…", B5 v1 → B7 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
the link to B5 (Interpersonal tension & identity salience activation) follows directly
```

```novo
the link to B7 (Interpersonal political tension) follows directly
```

**Justificativa**: ID e nome da lista final (correspondência da 14.6).

---

## T02-A184 — Seção 7.1, AF7, lista It feeds… (revisão dos autores, em amarelo)

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF7, lista "It feeds…" (revisão dos autores, em amarelo) |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
It feeds mechanisms in two blocks (Figure 11). Block A (Algorithmic curation and architecture): Algorithmic agenda-setting (A5). Block F (Interaction and communication): Low-context communication (F3).
```

```novo
It feeds mechanisms in two blocks (Figure 11). Block A (Algorithmic curation): Algorithmic agenda-setting (A4). Block F (Interaction): Message brevity (F3).
```

**Justificativa**: Lista refeita pela linha da affordance na Tabela 6 nova (T02-A91), com os IDs, nomes e blocos da lista final (D6, D36), em ordem de bloco.

---

## T02-A185 — Seção 7.1, AF7, Why AF7…, F3

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF7, "Why AF7…", F3 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The link to F3 (Low-context communication) is definitional
```

```novo
The link to F3 (Message brevity) is definitional
```

**Justificativa**: ID e nome da lista final (correspondência da 14.6).

---

## T02-A186 — Seção 7.1, AF7, Why AF7…, A5 v1 → A4

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF7, "Why AF7…", A5 v1 → A4 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The link to A5 (Algorithmic agenda-setting) is indirect
```

```novo
The link to A4 (Algorithmic agenda-setting) is indirect
```

**Justificativa**: ID e nome da lista final (correspondência da 14.6).

---

## T02-A187 — Seção 7.1, AF8, lista It feeds… (revisão dos autores, em amarelo)

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF8, lista "It feeds…" (revisão dos autores, em amarelo) |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
It feeds mechanisms in two blocks (Figure 12). Block F (Interaction and communication): Online disinhibition effect (F1) and Dogpiling (F2). Block M (Cross-cutting mechanisms): Coordinated inauthentic behavior (M5).
```

```novo
It feeds mechanisms in two blocks (Figure 12). Block F (Interaction): Online disinhibition effect (F1) and Dogpiling (F2). Block G (Information ecosystem and supply): Manufactured consensus (G3).
```

**Justificativa**: Lista refeita pela linha da affordance na Tabela 6 nova (T02-A91), com os IDs, nomes e blocos da lista final (D6, D36), em ordem de bloco.

---

## T02-A188 — Seção 7.1, AF8, Why AF8…, M5 → G3

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF8, "Why AF8…", M5 → G3 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The link to M5 (Coordinated inauthentic behavior) is about production cost
```

```novo
The link to G3 (Manufactured consensus) is about production cost
```

**Justificativa**: ID e nome da lista final (correspondência da 14.6).

---

## T02-A189 — Seção 7.1, AF9, lista It feeds… (revisão dos autores, em amarelo)

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF9, lista "It feeds…" (revisão dos autores, em amarelo) |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
It feeds mechanisms in three blocks (Figure 13). Block A (Algorithmic curation and architecture): Engagement-based ranking (A1). Block C (Cognitive micro-foundations): Illusory truth effect (C4) and Negativity bias & moral contagion (C5). Block H (Information avoidance and disengagement): News avoidance (H1).
```

```novo
It feeds mechanisms in three blocks (Figure 13). Block A (Algorithmic curation): Algorithmic amplification (A2). Block B (Networks, groups, and diffusion): Moral contagion (B5). Block C (Individual selection and processing of information): Illusory truth effect (C6) and News avoidance (C7).
```

**Justificativa**: Lista refeita pela linha da affordance na Tabela 6 nova (T02-A91), com os IDs, nomes e blocos da lista final (D6, D36), em ordem de bloco.

---

## T02-A190 — Seção 7.1, AF9, Why AF9…, A1/C4/C5/H1 v1

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF9, "Why AF9…", A1/C4/C5/H1 v1 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
More session time inside the engagement-ranked feed (A1, Engagement-based ranking) means more cumulative repetition, feeding the illusory truth effect (C4, Illusory truth effect) [Hasher et al., 66], and more cumulative exposure to moral-emotional content (C5, Negativity bias & moral contagion) [Brady et al., 67]. The link to H1 (News avoidance)
```

```novo
More session time inside the algorithmically amplified feed (A2, Algorithmic amplification) means more cumulative repetition, feeding the illusory truth effect (C6) [Hasher et al., 66], and more cumulative exposure to moral-emotional content, feeding moral contagion (B5) [Brady et al., 67]. The link to C7 (News avoidance)
```

**Justificativa**: IDs e nomes novos (A1 v1 → A2, C4 → C6, C5 → B5, H1 → C7). Sai a repetição do nome entre parênteses em C6.

---

## T02-A191 — Seção 7.1, AF10, lista It feeds… (revisão dos autores, em amarelo)

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF10, lista "It feeds…" (revisão dos autores, em amarelo) |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
It feeds three mechanisms of Block G (Information ecosystem and supply), shown in Figure 14: Disintermediation / gatekeeping decline (G1), Deplatforming & migration (G4), and Perceived censorship (G5).
```

```novo
It feeds three mechanisms of Block G (Information ecosystem and supply), shown in Figure 14: Gatekeeping decline (G1), Platform migration (G4), and Perceived censorship (G5).
```

**Justificativa**: Lista refeita pela linha da affordance na Tabela 6 nova (T02-A91), com os IDs, nomes e blocos da lista final (D6, D36), em ordem de bloco.

---

## T02-A192 — Seção 7.1, AF10, Why AF10…, G1

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF10, "Why AF10…", G1 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The link to G1 (Disintermediation/gatekeeping decline)
```

```novo
The link to G1 (Gatekeeping decline)
```

**Justificativa**: ID e nome da lista final (correspondência da 14.6).

---

## T02-A193 — Seção 7.1, AF10, Why AF10…, G4

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF10, "Why AF10…", G4 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The link to G4 (Deplatforming & migration)
```

```novo
The link to G4 (Platform migration)
```

**Justificativa**: ID e nome da lista final (correspondência da 14.6).

---

## T02-A194 — Seção 7.1, AF11, parágrafo de abertura, nome de AF2

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF11, parágrafo de abertura, nome de AF2 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
distinguished from AF2 (Connection recommendation)
```

```novo
distinguished from AF2 (Network-informed associating)
```

**Justificativa**: Nome novo de AF2 (D21).

---

## T02-A195 — Seção 7.1, AF11, lista It feeds… (revisão dos autores, em amarelo)

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF11, lista "It feeds…" (revisão dos autores, em amarelo) |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
It feeds mechanisms in two blocks (Figure 15). Block B (Network structure and group dynamics): Partisan sorting (B4). Block G (Information ecosystem and supply): Radicalization pipeline (G3).
```

```novo
It feeds two mechanisms of Block B (Networks, groups, and diffusion), shown in Figure 15: Partisan sorting (B6) and Online community radicalization (B8).
```

**Justificativa**: Lista refeita pela linha da affordance na Tabela 6 nova (T02-A91), com os IDs, nomes e blocos da lista final (D6, D36), em ordem de bloco. G3 v1 virou B8 (D32), e os dois mecanismos ficam no Bloco B.

---

## T02-A196 — Seção 7.1, AF11, Why AF11…, B4 v1 → B6

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF11, "Why AF11…", B4 v1 → B6 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The link to B4 (Partisan sorting)
```

```novo
The link to B6 (Partisan sorting)
```

**Justificativa**: ID e nome da lista final (correspondência da 14.6).

---

## T02-A197 — Seção 7.1, AF11, Why AF11…, G3 v1 → B8

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF11, "Why AF11…", G3 v1 → B8 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The link to G3 (Radicalization pipeline)
```

```novo
The link to B8 (Online community radicalization)
```

**Justificativa**: ID e nome da lista final (correspondência da 14.6).

## T02-A198 — Seção 7.1, AF2, Why AF2…, M1 → B2 (segunda metade de T02-A162)

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF2, Why AF2…, M1 → B2 (segunda metade de T02-A162) |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
that of Algorithmic content curation (AF1): this is the social pathway to informational isolation, complementary to the algorithmic one.
```

```novo
the link between AF1 and the filter bubble (A1). It is the social pathway to informational isolation, complementary to the algorithmic one.
```

**Justificativa**: T02-A162 foi dividido em dois porque há um trecho já riscado pelos autores (AF1's) no meio da frase.

---

## T02-A199 — Seção 7.1, AF3, Why AF3…, nome de AF2 (segunda metade de T02-A166)

| Campo | Valor |
|---|---|
| Lote | 10d |
| Decisões | D6, D36; Tabela 6 nova (T02-A91) |
| Localização | Seção 7.1, AF3, Why AF3…, nome de AF2 (segunda metade de T02-A166) |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
that of Connection recommendation (AF2): the affordance
```

```novo
that of Network-informed associating (AF2): the affordance
```

**Justificativa**: T02-A166 foi dividido em dois porque há um trecho já riscado pelos autores (AF2's) no meio da frase. Nome novo de AF2 (D21).

---

## Log de aplicação

| Data | Documento | Aplicados | Pulados | Revisão antes | Revisão depois |
|---|---|---|---|---|---|
| 2026-10-13 11:47 | `13O5Uco9-ItlpHioS_M_tsUr8UbqxppoQ2bx1fBmQ00g` | T02-A1, T02-A2, T02-A3, T02-A4, T02-A5, T02-A6, T02-A7, T02-A8 | — | `AHj4eMQDUdVj8O5qdLVvEG-pKCLO6A9eF0qscqbiiUEumxn2UNUIZUqtV-yh828jQNZztjtKoVjKRrNQHReSfzXjnTU9LwaSC912pLGqBxF_LAc` | `AHj4eMSMC5caunbESFp_8FdN0Wu-ffyjSPW02bGnCltvrebJ8aMPtj9Q2SX1QxwSVkxyyjaVZ0_wmcNHXdZclf7NdgKQnqKHi8_JmeJSnMTCiB8` |
| 2026-10-13 11:53 | `13O5Uco9-ItlpHioS_M_tsUr8UbqxppoQ2bx1fBmQ00g` | negrito nos rótulos de T02-A3, A4, A5, A8 (comando `bold`; só formatação de texto inserido) | — | — | — |
| 2026-10-13 14:51 | `13O5Uco9-ItlpHioS_M_tsUr8UbqxppoQ2bx1fBmQ00g` | T02-A9, T02-A10, T02-A11, T02-A12, T02-A13, T02-A14, T02-A15, T02-A16, T02-A17, T02-A18, T02-A19, T02-A20, T02-A21, T02-A22 | — | `AHj4eMQcpG8O6dD8-XHE9-YYYEfu2Og0UOjjwV2E7tUjd3ZPqbaEy-E2Lp9DtjUbXnv7elUk993-VBO7yyEYASLUXZR1QDV7s9LG31MFJcPPC6w` | `AHj4eMTI_mgEYvXMU9I6sR7DZrxZ2UHd5npWZELOzAknsJJaR9LNaVENQdDC0trnOVT4lwYVP90L_3mJI1TV3L8CHsGEriDNxU96btxMHYFtCww` |
| 2026-10-13 15:04 | `13O5Uco9-ItlpHioS_M_tsUr8UbqxppoQ2bx1fBmQ00g` | T02-A23, T02-A24, T02-A25, T02-A26, T02-A27, T02-A28, T02-A29, T02-A30, T02-A31, T02-A32, T02-A33, T02-A34, T02-A35, T02-A36, T02-A37 | — | `AHj4eMRkBocpwidKdjwcr7MQGAh2agTIbeA1untT-W6UhvF62q6JI6cjeqScu7Q0II1tpUhQ-qWy-iCdBemOsnlWe6QM0BOrSz-f_WtgUU0MQJI` | `AHj4eMT5S4HdAZWJYDQzKdNySX2zFv2P1sBGQT3fY9AgzQDWjGonACjy8uFFKTFEVp3pwGNPOKaZSldaubGrLe47woj7ddd608TW7YLagLuN9Ik` |
| 2026-10-13 15:15 | `13O5Uco9-ItlpHioS_M_tsUr8UbqxppoQ2bx1fBmQ00g` | T02-A38, T02-A39, T02-A40, T02-A41, T02-A42, T02-A43, T02-A44, T02-A45, T02-A46, T02-A47, T02-A48 | — | `AHj4eMRgYS8UOaBJdLXMd-yFGXOPTjeY75Zc0wr37ar7bI1g2WGvWdujleEXlblaCAwV3m5-XeDbHk6u2BpO293zSZ2kJQJk7Gh7zMjG4mY57Ag` | `AHj4eMR-0-HDcCPhbKvPUYfmXOSldq1DR2joLbnp-SAy5Mk2ELMp6A3FlHEsoskmpaNbeszcMcgcoyjOXlySO16Y-PlZp5JpJdZGbHsgqIdYCtU` |
| 2026-10-13 15:26 | `13O5Uco9-ItlpHioS_M_tsUr8UbqxppoQ2bx1fBmQ00g` | T02-A49, T02-A50, T02-A51, T02-A52, T02-A53, T02-A54 | — | `AHj4eMTkBfDPWfaNDFEKa4l9g-HBIF79Egs8rYr96I5x4mvaqXZ97scqpzuy8NFoKgeJdYOLeLBlv_IzCAcRt1vgcCC-SSF6YiOWqirrqbIDvF0` | `AHj4eMQj1PmU99zCr5H6hxGLuqAxN4ghCjXxeTPqbcbzkpQNPynasbPPkE_rXctMX9xiY2N5bBd1RytPjdYL4WI5GTPjKS8KUY491k0IDIQeij4` |
| 2026-10-13 15:51 | `13O5Uco9-ItlpHioS_M_tsUr8UbqxppoQ2bx1fBmQ00g` | T02-A55, T02-A56, T02-A57, T02-A58, T02-A59, T02-A60, T02-A61, T02-A62, T02-A63 | — | `AHj4eMR1RG7GMND3VEsmwFTRLnC1Y7-wUX7ep-B-nYjhqZGJBJYqUFDHYhVcTTQHh32iVMcvjZfzqCnDNb4jbq9i4NNYduh8USzWK4HaW9OJWuc` | `AHj4eMSAdeEk4kSXaVRG0S0Mq4ygfAMitwTeag4N6sTNoKDfc5fleFnyAT1pYVFZC3QIfH3ci-R6YYVYMIoBoXPCP0wszq6_dNl2vSy8kkMuAJc` |
| 2026-10-13 16:00 | `13O5Uco9-ItlpHioS_M_tsUr8UbqxppoQ2bx1fBmQ00g` | T02-A64, T02-A65, T02-A66, T02-A67, T02-A68, T02-A69, T02-A70, T02-A71 | — | `AHj4eMQFQrkXGNQkPrutjHXZoLtYo8W-ixPrLC3-1KDwrgyPxhltUxiSW-HWcXImpiktMpE4Lt5i9XjRo2eT99LFjmwz7xm_ivKeBGAjldyZNrU` | `AHj4eMQ9vNiFKOPrXUmhBlu25vQKfQWd17w5G4Ql_YqbKs1mnzdVp8DfN2j5jzv-LcfJZRsDv7P7hi8zz19B2YxLjYtLF3nPferflF1Bl7NpWuA` |
| 2026-10-16 17:48 | `13O5Uco9-ItlpHioS_M_tsUr8UbqxppoQ2bx1fBmQ00g` | T02-A72, T02-A73, T02-A74, T02-A75, T02-A76, T02-A77, T02-A78 | — | `AHj4eMT0zg0UMHBwzetMxibNBs7XCOAO3f2yUr3neJqtCgAR1rc32YloQ32nPHBw9IV1nodpEC7lUrkDj5UVy2nL8CgBQBmwkFhCfTR8dNNvnjs` | `AHj4eMSeYYOcXGPJjEzOF-wHML2BDXVJgoBxhT1FiQDt8e7MGm99u9fRw3zz6EbMcDF0SUZlhR68ZOfHpPR8ayrb9MqCtxK5EClbVWcPluDNOHs` |
| 2026-10-16 18:17 | `13O5Uco9-ItlpHioS_M_tsUr8UbqxppoQ2bx1fBmQ00g` | T02-A79, T02-A80, T02-A81, T02-A82, T02-A83, T02-A84, T02-A85, T02-A86, T02-A87, T02-A88, T02-A89, T02-A91 | — | `AHj4eMT-CoAd7SnKoHTR9bBFpHKVjt8vFYD6eT1kEdEpB-gcLeqyVHbkuwdOQqIepVOT7odXYodkOJAeC1XcZXILJ4J0F7aTl17ZACFk9R-tBM4` | `AHj4eMTxk_pNS8lPYv4EtrQpUIIiwBp2fj-AwYzFtgpO8UVB0o2mZpVsGn5R1xv3xgIlW6GwWzavJHj04FLvMk0wjcf1FWsQDtYD81yex2cs-5c` |
| 2026-10-16 18:18 | `13O5Uco9-ItlpHioS_M_tsUr8UbqxppoQ2bx1fBmQ00g` | T02-A90 | — | `AHj4eMTxk_pNS8lPYv4EtrQpUIIiwBp2fj-AwYzFtgpO8UVB0o2mZpVsGn5R1xv3xgIlW6GwWzavJHj04FLvMk0wjcf1FWsQDtYD81yex2cs-5c` | `AHj4eMSEOMgUTqaj3iCruBie1UoebYyuAwXaw3ZzRwSK3RPWLoIbXOU1Zf8eFQ67exR3X0jkiW57kVJQ7FCtyYIAu1-RbEmUPWA8v2Mo4cTIhxs` |
| 2026-10-16 18:46 | `13O5Uco9-ItlpHioS_M_tsUr8UbqxppoQ2bx1fBmQ00g` | T02-A92, T02-A93, T02-A94, T02-A95, T02-A96, T02-A97, T02-A98, T02-A99, T02-A100, T02-A101, T02-A102, T02-A103, T02-A104, T02-A105, T02-A106, T02-A107, T02-A108, T02-A109, T02-A110, T02-A111, T02-A112, T02-A113, T02-A114, T02-A115, T02-A116, T02-A117, T02-A118 | — | `AHj4eMSEOMgUTqaj3iCruBie1UoebYyuAwXaw3ZzRwSK3RPWLoIbXOU1Zf8eFQ67exR3X0jkiW57kVJQ7FCtyYIAu1-RbEmUPWA8v2Mo4cTIhxs` | `AHj4eMRTLmJxlctiE8Q0BZIk8JNpT07fcJKgGDRg1Y2U26QbMIlwAoMhPwr4ZCzcNLFUCJz5yz8e6y48P3QhMz3nhNWpzTpSDHRl3RheQuK2SoY` |
| 2026-10-16 18:51 | `13O5Uco9-ItlpHioS_M_tsUr8UbqxppoQ2bx1fBmQ00g` | T02-A119, T02-A120, T02-A121, T02-A122, T02-A123, T02-A124, T02-A125, T02-A126, T02-A127, T02-A128, T02-A129, T02-A130, T02-A131, T02-A132, T02-A133, T02-A134, T02-A135, T02-A136, T02-A137, T02-A138, T02-A139, T02-A140, T02-A141, T02-A142, T02-A143, T02-A144, T02-A145, T02-A146, T02-A147 | — | `AHj4eMRTLmJxlctiE8Q0BZIk8JNpT07fcJKgGDRg1Y2U26QbMIlwAoMhPwr4ZCzcNLFUCJz5yz8e6y48P3QhMz3nhNWpzTpSDHRl3RheQuK2SoY` | `AHj4eMQJsrUqyxjSH2OX21cAfkXXQpN0fPb8R7Kbv0OHPAMYf0Zma3N50yBHFBxms-Ih4GzuP4MniRtHGXkucMQ-zZdlaJd0ytgivqidbIejYSI` |
| 2026-10-18 22:00 | `13O5Uco9-ItlpHioS_M_tsUr8UbqxppoQ2bx1fBmQ00g` | T02-A148, T02-A149, T02-A150, T02-A151, T02-A152, T02-A153, T02-A154, T02-A155, T02-A156, T02-A157, T02-A158, T02-A159, T02-A160, T02-A161, T02-A162, T02-A163, T02-A164, T02-A165, T02-A166, T02-A167, T02-A168, T02-A169, T02-A170, T02-A171, T02-A172, T02-A173, T02-A174, T02-A175, T02-A176, T02-A177, T02-A178, T02-A179, T02-A180, T02-A181, T02-A182, T02-A183, T02-A184, T02-A185, T02-A186, T02-A187, T02-A188, T02-A189, T02-A190, T02-A191, T02-A192, T02-A193, T02-A194, T02-A195, T02-A196, T02-A197, T02-A198, T02-A199 | — | `AHj4eMRbEqDV5nwvvv-FcZykXWZT4ALK-HjEheCUgGDYdQ_t2mco_jlf6zgZOJaYMxDMY3lY_FNavLjh2hoe97FrSYNPDwqSNswj2CPbDcaMiL4` | `AHj4eMSm2uDX7KBXYjTxOqd2h4oG4i5MzLtoXG_zEwRXz4No5v9_kNT8kFhXBWb2jgulQEIBZH0ZF-TqbLmvjnAIA3P98qdWNfeHj_C77p19R2s` |
