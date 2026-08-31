# Protocolo de triagem — LLMs para geração de WBS/EAP

- **Localização**: innovox/radix/llm-wbs-generation
- **Derivado de**: `context.md` e `search-protocol.md`
- **Uso**: aplicar a cada PDF obtido, em qualquer assistente de IA, para decidir
  objetivamente se o paper pertence ao corpus da revisão.

---

## O que esta triagem decide

A busca no OpenAlex filtra por termos; ela não distingue um paper que **usa LLM
para produzir WBS** de um que apenas menciona LLM e gestão de projetos na mesma
frase. Esta triagem faz esse corte, lendo o texto completo.

O critério decisivo é a **direção da relação**:

| Direção | Veredito |
|---|---|
| LLM → estrutura (o modelo **produz** a decomposição) | INCLUIR |
| estrutura → LLM (o WBS é entrada, treino ou condicionamento) | EXCLUIR |
| LLM e gestão de projetos coexistem, sem geração de estrutura | EXCLUIR |

---

## Perguntas de investigação

Cada paper deve ser respondido nestas seis perguntas.

**Q1 — Geração.** O trabalho usa LLM/IA generativa para **produzir** uma estrutura
de decomposição de escopo, trabalho ou tarefas (WBS, EAP, backlog hierárquico,
árvore de tarefas, plano de projeto estruturado)?

**Q2 — Hierarquia.** A estrutura produzida é **hierárquica** (pai-filho, níveis,
decomposição sucessiva) ou apenas uma lista plana de itens?

**Q3 — Domínio.** O objeto decomposto é **escopo de projeto** (entregas, pacotes de
trabalho, atividades) ou outra coisa (plano de ação robótico, cadeia de chamadas de
API, passos de raciocínio)?

**Q4 — Nomenclatura.** O paper usa explicitamente o termo **WBS / Work Breakdown
Structure / EAP / Estrutura Analítica de Projeto**, ou um vocabulário vizinho
(user story mapping, backlog, task tree, hierarchical plan)?

**Q5 — Avaliação.** O trabalho **avalia** a estrutura gerada? Se sim, com que
método e quais métricas — completude, consistência, cobertura de entregas,
comparação com baseline humano, julgamento por especialistas, LLM-as-judge?

**Q6 — Lacuna.** O paper aponta limitações ou trabalhos futuros relacionados à
geração ou avaliação de estruturas hierárquicas de escopo?

---

## Regras de veredito

- **INCLUIR** — Q1 sim **e** Q3 é escopo de projeto. Núcleo do corpus.
- **TALVEZ** — Q1 sim, mas Q3 é outro domínio **e** o mecanismo de estruturação
  parece transferível para escopo de projeto. Registrar como correlato.
- **EXCLUIR** — Q1 não; ou o WBS é entrada e não saída (E3); ou não há LLM
  envolvido na estruturação (E2); ou nada tem a ver com decomposição (E1).

### Score de aderência (0-10)

| Faixa | Significado |
|---|---|
| 9-10 | LLM gera WBS/EAP hierárquico de escopo de projeto, com avaliação |
| 7-8 | LLM gera estrutura hierárquica de escopo, sem avaliação formal |
| 5-6 | LLM gera plano/decomposição de projeto, hierarquia fraca ou implícita |
| 3-4 | LLM decompõe tarefas em outro domínio, mecanismo transferível |
| 1-2 | LLM em gestão de projetos sem gerar estrutura; ou WBS sem LLM |
| 0 | Sem relação com o tema |

---

## Prompt pronto para colar

Copie o bloco abaixo e envie junto com o PDF (ou seu texto) à outra IA.

