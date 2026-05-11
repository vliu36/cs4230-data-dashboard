import streamlit as st
from utils.figure_builder import build_graph_with_target, build_deg_dist
from utils.load_data import graph_stats
from utils.common import display_basic_metrics
from Overview import G_dict, node_df_dict, edge_df_dict, degree_df_dict

dates = ["05-03-2009", "05-13-2009", "05-23-2009", "06-04-2009", "06-14-2009", "06-24-2009", "07-05-2009", "07-15-2009"]

st.set_page_config(
    page_title="Metrics - Contagion in the Gallery",
    layout="wide"
)

st.markdown("# Metrics")
st.sidebar.markdown("""
                    ## Metrics
                    - [Graph Stats](#graph-stats)
                    - [Degree Centrality](#degree-centrality)
                    - [Betweenness Centrality](#betweenness-centrality)
                    - [Communities](#communities)
                    """)

st.markdown(
"""
Out of data recorded across multiple months, we picked out 8 networks in total, one for every 10th day starting on May 3rd. 
Since we were provided with over 60 datasets, selecting every 10th day allow us to perform analysis across all datasets 
without dealing with an overwhelming amount of data. 

For each dataset, we examined the characteristics of the network and compared them to characteristics of a real-world network.
Although these datasets are meant to simulate real-world interactions, most of them differ slightly to characteristics in real-world
networks, such as a heavy-tailed degree distribution and high clustering coefficient. We additionally identified high betweenness centrality,
high degree centrality, and community nodes for use in contagion modeling.
"""
)

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(dates)

with tab1:
    date = dates[0]
    stats = graph_stats(G_dict[date])

    display_basic_metrics(stats)
    fig_deg_dist = build_deg_dist(degree_df_dict[date])
    st.plotly_chart(fig_deg_dist, width="stretch")
    st.caption("Degree distribution of the selected network.")
    st.markdown("""
                The degree distribution for this network is slightly skewed right and the clustering coefficient is 
                on the lower end. However, the average path length is short like that of a real-world network.

                These characteristics show that the structure of this network slightly differs to that of a real-world
                network.
                """)
    st.divider()

    st.header(body="Degree Centrality", anchor="degree-centrality")
    fig_deg_network = build_graph_with_target(node_df_dict[date], edge_df_dict[date], "degree")
    st.plotly_chart(fig_deg_network, width="stretch")
    st.caption("Network visualization showing the highest degree centrality nodes.")
    st.divider()

    st.header(body="Betweenness Centrality", anchor="betweenness-centrality")
    fig_btwn_network = build_graph_with_target(node_df_dict[date], edge_df_dict[date], "betweenness")
    st.plotly_chart(fig_btwn_network, width="stretch")
    st.caption("Network visualization showing the highest betweenness centrality nodes.")
    st.divider()

    st.header(body="Communities", anchor="communities")
    fig_btwn_network = build_graph_with_target(node_df_dict[date], edge_df_dict[date], "community")
    st.plotly_chart(fig_btwn_network, width="stretch")
    st.caption("Network visualization showing its communities, according to the greedy modularity algorithm")


with tab2:
    date = dates[1]
    stats = graph_stats(G_dict[date])
    
    display_basic_metrics(stats)
    fig_deg_dist = build_deg_dist(degree_df_dict[date])
    st.plotly_chart(fig_deg_dist, width="stretch")
    st.caption("Degree distribution of the selected network.")
    st.markdown("""
                The degree distribution for this network is rather heavy-tailed and the clustering coefficient is 
                moderate. The average path length is also short like that of a real-world network.

                These characteristics show that the structure of this network is similar to that of a real-world
                network.
                """)
    st.divider()

    st.header(body="Degree Centrality", anchor="degree-centrality")
    fig_deg_network = build_graph_with_target(node_df_dict[date], edge_df_dict[date], "degree")
    st.plotly_chart(fig_deg_network, width="stretch")
    st.caption("Network visualization showing the highest degree centrality nodes.")
    st.divider()

    st.header(body="Betweenness Centrality", anchor="betweenness-centrality")
    fig_btwn_network = build_graph_with_target(node_df_dict[date], edge_df_dict[date], "betweenness")
    st.plotly_chart(fig_btwn_network, width="stretch")
    st.caption("Network visualization showing the highest betweenness centrality nodes.")
    st.divider()

    st.header(body="Communities", anchor="communities")
    fig_btwn_network = build_graph_with_target(node_df_dict[date], edge_df_dict[date], "community")
    st.plotly_chart(fig_btwn_network, width="stretch")
    st.caption("Network visualization showing its communities, according to the greedy modularity algorithm")

