import networkx as nx
import random
import streamlit as st


def get_greatest_weight(G):

  max_weight = 0
  for edge in G.edges():
    current_edge_weight = G.get_edge_data(edge[0], edge[1])["weight"]

    if current_edge_weight > max_weight:
      max_weight = current_edge_weight

  return max_weight

def independent_cascade(G, seed_nodes):

  # List of activated nodes that have not attempted to activate their neighbors
  node_activators = seed_nodes[:]

  # List of all activated nodes
  activated_nodes = seed_nodes[:]

  # Create initial network with seed nodes
  activation_network = nx.Graph()
  activation_network.add_nodes_from(seed_nodes)

  # Contains the greatest weight found in the network which will be used
  # as the denominator for the probability
  greatest_edge_weight = get_greatest_weight(G)

  # Continues activation spread as long as there are nodes that have not
  # attempted to activate their neighbors
  while len(node_activators) != 0:

    # Retrieves the first node in the list
    current_node = node_activators.pop(0)

    # Evaluates each neighbor of the current node
    for neighbor in G.neighbors(current_node):
      current_weight = G.get_edge_data(current_node, neighbor)["weight"]
      p = current_weight / greatest_edge_weight
      random_number = random.random()

      # Activates neighbor if the random number is less than p and is
      # not an activated node
      if (random_number < p) and (neighbor not in activated_nodes):
        node_activators.append(neighbor)
        activated_nodes.append(neighbor)
        activation_network.add_node(neighbor)
        activation_network.add_edge(current_node, neighbor)

  return activation_network


def get_highest_degree_nodes(G):
    highest_degree_list = []

    # For each network, stores the top 5 highest degree nodes into the dictionary
    degrees = [(degree[0], degree[1] / (len(list(G.nodes())) - 1)) for degree in G.degree()]
    degrees = sorted(degrees, key=lambda x: x[1], reverse=True)
    for i in range(5):
        highest_degree_list.append(degrees[i])
    
    return [node for node, degree in highest_degree_list]

def get_highest_betweenness_nodes(G):
    btwn_cent_list = []

    # For each network, stores the top 5 highest betweenness nodes into the dictionary
    btwn_cent = nx.betweenness_centrality(G, normalized=True).items()
    btwn_cent = sorted(btwn_cent, key=lambda x: x[1], reverse=True)
    for i in range(5):
        btwn_cent_list.append(btwn_cent[i])
    
    return [node for node, degree in btwn_cent_list]
def get_random_seed_nodes(G):
    random_seed_node_list = []

    for i in range(5):
        network_size = len(G.nodes())
        random_number = random.randrange(0, network_size)
        while (random_number in random_seed_node_list):
            random_number = random.randrange(0, network_size)
        random_seed_node_list.append(random_number)

    return random_seed_node_list

def get_independent_cascade_dict(G, seed_node_type, num_of_iterations):

    activation_frequency_dict = dict()

    if seed_node_type == "degree":
        seed_nodes = get_highest_degree_nodes(G)
    elif seed_node_type == "betweenness":
        seed_nodes = get_highest_betweenness_nodes(G)
    else:
        seed_nodes = get_random_seed_nodes(G)

    for iteration in range(num_of_iterations):
        cascade_network = independent_cascade(G, seed_nodes)
        for node in cascade_network.nodes():
            activation_frequency_dict[node] = activation_frequency_dict.get(node, 0) + 1

    return activation_frequency_dict