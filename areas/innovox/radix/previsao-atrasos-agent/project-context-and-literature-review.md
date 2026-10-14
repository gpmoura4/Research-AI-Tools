# A4 — Briefing da revisão de literatura (Agente de Previsão de Atraso)

> Documento de partida da atividade **A4.1–A4.4 Previsão de Atraso — revisão de literatura (predição de atraso em projetos de engenharia)** de [`tasks.md`](../../tasks.md). Resume o agente, o que já está definido e o que a revisão precisa responder. Escrito para ser lido sem acesso ao repositório: as seções 1 a 5 bastam para entender o projeto, e a seção 6 descreve a tarefa. Situação em 2026-10-09. Antecede o protocolo formal de busca (A4.1).

## 1. O projeto em um parágrafo

A plataforma **CORTEX** é um copiloto de gestão de projetos. Três agentes de IA fazem parte dela: **Boas Práticas** (memória curada de práticas recomendadas, consultada por RAG), **Geração de EAP/WBS** (propõe a estrutura analítica de um projeto a partir do escopo) e **Previsão de Atraso**, objeto desta revisão. Uma equipe de co-execução, da qual esta revisão faz parte, especifica contratos, faz benchmarks e revisões de literatura. A integração em produção fica com a Squad de IA da organização. O projeto prevê uma **publicação científica** que reúna as contribuições dos três agentes.

## 2. O Agente de Previsão de Atraso

### 2.1 Objetivo

Acompanhar os projetos ativos do portfólio, identificar **sinais precoces de risco** e estimar a **probabilidade de desvio antes que ele vire impacto financeiro ou contratual**. O gestor recebe um número (probabilidade), uma classe de criticidade com ação sugerida, os fatores que mais pesaram e uma explicação em linguagem natural.

### 2.2 Princípio central: separação de camadas

O desenho tem um princípio **não negociável**: o cálculo do risco e a explicação em texto ficam em componentes separados.

| Camada | O que faz | O que **não** faz |
|---|---|---|
| **Preditiva** | Modelo de aprendizado de máquina supervisionado sobre dados tabulares. Calcula probabilidade, classe, tendência e a contribuição de cada atributo | Não usa LLM em nenhum ponto do cálculo. É determinística e auditável |
| **Validação** | Verifica, por regras fixas, se o resultado é confiável o bastante para virar texto | Não usa LLM. Não altera o número |
| **Generativa** | Um LLM transforma o resultado já validado em explicação e recomendação para o gestor | Não acessa a base, não recalcula, não decide e não menciona valor ou fator que não recebeu |

Juntar as duas coisas, por exemplo deixando o LLM calcular o risco ou ler os dados diretamente, é tratado como **antipadrão rejeitado**. Como o agente atua em gestão financeira de projetos, a meta de **fundamentação total** (nenhuma afirmação da narrativa sem base no resultado do modelo) é tratada como requisito de segurança.

### 2.3 Funcionalidades previstas

| Código | Funcionalidade | Situação no MVP |
|---|---|---|
| F01 | Monitoramento contínuo: recálculo diário, relatório semanal de tendência, reanálise sob demanda | MVP |
| F02 | Predição por modelo supervisionado: probabilidade calibrada, tendência e, mais adiante, severidade (magnitude esperada do desvio) | MVP, severidade adiada |
| F03 | Classificação de criticidade (Baixo / Médio / Alto / Crítico) por limiares configuráveis | MVP |
| F04 | Explicabilidade em dois níveis: técnica (contribuição de atributos) e narrativa (texto do LLM) | MVP |
| F05 | Recomendações preventivas e corretivas | MVP: só a ação da classe e os atributos dominantes. V1.0: práticas recuperadas do Agente de Boas Práticas |
| F06 | Painel: ranking de risco, mapa de calor do portfólio, tendência por projeto | MVP |
| F07 | Consulta conversacional pelo copiloto, sobre o resultado da última execução | MVP |

### 2.4 Indicadores de qualidade definidos

Precisão e revocação (entre os sinalizados, quantos se confirmaram; entre os que desviaram, quantos foram sinalizados), **antecedência** do alerta em relação ao desvio confirmado, utilização do painel pelos gestores e fundamentação da narrativa.

