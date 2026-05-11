import streamlit as st
from utils.figure_builder import build_graph_with_target, build_deg_dist
from Overview import node_df_dict, edge_df_dict, dates, icm_degree_spread_info_dict, icm_betweenness_spread_info_dict, icm_degree_spread_out_spread_info_dict, icm_random_spread_info_dict, ltm_degree_spread_info_dict, ltm_betweenness_spread_info_dict, ltm_degree_spread_out_spread_info_dict, ltm_random_spread_info_dict

st.set_page_config(
    page_title="Contagion Models - Contagion in the Gallery",
    layout="wide"
)

st.markdown("# Contagion Models")
st.sidebar.markdown("""
                    ## Contagion Models
                    - [Independent Cascade Model](#independent-cascade-model)
                    - [Linear Threshold Model](#linear-threshold-model)
                    """)

st.markdown(
    """
    In order to identify nodes that increase the rate of diffusion in our networks, we utilized and compared different contagion models using different
    seed nodes. We used the independent cascade model and linear threshold models to examine simple and complex contagion. The probabilities of activation
    on each edge were calculated using the normalized weight of each edge provided by the dataset. For both models, we examined spread
    using seeds made up of high degree centrality nodes, high betweenness centrality nodes, and high degree centrality nodes within separate communities.
    """
)

selected_date = st.selectbox(
        "Select a date",
        dates,
        key="selected_date"
    )
st.divider()

st.header(body="Independent Cascade Model", anchor="independent-cascade-model")
st.markdown("""
            The activation metrics displayed below also includes the seed nodes. So the number represents the number of seed nodes
            plus the number of nodes that were activated. Each network has 50 seed nodes.
            """)
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
col1.metric("Highest Degree Seed Nodes Activated Average", icm_degree_spread_info_dict[selected_date][1], border=True)
col2.metric("Highest Betweenness Seed Nodes Activated Average", icm_betweenness_spread_info_dict[selected_date][1], border=True)
col3.metric("Highest Degree Seed Nodes Across Communities Activated Average", icm_degree_spread_out_spread_info_dict[selected_date][1], border=True)
col4.metric("Random Seed Nodes Activated Average", icm_random_spread_info_dict[selected_date][1], border=True)
selected_target_icm = st.selectbox(
    "Select seed node preference",
    ["highest betweenness", "highest degree", "highest degree prioritizing communities", "random"],
    key="selected_target_icm"
)

icm_seed_node_type = "icm_betweenness_frequency"
icm_activation_stats = icm_betweenness_spread_info_dict[selected_date]
if selected_target_icm == "highest betweennness":
    icm_seed_node_type = "icm_betweenness_frequency"
    icm_activation_stats = icm_betweenness_spread_info_dict[selected_date]
elif selected_target_icm == "highest degree":
    icm_seed_node_type = "icm_degree_frequency"
    icm_activation_stats = icm_degree_spread_info_dict[selected_date]
elif selected_target_icm == "highest degree prioritizing communities":
    icm_seed_node_type = "icm_degree_spread_out_frequency"
    icm_activation_stats = icm_degree_spread_out_spread_info_dict[selected_date]
elif selected_target_icm == "random":
    icm_seed_node_type = "icm_random_frequency"
    icm_activation_stats = icm_random_spread_info_dict[selected_date]

fig_network = build_graph_with_target(node_df_dict[selected_date], edge_df_dict[selected_date], icm_seed_node_type)
fig_spread_dist = build_deg_dist(icm_activation_stats[0])
st.plotly_chart(fig_network, width="stretch")
st.caption("Network visualization showing the frequency that nodes got activated throughout the 200 iterations. This network also colors the seed nodes so they're frequency are 200 by default.")
st.plotly_chart(fig_spread_dist, width="stretch")
st.caption("Histogram showing the distribution of spread throughout the 200 iterations. This histogram includes the seed nodes as part of the distribution as well.")

