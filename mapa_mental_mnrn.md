# Mapa Mental - Adiamento Leilão (SP ROADS III)

## 1. Visão Geral em Diagrama de Fluxo / Rede (Mermaid Flowchart)

```mermaid
flowchart LR
    %% Subgraphs para contextualização dos ramos de atuação do MP
    subgraph MP_Habitacao["MP Habitação e Urbanístico"]
        IL[Interesse Local]
        PU[Pedágio Urbano]
    end

    subgraph MP_Ambiente["MP Meio Ambiente"]
        AP[Anteprojeto]
        IFC[Relatório IFC<br/>E&S Study Draft I SP ROADS III]
    end

    subgraph MP_Patrimonio["MP Patrimônio Público / Interesses Difusos e Coletivos"]
        ROOT(("Adiamento<br/>Leilão"))
        JUST[Justificativa]
        DESAP[Desapropriações]
        PUB[Publicização]
    end

    %% Conexões a partir do Nó Central
    ROOT --- AP
    ROOT --- IL
    ROOT --- JUST
    ROOT --- DESAP
    ROOT --- PUB

    %% Ramo: Anteprojeto
    AP -->|não atende requisitos| ART6["Art. 6º, inciso XXIV (Anteprojeto)"]
    ART6 --- A1["a) Demanda, justificativa e nível de serviço"]
    ART6 --- A2["e) Adequação ao interesse público e impacto ambiental"]
    ART6 --- A3["j) Memorial descritivo e padrões mínimos"]

    AP --> IFC
    IFC -->|não inclui| NI1["Impacto em Áreas Verdes e Parques"]
    IFC -->|não inclui| NI2["Estudo de impacto na temperatura do Bairro"]
    IFC -->|não inclui| NI3["Córregos e Nascentes (recursos hídricos)"]
    IFC -->|usa como premissas| PAD["Padrão IFC não compete a perímetro urbano"]

    %% Ramo: Interesse Local
    IL --- IL1["Estatuto das Cidades / ODS"]
    IL --- IL2["Lei de Zoneamento"]
    IL --- IL3["Plano Diretor - PDE"]
    IL --- IL4["Mobilidade Urbana"]
    IL4 --- IL4_1["Falta de Estudos de Alternativas"]
    IL --- IL5["Segurança / Acidentes"]
    IL --- IL6["Convênio Prefeitura"]
    IL --- PU
    PU --- PU1["Jurisprudência STF vs. restrição ao trânsito e direito de ir e vir"]
    PU --- PU2["Lei Federal nº 12.587/2012 (Política de Mobilidade Urbana)"]

    %% Ramo: Justificativa
    JUST --- J1["Art. 45 da Lei 14.133/21"]
    JUST --- J2["Plano São Paulo Roads III não define ganho social"]
    JUST --- J3["Falta de demonstração de Programa de Necessidade"]

    %% Ramo: Desapropriações
    DESAP --- D1["Marco de Ressarcimento"]
    DESAP --- D2["Desapropriação Parcial"]
    DESAP --- D3["Insegurança jurídica"]
    D3 --- D3_1["Indefinição de áreas irregulares"]

    %% Ramo: Publicização
    PUB --- P1["Só 2 Audiências Públicas"]
    PUB --- P2["Inexistência de Relatório das supostas Contribuições"]
    PUB --- P3["Inexistência de evidências de informes à grande imprensa"]
    PUB --- P4["Resposta à Ação Marina Helou (Antecipação de provas)"]
    PUB --- P5["Pesquisa Opinião NRN"]

    %% Relações Cruzadas / Linhas Tracejadas
    ART6 -.->|não inclui| JUST
    AP -.->|não inclui| IL
    ROOT -.->|Não define| AP
    DESAP -.->|não houve comunicação prévia| PUB
```

---

## 2. Visão em Formato Mindmap Nativo (Mermaid Mindmap)

```mermaid
mindmap
  root((Adiamento Leilão))
    Anteprojeto
      Art. 6º inciso XXIV anteprojeto
        a) Demonstração e justificativa do programa de necessidades, avaliação de demanda
        e) Parâmetros de adequação ao interesse público, economia, facilidade, impacto ambiental e acessibilidade
        j) Memorial descritivo dos elementos da edificação, componentes construtivos e materiais
      Relatório IFC E&S Study Draft I SP ROADS III
        Não inclui Impacto em Áreas Verdes e Parques
        Não inclui Estudo de impacto na temperatura do Bairro
        Não inclui Córregos e Nascentes recursos hídrico
        Padrão de Desempenho IFC não compete a perímetro urbano
    Interesse Local
      Estatuto das Cidades ODS
      Lei de Zoneamento
      Plano Diretor - PDE
      Mobilidade Urbana
        Falta de Estudos de Alternativas
      Segurança / Acidentes
      Convênio Prefeitura
      Pedágio Urbano
        Jurisprudência STF vs. restrição ao trânsito interno e direito de ir e vir
        Lei Federal nº 12.587/2012 Política Nacional de Mobilidade Urbana
    Justificativa
      Art. 45 da Lei 14.133/21
      Plano São Paulo Roads III não define ganho social
      Falta de demonstração de Programa de Necessidade
    Desapropriações
      Marco de Ressarcimento
      Desapropriação Parcial
      Insegurança jurídica
        Indefinição de áreas irregulares
    Publicização
      Só 2 Audiências Públicas
      Inexistência de Relatório das supostas Contribuições
      Inexistência de evidências de informes à grande imprensa
      Resposta à Ação Marina Helou Antecipação de provas
      Pesquisa Opinião NRN
```
