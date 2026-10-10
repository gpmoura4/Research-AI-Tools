# T02 — Nomear por extenso itens citados só pelo ID ou pelo número

- **Manuscrito**: smip-famo-framework
- **Versão revisada**: `paper/v1-2026-10-08.pdf`, com o texto conferido na cópia de revisão
  em Google Docs após os ajustes da T01 (revisão `AHj4eMQuw-…`, 2026-10-10)
- **Data**: 2026-10-10
- **Relatórios anteriores consultados**: T01

## 1. Escopo

**Pedido do usuário**: onde o texto se refere a um mecanismo, affordance, bloco ou obra
citada só pelo ID (M3, AF7, Bloco A) ou só pelo número ([6–8]), acrescentar o nome por
extenso, para deixar o texto mais claro. Exemplo dado pelo usuário (Seção 6.2, M3): "melhor
capturado por F1, F2 e F4" → nomes de F1, F2 e F4 com o rótulo do bloco.

**Decisões do usuário (2026-10-10)**:

| # | Tema | Decisão |
|---|---|---|
| D1 | IDs a expandir | **Só os IDs citados.** Não acrescentar itens do mesmo bloco que o original não cita (no exemplo, F3 não entra). |
| D2 | Rótulo do bloco | **"Bloco F (Interação e comunicação)"**, sem travessão. Nas seções em inglês, "Block F (Interaction and communication)". |
| D3 | Listas "Feeds:" da 7.1 | **Expandir, agrupadas por bloco.** |
| D4 | Repetições | **Só a primeira menção sem nome em cada parágrafo.** Exceção: dentro das listas "Feeds:", todo item recebe o nome. |

**Convenções adotadas**:
- Nomes de mecanismos e affordances: os da Table 5 (taxonomia, atual numeração) e da
  Table 6 (affordances), literalmente, inclusive "&".
- Forma "Nome (ID)", como no exemplo do usuário.
- Nas seções 6.1–6.10 (ainda em português), o texto novo segue em português, com os nomes
  dos itens em inglês, como nas entradas da própria seção.
- Nomes dos blocos em inglês: tradução dos títulos 6.2–6.10, que ainda estão em português.
  Os autores podem preferir outra tradução ao traduzir a Seção 6.

**Fora do escopo**: tabelas (organizadas por ID por desenho), figuras (imagens), as
entradas de definição ("M3 — Online toxicity…") e menções que já trazem o nome, mesmo
quando o nome diverge do canônico (ver I01).

## 2. Mapeamento

Inventário automático no texto corrido da cópia de revisão, conferido à mão:

| Tipo | Menções | Sem nome | Ajustes |
|---|---|---|---|
| IDs de mecanismos e affordances | 260 | 84 pela heurística; 62 após conferência (o resto já tinha nome no parágrafo ou é repetição) | 30 |
| Blocos citados só pela letra | 6 menções a "Bloco X" na Seção 6 | 3 sem descrição | 3 (inclusos acima) |
| Citações só numéricas | 169 citações | 1 real ([6–8], Introdução); as demais trazem o autor ou o nome da obra (SPIR [2]) | 1 |

Concentração: as 11 listas "Feeds:" da 7.1 respondem por 49 das menções sem nome.

## 3. Avaliação

### T02-F01 — Itens referidos só pelo ID ou pelo número · **Menor**
- **Localização**: Introdução (§ das contribuições); Seções 6.2, 6.4, 6.7 e 6.10; 7.1
  (as 11 listas "Feeds:" e dois parágrafos "Why…"); 7.3; 9.1; 9.2; 10.2; 11 (item 4).
- **Fato**: exemplos: "o mecanismo por trás é melhor capturado por F1, F2 e F4" (6.2);
  "Feeds: A1, A2, A5, C4, C5, D1, D2, G2, H1, H2 (indirect), M1 (indirect), M5, M6"
  (7.1, AF1); "four of the eleven affordances (AF2, AF3, AF4, and AF8)" (9.1); "only a
  single mechanism, AF7 via F3" (9.1); "the social media affordance literature [6–8]"
  (Introdução). Na Seção 11 há placeholders dos autores: "F2 (nomear mecanismo) and M7
  (nomear mecanismo)" e "E1 and E4 (nomear mecanismos)".
- **Julgamento**: com 52 IDs em nove blocos, o leitor precisa voltar às tabelas para
  entender a frase. O problema pesa mais nas Seções 9–11, lidas por quem pula a taxonomia.
  É polimento, mas melhora muito a legibilidade. Os ajustes T02-A1 a A32 cobrem todos os
  casos e preenchem os placeholders da Seção 11.
- **Relação com revisões anteriores**: nova.

## 4. Achados indiretos

### T02-I01 — Nomes dos itens variam entre tabela, definição, prosa e figura · **Menor**
- **Localização**: Seções 6, 7.1, 8, 9.1, 10.2, 11; Figura 4.
- **Fato**: exemplos: B5 é "Interpersonal tension & identity salience" na Table 5,
  "Interpersonal political tension & identity salience activation" na 6.4 e
  "…salience activation" na 5.1 e na 7.1. C5 é "Negativity bias & moral contagion" na
  tabela e "Negativity bias & moral-emotional contagion" na 6.5. AF1 aparece como
  "algorithmic curation" (8, 10.2), AF6 como "audience collapse" (11), G1 como
  "disintermediation and gatekeeping erosion" (10.2), M6 como "reinforcement spirals"
  (10.2), E4 como "social quantification and status metrics" (10.2) e B4 como "sorting"
  (9.1). A Figura 4 rotula AF3 "Association", AF7 "Format" e os blocos com uma palavra
  ("M — spirals", "A — algorithm"), diferente dos títulos da Seção 6.
- **Julgamento**: o leitor que procura o item pelo nome não o encontra na tabela. Convém
  fixar um nome canônico por item, usado em todo o texto e na figura. Fora do escopo da
  T02, que só acrescenta nomes onde não há. Os ajustes usam os nomes das tabelas.

### T02-I02 — "AF7 via F3" chamado de mecanismo · **Menor**
- **Localização**: Seção 9.1, § 2.
- **Fato**: "only a single mechanism, AF7 via F3, is supported by robust, direct causal
  evidence".
- **Julgamento**: confirma T01-I02. AF7 é affordance, e o que tem evidência é o vínculo
  AF7 → F3. O A26 só nomeia os itens e não muda "mechanism", para não alterar a
  afirmação. A correção conceitual fica para tarefa própria.

## 5. Sugestões
- F01: T02-A1 a A32 **aplicados** na cópia de revisão em 2026-10-10, nos três lotes aprovados juntos. Os 32 foram conferidos no documento depois da gravação, e não havia edições humanas no texto desde o retrato anterior (ver `adjustments/T02-ajustes.md`).
- I01: definir com os autores um nome canônico por item e uniformizar texto, tabelas e
  Figura 4.

## 6. Pendências

| # | Item [a verificar] | Achado | O que falta |
|---|---|---|---|
| P1 | Tradução dos nomes dos blocos para o inglês | F01 | Confirmação dos autores ao traduzir a Seção 6 |
