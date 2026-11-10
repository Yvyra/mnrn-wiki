# Roteiro de Dossiê — Nova Raposo: efeitos sobre a cidade de São Paulo

**Origem**: derivado da apresentação técnica `raw/Nova_Raposo_Efeitos_Sao_Paulo_CET.pptx`
(14 slides, 02/10/2026, discussão com Planejamento/CET).
**Texto integral extraído**: `dados/extraidos/raw/Nova_Raposo_Efeitos_Sao_Paulo_CET.txt`
**Status**: proposta de estrutura (rascunho para validação).

---

## 1. Objetivo do dossiê

Documentar, com base em fontes primárias já extraídas, os efeitos do Projeto Nova
Raposo sobre a rede urbana de São Paulo — em especial a cadeia de gargalos
Raposo → Escola Politécnica → Marginal Pinheiros → Eusébio Matoso → Túnel Fernando
Vieira de Mello → Rebouças — e confrontá-los com alternativas integradas de
transporte (BRT estruturante + Metrô + rede local).

## 2. Pergunta central

> O ganho de capacidade na rodovia pode transferir demanda para gargalos urbanos
> já saturados?

## 3. Princípio metodológico (obrigatório em todo o texto)

Os efeitos futuros descritos na apresentação são **hipóteses para modelagem**, não
resultados comprovados. O dossiê deve marcar explicitamente, em cada seção, o que é
fato documentado (fonte em `raw/`/`dados/`) e o que é inferência a testar.

## 4. Estrutura proposta do dossiê

Cada item abaixo lista: tese, evidências a mobilizar e fontes disponíveis.

### 4.1 Sumário executivo
- Síntese da pergunta central, do efeito-funil e da recomendação (modelar antes de ampliar capacidade).

### 4.2 O que o projeto prevê
- Intervenções previstas: marginais contínuas SP–Cotia, reorganização de acessos e
  pontos de ônibus, túnel Av. Benjamin Mansur, nova alça Escola Politécnica, alças
  Granja Viana, faixa adicional a partir do km 15,27.
- Fontes:
  - `dados/extraidos/raw/2024 09 NFMA D06a_LOTE 1 - EDITAL.txt`
  - `dados/extraidos/raw/2024 09 NFMA D06b_LOTE 1 - Anexo 04 - Estrutura Tarif†ria.txt`
  - `dados/extraidos/Lote 34 - Contrato, Anexos e Apêndices/Anexo 01 - Regulamento da concessão.txt`
  - `dados/extraidos/Lote 34 - Contrato, Anexos e Apêndices/Anexo 02 - Sistema Rodoviário.txt`
  - `dados/extraidos/Lote 34 - Contrato, Anexos e Apêndices/Anexo 12 - Projetos Funcionais da Malha Concedida.txt` (e subprojetos SP-029/SP-270/SP-280)
  - `dados/extraidos/Lote 34 - Contrato, Anexos e Apêndices/Apêndice E - ACESSOS.txt`

### 4.3 Metodologia de análise
- Modelagem de tráfego integrada Estado–Município; nível de serviço por elo da
  cadeia; pessoas/hora e tempo total de viagem (não só veículos/hora).
- Benchmark: `dados/extraidos/raw/2025-04 - Apresentação Seminário Mobilidade - Marta Estudo de Caso Barcelona.txt`

### 4.4 A cadeia de gargalos (o "efeito-funil")
#### 4.4.1 O efeito-funil na entrada da cidade
- Capacidade ampliada a montante → gargalos urbanos a jusante; transferência de
  congestionamento para a rede municipal.
#### 4.4.2 A Marginal Pinheiros como nó crítico
- Função de distribuidora metropolitana; repercussão em interseções, pontes e
  conexões municipais; propagação para deslocamentos sem origem na rodovia.
#### 4.4.3 O Túnel Fernando Vieira de Mello como "teste de realidade"
- Tratar o túnel como parte de uma cadeia de capacidade, não como ponto isolado.
- Fontes da seção (hipóteses + contexto operacional):
  - `dados/extraidos/raw/2025-04 - Apresentação Seminário Mobilidade - Elio Pedágio Controle Demanda.txt`
  - `dados/extraidos/raw/2025-04 - Apresentação Seminário Mobilidade - Horácio Analise e Refelxões Proposta Nova Raposo.txt`

### 4.5 Efeitos além dos automóveis
- Congestionamento, ônibus (perda de velocidade), transporte local, emissões e
  ruído, usuários que nunca usaram a Raposo.
