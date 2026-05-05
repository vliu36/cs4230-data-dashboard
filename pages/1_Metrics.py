import streamlit as st
from utils.figure_builder import build_figure_with_target
from utils.load_data import graph_stats
from Overview import G_dict, node_df_dict, edge_df_dict

dates = ["05-03-2009", "05-13-2009", "05-23-2009", "06-04-2009", "06-14-2009", "06-24-2009", "07-05-2009", "07-15-2009"]

st.set_page_config(
    page_title="Metrics - Contagion in the Gallery",
    layout="wide"
)

st.markdown("# Metrics")
st.sidebar.header("Metrics")
st.sidebar.markdown("- [Graph Stats](#network-structure-overview)")

st.markdown(
"""
Out of data recorded across multiple months, we picked out 8 networks in total, one for every 10th day starting on May 3rd. 
Since we were provided with over 60 datasets, selecting every 10th day allow us to perform analysis across all datasets 
without dealing with an overwhelming amount of data. 

Each day tells its own story:
"""
)

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(dates)

with tab1:
    date = dates[0]
    stats = graph_stats(G_dict[date])

    st.header(body="Graph Stats",
              anchor="network-structure-overview"
              )
    st.text(f"This network has {stats["n"]} nodes and {stats["m"]} edges.")
    st.text(f"The average degree is {stats["avg_deg"]}")
    st.text(f"The global clustering coefficient is {stats["C"]}")

    fig_btwn_network = build_figure_with_target(node_df_dict[date], edge_df_dict[date], "betweenness")
    st.plotly_chart(fig_btwn_network, width="stretch", key="Betweenness Chart 1")

with tab2:
    date = dates[1]
    stats = graph_stats(G_dict[date])
    
    st.header(body="Graph Stats",
              anchor="network-structure-overview"
              )
    st.text(f"This network has {stats["n"]} nodes and {stats["m"]} edges.")
    st.text(f"The average degree is {stats["avg_deg"]}")
    st.text(f"The global clustering coefficient is {stats["C"]}")

    fig_btwn_network = build_figure_with_target(node_df_dict[date], edge_df_dict[date], "betweenness")
    st.plotly_chart(fig_btwn_network, width="stretch", key="Betweenness Chart 2")

with tab3:
    date = dates[2]
    stats = graph_stats(G_dict[date])

    st.header(body="Graph Stats",
              anchor="network-structure-overview"
              )
    st.text(f"This network has {stats["n"]} nodes and {stats["m"]} edges.")
    st.text(f"The average degree is {stats["avg_deg"]}")
    st.text(f"The global clustering coefficient is {stats["C"]}")

    fig_btwn_network = build_figure_with_target(node_df_dict[date], edge_df_dict[date], "betweenness")
    st.plotly_chart(fig_btwn_network, width="stretch", key="Betweenness Chart 3")
    
with tab4:
    date = dates[3]
    stats = graph_stats(G_dict[date])

    st.header(body="Graph Stats",
              anchor="network-structure-overview"
              )
    st.text(f"This network has {stats["n"]} nodes and {stats["m"]} edges.")
    st.text(f"The average degree is {stats["avg_deg"]}")
    st.text(f"The global clustering coefficient is {stats["C"]}")

    fig_btwn_network = build_figure_with_target(node_df_dict[date], edge_df_dict[date], "betweenness")
    st.plotly_chart(fig_btwn_network, width="stretch", key="Betweenness Chart 4")
    
with tab5:
    date = dates[4]
    stats = graph_stats(G_dict[date])

    st.header(body="Graph Stats",
              anchor="network-structure-overview"
              )
    st.text(f"This network has {stats["n"]} nodes and {stats["m"]} edges.")
    st.text(f"The average degree is {stats["avg_deg"]}")
    st.text(f"The global clustering coefficient is {stats["C"]}")

    fig_btwn_network = build_figure_with_target(node_df_dict[date], edge_df_dict[date], "betweenness")
    st.plotly_chart(fig_btwn_network, width="stretch", key="Betweenness Chart 5")
    
with tab6:
    date = dates[5]
    stats = graph_stats(G_dict[date])

    st.header(body="Graph Stats",
              anchor="network-structure-overview"
              )
    st.text(f"This network has {stats["n"]} nodes and {stats["m"]} edges.")
    st.text(f"The average degree is {stats["avg_deg"]}")
    st.text(f"The global clustering coefficient is {stats["C"]}")

    fig_btwn_network = build_figure_with_target(node_df_dict[date], edge_df_dict[date], "betweenness")
    st.plotly_chart(fig_btwn_network, width="stretch", key="Betweenness Chart 6")

with tab7:
    date = dates[6]
    stats = graph_stats(G_dict[date])

    st.header(body="Graph Stats",
              anchor="network-structure-overview"
              )
    st.text(f"This network has {stats["n"]} nodes and {stats["m"]} edges.")
    st.text(f"The average degree is {stats["avg_deg"]}")
    st.text(f"The global clustering coefficient is {stats["C"]}")

    fig_btwn_network = build_figure_with_target(node_df_dict[date], edge_df_dict[date], "betweenness")
    st.plotly_chart(fig_btwn_network, width="stretch", key="Betweenness Chart 7")

with tab8:
    date = dates[7]
    stats = graph_stats(G_dict[date])
    
    st.header(body="Graph Stats",
              anchor="network-structure-overview"
              )
    st.text(f"This network has {stats["n"]} nodes and {stats["m"]} edges.")
    st.text(f"The average degree is {stats["avg_deg"]}.")
    st.text(f"The global clustering coefficient is {stats["C"]}.")

    fig_btwn_network = build_figure_with_target(node_df_dict[date], edge_df_dict[date], "betweenness")
    st.plotly_chart(fig_btwn_network, width="stretch", key="Betweenness Chart 8")
    
# st.markdown(
# """
# This section will include:
# - structural analysis of each network aiming to answer the first research question
# - degree distribution figures for each network
# - comparisons of each network to characteristics of a real-world network
# - visualization of high betweenness centrality and high degree nodes (may be moved to contagion section)
# """
# )