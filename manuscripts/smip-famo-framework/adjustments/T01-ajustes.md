# Ajustes T01 — Justificativa metodológica

- **Manuscrito**: smip-famo-framework · **Versão de referência**: `paper/v1-2026-10-08.pdf`
- **Relatório**: [`reviews/T01-justificativa-metodologica.md`](../reviews/T01-justificativa-metodologica.md) (decisões na Seção 9)
- **Destino**: cópia de revisão em Google Docs (ID em `context.md`)
- **Marcação**: texto substituído fica riscado; novo texto em preto com marca-texto amarelo.
- **Aplicação**: `uv run python -m scripts.gdocs_apply apply <doc> manuscripts/smip-famo-framework/adjustments/T01-ajustes.md --ids A6,A3,A5,A1` (simulação; `--apply` grava)

## Lotes

| Lote | Ajustes | Estado |
|---|---|---|
| 1 | A6, A3, A5, A1 | **aplicado** em 2026-10-10; A6 e A5 revisados (A6v2, A5v2) no mesmo dia |
| 1b | A16, A17 (F12, PRISMA de [3]) | **aplicado** em 2026-10-10 |
| 2 | A13, A14 | a redigir |
| 3 | A7, A4, A8 | a redigir |
| 4 | A2, A9, A11 (rótulo) | a redigir |
| — | A10, A11 (iteração) | bloqueados (T01-D2) |
| — | A12, A15 | retirados → `backlog.md` B01 |

**Nota sobre o lote 1**: A6 e A5 citam a "Table 3" (tabela de diferenciação), que só entra
no lote 3, junto da renumeração das tabelas atuais (A8). Até lá, o documento terá duas
referências a "Table 3" com sentidos diferentes.

---

## T01-A6 — Seção 4.1: objetivo → tipo de revisão → critérios; desvio declarado

| Campo | Valor |
|---|---|
| Lote | 1 |
| Achados | T01-F01, F02, F03, F04, F05, F08 |
| Decisões | D1a, D1b, D1c, D-overlap |
| Localização | Seção 4.1 (Methodological Positioning), parágrafo 1 (único), começa com "This article does not conduct a new systematic review of the literature." |
| Ação | substituir-paragrafo |
| Estado | aplicado em 2026-10-10 (lote 1); revisado em 2026-10-10 (T01-A6v2) |

**Texto original**

```original
This article does not conduct a new systematic review of the literature. This choice is deliberate, and three reasons support it. First, the stated objective of this work — the conceptual integration and refinement of a causal structure, not the systematic and exhaustive aggregation of empirical evidence — corresponds to what Paré et al. [15] classify as a theoretical review, a review category with its own objectives and standards of rigor, distinct from the systematic review. SPIR itself [2], published without a systematic search protocol, without a selection flow diagram, and without a reported article count, exemplifies that this genre is recognized and accepted within the same disciplinary conversation this article aims to join. Second, and more fundamentally: a rigorous systematic review of this exact domain has already been conducted twice recently, by Arora et al. [3], covering 264 articles, and by Tölle and Trier [4], covering 58 articles with considerable corpus overlap. Reproducing that effort now would be redundant, not more rigorous; the intended contribution here is not a new sweep of the same corpus, but a conceptual reorganization that builds on the outcome of those reviews and refines it at specific points that neither, by its very nature as an aggregated synthesis, was positioned to resolve. Third, the literature identification process actually employed is described transparently in Section 4.3, and its limitations are discussed explicitly in Section 9.2, rather than left implicit.
```

**Novo texto**

