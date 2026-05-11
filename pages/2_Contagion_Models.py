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

# st.markdown(
# """
# This section will include:
# - contagion model analysis using different seed nodes
# - visualization of spread given different seed nodes
# - aims to answer 2nd research question
# """
# )