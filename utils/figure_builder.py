import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import streamlit as st

@st.cache_data

def build_graph(plot_nodes: pd.DataFrame, plot_edges: pd.DataFrame):
    """Create a Plotly network figure from node and edge tables."""
    edge_x = []
    edge_y = []

    node_lookup = plot_nodes.set_index("node")

    for _, row in plot_edges.iterrows():
        source = row["source"]
        target = row["target"]

        if source not in node_lookup.index or target not in node_lookup.index:
            continue

        x0, y0 = node_lookup.loc[source, ["x", "y"]]
        x1, y1 = node_lookup.loc[target, ["x", "y"]]

        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    edge_trace = go.Scatter(
        x=edge_x,
        y=edge_y,
        mode="lines",
        hoverinfo="none",
        line=dict(width=0.5, color="gray")
    )

    node_trace = go.Scatter(
        x=plot_nodes["x"],
        y=plot_nodes["y"],
        mode="markers+text",
        textposition="top center",
        customdata=plot_nodes[["node", "community", "degree", "betweenness"]].values,
        hovertemplate=(
            "Node: %{customdata[0]}<br>"
            "Community: %{customdata[1]}<br>"
            "Degree: %{customdata[2]}<br>"
            "Betweenness: %{customdata[3]:.3f}<br>"
        ),
        marker=dict(
            size=10,
            color=plot_nodes["community"],
            colorscale="Blues",
            line=dict(width=1, color="black"),
            showscale=True,
            colorbar=dict(title="Community")
        )
    )

    fig = go.Figure(data=[edge_trace, node_trace])
    fig.update_layout(
        showlegend=False,
        xaxis=dict(showgrid=False, zeroline=False, visible=False),
        yaxis=dict(showgrid=False, zeroline=False, visible=False),
        margin=dict(l=10, r=10, t=50, b=10),
        height=650
    )

    return fig