```novo
This article does not conduct a new systematic review of the literature, and the reason lies in its objective rather than in a relaxation of rigor. The goal of this work is explanation building: to identify, define, and relate the constructs of the framework (features, affordances, mechanisms, and outcomes) and to derive testable hypotheses from their relationships, not to aggregate empirical evidence on the direction or size of a delimited effect. As previously introduced, in the typology of Paré et al. [15], this objective corresponds to a theoretical review, whose primary goal is "to develop a conceptual framework or model with a set of research propositions or hypotheses" (p. 188). Systematic reviews, by contrast, rely on comprehensive searches and explicit selection over a delimited body of studies, whose evidence they then aggregate or integrate. The same authors caution against confusing the rigor of a review with its exhaustiveness, and against judging different review types by the same criteria. What each type owes its readers is internal consistency between objective and method, and a clear account of the steps actually taken [15].

Accordingly, this article follows the theoretical review type with one explicitly declared deviation from its ideal profile, which Paré et al. [15] describe as relying on a comprehensive search. Here, the search is directed rather than comprehensive. Because the unit of analysis of the framework is the individual mechanism or affordance, the search targeted the source that defines each item, through citation chaining from four anchor works (Section 4.3), rather than a census of studies on social media and polarization. The breadth of that literature has already been systematically mapped by two recent reviews, by Arora et al. [3], covering 264 articles, and by Tölle and Trier [4], covering 58 articles. This article builds on that breadth and adds item-level definitional depth, refining the structure of the field at specific points that neither review, bounded by the corpus its own search retrieved, was positioned to resolve. Table 3 summarizes how this approach differs from a systematic review along the dimensions proposed by Paré et al. [15]. The literature identification process is described in Section 4.3, and its limitations are discussed in Section 9.2.
```

**Justificativa**: o parágrafo inteiro muda porque a lógica muda. As três razões em
sequência dão lugar a um argumento só: o objetivo define o tipo de revisão, e o tipo
define os critérios de qualidade. O texto novo:
- tira o SPIR como precedente (F01, F02);
- assume o desvio na busca em vez de atribuí-lo a Paré (F03; Paré pp. 184, 186);
- restringe a redundância à amplitude empírica (F05);
- remove "considerable corpus overlap" (F04);
- troca "described transparently" por "described", porque a documentação da 4.3 ainda
  está pendente (A10).

A citação literal confere com Paré p. 188. "Rigor × exaustividade" e "mesmos critérios"
vêm da p. 192–193.

---

## T01-A3 — Introdução: nota metodológica alinhada à 4.1

| Campo | Valor |
|---|---|
| Lote | 1 |
| Achados | T01-F01, F02, F03, F08 |
| Decisões | D1a |
| Localização | Introdução, parágrafo 8, começa com "A methodological note is warranted at this point." — da 2ª frase até o fim do parágrafo |
| Ação | substituir |
| Estado | aplicado em 2026-10-10 (lote 1) |

**Texto original**

```original
This article does not conduct a new systematic literature review; this choice is deliberate and is justified in Section 4, after the related work is presented in Section 3. The approach follows what Paré et al. [15] classify as a theoretical review, a category distinct from the systematic review employed by Arora et al. [3] and Tölle and Trier [4].
```

**Novo texto**

```novo
This article does not conduct a new systematic literature review. Because its objective is to build and refine a theoretical structure rather than to aggregate evidence on a delimited effect, it is conducted as what Paré et al. [15] classify as a theoretical review, a review type whose objectives and quality criteria differ from those of the systematic reviews conducted by Arora et al. [3] and Tölle and Trier [4]. Section 4 develops this choice, declares where the approach departs from the ideal profile of a theoretical review, and describes the literature identification process.
```

**Justificativa**: antecipa na Introdução a mesma linha da 4.1 (objetivo → tipo →
critérios). Também anuncia o desvio declarado, para que o leitor não descubra a busca
não exaustiva só na 9.2 (F08). A primeira frase do parágrafo ("A methodological note…")
fica como está.

---

## T01-A5 — Seção 3.4, "Base methodology": diferença de objetivo, não de rigor

| Campo | Valor |
|---|---|
| Lote | 1 |
| Achados | T01-F03, F08 |
| Decisões | D1a |
| Localização | Seção 3.4, último parágrafo, começa com "Base methodology." — a frase após o rótulo em negrito |
| Ação | substituir |
| Estado | aplicado em 2026-10-10 (lote 1); revisado em 2026-10-10 (T01-A5v2) |

**Texto original**

