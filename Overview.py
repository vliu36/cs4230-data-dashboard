import streamlit as st
import networkx as nx
import pandas as pd

from utils.load_data import load_network_data, giant_component_subgraph
from utils.figure_builder import build_graph

st.set_page_config(
    page_title="Overview - Contagion in the Gallery",
    page_icon="✔️",
    layout="wide"
)
st.sidebar.header("Overview")
st.sidebar.markdown("- [What does this graph represent?](#what-does-this-graph-represent)")

# Loads network, subgraph from the 8 datasets in graph and dataframe formats
dates = ["05-03-2009", "05-13-2009", "05-23-2009", "06-04-2009", "06-14-2009", "06-24-2009", "07-05-2009", "07-15-2009"]
G_dict = {}
node_df_dict = {}
edge_df_dict = {}

for date in dates:
    G, node_df, edge_df = load_network_data(f"./datasets/{date}.gml")
    G_dict.update({date: G})
    node_df_dict.update({date: node_df})
    edge_df_dict.update({date: edge_df})

st.markdown("## Contagion in the Gallery: Examining Diffusion in Real-World Networks")
st.markdown(
"""
Our project focuses on the patterns of human interaction and contact in a public space by plotting a network of nodes 
representing sustained face-to-face proximity. This topic could be applied to study the mechanisms of disease spread, 
information spread, or adoption of trends. This means although this dataset is based on simulated face-to-face exposure, 
patterns identified could be applied to real-world scenarios where something spreads from close contact. We can also use 
contagion models to predict the spread of diseases or information through the exposure network.

**Research Questions**
1. What is the structure of the simulated real-world network?
2. Are there nodes that allow the activation of more people or communities?
3. What can be changed to reduce the spread of activation?
"""
)

st.header(
    body="What does this graph represent?",
    anchor="what-does-this-graph-represent"
)
st.markdown(
"""
- **Nodes:** visitors at the Science Gallery in Dublin (people).\n
- **Edges:** people who spent time with each other within close proximity.
- The graph is undirected.
- The graph is weighted, with weights representing the number of times two nodes were in close, face-to-face proximity with one another.
- There are 8 datasets in total, each representing a different day at the Science Gallery in Dublin.
"""
)
selected_date = st.selectbox(
        "Select a date",
        dates,
        key="selected_date"
    )

fig_network = build_graph(node_df_dict[selected_date], edge_df_dict[selected_date])
st.plotly_chart(fig_network, width="stretch", key="Overview Chart")
st.dataframe(node_df_dict[selected_date][["node", "degree", "degree_centrality", "betweenness","closeness", "eigenvector", "community"]], width='stretch')