with tab3:
    date = dates[2]
    stats = graph_stats(G_dict[date])

    display_basic_metrics(stats)
    fig_deg_dist = build_deg_dist(degree_df_dict[date])
    st.plotly_chart(fig_deg_dist, width="stretch")
    st.caption("Degree distribution of the selected network.")
    st.markdown("""
                The degree distribution for this network is slightly skewed right and the clustering coefficient is 
                on the lower end. However, the average path length is short like that of a real-world network.

                These characteristics show that the structure of this network slightly differs to that of a real-world
                network.
                """)
    st.divider()

    st.header(body="Degree Centrality", anchor="degree-centrality")
    fig_deg_network = build_graph_with_target(node_df_dict[date], edge_df_dict[date], "degree")
    st.plotly_chart(fig_deg_network, width="stretch")
    st.caption("Network visualization showing the highest degree centrality nodes.")
    st.divider()

    st.header(body="Betweenness Centrality", anchor="betweenness-centrality")
    fig_btwn_network = build_graph_with_target(node_df_dict[date], edge_df_dict[date], "betweenness")
    st.plotly_chart(fig_btwn_network, width="stretch")
    st.caption("Network visualization showing the highest betweenness centrality nodes.")
    st.divider()

    st.header(body="Communities", anchor="communities")
    fig_btwn_network = build_graph_with_target(node_df_dict[date], edge_df_dict[date], "community")
    st.plotly_chart(fig_btwn_network, width="stretch")
    st.caption("Network visualization showing its communities, according to the greedy modularity algorithm")
    
with tab4:
    date = dates[3]
    stats = graph_stats(G_dict[date])

    display_basic_metrics(stats)
    fig_deg_dist = build_deg_dist(degree_df_dict[date])
    st.plotly_chart(fig_deg_dist, width="stretch")
    st.caption("Degree distribution of the selected network.")
    st.markdown("""
                The degree distribution for this network is heavy-tailed and the clustering coefficient is 
                moderate. The average path length is also short like that of a real-world network.

                These characteristics show that the structure of this network is similar to that of a real-world
                network.
                """)
    st.divider()

    st.header(body="Degree Centrality", anchor="degree-centrality")
    fig_deg_network = build_graph_with_target(node_df_dict[date], edge_df_dict[date], "degree")
    st.plotly_chart(fig_deg_network, width="stretch")
    st.caption("Network visualization showing the highest degree centrality nodes.")
    st.divider()

    st.header(body="Betweenness Centrality", anchor="betweenness-centrality")
    fig_btwn_network = build_graph_with_target(node_df_dict[date], edge_df_dict[date], "betweenness")
    st.plotly_chart(fig_btwn_network, width="stretch")
    st.caption("Network visualization showing the highest betweenness centrality nodes.")
    st.divider()

    st.header(body="Communities", anchor="communities")
    fig_btwn_network = build_graph_with_target(node_df_dict[date], edge_df_dict[date], "community")
    st.plotly_chart(fig_btwn_network, width="stretch")
    st.caption("Network visualization showing its communities, according to the greedy modularity algorithm")
    
with tab5:
    date = dates[4]
    stats = graph_stats(G_dict[date])

    display_basic_metrics(stats)
    fig_deg_dist = build_deg_dist(degree_df_dict[date])
    st.plotly_chart(fig_deg_dist, width="stretch")
    st.caption("Degree distribution of the selected network.")
    st.markdown("""
                The degree distribution for this network is slightly skewed right and the clustering coefficient is 
                on the lower end. However, the average path length is short like that of a real-world network.

                These characteristics show that the structure of this network slightly differs to that of a real-world
                network.
                """)
    st.divider()

    st.header(body="Degree Centrality", anchor="degree-centrality")
    fig_deg_network = build_graph_with_target(node_df_dict[date], edge_df_dict[date], "degree")
    st.plotly_chart(fig_deg_network, width="stretch")
    st.caption("Network visualization showing the highest degree centrality nodes.")
    st.divider()

    st.header(body="Betweenness Centrality", anchor="betweenness-centrality")
    fig_btwn_network = build_graph_with_target(node_df_dict[date], edge_df_dict[date], "betweenness")
    st.plotly_chart(fig_btwn_network, width="stretch")
    st.caption("Network visualization showing the highest betweenness centrality nodes.")
    st.divider()

    st.header(body="Communities", anchor="communities")
    fig_btwn_network = build_graph_with_target(node_df_dict[date], edge_df_dict[date], "community")
    st.plotly_chart(fig_btwn_network, width="stretch")
    st.caption("Network visualization showing its communities, according to the greedy modularity algorithm")
    