```text
Você vai triar um artigo científico para uma revisão de literatura.

TEMA DA REVISÃO
Uso de Large Language Models (LLMs) na geração, decomposição e estruturação
hierárquica de Work Breakdown Structures (WBS / Estrutura Analítica de Projeto).
Interessa o LLM PRODUZINDO a estrutura — não o WBS servindo de entrada, treino
ou condicionamento para o modelo. A direção da relação é o critério decisivo.

REGRAS
1. Responda APENAS com base no texto do artigo fornecido. Não use conhecimento
   prévio sobre o paper nem sobre os autores.
2. Toda afirmação factual deve vir acompanhada de citação textual literal do
   artigo (entre aspas). Se não houver trecho que sustente, escreva
   "não encontrado no texto".
3. Não infira o que o artigo não diz. Ausência de informação é uma resposta
   válida e útil.

PERGUNTAS
Q1 GERAÇÃO: o trabalho usa LLM/IA generativa para PRODUZIR uma estrutura de
   decomposição de escopo, trabalho ou tarefas?
Q2 HIERARQUIA: a estrutura produzida é hierárquica (níveis, pai-filho,
   decomposição sucessiva) ou uma lista plana?
Q3 DOMÍNIO: o objeto decomposto é escopo de projeto (entregas, pacotes de
   trabalho, atividades) ou outro domínio (robótica, chamadas de API,
   passos de raciocínio)?
Q4 NOMENCLATURA: o artigo usa os termos "WBS", "Work Breakdown Structure",
   "EAP" ou "Estrutura Analítica de Projeto"? Se não, que vocabulário usa
   para a estrutura (backlog, user story mapping, task tree, hierarchical plan)?
Q5 AVALIAÇÃO: o trabalho avalia a estrutura gerada? Com que método e quais
   métricas (completude, consistência, cobertura de entregas, baseline humano,
   julgamento de especialistas, LLM-as-judge)?
Q6 LACUNA: que limitações ou trabalhos futuros o artigo aponta sobre geração ou
   avaliação de estruturas hierárquicas de escopo?

FORMATO DA RESPOSTA (siga exatamente)

VEREDITO: INCLUIR | TALVEZ | EXCLUIR
SCORE: <0-10>
JUSTIFICATIVA: <uma frase>

Q1 GERAÇÃO: <Sim/Não/Parcial> — <evidência: "citação literal">
Q2 HIERARQUIA: <Hierárquica/Plana/Não se aplica> — <evidência>
Q3 DOMÍNIO: <escopo de projeto / outro: qual> — <evidência>
Q4 NOMENCLATURA: <termos usados> — <evidência>
Q5 AVALIAÇÃO: <método e métricas, ou "não avalia"> — <evidência>
Q6 LACUNA: <limitações declaradas, ou "não declara">

TIPO DE FONTE: <revisado por pares / preprint / não identificado>
DIREÇÃO DA RELAÇÃO: <LLM produz a estrutura / estrutura alimenta o LLM / ambos / nenhum>

CRITÉRIO DE VEREDITO
- INCLUIR: Q1 = Sim E Q3 = escopo de projeto.
- TALVEZ: Q1 = Sim, Q3 = outro domínio, mas o mecanismo parece transferível
  para escopo de projeto.
- EXCLUIR: Q1 = Não; ou o WBS é entrada e não saída; ou não há LLM na
  estruturação; ou o artigo não trata de decomposição.

CRITÉRIO DE SCORE
9-10 gera WBS/EAP hierárquico de escopo, com avaliação
7-8  gera estrutura hierárquica de escopo, sem avaliação formal
5-6  gera plano/decomposição de projeto, hierarquia fraca
3-4  decompõe tarefas em outro domínio, mecanismo transferível
1-2  LLM em gestão de projetos sem gerar estrutura; ou WBS sem LLM
0    sem relação
```

---

## Registro das triagens

Preencha conforme for triando. O que for INCLUIR ou TALVEZ segue para o pipeline
(`materials/` → `/process-materials`).

| Paper | Veredito | Score | Direção | Avalia? | Nota |
|---|---|---|---|---|---|
| Schröder 2023 — AutoScrum | INCLUIR | 10 | LLM produz | Não | Vocabulário Scrum, não WBS; sem avaliação da estrutura |
