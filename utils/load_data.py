import networkx as nx
import pandas as pd
import streamlit as st

@st.cache_data

def load_network_data(path):
    G = nx.read_gml(path, label=None)

    degree_dict = dict(G.degree())
    degree_centrality = nx.degree_centrality(G)
    betweenness = nx.betweenness_centrality(G)
    closeness = nx.closeness_centrality(G)
    eigenvector = nx.eigenvector_centrality(G, max_iter=1000)

    communities = list(nx.community.greedy_modularity_communities(G))
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
        "x": [positions[n][0] for n in G.nodes()],
        "y": [positions[n][1] for n in G.nodes()]
    })

    edge_df = pd.DataFrame(list(G.edges()), columns=["source", "target"])
    return G, node_df, edge_df

def giant_component_subgraph(G):
    """Return the subgraph of the largest connected component (undirected)."""
    if G.number_of_nodes() == 0:
        return G.copy()
    components = list(nx.connected_components(G))
    gcc_nodes = max(components, key=len)
    return G.subgraph(gcc_nodes).copy()