```original
Unlike Arora et al. [3] and Tölle and Trier [4], who employ systematic review following the PRISMA protocol, the framework proposed in this article follows what Paré et al. [15] classify as a theoretical review — a methodological choice justified in detail in Section 4.1.
```

**Novo texto**

```novo
Arora et al. [3] and Tölle and Trier [4] conduct systematic reviews based on structured searches, explicit selection criteria, and a documented selection flow, which Tölle and Trier [4] report according to the PRISMA guidelines. The framework proposed in this article pursues a different objective, the construction of a theoretical structure, and therefore follows what Paré et al. [15] classify as a theoretical review. The difference lies in objective and quality criteria, not in a relaxation of rigor. Section 4.1 develops this distinction, and Table 3 summarizes it.
```

**Justificativa**: a frase atual apresenta a diferença só como "eles fazem PRISMA, nós não".
A nova versão diz o que cada desenho busca, o que tira da comparação a leitura de "menos
rigor" (F03, F08). O rótulo "Base methodology." em negrito fica como está.

---

## T01-A1 — Abstract: declarar a abordagem

| Campo | Valor |
|---|---|
| Lote | 1 |
| Achados | T01-F09 |
| Decisões | D-simples |
| Localização | Abstract, logo após a frase que termina em "incorporating contextual moderators and an explicit feedback loop." |
| Ação | inserir-apos |
| Estado | aplicado em 2026-10-10 (lote 1) |

**Texto original** (âncora)

```original
incorporating contextual moderators and an explicit feedback loop.
```

**Novo texto**

```novo
Methodologically, the article is a theoretical review built through citation chaining from four anchor works.
```

**Justificativa**: Paré recomenda declarar o tipo de revisão no título ou no Abstract
(p. 191). Com 15 palavras, o Abstract vai de 184 para 199 palavras. O limite da
*Journalism and Media* parece ser de cerca de 200 palavras **[a verificar]**.

## T01-A16 — Seção 3.2: método de Arora et al. [3] sem PRISMA

