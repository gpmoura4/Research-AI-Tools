# Protocolo de triagem — Journalism and Media × FAMO

- **Localização**: mestrado/research/journalism-and-media-affordances
- **Derivado de**: `context.md` e `search-protocol.md` (validado em 2026-10-15)
- **Uso**: aplicar a cada PDF obtido, em qualquer assistente de IA ou na leitura própria,
  para decidir se o artigo pertence ao corpus e onde ele conversa com o manuscrito
  (tarefa T04 de `manuscripts/smip-famo-framework/`).
- **Confidencialidade**: o prompt abaixo descreve o FAMO só no nível do `context.md`
  (camadas e tipos de outcome). Não colar nele trechos do manuscrito.

---

## O que esta triagem decide

A busca filtra por termos dentro da revista. Ela não distingue um artigo que **analisa o
design da plataforma** (features, affordances, algoritmos, métricas, regras) como causa ou
condição de algum efeito de um artigo que **usa a plataforma só como fonte de dados** ou
que estuda prática jornalística sem dimensão de plataforma.

O critério central é o **papel da plataforma** no estudo:

| Papel da plataforma | Veredito |
|---|---|
| Design (features, affordances, algoritmo, métricas, governança) é variável ou objeto de análise | INCLUIR |
| Plataforma é contexto relevante, mas o design não é analisado (ex.: jornalismo em plataformas descrito sem algoritmo, métricas ou visibilidade) | TALVEZ |
| Plataforma é só fonte de dados (corpus de posts sobre um tema qualquer) ou não aparece | EXCLUIR |

Um segundo eixo diz **onde** o artigo entra no manuscrito: camada do FAMO
(feature, affordance, mecanismo, outcome, moderador, intervenção) ou Seção 10.2
(implicações para o jornalismo). Esse eixo não decide o veredito, mas orienta o mapeamento
da T04 (apoia, contrasta ou estende).

---

## Perguntas de investigação

**Q0 — Tipo de texto.** Artigo de pesquisa (empírico ou teórico) ou revisão? Editorial,
errata, resenha e chamada de edição especial são excluídos.

**Q1 — Papel da plataforma.** O design da plataforma (features, affordances, algoritmos de
recomendação ou ranqueamento, métricas visíveis, regras de moderação ou governança) é
analisado como causa, condição ou objeto? Ou a plataforma é só de onde vêm os dados?

**Q2 — Affordances.** O artigo usa o conceito de affordance? Com que definição e
referências (Gibson, Hutchby, Evans et al., Bucher e Helmond, outros)? Quais affordances
nomeia (visibilidade, persistência, editabilidade, associação, quantificação, curadoria
algorítmica, anonimato, escalabilidade, colapso de contexto…)? Separa feature de affordance?

**Q3 — Mecanismos.** O artigo descreve um processo pelo qual o design produz efeitos sobre
usuários ou sobre o ecossistema? Exemplos: exposição seletiva, amplificação algorítmica,
homofilia de rede, recompensa por engajamento, quantificação social, normas percebidas,
incivilidade, circulação de desinformação, evitação de notícias, dependência de redações.

**Q4 — Outcomes.** O artigo mede ou discute polarização (ideológica, afetiva, percebida,
estrutural ou comportamental) ou um outcome adjacente (fragmentação de audiência,
incivilidade, desconfiança na mídia, evitação de notícias)? Com que medida?

**Q5 — Jornalismo em plataformas.** O artigo trata da relação entre jornalismo e o design
das plataformas: dependência de curadoria algorítmica, métricas de audiência, visibilidade,
regras de governança, adaptação das rotinas de redação a essas condições?

**Q6 — Moderadores e intervenções.** O artigo identifica condições que mudam o efeito
(país, sistema midiático, plataforma, características individuais, contexto político) ou
propõe intervenções (de design, regulação, prática jornalística, letramento)?

**Q7 — Evidência.** Tipo de estudo (experimento, survey, análise de conteúdo, entrevistas,
etnografia, modelagem, ensaio teórico, revisão), plataforma(s), país(es), período e tamanho
da amostra.

---

## Regras de veredito

- **INCLUIR**: Q0 = pesquisa ou revisão **e** Q1 = design analisado **e** ao menos uma de
  Q2–Q5 com resposta substantiva.
