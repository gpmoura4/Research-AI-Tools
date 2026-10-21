# Ajustes T03 — Novo levantamento de mecanismos e atores

- **Manuscrito**: smip-famo-framework · **Versão de referência**: cópia de revisão em Google Docs, lida em 2026-10-18
- **Relatório**: [`reviews/T03-novo-levantamento-mecanismos.md`](../reviews/T03-novo-levantamento-mecanismos.md) (roteiro na Seção 4; T03.8)
- **Destino**: cópia de revisão em Google Docs (ID em `context.md`)
- **Marcação**: texto substituído fica riscado, sem ser apagado; novo texto logo depois, em preto com marca-texto verde (`#00FF00`).
- **Aplicação** (na raiz do repositório): `uv run scripts/gdocs_apply.py apply <doc> manuscripts/smip-famo-framework/adjustments/T03-ajustes.md --ids A1,A2` (simulação; `--apply` grava). A ação `inserir-tabela-apos` foi acrescentada ao script em 2026-10-18 para a tabela nova da 5.3.
- **IDs dos mecanismos**: o texto novo usa a **numeração nova** (relatório, 9.1). A renumeração do resto do paper entra no lote 6, que **não deve renumerar** os trechos inseridos por este lote.

## Lotes

| Lote | Conteúdo | Ajustes | Estado |
|---|---|---|---|
| 1 | Atores: 2.3, Introdução, 5.1, 5.2, Figura 2, Seção 5.3 e Tabela 5 nova | T03-A1 a T03-A9 | **aplicado em 2026-10-18** (A1–A4, A6–A9; conferido na releitura). **A5 (imagem) e o estilo do título 5.3: manuais, com o usuário** |
| 2 | Fichas dos mecanismos novos (B2, B7, C5, G6) e acréscimos nas fichas existentes | T03-A10 a T03-A39 | **aplicado em 2026-10-18** (30 ajustes; conferido na releitura). C8 sem ficha (espera o B02) |
| 3 | **3a**: tabela consolidada (9 colunas) e Tabela 6 (matriz das affordances). **3b**: ligações novas na 7.1 | 3a: T03-A40 a T03-A43. 3b: T03-A44 a T03-A57 | **aplicado em 2026-10-18** (3a e 3b, conferidos na releitura). Lote 10d da T02 (7.1) aplicado no mesmo dia, como pré-requisito da 3b |
| 4 | Subseção nova 9.2 (o que as plataformas fazem com os mecanismos), 9.1, limitações (passam a 9.3), 5.2, 10.2 | T03-A58 a T03-A71 | **aplicado em 2026-10-18** (conferido na releitura). **Título da 9.2 nova: estilo manual, com o usuário** |
| 5 | Método (4.3), 6.1, 9.3, Seção 11, Apêndice A, Table A1, *Acknowledgments* | T03-A72 a T03-A79 | **aplicado em 2026-10-18** (conferido na releitura), com *placeholders* [AUTHORS: …] para D12. **Manuais, com o usuário**: estilo de título no Apêndice A (A, A.1–A.4) e inserção da Figura A1 (`figures/figura_A1_fluxo.png`, fonte em `figures/figura_A1_fonte.py`) no lugar do marcador [FIGURE A1: …] |
| 6 | Propagação. **Rodada 1**: correção do Apêndice (42 citados), contagens, tabelas e colunas (6.1 incluída), referências [120]–[161]. **Rodada 2**: IDs no texto antigo, ordem das fichas do bloco B, subgrupos, IDs nos parágrafos que citam os novos só pelo nome | Rodada 1: T03-A80 a T03-A152. Rodada 2: T03-A153 a T03-A212. Rodada 3: T03-A213, A214 | **rodada 1 aplicada em 2026-10-18** (conferida na releitura: nenhum [NEW: …] visível, 161 referências). Figura A1 regenerada (42 e 102): substituição manual da imagem. **Rodada 2 aplicada em 2026-10-18** (IDs conferidos na releitura). Rodada 3 (ordem de B8 e B9) proposta e simulada |

**Ordem de aplicação do lote 1**: `--ids A1,A2,A3,A4,A6,A7,A8,A9`. A1 vem antes de A2 porque os
dois partem do mesmo parágrafo (a definição de *Actor*): inserindo primeiro o parágrafo novo de A1, a
definição nova de A2 fica entre o texto riscado e esse parágrafo. A5 é manual.

---

## T03-A1 — 2.3, parágrafo novo de fronteira (algoritmo e plataforma)

| Campo | Valor |
|---|---|
| Lote | 1 |
| Achados | T03-F08 |
| Decisões | D14 (9.1-b), D15 (9.1-c), 9.6-b |
| Localização | Seção 2.3, logo depois do parágrafo "Actor: An agent, whether human, institutional…" (a definição nova de A2 fica entre os dois) |
| Ação | inserir-apos |
| Estado | aplicado em 2026-10-18 |

```ancora
Actor: An agent, whether human, institutional, or automated, that deliberately triggers or exploits a mechanism, such as in coordinated manipulation campaigns.
```

**Novo texto**

```novo
Two elements of social media can appear under more than one of these categories, and the framework keeps their roles apart. A recommendation algorithm can appear in two roles. As a feature, it is the technical element that the platform specifies. As an actor, it is the system in operation, whose aggregate behavior, such as the content it learns to prioritize, no one decides directly. The platform also appears in two roles. As an actor, it is the organization that sets the rules, the design of features, and the objective that its ranking systems optimize. Platform governance (AF10) is the affordance, that is, what those rules make possible for users.
```

**Justificativa**: a 2.3 dá "a recommendation algorithm" como exemplo de *feature*, e a 5.3 nova trata o
algoritmo e a plataforma como atores. A frase de fronteira mantém a separação de camadas da
contribuição 1 (relatório, 15.1 e 15.2).

---

## T03-A2 — 2.3, definição de *Actor*

| Campo | Valor |
|---|---|
| Lote | 1 |
| Achados | T03-F08 |
| Decisões | D13 (9.1-a), 9.6-a |
| Localização | Seção 2.3, quinto item da lista, "Actor: An agent, whether human, institutional…" |
| Ação | substituir-paragrafo |
| Estado | aplicado em 2026-10-18 |

**Texto original**

```original
Actor: An agent, whether human, institutional, or automated, that deliberately triggers or exploits a mechanism, such as in coordinated manipulation campaigns.
```

**Novo texto**

```novo
Actor: An agent, whether individual, collective, institutional, or automated, whose behavior enacts, triggers, or exploits a mechanism. Some actors do so deliberately, as in coordinated manipulation campaigns. Others do so without strategic intent, as ordinary users and the algorithmic systems of platforms do (Section 5.3).
```

**Justificativa**: a definição atual exige intenção ("deliberately") e exclui dois dos seis tipos de ator
(usuários comuns e o sistema algorítmico).

---

## T03-A3 — Introdução, frase sobre moderadores e atores

| Campo | Valor |
|---|---|
| Lote | 1 |
| Decisões | 9.6 (pedido do usuário, Introdução) |
| Localização | Introdução, parágrafo "This article proposes a four-layer framework…", fim da primeira frase |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

**Texto original**

```original
with four central contributions.
```

**Novo texto**

```novo
with four central contributions. Around these layers, the framework places moderators, which change how strongly a mechanism operates, and six types of actors, which enact or exploit mechanisms (Section 5).
```

**Justificativa**: os atores ganham uma seção própria (5.3) e entram na figura do framework. O mesmo
parágrafo diz "forty-one distinct mechanisms", que muda para "forty-three" no lote 6.

---

## T03-A4 — Figura 2, legenda

| Campo | Valor |
|---|---|
| Lote | 1 |
| Decisões | 9.6-c |
| Localização | Seção 5.1, legenda "Figure 2. A four-layer framework…" (só o texto depois de "Figure 2. ") |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

**Texto original**

```original
A four-layer framework: features, affordances, mechanisms, and outcomes.
```

**Novo texto**

```novo
The framework: four layers (features, affordances, mechanisms, and outcomes), with moderators and actors acting on the mechanisms layer and a feedback loop from outcomes to features.
```

**Justificativa**: a figura nova mostra os moderadores e os atores agindo sobre os mecanismos.

---

## T03-A5 — Figura 2, imagem (manual)

| Campo | Valor |
|---|---|
| Lote | 1 |
| Decisões | 9.3-a a d |
| Localização | Seção 5.1, imagem da Figura 2 |
| Ação | manual (fora do script) |
| Estado | proposto |

**Instrução**: no Google Docs, inserir a imagem `manuscripts/smip-famo-framework/actors/new_model_famo_v2.png`
logo abaixo da figura atual e **não apagar** a figura antiga: marcar a antiga com um comentário
"substituída pela figura abaixo (T03-A5)", seguindo a política de marcação. A API do Docs só insere
imagens a partir de uma URL pública, por isso este ajuste é manual.

---

## T03-A6 — 5.1, frase sobre moderadores e atores

| Campo | Valor |
|---|---|
| Lote | 1 |
| Decisões | 9.6-d |
| Localização | Seção 5.1, parágrafo "As established in Section 2.3, this article distinguishes…", fim |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

**Texto original**

```original
represented in Figure 2.
```

**Novo texto**

```novo
represented in Figure 2. Two further elements act on the mechanisms layer without forming part of the chain: moderators, which change the strength with which a mechanism operates (Section 5.2), and actors, which enact or exploit mechanisms (Section 5.3).
```

**Justificativa**: a 5.1 descreve as quatro camadas e não diz onde entram os moderadores e os atores.

---

## T03-A7 — 5.2, primeira frase

| Campo | Valor |
|---|---|
| Lote | 1 |
| Achados | T03-F09 |
| Decisões | 9.3-a, 9.6-e |
| Localização | Seção 5.2, primeiro parágrafo, primeira frase |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

**Texto original**

```original
A moderators layer, represented on the left side of Figure 2, cuts across the four layers without forming part of the main causal chain.
```

**Novo texto**

```novo
A moderators layer, represented on the left side of Figure 2, acts on the mechanisms layer without forming part of the main causal chain.
```

**Justificativa**: a 2.3 e a própria 5.2 dizem que o moderador altera a força do mecanismo. A figura nova
liga os moderadores aos mecanismos.

---

## T03-A8 — Seção 5.3 nova, *Actors*

| Campo | Valor |
|---|---|
| Lote | 1 |
| Achados | T03-F07, T03-F08 |
| Decisões | 9.4-a, 9.4-b, 9.2-e, 9.5-a |
| Localização | Fim da Seção 5.2, depois do parágrafo "These three points do not exhaust…" e antes de "6. Taxonomy of Mechanisms" |
| Ação | inserir-apos |
| Estado | aplicado em 2026-10-18 |

```ancora
a set of specific, testable causal hypotheses.
```

**Novo texto** (o título "5.3. Actors" entra como parágrafo comum: aplicar o estilo de título de
seção à mão depois da aplicação; a última linha é a legenda da Tabela 5, que T03-A9 completa)

```novo
5.3. Actors
Actors are the agents whose behavior enacts, triggers, or exploits the mechanisms catalogued in Section 6 (Section 2.3). Some act with strategic intent and others without it. Figure 2 distinguishes six types, and Table 5 assigns a primary and, where relevant, a secondary actor to each of the 43 mechanisms. Each type is illustrated below through one mechanism and the outcome it most directly shapes.
Ordinary users enact most mechanisms without any intention to polarize, and they are the primary actor for 32 of the 43 mechanisms. Homophily (B1) is the clearest case. Similar people form ties at a higher rate than dissimilar people [37], and on social media the sum of these individually unremarkable choices sorts users into homogeneous clusters, which is structural polarization. Ordinary users are also the only primary actor of the mechanisms with behavioral outcomes. In online firestorms (F2), large numbers of users sanction a perceived transgression as a form of social norm enforcement, and in the data analyzed by Rost et al. [73], non-anonymous users were more aggressive than anonymous ones. In the spiral of silence (D5), people who perceive their opinion as losing ground become less willing to express it [24].
Social groups act as collective units. In the mechanisms they drive, a shared identity matters more than the choice of any member or leader. Partisan sorting (B3) shows this. When partisan and ideological identities align, each party becomes a more homogeneous social group, and partisan bias, activism, and anger increase even when issue positions do not polarize to the same degree [62]. The outcome is mainly affective.
Organized political or commercial actors exploit mechanisms toward a strategic goal. In the propaganda feedback loop (G2), partisan media outlets, political figures, and audiences reward stories that confirm the group's identity and penalize outlets and journalists that check them, so that the media ecosystem becomes insular and resistant to correction [75]. The outcome is ideological and perceived polarization. News organizations belong to this type as well when they adjust what they publish to engagement metrics (E3) [102]. Journalism therefore appears in the framework as an actor, in addition to being one of the fields affected by polarization.
Automated or coordinated agents depend on cheap and scalable activity rather than on individual conviction. In manufactured consensus (G3), coordinated accounts, often automated, fabricate signals of popularity [53]. Elmas et al. [54] detected over 19,000 fake trends on Twitter promoted by over 108,000 accounts, and these attacks accounted for at least 20% of the top ten global trends. The outcome is mainly perceived polarization, since observers misjudge how widely a position is held.
The algorithmic system is treated as an actor in a restricted sense. As a feature, a recommendation algorithm is a technical element specified by the platform (Section 2.3). As an actor, it is the system in operation, whose aggregate behavior, such as the kind of content it learns to prioritize, is not decided directly by anyone. It is the primary actor of the four mechanisms in Block A. In algorithmic amplification (A2), Milli et al. [14] found that the engagement-based ranking of Twitter amplified emotionally charged and out-group hostile content that users said made them feel worse about their political out-group, and that users did not prefer the political posts it selected. The outcome is mainly affective.
The platform acts as an institution. It sets the rules of governance (AF10), the design of features, and the objective that its ranking systems optimize. Munn [70] argues that design architectures such as the Facebook Feed privilege incendiary content and set up a stimulus-response loop that promotes outrage expression. Platform migration (G4) shows the platform as primary actor. After Reddit banned two communities, both moved to standalone websites, where posting activity fell but users of one of them showed more signals of toxicity and radicalization [77]. The outcome is structural, through the separation of communities across platforms, and affective.
Two patterns emerge from Table 5. Organized and automated actors appear as primary actors only in Block G and in metric-driven content production (E3), while ordinary users are the primary actor in every block except Block A. Behavioral polarization appears only with ordinary users as the primary actor, which suggests that self-censorship and collective sanctioning arise from aggregated individual action rather than from strategy, at least in the evidence reviewed here. As with the links between affordances and mechanisms (Section 5.1), the mapping indicates which actors can enact or exploit a mechanism. It does not predict the outcome of a specific case.
Table 5. Actor types, their mode of action, and the mechanisms for which each is the primary or secondary actor (mechanism IDs as in Section 6).
```

**Justificativa**: texto aprovado no passo 9.4 (relatório, 15.5), com "Table [N]" resolvido como Tabela 5
(9.5-c). Os IDs seguem a numeração nova (B3 = *partisan sorting*). As Tabelas 5 e 6 atuais passam a 6 e
7 no lote 6.

---

## T03-A9 — Tabela 5 nova (atores)

| Campo | Valor |
|---|---|
| Lote | 1 |
| Decisões | 9.5-a, 9.2 |
| Localização | Seção 5.3, logo depois da legenda inserida por T03-A8 |
| Ação | inserir-tabela-apos |
| Estado | aplicado em 2026-10-18 |

```ancora
(mechanism IDs as in Section 6).
```

```tabela
| Actor type | Mode of action | Primary actor of | Secondary actor of | Outcomes reached as primary actor |
|---|---|---|---|---|
| Ordinary users | Enact mechanisms without strategic intent | 32 mechanisms: B1, B2, B4–B9, C1–C9, D1–D6, E1, E2, F1–F5, G5, G6 | A1, A3, B3, G2 | Structural, ideological, affective, perceived, behavioral |
| Social groups | Shared identity drives the mechanism | B3, B10 | B5, B6, B7, D4, E2, G4 | Affective, ideological |
| Organized actors | Exploit mechanisms strategically | E3, G2 | B8, B10, G1, G3, G5, G6 | Affective, ideological, perceived |
| Automated or coordinated agents | Exploit mechanisms strategically, at scale | G3 | A4, B9, D2 | Perceived, affective |
| Algorithmic system | Emergent behavior of a system in operation | A1–A4 | B1, C9 | Ideological, affective, perceived |
| Platform | Institutional choices of rules, design, and objectives | G1, G4 | A2, C5, E1, E3 | Ideological, perceived, structural, affective |
```

**Justificativa**: tabela compacta aprovada no passo 9.5 (relatório, 15.6).

---

## Lote 2 — Fichas: mecanismos novos e acréscimos nas existentes

**Convenções do lote 2**:
- **Citações novas** entram como `[NEW: Autor Ano]`. O lote 6 troca pelo número na lista, junto com as
  outras 43 obras de `references-T03-novas.bib`.
- **IDs**: as **fichas novas** (B2, B7, C5, G6) usam a numeração nova, como a Seção 5.3. Os
  **acréscimos nas fichas existentes** usam os IDs atuais, que o lote 6 renumera junto com o resto da
  ficha. Onde um acréscimo precisa citar um mecanismo novo, usa o nome e a seção, sem ID.
- **Posição das fichas novas**: logo depois da ficha vizinha (Unfriending depois de Homophily;
  Negative social influence depois de Group polarization; Backfire effect depois de Biased
  assimilation; Partisan flagging depois de Perceived censorship). A ordem física final dos blocos B
  e C segue a numeração nova e é resolvida no lote 6.
- **Ficam de fora**: C8 (*Reinforcing spiral*) não tem ficha no texto em inglês (só a linha da
  tabela), e espera o B02. O acréscimo de F5 (Kobellarz et al. 2024, tangencial) vai para a discussão
  (lote 4). O enquadramento em C2 (K24) fica de fora porque a fonte (Antinyan et al. 2024) não está
  entre os incluídos.

**Ordem de aplicação**: `--ids A12,A13,A14,A10,A11,A15,A16,A17,A18,A19,A20,A21,A22,A23,A24,A25,A26,A27,A28,A29,A30,A31,A32,A33,A34,A35,A36,A37,A38,A39`.
Cada ficha nova vem depois do acréscimo na ficha vizinha, porque a âncora dela é o fim desse acréscimo.

---

## T03-A10 — B1 (Homophily): homofilia afetiva e segregação offline

| Campo | Valor |
|---|---|
| Lote | 2 |
| Decisões | 3.2-G1 |
| Localização | Seção 6.4, ficha B1, última frase |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
Repeated homophilous tie formation sorts users into politically homogeneous clusters, which is the network segregation measured as structural polarization (Section 2.2).
```

```novo
Repeated homophilous tie formation sorts users into politically homogeneous clusters, which is the network segregation measured as structural polarization (Section 2.2). Similarity can be affective as well as attitudinal: in online conflict discourse networks, link formation was organized mainly by shared emotion [NEW: Gu et al. 2025]. Offline segregation can be stronger than its online counterpart, since in the United States partisan exposure in physical space predicted vote choice better than online ties [NEW: Tonin et al. 2025].
```

---

## T03-A11 — B2 nova: Unfriending

| Campo | Valor |
|---|---|
| Lote | 2 |
| Decisões | D5, D6, 3.3-K04-a a d |
| Localização | Seção 6.4, logo depois da ficha B1 |
| Ação | inserir-apos |
| Estado | aplicado em 2026-10-18 |

```ancora
than online ties [NEW: Tonin et al. 2025].
```

```novo
B2. Unfriending (alt. unfollowing, partisan blocking). The cutting of existing ties, by unfollowing, unfriending, blocking, muting, or leaving a community, with users who hold opposing political views or share content judged unacceptable. Ending such ties offline carries social costs, but on platforms a single action ends a tie without reciprocity (AF3), and the political identity displayed on profiles signals the other side before any conversation takes place (AF8). In two field experiments on Twitter, users were 12 and 4 times more likely to block counter-partisan than copartisan accounts, a preferential prevention of social ties that Martel et al. [NEW: Martel et al. 2024] identify as a source of political assortment beyond homophily (B1). In two experiments with a representative sample of social media users, people were more likely to block or unfollow politically dissimilar than similar friends who shared misinformation [NEW: Kaiser et al. 2022]. In simulations, unfriending combined with social influence rapidly divided networks into homogeneous communities [NEW: Sasahara et al. 2020], and cascades of exits from communities produced strong segregation without any preference for homogeneity, although algorithmic personalization slowed them under some conditions [NEW: Törnberg 2026]. The mechanism acts on structural polarization. It differs from homophily (B1), which concerns which ties are formed, and from selective avoidance (C3), which concerns content rather than ties.
```

---

## T03-A12 — A1 (Filter bubble): evidência experimental e contrária

| Campo | Valor |
|---|---|
| Lote | 2 |
| Decisões | 3.2-G1, 5.3 (Direction = Mixed) |
| Localização | Seção 6.3, ficha A1, frase "The evidence is mixed: on Facebook…" |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The evidence is mixed: on Facebook, individual choices limited exposure to cross-cutting content more than algorithmic ranking did [45].
```