with tab6:
    date = dates[5]
    stats = graph_stats(G_dict[date])

    display_basic_metrics(stats)
    fig_deg_dist = build_deg_dist(degree_df_dict[date])
    st.plotly_chart(fig_deg_dist, width="stretch")
    st.caption("Degree distribution of the selected network.")
    st.markdown("""
                The degree distribution for this network is slightly skewed right and the clustering coefficient is 
                on the lower end. However, the average path length is short like that of a real-world network.

                These characteristics show that the structure of this network slightly differs to that of a real-world
                network.
                """)
    st.divider()

    st.header(body="Degree Centrality", anchor="degree-centrality")
    fig_deg_network = build_graph_with_target(node_df_dict[date], edge_df_dict[date], "degree")
    st.plotly_chart(fig_deg_network, width="stretch")
    st.caption("Network visualization showing the highest degree centrality nodes.")
    st.divider()

    st.header(body="Betweenness Centrality", anchor="betweenness-centrality")
    fig_btwn_network = build_graph_with_target(node_df_dict[date], edge_df_dict[date], "betweenness")
    st.plotly_chart(fig_btwn_network, width="stretch")
    st.caption("Network visualization showing the highest betweenness centrality nodes.")
    st.divider()

    st.header(body="Communities", anchor="communities")
    fig_btwn_network = build_graph_with_target(node_df_dict[date], edge_df_dict[date], "community")
    st.plotly_chart(fig_btwn_network, width="stretch")
    st.caption("Network visualization showing its communities, according to the greedy modularity algorithm")

with tab7:
    date = dates[6]
    stats = graph_stats(G_dict[date])

    display_basic_metrics(stats)
    fig_deg_dist = build_deg_dist(degree_df_dict[date])
    st.plotly_chart(fig_deg_dist, width="stretch")
    st.caption("Degree distribution of the selected network.")
    st.markdown("""
                The degree distribution for this network is closer to that of a normal distribution. However, the average path length is short like that of a real-world network.

                These characteristics show that the structure of this network slightly differs to that of a real-world
                network.
                """)
    st.divider()

    st.header(body="Degree Centrality", anchor="degree-centrality")
    fig_deg_network = build_graph_with_target(node_df_dict[date], edge_df_dict[date], "degree")
    st.plotly_chart(fig_deg_network, width="stretch")
    st.caption("Network visualization showing the highest degree centrality nodes.")
    st.divider()

    st.header(body="Betweenness Centrality", anchor="betweenness-centrality")
    fig_btwn_network = build_graph_with_target(node_df_dict[date], edge_df_dict[date], "betweenness")
    st.plotly_chart(fig_btwn_network, width="stretch")
    st.caption("Network visualization showing the highest betweenness centrality nodes.")
    st.divider()

    st.header(body="Communities", anchor="communities")
    fig_btwn_network = build_graph_with_target(node_df_dict[date], edge_df_dict[date], "community")
    st.plotly_chart(fig_btwn_network, width="stretch")
    st.caption("Network visualization showing its communities, according to the greedy modularity algorithm")

with tab8:
    date = dates[7]
    stats = graph_stats(G_dict[date])
    
    display_basic_metrics(stats)
    fig_deg_dist = build_deg_dist(degree_df_dict[date])
    st.plotly_chart(fig_deg_dist, width="stretch")
    st.caption("Degree distribution of the selected network.")
    st.markdown("""
                The degree distribution for this network is slightly skewed right and the clustering coefficient is 
                on the lower end. However, the average path length is short like that of a real-world network.

                These characteristics show that the structure of this network slightly differs to that of a real-world
                network.
                """)
    st.divider()

    st.header(body="Degree Centrality", anchor="degree-centrality")
    fig_deg_network = build_graph_with_target(node_df_dict[date], edge_df_dict[date], "degree")
    st.plotly_chart(fig_deg_network, width="stretch")
    st.caption("Network visualization showing the highest degree centrality nodes.")
    st.divider()

    st.header(body="Betweenness Centrality", anchor="betweenness-centrality")
    fig_btwn_network = build_graph_with_target(node_df_dict[date], edge_df_dict[date], "betweenness")
    st.plotly_chart(fig_btwn_network, width="stretch")
    st.caption("Network visualization showing the highest betweenness centrality nodes.")
    st.divider()

    st.header(body="Communities", anchor="communities")
    fig_btwn_network = build_graph_with_target(node_df_dict[date], edge_df_dict[date], "community")
    st.plotly_chart(fig_btwn_network, width="stretch")
    st.caption("Network visualization showing its communities, according to the greedy modularity algorithm")
    