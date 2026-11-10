# Dossiê — Nova Raposo: efeitos sobre a cidade de São Paulo

**Resumo**: Análise dos efeitos do Projeto Nova Raposo sobre a rede urbana de São
Paulo, com foco na cadeia de gargalos Raposo → Escola Politécnica → Marginal
Pinheiros → Eusébio Matoso → Túnel Fernando Vieira de Mello → Rebouças, e
contraponto a alternativas integradas de transporte (BRT estruturante + Metrô).

**Fontes**: `raw/Nova_Raposo_Efeitos_Sao_Paulo_CET.pptx` e os textos extraídos em
`dados/extraidos/` (contrato Lote 34, edital, clippings, peças judiciais, seminários,
Portaria SGM nº 159/2026 e Lei 12.587/2012).

**Última atualização**: 2026-11-10

---

## Sumário executivo

O Projeto Nova Raposo amplia a capacidade da rodovia a montante da cidade, mas o
gargalo decisivo está a jusante: a rede municipal de São Paulo, já saturada na
Marginal Pinheiros e nas conexões com a zona oeste. A pergunta central não é
"quantos veículos a rodovia comporta", e sim "para onde vai o fluxo adicional ao
entrar na cidade".

As intervenções previstas (marginais contínuas SP–Cotia, novas alças, viadutos na
Marginal e túnel na Av. Benjamin Mansur) tendem a concentrar mais tráfego de entrada
exatamente nos pontos críticos municipais. A apresentação técnica elaborada para a
CET (out/2026) propõe, antes de consolidar a ampliação de capacidade, **modelar o
sistema de forma integrada Estado–Município** e comparar o cenário rodoviário com um
cenário de transporte coletivo estruturante (BRT + Metrô).

O Município já reconhece a questão institucionalmente: a **Portaria SGM nº 159/2026**
designou um Grupo de Trabalho Intersecretarial para o novo viaduto na Marginal e a
requalificação da Raposo, com a CET formalmente representada. A **Lei 12.587/2012**
(Política Nacional de Mobilidade Urbana) dá base legal para priorizar o transporte
coletivo e para instrumentos econômicos de gestão da circulação.

## 1. Objeto e pergunta central

- **Objeto**: efeitos do Projeto Nova Raposo sobre a cidade de São Paulo.
- **Pergunta central**: o ganho de capacidade na rodovia pode transferir demanda
  para gargalos urbanos já saturados?
- **Foco espacial**: Raposo → Escola Politécnica → Marginal Pinheiros → Eusébio
  Matoso → Túnel Fernando Vieira de Mello → Rebouças
  (fonte: `dados/extraidos/raw/Nova_Raposo_Efeitos_Sao_Paulo_CET.txt`).

## 2. O que o projeto prevê

A apresentação oficial da Nova Raposo (ARTESP/Governo do Estado, 2024) prevê:

- marginais contínuas de São Paulo a Cotia;
- reorganização de acessos e de pontos de ônibus;
- túnel na Av. Benjamin Mansur;
- nova alça na Av. Escola Politécnica;
- novas alças na região da Granja Viana;
- faixa adicional a partir do km 15,27.

**Fato documentado** (fonte: `dados/extraidos/raw/Nova_Raposo_Efeitos_Sao_Paulo_CET.txt`):
o próprio material oficial destaca a ocorrência de acidentes e interrupções de fluxo
no trecho atual, o que fundamenta a intervenção.

Fontes primárias para o detalhamento das intervenções:

- `dados/extraidos/raw/2024 09 NFMA D06a_LOTE 1 - EDITAL.txt`
- `dados/extraidos/raw/2024 09 NFMA D06b_LOTE 1 - Anexo 04 - Estrutura Tarif†ria.txt`
- `dados/extraidos/Lote 34 - Contrato, Anexos e Apêndices/Anexo 01 - Regulamento da concessão.txt`
- `dados/extraidos/Lote 34 - Contrato, Anexos e Apêndices/Anexo 02 - Sistema Rodoviário.txt`
- `dados/extraidos/Lote 34 - Contrato, Anexos e Apêndices/Anexo 12 - Projetos Funcionais da Malha Concedida.txt` (e subprojetos SP-029/SP-270/SP-280)
- `dados/extraidos/Lote 34 - Contrato, Anexos e Apêndices/Apêndice E - ACESSOS.txt`

