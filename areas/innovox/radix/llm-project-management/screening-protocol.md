# Protocolo de triagem — LLMs em gestão e planejamento de projetos

- **Localização**: innovox/radix/llm-project-management
- **Derivado de**: `context.md` e `search-protocol.md`
- **Uso**: aplicar a cada PDF obtido, em qualquer assistente de IA, para decidir
  objetivamente se o paper pertence ao corpus.

---

## O que esta triagem decide

A busca filtra por termos; ela não distingue um paper que **aplica** LLM a
planejamento de um que apenas menciona os dois assuntos. Esta triagem faz o corte
lendo o texto completo.

Este tema cobre o **contexto amplo**: LLM/GenAI em planejamento, decomposição de
tarefas, metodologias ágeis e prática profissional de gestão de projetos.

| Situação | Veredito |
|---|---|
| LLM gera plano, backlog ou decomposição de tarefas | INCLUIR |
| LLM apoia prática de PM (agentes, automação de fase do SDLC) | INCLUIR |
| Estuda adoção, impacto ou percepção de GenAI em PM | INCLUIR |
| **WBS/EAP é o objeto central** | REALOCAR para `llm-wbs-generation` |
| Gestão de projetos sem IA generativa | EXCLUIR |
| LLM sem relação com planejamento ou gestão | EXCLUIR |

---

## Perguntas de investigação

**Q1 — Aplicação.** O trabalho aplica LLM/IA generativa a alguma atividade de
gestão ou planejamento de projetos? Qual atividade?

**Q2 — Artefato.** O sistema **produz** algum artefato de planejamento (plano,
backlog, user stories, cronograma, lista de tarefas), ou apenas apoia decisões e
comunicação?

**Q3 — Estrutura.** O artefato produzido tem organização hierárquica (níveis,
pai-filho, decomposição sucessiva) ou é uma lista plana?

**Q4 — Metodologia.** O trabalho se ancora em alguma metodologia declarada (Scrum,
SAFe, Kanban, PMBOK, waterfall) ou é agnóstico?

**Q5 — Avaliação.** Há avaliação do que o LLM produz? Com que método — comparação
com baseline humano, julgamento de especialistas, métricas automáticas, estudo com
usuários, LLM-as-judge?

**Q6 — WBS.** O artigo menciona WBS, Work Breakdown Structure, EAP ou Estrutura
Analítica de Projeto? Se for objeto central, o paper deve ser realocado.

**Q7 — Lacuna.** Que limitações ou trabalhos futuros o artigo declara?

---

## Regras de veredito

- **INCLUIR** — Q1 sim. Núcleo do corpus deste tema.
- **REALOCAR** — Q6 indica WBS/EAP como objeto central: pertence a
  `llm-wbs-generation`.
- **TALVEZ** — Q1 sim, mas a aplicação é tangencial (ex.: LLM para comunicação de
  equipe, sem tocar planejamento).
- **EXCLUIR** — Q1 não; ou é gestão de projetos sem IA generativa; ou o LLM atua
  em domínio sem relação com planejamento.

### Score de aderência (0-10)

| Faixa | Significado |
|---|---|
| 9-10 | LLM gera artefato de planejamento hierárquico, **com** avaliação |
| 7-8 | LLM gera artefato de planejamento, sem avaliação formal |
| 5-6 | LLM apoia atividade de gestão sem gerar artefato estruturado |
| 3-4 | Estudo de adoção, percepção ou impacto de GenAI em PM |
| 1-2 | Menção tangencial a gestão de projetos |
| 0 | Sem relação com o tema |

---

## Prompt pronto para colar

Copie o bloco abaixo e envie junto com o PDF (ou seu texto) à outra IA.

