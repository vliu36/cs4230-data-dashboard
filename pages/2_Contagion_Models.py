import streamlit as st

dates = ["05-03-2009", "05-13-2009", "05-23-2009", "06-04-2009", "06-14-2009", "06-24-2009", "07-05-2009", "07-15-2009"]

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
    ["highest betweenness", "highest degree", "highest degree prioritizing communities"],
    key="selected_target_icm"
)
st.text("TODO: Add network visualization here")
n_seed_icm = st.slider("Number of seed nodes", 1, 20, 5, key="slider_n_icm")
st.divider()

st.header(body="Linear Threshold Model", anchor="linear-threshold-model")
selected_target_ltm = st.selectbox(
    "Select seed node preference",
    ["highest betweenness", "highest degree", "highest degree prioritizing communities"],
    key="selected_target_ltm"
)
st.text("TODO: Add network visualization here")
n_seed_ltm = st.slider("Number of seed nodes", 1, 20, 5, key="slider_n_ltm")

# st.markdown(
# """
# This section will include:
# - contagion model analysis using different seed nodes
# - visualization of spread given different seed nodes
# - aims to answer 2nd research question
# """
# )