## 3. Definições conceituais já fixadas

Estas definições já valem no projeto. Parte delas é provisória e pode mudar com o que a revisão encontrar (seção 6.4).

| Conceito | Definição adotada |
|---|---|
| **Atraso (fenômeno de interesse)** | O interesse final é atraso de cronograma. No MVP ele é medido por um **proxy financeiro**: marco não entregue não é faturado, então o atraso aparece no faturamento. Atraso medido no cronograma real fica para a V2.0 |
| **Variável-alvo (MVP)** | Binária. **"Sim"** quando, **no fim de um horizonte de 3 meses**, o faturamento **acumulado** do projeto está **10% ou mais abaixo** do previsto no **plano vigente** (o plano com os aditivos aprovados). Faturamento acima do previsto não conta, e desvio menor que 10% é tratado como oscilação. Definição **provisória** (v0.1, 2026-10-07), a confirmar com as áreas de negócio |
| Por que acumulado, plano vigente e fim da janela | Um mês ruim compensado depois não é atraso. Mudança de escopo aprovada pelo cliente não é desvio (e aditivos já entram como atributo de risco). Recuperação dentro da janela não conta, e a frase ao gestor ganha uma data ("até dezembro") |
| **Desvio observado × desvio previsto** | O desvio de faturamento **já ocorrido** é **atributo** (entrada do modelo). O desvio **daqui a 3 meses** é o **alvo**. São coisas distintas e não devem ser confundidas |
| **Unidade de observação** | **Uma observação por projeto por período** (mês), e não uma por projeto. O mesmo projeto aparece várias vezes ao longo da vida |
| **Probabilidade calibrada** | A probabilidade deve significar frequência: 50% quer dizer "metade dos projetos nessa situação desvia". Por isso, probabilidade próxima de 50% **não** é tratada como baixa confiança |
| **Classe de criticidade** | Baixo (verde, monitoramento padrão), Médio (amarelo, revisão periódica), Alto (laranja, reunião de contingência e plano de mitigação), Crítico (vermelho, alerta imediato e escalada). Limiares provisórios de exemplo: 0,25 / 0,50 / 0,75, a calibrar com as áreas de negócio depois de um período de operação assistida |
| **Tendência** | Variação da probabilidade em relação ao período anterior (sobe, estável, desce) |
| **Severidade** | Magnitude esperada do desvio, com intervalo. **Opcional no MVP**, porque o alvo é binário. Regressão de magnitude (ex.: dias de desvio) fica para depois |
| **Comparáveis** | Outros projetos parecidos com desfecho conhecido. **Opcional no MVP**: depende de histórico de projetos encerrados, ainda não confirmado |
| **Contribuição de atributo** | Quanto cada atributo empurrou o resultado para cima ou para baixo. O contrato exige **contribuições aditivas** de todos os atributos (valor base + soma das contribuições = saída bruta do modelo), o que restringe os explicadores a métodos aditivos, como SHAP |
| **Registro preditivo × projeção narrativa** | O resultado tem duas versões. O **registro** é completo (valores brutos, contribuições, versões, sinais de qualidade) e serve à auditoria e à validação. A **projeção** é a única coisa que o LLM recebe. É derivada do registro por código determinístico, com valores numéricos em **faixas** (ex.: "mais de 10% e até 20% abaixo do previsto") e nunca exatos, porque indicadores financeiros só podem ser mostrados ao usuário em faixa |
| **Validação em três estados** | **Liberado**, **liberado com ressalvas** (o texto é obrigado a mencionar cada ressalva) ou **bloqueado** (sem texto; o gestor vê número, classe e motivo, e o alerta crítico dispara mesmo assim). Regras: atributos essenciais presentes, completude mínima, atributos ausentes, **caso fora da distribuição de treino**, defasagem dos dados e salto brusco de probabilidade. Todos os limites são provisórios |
| **Validação temporal** | Obrigatória. Treino e teste são separados no tempo, nunca ao acaso, porque a separação aleatória deixa o modelo aprender com o futuro. Os últimos 3 meses de cada projeto ficam sem rótulo, e treino e teste não podem compartilhar janelas de horizonte |

