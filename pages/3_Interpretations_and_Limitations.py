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
    #### Research Question 1:

    #### Research Question 2: Are there nodes that allow the activation of more people or communities?
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


    ### Research Question 3: What can be changed to reduce the spread of activation?
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