Os três novos viadutos previstos na Marginal Pinheiros (paralelos às pontes Eusébio
Matoso e Bernardo Goldfarb, e a ligação Valentim Gentil–Antônio Batuira) são o elo
físico entre a concessão rodoviária e a rede municipal
(fonte: `dados/extraidos/4.2.Clipping/4.2.1.Noticias Sobre NRN/Prefeitura de SP cria grupo de trabalho para estudar novo viaduto na Marginal Pinheiros __ Reader View.txt`).

## 3. Princípio metodológico e método

- **Princípio**: os efeitos futuros descritos são **hipóteses para modelagem**, não
  resultados comprovados. A apresentação-fonte registra essa ressalva explicitamente
  (fonte: `dados/extraidos/raw/Nova_Raposo_Efeitos_Sao_Paulo_CET.txt`, slide "Fontes").
- **Método proposto**:
  - modelagem de tráfego integrada Estado–Município, com cenários de demanda;
  - avaliação do nível de serviço de cada elo da cadeia de capacidade;
  - comparação em pessoas/hora e tempo total de viagem, não apenas veículos/hora;
  - avaliação ambiental e urbanística das novas alças, viadutos e ampliações.
- **Benchmark de referência**: `dados/extraidos/raw/2025-04 - Apresentação Seminário Mobilidade - Marta Estudo de Caso Barcelona.txt` (integração viária + transporte coletivo).

## 4. A cadeia de gargalos (o "efeito-funil")

### 4.1 O efeito-funil na entrada da cidade

**Hipótese a testar**: capacidade ampliada a montante (Raposo Tavares) transfere
congestionamento para gargalos urbanos a jusante (Escola Politécnica, Marginal,
Eusébio Matoso, Túnel Fernando Vieira, Rebouças). A sequência proposta pela
apresentação é: *capacidade ampliada a montante → gargalos urbanos a jusante →
possível transferência de congestionamento para a rede municipal*
(fonte: `dados/extraidos/raw/Nova_Raposo_Efeitos_Sao_Paulo_CET.txt`).

O relatório preliminar do Movimento Nova Raposo NÃO! dimensiona a ordem de grandeza:
o aumento esperado de **111.000 veículos** (conforme o edital) seria "descarregado
mais velozmente nos atuais gargalos da Ponte Eusébio Matoso e Marginal Pinheiros"
(fonte: `dados/extraidos/raw/2024 09 NFMA D07_RELAT PREL IMPACTO AMBIENTAL NR R00 0824.txt`).
É a demanda a montante cuja destinação a jusante ainda precisa ser modelada — reforça,
sem comprovar, a hipótese do funil.

### 4.2 A Marginal Pinheiros como nó crítico

A Marginal funciona como distribuidora metropolitana e já recebe fluxos de vários
eixos. Um aumento concentrado de entradas pode repercutir em interseções, acessos,
pontes e conexões municipais. A análise deve considerar o sistema completo, incluindo
Escola Politécnica, Ponte do Jaguaré, Eusébio Matoso, Túnel Fernando Vieira e
Rebouças (fonte: `dados/extraidos/raw/Nova_Raposo_Efeitos_Sao_Paulo_CET.txt`).

### 4.3 O Túnel Fernando Vieira de Mello como "teste de realidade"

O túnel deve ser tratado como parte de uma cadeia de capacidade, não como ponto
isolado: *entrada de fluxo → capacidade limitada → fila/retenção → repercussão na
rede*. Se a demanda adicional chegar simultaneamente aos acessos urbanos, a retenção
pode deslocar-se para vias paralelas e cruzamentos
(fonte: `dados/extraidos/raw/Nova_Raposo_Efeitos_Sao_Paulo_CET.txt`).

Contexto operacional adicional:

- `dados/extraidos/raw/2025-04 - Apresentação Seminário Mobilidade - Elio Pedágio Controle Demanda.txt` (pedágio como instrumento de controle de demanda)
- `dados/extraidos/raw/2025-04 - Apresentação Seminário Mobilidade - Horácio Analise e Refelxões Proposta Nova Raposo.txt`

