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
            line=dict(width=0.5, color="black")
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

@st.cache_data
def build_graph_with_target(plot_nodes: pd.DataFrame, plot_edges: pd.DataFrame, metric: str):
    """Create a Plotly network figure from node and edge tables, with top nodes of the target metric in a different color."""
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

    dataColumns = ["node", "community", "degree", "betweenness"]
    
    if metric == "betweenness":
        scaleText = "Betweenness Centrality"
    elif metric == "degree":
        scaleText = "Degree"
    elif metric == "icm_degree_frequency":
        scaleText = "Times Activated"
        dataColumns.append("icm_degree_frequency")
    elif metric == "icm_betweenness_frequency":
        scaleText = "Times Activated"
        dataColumns.append("icm_betweenness_frequency")
    else:
        scaleText = "community"
    
    metric_values = plot_nodes[metric]
    metric_min = metric_values.min()
    metric_max = metric_values.max()

    if metric != "betweenness" or metric != "degree":
        metric_min = 1
        metric_max = 1

    if metric_max == metric_min:
        scaled_sizes = [10] * len(plot_nodes)
    else:
        scaled_sizes = 12 + 20 * (metric_values - metric_min) / (metric_max - metric_min)

    node_trace = go.Scatter(
        x=plot_nodes["x"],
        y=plot_nodes["y"],
        mode="markers+text",
        textposition="top center",
        customdata=plot_nodes[dataColumns].values,
        hovertemplate=(
            "Node: %{customdata[0]}<br>"
            "Community: %{customdata[1]}<br>"
            "Degree: %{customdata[2]}<br>"
            "Betweenness: %{customdata[3]:.3f}<br>"
            "Times Activated: %{customdata[4]}<br>"
        ),
        marker=dict(
            size=scaled_sizes,
            color=plot_nodes[metric],
            colorscale="Jet",
            line=dict(width=0.5, color="black"),
            showscale=True,
            colorbar=dict(title=scaleText)
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

@st.cache_data
def build_deg_dist(degree_df):
    fig = px.histogram(degree_df)

    return fig