### 3.1 Atributos candidatos e engenharia de atributos

- **Atributos candidatos** (catálogo ilustrativo; o real sai da A1.1): desvio de faturamento em janelas móveis (ex.: últimos 3 meses); instabilidade contratual (quantidade e variação de aditivos em 12 meses); desvio de margem ao longo do tempo; idade e fase do projeto; tipo de contrato, segmento e metodologia de gestão; faixa de valor contratado (proxy de complexidade, sempre em faixa).
- **Etapas obrigatórias**: janelamento temporal (defasagens e janelas deslizantes); normalização pelo contexto (o mesmo desvio relativo pesa diferente conforme o porte); tratamento de extremos por corte em percentis, sem remover observações informativas; transformação logarítmica de valores assimétricos; codificação de categóricos.
- **Algoritmos candidatos** (a decidir por benchmark na A1): modelo linear como referência, comitê de árvores e gradient boosting.

## 4. O que já foi feito e o que falta

| Atividade | Situação |
|---|---|
| A2.1 Contrato do resultado preditivo (registro, projeção, variável-alvo) | Concluída. Especificação e código com schemas versionados e testes |
| A2.2 Camada de validação (três estados, seis regras) | Concluída. Limites provisórios |
| A2.3 Instrução da camada generativa (restrições do LLM) | A fazer |
| A2.4 Teste de fundamentação com amostra revisada por humano | A fazer |
| A2.5 Consolidação do protocolo entre camadas | A fazer |
| A1.1–A1.7 Benchmark de modelos (atributos, validação temporal, métricas para dados desbalanceados, comparação de modelos, explicabilidade, registro, relatório) | A fazer. Será feito sobre **dados sintéticos ou públicos equivalentes** enquanto não houver autorização para dados reais |
| **A4.1–A4.4 Revisão de literatura** | **Esta tarefa** |
| A5 Séries temporais | Ciclo posterior e condicional |

**Risco central do agente:** não é de engenharia, porque camadas, validação temporal, explicabilidade e painel usam técnicas maduras. O risco é de **existência de sinal**: não se sabe se atributos financeiros e contratuais preveem desvio de faturamento com utilidade prática. Além disso, ainda não foi confirmado que existe histórico financeiro e contratual suficiente para treinar.

## 5. Escopo do agente

### 5.1 Dentro do MVP

Classificador supervisionado com alvo financeiro binário, atributos tabulares do histórico, explicabilidade por contribuição de atributos, validação, narrativa pré-calculada em lote, painel, alerta de classe crítica e registro de modelos e experimentos.

### 5.2 Fora do MVP (evolução prevista)

| Ciclo | Capacidades |
|---|---|
| V1.0 | Séries temporais, atributos de esforço, recomendações por RAG sobre Boas Práticas, simulação de cenários, alerta de tendência crescente |
| V2.0 | Sinais de progresso de execução, migração do alvo para o **cronograma real**, regressão de **dias de desvio**, previsão de impacto financeiro |
| V3.0 | Recomendação automática de ações, aprendizado contínuo com retorno dos gestores, **propagação de impacto entre projetos do portfólio** |

### 5.3 Fora de escopo em qualquer ciclo

LLM no cálculo do risco; LLM com acesso direto à base; valores financeiros exatos mostrados ao usuário; integração com o ambiente de produção pela equipe de co-execução.

## 6. A tarefa: revisão de literatura (A4.1–A4.4)

### 6.1 Objetivo

Mapear como a literatura científica e a prática **definem, modelam, avaliam e explicam** a predição de atraso em projetos de engenharia e em domínios análogos, e confrontar isso com as decisões já tomadas (seção 3). Interessam tanto **técnicas e abordagens teóricas** quanto **sistemas práticos e estudos de caso**. Se não houver literatura sobre algum ponto, isso também é achado e deve ser registrado como lacuna.

A revisão tem três usos:

