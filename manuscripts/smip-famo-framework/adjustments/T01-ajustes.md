# Ajustes T01 — Justificativa metodológica

- **Manuscrito**: smip-famo-framework · **Versão de referência**: `paper/v1-2026-10-08.pdf`
- **Relatório**: [`reviews/T01-justificativa-metodologica.md`](../reviews/T01-justificativa-metodologica.md) (decisões na Seção 9)
- **Destino**: cópia de revisão em Google Docs (ID em `context.md`)
- **Marcação**: texto substituído fica riscado; novo texto em preto com marca-texto amarelo.
- **Aplicação**: `uv run python -m scripts.gdocs_apply apply <doc> manuscripts/smip-famo-framework/adjustments/T01-ajustes.md --ids A6,A3,A5,A1` (simulação; `--apply` grava)

## Lotes

| Lote | Ajustes | Estado |
|---|---|---|
| 1 | A6, A3, A5, A1 | redigido, aguardando revisão do usuário |
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
| Estado | planejado |

**Texto original**

```original
This article does not conduct a new systematic review of the literature. This choice is deliberate, and three reasons support it. First, the stated objective of this work — the conceptual integration and refinement of a causal structure, not the systematic and exhaustive aggregation of empirical evidence — corresponds to what Paré et al. [15] classify as a theoretical review, a review category with its own objectives and standards of rigor, distinct from the systematic review. SPIR itself [2], published without a systematic search protocol, without a selection flow diagram, and without a reported article count, exemplifies that this genre is recognized and accepted within the same disciplinary conversation this article aims to join. Second, and more fundamentally: a rigorous systematic review of this exact domain has already been conducted twice recently, by Arora et al. [3], covering 264 articles, and by Tölle and Trier [4], covering 58 articles with considerable corpus overlap. Reproducing that effort now would be redundant, not more rigorous; the intended contribution here is not a new sweep of the same corpus, but a conceptual reorganization that builds on the outcome of those reviews and refines it at specific points that neither, by its very nature as an aggregated synthesis, was positioned to resolve. Third, the literature identification process actually employed is described transparently in Section 4.3, and its limitations are discussed explicitly in Section 9.2, rather than left implicit.
```

**Novo texto**

```novo
This article does not conduct a new systematic review of the literature, and the reason lies in its objective rather than in a relaxation of rigor. The goal of this work is explanation building: to identify, define, and relate constructs — features, affordances, mechanisms, and outcomes — and to derive testable hypotheses from their relationships, not to aggregate empirical evidence on the direction or size of a delimited effect. In the typology of Paré et al. [15], this objective corresponds to a theoretical review, whose primary goal is "to develop a conceptual framework or model with a set of research propositions or hypotheses" (p. 188); systematic reviews, by contrast, aggregate or integrate evidence around narrow questions. The same authors caution against confusing the rigor of a review with its exhaustiveness, and against judging different review types by the same criteria: what each type owes its readers is internal consistency between objective and method, and a clear account of the steps actually taken [15].

Accordingly, this article follows the theoretical review type with one explicitly declared deviation from its ideal profile, which Paré et al. [15] describe as relying on a comprehensive search: here, the search is directed rather than comprehensive. Because the unit of analysis of the framework is the individual mechanism or affordance, the search targeted the source that defines each item, through citation chaining from four anchor works (Section 4.3), rather than a census of empirical studies on social media and polarization. The empirical breadth of the field has already been systematically mapped by two recent PRISMA-based reviews, by Arora et al. [3], covering 264 articles, and by Tölle and Trier [4], covering 58 articles. This article builds on that breadth and adds item-level definitional depth, refining the structure of the field at specific points that neither review, as an aggregated synthesis, was positioned to resolve. Table 3 summarizes how this approach differs from a systematic review along the dimensions proposed by Paré et al. [15]; the literature identification process is described in Section 4.3, and its limitations are discussed in Section 9.2.
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
| Estado | planejado |

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
| Estado | planejado |

**Texto original**

```original
Unlike Arora et al. [3] and Tölle and Trier [4], who employ systematic review following the PRISMA protocol, the framework proposed in this article follows what Paré et al. [15] classify as a theoretical review — a methodological choice justified in detail in Section 4.1.
```

**Novo texto**

```novo
Arora et al. [3] and Tölle and Trier [4] employ systematic reviews following the PRISMA protocol, a design oriented to the comprehensive identification and synthesis of a body of studies. The framework proposed in this article pursues a different objective, the construction of a theoretical structure, and therefore follows what Paré et al. [15] classify as a theoretical review. The difference lies in objective and quality criteria, not in a relaxation of rigor; Section 4.1 develops this distinction, and Table 3 summarizes it.
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
| Estado | planejado |

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