```novo
The evidence is mixed: on Facebook, individual choices limited exposure to cross-cutting content more than algorithmic ranking did [45]. In a laboratory experiment that used the YouTube recommender with manipulated search and watch histories, the recommended political videos heightened affective polarization [NEW: Cho et al. 2020], while naturalistic experiments that manipulated YouTube recommendations to create filter bubbles found limited effects on opinions [NEW: Liu et al. 2025]. In a simulation, personalization even reduced segregation under some conditions [NEW: Törnberg 2026].
```

---

## T03-A13 — A2 (Algorithmic amplification): via das contas priorizadas

| Campo | Valor |
|---|---|
| Lote | 2 |
| Decisões | 3.4-e, 3.2-G1 |
| Localização | Seção 6.3, ficha A2, antes da última frase |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
It differs from moral contagion (B5), the human sharing preference that the algorithm learns, and from the social learning of outrage (E1), which concerns the authors rewarded for producing such content.
```

```novo
A second route amplifies accounts rather than content. Platforms grant some accounts greater reach through verification or boosting, and in a simulation, prioritizing users reduced polarization when they behaved like other users but sharpened echo chambers when the prioritized users were stubborn ideologues [NEW: Arruda et al. 2024]. A review of the evidence concludes that algorithms mostly reinforce existing social drivers [NEW: Metzler and García 2023]. It differs from moral contagion (B5), the human sharing preference that the algorithm learns, and from the social learning of outrage (E1), which concerns the authors rewarded for producing such content.
```

---

## T03-A14 — A3 (Algorithmic radicalization): experimento com *rabbit holes*

| Campo | Valor |
|---|---|
| Lote | 2 |
| Decisões | 5.1-b |
| Localização | Seção 6.3, ficha A3, frase "The evidence is therefore mixed." |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The evidence is therefore mixed.
```

```novo
Naturalistic experiments that manipulated YouTube recommendations to create rabbit holes also found limited effects on opinions [NEW: Liu et al. 2025]. The evidence is therefore mixed.
```

---

## T03-A15 — B2 atual (Echo chamber): influência assimilativa e tamanho das câmaras de eco

| Campo | Valor |
|---|---|
| Lote | 2 |
| Decisões | 3.2-G1, 5.3 (Direction = Mixed) |
| Localização | Seção 6.4, ficha B2 (Echo chamber), última frase |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The echo chamber differs from the filter bubble (A1), where the narrowing comes from algorithmic selection, and from group polarization (B3), which concerns the shift of positions after discussion among like-minded people.
```

```novo
The echo chamber differs from the filter bubble (A1), where the narrowing comes from algorithmic selection, and from group polarization (B3), which concerns the shift of positions after discussion among like-minded people. In repeated exchanges, the reinforcement takes the form of assimilative influence among like-minded peers. The size of echo chambers is contested. In most of the seven countries studied by Fletcher et al., only about 5% of internet users inhabited partisan online news echo chambers [NEW: Fletcher et al. 2021], political interest and diverse media use moderate the risk of being caught in one [NEW: Dubois and Blank 2018], and apparent evidence of echo chambers disappeared once news media use was controlled for [NEW: Geiß et al. 2021]. In a simulation, echo chambers emerged without algorithmic personalization and without any preference for homogeneity [NEW: Törnberg 2026].
```

---

## T03-A16 — B3 atual (Group polarization): laboratório, casos online e *groupthink*

| Campo | Valor |
|---|---|
| Lote | 2 |
| Decisões | 3.2-G1 |
| Localização | Seção 6.4, ficha B3 (Group polarization), última frase |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The evidence is strong in laboratory settings and more limited online.
```

```novo
In a laboratory study, discussion in homogeneous groups led to more extreme views than discussion in heterogeneous groups [NEW: Sobeh et al. 2025]. Online, case studies of extreme-right lone actors found that the internet amplified group polarization [NEW: Mølmen and Ravndal 2021]. The evidence is strong in laboratory settings and more limited online. Groupthink, in which the desire for cohesion suppresses critical evaluation, is a related construct and is not treated here as a synonym.
```

---

## T03-A17 — B7 nova: Negative social influence

| Campo | Valor |
|---|---|
| Lote | 2 |
| Decisões | D5, 3.3-K10-a a c |
| Localização | Seção 6.4, logo depois da ficha B3 atual (Group polarization) |
| Ação | inserir-apos |
| Estado | aplicado em 2026-10-18 |

```ancora
is a related construct and is not treated here as a synonym.
```

```novo
B7. Negative social influence (alt. repulsive influence, anticonformity). The shift of a person's opinion away from that of another person who is seen as too distant or as a member of the out-group. In the form of anticonformity, people adopt the opposite of the position taken by the out-group. In the form of structural balance, they align with friends and oppose those they see as enemies, and the network splits into two blocks. The process exists offline, and platforms raise the dose of contact with distant others through connections beyond the local network (AF2) and low audience segmentation (AF6), while visible partisan identity (AF8) marks the other as out-group before any argument is read. In agent-based models, polarization follows from interaction between dissimilar actors that increases their difference [NEW: Axelrod et al. 2021], from anticonformity across antagonistic groups once they are densely connected [NEW: Krueger et al. 2017], and from out-group animosity that outweighs in-group favoritism [NEW: Nettasinghe et al. 2025]. In a model with homophily and social balance, polarization rises abruptly above a critical level of social connectivity [NEW: Thurner et al. 2025]. Direct evidence is weak: in the only model in this group derived from experimental data, influence between participants was very weak but significant, and participants with extreme opinions changed least [NEW: Carpentras et al. 2022]. The mechanism acts on ideological and affective polarization. It differs from the backfire effect (C5), a response to the content of a message, because here the shift depends on who the source is.
```

---

## T03-A18 — B4 (Information cascades): simulação de contágio complexo

| Campo | Valor |
|---|---|
| Lote | 2 |
| Decisões | 5.1-b |
| Localização | Seção 6.4, ficha B4, última frase |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
By circulating unverified claims within like-minded clusters, the mechanism acts on ideological and perceived polarization.
```

```novo
By circulating unverified claims within like-minded clusters, the mechanism acts on ideological and perceived polarization. In a network simulation, clusters polarized in both opinion and network structure helped misinformation spread as a complex contagion, acting as its initial bandwagon [NEW: Törnberg 2018].
```

---

## T03-A19 — B5 (Moral contagion): linguagem polarizada e via da mídia partidária

| Campo | Valor |
|---|---|
| Lote | 2 |
| Decisões | 3.2-G1, 2.3-b |
| Localização | Seção 6.4, ficha B5, antes da última frase |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
It is the preference that engagement-based ranking learns and amplifies (A2), and it differs from the social learning of outrage (E1), which concerns the authors rewarded for expressing it.
```

```novo
Polarized language is associated with greater engagement among politically engaged users, and Russian troll accounts used it more than regular users, and increasingly over time [NEW: Simchon et al. 2022]. The same chain can start outside platforms: in a panel study, use of pro-attitudinal partisan news online was associated with anger at the opposing candidate, which in turn facilitated political information sharing on social media [NEW: Hasell and Weeks 2016]. It is the preference that engagement-based ranking learns and amplifies (A2), and it differs from the social learning of outrage (E1), which concerns the authors rewarded for expressing it.
```

---

## T03-A20 — B6 (Partisan sorting): via de plataforma e alinhamento de temas

| Campo | Valor |
|---|---|
| Lote | 2 |
| Decisões | 3.2-G1 (K09 absorvido) |
| Localização | Seção 6.4, ficha B6, antes da última frase |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The mechanism acts on affective polarization: the other party comes to be seen as a distinct social group rather than as people who disagree on some issues.
```

```novo
A model proposes a specific route: digital media bring people to interact outside their local networks, and these interactions align previously cross-cutting differences into two increasingly homogeneous camps [NEW: Törnberg 2022]. Alignment can extend to issue positions, and in a model of opinion dynamics across several topics, correlations between extreme positions emerged from social interaction without being assumed in individual preferences [NEW: Baumann et al. 2021]. The mechanism acts on affective polarization: the other party comes to be seen as a distinct social group rather than as people who disagree on some issues.
```

---

## T03-A21 — B8 (Online community radicalization): casos de radicalização online

| Campo | Valor |
|---|---|
| Lote | 2 |
| Decisões | 5.1-b |
| Localização | Seção 6.4, ficha B8, antes da última frase |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
Together with algorithmic radicalization (A3), it forms what the literature calls the radicalization pipeline, here split into a community route and an algorithmic route.
```

```novo
In three cases of extreme-right lone actors, the internet facilitated radicalization mainly through information provision, the amplification of group polarization, and echoing, while offline push factors made extreme online messages more impactful [NEW: Mølmen and Ravndal 2021]. Together with algorithmic radicalization (A3), it forms what the literature calls the radicalization pipeline, here split into a community route and an algorithmic route.
```

---

## T03-A22 — C1 (Motivated reasoning): meta-análise e modelo

| Campo | Valor |
|---|---|
| Lote | 2 |
| Decisões | 3.2-G2 |
| Localização | Seção 6.5, ficha C1, última frase |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The main effect is on ideological polarization.
```

```novo
In a meta-analysis of 31 experiments, ideological congruence between participants and news, together with motivated reflection, increased the tendency to judge online news as true [NEW: Sultan et al. 2024]. An agent-based model comparing confirmation bias and politically motivated reasoning shows that, depending on how strongly agents filter information, a population exposed to an objective source can either converge on the truth or remain divided [NEW: Sobkowicz 2018]. The main effect is on ideological polarization.
```

---

## T03-A23 — C2 (Confirmation bias): exposição ao outro lado

| Campo | Valor |
|---|---|
| Lote | 2 |
| Decisões | 3.2-G2, 5.3 (Direction = Mixed) |
| Localização | Seção 6.5, ficha C2, última frase |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
Confirmation bias differs from motivated reasoning (C1), which is the motive, from biased assimilation (C4), which concerns how evidence already encountered is weighed, and from selective avoidance (C3), the avoidance of challenging content.
```

```novo
Confirmation bias differs from motivated reasoning (C1), which is the motive, from biased assimilation (C4), which concerns how evidence already encountered is weighed, and from selective avoidance (C3), the avoidance of challenging content. Platforms do not always narrow exposure: in Spain, users more active on social media were more likely to encounter news from outlets with a different ideology [NEW: Masip et al. 2020].
```

---

## T03-A24 — C3 (Selective avoidance): definição sem "contacts"

| Campo | Valor |
|---|---|
| Lote | 2 |
| Decisões | D6 |
| Localização | Seção 6.5, ficha C3, primeira frase depois do nome |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The avoidance of content, sources, and contacts that challenge one's political views.
```

```novo
The avoidance of content and sources that challenge one's political views.
```

---

## T03-A25 — C3: o corte de laços passa ao Unfriending

| Campo | Valor |
|---|---|
| Lote | 2 |
| Decisões | D6 |
| Localização | Seção 6.5, ficha C3, frase "On social media, avoidance can also take the form of cutting ties…" |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
On social media, avoidance can also take the form of cutting ties, since asymmetric following (AF3) lets users unfollow or unfriend disagreeing contacts at low cost.
```

```novo
Cutting ties with disagreeing contacts is treated separately as unfriending (Section 6.4).
```

---

## T03-A26 — C3: última frase sem a remoção de laços

| Campo | Valor |
|---|---|
| Lote | 2 |
| Decisões | D6 |
| Localização | Seção 6.5, ficha C3, última frase |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
by narrowing exposure and removing disagreeing ties, avoidance can reinforce attitudes
```

```novo
by narrowing exposure, avoidance can reinforce attitudes
```

---

## T03-A27 — C4 (Biased assimilation): modelo de rede

| Campo | Valor |
|---|---|
| Lote | 2 |
| Decisões | 3.2-G2 |
| Localização | Seção 6.5, ficha C4, última frase |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
It differs from confirmation bias (C2), which concerns which evidence is sought, because it concerns how evidence already encountered is weighed.
```

```novo
It differs from confirmation bias (C2), which concerns which evidence is sought, because it concerns how evidence already encountered is weighed. In a network model in which a minority of agents rejects incongruent information, this simple bias was enough to generate permanent opinion polarization [NEW: Sikder et al. 2020].
```

---

## T03-A28 — C5 nova: Backfire effect

| Campo | Valor |
|---|---|
| Lote | 2 |
| Decisões | D5, 3.3-K11-a a d |
| Localização | Seção 6.5, logo depois da ficha C4 |
| Ação | inserir-apos |
| Estado | aplicado em 2026-10-18 |

```ancora
permanent opinion polarization [NEW: Sikder et al. 2020].
```

```novo
C5. Backfire effect (alt. boomerang effect, trench warfare). The strengthening of a prior attitude, or a move away from the position advocated, after exposure to counter-attitudinal messages or to corrections. Motivated reasoning (C1) drives the response: the message is read as a threat, and people counterargue and discredit the source. The process exists offline, and platforms raise the dose of such encounters through incidental exposure, low audience segmentation (AF6), following accounts of the other side (AF3), and public corrections and labels (AF10). In a field experiment, Republicans who followed for a month a Twitter bot that exposed them to messages from the opposing side became substantially more conservative [84], and survey experiments on online debates found that contradicting arguments reinforced attitudes as much as confirming ones, a dynamic that Karlsen et al. [NEW: Karlsen et al. 2017] call trench warfare. The response can also be behavioral: on Twitter, users whose posts were tagged as misinformation by other users retreated into information bubbles, an effect softened when tagging went through the collective verification of Community Notes [NEW: Kim et al. 2025]. Design and context matter in other ways too. Counter-attitudinal news was accepted more when delivered by a chatbot than on a news website [NEW: Zarouali et al. 2020], and prior work reviewed by Nordbrandt [NEW: Nordbrandt 2022] suggests that cross-cutting experiences raise polarization mainly when disagreement is perceived as intense. The evidence is mixed. The mechanism acts on ideological polarization. It differs from biased assimilation (C4), which weighs the same evidence unequally, because here the counter-message reverses or hardens the attitude.
```

---

## T03-A29 — C6 (Illusory truth effect): ausência de evidência de plataforma

| Campo | Valor |
|---|---|
| Lote | 2 |
| Decisões | 3.2-G2, 5.3 (Evidence = Plausible) |
| Localização | Seção 6.5, ficha C6, última frase |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
Repeated partisan claims, false ones included, can then come to seem true to those who see them most often, with effects on ideological and perceived polarization.
```

```novo
Repeated partisan claims, false ones included, can then come to seem true to those who see them most often, with effects on ideological and perceived polarization. Direct evidence of this amplification on platforms is still missing. In a preregistered experiment outside social media, two weeks of daily exposure to polarized health news shifted explicit attitudes toward the topic in the direction of the news, while implicit attitudes did not change [NEW: Secară and Opre 2026]. That study measured evaluation rather than perceived truth.
```

---

## T03-A30 — C7 (News avoidance): escala da não exposição a notícias online

| Campo | Valor |
|---|---|
| Lote | 2 |
| Decisões | 5.2-d |
| Localização | Seção 6.5, ficha C7, última frase |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
On the Russian platform Vkontakte, Urman [109] found a politically apathetic majority and a news-interested minority polarized along political lines.
```

```novo
On the Russian platform Vkontakte, Urman [109] found a politically apathetic majority and a news-interested minority polarized along political lines. In each of seven countries, more internet users consumed no online news at all than lived in partisan online news echo chambers [NEW: Fletcher et al. 2021].
```

---

## T03-A31 — D3 (False consensus): modelo de amostragem social

| Campo | Valor |
|---|---|
| Lote | 2 |
| Decisões | 5.1-b |
| Localização | Seção 6.6, ficha D3, última frase |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
False consensus is the opposite error of pluralistic ignorance (D4), in which people underestimate how common their private views are.
```

```novo
False consensus is the opposite error of pluralistic ignorance (D4), in which people underestimate how common their private views are. In an agent-based model in which people balance a preference for authenticity against the aversion to appearing extreme within their local norm, both false consensus and pluralistic ignorance emerge [NEW: Brown et al. 2022].
```

---

## T03-A32 — D4 (Pluralistic ignorance): norma percebida do próprio grupo

| Campo | Valor |
|---|---|
| Lote | 2 |
| Decisões | 5.1-b (K26) |
| Localização | Seção 6.6, ficha D4, última frase |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
It is the opposite error of false consensus (D3).
```

```novo
Partisans also exaggerate how negative their own group's norm toward the out-group is, and in three studies this perception predicted affective polarization far better than outgroup meta-perceptions did [NEW: You and Lee 2024]. It is the opposite error of false consensus (D3).
```

---

## T03-A33 — D5 (Spiral of silence): estudo de diário e modelo

| Campo | Valor |
|---|---|
| Lote | 2 |
| Decisões | 3.2-G3, 5.1-c (sem K28), 7.1-b (sem Cheong) |
| Localização | Seção 6.6, ficha D5, última frase |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The evidence for its operation online is mixed.
```

```novo
The evidence for its operation online is mixed. In a diary study during the refugee debate in Germany, reliance on social media did not generally stimulate opinion expression [NEW: Geiß et al. 2021]. In a model of learning from social feedback, a cohesive minority could silence even a strong majority, while platforms that organize users around opinions also favored regimes in which opposing voices compete in public [NEW: Banisch et al. 2022].
```

---

## T03-A34 — D6 (Exaggerated meta-perceptions): peso do mecanismo

| Campo | Valor |
|---|---|
| Lote | 2 |
| Decisões | 5.1-b |
| Localização | Seção 6.6, ficha D6, última frase |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The mechanism turns perceived polarization into affective polarization.
```

```novo
The weight of the mechanism is debated. In three studies, partisans' perception of their own group's norm toward the out-group explained 8.4 times more variance in affective polarization than outgroup meta-perceptions, and a reanalysis of existing data found that meta-perceptions explained none of the variance in support for partisan violence [NEW: You and Lee 2024]. The mechanism turns perceived polarization into affective polarization.
```

---

## T03-A35 — E1 (Social learning of outrage): opinião extrema e desenho do feedback

| Campo | Valor |
|---|---|
| Lote | 2 |
| Decisões | 3.2-G3 |
| Localização | Seção 6.7, ficha E1, antes da última frase |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
It concerns the authors who learn from feedback, whereas moral contagion (B5) concerns the users who share such content.
```

```novo
The same learning extends beyond outrage to extreme opinions in general, and it depends on the design of feedback: simulations, Twitter data, and online experiments indicate that opinions expressed on platforms are more extreme when counts of positive reactions are visible but counts of negative reactions are not [NEW: Konovalova et al. 2023]. It concerns the authors who learn from feedback, whereas moral contagion (B5) concerns the users who share such content.
```

---

## T03-A36 — E2 (Identity signaling): evidência do Facebook

| Campo | Valor |
|---|---|
| Lote | 2 |
| Decisões | 3.2-G3, 5.3 (Evidence = Moderate) |
| Localização | Seção 6.7, ficha E2, última frase |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The evidence comes mainly from theoretical models of partisan identity, with less direct evidence on platform behavior.
```

```novo
The evidence comes mainly from theoretical models of partisan identity. On Facebook, users engaged more with posts from German news outlets whose slant was congenial to them, especially through likes, which the authors attribute to psychological and social motives rather than to a demand for accurate information [NEW: Garz et al. 2020].
```

---

## T03-A37 — E3 (Metric-driven content production): amplifica, não cria

