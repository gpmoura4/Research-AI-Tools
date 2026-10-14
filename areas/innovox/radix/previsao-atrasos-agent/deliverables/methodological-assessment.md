# Avaliação metodológica do corpus — Agente de Previsão de Atraso

- **Localização**: innovox / radix / previsao-atrasos-agent
- **Data**: 2026-10-09
- **Documento de contexto**: [project-context-and-literature-review.md](../project-context-and-literature-review.md) (situação em 2026-10-09)
- **Corpus avaliado**: os 8 PDFs de [`materials/`](../materials/). Todos foram lidos na íntegra a partir do texto extraído (`pdftotext -layout`), e nenhum precisou de OCR.
- **Pergunta desta avaliação**: que papers dão base metodológica ao agente, seja para sustentar decisões já tomadas, seja para justificar uma mudança de paradigma. Não substitui a síntese por PR da A4.3.
- **Status**: concluído.

**Convenções de leitura**
- **Páginas**: usa-se a paginação do periódico quando existe (ex.: p. 530). Nos artigos MDPI e Springer, o número da página do artigo (ex.: p. 10/38). Em Pal et al. (anais sem paginação), a página do PDF.
- **Afirmação × inferência**: nas fichas (§4), os blocos de *Problema* a *Limitações* relatam o que o paper diz, com página, e os blocos *Aproveitar no agente* e *Não se aplica* são inferência desta avaliação. Fora das fichas, as inferências levam a marca *(inferência)*.

## Sumário

