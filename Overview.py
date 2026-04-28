import streamlit as st
import networkx as nx
import pandas as pd

from utils.load_data import load_network_data

st.set_page_config(
    page_title="Overview",
    page_icon="✔️",
    layout="wide"
)

# Loads data from the 8 datasets in graph and dataframe formats
dates = ["07-15", "07-05", "06-24", "06-14", "06-04", "05-23", "05-13", "05-03"]
G_dict = {}
node_df_dict = {}
edge_df_dict = {}

for date in dates:
    G, node_df, edge_df = load_network_data(f"./datasets/{date}.gml")
    G_dict.update({date: G})
    node_df_dict.update({date: node_df})
    edge_df_dict.update({date: edge_df})

st.title("Contagion in the Gallery: Examining Diffusion in Real-World Networks")
st.write(
    "Our project focuses on the patterns of human interaction and contact in a public space by plotting a network of nodes representing " \
    "sustained face-to-face proximity. This topic could be applied to study the mechanisms of disease spread, information spread, or adoption of trends. " \
    "This means although this dataset is based on simulated face-to-face exposure, patterns identified could be applied to real-world scenarios where something spreads from close contact. " \
    "We can also use contagion models to predict the spread of diseases or information through the exposure network."
)

