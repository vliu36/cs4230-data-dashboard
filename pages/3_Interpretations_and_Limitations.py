import streamlit as st

st.set_page_config(
    page_title="Interpretations and Limitations - Contagion in the Gallery",
    layout="wide"
)

st.markdown("# Interpretations and Limitations")
st.sidebar.markdown(
    """
    ## Interpretations and Limitations
    - [Interpretations](#interpretations)
    - [Limitations](#limitations)
    """)

st.header("Interpretations", anchor="interpretations")
st.markdown(
    """
    **Key Takeaways:** 
    - The network structure shows that the simulation is a limited representation of a real-world network under a certain context.
    - High betweenness centrality nodes have higher average spread within the simulated networks.
    - Reducing the number of bridges and local bridges can reduce diffusion.

    #### What is the structure of the simulated real-world network?

    The characteristics of most of the networks slightly differ from that of a real-world network. 
    For the 8 sample networks, the range for the clustering coefficient is around 0.36 to 0.58. For the giant components of the 8 sample networks, 
    the range is around 0.36 to 0.67. Since the clustering coefficient is overall moderate, this suggests that there may be a substantial number of 
    local bridges or bridges in the sample networks. Furthermore, a moderate clustering coefficient may imply the formation of loose groups where people 
    interact with groups that have some leaving and others who already interacted with others joining. Looking at the degree distribution, there are hubs 
    within this network, but more nodes have a higher degree centrality compared to that of a real-world network. Some networks, such as the ones on 05-03, 
    05-13, and 07-15 are somewhat heavy-tailed. The networks of 6-24, 6-14, and 5-23 don't show a strong similarity with that of a heavy-tailed pattern, but 
    still show degree distributions displaying fewer high degree nodes and greater low degree nodes. The remaining networks show little evidence of containing 
    potential hubs.

    These findings could be explained by the fact that the data was gathered from visitors at a Science Gallery, where visitors tend to form "groups" 
    that move from exhibit to exhibit. The highly clustered nodes may be visitors that are viewing exhibits alongside other visitors of the same "group" 
    and bridges form when some visitors move on to another exhibit at varying times. This explains why the simulated network differs slightly in terms 
    of structure compared to real-world networks. It also shows the extent to which we can apply the patterns from these networks to the real world.

    #### Are there nodes that allow the activation of more people or communities?
    For the independent cascade model, the highest betweenness seed nodes nodes overall did the best at spreading
    activation. While not as good at spreading activation as the highest betwenness seed nodes, the high degree 
    seed nodes selected across communities also spread activation better than the high degree seed nodes.
    For the independent cascade model, since it focuses on spread from one neighbor at a time, this could 
    be representative of disease spread. So in the context of disease spread, our results show that high 
    betweenness centrality seed nodes are most prone to spreading disease.

    For the linear threshold mode, the highest betwenness and randomly selected seed nodes did the best. The
    high degree seed nodes did surprisingly worse at spreading activation. For the linear threshold model, 
    since this focuses on influence from multiple people to a target node, this can be representative of an 
    idea spreading. In that context, if the threshold is 15 interactions, then it takes 15 interactions across 
    multiple neighbors to convince a target node of an idea.

    In the context of the networks, high betweenness centrality nodes are those who bridge "groups" of visitors. This could be singular 
    or small groups of visitors who move between exhibits ahead of those they entered the gallery with. This could also be people
    who stay at a single exhibit and interact with multiple clusters. In this case, these people would additionally have a high degree
    centrality. In other network models, such as preferential attachment, these people could be hubs that connect to many
    low-degree nodes. However, the degree distribution of these networks show that the average degree is rather high, so it is 
    more likely that hub nodes will additionally connect to nodes with a decent number of connections themselves. This supports
    the idea of "groups" in the gallery, where people tend to spend time in close proximity with those they visit with as they
    travel from exhibit to exhibit, and can explain how high betweenness centrality nodes could also be hubs in this scenario.

    #### What can be changed to reduce the spread of activation?
    Based on the results for the independent cascade model, the best way to reduce the spread of activation is to 
    isolate nodes with high betweenness centrality. In the case of disease spread, it would be to isolate infected 
    individuals who have high betweenness centrality. Additionally, it could even be to isolate individuals who are 
    undetermined to be infected but also have a high betweenness centrality in the event of rapid spread. 

    Based on the results of the independent cascade model, the best way to reduce the spread of activation is to 
    also address high betweenness centrality nodes. So for instance, if a rumor is spreading in a highly populated 
    area, it would be best to address the fallacy of a rumor to people who have high centrality before the rumor reaches them.

    """
)
st.divider()

st.header("Limitations", anchor="limitations")
st.markdown("""
    #### Contagion Model Limitations
    For both contagion models, we did very limited testing, only sticking with 50 seed nodes and using only 15 as the 
    threshold for the linear threshold model. Due to this, our findings have very limited interpretations. In the case of
    the linear threshold model, our interpretations are only based on the threshold of 15 interactions which may not be
    applicable to different scenarios. 
            
    Also, initially we started with only 5 seed nodes. Our results were pretty different from what they are now for the
    independent cascade model. Initially, highest degree seed nodes did better at spreading activation. We changed it to
    50 seed nodes as the spread was very small overall, so it was difficult to gauge the behavior of spread. However, with
    50 seed nodes, now it seems that high betweenness seed nodes do better. Since we only made interpretations for 50 seed
    nodes, we were unable to discuss the behavior of varying seed nodes in the context of activation. 
""")


# st.markdown(
# """
# This section will include:
# - synthesis of information in the previous sections to answer the research questions
# - limitations of the study
# """
# )