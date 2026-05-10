import streamlit as st
from utils.figure_builder import build_graph_with_target, build_deg_dist
from Overview import G_dict, node_df_dict, edge_df_dict, dates, icm_degree_spread_info_dict, icm_betweenness_spread_info_dict, icm_random_spread_info_dict

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
selected_target_icm = st.selectbox(
    "Select seed node preference",
    ["highest betweenness", "highest degree", "highest degree prioritizing communities", "random"],
    key="selected_target_icm"
)

seed_node_type = "icm_betweenness_frequency"
activation_distribution = icm_betweenness_spread_info_dict[selected_date][0]
if selected_target_icm == "highest betweennness":
    seed_node_type = "icm_betweenness_frequency"
    activation_distribution = icm_betweenness_spread_info_dict[selected_date][0]
elif selected_target_icm == "highest degree":
    seed_node_type = "icm_degree_frequency"
    activation_distribution = icm_degree_spread_info_dict[selected_date][0]
elif selected_target_icm == "random":
    seed_node_type = "icm_random_frequency"
    activation_distribution = icm_random_spread_info_dict[selected_date][0]


fig_btwn_network = build_graph_with_target(node_df_dict[selected_date], edge_df_dict[selected_date], seed_node_type)
fig_deg_dist = build_deg_dist(activation_distribution)
st.plotly_chart(fig_btwn_network, width="stretch")
st.plotly_chart(fig_deg_dist, width="stretch")

n_seed_icm = st.slider("Number of seed nodes", 1, 20, 5, key="slider_n_icm")
st.divider()

st.header(body="Linear Threshold Model", anchor="linear-threshold-model")
selected_target_ltm = st.selectbox(
    "Select seed node preference",
    ["highest betweenness", "highest degree", "highest degree prioritizing communities"],
    key="selected_target_ltm"
)
n_seed_ltm = st.slider("Number of seed nodes", 1, 20, 5, key="slider_n_ltm")

# st.markdown(
# """
# This section will include:
# - contagion model analysis using different seed nodes
# - visualization of spread given different seed nodes
# - aims to answer 2nd research question
# """
# )