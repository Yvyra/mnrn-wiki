"""Gera o grafo interativo d3blocks da malha normativa da Nova Raposo."""
import pandas as pd
from d3blocks.elasticgraph import Elasticgraph

edges = [
    ("Decreto 68.695/2024", "Edital Lote 1 (02/2024)", 3),
    ("Edital Lote 1 (02/2024)", "Contrato 0548/ARTESP/2025", 3),
    ("Edital Lote 1 (02/2024)", "Lei 14.133/2021 (Licitações)", 2),
    ("Contrato 0548/ARTESP/2025", "Lei 12.587/2012 (PNMU)", 1),
    ("Inquérito Civil 0482.0000571/2024", "Parecer CAEX 15789370", 3),
    ("Parecer CAEX 15789370", "Resolução CONAMA 01/1986 (EIA/RIMA)", 3),
    ("Parecer CAEX 15789370", "ACP 1500561-14 (MPSP)", 2),
    ("Parecer CAEX 15789370", "Ação Popular 1120375-77", 2),
    ("ACP 1500561-14 (MPSP)", "Lei 7.347/1985 (LACP)", 2),
    ("Ação Popular 1120375-77", "Lei 4.717/1965 (Ação Popular)", 2),
    ("Parecer CAEX 15789370", "Lei 11.428/2006 (Mata Atlântica)", 2),
    ("Portaria SGM 257/2025", "Portaria SGM 258/2025", 2),
    ("Portaria SGM 155/2026", "Portaria SGM 159/2026", 3),
    ("Portaria SGM 159/2026", "Portaria SGM 258/2025", 2),
    ("Cautelar Antecedente 2024", "Contrato 0548/ARTESP/2025", 2),
    ("Ação Popular 1120375-77", "Contrato 0548/ARTESP/2025", 2),
    ("ACP 1500561-14 (MPSP)", "Contrato 0548/ARTESP/2025", 2),
]

df = pd.DataFrame(edges, columns=["source", "target", "weight"])

node_colors = {
    "Contrato 0548/ARTESP/2025": "#ed1c24",
    "Edital Lote 1 (02/2024)": "#ed1c24",
    "Decreto 68.695/2024": "#ed1c24",
    "Lei 14.133/2021 (Licitações)": "#ff9900",
    "Lei 12.587/2012 (PNMU)": "#ff9900",
    "Lei 4.717/1965 (Ação Popular)": "#ff9900",
    "Lei 7.347/1985 (LACP)": "#ff9900",
    "Resolução CONAMA 01/1986 (EIA/RIMA)": "#2e7d32",
    "Lei 11.428/2006 (Mata Atlântica)": "#2e7d32",
    "Portaria SGM 257/2025": "#1565c0",
    "Portaria SGM 258/2025": "#1565c0",
    "Portaria SGM 155/2026": "#1565c0",
    "Portaria SGM 159/2026": "#1565c0",
    "Parecer CAEX 15789370": "#6a1b9a",
    "ACP 1500561-14 (MPSP)": "#6a1b9a",
    "Ação Popular 1120375-77": "#6a1b9a",
    "Inquérito Civil 0482.0000571/2024": "#6a1b9a",
    "Cautelar Antecedente 2024": "#6a1b9a",
}

# matriz de adjacência (não-direcionada)
nodes = sorted(set([s for s, _, _ in edges] + [t for _, t, _ in edges]))
adj = pd.DataFrame(0, index=nodes, columns=nodes, dtype=int)
for s, t, w in edges:
    adj.loc[s, t] = w
    adj.loc[t, s] = w

colors = [node_colors.get(n, "#888888") for n in nodes]

d3 = Elasticgraph(charge=250, dark_mode=False)
d3.graph(adj)
d3.set_node_properties(color=colors, size=14)
d3.show(
    title="Malha normativa — Nova Raposo",
    filepath="mnrn/assets/grafos/malha-normativa-nova-raposo.htm",
    showfig=False,
    overwrite=True,
)
print("grafo gerado:", len(nodes), "nos,", len(edges), "arestas")
