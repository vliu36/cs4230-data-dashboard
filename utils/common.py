import streamlit as st
import networkx as nx

@st.cache_data

def display_basic_metrics(stats):
    st.header(body="Graph Stats", anchor="graph-stats")
    
    col1, col2 = st.columns(2)
    col1.metric("Nodes", stats["n"], border=True)
    col2.metric("Edges", stats["m"], border=True)

    col3, col4, col5 = st.columns(3)
    col3.metric("Average Degree", round(stats["avg_deg"], 4), border=True)
    col4.metric("Clustering Coefficient", round(stats["C"], 4), border=True)
    col5.metric("Connected Components", stats["cc"], border=True)
    
    st.text("Giant Connected Component metrics:")
    col6, col7 = st.columns(2)
    col6.metric("Nodes", stats["gcc_size"], border=True)
    col7.metric("Average Path Length", round(stats["L_gcc"], 4), border=True)