## 5. Efeitos além do automóvel

A apresentação lista efeitos em cascata que vão além do congestionamento:

- **Congestionamento**: filas mais longas e maior variabilidade dos tempos de viagem.
- **Ônibus**: perda de velocidade operacional quando compartilham os gargalos.
- **Transporte local**: atrasos propagados para linhas alimentadoras e transversais.
- **Emissões e ruído**: maior tempo parado e mais acelerações/frenagens.
- **Rede municipal**: impactos sobre usuários que nunca utilizaram a Raposo.

A avaliação deve comparar pessoas/hora e tempo total de viagem, não apenas
veículos/hora (fonte: `dados/extraidos/raw/Nova_Raposo_Efeitos_Sao_Paulo_CET.txt`).

O clipping confirma a dimensão ambiental e de saúde do tráfego motorizado:

- Em set/2024, São Paulo chegou a registrar "a pior qualidade de ar no mundo", com
  qualidade "muito ruim" na capital e RMSP (fonte:
  `dados/extraidos/4.2.Clipping/São Paulo tem a pior qualidade de ar do mundo nesta segunda (9), diz site __ Reader View.txt`;
  notícia original: folha.uol.com.br/cotidiano/2024/09).
- O conjunto de clippings registra ainda ilhas de calor, síndrome respiratória
  aguda e congestionamento (`dados/extraidos/4.2.Clipping/*`).
- `dados/extraidos/raw/2025-04 - Apresentação Seminário Mobilidade - Felipe Clima Mobilidade Cidades.txt`

## 6. Meio ambiente e urbanização

A expansão viária deve ser analisada também pelo uso do solo e pelos efeitos sobre
áreas verdes e arborização. Pontos de atenção:

- trechos vegetados junto à rodovia com funções ambientais e de conectividade
  ecológica que não aparecem em análise exclusivamente viária;
- novos acessos, alças, viadutos e ampliações podem produzir desapropriações,
  fragmentação urbana e pressão de ocupação;
- necessidade de avaliar corredor ecológico, parques/áreas verdes, habitações e
  atividades econômicas afetadas (fonte: `dados/extraidos/raw/Nova_Raposo_Efeitos_Sao_Paulo_CET.txt`).

Fontes primárias ambientais e urbanísticas:

- `dados/extraidos/raw/2024 09 NFMA D07_RELAT PREL IMPACTO AMBIENTAL NR R00 0824.txt`
- `dados/extraidos/raw/2024 09 NFMA D08_PROJETO NOVA RAPOSO_PARQUES ADJACENTES.txt`
- `dados/extraidos/raw/2025 09 Parecer CAEX Nova Raposo ... ParecerCAEX.txt`
- `dados/extraidos/raw/1500561-14.2025.8.26.0053 ACP Nova Raposo.txt`
- `dados/extraidos/raw/2024 11 CAUTELAR ANTECEDENTE - NOVA RAPOSO.txt`

O relatório preliminar do Movimento Nova Raposo NÃO! dimensiona a supressão vegetal
em cerca de **425.000 m² de cobertura** nessa versão do projeto, além de tabelar
áreas de APP invadidas (fonte: `dados/extraidos/raw/2024 09 NFMA D07_RELAT PREL
IMPACTO AMBIENTAL NR R00 0824.txt`). A pressão sobre habitações é corroborada pela
imprensa local: moradores da beira da Raposo passaram a receber notificações de
desapropriação do Governo do Estado, com parte de terrenos, casas e comércios
afetada (fonte: `dados/extraidos/4.2.Clipping/4.2.1.Noticias Sobre NRN/Moradores da beira da Raposo Tavares começam a receber notificação de desapropriação __ Reader View.txt`).

## 7. Contexto institucional

O Município de São Paulo formalizou um **Grupo de Trabalho Intersecretarial** para o
estudo de implantação de novo viaduto na Marginal Pinheiros e requalificação da
Rodovia Raposo Tavares.

Cadeia normativa (confirmada no Catálogo de Legislação Municipal, Prefeitura de SP):