| Campo | Valor |
|---|---|
| Lote | 2 |
| Decisões | 5.3-b (Platform role: Creates → Amplifies) |
| Localização | Seção 6.7, ficha E3, frase "The mechanism creates an incentive…" |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The mechanism creates an incentive that did not exist in this form before platform metrics: producers learn which content travels and supply more of it.
```

```novo
Audience measures shaped editorial decisions before platforms, and real-time platform metrics make this feedback faster and more visible: producers learn which content travels and supply more of it.
```

---

## T03-A38 — G3 (Manufactured consensus): remissão aos atores

| Campo | Valor |
|---|---|
| Lote | 2 |
| Decisões | 9.6-g |
| Localização | Seção 6.9, ficha G3, última frase |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
It is the clearest case of the actors defined in Section 2.3, who deliberately trigger or exploit mechanisms.
```

```novo
Its primary actors are automated or coordinated agents, the clearest case of actors who exploit mechanisms deliberately (Section 5.3).
```

---

## T03-A39 — G6 nova: Partisan flagging

| Campo | Valor |
|---|---|
| Lote | 2 |
| Decisões | D5, 3.3-K32-a a c |
| Localização | Seção 6.9, logo depois da ficha G5 |
| Ação | inserir-apos |
| Estado | aplicado em 2026-10-18 |

```ancora
The evidence is plausible rather than demonstrated, since the available work documents the beliefs more than their effect on attitudes toward the out-group.
```

```novo
G6. Partisan flagging (alt. biased crowdsourced flagging). The biased use of reporting tools, in which users flag content from the other side more than content from their own, the targeted side responds by lowering its own tolerance, and news sources adjust what they publish to avoid being flagged. The mechanism exists only where user reports affect the distribution of content (AF10). As Westermann and Coscia [NEW: Westermann and Coscia 2022] note, crowdsourced flagging systems assume that users are impartial arbiters of truth. In their simulation, sources on the side opposite to intolerant users attracted more flags and were nudged toward the side of those users, and high-tolerance regimes converged toward low-tolerance states. Users who have had content removed sometimes attribute the removal to coordinated reporting by their opponents [78]. The evidence is limited to this model. The mechanism acts on ideological polarization, by shifting the positions of sources, and on affective polarization, through mutual intolerance. It differs from perceived censorship (G5), a belief about moderation, because it concerns how users employ the moderation tools, and it sits on the supply side alongside metric-driven content production (E3).
```

---


## Lote 3a — Tabela consolidada e Tabela 6 (matriz das affordances)

**Convenções do lote 3a**:
- As duas tabelas são **refeitas por inteiro** (`substituir-tabela`): a tabela atual (a da T02, em
  verde) fica riscada, e a nova entra logo abaixo. Ambas usam os **IDs novos** (relatório, 9.1), e o
  lote 6 não as renumera.
- **Números das tabelas**: as legendas continuam "Table 5" e "Table 6" até o lote 6, que renumera
  todas as tabelas de uma vez (5 → 6 e 6 → 7) e as remissões no texto.
- **Tabela consolidada** com 9 colunas (9.5-a, b; 9.6-f): ID, Mechanism, Outcome, Platform role,
  Direction, Evidence strength, Primary actor, Secondary actor, Ref. Os valores de *Platform role*,
  *Direction* e *Evidence strength* seguem a 10.3 (5.3-a a e). Os atores seguem a 15.3 (9.2-a a e),
  com as abreviações da 9.6-f. Na coluna *Ref*, as referências atuais ficam, e entram as do segundo
  levantamento em que a força da evidência passou a se apoiar (base da 10.3), como `[NEW: …]`.
- **Tabela 6**: a coluna *Mechanisms fed* passa aos IDs novos e ganha as 14 ligações aprovadas no
  passo 4.3, com o sinal onde ele não é "+" (2.4-d). A coluna *Known intervention(s)* não muda.
- **Ordem de aplicação**: `--ids A40,A41,A42,A43`.

---

## T03-A40 — Tabela consolidada: legenda

| Campo | Valor |
|---|---|
| Lote | 3a |
| Decisões | 2.4-a a c, 5.3, 9.5-a, 9.6-f |
| Localização | Seção 6.11, legenda da tabela consolidada ("Complete mechanism taxonomy (39 mechanisms).") |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
(39 mechanisms).
```

```novo
(43 mechanisms). Platform role: whether social media creates, amplifies, or hosts the mechanism (Section 6.1). Direction and Evidence strength refer to the evidence on that role. Reinf., reinforcing. Actors (Section 5.3): OU, ordinary users. SG, social groups. OA, organized actors. CA, automated or coordinated agents. AS, algorithmic system. PL, platform.
```

---

## T03-A41 — Tabela consolidada: 43 mecanismos, 9 colunas

| Campo | Valor |
|---|---|
| Lote | 3a |
| Decisões | D5, D6, D10, 2.4-a a c, 5.3-a a e, 9.2-a a e, 9.5-a, 9.6-f |
| Localização | Seção 6.11, tabela consolidada |
| Ação | substituir-tabela |
| Estado | aplicado em 2026-10-18 |

**Âncora** (célula da tabela atual)

```ancora
Moderate–mixed
```

**Nova tabela**

```tabela
| ID | Mechanism | Outcome | Platform role | Direction | Evidence strength | Primary actor | Secondary actor | Ref |
| A1 | Filter bubble | Ideological | Creates | Mixed | Strong | AS | OU | [44,45], [NEW: Liu et al. 2025] |
| A2 | Algorithmic amplification | Affective, Ideological | Amplifies | Reinf. | Moderate | AS | PL | [14] |
| A3 | Algorithmic radicalization | Ideological | Creates | Mixed | Strong | AS | OU | [56,57], [NEW: Liu et al. 2025] |
| A4 | Algorithmic agenda-setting | Perceived | Amplifies | Reinf. | Plausible | AS | CA | [16,21] |
| B1 | Homophily | Structural | Amplifies | Reinf. | Moderate | OU | AS | [37,46], [NEW: Martel et al. 2024] |
| B2 | Unfriending | Structural | Amplifies | Reinf. | Strong | OU | — | [NEW: Martel et al. 2024; Kaiser et al. 2022] |
| B3 | Partisan sorting | Affective | Amplifies | Reinf. | Plausible | SG | OU | [62], [NEW: Törnberg 2022] |
| B4 | Interpersonal political tension | Affective, Perceived | Amplifies | Reinf. | Moderate | OU | — | [5] |
| B5 | Echo chamber | Ideological, Structural | Amplifies | Mixed | Moderate | OU | SG | [46], [NEW: Fletcher et al. 2021] |
| B6 | Group polarization | Ideological | Amplifies | Reinf. | Plausible | OU | SG | [61] |
| B7 | Negative social influence | Ideological, Affective | Amplifies | Mixed | Plausible | OU | SG | [NEW: Krueger et al. 2017; Carpentras et al. 2022] |
| B8 | Moral contagion | Affective | Amplifies | Reinf. | Moderate | OU | OA | [67] |
| B9 | Information cascades | Ideological, Perceived | Amplifies | Reinf. | Moderate | OU | CA | [51,52] |
| B10 | Online community radicalization | Ideological, Affective | Amplifies | Reinf. | Moderate | SG | OA | [76] |
| C1 | Motivated reasoning | Ideological, Affective | Hosts | Reinf. | Plausible | OU | — | [63] |
| C2 | Confirmation bias | Ideological, Affective | Amplifies | Mixed | Moderate | OU | — | [48], [NEW: Masip et al. 2020] |
| C3 | Selective avoidance | Ideological | Hosts | Mixed | Plausible | OU | — | [107,108] |
| C4 | Biased assimilation | Ideological | Hosts | Reinf. | Plausible | OU | — | [65] |
| C5 | Backfire effect | Ideological | Amplifies | Mixed | Moderate | OU | PL | [84], [NEW: Karlsen et al. 2017; Kim et al. 2025] |
| C6 | Hostile media effect | Affective | Hosts | Reinf. | Plausible | OU | — | [23] |
| C7 | Illusory truth effect | Ideological, Perceived | Amplifies | Reinf. | Plausible | OU | — | [66] |
| C8 | News avoidance | Structural (indirect), Behavioral | Amplifies | Reinf. | Plausible | OU | — | [79,80] |
| C9 | Reinforcing spiral | Varies | Amplifies | Reinf. | Plausible | OU | AS | [55] |
| D1 | Vocal minority | Perceived, Affective | Amplifies | Reinf. | Moderate | OU | — | [68] |
| D2 | Social proof | Perceived, Ideological | Amplifies | Reinf. | Moderate | OU | CA | [41] |
| D3 | False consensus | Perceived | Amplifies | Reinf. | Plausible | OU | — | [39] |
| D4 | Pluralistic ignorance | Perceived | Amplifies | Reinf. | Plausible | OU | SG | [40] |
| D5 | Spiral of silence | Perceived, Behavioral | Amplifies | Mixed | Moderate | OU | — | [24], [NEW: Geiß et al. 2021] |
| D6 | Exaggerated meta-perceptions | Affective, Perceived | Amplifies | Reinf. | Plausible | OU | — | [10,11] |
| E1 | Social learning of outrage | Affective | Amplifies | Reinf. | Strong | OU | PL | [13,71], [NEW: Konovalova et al. 2023] |
| E2 | Identity signaling | Affective | Amplifies | Reinf. | Moderate | OU | SG | [69], [NEW: Garz et al. 2020] |
| E3 | Metric-driven content production | Affective | Amplifies | Reinf. | Plausible | OA | PL | [102] |
| F1 | Online disinhibition effect | Affective | Amplifies | Mixed | Moderate | OU | — | [72] |
| F2 | Dogpiling | Behavioral, Affective | Amplifies | Reinf. | Moderate | OU | — | [73] |
| F3 | Message brevity | Affective | Amplifies | Reinf. | Moderate | OU | — | [9] |
| F4 | Incivility contagion | Behavioral, Affective | Amplifies | Reinf. | Moderate | OU | — | [50] |
| F5 | Incivility exposure effect | Ideological, Affective | Amplifies | Reinf. | Moderate | OU | — | [49,50] |
| G1 | Gatekeeping decline | Ideological, Perceived | Amplifies | Mixed | Plausible | PL | OA | [17,74] |
| G2 | Propaganda feedback loop | Ideological, Perceived | Amplifies | Reinf. | Moderate | OA | OU | [75] |
| G3 | Manufactured consensus | Perceived, Affective | Amplifies | Reinf. | Moderate | CA | OA | [54] |
| G4 | Platform migration | Structural, Affective | Amplifies | Mixed | Moderate | PL | SG | [77] |
| G5 | Perceived censorship | Affective | Amplifies | Reinf. | Plausible | OU | OA | [78] |
| G6 | Partisan flagging | Ideological, Affective | Creates | Reinf. | Plausible | OU | OA | [NEW: Westermann and Coscia 2022] |
```

---

## T03-A42 — Tabela 6: legenda

| Campo | Valor |
|---|---|
| Lote | 3a |
| Decisões | 2.4-d, 4.3 |
| Localização | Seção 8, legenda da Tabela 6 ("Complete affordance matrix.") |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
Complete affordance matrix.
```

```novo
Complete affordance matrix. Mechanism IDs as in Section 6. An asterisk marks an indirect link. (−) marks a link through which the affordance can weaken the mechanism, and (±) a link whose sign depends on how the feature is designed.
```

---

## T03-A43 — Tabela 6: ligações com os IDs novos e os mecanismos novos

| Campo | Valor |
|---|---|
| Lote | 3a |
| Decisões | 4.2 (a), 4.3, 2.4-d, D6 |
| Localização | Seção 8, Tabela 6 |
| Ação | substituir-tabela |
| Estado | aplicado em 2026-10-18 |

**Âncora** (célula da tabela atual)

```ancora
B1, B2*, B3*, D3*, D4*
```

**Nova tabela**

```tabela
| ID | Affordance | Alt. nomenclature | Mechanisms fed | Known intervention(s) |
| AF1 | Algorithmic content curation | algorithmic selection | A1, A2, A3, A4, B2 (−), B8, C3*, C7, C8, C9, D1, D6, G2, G3 | Chronological feed, tested, no detected attitude effect [94] |
| AF2 | Network-informed associating | connection recommendation, friend recommendation | B1, B5*, B6*, B7, D3*, D4* | Diversity-weighted recommendation, tested by simulation [59] |
| AF3 | Asymmetric following | directed association | B1, B2, B4*, B5*, B6*, C5, D3*, D4* | Paid cross-cutting exposure, tested in the field, reverse effect [84] |
| AF4 | Social quantification | metavoicing, metrification of sociality | B4*, B9, D2, E1, E2, G3 | Hiding public counters, industry practice, not peer-reviewed |
| AF5 | Replicability | n/a | B9, D6, E2 | Forward limits and accuracy nudges, tested [98] |
| AF6 | Audience segmentation | context collapse (low end) | B2, B4, B7, C5, D5, F2, F4 | Audience segmentation tools, under-tested |
| AF7 | Constraint affordance | n/a | A4, F3 | Character limit expansion, tested, robust [9] |
| AF8 | Identifiability | anonymity–identifiability spectrum | B2, B7, C5, F1, F2, G3 | Revise-before-post prompts, tested [95] |
| AF9 | Infinite scroll | absence of stopping cues | A2, B8, C7, C8 | Autoplay removal, open question |
| AF10 | Platform governance | n/a | A2 (±), C5 (±), G1, G4, G5, G6 | Deplatforming, tested, heterogeneous [77]. Transparency, tested [97] |
| AF11 | Group/community formation | n/a | B2, B3, B10 | Community quarantine, under-tested |
```

**Conversão dos IDs** (9.1): B2 → B5, B3 → B6, B4 → B9, B5 → B8, B6 → B3, B7 → B4, B8 → B10, C5 →
C6, C6 → C7, C7 → C8, C8 → C9. **Ligações novas** (4.3): AF1 → B2 (−); AF2 → B7; AF3 → B2, C5;
AF6 → B2, B7, C5; AF8 → B2, B7, C5; AF10 → A2 (±), C5 (±), G6; AF11 → B2. **Ligação retirada**:
AF3 → C3 (ver o ponto 1 abaixo).

**Ponto 1 — AF3 → C3**: a ligação se apoiava só no corte de laços ("asymmetric following (AF3) lets
users unfollow or unfriend disagreeing contacts at low cost", frase da ficha de C3 riscada no
lote 2, A25). Com a D6, o corte de laços passa a ser o *Unfriending* (B2), que já recebe AF3. Sem ele,
a C3 não tem passo causal próprio via AF3. **Proposta**: retirar AF3 → C3. AF1 → C3* (indireta)
continua.

**Decisões do usuário — lote 3a (2026-10-18)**: **3a-1**: retirar AF3 → C3 (aprovado). Os ajustes
T02-A165 e T02-A166, ainda não aplicados, foram revisados antes da aplicação para não introduzir a
ligação. **3a-2**: manter as referências novas na coluna *Ref* (aprovado). **3a-3 = (a)**: re-simular o
lote 10d da T02 e aplicá-lo antes da 3b (52 ajustes, simulação de 2026-10-18 sem erro).

---

## Lote 3b — Seção 7.1: ligações novas (passo 4.3)

**Convenções do lote 3b**:
- **Listas "It feeds…"**: as sete listas das affordances que ganham ligações (AF1, AF2, AF3, AF6, AF8,
  AF10, AF11) são refeitas pela linha da Tabela 6 nova (T03-A43), com os **IDs novos**, porque o B2
  novo (*Unfriending*) colide com o B2 atual (*Echo chamber*). O lote 6 não as renumera. As listas de
  AF4, AF5, AF7 e AF9 não ganham ligações e são renumeradas no lote 6.
- **Sinal nas listas**: "attenuating" para (−) e "sign depends on design" para (±), como na legenda da
  Tabela 6 (2.4-d).
- **Parágrafos "Why…"**: cada affordance ganha **um parágrafo novo** logo depois do seu "Why…"
  (`inserir-apos`), para não riscar texto dos autores. Os mecanismos novos aparecem pelo nome e pela
  seção, sem ID (regra do lote 2); o lote 6 acrescenta os IDs ao renumerar a 7.1.
- **Ligações como justificativa teórica** (4.3): AF6 → Unfriending e AF8 → Backfire effect, ditas
  assim no texto.
- **As Figuras 5–15** não mudam aqui (refação das figuras, pendência da T02).
- **Ordem de aplicação**: `--ids A44,A45,A46,A47,A48,A49,A50,A51,A52,A53,A54,A55,A56,A57`.

---

## T03-A44 — 7.1, AF1, lista It feeds…

| Campo | Valor |
|---|---|
| Lote | 3b |
| Decisões | 4.2 (a), 4.3 (AF1 → B2, −), 2.4-d |
| Localização | Seção 7.1, AF1, lista "It feeds…" |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
It feeds mechanisms in five blocks (Figure 5). Block A (Algorithmic curation): Filter bubble (A1), Algorithmic amplification (A2), Algorithmic radicalization (A3), and Algorithmic agenda-setting (A4). Block B (Networks, groups, and diffusion): Moral contagion (B5). Block C (Individual selection and processing of information): Selective avoidance (C3, indirect), Illusory truth effect (C6), News avoidance (C7), and Reinforcing spiral (C8). Block D (Perceptions of others): Vocal minority (D1) and Exaggerated meta-perceptions (D6). Block G (Information ecosystem and supply): Propaganda feedback loop (G2) and Manufactured consensus (G3).
```

```novo
It feeds mechanisms in five blocks (Figure 5). Block A (Algorithmic curation): Filter bubble (A1), Algorithmic amplification (A2), Algorithmic radicalization (A3), and Algorithmic agenda-setting (A4). Block B (Networks, groups, and diffusion): Unfriending (B2, attenuating) and Moral contagion (B8). Block C (Individual selection and processing of information): Selective avoidance (C3, indirect), Illusory truth effect (C7), News avoidance (C8), and Reinforcing spiral (C9). Block D (Perceptions of others): Vocal minority (D1) and Exaggerated meta-perceptions (D6). Block G (Information ecosystem and supply): Propaganda feedback loop (G2) and Manufactured consensus (G3).
```

---

## T03-A45 — 7.1, AF2, lista It feeds…

| Campo | Valor |
|---|---|
| Lote | 3b |
| Decisões | 4.2 (a), 4.3 (AF2 → B7) |
| Localização | Seção 7.1, AF2, lista "It feeds…" |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
It feeds mechanisms in two blocks (Figure 6). Block B (Networks, groups, and diffusion): Homophily (B1), Echo chamber (B2, indirect), and Group polarization (B3, indirect). Block D (Perceptions of others): False consensus (D3, indirect) and Pluralistic ignorance (D4, indirect).
```

```novo
It feeds mechanisms in two blocks (Figure 6). Block B (Networks, groups, and diffusion): Homophily (B1), Echo chamber (B5, indirect), Group polarization (B6, indirect), and Negative social influence (B7). Block D (Perceptions of others): False consensus (D3, indirect) and Pluralistic ignorance (D4, indirect).
```

---

## T03-A46 — 7.1, AF3, lista It feeds…

| Campo | Valor |
|---|---|
| Lote | 3b |
| Decisões | 4.2 (a), 4.3 (AF3 → B2, C5) |
| Localização | Seção 7.1, AF3, lista "It feeds…" |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
It feeds mechanisms in two blocks (Figure 7). Block B (Networks, groups, and diffusion): Homophily (B1), Echo chamber (B2, indirect), Group polarization (B3, indirect), and Interpersonal political tension (B7, indirect). Block D (Perceptions of others): False consensus (D3, indirect) and Pluralistic ignorance (D4, indirect).
```

```novo
It feeds mechanisms in three blocks (Figure 7). Block B (Networks, groups, and diffusion): Homophily (B1), Unfriending (B2), Interpersonal political tension (B4, indirect), Echo chamber (B5, indirect), and Group polarization (B6, indirect). Block C (Individual selection and processing of information): Backfire effect (C5). Block D (Perceptions of others): False consensus (D3, indirect) and Pluralistic ignorance (D4, indirect).
```

---

## T03-A47 — 7.1, AF6, lista It feeds…

| Campo | Valor |
|---|---|
| Lote | 3b |
| Decisões | 4.2 (a), 4.3 (AF6 → B2, B7, C5) |
| Localização | Seção 7.1, AF6, lista "It feeds…" |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
It feeds mechanisms in three blocks (Figure 10). Block B (Networks, groups, and diffusion): Interpersonal political tension (B7). Block D (Perceptions of others): Spiral of silence (D5). Block F (Interaction): Dogpiling (F2) and Incivility contagion (F4).
```