```text
Você vai triar um artigo científico para uma revisão de literatura.

TEMA DA REVISÃO
Uso de Large Language Models e IA generativa em gestão e planejamento de
projetos: geração de planos, decomposição de tarefas, apoio a metodologias
ágeis, agentes autônomos em funções de PM, e adoção pela prática profissional.

ATENÇÃO — TEMA IRMÃO
Existe uma revisão separada dedicada a Work Breakdown Structure (WBS/EAP). Se o
artigo tem WBS/EAP como OBJETO CENTRAL, marque REALOCAR em vez de INCLUIR.
Mencionar WBS de passagem não é motivo para realocar.

REGRAS
1. Responda APENAS com base no texto do artigo fornecido. Não use conhecimento
   prévio sobre o paper nem sobre os autores.
2. Toda afirmação factual deve vir acompanhada de citação textual literal do
   artigo (entre aspas). Se não houver trecho que sustente, escreva
   "não encontrado no texto".
3. Não infira o que o artigo não diz. Ausência de informação é resposta válida.

PERGUNTAS
Q1 APLICAÇÃO: o trabalho aplica LLM/IA generativa a alguma atividade de gestão
   ou planejamento de projetos? Qual atividade?
Q2 ARTEFATO: o sistema PRODUZ algum artefato de planejamento (plano, backlog,
   user stories, cronograma, lista de tarefas), ou apenas apoia decisões?
Q3 ESTRUTURA: o artefato produzido é hierárquico (níveis, pai-filho) ou uma
   lista plana?
Q4 METODOLOGIA: o trabalho se ancora em metodologia declarada (Scrum, SAFe,
   Kanban, PMBOK, waterfall) ou é agnóstico?
Q5 AVALIAÇÃO: há avaliação do que o LLM produz? Com que método (baseline
   humano, especialistas, métricas automáticas, estudo com usuários,
   LLM-as-judge)?
Q6 WBS: o artigo menciona "WBS", "Work Breakdown Structure", "EAP" ou
   "Estrutura Analítica de Projeto"? É objeto central ou menção de passagem?
Q7 LACUNA: que limitações ou trabalhos futuros o artigo declara?

FORMATO DA RESPOSTA (siga exatamente)

VEREDITO: INCLUIR | REALOCAR | TALVEZ | EXCLUIR
SCORE: <0-10>
JUSTIFICATIVA: <uma frase>

Q1 APLICAÇÃO: <atividade, ou "não aplica"> — <evidência: "citação literal">
Q2 ARTEFATO: <artefato produzido, ou "apenas apoio"> — <evidência>
Q3 ESTRUTURA: <Hierárquica/Plana/Não se aplica> — <evidência>
Q4 METODOLOGIA: <metodologia, ou "agnóstico"> — <evidência>
Q5 AVALIAÇÃO: <método e métricas, ou "não avalia"> — <evidência>
Q6 WBS: <objeto central / menção de passagem / não menciona> — <evidência>
Q7 LACUNA: <limitações declaradas, ou "não declara">

TIPO DE FONTE: <revisado por pares / preprint / não identificado>

CRITÉRIO DE VEREDITO
- INCLUIR: Q1 = sim.
- REALOCAR: Q6 = objeto central (pertence ao tema llm-wbs-generation).
- TALVEZ: Q1 = sim, mas aplicação tangencial ao planejamento.
- EXCLUIR: Q1 = não; ou gestão de projetos sem IA generativa; ou LLM em
  domínio sem relação com planejamento.

CRITÉRIO DE SCORE
9-10 gera artefato de planejamento hierárquico, com avaliação
7-8  gera artefato de planejamento, sem avaliação formal
5-6  apoia atividade de gestão sem gerar artefato estruturado
3-4  estudo de adoção, percepção ou impacto de GenAI em PM
1-2  menção tangencial a gestão de projetos
0    sem relação
```

---

## Registro das triagens

Preencha conforme for triando. O que for INCLUIR segue para o pipeline
(`materials/` → `/process-materials`).

| Paper | Veredito | Score | Artefato | Avalia? | Nota |
|---|---|---|---|---|---|
| Schröder 2023 — AutoScrum | INCLUIR | 9 | plano Scrum hierárquico | Não | Requisitos → user stories → features → tasks; nunca menciona WBS |