- **Portaria SGM nº 257, de 10/10/2025** — institui o "GT Marginal Pinheiros".
- **Portaria SGM nº 258, de 13/10/2025** — designa os membros do GT instituído pela 257.
- **Portaria SGM nº 155, de 31/07/2026** — institui novo GT "Marginal Pinheiros/
  Requalificação da Raposo Tavares" (composição ampliada).
- **Portaria SGM nº 159, de 03/08/2026** — designa os representantes do GT da 155 e
  **revoga a Portaria SGM nº 258/2025**. Processo SEI 6011.2025/0003642-5.

Órgãos com assento no GT vigente (11): SGM, SIURB, SMT/SEMTRA, SEPLAN, SMUL, SMDET,
SVMA, SPObras, CET, SP-Urbanismo e SPTrans. A CET está formalmente representada.

Fontes oficiais (internet):
- legislacao.prefeitura.sp.gov.br/portaria-secretaria-do-governo-municipal-sgm-257-de-10-de-outubro-de-2025
- legislacao.prefeitura.sp.gov.br/portaria-secretaria-do-governo-municipal-sgm-258-de-13-de-outubro-de-2025
- legislacao.prefeitura.sp.gov.br/portaria-secretaria-do-governo-municipal-sgm-155-de-31-de-julho-de-2026
- legislacao.prefeitura.sp.gov.br/portaria-secretaria-do-governo-municipal-sgm-159-de-3-de-agosto-de-2026