1. **Embasar ou contestar** as definições provisórias (alvo, horizonte, limiar, atributos, regras de validação) antes do benchmark A1.
2. **Desenhar o benchmark A1**: modelos, validação temporal, métricas e, sobretudo, **conjuntos de dados públicos** que substituam os dados reais ainda indisponíveis.
3. **Posicionar a contribuição científica**: o que no desenho do agente é novo em relação ao que já foi publicado.

### 6.2 Entregáveis (mesmo formato das revisões A4 dos outros dois agentes)

| # | Subtarefa | Entregável |
|---|---|---|
| A4.1 | Definir escopo de busca, perguntas de pesquisa e termos-chave | Protocolo de busca |
| A4.2 | Levantar e priorizar fontes revisadas por pares, sinalizando materiais preliminares | Lista de fontes triadas, com data de corte e bases cobertas |
| A4.3 | Sintetizar os achados relevantes ao desenho do agente | Síntese estruturada por pergunta de pesquisa |
| A4.4 | Redigir o relatório final e identificar a contribuição para a publicação científica | Relatório de revisão de literatura |

### 6.3 Perguntas de pesquisa propostas (ponto de partida para a A4.1)

| # | Pergunta | Informa |
|---|---|---|
| **PR1 — Conceito e variável-alvo** | Como a literatura conceitua e **operacionaliza** atraso e desvio em projetos de engenharia: cronograma, custo, faturamento, indicadores de valor agregado (SPI, CPI, *earned schedule*)? Há uso de **proxies financeiros** de atraso? Que **limiares** e **horizontes de previsão** são usados, e como o histórico é rotulado? Que bases teóricas (fatores críticos de atraso, sinais precoces de alerta, gestão de risco) sustentam esses conceitos? | Revisão da variável-alvo (10%, 3 meses, acumulado, plano vigente); migração para cronograma real na V2.0 |
| **PR2 — Preditores e engenharia temporal** | Quais **preditores** têm evidência (financeiros, contratuais, aditivos ou *change orders*, margem, fase, tipo de contrato, porte, metodologia)? Como os estudos tratam o tempo: janelas, defasagens, várias observações por projeto, normalização por porte? Que fontes de dados foram usadas? | A1.1 (pipeline de atributos), lista de atributos essenciais da validação |
| **PR3 — Modelos e avaliação** | Que algoritmos foram comparados e com que resultado relativo (linear, árvores, *boosting*, redes, séries temporais)? Como os estudos evitam **vazamento** (validação temporal) e lidam com **desbalanceamento** (métricas como área sob a curva PR, reamostragem)? A **calibração** de probabilidade é tratada? Como lidam com **poucos dados**? Há **conjuntos de dados públicos** ou geradores sintéticos realistas? | A1.2, A1.3, A1.4; escolha de dados para o benchmark |
| **PR4 — Explicabilidade e confiança** | Como se explicam modelos de risco de projeto (SHAP e outros métodos aditivos, importância de atributos)? Como se detecta que um caso está **fora da distribuição** de treino (domínio de aplicabilidade)? Que critérios de qualidade de dados ou de confiança são usados para **não emitir** uma predição? Como se mede a **antecedência** do alerta? | A1.5; regras e limites da validação (A2.2), em especial o método de fora da distribuição, exigido do A1.4 |
| **PR5 — Separação preditiva/generativa** | Há trabalhos em que um **LLM narra a saída de um modelo de ML** (*data-to-text*, explicação em linguagem natural de SHAP, relatórios gerados a partir de predições)? Como garantem **fidelidade numérica** e ausência de alucinação? Há tradução determinística de valores em faixas ou rótulos antes do LLM? Como avaliam com humanos? | A2.3 (instrução do LLM), A2.4 (teste de fundamentação), contribuição científica |
| **PR6 — Sistemas práticos e análogos** | Que **sistemas de alerta precoce** de risco de projeto ou portfólio foram implantados ou avaliados na prática (construção, EPC, infraestrutura, *software*, consultoria de engenharia)? Que **ferramentas comerciais ou industriais** existem? Como os gestores usam e aceitam esses alertas? | Posicionamento do agente; F06, F05; utilização como indicador |

### 6.4 Decisões provisórias que a revisão deve testar

Para cada uma, registrar se a literatura **apoia**, **contradiz** ou **não trata**:

