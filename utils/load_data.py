import networkx as nx
import pandas as pd
import streamlit as st
from utils.contagion_helpers import get_independent_cascade_dict

@st.cache_data

def load_network_data(path):
    G = nx.read_gml(path, label=None)

    degree_dict = dict(G.degree())
    degree_centrality = nx.degree_centrality(G)
    betweenness = nx.betweenness_centrality(G)
    closeness = nx.closeness_centrality(G)
    eigenvector = nx.eigenvector_centrality(G, max_iter=1000)

    communities = list(nx.community.greedy_modularity_communities(G))
    icm_degree_frequency = get_independent_cascade_dict(G, "degree", 200)
    icm_betweenness_frequency = get_independent_cascade_dict(G, "betweenness", 200)
    icm_random_frequency = get_independent_cascade_dict(G, "random", 200)

    community_map = {}
    for i, community in enumerate(communities):
        for node in community:
            community_map[node] = i

    positions = nx.spring_layout(G, seed=42)

    node_df = pd.DataFrame({
        "node": list(G.nodes()),
        "degree": [degree_dict[n] for n in G.nodes()],
        "degree_centrality": [degree_centrality[n] for n in G.nodes()],
        "betweenness": [betweenness[n] for n in G.nodes()],
        "closeness": [closeness[n] for n in G.nodes()],
        "eigenvector": [eigenvector[n] for n in G.nodes()],
        "community": [community_map[n] for n in G.nodes()],
        "icm_degree_frequency": [float(icm_degree_frequency[n]) if n in icm_degree_frequency.keys() else 0 for n in G.nodes()],
        "icm_betweenness_frequency": [float(icm_betweenness_frequency[n]) if n in icm_betweenness_frequency.keys() else 0 for n in G.nodes()],
        "icm_random_frequency": [float(icm_random_frequency[n]) if n in icm_random_frequency.keys() else 0 for n in G.nodes()],
        "x": [positions[n][0] for n in G.nodes()],
        "y": [positions[n][1] for n in G.nodes()]
    })

    edge_df = pd.DataFrame(list(G.edges()), columns=["source", "target"])

    degrees = pd.DataFrame({
        "degree": [d for _, d in G.degree()]
    })
    
    return G, node_df, edge_df, degrees

def giant_component_subgraph(G):
    """Return the subgraph of the largest connected component (undirected)."""
    if G.number_of_nodes() == 0:
        return G.copy()
    components = list(nx.connected_components(G))
    gcc_nodes = max(components, key=len)
    return G.subgraph(gcc_nodes).copy()

def graph_stats(G):
    """
    Compute basic stats:
    - n, m
    - avg degree
    - average clustering (nx.average_clustering)
    - average shortest path length on giant component (if >= 2 nodes)
    - number of components
    """
    n = G.number_of_nodes()
    m = G.number_of_edges()
    avg_deg = (2*m / n) if n > 0 else float('nan')
    C = nx.average_clustering(G) if n > 0 else float('nan')
    cc = nx.number_connected_components(G)

    GCC = giant_component_subgraph(G)
    if GCC.number_of_nodes() >= 2 and nx.is_connected(GCC):
        L = nx.average_shortest_path_length(GCC)
    else:
        L = float('nan')

    return {"n": n, "m": m, "avg_deg": avg_deg, "C": C, "L_gcc": L, "gcc_size": GCC.number_of_nodes(), "cc": cc}