```novo
It feeds mechanisms in four blocks (Figure 10). Block B (Networks, groups, and diffusion): Unfriending (B2), Interpersonal political tension (B4), and Negative social influence (B7). Block C (Individual selection and processing of information): Backfire effect (C5). Block D (Perceptions of others): Spiral of silence (D5). Block F (Interaction): Dogpiling (F2) and Incivility contagion (F4).
```

---

## T03-A48 — 7.1, AF8, lista It feeds…

| Campo | Valor |
|---|---|
| Lote | 3b |
| Decisões | 4.2 (a), 4.3 (AF8 → B2, B7, C5) |
| Localização | Seção 7.1, AF8, lista "It feeds…" |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
It feeds mechanisms in two blocks (Figure 12). Block F (Interaction): Online disinhibition effect (F1) and Dogpiling (F2). Block G (Information ecosystem and supply): Manufactured consensus (G3).
```

```novo
It feeds mechanisms in four blocks (Figure 12). Block B (Networks, groups, and diffusion): Unfriending (B2) and Negative social influence (B7). Block C (Individual selection and processing of information): Backfire effect (C5). Block F (Interaction): Online disinhibition effect (F1) and Dogpiling (F2). Block G (Information ecosystem and supply): Manufactured consensus (G3).
```

---

## T03-A49 — 7.1, AF10, lista It feeds…

| Campo | Valor |
|---|---|
| Lote | 3b |
| Decisões | 4.2 (a), 4.3 (AF10 → A2 ±, C5 ±, G6), 2.4-d |
| Localização | Seção 7.1, AF10, lista "It feeds…" |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
It feeds three mechanisms of Block G (Information ecosystem and supply), shown in Figure 14: Gatekeeping decline (G1), Platform migration (G4), and Perceived censorship (G5).
```

```novo
It feeds mechanisms in three blocks (Figure 14). Block A (Algorithmic curation): Algorithmic amplification (A2, sign depends on design). Block C (Individual selection and processing of information): Backfire effect (C5, sign depends on design). Block G (Information ecosystem and supply): Gatekeeping decline (G1), Platform migration (G4), Perceived censorship (G5), and Partisan flagging (G6).
```

---

## T03-A50 — 7.1, AF11, lista It feeds…

