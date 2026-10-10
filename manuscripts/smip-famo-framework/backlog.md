# Backlog — smip-famo-framework

Ideias e propostas **adiadas** por decisão do usuário: não entram em nenhuma tarefa até
serem retomadas. Diferem das pendências do `INDEX.md`, que são itens [a verificar] de
tarefas em curso. Ao retomar um item, ele vira tarefa (ou subtarefa) no `INDEX.md`.

| ID | Item | Origem | Estado | Depende de |
|---|---|---|---|---|
| B01 | Supplementary Table S1 — trilha de auditoria | T01 (A12, A15) | **Adiado: o usuário ainda decide se entra no paper** | T01-D2; verificação de referências; PDFs de [4] e [5] |

---

## B01 — Supplementary Table S1: trilha de auditoria

**Registrado em**: 2026-10-09 · **Relatório de origem**: `reviews/T01-justificativa-metodologica.md`
(achado T01-F07; Seções 4.4 e 9)

### Problema que resolveria
A Seção 4.3 afirma "directed and auditable coverage", mas não demonstra como o
*citation chaining* chegou a cada mecanismo e affordance. A afirmação fica sem prova.

### O que já existe no paper e o que seria novo
- **De onde vem cada item** (item → fonte definidora): **já existe** na prosa das Seções 6–7
  e na coluna "Ref" da Tabela 4. Tabular só isso seria quase redundante; corrigir a
  numeração da coluna "Ref" (que diverge da lista; ex.: M1 → [39] = Ross 1977) resolve
  essa parte mais barato.
- **Como cada fonte foi encontrada** (âncora de origem, direção, passo): **não existe**.
  É o único valor novo da S1. Sem essa coluna, a S1 não vale a pena.

### Como preencher a coluna "como foi encontrada"
1. **Registro dos autores** (anotações, Zotero, histórico): mais fiel; depende de existir.
2. **Reconstrução verificável**: para cada fonte, conferir se consta das referências das
   âncoras [2]–[5] (1 passo), de outra fonte já incluída (2º passo) ou de nenhuma
   ("fora da cadeia"). Fontes: PDFs das âncoras ou metadados do OpenAlex (os anais
   ECIS/ICIS de [4] e [5] costumam não ter referências no OpenAlex → PDFs).
   Limite: mostra que **existe** um caminho, não que foi **o** caminho usado; o texto
   deve falar em "rastreabilidade reconstruída".
3. **Misto (recomendado)**: reconstrução (2) + confirmação/correção dos autores por linha.

### Efeito esperado
Algumas fontes devem cair em "fora da cadeia" (candidatos: clássicos como Festinger
[47] e Noelle-Neumann [24]). A Seção 4.3 teria de declarar que o *chaining* foi
complementado pelo conhecimento dos autores, um fato que depende de T01-D2.

### Ajustes de T01 associados (retirados da T01)
- **A12**: Seção 4.3, §2 — trocar a afirmação de auditabilidade por remissão à Table S1.
- **A15**: seção "Supplementary Materials" do template MDPI + a própria Table S1
  (52 linhas: 41 mecanismos + 11 affordances).

### Para retomar
Decisão do usuário sobre incluir a S1 no paper → resolver T01-D2 (perguntas aos autores) →
tarefa de verificação de referências (numeração) → reconstrução e confirmação dos autores.