1. [Local e ambiguidades](#1-local-deste-relatório-e-ambiguidades)
2. [Entendimento do projeto](#2-entendimento-do-projeto)
3. [Ranking](#3-ranking)
4. [Fichas dos papers](#4-fichas-dos-papers)
5. [Decisões provisórias × corpus](#5-decisões-provisórias--corpus)
6. [Recomendações para o agente](#6-recomendações-para-o-agente)
7. [Lacunas da literatura](#7-lacunas-da-literatura)
8. [Observações sobre o corpus](#8-observações-sobre-o-corpus)

---

## 1. Local deste relatório e ambiguidades

**Local.** O repositório não tem padrão para relatórios analíticos no modo revisão de literatura. Por isso este arquivo fica em `deliverables/` do tema, onde ficam os entregáveis, com nome em kebab-case e em inglês, como `candidates.md` e `pending.md`. Um arquivo único evita criar estrutura nova, e o tema não tem índice a atualizar.

**Ambiguidades registradas** (seguidas com a interpretação indicada):

| ID | Ambiguidade | Interpretação adotada |
|---|---|---|
| A01 | O pedido fala em PR1–PR3, mas o contexto define PR1–PR6 (§6.3) | O mapeamento cobre as seis PRs, com PR1–PR3 em destaque |
| A02 | O pedido situa o Markdown em `Materials/`, mas ele está na raiz do tema e a pasta se chama `materials/` | Sem efeito |
| A03 | O §3 define o plano vigente como "o plano com os aditivos aprovados", mas não diz em que data esse plano é fixado quando um aditivo é aprovado **dentro** da janela de 3 meses | Fica como decisão em aberto (R03) |
| A04 | O F01 prevê recálculo diário, mas a unidade de observação é o mês (§3) | O recálculo diário reaproveita os atributos mensais, atualizados à medida que os dados chegam. Isso afeta as regras de salto e de defasagem |
| A05 | Os limites da validação (completude de 80%, fora da distribuição 0,6/0,8, defasagem de 2/4 meses, salto de 40 pontos) não têm fonte declarada | São provisórios e devem ser calibrados no benchmark (R07) |

---

## 2. Entendimento do projeto

**Problema e domínio.** O agente acompanha os projetos ativos de um portfólio de engenharia (plataforma CORTEX) e estima a probabilidade de desvio **antes** que ele vire impacto financeiro ou contratual. O gestor recebe uma probabilidade calibrada, uma classe de criticidade (Baixo/Médio/Alto/Crítico, com limiares provisórios de 0,25/0,50/0,75), a tendência, os atributos que mais pesaram e uma explicação em linguagem natural (§2.1, §3).

**Arquitetura e decisões técnicas**
- **Três camadas separadas**, por princípio não negociável (§2.2):
  - **preditiva**: aprendizado de máquina supervisionado sobre dados tabulares, determinístico e sem LLM;
  - **validação**: regras fixas, com três estados (liberado, liberado com ressalvas, bloqueado);
  - **generativa**: o LLM narra apenas a *projeção*, já em faixas.
- **Dados**: histórico financeiro e contratual, cuja existência e suficiência ainda não foram confirmadas. Sem autorização para dados reais, o benchmark A1 roda sobre dados sintéticos ou públicos (§4).
- **Alvo do MVP**: binário. É "sim" quando, no fim de um horizonte de 3 meses, o faturamento acumulado está 10% ou mais abaixo do plano vigente. Funciona como proxy financeiro do atraso de cronograma e é provisório, na versão v0.1 (§3).
- **Unidade de observação**: projeto-mês. Os últimos 3 meses de cada projeto ficam sem rótulo, e a validação temporal é obrigatória (§3).
- **Atributos**: desvio de faturamento em janelas, aditivos em 12 meses, desvio de margem, idade e fase, tipo de contrato, segmento, metodologia e faixa de valor. O tratamento inclui janelamento, normalização por porte, corte por percentis, log e codificação (§3.1).
- **Modelos**: modelo linear como referência, comitê de árvores e boosting. O contrato exige explicador aditivo, como SHAP (§3, §3.1).
- **Avaliação**: precisão, revocação, antecedência do alerta, uso do painel e fundamentação da narrativa (§2.4).

**Perguntas de pesquisa** (§6.3)
- **PR1 — Conceito e variável-alvo**: como atraso e desvio são operacionalizados, uso de proxies financeiros, limiares, horizontes e rotulagem.
- **PR2 — Preditores e engenharia temporal**: atributos com evidência, janelas, defasagens, várias observações por projeto, normalização.
- **PR3 — Modelos e avaliação**: comparação de algoritmos, vazamento, desbalanceamento, calibração, poucos dados, dados públicos.
- PR4 — Explicabilidade e confiança: SHAP, detecção de caso fora da distribuição, abstenção, antecedência.
- PR5 — Separação preditiva/generativa: LLM que narra a saída de um modelo de ML, com fidelidade numérica.
- PR6 — Sistemas práticos e domínios análogos.

**Restrições e premissas**
- O LLM nunca calcula o risco nem acessa a base, e valores financeiros só aparecem em faixa (§5.3).
- A equipe de co-execução não faz a integração em produção (§5.3).
- O risco central é a **existência de sinal** (§4).
- A revisão aceita domínios análogos, desde que o domínio de cada fonte seja registrado (§6.5).

---

## 3. Ranking

Score = (3·C1 + 3·C2 + 2·C3 + 2·C4 + 2·C5) / 12. Em caso de empate, vence o maior C2.

C1 aderência ao problema · C2 transferibilidade metodológica · C3 robustez da evidência · C4 compatibilidade com o projeto · C5 potencial de mudança de paradigma.

| Pos. | Paper | C1 | C2 | C3 | C4 | C5 | Score | PRs | Justificativa |
|---|---|---|---|---|---|---|---|---|---|
| 1 | [Bai, Lositska e Bukhanenko (2026)](#41-bai-lositska-e-bukhanenko-2026--358) | 4 | 5 | 2 | 4 | 2 | **3,58** | **PR1, PR2, PR3**, PR4 | Tem o desenho mais próximo do agente: alvo binário de estouro acima de 10%, observações projeto-período com janelas e baselines ingênuos. A evidência é frágil (15 projetos reais) |
| 2 | [Natarajan (2022)](#42-natarajan-2022--342) | 3 | 4 | 3 | 3 | 4 | **3,42** | **PR1, PR2, PR3** | Combina reference class forecasting e ML sobre 130 projetos reais. Traz a "visão de fora" como baseline e como caminho para comparáveis e severidade |
| 3 | [Gundidza, Kikuchi e Ozono (2026)](#43-gundidza-kikuchi-e-ozono-2026--292) | 2 | 3 | 4 | 3 | 3 | **2,92** | **PR1, PR2**, PR5 | Não faz previsão, mas é o mais rigoroso do corpus: extração por LLM com filtro de modalidade, anotação humana e análises de robustez. Serve ao teste de fundamentação e às regras de rotulagem |
| 4 | [Gao et al. (2026)](#44-gao-et-al-2026--258) | 3 | 2 | 3 | 3 | 2 | **2,58** | **PR3**, PR6 | Revisão sistemática ampla. Vale como mapa e pelas pistas (predição de atraso com teste muito abaixo do treino), não como método |
| 5 | [Pal, Murguia e Middleton (2024)](#45-pal-murguia-e-middleton-2024--208) | 2 | 3 | 1 | 2 | 2 | **2,08** | **PR1**, PR5 | O LLM extrai atraso acumulado e causas de relatórios semanais. Um único projeto, sem baseline |
| 6 | [Edeh et al. (2026)](#46-edeh-et-al-2026--208) | 3 | 2 | 1 | 2 | 2 | **2,08** | **PR3**, PR6 | O tema é o certo (detecção precoce de atraso e sobrecusto), mas a revisão é genérica e tem contagens PRISMA incoerentes |
| 7 | [Sun et al. (2025)](#47-sun-et-al-2025--200) | 2 | 2 | 2 | 1 | 3 | **2,00** | **PR1**, PR5 | Domínio análogo (propagação de atraso em rede aérea). Relevante para a V3.0 e como contraponto ao uso de LLM no cálculo |
| 8 | [Zahedi e Golchin (2024)](#48-zahedi-e-golchin-2024--092) | 0 | 1 | 3 | 1 | 0 | **0,92** | — | Fora do tema (carga de explosão em fachadas). Provável inclusão por homonímia (§8) |

**Leitura geral**
- **Onde o corpus não ajuda**: nenhum paper faz validação temporal, calibração de probabilidade, explicação por SHAP, regra de abstenção ou narração da saída de um modelo por LLM. Nesses pontos o desenho do agente está à frente do corpus, que por isso não serve para fundamentá-los. É preciso busca complementar (§7).
- **Apoio mais direto**: vem de Bai et al. (alvo acima de 10%, janelas, baselines ingênuos, projetos separados para teste). A evidência, porém, é fraca, então o paper serve de inspiração para o desenho e não de prova de desempenho.
- **Candidata a mudança de paradigma**: a "visão de fora" de Natarajan, isto é, ancorar a previsão na distribuição de projetos parecidos. Ela dá um baseline que testa o risco de existência de sinal e abre caminho para comparáveis e severidade.
- **Fidelidade de LLM**: Gundidza et al. são os únicos que tratam o tema com rigor. A tipologia de falhas deles se transpõe ao teste de fundamentação A2.4.
- **Hipótese de contribuição (§6.8)**: nenhuma fonte reúne as três peças. Com 8 papers isso não prova a lacuna, mas também não a contradiz.

---

## 4. Fichas dos papers

### 4.1 Bai, Lositska e Bukhanenko (2026) — 3,58

[*An Integrated Digital Risk Management System for Construction Projects Using Machine Learning*](<../materials/Bai et al - 2026 - An Integrated Digital Risk Management System for Construction Projects Using Machine Learning.pdf>). MAS Journal of Applied Sciences 11(3): 524–539. DOI 10.5281/zenodo.21808953.
- **Tipo**: revisado por pares; as datas de recebimento, revisão e aceite estão na p. 524.
- **Domínio**: construção residencial e comercial. Os orçamentos estão em UAH (p. 531), e os autores são de Kyiv.

**Problema.** Prever riscos de prazo, financeiros e técnicos em obras, num sistema que integra BIM, dados de gestão e aprendizado de máquina (p. 524, 528).

**Método**
- **Três modelos especializados** (p. 530):
  - Random Forest multiclasse (risco baixo, médio ou alto) com 24 atributos;
  - LSTM para o desvio de prazo em 4 a 8 semanas;
  - XGBoost multitarefa, que estima a probabilidade de estouro de orçamento **acima de 10%** e a magnitude do estouro.
- **Janelas deslizantes** de 4 semanas, com passo de 1 semana, sobre as quais se calculam a média, a **tendência linear** e a **volatilidade** (desvio-padrão) dos indicadores (p. 530).
- **Baselines**: avaliação de especialistas, regressão linear múltipla e extrapolação ingênua da tendência. Na classificação financeira, também regressão logística e Naive Bayes (p. 531, 534).
- **Divisão dos dados**: treino com 35 projetos sintéticos e 10 reais; teste com 5 projetos reais nunca vistos; validação cruzada 5-fold dentro do treino (p. 530–531).

**Dados**
- **Reais**: 15 projetos concluídos entre 2019 e 2025, com 1.847 pontos de controle e 8.234 observações (p. 528–529).
- **Sintéticos**: 35 cenários gerados por Monte Carlo. As marginais são empíricas, escolhidas por Anderson–Darling entre normal, lognormal e beta, e a correlação é preservada por decomposição de Cholesky. A diferença média de correlação entre real e sintético é de 0,043 (p. 529).
- **Disponibilidade**: sem dados nem código públicos.

**Resultados**
- **Classificação de risco (RF)**: acurácia de 82,3%, com F1 de 0,733 na classe "alto" (p. 532).
- **Estouro financeiro (XGBoost)**: acurácia de 0,857, precisão de 0,824, revocação de 0,778 e AUC-ROC de 0,912, com limiar ótimo de 0,45. A regressão logística fica em 72,4% de acurácia e 0,808 de AUC (p. 533–534).
- **Prazo (LSTM)**: MAE de 3,8 dias no horizonte de 4 semanas e de 8,1 dias em 8 semanas (p. 533).
- **Atributos mais importantes**:
  - no RF: desvio acumulado de prazo, volatilidade financeira nas últimas 4 semanas e número de mudanças na documentação (p. 532);
  - na regressão de magnitude do XGBoost: desvio acumulado de custo, índice de preços de materiais nos 3 meses anteriores, mudanças não programadas e número de subcontratadas (p. 533).
- **Acurácia por avanço do projeto**: sobe de 68,3% com 20% de execução para 93,4% com 80% (Tabela 10, p. 534).
- **Qualidade dos dados**: completude acima de 95% acrescenta 13,2 pontos percentuais de acurácia, e atualização em menos de 3 dias reduz o MAE de 7,8 para 4,2 dias (Tabela 11, p. 535).
- **Causas de erro**: 34,0% eventos externos, 26,4% qualidade dos dados, 20,8% **riscos raros ausentes do treino** e 13,2% relatórios distorcidos (Tabela 12, p. 535).

**Limitações**
- *Declaradas pelos autores*: só 15 projetos reais e dependência dos dados sintéticos, que podem carregar viés estrutural; ausência de explicabilidade (XAI) (p. 536).
- *Observadas nesta leitura*:
  - as descrições da divisão de dados conflitam: na p. 529 os projetos reais servem para "validação e teste", na p. 530 dez deles entram no treino e o RF aparece com divisão "80/20";
  - a conclusão afirma 89% de acurácia com 20% de execução (p. 537), mas a Tabela 10 mostra 68,3% (p. 534);
  - não há calibração de probabilidade;
  - a validação cruzada dentro do treino é aleatória;
  - o horizonte do alvo financeiro não é declarado.

**Aproveitar no agente** *(inferência)*
- (a) Tendência e volatilidade do desvio dentro das janelas, como atributos (R04).
- (b) Persistência e regressão logística como baselines no A1 (R01).
- (c) Projetos separados para teste, combinados com a divisão temporal, e métricas por fase de execução (R02).
- (d) Uma receita de gerador sintético para testar o pipeline (R06).
- (e) A taxonomia de erros como argumento para as regras da validação. Riscos raros correspondem à regra de caso fora da distribuição, e qualidade dos dados às regras de completude e defasagem (R07).

**Não se aplica**
- BIM, IoT e o LSTM, que dependem de dados semanais de obra que o agente não tem.
- A acurácia multiclasse como métrica principal.
- Os números absolutos, dado o tamanho da amostra e as incoerências apontadas.

### 4.2 Natarajan (2022) — 3,42

[*Reference Class Forecasting and Machine Learning for Improved Offshore Oil and Gas Megaproject Planning: Methods and Application*](<../materials/Natarajan et al- 2022 -reference-class-forecasting-and-machine-learning-for-improved-offshore-oil-and-gas-megaproject-planning.pdf>). Project Management Journal 53(5): 456–484. DOI 10.1177/87569728211045889.
- **Autoria**: autor único.
- **Domínio**: megaprojetos offshore de óleo e gás (plataformas flutuantes), em escala global.

**Problema.** Prever sobrecusto e atraso de cronograma no momento da decisão final de investimento (FID), corrigindo os vieses das previsões feitas pela "visão de dentro" (p. 456–457).

**Método**
1. Questionário com 26 gerentes de projeto para evidenciar vieses de previsão (p. 462).
2. Caracterização das distribuições de sobrecusto e atraso: não são normais e têm cauda pesada. O melhor ajuste é a distribuição Birnbaum–Saunders (p. 468–471).
3. Reference class forecasting (RCF) clássico, com *uplifts* por percentil de risco aceitável (p. 469; Tabela 12, p. 474).
4. Redes neurais de 2 e 4 camadas com 18 atributos conhecidos na FID, um modelo para custo e outro para prazo. A avaliação usa divisão 85:15, validação 10-fold e um teste progressivo 90:10 em que cada projeto entra uma única vez como dado novo (p. 477, 480).
5. Combinação bayesiana: a distribuição da classe de referência entra como *prior*, com peso de 50% para a previsão do modelo, e o resultado são curvas de *uplift* por projeto (p. 480).

**Dados**
- 358 projetos identificados, dos quais 130 têm dado de prazo e 106 têm dado de custo. Foram coletados em relatórios anuais, documentos de reguladores e imprensa especializada (p. 462–463).
- O desvio é medido contra o orçamento e o cronograma da FID. Mudanças de escopo materiais são **rebaselinadas** à FID (p. 459).
- Atributos ordinais (novidade tecnológica, lições aprendidas, detalhamento do FEED) foram codificados pelo autor em escala de 5 pontos (p. 464).
- Os dados não foram publicados.

**Resultados**
- **Desempenho do portfólio**: sobrecusto médio de +32,8% e atraso médio de +25,6%; 82% dos projetos atrasaram e 80% estouraram o orçamento (p. 467).
- **Custo × prazo**: a covariância entre sobrecusto e atraso é **fraca** (PCC de 0,37 no total e de 0,25 no aglomerado mais denso) (p. 472).
- **Desempenho em dados novos**:
  - MSE de 6% (prazo) e 12,2% (custo), contra 9,3% e 20,2% do RCF P50;
  - previsões dentro de ±10% do real em 40% (prazo) e 43% (custo) dos casos, contra 23% e 24% do RCF (Tabelas 14 e 15, p. 477; p. 480).
- **Outliers**: o modelo falha nos casos extremos (p. 480).

**Limitações**
- *Declaradas pelo autor*: poucos projetos, custos reais às vezes indisponíveis ou pouco confiáveis, viés de relato (projetos bem-sucedidos aparecem mais) e aproximações de datas e custos (p. 481).
- *Observadas nesta leitura*:
  - rede neural treinada com cerca de 100 casos;
  - codificação ordinal subjetiva;
  - não há calibração de probabilidade;
  - há uma única observação por projeto, feita na FID, e não ao longo da execução.

**Aproveitar no agente** *(inferência)*
- (a) **RCF como baseline do A1**: a taxa de desvio de uma classe de projetos parecidos é o teste mais direto do risco de existência de sinal (R01).
- (b) As curvas de *uplift* e a combinação bayesiana como desenho para os "comparáveis" e para a severidade (F02) (R08).
- (c) A cauda pesada justifica o corte por percentis já previsto (§3.1) e reforça que casos extremos não são previsíveis, o que sustenta as ressalvas.
- (d) **Alerta para o proxy financeiro**: a covariância fraca entre custo e prazo vale para sobrecusto, não para faturamento, então não testa o proxy diretamente. Mostra, porém, que as dimensões financeira e de prazo de um mesmo projeto podem divergir bastante. Esse é um argumento para manter modelos separados quando o alvo migrar para o cronograma (R09).

**Não se aplica**
- Os atributos específicos de óleo e gás.
- A previsão feita só na FID, já que o agente prevê durante a execução.
- Redes neurais com essa amostra.

### 4.3 Gundidza, Kikuchi e Ozono (2026) — 2,92

[*From Unstructured Reports to Exploratory Causal Modeling: A Modality-Aware AI Pipeline for Infrastructure Delay Analysis*](<../materials/Gundidza et al - 2026 - From Unstructured Reports to Exploratory Causal Modeling- A Modality-Aware AI Pipeline for Infrastructure Delay Analysis  .pdf>). Big Data and Cognitive Computing 10(8): 269. DOI 10.3390/bdcc10080269.
- **Domínio**: 55 projetos rodoviários financiados por ADB, AfDB e JICA, na Ásia e na África.

**Problema.** Transformar relatórios narrativos de avaliação em conhecimento causal sobre as causas de atraso. Os autores declaram que o objetivo é atribuição retrospectiva, **não** previsão em projetos novos (p. 3/38).

**Método**
- **Pipeline em 8 etapas** (p. 8–9/38; schema nas p. 11–12/38; algoritmos na p. 21/38):
  1. conversão do PDF para markdown;
  2. divisão em *chunks* por seção;
  3. extração por LLM em JSON. Cada evento recebe:
     - modalidade: fato confirmado, condicional, hipotético ou observação geral;
     - escopo: projeto inteiro, componente ou projeto relacionado;
     - flag de mudança de escopo e flags de recuperação;
     - aplicação da "regra de normalidade";
  4. montagem de uma matriz binária projeto × causa;
  5. aprendizado de estrutura por Hill-Climb com lista de direções proibidas, corroborado por PC, GES e FCI;
  6. do-cálculo sobre uma rede bayesiana.
- **Tipologia de seis falhas da extração ingênua** (Tabela 1, p. 10/38):
  - armadilha de modalidade;
  - armadilha temporal;
  - armadilha de escopo;
  - recuperação ignorada;
  - "superaquecimento lexical";
  - confusão com mudança de escopo.

**Dados**
- 183 eventos extraídos, dos quais 122 são fatos confirmados de escopo de projeto inteiro.
- Só 29 dos 55 projetos têm ao menos um evento confirmado (p. 7/38, 14/38).
- O pacote de reprodutibilidade está publicado no Zenodo (p. 34/38).

**Resultados**
- **Anotação humana cega** com três anotadores (p. 11/38):
  - precisão de detecção de eventos de 0,795;
  - acurácia de 0,887 na modalidade e de 0,66 no escopo;
  - acurácia de 0,50 na causa (15 classes);
  - revocação por *chunk* de 0,50;
  - concordância entre anotadores (κ) de 0,27–0,43 para a causa e próxima de zero para a modalidade.
- **Efeito do filtro**: sem o filtro de modalidade, a estrutura aprendida não compartilha nenhuma aresta com a estrutura filtrada (p. 25/38).
- **Fragilidade do efeito principal** (financeiro → gestão, ΔP = +0,638):
  - o intervalo passa a incluir zero quando se propaga a incerteza de estrutura (p. 18–19/38);
  - o efeito é recuperado por apenas 1 dos 9 modelos extratores testados (p. 20/38).
- **Não determinismo**: mesmo com temperatura 0 e semente fixa, a extração não se repete evento a evento (Jaccard por *chunk* entre 0,17 e 1,0) (p. 34/38).

**Limitações**
- Amostra efetiva de cerca de 29 projetos, viés de relato, resultados dependentes do extrator e suposições causais não testáveis (p. 32/38).
- Os autores recomendam o uso como triagem de portfólio, e não como ferramenta de decisão projeto a projeto (p. 31/38).

**Aproveitar no agente** *(inferência)*
- (a) **A tipologia de falhas se transpõe à narrativa do A2.4** (R05):
  - a armadilha temporal corresponde a confundir o desvio *observado* com o *previsto*, distinção que o próprio §3 do contexto exige;
  - a armadilha de modalidade corresponde a apresentar uma probabilidade como certeza;
  - a confusão com mudança de escopo corresponde a tratar aditivo como desvio;
  - o superaquecimento lexical corresponde ao tom alarmista.
- (b) O protocolo de avaliação humana: anotadores cegos, gabarito por maioria, κ e precisão das afirmações "confirmadas".
- (c) Arquivar as saídas do LLM, já que temperatura 0 não garante repetição.
- (d) As regras de mudança de escopo e de recuperação reforçam o desenho do alvo: plano vigente, e recuperação dentro da janela não conta (R03).
- (e) Para a V2.0, relatórios como fonte de rótulos de cronograma (R11).

**Não se aplica**
- Descoberta causal com cerca de 29 casos como base de decisão.
- LLM extraindo atributos que alimentam o modelo, sem uma decisão prévia sobre como isso convive com a regra de "LLM fora do cálculo" (R11).

### 4.4 Gao et al. (2026) — 2,58

[*Artificial Intelligence in Construction Project Management: A Systematic Literature Review of Cost, Time, and Safety Management*](<../materials/Gao et al - 2026 - Artificial Intelligence in Construction Project Management- A Systematic Literature Review of Cost, Time, and Safety Management.pdf>). Buildings 16(5): 1061. DOI 10.3390/buildings16051061.

**Problema.** Mapear as aplicações de IA na gestão de custo, prazo e segurança na construção (p. 1/34, 3/34).

**Método.** Revisão PRISMA no Scopus (2013 a janeiro de 2026), restrita a periódicos revisados por pares e em inglês. Dois revisores, checklist de qualidade com corte de 70% e *snowballing* (p. 4–7/34).

**Dados.** 392 artigos (p. 7/34).

**Resultados** (os relevantes ao agente)
- **Áreas de aplicação em prazo**: planejamento, predição de risco de atraso, otimização e tempo de ciclo (p. 17/34).
- **Predição de atraso**:
  - Gondia et al. (árvore de decisão e Naive Bayes) obtêm **47,2% e 51,2% de acurácia no teste**, contra 74,5% e 78,4% no treino;
  - Shirazi e Toosi (MLP profunda) obtêm 94,36% em barragens iranianas (p. 18/34).
- **Valor agregado**: Mohammed et al. preveem SPI, CPI e TCPI com MLR, ANN e SVM (p. 16/34).
- **Diagnóstico dos autores**:
  - os estudos de predição de atraso usam bases pequenas e específicas, priorizam acurácia sobre interpretabilidade, e a conversão da predição em ação é pouco explorada (p. 19/34);
  - as aplicações de custo e prazo são validadas em dados retrospectivos e estão longe da implantação (p. 25–26/34).

**Limitações**
- *Declaradas*: só Scopus, só inglês, só periódicos (p. 29/34).
- *Observadas nesta leitura*:
  - as métricas são relatadas sem crítica (ex.: R² = 1,0 e RMSE = 0 numa regressão ridge, p. 14/34);
  - as contagens da triagem divergem entre o texto e a Tabela 2 (5.873, depois 3.611, depois 3.911; p. 5–6/34);
  - não há discussão de vazamento.

**Aproveitar no agente** *(inferência)*
- Pistas de busca (§7).
- O diagnóstico de bases pequenas e retrospectivas reforça a validação temporal e o uso de projetos separados para teste.
- A diferença entre treino e teste em Gondia et al. é um exemplo citável do otimismo que a validação do agente evita.

**Não se aplica**
- As propostas de agentes LLM para cronograma (p. 27–28/34), que contrariam a separação de camadas.
- A parte de segurança.

### 4.5 Pal, Murguia e Middleton (2024) — 2,08

[*Automatic Inference of Construction Delays through Analysis of Weekly Progress Reports Using LLMs*](<../materials/Pal et al - 2024 - Automatic Inference of Construction Delays through Analysis of Weekly Progress Reports Using LLMs.pdf>). CIB W78 2024, Marrakesh (anais de congresso; as páginas citadas são do PDF).
- **Domínio**: um edifício comercial em Londres.

**Problema.** Identificar e classificar as causas de atraso registradas em relatórios semanais de obra e visualizar o impacto delas no cronograma (p. 1–2).

**Método**
- O gpt-3.5-turbo-0125 extrai do relatório, em JSON, a data, o atraso da semana, o **atraso acumulado** e o baseline (p. 3–4).
- O mesmo modelo classifica cada problema em 10 categorias (Tabela 1, p. 5).
- Linhas de balanço comparam o planejado e o realizado (p. 4).
- O atraso da semana é dividido entre as causas na proporção das ocorrências (p. 7).

**Dados.** 44 relatórios semanais de um único projeto (88 semanas previstas), com 562 problemas identificados. **O baseline foi revisado na semana 60** (p. 5).

**Resultados.**
- Em 157 problemas rotulados manualmente: precisão de 0,91, revocação de 0,97 e F1 de 0,93, em média por classe (p. 6, 8).
- Atraso acumulado de 87 dias na semana 59 (p. 5).

**Limitações** *(observadas nesta leitura)*
- Um único projeto.
- O paper não informa quem rotulou o conjunto de validação nem com que concordância.
- Não há baseline de comparação.
- A atribuição proporcional do atraso às causas é heurística.
- O LLM é proprietário; os autores propõem modelos abertos ajustados como trabalho futuro (p. 9).

**Aproveitar no agente** *(inferência)*
- Para a V2.0: relatórios de progresso como fonte do atraso de cronograma real, tanto como rótulo quanto como atraso acumulado (R11).
- A revisão do baseline na semana 60 é um caso concreto do problema do plano vigente (A03, R03).

**Não se aplica** ao MVP: os dados previstos não incluem relatórios textuais, e o paper não tem componente preditivo.

### 4.6 Edeh et al. (2026) — 2,08

[*Integration of Digital Twin Platforms with Machine Learning Models for Early Detection of Project Delays and Cost Overruns*](<../materials/Edeh et al - 2026 - Integration of Digital Twin Platforms with Machine Learning Models for Early Detection of Project Delays and Cost Overruns.pdf>). Asian Journal of Advanced Research and Reports 20(1): 332–349. DOI 10.9734/ajarr/2026/v20i11271.
- **Tipo**: revisão sistemática.

**Problema.** Avaliar se gêmeos digitais combinados com ML melhoram a detecção precoce de atraso e sobrecusto (p. 333–334).

**Método.** Busca no Scopus, com VOSviewer e PRISMA (p. 337–339).

**Dados.** 51 estudos (p. 333).

**Resultados**
- Classifica os modelos em três tipos (p. 339–340, 344):
  - caixa-branca: simulação e regras;
  - caixa-preta: ANN, RF, SVM, LSTM;
  - caixa-cinza: híbridos com gêmeo digital.
- A validação em projetos reais é rara; predominam simulação e estudos de projeto único (p. 344).
- Lacunas apontadas: validação externa, comparação entre ML e deep learning em dados temporais e gêmeos digitais de portfólio (p. 345).

**Limitações** *(observadas nesta leitura)*
- As contagens PRISMA são impossíveis: 182 registros viram 813 após a remoção de duplicatas (p. 339).
- O gráfico de distribuição anual não tem sentido (p. 339).
- Não há extração por estudo: nenhuma tabela traz dados, métricas ou validação de cada trabalho.
- As afirmações são gerais e não trazem números.

**Aproveitar no agente** *(inferência)*. Apenas como pano de fundo para o posicionamento: falta de validação externa e de dados temporais.

**Não se aplica.** Gêmeo digital, BIM e IoT, porque o agente não tem esses dados.

### 4.7 Sun et al. (2025) — 2,00

[*A review of network delay prediction and advances in large language models for air traffic*](<../materials/Sun et al - 2025 - A review of network delay prediction and advances in large language models for air traffic.pdf>). Artificial Intelligence Review 59:36 (2026; publicado online em 2025-12-16). DOI 10.1007/s10462-025-11400-w.
- **Domínio**: análogo — atraso de voos numa rede de aeroportos.

**Problema.** Revisar os métodos de previsão de atraso propagado em redes aéreas e propor um LLM específico para o domínio (p. 1–5/43).

**Método**
- Busca no Web of Science (1990–2025): 876 registros, dos quais 110 artigos foram analisados e outros 35 usados na discussão de desafios (p. 5/43).
- Proposta conceitual do STC-LLM, que combina uma GCN causal baseada em entropia de transferência, uma GRU e um LLM ajustado (p. 30–32/43).

**Resultados**
- **Definição de atraso**: fixada por convenção institucional, com limiar de 15 minutos (DOT, EUROCONTROL, CAAC) (p. 2/43).
- **Tipos de atraso**: separação entre atraso inicial e atraso propagado (p. 2/43).
- **Métodos**: causalidade de Granger, entropia de transferência, algoritmo PC e redes em grafo para modelar a propagação (p. 11–19/43).
- **Dados e reprodutibilidade**: a base pública BTS é amplamente usada, mas o código quase nunca é publicado (p. 6/43, 20/43).
- **LLMs**: lidam mal com dados estruturados numéricos e exigem camadas de tradução (p. 26/43). Os autores propõem uso com humano no circuito e incerteza calibrada (p. 33/43).
- **Limites dos LLMs**: privacidade, opacidade, latência e custo (p. 34–35/43).

**Limitações.** O STC-LLM não tem validação experimental (p. 1/43, 36/43), e a revisão não relata critérios de qualidade.

**Aproveitar no agente** *(inferência)*
- (a) **Contraponto citável**: o próprio campo que propõe LLM na previsão reconhece a fragilidade dele com números e a necessidade de tradução e de humano no circuito. Isso reforça a separação de camadas e a projeção em faixas.
- (b) O limiar fixado por convenção institucional é precedente para um limiar de 10% definido pelas áreas de negócio.
- (c) A distinção entre atraso inicial e propagado, e os métodos de causalidade, para a V3.0 (propagação no portfólio, R12).

**Não se aplica**
- O STC-LLM, que coloca o LLM no cálculo, antipadrão do agente.
- Dados de alta frequência e infraestrutura de GPUs.

### 4.8 Zahedi e Golchin (2024) — 0,92

[*Prediction of blast loading on protruded structures using machine learning methods*](<../materials/Zahedi et al - 2024 - Prediction of blast loading on protruded structures using machine learning methods.pdf>). International Journal of Protective Structures 15(1): 122–140. DOI 10.1177/20414196221144067.

**Problema.** Prever a pressão de pico e o impulso de explosões sobre fachadas com saliência, a partir de simulações CFD (p. 122).

**Método e dados.** 1.287 simulações no ProSAir, com mais de 250 mil pontos. Divisão aleatória 80/20 e busca aleatória de hiperparâmetros com validação 5-fold (p. 125, 127).

**Resultados.** GBDT e XGBoost (R² entre 0,998 e 1,000) superam ANN, RF e regressão polinomial. Importância de atributos por permutação (Tabela 3, p. 134; p. 135).

**Limitações.** Dados simulados e divisão aleatória, o que é aceitável para simulação, mas não para séries de projetos.

**Aproveitar no agente** *(inferência)*. No máximo, mais um caso em que boosting supera redes neurais em dados tabulares. A evidência é fraca e vem de outro domínio.

**Não se aplica.** O problema inteiro. Ver o §8 sobre a provável inclusão por engano.

---

## 5. Decisões provisórias × corpus

Confronto com as decisões listadas no §6.4 do contexto.

| Decisão | Veredito do corpus | Base |
|---|---|---|
| Faturamento como proxy de atraso | **Não trata** | Nenhum paper usa faturamento. Natarajan mostra covariância fraca entre sobrecusto e atraso (p. 472). *(Inferência: as dimensões financeira e de prazo podem divergir, então o proxy precisa de teste empírico)* |
| Limiar de 10% | Apoio parcial | Bai usa estouro de orçamento acima de 10% como alvo binário (p. 530, 533) e cita outro estudo com o mesmo corte (p. 527). Vale para custo, não para faturamento. Em Sun, os limiares de atraso são fixados por convenção institucional (p. 2/43) |
| Horizonte de 3 meses | **Não trata** | O maior horizonte avaliado no corpus é de 8 semanas, com erro crescente (Bai, Tabela 4, p. 533) |
| Medida acumulada contra o plano vigente, avaliada no fim da janela | Apoio parcial | Natarajan rebaselina as mudanças de escopo (p. 459). Gundidza separa do atraso as mudanças de escopo aprovadas e os atrasos recuperados (p. 10–12/38). Pal registra uma revisão de baseline (p. 5) |
| Uma observação por projeto por período | Apoia | Bai usa pontos de controle quinzenais e janelas deslizantes (p. 529–530) e cita um estudo em que a granularidade mensal aumentou o número de observações, mas não a diversidade de situações (p. 527) |
| Validação temporal; últimos meses sem rótulo | **Não trata** | Nenhum paper faz divisão temporal. Bai separa projetos para teste (p. 530–531) e critica a validação cruzada numa base única (p. 526). Natarajan (p. 477) e Zahedi (p. 127) usam divisão aleatória |
| Atributos essenciais (desvio de faturamento de 3 meses, desvio de margem) | Apoio parcial | Desvio acumulado, volatilidade financeira e número de mudanças lideram a importância de atributos (Bai, p. 532–533). O desvio de margem não aparece no corpus |
| Completude mínima de 80% | Apoia a regra, não o valor | Completude acima de 95% acrescenta 13,2 pontos percentuais de acurácia (Bai, Tabela 11, p. 535) |
| Modelo linear como referência contra árvores e boosting | Apoia | Bai compara com regressão linear, regressão logística, extrapolação ingênua e especialistas (p. 533–534). Natarajan usa o RCF como referência (p. 477) |
| SHAP como exigência do contrato | **Não trata** | Bai observa que nenhum dos estudos de deep learning que revisa usa XAI (p. 527). Bai e Zahedi usam apenas importância de atributos |
| Fora da distribuição 0,6/0,8; defasagem de 2/4 meses; salto de 40 pontos | Apoia a existência das regras, não os valores | Riscos raros ausentes do treino respondem por 20,8% dos erros, e atualização mais espaçada piora o erro (Bai, p. 535). Casos extremos são imprevisíveis (Natarajan, p. 480) |
| Valores sempre em faixa; o LLM só recebe a projeção | Não trata diretamente | Apoio indireto: LLMs são frágeis com dados numéricos (Sun, p. 26/43), e Gundidza usa extração estruturada com filtro de modalidade (p. 10–12/38) |
| Hipótese de contribuição (§6.8) | Não contradita | Nenhuma fonte reúne predição com validação temporal, camada de validação e ponte determinística para o LLM |

---

## 6. Recomendações para o agente

A ordem é por prioridade: primeiro alto impacto com baixo esforço, depois o resto. Cada linha indica se a mudança é um **reforço** de decisão existente ou uma **mudança de paradigma**.

| ID | O que mudaria (componente) | Sustentação | Impacto esperado | Esforço | Riscos | Tipo |
|---|---|---|---|---|---|---|
| R01 | **Benchmark A1**: incluir dois baselines além do linear. (i) **Persistência**: o desvio atual se mantém ou segue a tendência. (ii) **Taxa de base por classe de referência** (segmento × faixa de valor × tipo de contrato). O modelo só demonstra ter sinal se superar os dois | Bai, Tabelas 5 e 8 (p. 533–534); Natarajan, RCF e Tabelas 14–15 (p. 474, 477) | **Alto**: transforma o risco de existência de sinal num teste explícito | Baixo | A classe de referência exige histórico de projetos encerrados; com poucos projetos, as classes ficam grosseiras | Reforço |
| R02 | **Protocolo de validação**: combinar a divisão temporal com a divisão por projeto (projetos de teste nunca aparecem no treino) e relatar as métricas por fase e idade do projeto, o que dá a curva de antecedência | Bai: projetos separados para teste (p. 530–531), acurácia por % de execução (Tabela 10, p. 534) e crítica à validação cruzada (p. 526); Gao: diferença treino × teste em Gondia et al. (p. 18/34) | **Alto**: estimativa realista do desempenho e da antecedência | Baixo | Menos dados de treino; poucos projetos em cada fase | Reforço |
| R03 | **Regras de rotulagem**: explicitar (a) a data de referência do plano vigente quando um aditivo é aprovado dentro da janela (A03); (b) que uma revisão de baseline sem aditivo aprovado não redefine o plano vigente (a confirmar com o negócio); (c) que a recuperação dentro da janela não conta, como já previsto | Gundidza, falhas de mudança de escopo e de recuperação (Tabela 1, p. 10/38; p. 12/38); Natarajan, rebaseline de escopo à FID (p. 459); Pal, baseline revisado na semana 60 (p. 5) | **Alto**: evita rótulo ambíguo e o vazamento causado por um aditivo futuro entrar no rótulo | Baixo | Depende de decisão das áreas de negócio | Reforço |
| R04 | **Atributos**: acrescentar a tendência (inclinação) e a volatilidade (desvio-padrão) do desvio de faturamento nas janelas móveis, além da contagem de mudanças contratuais recentes | Bai, janelas com média, tendência e volatilidade (p. 530); importância de atributos (p. 532–533) | Médio | Baixo | Com dados mensais, uma janela de 3 meses tem só 3 pontos, e inclinação e desvio-padrão ficam ruidosos. Testar janelas de 6 a 12 meses | Reforço |
| R05 | **Teste de fundamentação (A2.4)**: adotar a tipologia de falhas de Gundidza, adaptada à narrativa (modalidade, temporal, escopo/aditivo, superaquecimento lexical), e o protocolo de anotação (revisores cegos, gabarito por maioria, κ). Rodar a narrativa com mais de um LLM e arquivar as saídas | Gundidza, Tabela 1 (p. 10/38), anotação (p. 11/38), comparação entre extratores (p. 20/38) e não determinismo (p. 34/38) | **Alto** para o A2.4 e para a publicação | Médio | A tipologia foi criada para extração, não para geração; precisa de adaptação e de um piloto | Reforço |
| R06 | **Gerador sintético do A1**: marginais empíricas escolhidas por teste de aderência, correlação por Cholesky e cauda pesada (Birnbaum–Saunders) para os desvios. Validar com teste de aderência e com a diferença entre as matrizes de correlação. Gerar trajetórias projeto-mês, e não linhas independentes | Bai (p. 529); Natarajan (p. 468–471, Tabela 11) | Médio: permite testar o pipeline, a validação temporal e as regras da validação | Médio | **Dado sintético não testa a existência de sinal**, porque o sinal é o que o gerador coloca. Há risco de viés estrutural (Bai, p. 536) | Reforço |
| R07 | **Camada de validação**: calibrar os limites provisórios (completude, defasagem, caso fora da distribuição) com curvas de desempenho × nível de cada sinal no benchmark, em vez de fixá-los a priori | Bai, Tabelas 11 e 12 (p. 535) | Médio | Médio | O benchmark sintético não reproduz as falhas reais de dados | Reforço |
| R08 | **Visão de fora**: combinar a probabilidade do modelo com a distribuição da classe de referência e usar curvas de *uplift* por percentil para os comparáveis e para a severidade (F02, adiada) | Natarajan, combinação bayesiana e curvas (p. 480, Fig. 22, Tabela 17) | Médio a alto: severidade com intervalo e comparáveis com base declarada | Alto | Exige histórico de encerrados (não confirmado); Natarajan fixa o peso da previsão do modelo em 50% sem justificar (p. 480) | **Mudança de paradigma** (parcial) |
| R09 | **V2.0**: manter modelos separados para o alvo financeiro e para o alvo de cronograma, em vez de trocar um pelo outro | Bai: um modelo único perde de 12% a 18% de acurácia (p. 535); Natarajan: covariância fraca entre custo e prazo (p. 472) | Médio | Médio | Duas pipelines para manter; a validação e a narrativa precisam distinguir os dois alvos | Reforço |
| R10 | **Classes de criticidade**: avaliar, na operação assistida, limiares diferentes por fase do projeto | Bai, "calibração dinâmica" por fase (p. 535–536) | Baixo a médio | Baixo | Com probabilidade calibrada e a fase como atributo, limiares por fase podem ser redundantes, e complicam a explicação ao gestor | Reforço (ajuste) |
| R11 | **V2.0**: usar relatórios de progresso como fonte de rótulos de cronograma e de sinais de execução, via extração por LLM com filtro de modalidade. As saídas seriam validadas, congeladas e auditadas antes de entrar no modelo | Pal (p. 3–8); Gundidza (p. 10–12/38, 20/38) | Alto potencial: viabiliza o rótulo de cronograma real | Alto | **Choca com a regra "LLM fora do cálculo"** e exige decisão explícita de negócio. O ruído de extração é alto (acurácia de 0,50 na causa e revocação de 0,50) e depende do modelo usado | **Mudança de paradigma** |
| R12 | **V3.0**: modelar a propagação de impacto entre projetos do portfólio com métodos causais (Granger, entropia de transferência) ou redes bayesianas | Sun (p. 11–19/43, 26–28/43); Gundidza (p. 18–21/38) | Incerto | Alto | Estruturas instáveis com amostras pequenas (Gundidza, p. 18–19/38); suposições causais não testáveis | **Mudança de paradigma** |

**Descartadas**
- LLM no cálculo da previsão: o STC-LLM (Sun, p. 30–32/43) e os agentes LLM de cronograma (Gao, p. 27–28/34). É o antipadrão do agente.
- Gêmeo digital, BIM e IoT (Edeh; Bai): o agente não tem esses dados.

---

## 7. Lacunas da literatura

Aspectos do agente que nenhum paper do corpus cobre bem. Os termos sugeridos alimentam uma nova rodada pelo `/literature-review`, com aprovação por item (G4).

| ID | Aspecto do agente | O que o corpus tem | Termos de busca sugeridos |
|---|---|---|---|
| L01 | Faturamento como proxy de atraso | Nada | `"progress billing" AND (delay OR "schedule slippage")`; `"milestone payment" AND "schedule performance"`; `"cash flow forecasting" AND construction AND "machine learning"`; `"S-curve" AND deviation AND prediction`; `medição de obra atraso`; `faturamento atraso de cronograma` |
| L02 | Horizonte de previsão e antecedência do alerta | Bai, até 8 semanas | `"early warning" AND "lead time" AND (overrun OR delay) AND project`; `"forecast horizon" AND "earned schedule"`; `"survival analysis" AND "project delay"`; `"dynamic prediction" AND "project completion"` |
| L03 | Validação temporal e vazamento | Nada | `("temporal validation" OR "out-of-time") AND "project performance prediction"`; `"data leakage" AND construction AND "machine learning"`; `"grouped cross-validation" AND projects`; `"rolling origin" AND evaluation` |
| L04 | Calibração de probabilidade | Nada | `"probability calibration" AND (risk OR overrun) AND classifier`; `"Brier score" AND project`; `("isotonic regression" OR "Platt scaling") AND construction` |
| L05 | Desbalanceamento e métricas adequadas | Bai nota F1 menor na classe rara (p. 532) | `"precision-recall" AND imbalanced AND "cost overrun"`; `SMOTE AND "construction cost overrun"` |
| L06 | SHAP em risco de projeto | Nada | `SHAP AND ("cost overrun" OR "schedule delay" OR "project risk")`; `"explainable AI" AND "construction project" AND prediction` |
| L07 | Caso fora da distribuição e abstenção | Nada | `"applicability domain" AND "machine learning"`; `"out-of-distribution detection" AND tabular`; `("selective prediction" OR "reject option") AND classifier`; `"dataset shift" AND "project data"` |
| L08 | LLM que narra a saída de um modelo de ML | Nada | `"natural language explanation" AND SHAP AND LLM`; `"narrative explanation" AND "machine learning predictions"`; `"data-to-text" AND faithfulness AND numbers`; `"numerical hallucination" AND LLM` |
| L09 | Dados públicos em formato projeto-período | Nada utilizável: Natarajan não publica os dados, e Sun cita a BTS, que é de voos | `"project dataset" AND "earned value" AND public`; `"construction project database" AND open`; `"public procurement" AND "contract amendments" AND dataset`; `dados abertos obras públicas aditivos` |
| L10 | Aditivos e *change orders* como preditores | Bai, contagem de mudanças (p. 532–533) | `"change orders" AND predictor AND (overrun OR delay) AND "machine learning"`; `"contract amendments" AND "public works" AND delay`; `aditivos contratuais atraso obras públicas` |
| L11 | Projetos de serviços de engenharia e consultoria | Nada: o corpus cobre construção, óleo e gás e aviação | `"engineering services" AND project AND overrun`; `"professional services" AND "project profitability" AND prediction`; `"IT projects" AND "budget overrun" AND prediction` |
| L12 | Uso e aceitação dos alertas pelos gestores | Bai, fatores organizacionais (p. 535) | `"early warning system" AND "project portfolio" AND adoption`; `"decision support" AND "project managers" AND trust AND prediction` |

**Pistas citadas dentro do corpus.** Estas obras não foram lidas e não entram no `references.bib` sem passar pelo Crossref (G1):
- Coffie e Cudjoe (2024): XGBoost para estouro de orçamento acima de 10%, com SMOTE, em 135 projetos em Gana. Citado por Bai, p. 527.
- Gondia et al. (2020): predição de risco de atraso em construção. Citado por Pal e por Gao, p. 18/34.
- Ishdorj et al. (2025): LLMs para prever atraso de cronograma. Citado por Gundidza, p. 4/38.
- Batselier e Vanhoucke (2016): RCF comparado com valor agregado e Monte Carlo. Citado por Natarajan, p. 459.
- Mohammed et al. (2022): previsão de SPI e CPI. Citado por Gao, p. 16/34.
- Espinoza e Presbitero (2022): atrasos em investimentos públicos. Citado por Gundidza, p. 1–2/38.

---

## 8. Observações sobre o corpus

- **Zahedi e Golchin (2024) está fora do tema.** *(Hipótese)* O paper deve ter entrado por homonímia. Edeh et al. citam "Zahedi et al., 2024" (p. 335), mas a lista de referências mostra que a obra é outra: Zahedi, Alavi, Majrouhi Sardroud e Dang, *Digital twins in the sustainable construction industry*, Buildings 14(11): 3613. Sugestão: retirar o PDF atual e, se o tema interessar, buscar o paper correto pelo fluxo de busca.
- **Os PDFs não passaram pelo `/process-materials`**: não há resumos, `references.bib` nem `deliverables/papers/`. Alguns nomes de arquivo fogem da convenção:
  - "Natarajan et al-", para um autor único;
  - "Zahedi et al", para dois autores;
  - espaços extras no nome do PDF de Gundidza.
  Nada foi renomeado nesta tarefa.
- **O tema não tem `context.md`**. O papel dele é cumprido por `project-context-and-literature-review.md`.
- **Incoerências internas** estão anotadas nas fichas: Bai (divisão treino/teste; 89% × 68,3%), Edeh (contagens PRISMA) e Gao (contagens da triagem).