- Fontes (clipping):
  - `dados/extraidos/4.2.Clipping/*` (matérias de trânsito, poluição do ar, ilha de calor, desapropriação)
  - `dados/extraidos/raw/2025-04 - Apresentação Seminário Mobilidade - Felipe Clima Mobilidade Cidades.txt`

### 4.6 Meio ambiente e urbanização
- Uso do solo, áreas verdes e arborização, corredor ecológico, desapropriações,
  fragmentação urbana, pressão de ocupação.
- Fontes:
  - `dados/extraidos/raw/2024 09 NFMA D07_RELAT PREL IMPACTO AMBIENTAL NR R00 0824.txt`
  - `dados/extraidos/raw/2024 09 NFMA D08_PROJETO NOVA RAPOSO_PARQUES ADJACENTES.txt`
  - `dados/extraidos/raw/2025 09 Parecer CAEX Nova Raposo ... ParecerCAEX.txt`
  - `dados/extraidos/raw/1500561-14.2025.8.26.0053 ACP Nova Raposo.txt`
  - `dados/extraidos/raw/2024 11 CAUTELAR ANTECEDENTE - NOVA RAPOSO.txt`

### 4.7 Contexto institucional (Portaria SGM nº 159/2026)
- GT intersecretarial (CET, SPTrans, SMT/SEMTRA, SEPLAN, SMUL, SVMA, SPObras e
  outros) para novo viaduto na Marginal Pinheiros e requalificação da Raposo.
  Processo SEI 6011.2025/0003642-5.
- Fonte a obter (não está em `raw/`): Portaria SGM nº 159, de 03/08/2026, Diário
  Oficial do Município / Portal da Prefeitura. **[verificar]**

### 4.8 Perguntas a responder antes da decisão (o que a CET precisa saber)
- Quantos veículos/pessoas adicionais por ponto crítico; impacto em Marginal,
  Eusébio Matoso, Túnel Fernando Vieira, Rebouças, Ponte do Jaguaré, Escola
  Politécnica; distribuição temporal e propagação de filas; linhas de ônibus
  afetadas; intervenções municipais necessárias e seu custo urbano.

### 4.9 Alternativa integrada: transportar pessoas, não apenas veículos
- BRT estruturante com prioridade semafórica e segregação física; integração
  tarifária/física com Metrô/CPTM; linhas locais alimentadoras.
- Fontes:
  - `dados/extraidos/raw/2025-04 - Apresentação Seminário Mobilidade - Nestor Linha Marrom.txt`
  - `dados/extraidos/raw/2025-04 - Apresentação Seminário Mobilidade - Marta Estudo de Caso Barcelona.txt`

### 4.10 Financiamento e política de mobilidade
- Gestão da circulação (rodízio como instrumento econômico), destinação da receita
  ao transporte coletivo, Lei Federal 12.587/2012.
- Fonte a obter (não está em `raw/`): Lei 12.587/2012 (PNMU), Planalto. **[verificar]**

### 4.11 Encaminhamentos (6 passos)
1. Modelar conjuntamente Nova Raposo + rede municipal, com cenários de demanda.
2. Mapear gargalos e efeitos de fila nos acessos à cidade.
3. Quantificar impactos sobre ônibus, automóveis, emissões e tempo de viagem.
4. Avaliar ambiental e urbanisticamente novas alças, viadutos e ampliações.
5. Comparar cenário rodoviário com cenário de transporte coletivo estruturante.
6. Levar resultados ao GT intersecretarial Estado–Município.

### 4.12 Referências e fontes
- Consolidar em uma seção final, com mapeamento para os caminhos em `dados/extraidos/`.

## 5. Lacunas a resolver antes de redigir

- [ ] Obter Portaria SGM nº 159/2026 (texto integral) e confirmação do SEI 6011.2025/0003642-5.
- [ ] Obter referência formal da Lei 12.587/2012 para citação.
- [ ] Definir se a modelagem de tráfego será executada (quem/ferramenta) ou se o
      dossiê registra apenas a demanda por modelagem.
- [ ] Verificar se há dados quantitativos (contagens, velocidades) em `raw/` ainda
      não extraídos — os `.dwg`/`.xlsx` do Lote 34 podem conter geometria/tabelas.

## 6. Observação

Esta é a **proposta de estrutura**; o texto do dossiê ainda não foi redigido. A
estrutura espelha a ordem argumentativa dos 14 slides da apresentação CET.
