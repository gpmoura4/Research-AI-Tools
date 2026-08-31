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

Este tema é **estrito**. São dois testes, ambos obrigatórios:

**Teste 1 — o objeto é WBS/EAP?** O trabalho trata de Work Breakdown Structure,
Estrutura Analítica de Projeto, ou estrutura hierárquica de decomposição de escopo
explicitamente equiparada a isso. Planejamento de projeto, backlog ágil e gestão em
geral **não bastam** — pertencem ao tema `llm-project-management`.

**Teste 2 — a direção da relação.**

| Direção | Veredito |
|---|---|
| método → WBS (o sistema **produz** a estrutura) | INCLUIR |
| WBS → método (a estrutura é entrada, treino ou insumo) | EXCLUIR |
| WBS mencionado sem ser objeto do trabalho | EXCLUIR |

**Sobre trabalhos pré-LLM**: geração automática de WBS por ontologias, case-based
reasoning ou otimização é **INCLUIR** com marcação `[PRÉ-LLM]`. Eles são a linha de
base contra a qual os LLMs devem ser comparados — fundamentação do estado da arte,
não ruído.

---

## Perguntas de investigação

Cada paper deve ser respondido nestas seis perguntas.

**Q0 — Objeto.** O trabalho trata de **WBS / Work Breakdown Structure / EAP /
Estrutura Analítica de Projeto** como objeto central? Se o termo aparece apenas de
passagem, ou se a estrutura discutida é um backlog ágil sem equiparação a WBS,
a resposta é não — e o paper pertence ao tema irmão.

**Q1 — Geração.** O trabalho **produz** a estrutura automaticamente ou de forma
assistida (por LLM, IA generativa, ontologia, case-based reasoning, otimização), ou
apenas usa/organiza um WBS já existente?

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

- **INCLUIR** — Q0 sim **e** Q1 produz. Núcleo do corpus. Marcar `[PRÉ-LLM]`
  quando o método não usar LLM: esses trabalhos são a linha de base.
- **TALVEZ** — Q0 sim, mas o trabalho apenas usa/organiza o WBS sem gerá-lo;
  entra como fundamentação conceitual, não como estado da arte.
- **EXCLUIR** — Q0 não (sem WBS/EAP como objeto — realocar para
  `llm-project-management` se tratar de planejamento com LLM); ou o WBS é entrada
  e não saída; ou o acrônimo casou por homonímia (ex.: Williams-Beuren Syndrome).

### Score de aderência (0-10)

| Faixa | Significado |
|---|---|
| 9-10 | LLM gera WBS/EAP, **com** avaliação da estrutura produzida |
| 7-8 | Gera WBS/EAP automaticamente, sem avaliação formal (inclui pré-LLM) |
| 5-6 | Fundamenta WBS (framework, dicionário, métricas) sem gerá-lo |
| 3-4 | Usa WBS como insumo de outro sistema (BIM, cronograma, banco de dados) |
| 1-2 | WBS mencionado de passagem |
| 0 | Falso positivo ou sem relação |

---

## Prompt pronto para colar

Copie o bloco abaixo e envie junto com o PDF (ou seu texto) à outra IA.

```text
Você vai triar um artigo científico para uma revisão de literatura.

TEMA DA REVISÃO
Geração, decomposição e estruturação hierárquica de Work Breakdown Structures
(WBS / Estrutura Analítica de Projeto), com foco em Large Language Models — mas
incluindo métodos automatizados anteriores (ontologias, case-based reasoning,
otimização), que servem de linha de base.

DOIS TESTES OBRIGATÓRIOS
1. O WBS/EAP é objeto central do trabalho? Planejamento de projeto ou backlog
   ágil sem equiparação explícita a WBS NÃO conta.
2. O método PRODUZ a estrutura, ou apenas usa uma já existente? Interessa
   produzir. WBS como entrada que alimenta o sistema é motivo de exclusão.

ATENÇÃO: "WBS" também é acrônimo de Williams-Beuren Syndrome e de outros termos.
Confirme que se trata de Work Breakdown Structure.

REGRAS
1. Responda APENAS com base no texto do artigo fornecido. Não use conhecimento
   prévio sobre o paper nem sobre os autores.
2. Toda afirmação factual deve vir acompanhada de citação textual literal do
   artigo (entre aspas). Se não houver trecho que sustente, escreva
   "não encontrado no texto".
3. Não infira o que o artigo não diz. Ausência de informação é uma resposta
   válida e útil.

PERGUNTAS
Q0 OBJETO: o artigo trata de WBS/EAP como objeto central, ou apenas menciona
   o termo de passagem?
Q1 GERAÇÃO: o trabalho PRODUZ a estrutura automaticamente ou de forma assistida
   (LLM, IA generativa, ontologia, case-based reasoning, otimização), ou apenas
   usa/organiza um WBS já existente?
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

Q0 OBJETO: <Sim/Não/De passagem> — <evidência: "citação literal">
Q1 GERAÇÃO: <Produz/Usa existente/Não se aplica> — <evidência: "citação literal">
MÉTODO DE GERAÇÃO: <LLM / IA generativa / ontologia / CBR / otimização / outro / nenhum>
Q2 HIERARQUIA: <Hierárquica/Plana/Não se aplica> — <evidência>
Q3 DOMÍNIO: <escopo de projeto / outro: qual> — <evidência>
Q4 NOMENCLATURA: <termos usados> — <evidência>
Q5 AVALIAÇÃO: <método e métricas, ou "não avalia"> — <evidência>
Q6 LACUNA: <limitações declaradas, ou "não declara">

TIPO DE FONTE: <revisado por pares / preprint / não identificado>
DIREÇÃO DA RELAÇÃO: <LLM produz a estrutura / estrutura alimenta o LLM / ambos / nenhum>

CRITÉRIO DE VEREDITO
- INCLUIR: Q0 = Sim E Q1 = Produz. Marque [PRÉ-LLM] se o método não usa LLM.
- TALVEZ: Q0 = Sim, mas apenas usa/organiza o WBS — fundamentação conceitual.
- EXCLUIR: Q0 = Não (se tratar de planejamento com LLM sem WBS, indique que
  pertence ao tema irmão llm-project-management); ou WBS é entrada e não saída;
  ou o acrônimo casou por homonímia.

CRITÉRIO DE SCORE
9-10 gera WBS/EAP com avaliação da estrutura produzida
7-8  gera WBS/EAP automaticamente, sem avaliação formal (inclui pré-LLM)
5-6  fundamenta WBS (framework, dicionário, métricas) sem gerá-lo
3-4  usa WBS como insumo de outro sistema (BIM, cronograma, banco)
1-2  WBS mencionado de passagem
0    falso positivo ou sem relação
```

---

## Registro das triagens

Preencha conforme for triando. O que for INCLUIR ou TALVEZ segue para o pipeline
(`materials/` → `/process-materials`).

| Paper | Veredito | Score | Método | Avalia? | Nota |
|---|---|---|---|---|---|