- **TALVEZ**: Q0 = pesquisa ou revisão **e** Q1 = plataforma como contexto relevante, sem
  análise do design, mas com contribuição conceitual aproveitável (ex.: uso do conceito de
  affordance em jornalismo, ou outcome de polarização sem ligação explícita com o design).
- **EXCLUIR**: Q0 = editorial, errata, resenha ou chamada (exclusão 1); estudo de prática
  jornalística sem dimensão de plataforma ou de design (exclusão 2); plataforma só como
  fonte de dados para tema sem relação com o FAMO (exclusão 3); texto fora de en/pt (G7).

### Score de aderência (0-10)

| Faixa | Significado |
|---|---|
| 9-10 | Liga explicitamente design ou affordances a um mecanismo e a um outcome de polarização (ou adjacente), com evidência empírica ou modelo teórico detalhado |
| 7-8 | Análise explícita de affordances ou features de plataforma, **ou** polarização ligada a plataformas, sem cobrir a cadeia toda |
| 5-6 | Jornalismo em plataformas com algoritmo, métricas ou visibilidade como variável (Seção 10.2), **ou** um mecanismo isolado (incivilidade, desinformação, evitação) com a plataforma como variável |
| 3-4 | Conceito do FAMO usado de passagem, ou plataforma como contexto sem análise do design |
| 1-2 | Plataforma só como fonte de dados |
| 0 | Falso positivo ou sem relação |

---

## Prompt pronto para colar

Copie o bloco abaixo e envie junto com o PDF (ou seu texto) à outra IA.

```text
Você vai triar um artigo científico para uma revisão de literatura.

TEMA DA REVISÃO
Como o design das plataformas de mídia social (features técnicas, affordances,
algoritmos, métricas visíveis, regras de moderação e governança) se relaciona com
polarização e fenômenos vizinhos, e como o jornalismo depende dessas condições.
O quadro de referência tem quatro camadas: features (elementos técnicos concretos)
→ affordances (possibilidades de ação que surgem da relação entre feature e usuário)
→ mecanismos (processos causais recorrentes) → outcomes (polarização ideológica,
afetiva, percebida, estrutural e comportamental). Há ainda moderadores (condições
que mudam o efeito) e intervenções.

TESTE CENTRAL
O design da plataforma é analisado no artigo (como causa, condição ou objeto)?
Ou a plataforma é só a fonte de onde vieram os dados? Interessa o primeiro caso.

REGRAS
1. Responda APENAS com base no texto do artigo fornecido. Não use conhecimento
   prévio sobre o artigo nem sobre os autores.
2. Toda afirmação factual deve vir com citação textual literal do artigo (entre
   aspas) e a página, quando houver. Se não houver trecho que sustente, escreva
   "não encontrado no texto".
3. Não infira o que o artigo não diz. Ausência de informação é uma resposta válida.

PERGUNTAS
Q0 TIPO: artigo de pesquisa (empírico ou teórico), revisão, ou editorial / errata /
   resenha / chamada de edição especial?
Q1 PAPEL DA PLATAFORMA: o design (features, affordances, algoritmo, métricas,
   moderação, governança) é analisado como causa, condição ou objeto, é só contexto,
   ou a plataforma é apenas fonte de dados?
Q2 AFFORDANCES: o artigo usa o conceito de affordance? Com que definição e quais
   referências? Quais affordances nomeia? Distingue feature de affordance?
Q3 MECANISMOS: o artigo descreve um processo pelo qual o design produz efeitos
   (exposição seletiva, amplificação algorítmica, homofilia, recompensa por
   engajamento, quantificação social, normas percebidas, incivilidade,
   desinformação, evitação de notícias, dependência de redações, outro)?
Q4 OUTCOMES: o artigo mede ou discute polarização (ideológica, afetiva, percebida,
   estrutural, comportamental) ou outcome vizinho (fragmentação, incivilidade,
   desconfiança, evitação)? Com que medida?
Q5 JORNALISMO EM PLATAFORMAS: o artigo trata da dependência do jornalismo em relação
   a algoritmos, métricas de audiência, visibilidade ou regras das plataformas?
Q6 MODERADORES E INTERVENÇÕES: que condições mudam o efeito (país, plataforma,
   indivíduo, contexto político)? Que intervenções propõe (design, regulação,
   prática jornalística, letramento)?
Q7 EVIDÊNCIA: tipo de estudo, plataforma(s), país(es), período, tamanho da amostra.

FORMATO DA RESPOSTA (siga exatamente)

VEREDITO: INCLUIR | TALVEZ | EXCLUIR
SCORE: <0-10>
JUSTIFICATIVA: <uma frase>

Q0 TIPO: <pesquisa empírica / pesquisa teórica / revisão / editorial etc.> — <evidência>
Q1 PAPEL DA PLATAFORMA: <design analisado / contexto / só fonte de dados> — <"citação literal", p.>
Q2 AFFORDANCES: <Sim/Não> — <definição e referências usadas> — <affordances nomeadas> — <evidência>
Q3 MECANISMOS: <processos descritos, ou "não descreve"> — <evidência>
Q4 OUTCOMES: <outcomes e medidas, ou "não trata"> — <evidência>
Q5 JORNALISMO EM PLATAFORMAS: <Sim/Não> — <evidência>
Q6 MODERADORES / INTERVENÇÕES: <listar, ou "não trata"> — <evidência>
Q7 EVIDÊNCIA: <tipo de estudo; plataforma; país; período; N>

CAMADA PRINCIPAL: <feature / affordance / mecanismo / outcome / moderador /
                   intervenção / jornalismo em plataformas / nenhuma>

CRITÉRIO DE VEREDITO
- INCLUIR: Q0 = pesquisa ou revisão E Q1 = design analisado E ao menos uma de
  Q2–Q5 substantiva.
- TALVEZ: Q0 = pesquisa ou revisão E Q1 = contexto, com contribuição conceitual
  aproveitável.
- EXCLUIR: editorial, errata, resenha ou chamada; prática jornalística sem dimensão
  de plataforma; plataforma só como fonte de dados; texto fora de inglês/português.

CRITÉRIO DE SCORE
9-10 liga design/affordances a mecanismo e a outcome de polarização (ou vizinho),
     com evidência ou modelo teórico detalhado
7-8  análise explícita de affordances/features, ou polarização ligada a plataformas,
     sem a cadeia toda
5-6  jornalismo em plataformas com algoritmo/métricas/visibilidade como variável,
     ou um mecanismo isolado com a plataforma como variável
3-4  conceito usado de passagem, ou plataforma como contexto sem análise do design
1-2  plataforma só como fonte de dados
0    falso positivo ou sem relação
```