Nota: a aparente divergência do clipping Diário do Transporte (que citava "SGM
nº 257" em 13/10) era imprecisão de data/número — a 257 é de 10/10 e institui; a
portaria publicada em 13/10 é a 258 (designa). Não há contradição entre as normas.

## 8. Perguntas a responder antes da decisão

Para subsidiar a decisão sobre as obras, a apresentação elenca perguntas técnicas
(fonte: `dados/extraidos/raw/Nova_Raposo_Efeitos_Sao_Paulo_CET.txt`):

1. Quantos veículos e, principalmente, quantas pessoas adicionais chegarão a cada
   ponto crítico?
2. Qual o impacto sobre Marginal Pinheiros, Eusébio Matoso, Túnel Fernando Vieira,
   Rebouças, Ponte do Jaguaré e Escola Politécnica?
3. Qual a distribuição temporal dos fluxos e a propagação das filas?
4. Quais linhas de ônibus perderão velocidade e regularidade?
5. Quais intervenções municipais seriam necessárias para absorver o fluxo — e qual
   seu custo urbano?

Proposta-síntese: **simulação integrada antes da consolidação das obras que aumentem
a capacidade de entrada na cidade**.

## 9. Alternativa integrada: transportar pessoas, não apenas veículos

A apresentação contrapõe ao cenário rodoviário um cenário de transporte coletivo
estruturante:

- **BRT estruturante** com prioridade semafórica e segregação física onde necessária;
- integração tarifária e física com Metrô/CPTM;
- linhas locais alimentadoras conectadas ao corredor estruturante;
- estações e travessias com acesso seguro e rápido;
- objetivo: reduzir a necessidade de entrada de automóveis na rede urbana.

A lógica em cadeia é *linhas locais → BRT Raposo → Metrô → centro expandido →
destinos → retorno*, captando passageiros antes que ingressem nos gargalos urbanos
(fonte: `dados/extraidos/raw/Nova_Raposo_Efeitos_Sao_Paulo_CET.txt`).

Fontes de apoio:

- `dados/extraidos/raw/2025-04 - Apresentação Seminário Mobilidade - Nestor Linha Marrom.txt`
- `dados/extraidos/raw/2025-04 - Apresentação Seminário Mobilidade - Marta Estudo de Caso Barcelona.txt`

## 10. Financiamento e política de mobilidade

A **Lei 12.587/2012** (Política Nacional de Mobilidade Urbana) fornece a base legal
para a priorização do transporte coletivo e para instrumentos econômicos
(fonte: `dados/extraidos/raw/Lei 12587-2012.txt`):

- **Art. 6º, II** — prioridade dos modos não motorizados sobre os motorizados e do
  transporte público coletivo sobre o individual motorizado.
- **Art. 6º, VI** — priorização de projetos de transporte público coletivo
  estruturadores do território.
- **Art. 23, I** — restrição e controle de acesso e circulação, permanente ou
  temporário, de veículos motorizados em locais e horários predeterminados.
- **Art. 23, III** — aplicação de tributos sobre modos e serviços de transporte
  urbano para desestimular o uso de determinados modos, **vinculando-se a receita à
  aplicação exclusiva em infraestrutura de transporte público coletivo e não
  motorizado e ao subsídio público da tarifa**.
- **Art. 24** — Plano de Mobilidade Urbana como instrumento de efetivação da
  política (obrigatório para municípios como São Paulo).

A apresentação propõe avaliar a transformação do rodízio em instrumento de gestão da
circulação, com cobrança e destinação da receita ao transporte coletivo — como estudo
técnico e jurídico, não como decisão prévia
(fonte: `dados/extraidos/raw/Nova_Raposo_Efeitos_Sao_Paulo_CET.txt`).

## 11. Encaminhamentos

Os seis passos propostos à CET (fonte: `dados/extraidos/raw/Nova_Raposo_Efeitos_Sao_Paulo_CET.txt`):

1. Modelar conjuntamente Nova Raposo + rede municipal, com cenários de demanda.
2. Mapear gargalos e efeitos de fila nos acessos à cidade.
3. Quantificar impactos sobre ônibus, automóveis, emissões e tempo de viagem.
4. Avaliar ambiental e urbanisticamente novas alças, viadutos e ampliações.
5. Comparar cenário rodoviário com cenário de transporte coletivo estruturante
   (BRT + Metrô).
6. Levar os resultados ao grupo de trabalho intersecretarial Estado–Município.

Mensagem final: *antes de ampliar a capacidade de entrada de automóveis, medir o
efeito dessa capacidade sobre toda a rede urbana*.

## 12. Referências

- ARTESP/Governo do Estado — apresentação oficial do Projeto Nova Raposo (2024).
- Prefeitura de São Paulo — Portaria SGM nº 155/2026 e nº 159/2026
  (`dados/extraidos/raw/Portaria SGM n159-2026.txt`).
- Lei 12.587/2012 — Política Nacional de Mobilidade Urbana
  (`dados/extraidos/raw/Lei 12587-2012.txt`).
- Contrato nº 0548-ARTESP-2025 e anexos/apêndices
  (`dados/extraidos/Lote 34 - Contrato, Anexos e Apêndices/`).
- Clippings de imprensa (`dados/extraidos/4.2.Clipping/`).
- Peças e pareceres judiciais (`dados/extraidos/raw/`).
- Fontes oficiais (internet):
  - Projeto Nova Raposo — SP Parcerias em Investimentos:
    parceriaseminvestimentos.sp.gov.br (projetos contratados → Nova Raposo)
  - SEMIL — consulta pública do Lote Nova Raposo (mar/2024):
    semil.sp.gov.br
  - PPI — edital da Nova Raposo (R$ 7,3 bi em investimento):
    ppi.sp.gov.br
  - Catálogo de Legislação Municipal — Portarias SGM 257/2025, 258/2025, 155/2026 e 159/2026:
    legislacao.prefeitura.sp.gov.br

## Lacunas em aberto

- [x] **Portaria SGM 257 × 258** — resolvida (cadeia normativa confirmada na fonte oficial; ver seção 7).
- [x] **Dados quantitativos nos `.dwg`/`.xlsx`** — os `.xlsx` do Lote 34 contêm lista
  de obras (km, tipo, extensão, coordenadas), custos (EVTE) e alinhamento
  georreferenciado (ALN), mas **não contêm contagens de tráfego nem velocidades**.
  O único dado de demanda disponível no repositório é o de **111.000 veículos**
  (citado no relatório do MNRN a partir do edital). Contagens/velocidades/níveis de
  serviço, se existirem, estão nos estudos oficiais (SP Parcerias/SEMIL/ARTESP).
- [ ] **Modelagem de tráfego** — não executada neste repositório (que é documental).
  O dossiê registra a modelagem integrada Estado–Município como **encaminhamento
  pendente** (seção 11); os inputs parciais disponíveis são o dado de demanda
  (111.000 veículos), a lista de obras e a EVTE. A execução depende do GT/CET.