| Campo | Valor |
|---|---|
| Lote | 3b |
| Decisões | 4.2 (a), 4.3 (AF11 → B2) |
| Localização | Seção 7.1, AF11, lista "It feeds…" |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
It feeds two mechanisms of Block B (Networks, groups, and diffusion), shown in Figure 15: Partisan sorting (B6) and Online community radicalization (B8).
```

```novo
It feeds three mechanisms of Block B (Networks, groups, and diffusion), shown in Figure 15: Unfriending (B2), Partisan sorting (B3), and Online community radicalization (B10).
```

---

## T03-A51 — 7.1, AF1, parágrafo novo: Unfriending (sinal negativo)

| Campo | Valor |
|---|---|
| Lote | 3b |
| Decisões | 4.3 (AF1 → B2, −), 2.4-d |
| Localização | Seção 7.1, logo depois do segundo parágrafo "Why AF1…" |
| Ação | inserir-apos |
| Estado | aplicado em 2026-10-18 |

```ancora
the prototype of the reinforcing-spiral mechanism itself (Section 5.2).
```

```novo
The link to unfriending (Section 6.4) runs in the opposite direction. In a simulation, algorithmic personalization slowed the cascades of exits from communities under some conditions [NEW: Törnberg 2026], so curation can weaken this mechanism rather than feed it.
```

---

## T03-A52 — 7.1, AF2, parágrafo novo: Negative social influence

| Campo | Valor |
|---|---|
| Lote | 3b |
| Decisões | 4.3 (AF2 → B7) |
| Localização | Seção 7.1, logo depois do "Why AF2…" |
| Ação | inserir-apos |
| Estado | aplicado em 2026-10-18 |

```ancora
It sets the stage on which they can function.
```

```novo
The link to negative social influence (Section 6.4) is direct. Suggestions that reach beyond the local network multiply contacts with distant others, which is the condition for repulsive influence, and in a model with homophily and social balance, polarization rose abruptly above a critical level of social connectivity [NEW: Thurner et al. 2025].
```

---

## T03-A53 — 7.1, AF3, parágrafo novo: Unfriending e Backfire effect

| Campo | Valor |
|---|---|
| Lote | 3b |
| Decisões | 4.3 (AF3 → B2, C5), 3a-1 |
| Localização | Seção 7.1, logo depois do "Why AF3…" |
| Ação | inserir-apos |
| Estado | aplicado em 2026-10-18 |

```ancora
by Bail et al. [86] by Bail et al. [84].
```

```novo
The link to unfriending (Section 6.4) isolates the tie-cutting step described above for homophily. A single unilateral action ends a tie, and in two field experiments on Twitter, users were 12 and 4 times more likely to block counter-partisan than copartisan accounts [NEW: Martel et al. 2024]. The link to the backfire effect (Section 6.5) offers a further reading of the result of Bail et al. [84]: following accounts of the other side brings regular counter-attitudinal messages, which can harden prior positions.
```

---

## T03-A54 — 7.1, AF6, parágrafo novo: Unfriending, Negative social influence e Backfire effect

| Campo | Valor |
|---|---|
| Lote | 3b |
| Decisões | 4.3 (AF6 → B2 como justificativa teórica, B7, C5) |
| Localização | Seção 7.1, logo depois do "Why AF6…" |
| Ação | inserir-apos |
| Estado | aplicado em 2026-10-18 |

```ancora
the trigger at the core of the mechanism.
```

```novo
Low segmentation also feeds three further mechanisms. By making the political posts of every contact visible, it creates the occasion for unfriending (Section 6.4), a link that rests on theoretical grounds. By mixing audiences, it raises the dose of contact with the out-group, which drives negative social influence (Section 6.4) in models where antagonistic groups are densely connected [NEW: Krueger et al. 2017]. The same incidental exposure to the other side is the occasion for the backfire effect (Section 6.5), and in Spain, users more active on social media were more likely to encounter news from outlets with a different ideology [NEW: Masip et al. 2020].
```

---

## T03-A55 — 7.1, AF8, parágrafo novo: Unfriending, Negative social influence e Backfire effect

| Campo | Valor |
|---|---|
| Lote | 3b |
| Decisões | 4.3 (AF8 → B2, B7, C5 como justificativa teórica) |
| Localização | Seção 7.1, logo depois do "Why AF8…" |
| Ação | inserir-apos |
| Estado | aplicado em 2026-10-18 |

```ancora
coordinated manipulation at scale.
```

```novo
Identifiability also works before any message is read. Partisan identity displayed on a profile signals the other side, and in field experiments on Twitter, accounts identified as Democrats or Republicans were blocked along partisan lines [NEW: Martel et al. 2024], which feeds unfriending (Section 6.4). The same signal marks the other as a member of the out-group, the condition for negative social influence (Section 6.4) in models where out-group animosity outweighs in-group favoritism [NEW: Nettasinghe et al. 2025]. Finally, it can make a counter-attitudinal message read as an attack from the out-group, which on theoretical grounds feeds the backfire effect (Section 6.5).
```

---

## T03-A56 — 7.1, AF10, parágrafo novo: Partisan flagging, Backfire effect e Algorithmic amplification

| Campo | Valor |
|---|---|
| Lote | 3b |
| Decisões | 4.3 (AF10 → G6, C5 ±, A2 ±), 2.4-d, 3.4-e |
| Localização | Seção 7.1, logo depois do "Why AF10…" |
| Ação | inserir-apos |
| Estado | aplicado em 2026-10-18 |

```ancora
self-censored their posts to avoid them [Ronzhyn et al., 117].
```

```novo
Three further links depend on how governance tools are designed. Partisan flagging (Section 6.9) exists only where user reports affect the distribution of content, and in a simulation, biased reporting nudged news sources toward the side of intolerant users [NEW: Westermann and Coscia 2022]. For the backfire effect (Section 6.5), the sign depends on the form of correction: on Twitter, users whose posts were tagged as misinformation by other users retreated into information bubbles, an effect softened when tagging went through the collective verification of Community Notes [NEW: Kim et al. 2025]. For algorithmic amplification (Section 6.3), policies that grant some accounts greater reach reduced polarization in a simulation when the prioritized users behaved like other users, and sharpened echo chambers when they were stubborn ideologues [NEW: Arruda et al. 2024].
```

---

## T03-A57 — 7.1, AF11, parágrafo novo: Unfriending

| Campo | Valor |
|---|---|
| Lote | 3b |
| Decisões | 4.3 (AF11 → B2) |
| Localização | Seção 7.1, logo depois do "Why AF11…" |
| Ação | inserir-apos |
| Estado | aplicado em 2026-10-18 |

```ancora
rather than a single episode [Munn, 76].
```

```novo
The link to unfriending (Section 6.4) comes from the exit side of the same possibility. Communities offer destinations for users who leave when local dissatisfaction passes a threshold, and in a simulation, such exits cascaded into strong segregation without any preference for homogeneity [NEW: Törnberg 2026].
```

---

## Lote 4 — Discussão (Seção 9) e implicações para o jornalismo (10.2)

**Convenções do lote 4**:
- **IDs**: o texto novo usa a **numeração nova**, como no lote 1 e nas tabelas. O texto atual dos
  autores na Seção 9 e na 10.2 (ex.: "News avoidance (C7)") é renumerado no lote 6. Até lá, um mesmo
  mecanismo pode aparecer com dois IDs em parágrafos vizinhos, sempre acompanhado do nome.
- **Subseção nova** (2.3-a): entra como **9.2**, e *Limitations* passa a **9.3**. As quatro remissões
  à "Section 9.2" que se referem às limitações passam a "Section 9.3" neste lote (A62–A65).
- **Remissões a tabelas**: o texto novo cita a tabela consolidada como "Section 6.11" e a matriz das
  affordances como "Section 8", para não depender da renumeração das tabelas (lote 6).
- **6.1 em português**: a frase de remissão na 6.1 (2.3-a, 2.3-b, 2.4-e) entra em português, o idioma
  atual da seção, como na T02 (lote 10a). A tradução e a troca dos nomes das colunas na 6.1 ficam para
  a reescrita da 6.1 (pendência T02.4).
- **Estilo de título**: o título "9.2. What platforms do to mechanisms…" entra como parágrafo comum,
  como aconteceu com a 5.3. **Aplicar o estilo de título à mão.**
- **Ordem de aplicação**: `--ids A58,A59,A60,A61,A62,A63,A64,A65,A66,A67,A68,A69,A70,A71`.

---

## T03-A58 — 9.1, parágrafo sobre a avaliação da evidência

| Campo | Valor |
|---|---|
| Lote | 4 |
| Decisões | 5.3-a a d (D10); pendência da T02 sobre "only a single mechanism" (INDEX) |
| Localização | Seção 9.1, terceiro parágrafo ("The individual evidentiary assessment…") |
| Ação | substituir-paragrafo |
| Estado | aplicado em 2026-10-18 |

```original
The individual evidentiary assessment of all 41 mechanisms (Section 6.11 all 39 mechanisms (Section 6.11, Table 4 5) revealed a second unanticipated finding: only a single mechanism, AF7 via F3 Constraint affordance (AF7) via Low-context communication (F3) via Message brevity (F3), is supported by robust, direct causal evidence in the identified literature [Jaidka et al., 9]. The majority of the remaining mechanisms were classified as having moderate, mixed, or plausible support. Far from weakening the taxonomy, this heterogeneity is precisely what a unified, auditable table like Table 4 5 is designed to expose, a capability absent in previous synthesis literature (Section 3), which treats mechanisms in broad clusters without individual evaluation.
```

```novo
The individual assessment of the evidence on the role of platforms in each of the 43 mechanisms (Section 6.11) revealed a second unanticipated finding. Only four mechanisms, Filter bubble (A1), Algorithmic radicalization (A3), Unfriending (B2), and Social learning of outrage (E1), rest on experimental or quasi-experimental evidence from platforms that more than one study replicates, and for two of them, A1 and A3, the results point in opposite directions. Twenty-one mechanisms have moderate support, and eighteen remain plausible, supported by simulations, theory, or evidence of the phenomenon outside platforms. The most robust single causal result in this literature concerns an intervention rather than a mechanism: expanding the character limit on Twitter made discussions more civil [Jaidka et al., 9]. Far from weakening the taxonomy, this heterogeneity is precisely what a unified, auditable table like the one in Section 6.11 is designed to expose, a capability absent in previous synthesis literature (Section 3), which treats mechanisms in broad clusters without individual evaluation.
```

**Contagem** (tabela consolidada aplicada no lote 3a): Strong 4 (A1, A3, B2, E1) · Moderate 21 ·
Plausible 18 = 43. *Direction* = Mixed em A1 e A3.

---

## T03-A59 — 9.1, parágrafo novo: atores

| Campo | Valor |
|---|---|
| Lote | 4 |
| Decisões | 9.6-h, 9.2-e |
| Localização | Seção 9.1, logo depois do parágrafo sobre *perceived polarization* |
| Ação | inserir-apos |
| Estado | aplicado em 2026-10-18 |

```ancora
one of the framework's most generative dimensions.
```

```novo
The actor mapping (Section 5.3, Table 5) adds a further finding. Organized and automated actors are primary actors only in the supply of information, in Block G and in metric-driven content production (E3), while behavioral polarization appears only with ordinary users as the primary actor. Most of the mechanisms catalogued here therefore operate through the aggregated and largely non-strategic action of ordinary users, which limits what measures against manipulation campaigns can achieve on their own.
```

**Diferença em relação ao texto aprovado na 9.6-h**: a 5.3 (lote 1) já diz que atores organizados e
automatizados só são primários no bloco G e em E3, e que o outcome comportamental só aparece com
usuários comuns. Para não repetir a 5.3, este parágrafo junta os dois achados numa frase e acrescenta
a consequência para a Discussão (a última frase, **inferência nova**). Se preferir o texto da 9.6-h
como foi aprovado, eu troco.

**Decisão do usuário (2026-10-18)**: versão nova aprovada.

---

## T03-A60 — Subseção nova 9.2: o que as plataformas fazem com os mecanismos

| Campo | Valor |
|---|---|
| Lote | 4 |
| Decisões | 2.3-a, b, e, f; 5.3-b, c; 2.4-d |
| Localização | Seção 9, logo depois do último parágrafo da 9.1 (termina em "[Voinea, 115].") |
| Ação | inserir-apos |
| Estado | aplicado em 2026-10-18 |

```ancora
an algorithmic aversion loop [Voinea, 115].
```

```novo
9.2. What platforms do to mechanisms: create, amplify, host, or attenuate
The definition adopted in Section 2.1 treats SMIP as the processes through which platform design, usage, and governance generate, amplify, or host intergroup division, and the Platform role column (Section 6.11) records which of these applies to each mechanism. Thirty-six of the 43 mechanisms are amplified: the process exists without platforms, and platforms change its dose, speed, or reach. Three are created, because they depend on systems that exist only on platforms, namely the personalization behind the filter bubble (A1) and algorithmic radicalization (A3), and the reporting tools that partisan flagging (G6) uses. Four are hosted. Motivated reasoning (C1), selective avoidance (C3), biased assimilation (C4), and the hostile media effect (C6) work in the same way on and off platforms, which provide the occasion for them. For these four, the evidence on the role of platforms can at most be plausible, since by definition the platform does not change the process.
The Platform role column measures the contribution of platforms relative to other routes, not the presence of a mechanism. Most mechanisms also operate through partisan media, political elites, face-to-face networks, and residential segregation. In the United States, partisan exposure in physical space predicted vote choice better than online ties [NEW: Tonin et al. 2025]. In Spain, a survey of registered users of online news media found that the high selective exposure characteristic of offline news consumption was moderated online [NEW: Masip et al. 2020], and across seven countries, more internet users consumed no online news at all than lived in partisan online news echo chambers [NEW: Fletcher et al. 2021]. Observing a mechanism on a platform therefore does not show that the platform caused it, which is why the evidence ratings count only studies that isolate the role of platforms (Section 9.3).
Platforms can also weaken mechanisms, and the same design element can feed one mechanism while it weakens another. Personalization feeds the filter bubble (A1), but in a simulation it slowed the exit cascades that drive unfriending (B2) [NEW: Törnberg 2026]. Exposure to the other side counters the echo chamber (B5), yet Republicans who followed a Twitter bot that exposed them to opposing messages became more conservative [Bail et al., 84], a backfire effect (C5). Accounts whose content reaches users on both sides of a divide provoked less uncivil discourse than partisan accounts in Canada and more in Brazil [NEW: Kobellarz et al. 2024], so the effect of cross-cutting exposure also depends on the political context. None of the 43 mechanisms has evidence that platforms on balance attenuate it, but eleven have mixed evidence, and the affordance matrix (Section 8) marks the links whose sign is negative or depends on design. An intervention that mitigates one mechanism can therefore activate another, and evaluations of interventions need to measure more than the mechanism they target.
Causality also runs from polarization to platforms. In Dutch panel data, social media use did not predict later affective polarization, while affective polarization predicted later social media use [NEW: Nordbrandt 2021]. This adds to the feedback loop of Section 5.2, which closes through features, a second route that closes through usage, which the definition in Section 2.1 names alongside design and governance. Associations between platform use and polarization from cross-sectional designs are therefore compatible with either direction (Section 9.3).
```

**Contagens** (tabela consolidada): *Platform role* Amplifies 36 · Creates 3 (A1, A3, G6) · Hosts 4
(C1, C3, C4, C6) = 43. *Direction* Mixed 11, Attenuating 0.

---

## T03-A61 — Título da 9.2 atual (Limitations) passa a 9.3

| Campo | Valor |
|---|---|
| Lote | 4 |
| Decisões | 2.3-a |
| Localização | Seção 9, título "9.2. Limitations" |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
9.2. Limitations
```

```novo
9.3. Limitations
```

---

## T03-A62 — Remissão às limitações (1 de 4)

| Campo | Valor |
|---|---|
| Lote | 4 |
| Decisões | 2.3-a |
| Localização | "…a gap acknowledged in Section 9.2." |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
a gap acknowledged in Section 9.2.
```

```novo
a gap acknowledged in Section 9.3.
```

---

## T03-A63 — Remissão às limitações (2 de 4)

| Campo | Valor |
|---|---|
| Lote | 4 |
| Decisões | 2.3-a |
| Localização | "…its limitations are discussed in Section 9.2." |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
its limitations are discussed in Section 9.2.
```

```novo
its limitations are discussed in Section 9.3.
```

---

## T03-A64 — Remissão às limitações (3 de 4)

| Campo | Valor |
|---|---|
| Lote | 4 |
| Decisões | 2.3-a |
| Localização | "…discussed in more depth in Section 9.2." |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
discussed in more depth in Section 9.2.
```

```novo
discussed in more depth in Section 9.3.
```

---

## T03-A65 — Remissão às limitações (4 de 4)

| Campo | Valor |
|---|---|
| Lote | 4 |
| Decisões | 2.3-a |
| Localização | Seção 11, "As detailed in Section 9.2, the empirical foundation…" |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
As detailed in Section 9.2,
```

```novo
As detailed in Section 9.3,
```

---

## T03-A66 — 9.3, terceira limitação: regra da força da evidência e causalidade reversa

| Campo | Valor |
|---|---|
| Lote | 4 |
| Decisões | 5.3-a, 2.3-f |
| Localização | Seção 9.3 (atual 9.2), terceira limitação, última frase |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
rather than a established finding.
```

```novo
rather than an established finding. The Evidence strength column reduces this heterogeneity without removing it. It counts as evidence of the role of platforms only studies with data on actual platform use, such as field experiments, quasi-experiments, trace or content data, and surveys about platform use. Strong denotes experimental or quasi-experimental evidence from platforms that more than one study replicates, moderate denotes a single platform experiment or consistent observational or survey data from platforms, and plausible denotes support from simulations, theory, or evidence of the phenomenon outside platforms. Reverse causality is a general caveat, since polarization also shapes social media use (Section 9.2).
```

**Nota**: a troca corrige também "a established" para "an established".

---

## T03-A67 — 9.3, quarta limitação: sinais opostos

| Campo | Valor |
|---|---|
| Lote | 4 |
| Decisões | 2.3-e, 2.4-d |
| Localização | Seção 9.3 (atual 9.2), quarta limitação, última frase |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
is identified as a priority item in Section 11.
```

```novo
is identified as a priority item in Section 11. The links can also carry opposite signs. The same affordance can feed one mechanism and weaken another, as the links marked (−) and (±) in the affordance matrix record, so the effect of intervening on an affordance cannot be read from a single link (Section 9.2).
```

---

## T03-A68 — 5.2, parágrafo novo: o loop também fecha pelo uso

| Campo | Valor |
|---|---|
| Lote | 4 |
| Decisões | 2.3-f (T03-I03) |
| Localização | Seção 5.2, logo depois do último parágrafo (termina em "…testable causal hypotheses."), antes do título da 5.3 |
| Ação | inserir-apos |
| Estado | aplicado em 2026-10-18 |

```ancora
a set of specific, testable causal hypotheses.
```

```novo
The loop can also close through usage rather than through features. In Dutch panel data, it was affective polarization that predicted later social media use, and not social media use that predicted later polarization [NEW: Nordbrandt 2021]. Section 9.2 returns to this second route.
```

---

## T03-A69 — 10.2, primeiro item: jornais como atores organizados

| Campo | Valor |
|---|---|
| Lote | 4 |
| Decisões | 9.6-i |
| Localização | Seção 10.2, primeiro item, depois de "…a testable hypothesis." |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
a testable hypothesis.
```

```novo
a testable hypothesis. In the actor typology of Section 5.3, news organizations that adapt their output to engagement metrics are organized actors and the primary actor of E3.
```

---

## T03-A70 — 10.2, quinto item novo: o jornalismo dos dois lados da distinção

| Campo | Valor |
|---|---|
| Lote | 4 |
| Decisões | 2.3-d |
| Localização | Seção 10.2, logo depois do quarto item (termina em "…offers complementary frameworks.") |
| Ação | inserir-apos |
| Estado | aplicado em 2026-10-18 |

```ancora
offers complementary frameworks.
```

```novo
Fifth, news organizations stand on both sides of the distinction drawn in Section 9.2. Journalism is one of the routes outside platforms through which several mechanisms operate, since partisan outlets supply much of the content that platforms then amplify. In a panel study, use of pro-attitudinal partisan news online was associated with anger at the opposing candidate, which in turn facilitated political information sharing on social media [NEW: Hasell and Weeks 2016]. News organizations are also actors on platforms, as producers who adapt to engagement metrics (E3), as gatekeepers whose role platforms redistribute (G1), and as targets of the hostile media effect (C6) and of news avoidance (C8). Editorial choices can therefore add to the dose of the mechanisms that platforms amplify, or reduce it, within the part of the process that newsrooms control.
```

---

## T03-A71 — 6.1, parágrafo da coluna *Claim*: contribuição relativa e atenuação

| Campo | Valor |
|---|---|
| Lote | 4 |
| Decisões | 2.3-a, 2.3-b, 2.4-e; decisão do usuário de 2026-10-18 (incluir, item 3) |
| Localização | Seção 6.1, parágrafo "Para 'Claim'…", última frase |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
de forma substancial.
```

```novo
de forma substancial. A coluna mede a contribuição das plataformas em relação a outras vias, como a mídia partidária e as redes presenciais, e não a presença do mecanismo. Os mesmos elementos de design que criam, amplificam ou hospedam um mecanismo também podem atenuá-lo, e a coluna Direction registra o sentido da evidência sobre esse papel (Seção 9.2).
```

**Nota**: em português, como o resto da 6.1. A versão em inglês entra na reescrita da 6.1 (T02.4).

**Decisões do usuário — lote 4 (2026-10-18)**: **1** versão nova de A59 aprovada (sem repetir a 5.3);
**2** IDs novos no texto novo durante a transição, aprovado; **3** a remissão na 6.1 entra (A71).

---

## Lote 5 — Método (4.3), Apêndice A, Table A1 e *Acknowledgments*

**Convenções do lote 5**:
- **Informações dos autores ainda pendentes** (D12; pedido do usuário de 2026-10-18: redigir com o
  que já se sabe): o texto usa *placeholders* `[AUTHORS: …]` em inglês, para os autores preencherem
  ou apagarem. Pendentes: o processo da primeira lista (direção do *chaining*, iterações, critério de
  parada, janela temporal, exclusões, quem conduziu), o período, o modelo e a forma de uso do Claude
  na primeira lista, o critério de elegibilidade usado na triagem, e as versões e os prompts do Gemini.
- **Cuidado da T02.4**: os critérios de consolidação (teste de mecanismo, regras de nome, base dos
  blocos) aparecem em A.1 como **etapa posterior**, e não como critérios que guiaram a identificação
  original.
- **Posição** (template MDPI): *Acknowledgments* depois do *Informed Consent Statement*; o Apêndice A
  depois dos *Conflicts of Interest*, antes das *References*. Os títulos do apêndice (A, A.1–A.4)
  entram como parágrafos comuns: **estilo de título à mão**.
- **Figura A1** (fluxo 886 → 226 → 144 → 43): entra só a legenda, com um marcador para a imagem.
  A imagem é inserida à mão, como a Figura 2.
- **IDs**: numeração nova, como nos lotes anteriores.
- **Ordem de aplicação**: `--ids A72,A73,A74,A75,A76,A77,A78,A79`.

---

## T03-A72 — 4.3, parágrafo novo: as duas origens da lista

| Campo | Valor |
|---|---|
| Lote | 5 |
| Decisões | D1 (Opção C), D2 (a), D11, D12, 6.4-a; passo 8.1 (e) |
| Localização | Seção 4.3, logo depois do último parágrafo (termina em "…discussed in more depth in Section 9.3.") |
| Ação | inserir-apos |
| Estado | aplicado em 2026-10-18 |

```ancora
discussed in more depth in Section 9.3.
```

```novo
The 43 mechanisms of Section 6 come from two sources. The first list, identified through the process above, was initially compiled with the assistance of a generative AI tool and later consolidated from 41 into 39 mechanisms under a mechanism test. A second, structured survey of the Lens database then tested this list and added four mechanisms. Its search string was deliberately built around mechanisms already in the list, so the survey complements the directed search rather than replacing it. Appendix A describes both procedures, the use of generative AI and the human verification at each stage, and the relation between the two lists (Table A1).
```

---

## T03-A73 — 6.1, remissão à Table A1 (em português)

| Campo | Valor |
|---|---|
| Lote | 5 |
| Decisões | 5.2-b; passo 8.1 (e) |
| Localização | Seção 6.1, primeiro parágrafo, última frase |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
'Outcome', 'Claim' e 'Evidence'.
```

```novo
'Outcome', 'Claim' e 'Evidence'. A origem de cada mecanismo, na primeira lista ou no segundo levantamento, e o suporte que ele encontra no segundo levantamento estão na Table A1 (Apêndice A).
```

**Nota**: em português, como o resto da 6.1 (lote 4, A71).

---

## T03-A74 — 9.3, primeira limitação: o segundo levantamento tem o mesmo limite

| Campo | Valor |
|---|---|
| Lote | 5 |
| Decisões | D2 (a), T03-F01, 5.2-c |
| Localização | Seção 9.3, primeira limitação, frase que termina em "…did not capture it." |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
but only that the citation-chaining strategy applied here did not capture it.
```

```novo
but only that the citation-chaining strategy applied here did not capture it. The second survey (Appendix A) tested the list against a structured search, but it shares this limitation, since its string was built around mechanisms already in the list and did not reach the interaction and supply mechanisms of Blocks F and G.
```

---

## T03-A75 — Seção 11, remissão às limitações (correção do lote 4)

| Campo | Valor |
|---|---|
| Lote | 5 |
| Decisões | 2.3-a; **correção do lote 4** (regra 7): a busca do lote 4 procurou "Section 9.2" no singular e não pegou esta ocorrência no plural |
| Localização | Seção 11, "Systematic test of coverage" |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
As discussed in Sections 4.1 and 9.2,
```

```novo
As discussed in Sections 4.1 and 9.3,
```

---

## T03-A76 — Seção 11, teste de cobertura: o segundo levantamento como primeiro passo

| Campo | Valor |
|---|---|
| Lote | 5 |
| Decisões | 5.2-c |
| Localização | Seção 11, "Systematic test of coverage", frase que termina em "…reached by citation chaining." |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
cover the literature beyond the sources reached by citation chaining.
```

```novo
cover the literature beyond the sources reached by citation chaining. The second survey reported in Appendix A is a first, partial step, and a search directed at the interaction and supply mechanisms of Blocks F and G, which it did not reach, is the most immediate extension.
```

---

## T03-A77 — *Acknowledgments*: declaração do uso de IA generativa

| Campo | Valor |
|---|---|
| Lote | 5 |
| Decisões | 6.4-a a c (texto aprovado), D12 |
| Localização | Depois do *Informed Consent Statement* |
| Ação | inserir-apos |
| Estado | aplicado em 2026-10-18 |

```ancora
Informed consent was obtained from all subjects involved in the study.
```

```novo
Acknowledgments: During the preparation of this study, the authors used generative AI tools as follows. Claude (Anthropic, web interface) assisted in the initial compilation of the first list of mechanisms [AUTHORS: period and model, if available]. Gemini (Google, web interface) was used to screen the records retrieved from Lens, and Gemini Notebook (Google, web interface) was used to extract candidate mechanisms from the full texts of the eligible papers, between 11 and 18 October 2026. Claude (Anthropic), through Claude Code, assisted in consolidating the extracted mechanisms, checking their attributions against the papers, and revising and drafting parts of the manuscript. The procedure and the human verification applied at each stage are described in Section 4.3 and Appendix A. The authors reviewed and edited all output and take full responsibility for the content of this publication.
```

**Nota**: o texto é o aprovado em 6.4-c, com uma correção de fato: "against the full texts" passa a "against the papers", porque a conferência da T03.7 leu o abstract e a primeira página (16.1), e o texto completo só em parte dos casos. A política da MDPI sobre IA ainda precisa ser conferida
na página de ética antes da submissão (6.4-d, P8).

---

## T03-A78 — Apêndice A: identificação dos mecanismos

| Campo | Valor |
|---|---|
| Lote | 5 |
| Decisões | D11 (estrutura A.1–A.4), D12, D1, D2 (a), D3, D9, 5.2-b, 5.2-c, 5.5 (comentários 1–4), 5.6 |
| Localização | Depois dos *Conflicts of Interest*, antes das *References* |
| Ação | inserir-apos |
| Estado | aplicado em 2026-10-18 |

```ancora
The authors declare no conflicts of interest.
```

```novo
Appendix A. Identification of the mechanisms
The 43 mechanisms of Section 6 come from two sources: a first list compiled from the anchor works and the literature they cite, and a second, structured survey that tested the first list and added four mechanisms. This appendix describes both, the relation between them, and the use of generative AI in the process.
A.1. The first list
The first list was compiled from the four anchor works discussed in Sections 1 through 3 [2–5], by citation chaining to the foundational literature for each mechanism (Section 4.3). It was initially assembled with the assistance of a generative AI tool, Claude (Anthropic, web interface) [AUTHORS: period, model, and form of use]. A candidate mechanism was retained only if it could be anchored in at least one primary source with an explicit operational definition. [AUTHORS: direction of the chaining (backward, forward, or both), number of iterations, stopping criterion, time window, exclusions, and who conducted each step.] The resulting list had 41 mechanisms in nine blocks.
A later consolidation step, carried out during the revision of the manuscript, applied a mechanism test to each item. The test asked whether the item names a process rather than a state, whether the process can be written as a chain from an input condition to a change in at least two steps, whether that change is one of the five outcome types without being the outcome itself, and whether the item belongs to another category of Section 2.3, such as a feature, an affordance, a contingency, or an actor. The step also applied naming rules and a single criterion for grouping mechanisms into blocks, the locus of the process. It merged three items into others, excluded one, and split two, which yielded 39 mechanisms in seven blocks. These criteria were applied after the original identification and did not guide it.
A.2. The second survey
The second survey was designed to test the first list against a structured search and to identify mechanisms that it missed. It was not intended as a systematic review (Section 4.1). On 13 October 2026, the Lens database was searched with the string mechanism AND "social media" AND polarization AND (feature OR outcome OR contingencies) AND ("echo chamber" OR "filter bubble" OR "confirmation bias" OR "homophily" OR "news avoidance"), limited to journal articles, conference proceedings articles, and book chapters. The first part of the string restricts the search to studies of mechanisms of polarization on social media. The second targets studies that relate mechanisms to other layers of the framework (features, outcomes, and contingencies). The third deliberately requires at least one of five mechanisms already in the first list, so that the search retrieves studies that work within the same theoretical vocabulary, at the cost of missing mechanisms described in other terms.
The search returned 886 records, exported with their titles and, where Lens provided them, their abstracts. Most records came without an abstract. The records were screened in four batches of about 200 with Gemini (Google, web interface) [AUTHORS: eligibility criterion used in the screening]. The screening judged 226 records eligible, and full texts were obtained for 223 of them. Candidate mechanisms were then extracted from these full texts with Gemini Notebook (Google, web interface), which produced 66 entries, each with a definition, the papers that support it, and proposed links to the eleven affordances. Screening and extraction took place between 11 and 18 October 2026. The authors checked the titles of the eligible records and the coherence of the extracted mechanisms with the papers indicated and with the first list.
The 66 entries were grouped into 33 units, and each unit was submitted to the mechanism test of A.1 and to two further criteria: whether social media create, amplify, or host the process through an identified affordance, and how strong the evidence on that role is (Section 9.3). Fifteen units corresponded to mechanisms already in the first list, and four were accepted as new mechanisms: Unfriending (B2), Negative social influence (B7), Backfire effect (C5), and Partisan flagging (G6). The other fourteen were absorbed into the definitions of existing mechanisms, kept as evidence for them, or excluded, because they lacked a route through a platform affordance, rested on a single model or study, or described a process running from polarization to its causes. The links that Gemini Notebook proposed between the new mechanisms and the affordances were treated as drafts and kept only when a causal step could be stated, in the same way as the links of the first list (Section 7.1).
A paper entered the synthesis if it was cited as a reference for one of the resulting mechanisms, which included 144 of the 223 papers. This article cites 43 of them. Each of these 43 was checked against the paper itself, at least its abstract and first page, before being cited, which removed two papers whose content did not support the attribution and corrected the direction of the evidence attributed to several others. Figure A1 summarizes the flow.
Figure A1. Flow of the second survey: records retrieved from Lens, records judged eligible, papers included in the synthesis, and papers cited in this article. [FIGURE A1: insert the flow diagram, 886 → 226 (223 full texts) → 144 → 43]
A.3. Relation between the two lists
Table A1 lists the 43 mechanisms with their origin and the support each finds in the second survey. Of the 39 mechanisms of the first list, 16 correspond to a unit extracted in the second survey, 8 have partial support, meaning that papers from the survey inform their definitions without forming a unit of their own, and 15 have no support. The absence is concentrated in Blocks F and G, which the string does not reach, since its required terms name network and cognitive mechanisms. Three of the fifteen, the hostile media effect (C6), metric-driven content production (E3), and gatekeeping decline (G1), are among the mechanisms most directly tied to journalism. All fifteen remain in the taxonomy, because their absence reflects the scope of the search rather than evidence against them, and their sources were checked against the original works.
Table A1. Origin of each mechanism and its support in the second survey. Origin: first list (A.1) or second survey (A.2). Support: Yes, a unit extracted in the second survey corresponds to the mechanism. Partial, papers from the survey inform its definition without forming a unit of their own. No, no unit or paper from the survey addresses it. A dash marks mechanisms that originate in the second survey. Actors as in Table 5.
A.4. Use of generative AI and limitations of the procedure
Generative AI tools assisted every stage of the identification, always under human verification. Claude (Anthropic) assisted in the initial compilation of the first list, Gemini and Gemini Notebook (Google) in the screening and extraction of the second survey, and Claude, through Claude Code, in the consolidation of the extracted entries and in the verification of attributions against the papers. The authors take full responsibility for the result.
The procedure has four limitations. First, the string requires one of five known mechanisms, so it favors studies within the vocabulary of the first list (A.2). Second, because most records lacked abstracts, screening relied mainly on titles, and the records judged ineligible were not reassessed by the authors. Third, the inclusion criterion inherits the omissions of the extraction. Some eligible papers that no extracted mechanism cited deal directly with mechanisms of the list, such as studies of homophily and of echo chambers, and they were not reassessed. Fourth, the human check of coherence did not verify each attribution in the full text, which is why the papers cited in this article were checked individually (A.2). The outputs of the AI tools also depend on model versions and prompts, which limits exact reproduction [AUTHORS: model versions and prompts, if available].
```

---

## T03-A79 — Table A1: origem, suporte no segundo levantamento e atores

| Campo | Valor |
|---|---|
| Lote | 5 |
| Decisões | 5.2-b, 9.5-b; cruzamento final de 10.1 e 10.2 (16 sim, 8 parcial, 15 não) |
| Localização | Apêndice A, A.3, logo depois da legenda da Table A1 |
| Ação | inserir-tabela-apos |
| Estado | aplicado em 2026-10-18 |

```ancora
A dash marks mechanisms that originate in the second survey. Actors as in Table 5.
```

```tabela
| ID | Mechanism | Origin | Support in the second survey | Primary actor | Secondary actor |
| A1 | Filter bubble | First list | Yes | AS | OU |
| A2 | Algorithmic amplification | First list | Yes | AS | PL |
| A3 | Algorithmic radicalization | First list | Partial | AS | OU |
| A4 | Algorithmic agenda-setting | First list | No | AS | CA |
| B1 | Homophily | First list | Yes | OU | AS |
| B2 | Unfriending | Second survey | — | OU | — |
| B3 | Partisan sorting | First list | Yes | SG | OU |
| B4 | Interpersonal political tension | First list | No | OU | — |
| B5 | Echo chamber | First list | Yes | OU | SG |
| B6 | Group polarization | First list | Yes | OU | SG |
| B7 | Negative social influence | Second survey | — | OU | SG |
| B8 | Moral contagion | First list | Yes | OU | OA |
| B9 | Information cascades | First list | Partial | OU | CA |
| B10 | Online community radicalization | First list | Partial | SG | OA |
| C1 | Motivated reasoning | First list | Yes | OU | — |
| C2 | Confirmation bias | First list | Yes | OU | — |
| C3 | Selective avoidance | First list | Yes | OU | — |
| C4 | Biased assimilation | First list | Yes | OU | — |
| C5 | Backfire effect | Second survey | — | OU | PL |
| C6 | Hostile media effect | First list | No | OU | — |
| C7 | Illusory truth effect | First list | Yes | OU | — |
| C8 | News avoidance | First list | Partial | OU | — |
| C9 | Reinforcing spiral | First list | Yes | OU | AS |
| D1 | Vocal minority | First list | No | OU | — |
| D2 | Social proof | First list | No | OU | CA |
| D3 | False consensus | First list | Partial | OU | — |
| D4 | Pluralistic ignorance | First list | Partial | OU | SG |
| D5 | Spiral of silence | First list | Yes | OU | — |
| D6 | Exaggerated meta-perceptions | First list | Partial | OU | — |
| E1 | Social learning of outrage | First list | Yes | OU | PL |
| E2 | Identity signaling | First list | Yes | OU | SG |
| E3 | Metric-driven content production | First list | No | OA | PL |
| F1 | Online disinhibition effect | First list | No | OU | — |
| F2 | Dogpiling | First list | No | OU | — |
| F3 | Message brevity | First list | No | OU | — |
| F4 | Incivility contagion | First list | No | OU | — |
| F5 | Incivility exposure effect | First list | Partial | OU | — |
| G1 | Gatekeeping decline | First list | No | PL | OA |
| G2 | Propaganda feedback loop | First list | No | OA | OU |
| G3 | Manufactured consensus | First list | No | CA | OA |
| G4 | Platform migration | First list | No | PL | SG |
| G5 | Perceived censorship | First list | No | OU | OA |
| G6 | Partisan flagging | Second survey | — | OU | OA |
```

**Conversão** do cruzamento (IDs atuais → novos, 9.1): *sim* = A1, A2, B1, B2→B5, B3→B6, B5→B8,
B6→B3, C1, C2, C3, C4, C6→C7, C8→C9, D5, E1, E2 (16) · *parcial* = A3, B4→B9, B8→B10, C7→C8, D3,
D4, D6, F5 (8) · *não* = A4, B7→B4, C5→C6, D1, D2, E3, F1–F4, G1–G5 (15). Atores: como na tabela
consolidada (lote 3a).

---

## Lote 6, rodada 1 — Correção do Apêndice, contagens, tabelas e referências

**Convenções da rodada 1**:
- **6a**: correção do lote 5 (42 obras citadas, e não 43). A Figura A1 é regenerada com 42 e 102 e substituída à mão.
- **6b**: contagens "39", "41" e "forty-one" passam a 43, e as contagens por outcome da 9.1 seguem a tabela consolidada.
- **6c**: tabelas renumeradas (a consolidada passa a Tabela 6, a matriz das affordances a Tabela 7; a Tabela 5 é a de atores, do lote 1), nomes novos das colunas e a régua nova na 6.1 (em português).
- **6f**: as 42 referências novas entram como [120]–[161], e cada marcador [NEW: …] é trocado pelo número (`substituir-todas`, com o número de ocorrências conferido).
- **Rodada 2** (depois desta): IDs no texto antigo, ordem física das fichas do bloco B, subgrupos do bloco B e IDs nos parágrafos que citam os mecanismos novos só pelo nome.

---

## T03-A80 — Apêndice A, A.2: 42 obras citadas, e não 43

| Campo | Valor |
|---|---|
| Lote | 6 (6a) |
| Decisões | correção do lote 5 (regra 7): Ohme 2021 está no .bib, mas não é citado no texto |
| Localização | Apêndice A, A.2, último parágrafo |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
This article cites 43 of them. Each of these 43
```

```novo
This article cites 42 of them. Each of these 42
```

---

## T03-A81 — Abstract: 41 → 43

| Campo | Valor |
|---|---|
| Lote | 6 (6b) |
| Decisões | contagem (passo 8.6) |
| Localização | Abstract |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
We identify 41 individually
```

```novo
We identify 43 individually
```

---

## T03-A82 — Introdução: forty-one → forty-three

| Campo | Valor |
|---|---|
| Lote | 6 (6b) |
| Decisões | contagem; 9.6 (nota da Introdução) |
| Localização | Introdução |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
forty-one distinct mechanisms
```

```novo
forty-three distinct mechanisms
```

---

## T03-A83 — Tabela 2: 39 → 43

| Campo | Valor |
|---|---|
| Lote | 6 (6b) |
| Decisões | contagem |
| Localização | Tabela 2, linha Intermediate processes |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
39 mechanisms, each with an ID
```

```novo
43 mechanisms, each with an ID
```

---

## T03-A84 — 3.x: each of the 39 mechanisms → 43

| Campo | Valor |
|---|---|
| Lote | 6 (6b) |
| Decisões | contagem |
| Localização | Seção 3, comparação dos mecanismos |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
treats each of the 39 mechanisms as its own unit
```

```novo
treats each of the 43 mechanisms as its own unit
```

---

## T03-A85 — 5.1: 39 mechanisms in Table 5 → 43, Table 6

| Campo | Valor |
|---|---|
| Lote | 6 (6b) |
| Decisões | contagem; 9.5-c (tabelas) |
| Localização | Seção 5.1, fim do parágrafo sobre possibilidade |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
39 mechanisms in Table 4 5
```

```novo
43 mechanisms in Table 6
```

---

## T03-A86 — 7: all 39 individual mechanisms → 43

| Campo | Valor |
|---|---|
| Lote | 6 (6b) |
| Decisões | contagem |
| Localização | Seção 7, primeiro parágrafo |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
all 39 individual mechanisms
```

```novo
all 43 individual mechanisms
```

---

## T03-A87 — 9.3: the 39 mechanisms → 43

| Campo | Valor |
|---|---|
| Lote | 6 (6b) |
| Decisões | contagem |
| Localização | Seção 9.3, segunda limitação |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
the 39 mechanisms concentrates
```

```novo
the 43 mechanisms concentrates
```

---

## T03-A88 — Conclusões: 39 → 43

| Campo | Valor |
|---|---|
| Lote | 6 (6b) |
| Decisões | contagem |
| Localização | Seção 11, primeiro parágrafo |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
We identified 39 mechanisms
```

```novo
We identified 43 mechanisms
```

---

## T03-A89 — Seção 11: whether the 39 mechanisms → 43

| Campo | Valor |
|---|---|
| Lote | 6 (6b) |
| Decisões | contagem |
| Localização | Seção 11, Systematic test of coverage |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
whether the 39 mechanisms
```

```novo
whether the 43 mechanisms
```

---

## T03-A90 — 9.1: affective twenty-one → twenty-three

| Campo | Valor |
|---|---|
| Lote | 6 (6b) |
| Decisões | recontagem pela tabela consolidada (lote 3a) |
| Localização | Seção 9.1, parágrafo sobre perceived polarization |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
(twenty-one)
```

```novo
(twenty-three)
```

**Nota**: Recontagem nos 43: affective 23, ideological 19, perceived 13, structural 5, behavioral 4.

---

## T03-A91 — 9.1: ideological sixteen → nineteen

| Campo | Valor |
|---|---|
| Lote | 6 (6b) |
| Decisões | recontagem pela tabela consolidada (lote 3a) |
| Localização | Seção 9.1, parágrafo sobre perceived polarization |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
(sixteen)
```

```novo
(nineteen)
```

---

## T03-A92 — 6.1: maioria dos 39 → 43

| Campo | Valor |
|---|---|
| Lote | 6 (6b) |
| Decisões | contagem |
| Localização | Seção 6.1, parágrafo de Claim |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
dos 39 mecanismos foi classificada
```

```novo
dos 43 mecanismos foi classificada
```

---

## T03-A93 — Tabela 3: Table 5 → Table 6

| Campo | Valor |
|---|---|
| Lote | 6 (6c) |
| Decisões | 9.5-c |
| Localização | Tabela 3, linha Quality appraisal |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
for each mechanism (Table 5)
```

```novo
for each mechanism (Table 6)
```

---

## T03-A94 — Legenda da tabela consolidada: Table 5 → Table 6

| Campo | Valor |
|---|---|
| Lote | 6 (6c) |
| Decisões | 9.5-c |
| Localização | Seção 6.11, legenda |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
Table 4 5. Complete mechanism taxonomy
```

```novo
Table 6. Complete mechanism taxonomy
```

---

## T03-A95 — Seção 7: mappings detailed in Table 5 → 6

| Campo | Valor |
|---|---|
| Lote | 6 (6c) |
| Decisões | 9.5-c |
| Localização | Seção 7, primeiro parágrafo |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
mappings detailed in Table 4 5.
```

```novo
mappings detailed in Table 6.
```

---

## T03-A96 — 9.3: Evidence column in Table 5 → Evidence strength column in Table 6

| Campo | Valor |
|---|---|
| Lote | 6 (6c) |
| Decisões | 9.5-c; 2.4-c (nome da coluna) |
| Localização | Seção 9.3, terceira limitação |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
Evidence column in Table 4 5.
```

```novo
Evidence strength column in Table 6.
```

---

## T03-A97 — 3.x: interventions column that Table 6 → 7

| Campo | Valor |
|---|---|
| Lote | 6 (6c) |
| Decisões | 9.5-c |
| Localização | Seção 3, SPIR |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
interventions column that Table 6 (Section 8)
```

```novo
interventions column that Table 7 (Section 8)
```

---

## T03-A98 — 7.3: Table 6 → 7

| Campo | Valor |
|---|---|
| Lote | 6 (6c) |
| Decisões | 9.5-c |
| Localização | Seção 7.3, primeira frase |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
Table 6 (Section 8) outlines
```

```novo
Table 7 (Section 8) outlines
```

---

## T03-A99 — Seção 7: Table 6 synthesizes → 7

| Campo | Valor |
|---|---|
| Lote | 6 (6c) |
| Decisões | 9.5-c |
| Localização | Seção 7, antes da matriz |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
Table 5 6 synthesizes
```

```novo
Table 7 synthesizes
```

---

## T03-A100 — Legenda da matriz das affordances: Table 6 → Table 7

| Campo | Valor |
|---|---|
| Lote | 6 (6c) |
| Decisões | 9.5-c |
| Localização | Seção 8, legenda |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
Table 5 6. Complete affordance matrix.
```

```novo
Table 7.
```

**Nota**: O original inclui a legenda antiga, já riscada no lote 3a. Visível: "Table 7. Complete affordance matrix. Mechanism IDs…".

---

## T03-A101 — 10.2: interventions column in Table 6 → 7

| Campo | Valor |
|---|---|
| Lote | 6 (6c) |
| Decisões | 9.5-c |
| Localização | Seção 10.2, quarto item |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
Table 5 (Section 7.3) 6 (Section 8) serves
```

```novo
Table 7 (Section 8) serves
```

---

## T03-A102 — Seção 11: Table 6 (Section 8) shows → 7

| Campo | Valor |
|---|---|
| Lote | 6 (6c) |
| Decisões | 9.5-c |
| Localização | Seção 11, Intervention studies |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
Table 6 (Section 8) shows
```

```novo
Table 7 (Section 8) shows
```

---

## T03-A103 — Seção 11: affordance matrix in Table 6 → 7

| Campo | Valor |
|---|---|
| Lote | 6 (6c) |
| Decisões | 9.5-c |
| Localização | Seção 11, alternative platforms |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
affordance matrix in Table  6.
```

```novo
affordance matrix in Table 7.
```

---

## T03-A104 — 6.1: primeiro parágrafo com 43 mecanismos, Tabela 6 e os nomes novos das colunas

| Campo | Valor |
|---|---|
| Lote | 6 (6c) |
| Decisões | 2.4-a, 2.4-c, 9.5-c; contagem |
| Localização | Seção 6.1, primeiro parágrafo |
| Ação | substituir-paragrafo |
| Estado | aplicado em 2026-10-18 |

```original
Antes de apresentar os 41 mecanismos, cabe os 39 mecanismos, cabe explicitar a lógica usada para atribuir valor a cada uma das três colunas centrais da Tabela 5 (Seção 6.11): 'Outcome', 'Claim' e 'Evidence'. 'Outcome', 'Claim' e 'Evidence'. A origem de cada mecanismo, na primeira lista ou no segundo levantamento, e o suporte que ele encontra no segundo levantamento estão na Table A1 (Apêndice A).
```

```novo
Antes de apresentar os 43 mecanismos, cabe explicitar a lógica usada para atribuir valor às colunas centrais da Tabela 6 (Seção 6.11): Outcome, Platform role, Direction e Evidence strength. A origem de cada mecanismo, na primeira lista ou no segundo levantamento, e o suporte que ele encontra no segundo levantamento estão na Table A1 (Apêndice A).
```

**Nota**: Em português, como o resto da 6.1. Substitui o parágrafo inteiro porque ele já tinha três camadas de ajustes (41 → 39, a remissão do lote 5).

---

## T03-A105 — 6.1: Claim → Platform role

| Campo | Valor |
|---|---|
| Lote | 6 (6c) |
| Decisões | 2.4-c |
| Localização | Seção 6.1, início do parágrafo de Claim |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
Para 'Claim', cada mecanismo
```

```novo
Para Platform role, cada mecanismo
```

---

## T03-A106 — 6.1: parágrafo de Evidence com a régua nova e a coluna Direction

| Campo | Valor |
|---|---|
| Lote | 6 (6c) |
| Decisões | 2.1-e, 2.4-a, 2.4-b, 5.3-a; pendência aberta no lote 4 |
| Localização | Seção 6.1, parágrafo de Evidence |
| Ação | substituir-paragrafo |
| Estado | aplicado em 2026-10-18 |

```original
Para 'Evidence', a avaliação é qualitativa e reflete o tipo de desenho de pesquisa predominante na literatura identificada para cada mecanismo (Seção 4.3): evidência classificada como 'strong' corresponde a replicação experimental ou quase-experimental robusta; 'moderate', a estudos observacionais consistentes entre si; 'mixed', a achados conflitantes entre estudos; e 'plausible', a mecanismos teoricamente bem fundamentados mas com evidência direta ainda escassa ou indireta. Essa avaliação é necessariamente uma síntese qualitativa deste artigo, não uma metanálise formal, e deve ser lida como tal.
```

```novo
Para Evidence strength, a avaliação considera só a evidência sobre o papel da plataforma, isto é, estudos com dados de uso real de plataformas: experimentos de campo, quase-experimentos, dados de rastro ou de conteúdo e surveys sobre o uso de plataformas. Strong corresponde a evidência experimental ou quase-experimental em plataforma replicada por mais de um estudo, Moderate a um único experimento em plataforma ou a dados observacionais ou de survey consistentes, e Plausible a apoio vindo de simulações, de teoria ou de evidência do fenômeno fora das plataformas. A direção dessa evidência fica na coluna Direction: Reinforcing quando os estudos indicam que a plataforma aumenta o efeito do mecanismo, Mixed quando há achados em sentidos opostos ou achados nulos ao lado de positivos, e Attenuating quando indicam que ela o reduz. Essa avaliação é necessariamente uma síntese qualitativa deste artigo, não uma metanálise formal, e deve ser lida como tal.
```

**Nota**: Em português. Resolve a pendência aberta no lote 4 (escala antiga com 'mixed' como força). Sem aspas nos valores, pela regra de estilo.

---

## T03-A107 — Referências [120]–[161]: as 42 obras novas, no estilo MDPI

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | G1 (Crossref via DOI, references-T03-novas.bib); passo 8.6 |
| Localização | Lista de referências, depois de Nelson et al. [119] |
| Ação | inserir-apos |
| Estado | aplicado em 2026-10-18 |

```ancora
Remove User Commentary Functions? Journal. Media 2021, 2, 572–583.
```

```novo
Nordbrandt, M. Affective polarization in the digital age: Testing the direction of the relationship between social media and users’ feelings for out-group parties. New Media Soc. 2021, 25, 3392–3411.
Cho, J.; Ahmed, S.; Hilbert, M.; Liu, B.; Luu, J. Do Search Algorithms Endanger Democracy? An Experimental Investigation of Algorithm Effects on Political Polarization. J. Broadcast. Electron. Media 2020, 64, 150–172.
Liu, N.; Hu, X.E.; Savas, Y.; Baum, M.A.; Berinsky, A.J.; Chaney, A.J.B.; Lucas, C.; Mariman, R.; de Benedictis-Kessner, J.; Guess, A.M.; Knox, D.; Stewart, B.M. Short-term exposure to filter-bubble recommendation systems has limited polarization effects: Naturalistic experiments on YouTube. Proc. Natl. Acad. Sci. USA 2025, 122, e2318127122.
Törnberg, P. Echo chambers can emerge without algorithmic personalization or a preference for homogeneity. PLoS ONE 2026, 21, e0347207.
Ferraz de Arruda, H.; Andrade Oliveira, K.; Moreno, Y. Echo chamber formation sharpened by priority users. iScience 2024, 27, 111098.
Metzler, H.; Garcia, D. Social Drivers and Algorithmic Mechanisms on Digital Media. Perspect. Psychol. Sci. 2023, 19, 735–748.
Gu, Z.; Zhu, R.; Bian, F. Affective homophily as the dominant organizing principle in online conflict discourse networks. Sci. Rep. 2025, 15, 35542.
Tonin, M.; Lepri, B.; Tizzoni, M. Physical partisan proximity outweighs online ties in predicting US voting outcomes. PNAS Nexus 2025, 4, pgaf308.
Martel, C.; Mosleh, M.; Yang, Q.; Zaman, T.; Rand, D.G. Blocking of counter-partisan accounts drives political assortment on Twitter. PNAS Nexus 2024, 3, pgae161.
Kaiser, J.; Vaccari, C.; Chadwick, A. Partisan Blocking: Biased Responses to Shared Misinformation Contribute to Network Polarization on Social Media. J. Commun. 2022, 72, 214–240.
Sasahara, K.; Chen, W.; Peng, H.; Ciampaglia, G.L.; Flammini, A.; Menczer, F. Social influence and unfollowing accelerate the emergence of echo chambers. J. Comput. Soc. Sci. 2020, 4, 381–402.
Fletcher, R.; Robertson, C.T.; Nielsen, R.K. How Many People Live in Politically Partisan Online News Echo Chambers in Different Countries? J. Quant. Descr. Digit. Media 2021, 1.
Dubois, E.; Blank, G. The echo chamber is overstated: the moderating effect of political interest and diverse media. Inf. Commun. Soc. 2018, 21, 729–745.
Geiß, S.; Magin, M.; Jürgens, P.; Stark, B. Loopholes in the Echo Chambers: How the Echo Chamber Metaphor Oversimplifies the Effects of Information Gateways on Opinion Expression. Digit. Journal. 2021, 9, 660–686.
Sobeh, A.; Vakrat, T.M.; Shamay‐Tsoory, S. Interbrain Synchrony Mitigates Extremism Within Echo Chambers. Ann. N. Y. Acad. Sci. 2025, 1552, 117–128.
Mølmen, G.N.; Ravndal, J.A. Mechanisms of online radicalisation: how the internet affects the radicalisation of extreme-right lone actor terrorists. Behav. Sci. Terror. Political Aggress. 2021, 15, 463–487.
Axelrod, R.; Daymude, J.J.; Forrest, S. Preventing extreme polarization of political attitudes. Proc. Natl. Acad. Sci. USA 2021, 118, e2102139118.
Krueger, T.; Szwabiński, J.; Weron, T. Conformity, Anticonformity and Polarization of Opinions: Insights from a Mathematical Model of Opinion Dynamics. Entropy 2017, 19, 371.
Nettasinghe, B.; Percus, A.G.; Lerman, K. How out-group animosity can shape partisan divisions: A model of affective polarization. PNAS Nexus 2025, 4, pgaf082.
Thurner, S.; Hofer, M.; Korbel, J. Why more social interactions lead to more polarization in societies. Proc. Natl. Acad. Sci. USA 2025, 122, e2517530122.
Carpentras, D.; Maher, P.J.; O'Reilly, C.; Quayle, M. Deriving an Opinion Dynamics Model from Experimental Data. J. Artif. Soc. Soc. Simul. 2022, 25, 4.
Törnberg, P. Echo chambers and viral misinformation: Modeling fake news as complex contagion. PLoS ONE 2018, 13, e0203958.
Simchon, A.; Brady, W.J.; Van Bavel, J.J. Troll and divide: the language of online polarization. PNAS Nexus 2022, 1, pgac019.
Hasell, A.; Weeks, B.E. Partisan Provocation: The Role of Partisan News Use and Emotional Responses in Political Information Sharing in Social Media. Hum. Commun. Res. 2016, 42, 641–661.
Törnberg, P. How digital media drive affective polarization through partisan sorting. Proc. Natl. Acad. Sci. USA 2022, 119, e2207159119.
Baumann, F.; Lorenz-Spreen, P.; Sokolov, I.M.; Starnini, M. Emergence of Polarized Ideological Opinions in Multidimensional Topic Spaces. Phys. Rev. X 2021, 11, 011012.
Sultan, M.; Tump, A.N.; Ehmann, N.; Lorenz-Spreen, P.; Hertwig, R.; Gollwitzer, A.; Kurvers, R.H.J.M. Susceptibility to online misinformation: A systematic meta-analysis of demographic and psychological factors. Proc. Natl. Acad. Sci. USA 2024, 121, e2409329121.
Sobkowicz, P. Opinion Dynamics Model Based on Cognitive Biases of Complex Agents. J. Artif. Soc. Soc. Simul. 2018, 21, 8.
Masip, P.; Suau, J.; Ruiz-Caballero, C. Incidental Exposure to Non-Like-Minded News through Social Media: Opposing Voices in Echo-Chambers’ News Feeds. Media Commun. 2020, 8, 53–62.
Sikder, O.; Smith, R.E.; Vivo, P.; Livan, G. A minimalistic model of bias, polarization and misinformation in social networks. Sci. Rep. 2020, 10, 5493.
Karlsen, R.; Steen-Johnsen, K.; Wollebæk, D.; Enjolras, B. Echo chamber and trench warfare dynamics in online debates. Eur. J. Commun. 2017, 32, 257–273.
Kim, J.; Wang, Z.; Shi, H.; Ling, H.-K.; Evans, J. Differential impact from individual versus collective misinformation tagging on the diversity of Twitter (X) information engagement and mobility. Nat. Commun. 2025, 16, 973.
Zarouali, B.; Makhortykh, M.; Bastian, M.; Araujo, T. Overcoming polarization with chatbot news? Investigating the impact of news content containing opposing views on agreement and credibility. Eur. J. Commun. 2020, 36, 53–68.
Nordbrandt, M. Affective polarization in crosscutting communication networks: Offline and online evidence from Spain. Front. Political Sci. 2022, 4, 921188.
Secară, E.-C.; Opre, N.-A. Impact of Repeated Exposure to Polarized Health-Related News on Explicit and Implicit Attitudes Toward Dietary Supplements: Online Experimental Study. JMIR Infodemiology 2026, 6, e88632.
Brown, G.D.A.; Lewandowsky, S.; Huang, Z. Social sampling and expressed attitudes: Authenticity preference and social extremeness aversion lead to social norm effects and polarization. Psychol. Rev. 2022, 129, 18–48.
You, Z.T.; Lee, S.W.S. Explanations of and interventions against affective polarization cannot afford to ignore the power of ingroup norm perception. PNAS Nexus 2024, 3, pgae286.
Banisch, S.; Gaisbauer, F.; Olbrich, E. Modelling Spirals of Silence and Echo Chambers by Learning from the Feedback of Others. Entropy 2022, 24, 1484.
Konovalova, E.; Le Mens, G.; Schöll, N. Social media feedback and extreme opinion expression. PLoS ONE 2023, 18, e0293805.
Garz, M.; Sörensen, J.; Stone, D.F. Partisan selective engagement: Evidence from Facebook. J. Econ. Behav. Organ. 2020, 177, 91–108.
Westermann, C.J.; Coscia, M. A potential mechanism for low tolerance feedback loops in social media flagging systems. PLoS ONE 2022, 17, e0268270.
Kobellarz, J.K.; Brocic, M.; Silver, D.; Silva, T.H. Bubble reachers and uncivil discourse in polarized online public sphere. PLoS ONE 2024, 19, e0304564.
```

**Nota**: Numeração pela ordem da primeira citação no texto, a partir de [120], como a T02 fez com [115]–[119]. Metadados do Crossref pelo DOI de cada entrada do .bib. Abreviações dos periódicos pelo ISO 4 **[conferir]**. Ohme 2021 fica fora: está no .bib, mas não é citado (C9 não tem ficha, B02).

---

## T03-A108 — Citação Nordbrandt 2021 → [120]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 2 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: Nordbrandt 2021]
```

```novo
[120]
```

---

## T03-A109 — Citação Cho et al. 2020 → [121]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 1 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: Cho et al. 2020]
```

```novo
[121]
```

---

## T03-A110 — Citação Liu et al. 2025 → [122]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 4 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: Liu et al. 2025]
```

```novo
[122]
```

---

## T03-A111 — Citação Törnberg 2026 → [123]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 6 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: Törnberg 2026]
```

```novo
[123]
```

---

## T03-A112 — Citação Arruda et al. 2024 → [124]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 2 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: Arruda et al. 2024]
```

```novo
[124]
```

---

## T03-A113 — Citação Metzler and García 2023 → [125]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 1 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: Metzler and García 2023]
```

```novo
[125]
```

---

## T03-A114 — Citação Gu et al. 2025 → [126]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 1 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: Gu et al. 2025]
```

```novo
[126]
```

---

## T03-A115 — Citação Tonin et al. 2025 → [127]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 2 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: Tonin et al. 2025]
```

```novo
[127]
```

---

## T03-A116 — Citação Martel et al. 2024 → [128]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 4 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: Martel et al. 2024]
```

```novo
[128]
```

---

## T03-A117 — Citação Kaiser et al. 2022 → [129]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 1 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: Kaiser et al. 2022]
```

```novo
[129]
```

---

## T03-A118 — Citação Sasahara et al. 2020 → [130]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 1 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: Sasahara et al. 2020]
```

```novo
[130]
```

---

## T03-A119 — Citação Fletcher et al. 2021 → [131]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 4 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: Fletcher et al. 2021]
```

```novo
[131]
```

---

## T03-A120 — Citação Dubois and Blank 2018 → [132]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 1 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: Dubois and Blank 2018]
```

```novo
[132]
```

---

## T03-A121 — Citação Geiß et al. 2021 → [133]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 3 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: Geiß et al. 2021]
```

```novo
[133]
```

---

## T03-A122 — Citação Sobeh et al. 2025 → [134]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 1 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: Sobeh et al. 2025]
```

```novo
[134]
```

---

## T03-A123 — Citação Mølmen and Ravndal 2021 → [135]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 2 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: Mølmen and Ravndal 2021]
```

```novo
[135]
```

---

## T03-A124 — Citação Axelrod et al. 2021 → [136]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 1 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: Axelrod et al. 2021]
```

```novo
[136]
```

---

## T03-A125 — Citação Krueger et al. 2017 → [137]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 2 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: Krueger et al. 2017]
```

```novo
[137]
```

---

## T03-A126 — Citação Nettasinghe et al. 2025 → [138]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 2 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: Nettasinghe et al. 2025]
```

```novo
[138]
```

---

## T03-A127 — Citação Thurner et al. 2025 → [139]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 2 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: Thurner et al. 2025]
```

```novo
[139]
```

---

## T03-A128 — Citação Carpentras et al. 2022 → [140]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 1 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: Carpentras et al. 2022]
```

```novo
[140]
```

---

## T03-A129 — Citação Törnberg 2018 → [141]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 1 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: Törnberg 2018]
```

```novo
[141]
```

---

## T03-A130 — Citação Simchon et al. 2022 → [142]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 1 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: Simchon et al. 2022]
```

```novo
[142]
```

---

## T03-A131 — Citação Hasell and Weeks 2016 → [143]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 2 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: Hasell and Weeks 2016]
```

```novo
[143]
```

---

## T03-A132 — Citação Törnberg 2022 → [144]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 2 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: Törnberg 2022]
```

```novo
[144]
```

---

## T03-A133 — Citação Baumann et al. 2021 → [145]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 1 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: Baumann et al. 2021]
```

```novo
[145]
```

---

## T03-A134 — Citação Sultan et al. 2024 → [146]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 1 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: Sultan et al. 2024]
```

```novo
[146]
```

---

## T03-A135 — Citação Sobkowicz 2018 → [147]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 1 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: Sobkowicz 2018]
```

```novo
[147]
```

---

## T03-A136 — Citação Masip et al. 2020 → [148]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 4 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: Masip et al. 2020]
```

```novo
[148]
```

---

## T03-A137 — Citação Sikder et al. 2020 → [149]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 1 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: Sikder et al. 2020]
```

```novo
[149]
```

---

## T03-A138 — Citação Karlsen et al. 2017 → [150]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 1 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: Karlsen et al. 2017]
```

```novo
[150]
```

---

## T03-A139 — Citação Kim et al. 2025 → [151]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 2 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: Kim et al. 2025]
```

```novo
[151]
```

---

## T03-A140 — Citação Zarouali et al. 2020 → [152]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 1 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: Zarouali et al. 2020]
```

```novo
[152]
```

---

## T03-A141 — Citação Nordbrandt 2022 → [153]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 1 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: Nordbrandt 2022]
```

```novo
[153]
```

---

## T03-A142 — Citação Secară and Opre 2026 → [154]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 1 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: Secară and Opre 2026]
```

```novo
[154]
```

---

## T03-A143 — Citação Brown et al. 2022 → [155]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 1 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: Brown et al. 2022]
```

```novo
[155]
```

---

## T03-A144 — Citação You and Lee 2024 → [156]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 2 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: You and Lee 2024]
```

```novo
[156]
```

---

## T03-A145 — Citação Banisch et al. 2022 → [157]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 1 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: Banisch et al. 2022]
```

```novo
[157]
```

---

## T03-A146 — Citação Konovalova et al. 2023 → [158]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 2 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: Konovalova et al. 2023]
```

```novo
[158]
```

---

## T03-A147 — Citação Garz et al. 2020 → [159]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 2 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: Garz et al. 2020]
```

```novo
[159]
```

---

## T03-A148 — Citação Westermann and Coscia 2022 → [160]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 3 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: Westermann and Coscia 2022]
```

```novo
[160]
```

---

## T03-A149 — Citação Martel et al. 2024; Kaiser et al. 2022 → [128,129]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 1 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: Martel et al. 2024; Kaiser et al. 2022]
```

```novo
[128,129]
```

---

## T03-A150 — Citação Krueger et al. 2017; Carpentras et al. 2022 → [137,140]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 1 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: Krueger et al. 2017; Carpentras et al. 2022]
```

```novo
[137,140]
```

---

## T03-A151 — Citação Karlsen et al. 2017; Kim et al. 2025 → [150,151]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 1 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: Karlsen et al. 2017; Kim et al. 2025]
```

```novo
[150,151]
```

---

## T03-A152 — Citação Kobellarz et al. 2024 → [161]

| Campo | Valor |
|---|---|
| Lote | 6 (6f) |
| Decisões | passo 8.6 (numeração das referências novas) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 1 |
| Estado | aplicado em 2026-10-18 |

```original
[NEW: Kobellarz et al. 2024]
```

```novo
[161]
```

---

## Lote 6, rodada 2 — IDs no texto antigo, ordem do bloco B e subgrupos

**Convenções da rodada 2**:
- **6g**: o espaço que faltou na legenda da Tabela 7 (rodada 1).
- **6d**: os IDs atuais que mudam (B2–B8, C5–C8) passam aos novos (relatório 9.1) no texto que ainda usa a numeração atual. Cada trecho foi escolhido para ser único no texto bruto, que inclui o texto riscado. Os nomes dos mecanismos novos citados sem ID (lotes 2 e 3b) ganham o ID.
- **6e**: as fichas de Partisan sorting e Interpersonal political tension mudam de lugar (riscadas na posição antiga e reinseridas, com o rótulo novo, logo depois de Unfriending), e a abertura do bloco anuncia os três subgrupos.
- **Ordem de aplicação**: a da numeração (6g, 6d, 6e). Em 6e, B4 entra antes de B3, porque as duas ficam logo depois da mesma âncora.

---

## T03-A153 — Legenda da Tabela 7: espaço depois de "Table 7."

| Campo | Valor |
|---|---|
| Lote | 6 (6g) |
| Decisões | correção da rodada 1: o espaço que separava o texto novo herdou o risco do texto anterior |
| Localização | Seção 8, legenda da Tabela 7 |
| Ação | inserir-inline |
| Estado | aplicado em 2026-10-18 |

```ancora
Complete affordance matrix. Table 7.
```

```novo
 
```

**Nota**: Insere um espaço, em verde, logo depois de "Table 7." (ação nova `inserir-inline`, 2026-10-18).

---

## T03-A154 — ID: 5.1

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | 5.1 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
B7 (Interpersonal political tension), two mechanisms that arise
```

```novo
B4 (Interpersonal political tension), two mechanisms that arise
```

---

## T03-A155 — ID: 5.2, segundo fechamento do loop

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | 5.2, segundo fechamento do loop |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
moral contagion (B5, Section 6.4)
```

```novo
moral contagion (B8, Section 6.4)
```

---

## T03-A156 — ID: A1

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | A1 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
Unlike the echo chamber (B2)
```

```novo
Unlike the echo chamber (B5)
```

---

## T03-A157 — ID: A2

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | A2 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
[125]. It differs from moral contagion (B5)
```

```novo
[125]. It differs from moral contagion (B8)
```

---

## T03-A158 — ID: A3

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | A3 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
the community radicalization pathway (B8)
```

```novo
the community radicalization pathway (B10)
```

---

## T03-A159 — ID: Echo chamber, rótulo

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | Echo chamber, rótulo |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
B2. Echo chamber.
```

```novo
B5. Echo chamber.
```

---

## T03-A160 — ID: Echo chamber, remissão

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | Echo chamber, remissão |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
and from group polarization (B3), which concerns the shift of positions after discussion among like-minded people. In repeated
```

```novo
and from group polarization (B6), which concerns the shift of positions after discussion among like-minded people. In repeated
```

---

## T03-A161 — ID: Group polarization, rótulo

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | Group polarization, rótulo |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
B3. Group polarization.
```

```novo
B6. Group polarization.
```

---

## T03-A162 — ID: Information cascades, rótulo

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | Information cascades, rótulo |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
B4. Information cascades.
```

```novo
B9. Information cascades.
```

---

## T03-A163 — ID: Moral contagion, rótulo

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | Moral contagion, rótulo |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
B5. Moral contagion.
```

```novo
B8. Moral contagion.
```

---

## T03-A164 — ID: Online community radicalization, rótulo

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | Online community radicalization, rótulo |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
B8. Online community radicalization.
```

```novo
B10. Online community radicalization.
```

---

## T03-A165 — ID: C3

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | C3 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
feed the network separation described by the echo chamber (B2).
```

```novo
feed the network separation described by the echo chamber (B5).
```

---

## T03-A166 — ID: Hostile media effect, rótulo

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | Hostile media effect, rótulo |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
C5. Hostile media effect
```

```novo
C6. Hostile media effect
```

---

## T03-A167 — ID: Illusory truth effect, rótulo

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | Illusory truth effect, rótulo |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
C6. Illusory truth effect
```

```novo
C7. Illusory truth effect
```

---

## T03-A168 — ID: Illusory truth effect, remissão

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | Illusory truth effect, remissão |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
reshares, cascades (B4), and repeated
```

```novo
reshares, cascades (B9), and repeated
```

---

## T03-A169 — ID: News avoidance, rótulo

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | News avoidance, rótulo |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
C7. News avoidance.
```

```novo
C8. News avoidance.
```

---

## T03-A170 — ID: Bloco D

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | Bloco D |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
is treated as information cascades (B4).
```

```novo
is treated as information cascades (B9).
```

---

## T03-A171 — ID: Bloco D

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | Bloco D |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
and echo chambers (B2) surround
```

```novo
and echo chambers (B5) surround
```

---

## T03-A172 — ID: E1

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | E1 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
[158]. It concerns the authors who learn from feedback, whereas moral contagion (B5) concerns the users
```

```novo
[158]. It concerns the authors who learn from feedback, whereas moral contagion (B8) concerns the users
```

---

## T03-A173 — ID: G3

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | G3 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
and information cascades (B4). Its effects
```

```novo
and information cascades (B9). Its effects
```

---

## T03-A174 — ID: 7.1, Why AF1

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | 7.1, Why AF1 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The links to C6 (Illusory truth effect) and B5 (Moral contagion)
```

```novo
The links to C7 (Illusory truth effect) and B8 (Moral contagion)
```

---

## T03-A175 — ID: 7.1, Why AF1

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | 7.1, Why AF1 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
(feeding C6) and cumulative exposure to moralized content (feeding B5)
```

```novo
(feeding C7) and cumulative exposure to moralized content (feeding B8)
```

---

## T03-A176 — ID: 7.1, Why AF1

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | 7.1, Why AF1 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The links to C7 (News avoidance) and C3
```

```novo
The links to C8 (News avoidance) and C3
```

---

## T03-A177 — ID: 7.1, Why AF1

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | 7.1, Why AF1 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
Its social channel is the echo chamber (B2)
```

```novo
Its social channel is the echo chamber (B5)
```

---

## T03-A178 — ID: 7.1, Why AF1

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | 7.1, Why AF1 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The link to C8 (Reinforcing spiral)
```

```novo
The link to C9 (Reinforcing spiral)
```

---

## T03-A179 — ID: 7.1, Why AF2

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | 7.1, Why AF2 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The indirect link to B2 (Echo chamber)
```

```novo
The indirect link to B5 (Echo chamber)
```

---

## T03-A180 — ID: 7.1, Why AF2

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | 7.1, Why AF2 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The links to B3 (Group polarization), D3
```

```novo
The links to B6 (Group polarization), D3
```

---

## T03-A181 — ID: 7.1, AF3

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | 7.1, AF3 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
Interpersonal political tension (B7) helps explain
```

```novo
Interpersonal political tension (B4) helps explain
```

---

## T03-A182 — ID: 7.1, Why AF3

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | 7.1, Why AF3 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The indirect links to B2 (Echo chamber), B3 (Group polarization)
```

```novo
The indirect links to B5 (Echo chamber), B6 (Group polarization)
```

---

## T03-A183 — ID: 7.1, Why AF3

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | 7.1, Why AF3 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The link to B7 (Interpersonal political tension), also
```

```novo
The link to B4 (Interpersonal political tension), also
```

---

## T03-A184 — ID: 7.1, AF4, lista

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | 7.1, AF4, lista |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
Information cascades (B4) and Interpersonal political tension (B7, indirect)
```

```novo
Information cascades (B9) and Interpersonal political tension (B4, indirect)
```

---

## T03-A185 — ID: 7.1, Why AF4

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | 7.1, Why AF4 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The link to B4 (Information cascades) follows
```

```novo
The link to B9 (Information cascades) follows
```

---

## T03-A186 — ID: 7.1, Why AF4

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | 7.1, Why AF4 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
indirect link to B7 (Interpersonal political tension)
```

```novo
indirect link to B4 (Interpersonal political tension)
```

---

## T03-A187 — ID: 7.1, AF5, lista

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | 7.1, AF5, lista |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
Information cascades (B4). Block D
```

```novo
Information cascades (B9). Block D
```

---

## T03-A188 — ID: 7.1, Why AF5

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | 7.1, Why AF5 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The link to B4 (Information cascades) is the most
```

```novo
The link to B9 (Information cascades) is the most
```

---

## T03-A189 — ID: 7.1, Why AF5

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | 7.1, Why AF5 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
Since B4 also covers
```

```novo
Since B9 also covers
```

---

## T03-A190 — ID: 7.1, Why AF6

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | 7.1, Why AF6 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
the link to B7 (Interpersonal political tension) follows directly
```

```novo
the link to B4 (Interpersonal political tension) follows directly
```

---

## T03-A191 — ID: 7.1, AF9, lista

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | 7.1, AF9, lista |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
Moral contagion (B5). Block C (Individual selection and processing of information): Illusory truth effect (C6) and News avoidance (C7).
```

```novo
Moral contagion (B8). Block C (Individual selection and processing of information): Illusory truth effect (C7) and News avoidance (C8).
```

---

## T03-A192 — ID: 7.1, Why AF9

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | 7.1, Why AF9 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
feeding the illusory truth effect (C6)
```

```novo
feeding the illusory truth effect (C7)
```

---

## T03-A193 — ID: 7.1, Why AF9

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | 7.1, Why AF9 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
feeding moral contagion (B5) [Brady et al., 67]. The link to C7 (News avoidance)
```

```novo
feeding moral contagion (B8) [Brady et al., 67]. The link to C8 (News avoidance)
```

---

## T03-A194 — ID: 7.1, Why AF11

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | 7.1, Why AF11 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The link to B6 (Partisan sorting)
```

```novo
The link to B3 (Partisan sorting)
```

---

## T03-A195 — ID: 7.1, Why AF11

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | 7.1, Why AF11 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
The link to B8 (Online community radicalization)
```

```novo
The link to B10 (Online community radicalization)
```

---

## T03-A196 — ID: 9.1

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | 9.1 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
Information cascades (B4), Interpersonal political tension (B7), Illusory truth effect (C6),
```

```novo
Information cascades (B9), Interpersonal political tension (B4), Illusory truth effect (C7),
```

---

## T03-A197 — ID: 9.1

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | 9.1 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
B6 (partisan sorting), as public identity
```

```novo
B3 (partisan sorting), as public identity
```

---

## T03-A198 — ID: 9.3

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | 9.3 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
Mechanism B7 (Interpersonal political tension), for
```

```novo
Mechanism B4 (Interpersonal political tension), for
```

---

## T03-A199 — ID: 9.3

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | 9.3 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
Consequently, B7 should be interpreted
```

```novo
Consequently, B4 should be interpreted
```

---

## T03-A200 — ID: 9.3

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | 9.3 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
feeds Interpersonal political tension (B7),
```

```novo
feeds Interpersonal political tension (B4),
```

---

## T03-A201 — ID: 10.2

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | 10.2 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
B5 (moral contagion) and C8 (reinforcing spiral) were detailed
```

```novo
B8 (moral contagion) and C9 (reinforcing spiral) were detailed
```

---

## T03-A202 — ID: 10.2

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | 10.2 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
News avoidance (C7) and Selective avoidance (C3) (Section
```

```novo
News avoidance (C8) and Selective avoidance (C3) (Section
```

---

## T03-A203 — ID: 10.2

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | 4.2 (a); correspondência de IDs (relatório 9.1) |
| Localização | 10.2 |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
general news avoidance (C7) and selective
```

```novo
general news avoidance (C8) and selective
```

---

## T03-A204 — ID nos mecanismos novos: unfriending (Section 6.4)

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | convenção dos lotes 2 e 3b (o lote 6 acrescenta os IDs) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 6 |
| Estado | aplicado em 2026-10-18 |

```original
unfriending (Section 6.4)
```

```novo
unfriending (B2, Section 6.4)
```

---

## T03-A205 — ID nos mecanismos novos: negative social influence (Section 6.4)

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | convenção dos lotes 2 e 3b (o lote 6 acrescenta os IDs) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 3 |
| Estado | aplicado em 2026-10-18 |

```original
negative social influence (Section 6.4)
```

```novo
negative social influence (B7, Section 6.4)
```

---

## T03-A206 — ID nos mecanismos novos: the backfire effect (Section 6.5)

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | convenção dos lotes 2 e 3b (o lote 6 acrescenta os IDs) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 4 |
| Estado | aplicado em 2026-10-18 |

```original
the backfire effect (Section 6.5)
```

```novo
the backfire effect (C5, Section 6.5)
```

---

## T03-A207 — ID nos mecanismos novos: Partisan flagging (Section 6.9)

| Campo | Valor |
|---|---|
| Lote | 6 (6d) |
| Decisões | convenção dos lotes 2 e 3b (o lote 6 acrescenta os IDs) |
| Localização | todas as ocorrências |
| Ação | substituir-todas |
| Ocorrências | 1 |
| Estado | aplicado em 2026-10-18 |

```original
Partisan flagging (Section 6.9)
```

```novo
Partisan flagging (G6, Section 6.9)
```

---

## T03-A208 — Bloco B: ficha atual de Partisan sorting sai da posição antiga

| Campo | Valor |
|---|---|
| Lote | 6 (6e) |
| Decisões | 4.1-b, 4.2 (a): ordem lógica por subgrupo |
| Localização | Seção 6.4, ficha B6 atual |
| Ação | remover |
| Estado | aplicado em 2026-10-18 |

```original
B6. Partisan sorting (alt. partisan-ideological sorting). The alignment of partisan and ideological identities, through which each party becomes a more homogeneous social group [62]. Mason [62] found that this alignment strengthens partisan identity and increases partisan bias, activism, and anger even when issue positions do not polarize to the same degree. Platforms can make the alignment more visible, since profiles, communities, and shared content bundle political and cultural cues (AF11), although direct evidence of this amplification is limited. The mechanism acts on affective polarization: the other party comes to be seen as a distinct social group rather than as people who disagree on some issues. A model proposes a specific route: digital media bring people to interact outside their local networks, and these interactions align previously cross-cutting differences into two increasingly homogeneous camps [NEW: Törnberg 2022] [144]. Alignment can extend to issue positions, and in a model of opinion dynamics across several topics, correlations between extreme positions emerged from social interaction without being assumed in individual preferences [NEW: Baumann et al. 2021] [145]. The mechanism acts on affective polarization: the other party comes to be seen as a distinct social group rather than as people who disagree on some issues.
```

**Nota**: A ficha volta logo depois de Unfriending como B3 (ajuste seguinte da ordem: tension primeiro, depois sorting, ambos ancorados no fim de Unfriending).

---

## T03-A209 — Bloco B: ficha atual de Interpersonal political tension sai da posição antiga

| Campo | Valor |
|---|---|
| Lote | 6 (6e) |
| Decisões | 4.1-b, 4.2 (a) |
| Localização | Seção 6.4, ficha B7 atual |
| Ação | remover |
| Estado | aplicado em 2026-10-18 |

```original
B7. Interpersonal political tension. The strain that visible political disagreement places on existing relationships, which in turn raises the salience of political identity [5]. Tanyel and Windeler [5] proposed and tested this sequence with a survey of 2,820 Facebook and Twitter users and a second survey of 492 users: tension around differences in values triggers an us-versus-them awareness that leads to more positive attitudes toward the in-group and more negative attitudes toward the out-group. On social media, the low segmentation of audiences (AF6) keeps the political views of friends, relatives, and colleagues visible and recurrent, and asymmetric following (AF3) shapes which disagreeing ties stay in view. The mechanism acts on affective polarization. It differs from homophily (B1), which concerns which ties are formed, because here the disagreeing ties already exist and are kept.
```

---

## T03-A210 — Bloco B: B4. Interpersonal political tension, logo depois de Unfriending

| Campo | Valor |
|---|---|
| Lote | 6 (6e) |
| Decisões | 4.1-b, 4.2 (a) |
| Localização | Seção 6.4, depois de B2 (Unfriending) |
| Ação | inserir-apos |
| Estado | aplicado em 2026-10-18 |

```ancora
which concerns content rather than ties.
```

```novo
B4. Interpersonal political tension. The strain that visible political disagreement places on existing relationships, which in turn raises the salience of political identity [5]. Tanyel and Windeler [5] proposed and tested this sequence with a survey of 2,820 Facebook and Twitter users and a second survey of 492 users: tension around differences in values triggers an us-versus-them awareness that leads to more positive attitudes toward the in-group and more negative attitudes toward the out-group. On social media, the low segmentation of audiences (AF6) keeps the political views of friends, relatives, and colleagues visible and recurrent, and asymmetric following (AF3) shapes which disagreeing ties stay in view. The mechanism acts on affective polarization. It differs from homophily (B1), which concerns which ties are formed, because here the disagreeing ties already exist and are kept.
```

**Nota**: Texto idêntico ao da ficha atual, só com o rótulo novo.

---

## T03-A211 — Bloco B: B3. Partisan sorting, logo depois de Unfriending

| Campo | Valor |
|---|---|
| Lote | 6 (6e) |
| Decisões | 4.1-b, 4.2 (a) |
| Localização | Seção 6.4, depois de B2 (Unfriending), antes de B4 |
| Ação | inserir-apos |
| Estado | aplicado em 2026-10-18 |

```ancora
which concerns content rather than ties.
```

```novo
B3. Partisan sorting (alt. partisan-ideological sorting). The alignment of partisan and ideological identities, through which each party becomes a more homogeneous social group [62]. Mason [62] found that this alignment strengthens partisan identity and increases partisan bias, activism, and anger even when issue positions do not polarize to the same degree. Platforms can make the alignment more visible, since profiles, communities, and shared content bundle political and cultural cues (AF11), although direct evidence of this amplification is limited. A model proposes a specific route: digital media bring people to interact outside their local networks, and these interactions align previously cross-cutting differences into two increasingly homogeneous camps [144]. Alignment can extend to issue positions, and in a model of opinion dynamics across several topics, correlations between extreme positions emerged from social interaction without being assumed in individual preferences [145]. The mechanism acts on affective polarization: the other party comes to be seen as a distinct social group rather than as people who disagree on some issues.
```

**Nota**: Texto idêntico ao da ficha atual, só com o rótulo novo. Entra logo depois da âncora, e por isso fica antes de B4.

---

## T03-A212 — Bloco B: abertura anuncia os três subgrupos

| Campo | Valor |
|---|---|
| Lote | 6 (6e) |
| Decisões | 4.1-b |
| Localização | Seção 6.4, parágrafo de abertura, última frase |
| Ação | substituir |
| Estado | aplicado em 2026-10-18 |

```original
where the process takes place in the individual's own choice or judgment of information.
```

```novo
where the process takes place in the individual's own choice or judgment of information. The block has three subgroups: tie selection, which concerns who connects to whom (B1, B2), group identity, which concerns how identities align and gain salience (B3, B4), and influence and diffusion, which concerns how opinions and content change and travel through ties (B5 to B10).
```

---

## Lote 6, rodada 3 — Ordem de B8 e B9

**Motivo**: na releitura da rodada 2, a ficha B9 (*Information cascades*, antes B4) ainda vinha antes de B8
(*Moral contagion*, antes B5). A numeração nova inverte as duas, e a rodada 2 não tratou essa troca.

---

## T03-A213 — Bloco B: ficha de Information cascades sai da posição antiga

| Campo | Valor |
|---|---|
| Lote | 6 (6e) |
| Decisões | 4.2 (a): ordem lógica; correção da rodada 2 |
| Localização | Seção 6.4, ficha B9 (Information cascades), entre B7 e B8 |
| Ação | remover |
| Estado | proposto |

```original
B4. Information cascades. B9. Information cascades. The spread of content through chains of sharing in which each user passes information on because others have already shared it, rather than after an independent check of its accuracy. Sharing takes a single action and share counts are visible (AF4, AF5), so cascades can reach large audiences quickly, and false content travels as easily as true content. Vosoughi et al. [51] found that false news on Twitter diffused significantly farther, faster, deeper, and more broadly than true news, with the strongest effects for false political news. On Facebook, Del Vicario et al. [52] found that selective exposure drives diffusion within homogeneous clusters, each with its own cascade dynamics. The cascades of misinformation described here, false content shared without intent to deceive, differ from disinformation spread deliberately by coordinated actors, which is treated as manufactured consensus (G3). By circulating unverified claims within like-minded clusters, the mechanism acts on ideological and perceived polarization. By circulating unverified claims within like-minded clusters, the mechanism acts on ideological and perceived polarization. In a network simulation, clusters polarized in both opinion and network structure helped misinformation spread as a complex contagion, acting as its initial bandwagon [NEW: Törnberg 2018] [141].
```

**Nota**: a ficha volta logo depois de B8 (ajuste seguinte), com o mesmo texto.

---

## T03-A214 — Bloco B: B9. Information cascades, logo depois de B8

| Campo | Valor |
|---|---|
| Lote | 6 (6e) |
| Decisões | 4.2 (a); correção da rodada 2 |
| Localização | Seção 6.4, depois da ficha B8 (Moral contagion), antes de B10 |
| Ação | inserir-apos |
| Estado | proposto |

```ancora
[143]. It is the preference that engagement-based ranking learns and amplifies (A2), and it differs from the social learning of outrage (E1), which concerns the authors rewarded for expressing it.
```

```novo
B9. Information cascades. The spread of content through chains of sharing in which each user passes information on because others have already shared it, rather than after an independent check of its accuracy. Sharing takes a single action and share counts are visible (AF4, AF5), so cascades can reach large audiences quickly, and false content travels as easily as true content. Vosoughi et al. [51] found that false news on Twitter diffused significantly farther, faster, deeper, and more broadly than true news, with the strongest effects for false political news. On Facebook, Del Vicario et al. [52] found that selective exposure drives diffusion within homogeneous clusters, each with its own cascade dynamics. The cascades of misinformation described here, false content shared without intent to deceive, differ from disinformation spread deliberately by coordinated actors, which is treated as manufactured consensus (G3). By circulating unverified claims within like-minded clusters, the mechanism acts on ideological and perceived polarization. In a network simulation, clusters polarized in both opinion and network structure helped misinformation spread as a complex contagion, acting as its initial bandwagon [141].
```

**Nota**: texto idêntico ao da ficha atual (já com o rótulo B9 da rodada 2).

---

## Log de aplicação

| Data | Documento | Aplicados | Pulados | Revisão antes | Revisão depois |
|---|---|---|---|---|---|
| 2026-10-18 21:23 | `13O5Uco9-ItlpHioS_M_tsUr8UbqxppoQ2bx1fBmQ00g` | T03-A1, T03-A2, T03-A3, T03-A4, T03-A6, T03-A7, T03-A8, T03-A9 | — | `AHj4eMShT32I1cLp7gm9PoZ-W6jt6RwKplS0F7IsLdP7OgxgKVvyio6r3RWqG4_JfZFD28zoatypd-wdKiQ0dpD71RcDqYvMKhI0sO1vaTiC1AI` | `AHj4eMQGMzxGRYEKvhgl-yjX9xxO5I8XKQQd4TB9FB8yuOFSgZxVi1DFw1WBSf0vO96mtCbE4-CQy6QXSGpDwEprJytwYpixQ5elWaH90VLW7m4` |
| 2026-10-18 21:43 | `13O5Uco9-ItlpHioS_M_tsUr8UbqxppoQ2bx1fBmQ00g` | T03-A12, T03-A13, T03-A14, T03-A10, T03-A11, T03-A15, T03-A16, T03-A17, T03-A18, T03-A19, T03-A20, T03-A21, T03-A22, T03-A23, T03-A24, T03-A25, T03-A26, T03-A27, T03-A28, T03-A29, T03-A30, T03-A31, T03-A32, T03-A33, T03-A34, T03-A35, T03-A36, T03-A37, T03-A38, T03-A39 | — | `AHj4eMQsFITcAusRTlxrYgZNo08UvU08-ZyYSdmJmAOyjDn7EjNrgPYz7PLr0xaAEHmD9kgPAWNGVWp2GFi71aMS6C-aoOo-lyflMJAoDktSIPI` | `AHj4eMTMtkgYhQkQeygCTBf86BiMQRTJBtlqxdg5J5BMtD9zy0JjnlLcG2rBMNY7pyH2QW2T58W3AWH3p0KqKqC1UR3c1_xPU8hwqBZSzNbEqn0` |
| 2026-10-18 21:56 | `13O5Uco9-ItlpHioS_M_tsUr8UbqxppoQ2bx1fBmQ00g` | T03-A40, T03-A41, T03-A42, T03-A43 | — | `AHj4eMTMtkgYhQkQeygCTBf86BiMQRTJBtlqxdg5J5BMtD9zy0JjnlLcG2rBMNY7pyH2QW2T58W3AWH3p0KqKqC1UR3c1_xPU8hwqBZSzNbEqn0` | `AHj4eMRbEqDV5nwvvv-FcZykXWZT4ALK-HjEheCUgGDYdQ_t2mco_jlf6zgZOJaYMxDMY3lY_FNavLjh2hoe97FrSYNPDwqSNswj2CPbDcaMiL4` |
| 2026-10-18 22:08 | `13O5Uco9-ItlpHioS_M_tsUr8UbqxppoQ2bx1fBmQ00g` | T03-A44, T03-A45, T03-A46, T03-A47, T03-A48, T03-A49, T03-A50, T03-A51, T03-A52, T03-A53, T03-A54, T03-A55, T03-A56, T03-A57 | — | `AHj4eMSm2uDX7KBXYjTxOqd2h4oG4i5MzLtoXG_zEwRXz4No5v9_kNT8kFhXBWb2jgulQEIBZH0ZF-TqbLmvjnAIA3P98qdWNfeHj_C77p19R2s` | `AHj4eMQxHBEBpEx-SnjQDCoXqHqcXcsDErdg0iH5rMa1OhZEFRiIGgkK0W4BjZ50btrQftZoWNWK4FTc-33wAKp68BOGZph5ViJ-ZoR-NeL5Qo0` |
| 2026-10-18 22:23 | `13O5Uco9-ItlpHioS_M_tsUr8UbqxppoQ2bx1fBmQ00g` | T03-A58, T03-A59, T03-A60, T03-A61, T03-A62, T03-A63, T03-A64, T03-A65, T03-A66, T03-A67, T03-A68, T03-A69, T03-A70, T03-A71 | — | `AHj4eMQxHBEBpEx-SnjQDCoXqHqcXcsDErdg0iH5rMa1OhZEFRiIGgkK0W4BjZ50btrQftZoWNWK4FTc-33wAKp68BOGZph5ViJ-ZoR-NeL5Qo0` | `AHj4eMQ1Kjn_Fn5L-xc5_nnVd0DF-p5eWers75fgloT56JXtGX1OGcoK-do9P_MVddeejm3VWALdqrvKICqysA96N1VwVv-3rqKA3x_mQADIDBg` |
| 2026-10-18 22:33 | `13O5Uco9-ItlpHioS_M_tsUr8UbqxppoQ2bx1fBmQ00g` | T03-A72, T03-A73, T03-A74, T03-A75, T03-A76, T03-A77, T03-A78, T03-A79 | — | `AHj4eMQ1Kjn_Fn5L-xc5_nnVd0DF-p5eWers75fgloT56JXtGX1OGcoK-do9P_MVddeejm3VWALdqrvKICqysA96N1VwVv-3rqKA3x_mQADIDBg` | `AHj4eMTSk8_oGAd3x_2wGlGLJW0hCoysebQ00lbg8Ajez1033xDxT3BMLeAx8yeoAbVzhO7BGnCBTQmJa78TfSKwDNP1O4ID9xC1DAy6yu33heM` |
| 2026-10-18 23:00 | `13O5Uco9-ItlpHioS_M_tsUr8UbqxppoQ2bx1fBmQ00g` | T03-A80, T03-A81, T03-A82, T03-A83, T03-A84, T03-A85, T03-A86, T03-A87, T03-A88, T03-A89, T03-A90, T03-A91, T03-A92, T03-A93, T03-A94, T03-A95, T03-A96, T03-A97, T03-A98, T03-A99, T03-A100, T03-A101, T03-A102, T03-A103, T03-A104, T03-A105, T03-A106, T03-A107, T03-A108, T03-A109, T03-A110, T03-A111, T03-A112, T03-A113, T03-A114, T03-A115, T03-A116, T03-A117, T03-A118, T03-A119, T03-A120, T03-A121, T03-A122, T03-A123, T03-A124, T03-A125, T03-A126, T03-A127, T03-A128, T03-A129, T03-A130, T03-A131, T03-A132, T03-A133, T03-A134, T03-A135, T03-A136, T03-A137, T03-A138, T03-A139, T03-A140, T03-A141, T03-A142, T03-A143, T03-A144, T03-A145, T03-A146, T03-A147, T03-A148, T03-A149, T03-A150, T03-A151, T03-A152 | — | `AHj4eMRgDKeZlNI4Pn9faPS3W6AyYs7QzrNUVbmmWd1hByKr24FmxaEs85knm_i9yvHE3GS4CdMDi-f1eGCAtFXFjuyLrAFsNnenwkZPP_g2WsA` | `AHj4eMRGL52qgHYCRvrmgWsQx6AL6PQvrniSe6m1hAy3caVob-XpikEOrKejKrsMMwg7onrfMCVJKhjLfTmeeA0wKrcA-RBrHggnPw8jX4Yp6gE` |
| 2026-10-18 23:15 | `13O5Uco9-ItlpHioS_M_tsUr8UbqxppoQ2bx1fBmQ00g` | T03-A153, T03-A154, T03-A155, T03-A156, T03-A157, T03-A158, T03-A159, T03-A160, T03-A161, T03-A162, T03-A163, T03-A164, T03-A165, T03-A166, T03-A167, T03-A168, T03-A169, T03-A170, T03-A171, T03-A172, T03-A173, T03-A174, T03-A175, T03-A176, T03-A177, T03-A178, T03-A179, T03-A180, T03-A181, T03-A182, T03-A183, T03-A184, T03-A185, T03-A186, T03-A187, T03-A188, T03-A189, T03-A190, T03-A191, T03-A192, T03-A193, T03-A194, T03-A195, T03-A196, T03-A197, T03-A198, T03-A199, T03-A200, T03-A201, T03-A202, T03-A203, T03-A204, T03-A205, T03-A206, T03-A207, T03-A208, T03-A209, T03-A210, T03-A211, T03-A212 | — | `AHj4eMRGL52qgHYCRvrmgWsQx6AL6PQvrniSe6m1hAy3caVob-XpikEOrKejKrsMMwg7onrfMCVJKhjLfTmeeA0wKrcA-RBrHggnPw8jX4Yp6gE` | `AHj4eMTdj3TYQoX2eG2n7kkIniiF9QXVigfQfx4GWIPp3Vw0F-aDp5jP0AflQ3KcJfoxbzT7xppucpu4bm3NTnldx-QJb3_xynulSmQLRAQ2hrA` |