---

## Registro das triagens

Preencha conforme for triando. Os INCLUIR e TALVEZ seguem para o mapeamento da T04
(`manuscripts/smip-famo-framework/reviews/T04-journalism-and-media.md`).

| Paper | Passada | Veredito | Score | Camada / seção do manuscrito | Relação (apoia · contrasta · estende) | Nota |
|---|---|---|---|---|---|---|
| Voinea 2025 — gatekeeping e IA | P2 | INCLUIR | 8 | Gatekeeping decline; loop; 10.2 | apoia; contrasta em parte (gatekeeping redistribuído); estende o loop | síntese teórica de ~80 obras |
| Almakaty 2026 — agenda-setting, sistemas e regimes | P2 | INCLUIR | 8 | Algorithmic agenda-setting; moderadores; 9.2 | apoia | revisão integrativa, 108 fontes; publicada em out. 2026 |
| Ronzhyn et al. 2025 — ação coletiva no Facebook | P1 | INCLUIR | 7 | 2.3/5.1 (uso efetivo); AF10 | apoia; estende (governança restringe outras affordances) | 8 perfis, 3 entrevistas |
| Nelson et al. 2021 — remoção de comentários | P1 | INCLUIR | 6 | 10.2 | contrasta (controle editorial); apoia (dependência) | 20 declarações, EUA e Reino Unido |
| Fu et al. 2025 — polarização de grupo | P2 | INCLUIR | 6 | Group polarization; 7.3; Introdução | apoia | revisão sistemática, 143 artigos |
| Wazzan e Aldamen 2023 — estudantes turcos | P2 | TALVEZ | 4 | Spiral of silence; 9.2 | estende (censura estatal) | amostra de conveniência, α 0,515 |
| Nwafor et al. 2026 — affordances na Nigéria | P1 | TALVEZ | 4 | 5.1; 9.2 | apoia; estende (medida de affordance percebida) | outcome não é polarização |
| Serttaş et al. 2025 — Synthetic Social Alienation | P2 | EXCLUIR | 2 | Introdução | apoia (conceitual) | 10 entrevistas e dados sintéticos |
