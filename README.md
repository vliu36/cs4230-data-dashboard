# CS4230-Project

Our project focuses on the patterns of human interaction and contact in a public space by plotting a network of nodes 
representing sustained face-to-face proximity. This topic could be applied to study the mechanisms of disease spread, 
information spread, or adoption of trends. This means although this dataset is based on simulated face-to-face exposure, 
patterns identified could be applied to real-world scenarios where something spreads from close contact. We can also use 
contagion models to predict the spread of diseases or information through the exposure network.

**Research Questions**
1. What is the structure of the simulated real-world network?
2. Are there nodes that allow the activation of more people or communities?
3. What can be changed to reduce the spread of activation?

## Dataset Source
This dataset is obtained from [SocioPatterns's "Infectious" exhibition](https://sociopatterns.org/datasets.html#data-infectious-sociopatterns). Information on the dataset can be found in their paper, "What's in a crowd? Analysis of face-to-face behavioral networks". 

## How to Run
1. Clone the repository to your local device
2. In a Python environment, run ``pip install streamlit plotly pandas networkx`` or ``pip install -r requirements.txt``
3. In the root directory, run ``streamlit run Overview.py``