- Faturamento como proxy de atraso; limiar de 10%; horizonte de 3 meses; medida acumulada contra o plano vigente; avaliação no fim da janela.
- Uma observação por projeto por período, com os últimos meses de cada projeto sem rótulo.
- Atributos essenciais (desvio de faturamento de 3 meses e desvio de margem) e completude mínima de 80%.
- Modelo linear como referência contra árvores e *boosting*.
- Explicadores aditivos (SHAP) como exigência do contrato.
- Escore de fora da distribuição entre 0 e 1, com ressalva a partir de 0,6 e bloqueio a partir de 0,8; defasagem de dados de 2 meses (ressalva) e 4 meses (bloqueio); salto de 40 pontos de probabilidade como sinal.
- Valores sempre em faixa na narrativa; o LLM só recebe a projeção.

### 6.5 Escopo de busca (proposta)

- **Domínio principal**: projetos de engenharia (construção civil, infraestrutura, EPC, energia, industrial) e projetos de serviços de engenharia ou consultoria.
- **Domínios análogos aceitos**: projetos de *software* e TI, contratos públicos, gestão de portfólio. Registrar o domínio de cada fonte, porque achados de um domínio nem sempre transferem.
- **Idiomas**: inglês (prioritário) e português.
- **Janela temporal**: sem limite para a base conceitual (fatores de atraso, valor agregado, sinais precoces). Para ML aplicado, priorizar 2015 em diante; para LLM e narrativa, 2020 em diante.
- **Tipo de fonte**: revisado por pares como padrão. *Preprints* só com o rótulo explícito `[preprint]`. Normas e guias (ex.: PMBOK, ISO 21500) entram como referência conceitual, não como achado.
- **Bases**: Google Scholar, Semantic Scholar, arXiv e, se houver acesso institucional, Scopus, Web of Science, IEEE Xplore, ACM DL e ScienceDirect. Registrar data de corte, bases cobertas e strings usadas.
- **Fora de escopo**: estudos só descritivos sem predição, como *surveys* de percepção de fatores de atraso por índice de importância relativa. Esses estudos entram **apenas** como fonte de candidatos a preditor (PR2), não como evidência de desempenho. Também ficam fora a previsão de duração de atividades isoladas sem relação com o projeto como um todo e os LLMs usados para calcular o risco (é o antipadrão do agente; citar só como contraponto).

### 6.6 Termos-chave iniciais

| Tema | Inglês | Português |
|---|---|---|
| PR1 | `project delay prediction`, `schedule overrun prediction`, `cost overrun prediction`, `earned value forecasting`, `earned schedule`, `project early warning signs`, `delay definition construction projects` | `previsão de atraso em projetos`, `predição de sobrecusto`, `valor agregado previsão`, `sinais precoces de alerta em projetos` |
| PR2 | `predictors of project delay`, `contract change orders risk`, `feature engineering project performance`, `temporal features panel data projects` | `fatores de atraso em obras`, `aditivos contratuais risco`, `indicadores financeiros de projetos` |
| PR3 | `machine learning project risk prediction`, `gradient boosting construction delay`, `temporal cross-validation leakage`, `imbalanced classification precision-recall`, `probability calibration risk model`, `project dataset public` | `aprendizado de máquina risco de projetos`, `validação temporal` |
| PR4 | `SHAP project risk`, `explainable AI construction management`, `out-of-distribution detection tabular`, `applicability domain`, `prediction abstention data quality` | `IA explicável gestão de projetos` |
| PR5 | `LLM explanation of machine learning predictions`, `natural language explanations SHAP`, `data-to-text faithfulness numbers`, `grounded narrative generation tabular`, `hallucination numerical claims` | `explicação em linguagem natural de modelos preditivos` |
| PR6 | `project portfolio early warning system`, `AI project management tool case study`, `decision support system project risk adoption` | `sistema de alerta precoce portfólio de projetos` |

Exemplos de combinação: `("delay" OR "schedule overrun" OR "cost overrun") AND ("machine learning" OR "predictive model") AND (project OR construction)`; `("large language model" OR LLM) AND ("explanation" OR narrative) AND ("SHAP" OR "model prediction" OR "tabular")`.

