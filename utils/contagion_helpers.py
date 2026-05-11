import networkx as nx
import streamlit as st
import random
from networkx.algorithms.community import greedy_modularity_communities



def get_greatest_weight(G):

  max_weight = 0
  for edge in G.edges():
    current_edge_weight = G.get_edge_data(edge[0], edge[1])["weight"]

    if current_edge_weight > max_weight:
      max_weight = current_edge_weight

  return max_weight

def get_highest_degree_nodes(G, num_of_seeds):
    highest_degree_list = []

    degrees = [(degree[0], degree[1] / (len(list(G.nodes())) - 1)) for degree in G.degree()]
    degrees = sorted(degrees, key=lambda x: x[1], reverse=True)
    for i in range(num_of_seeds):
        highest_degree_list.append(degrees[i])
    
    return [node for node, degree in highest_degree_list]

def get_highest_betweenness_nodes(G, num_of_seeds):
    btwn_cent_list = []

    btwn_cent = nx.betweenness_centrality(G, normalized=True).items()
    btwn_cent = sorted(btwn_cent, key=lambda x: x[1], reverse=True)
    for i in range(num_of_seeds):
        btwn_cent_list.append(btwn_cent[i])
    
    return [node for node, degree in btwn_cent_list]

def get_spread_out_highest_degree(G, num_of_seeds):  
    communities = greedy_modularity_communities(G)
    communities_copy = []

    for community in communities:
        communities_copy.append(list(community))

    num_of_communities = len(communities_copy)
    community_index = 0
    highest_degree_spread_out = []
    degree_centrality = nx.degree_centrality(G)


    for i in range(num_of_seeds):
        if community_index >= num_of_communities:
            community_index = 0

        while len(communities_copy[community_index]) == 0:
            community_index += 1
            if community_index >= num_of_communities:
                community_index = 0


        highest_degree_found = communities_copy[community_index][0]
        for node in communities_copy[community_index]:
            if degree_centrality[highest_degree_found] < degree_centrality[node]:
                highest_degree_found = node

        highest_degree_spread_out.append(highest_degree_found)
        communities_copy[community_index].remove(highest_degree_found)
        community_index += 1

    return highest_degree_spread_out

def get_random_seed_nodes(G, num_of_seeds):
    random.seed(7)
    random_seed_node_list = []

    for i in range(num_of_seeds):
        network_size = len(G.nodes())
        random_number = random.randrange(0, network_size)
        while (random_number in random_seed_node_list):
            random_number = random.randrange(0, network_size)
        random_seed_node_list.append(random_number)

    return random_seed_node_list

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

def get_independent_cascade_dict(G, seed_node_type, num_of_iterations, num_of_seeds=50):
    random.seed(7)
    activation_frequency_dict = dict()
    activation_spread_list = []

    if seed_node_type == "degree":
        seed_nodes = get_highest_degree_nodes(G, num_of_seeds)
    elif seed_node_type == "betweenness":
        seed_nodes = get_highest_betweenness_nodes(G, num_of_seeds)
    elif seed_node_type == "degree spread":
        seed_nodes = get_spread_out_highest_degree(G, num_of_seeds)
    else:
        seed_nodes = get_random_seed_nodes(G, num_of_seeds)

    for iteration in range(num_of_iterations):
        cascade_network = independent_cascade(G, seed_nodes)
        for node in cascade_network.nodes():
            activation_frequency_dict[node] = activation_frequency_dict.get(node, 0) + 1
        activation_spread_list.append(len(cascade_network))
    
    average = sum(activation_spread_list) / len(activation_spread_list)

    return activation_frequency_dict, activation_spread_list, average

def linear_threshold(G, seed_nodes, threshold):

    # List of activated nodes that have not attempted to activate their neighbors
    node_activators = seed_nodes[:]

    # List of all activated nodes
    activated_nodes = seed_nodes[:]

    # Create initial network with seed nodes
    activation_network = nx.Graph()
    activation_network.add_nodes_from(seed_nodes)

    # Continues activation spread as long as there are nodes that have not
    # attempted to activate their neighbors
    while len(node_activators) != 0:

        # Retrieves the first node in the list
        current_node = node_activators.pop(0)

        # Evaluates each neighbor of the current node
        for neighbor in G.neighbors(current_node):

            # Checks if the neighbor is inactive
            if neighbor not in activated_nodes:
                sum_of_weights = 0

                # Evaluates the neighbors of the inactive neighbor
                for neighbor_of_neighbor in G.neighbors(neighbor):

                    # Adds more weight to influence if the the inactive neighbor's neighbor is active
                    if neighbor_of_neighbor in activated_nodes:
                        current_weight = G.get_edge_data(neighbor, neighbor_of_neighbor)["weight"]
                        sum_of_weights += current_weight

                # Adds neighbor to network if the sum of weights is greater than the threshold
                if sum_of_weights >= threshold:
                    node_activators.append(neighbor)
                    activated_nodes.append(neighbor)
                    activation_network.add_node(neighbor)
                    for neighbor_of_neighbor in G.neighbors(neighbor):
                        if neighbor_of_neighbor in activated_nodes:
                            activation_network.add_edge(neighbor, neighbor_of_neighbor)

    return activation_network

def get_linear_threshold_dict(G, seed_node_type, threshold, num_of_seeds=50):
    random.seed(7)
    activation_frequency_dict = dict()
    activation_spread_list = []

    if seed_node_type == "degree":
        seed_nodes = get_highest_degree_nodes(G, num_of_seeds)
    elif seed_node_type == "betweenness":
        seed_nodes = get_highest_betweenness_nodes(G, num_of_seeds)
    elif seed_node_type == "degree spread":
        seed_nodes = get_spread_out_highest_degree(G, num_of_seeds)
    else:
        seed_nodes = get_random_seed_nodes(G, num_of_seeds)

    activation_dict = dict()
    linear_threshold_network = linear_threshold(G, seed_nodes, threshold)
    for node in linear_threshold_network.nodes():
        activation_dict[node] = 1
    activation_spread = len(linear_threshold_network.nodes())

    return activation_dict, activation_spread