| Campo | Valor |
|---|---|
| Lote | 1b (F12) |
| Achados | T01-F12 |
| Decisões | aprovado pelo usuário em 2026-10-10 |
| Localização | Seção 3.2 (Arora et al.'s Systematic Review), parágrafo 1, primeira frase, começa com "Arora et al. [3] conduct a systematic review following PRISMA guidelines" |
| Ação | substituir |
| Estado | aplicado em 2026-10-10 |

**Texto original**

```original
Arora et al. [3] conduct a systematic review following PRISMA guidelines, selecting 264 articles from three databases (ABI/Inform, EBSCO, Web of Science).
```

**Novo texto**

```novo
Arora et al. [3] conduct a systematic review of three databases (ABI/Inform, EBSCO, Web of Science), selecting 264 articles through a documented selection process that also included ancestry mapping of the references of the selected studies.
```

**Justificativa**: [3] não menciona PRISMA. Descreve "a systematic identification
process", um fluxograma de seleção próprio (Fig. 1) e *ancestry mapping* ("references of
selected documents are checked for finding other relevant articles"), que respondeu por
21 dos 264 artigos ([3], p. 3). As bases e o total conferem com o original.

---

## T01-A17 — Tabela 2: célula de Arora et al. [3] sem PRISMA

| Campo | Valor |
|---|---|
| Lote | 1b (F12) |
| Achados | T01-F12 |
| Decisões | aprovado pelo usuário em 2026-10-10 |
| Localização | Tabela 2, linha "Base methodology", coluna "Arora et al. [3]" |
| Ação | substituir |
| Estado | aplicado em 2026-10-10 |

**Texto original**

```original
PRISMA systematic review, 264 articles
```

**Novo texto**

```novo
Systematic review, 264 articles
```

**Justificativa**: mesma razão de A16. A célula de Tölle e Trier [4] ("PRISMA systematic
review, 58 articles") está correta e não muda ([4], p. 4).

---

---

## Revisões de texto já inserido

Trocas feitas diretamente sobre o texto destacado (proposta ainda não incorporada), sem
riscar. Ver "Política de ajustes" em `manuscripts/CLAUDE.md`.

## T01-A6v2 — Revisão de A6: sem travessão e ponto e vírgula, PRISMA corrigido

| Campo | Valor |
|---|---|
| Lote | 1 (revisão) |
| Motivo | Edição humana no documento preservada ("As previously introduced, in the typology…"); premissa de estilo (sem — e ;); leitura de [3] e [4]: Arora et al. [3] não declaram PRISMA; o corpus de [3] é delimitado pela busca (exclui, p. ex., McPherson et al. [37]) e não só empírico |
| Localização | Seção 4.1, os dois parágrafos destacados inseridos por T01-A6 (trocados juntos) |
| Ação | revisar-insercao |
| Estado | aplicado em 2026-10-10 |

**Texto original** (v1, inserido em 2026-10-10)

```original
This article does not conduct a new systematic review of the literature, and the reason lies in its objective rather than in a relaxation of rigor. The goal of this work is explanation building: to identify, define, and relate constructs — features, affordances, mechanisms, and outcomes — and to derive testable hypotheses from their relationships, not to aggregate empirical evidence on the direction or size of a delimited effect. As previously introduced, in the typology of Paré et al. [15], this objective corresponds to a theoretical review, whose primary goal is "to develop a conceptual framework or model with a set of research propositions or hypotheses" (p. 188); systematic reviews, by contrast, aggregate or integrate evidence around narrow questions. The same authors caution against confusing the rigor of a review with its exhaustiveness, and against judging different review types by the same criteria: what each type owes its readers is internal consistency between objective and method, and a clear account of the steps actually taken [15].

Accordingly, this article follows the theoretical review type with one explicitly declared deviation from its ideal profile, which Paré et al. [15] describe as relying on a comprehensive search: here, the search is directed rather than comprehensive. Because the unit of analysis of the framework is the individual mechanism or affordance, the search targeted the source that defines each item, through citation chaining from four anchor works (Section 4.3), rather than a census of empirical studies on social media and polarization. The empirical breadth of the field has already been systematically mapped by two recent PRISMA-based reviews, by Arora et al. [3], covering 264 articles, and by Tölle and Trier [4], covering 58 articles. This article builds on that breadth and adds item-level definitional depth, refining the structure of the field at specific points that neither review, as an aggregated synthesis, was positioned to resolve. Table 3 summarizes how this approach differs from a systematic review along the dimensions proposed by Paré et al. [15]; the literature identification process is described in Section 4.3, and its limitations are discussed in Section 9.2.
```

**Novo texto**

```novo
This article does not conduct a new systematic review of the literature, and the reason lies in its objective rather than in a relaxation of rigor. The goal of this work is explanation building: to identify, define, and relate the constructs of the framework (features, affordances, mechanisms, and outcomes) and to derive testable hypotheses from their relationships, not to aggregate empirical evidence on the direction or size of a delimited effect. As previously introduced, in the typology of Paré et al. [15], this objective corresponds to a theoretical review, whose primary goal is "to develop a conceptual framework or model with a set of research propositions or hypotheses" (p. 188). Systematic reviews, by contrast, rely on comprehensive searches and explicit selection over a delimited body of studies, whose evidence they then aggregate or integrate. The same authors caution against confusing the rigor of a review with its exhaustiveness, and against judging different review types by the same criteria. What each type owes its readers is internal consistency between objective and method, and a clear account of the steps actually taken [15].

Accordingly, this article follows the theoretical review type with one explicitly declared deviation from its ideal profile, which Paré et al. [15] describe as relying on a comprehensive search. Here, the search is directed rather than comprehensive. Because the unit of analysis of the framework is the individual mechanism or affordance, the search targeted the source that defines each item, through citation chaining from four anchor works (Section 4.3), rather than a census of studies on social media and polarization. The breadth of that literature has already been systematically mapped by two recent reviews, by Arora et al. [3], covering 264 articles, and by Tölle and Trier [4], covering 58 articles. This article builds on that breadth and adds item-level definitional depth, refining the structure of the field at specific points that neither review, bounded by the corpus its own search retrieved, was positioned to resolve. Table 3 summarizes how this approach differs from a systematic review along the dimensions proposed by Paré et al. [15]. The literature identification process is described in Section 4.3, and its limitations are discussed in Section 9.2.
```

## T01-A5v2 — Revisão de A5: PRISMA só para Tölle e Trier, sem ponto e vírgula

| Campo | Valor |
|---|---|
| Lote | 1 (revisão) |
| Motivo | Arora et al. [3] não declaram PRISMA (verificado no PDF); premissa de estilo (sem ;) |
| Localização | Seção 3.4, "Base methodology.", frase destacada inserida por T01-A5 |
| Ação | revisar-insercao |
| Estado | aplicado em 2026-10-10 |

**Texto original** (v1)

```original
Arora et al. [3] and Tölle and Trier [4] employ systematic reviews following the PRISMA protocol, a design oriented to the comprehensive identification and synthesis of a body of studies. The framework proposed in this article pursues a different objective, the construction of a theoretical structure, and therefore follows what Paré et al. [15] classify as a theoretical review. The difference lies in objective and quality criteria, not in a relaxation of rigor; Section 4.1 develops this distinction, and Table 3 summarizes it.
```

**Novo texto**

```novo
Arora et al. [3] and Tölle and Trier [4] conduct systematic reviews based on structured searches, explicit selection criteria, and a documented selection flow, which Tölle and Trier [4] report according to the PRISMA guidelines. The framework proposed in this article pursues a different objective, the construction of a theoretical structure, and therefore follows what Paré et al. [15] classify as a theoretical review. The difference lies in objective and quality criteria, not in a relaxation of rigor. Section 4.1 develops this distinction, and Table 3 summarizes it.
```

## Log de aplicação

| Data | Documento | Aplicados | Pulados | Revisão antes | Revisão depois |
|---|---|---|---|---|---|
| 2026-10-10 11:20 | `13O5Uco9-ItlpHioS_M_tsUr8UbqxppoQ2bx1fBmQ00g` | T01-A6, T01-A3, T01-A5, T01-A1 | — | `AHj4eMQ9wf7l6Q2m_ZVSivmfxg23sKiv9KcIQry1stnxu9MPI5pgfiVVlwTkfkcvievzihbiq5QR_z2a5vlGVK3fuEZXItsAkbrQObyjZ064_u0` | `AHj4eMTTF0khdOen6ip2PRfxSnWYJ6ga5URX_v3nk4n73Ks-DGIXfHlylKQ9Z7_8kRDQ5gJpIgvtXt8J2BGOjuNikk_PFjg6B2LNyRS2iyBg7xk` |
| 2026-10-10 14:51 | `13O5Uco9-ItlpHioS_M_tsUr8UbqxppoQ2bx1fBmQ00g` | T01-A6v2, T01-A5v2 | — | `AHj4eMSCH5Pzf_VTyMBlZ3XjiOlRWD_OlqdTPohvIZPaHO6wAvU45sHPt4dltWz5qQi_nfzg-9TGurizKg_3FfJaU2UWfGVuXT6qfcoy6RvhWnY` | `AHj4eMRY_btVvB5Z-JV-E-9_yHGU2m8xSIwOXA2uObIe7j8I0LbpCfOLyDG2KXn1kZiVRde1lUX_tmugyhZ4wdnWnRRv6Z97i9ZuxOWv3K3lVzs` |
| 2026-10-10 15:01 | `13O5Uco9-ItlpHioS_M_tsUr8UbqxppoQ2bx1fBmQ00g` | T01-A16, T01-A17 | — | `AHj4eMRY_btVvB5Z-JV-E-9_yHGU2m8xSIwOXA2uObIe7j8I0LbpCfOLyDG2KXn1kZiVRde1lUX_tmugyhZ4wdnWnRRv6Z97i9ZuxOWv3K3lVzs` | `AHj4eMT-SjvGNehyv4m0dt3UQR1pcE_LM-MtWDCAJEIs6gnVoaiNgZ4FccX8VxFiIXp3vtVUcj6BHRFEb7MWYXwEMsm3YsLqzo_KUoKv_cFDO1k` |