st.markdown("""
            Overall, highest betweenneess seed nodes spread activation the most. The highest degree seed nodes do not do as well at
            spreading activation. While not as good at spreading activation as betweenness nodes, highest degree seed nodes selected 
            across different communities did better at contagion spread than highest degree seed nodes not selected across different 
            communities. We see both highest betweenness and highest degree seed nodes selected across different communities doing 
            better than highest degree seed nodes especially in networks where highest degree seed nodes result in a clustered spread. 
            For instance, for the dataset of “5-13”, we see that the spread of the highest degree nodes clustered into small parts of 
            the network. On the other hand, the spread of the highest betweenness seed nodes are noticeably more spread out across the 
            biggest component in the network. The highest degree seed nodes prioritizing communities also show wider spread. This 
            behavior for highest degree seed nodes prioritizing different communities, highest betweenness seed nodes, and highest degree 
            seed nodes is shown in datasets “6-04” and “5-03” as well. From what is observed, the clustered spread for highest degree seems 
            to be due to the highest degree seed nodes being clustered unlike betweenness and highest degree seed nodes across different 
            communities. Even for the networks that don’t show this behavior, betweenness centrality and degree centrality nodes across 
            communities mostly had a higher average of spread compared to only degree centrality nodes.
            """)
st.divider()

st.header(body="Linear Threshold Model", anchor="linear-threshold-model")
st.markdown("""
            The activation metrics displayed below also includes the seed nodes. So the number represents the number of seed nodes
            plus the number of nodes that were activated. Each network has 50 seed nodes. The set threshold for all nodes of every
            network is 15.
            """)
col5, col6 = st.columns(2)
col7, col8 = st.columns(2)

col5.metric("Highest Degree Seed Nodes Activated", ltm_degree_spread_info_dict[selected_date], border=True)
col6.metric("Highest Betweenness Seed Nodes Activated", ltm_betweenness_spread_info_dict[selected_date], border=True)
col7.metric("Highest Degree Seed Nodes Across Communities Activated", ltm_degree_spread_out_spread_info_dict[selected_date], border=True)
col8.metric("Random Seed Nodes Activated", ltm_random_spread_info_dict[selected_date], border=True)

selected_target_ltm = st.selectbox(
    "Select seed node preference",
    ["highest betweenness", "highest degree", "highest degree prioritizing communities", "random"],
    key="selected_target_ltm"
)

ltm_seed_node_type = "ltm_betweenness_spread"
ltm_activation_spread = ltm_betweenness_spread_info_dict[selected_date]
if selected_target_ltm == "highest betweennness":
    ltm_seed_node_type = "ltm_betweenness_spread"
    ltm_activation_spread = ltm_betweenness_spread_info_dict[selected_date]
elif selected_target_ltm == "highest degree":
    ltm_seed_node_type = "ltm_degree_spread"
    ltm_activation_spread = ltm_degree_spread_info_dict[selected_date]
elif selected_target_ltm == "highest degree prioritizing communities":
    ltm_seed_node_type = "ltm_degree_spread_out_spread"
    ltm_activation_spread = ltm_degree_spread_out_spread_info_dict[selected_date]
elif selected_target_ltm == "random":
    ltm_seed_node_type = "ltm_random_spread"
    ltm_activation_spread = ltm_random_spread_info_dict[selected_date]

fig_network = build_graph_with_target(node_df_dict[selected_date], edge_df_dict[selected_date], ltm_seed_node_type)
st.plotly_chart(fig_network, width="stretch")
st.caption("Network visualization showing the nodes that activated. This network also colors the seed nodes so they are activated by default.")
st.markdown("""
            Based on the results of the linear threshold model, both highest betweenness and randomly selected seed nodes spread activation
            the most. Surprisingly, highest degree seed nodes did overall the worst. This is shown by the number of activated nodes across 
            all networks. The difference is especially noticeable when it seems that the highest degree seed nodes are clustered. For 
            instance, with the network for “5-13”, there are only 68 activated nodes for highest degree seed nodes. Looking at the network, 
            the number of activated nodes are all clustered, so even though it may be difficult to tell which nodes are seed nodes in the 
            graph visualization, since only 18 nodes were activated from the 50 seed nodes, the clustering of activated nodes shows that the 
            seed nodes were clustered in small parts of the graph. For "5-13", ompared to the highest degree seed nodes, all the other methods of 
            selecting seed nodes have over 100 activated seed nodes, all which are more spread out. It seems that in cases where all the 
            high degree seed nodes are near each other, activation spread is worst. Generally speaking however, random seed nodes and highest 
            betweenness seed nodes have greater spread for the majority of datasets.
            """)
# st.markdown(
# """
# This section will include:
# - contagion model analysis using different seed nodes
# - visualization of spread given different seed nodes
# - aims to answer 2nd research question
# """
# )