### 6.7 O que extrair de cada fonte

Herdado das revisões A4 anteriores, com campos específicos deste agente:

1. Referência completa, tipo de fonte e situação de revisão por pares.
2. Domínio e país dos projetos estudados.
3. **Definição de atraso ou desvio** usada (cronograma, custo, financeiro), **limiar** e **horizonte**.
4. **Unidade de observação** (projeto ou projeto-período) e tamanho da amostra (projetos e observações).
5. Preditores usados e os que se mostraram mais relevantes.
6. Modelos comparados e o vencedor.
7. **Estratégia de validação** (temporal ou aleatória; se aleatória, sinalizar risco de vazamento).
8. Métricas reportadas e tratamento de desbalanceamento e calibração.
9. Explicabilidade usada e como foi apresentada ao gestor.
10. Disponibilidade dos dados (público, proprietário, sintético) e do código.
11. Uso de LLM ou geração de texto e como a fidelidade foi controlada.
12. Ligação com o agente: que decisão da seção 6.4 a fonte apoia, contradiz ou deixa sem resposta.

### 6.8 Ângulo provável de contribuição científica (hipótese a verificar)

Um sistema que combina: (a) predição de atraso supervisionada com alvo financeiro de horizonte definido e validação temporal; (b) uma **camada de validação** que decide, por regras auditáveis, se o resultado pode virar texto; e (c) uma **ponte determinística** que entrega ao LLM apenas uma projeção em faixas, com teste de fundamentação revisado por humano. A revisão deve verificar se alguma fonte já reúne essas três peças. Nas revisões dos outros dois agentes, a lacuna estava justamente na combinação, e não nas peças isoladas.

### 6.9 Cuidados

- **Terminologia**: *delay*, *schedule overrun*, *cost overrun* e *time overrun* são usados de forma inconsistente; registrar a definição de cada fonte, não só o termo.
- **Literatura de fatores × literatura preditiva**: grande parte da literatura de atraso em construção é de levantamento de percepção (questionários, rankings de fatores). Ela é útil para candidatos a preditor, mas não mede desempenho de predição.
- **Desempenho reportado com validação aleatória** tende a ser otimista em dados de projetos; não comparar diretamente com resultados de validação temporal.
- **Dados reais**: o projeto ainda não tem autorização para dados reais, e a existência de histórico suficiente não está confirmada. Conjuntos públicos e geradores sintéticos que a revisão encontrar valem por si só.
- **Não incluir** nos entregáveis dados de clientes, nomes de organizações parceiras ou valores reais de projetos.

## 7. Fontes no repositório

Para quem tiver acesso ao repositório `cortex`:

- Especificação do agente: [`agentes/agente_previsao_atraso.md`](../../agentes/agente_previsao_atraso.md)
- Regras não negociáveis (separação de camadas, faixas, validação temporal, fundamentação): [`business_rules.md`](../../business_rules.md)
- Variável-alvo e atributos: [`datamodel_reference.md`](../../datamodel_reference.md#variável-alvo-e-atributos-mvp)
- Contrato do resultado (A2.1): [`A2.1_schema_resultado_preditivo.md`](A2.1_schema_resultado_preditivo.md) · dicionário de campos: [`dicionario_resultado_preditivo.md`](dicionario_resultado_preditivo.md) · guia sem termos técnicos: [`guia_ponte_preditiva_generativa.md`](guia_ponte_preditiva_generativa.md)
- Validação (A2.2): [`A2.2_camada_validacao.md`](A2.2_camada_validacao.md)
- Decomposição das atividades A1–A5: [`resposta_contribuicao_tecnica.md`](../../resposta_contribuicao_tecnica.md#44-quebra-em-subtarefas-a1a5)
- Modelo de protocolo de revisão já usado em outro agente: [`eap_wbs/A4.1_escopo_busca.md`](../eap_wbs/A4.1_escopo_busca.md) e [`boas_praticas/A4.5.1_protocolo_revisao_sistematica.md`](../boas_praticas/A4.5.1_protocolo_revisao_sistematica.md)