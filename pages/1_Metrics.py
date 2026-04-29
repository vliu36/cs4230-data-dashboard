import streamlit as st

st.set_page_config(
    page_title="Metrics - Contagion in the Gallery",
    layout="wide"
)

st.markdown("# Metrics")
st.sidebar.header("Metrics")
st.markdown(
"""
This section will include:
- structural analysis of each network aiming to answer the first research question
- degree distribution figures for each network
- comparisons of each network to characteristics of a real-world network
- visualization of high betweenness centrality and high degree nodes (may be moved to contagion section)
"""
)