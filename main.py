import json
import networkx as nx
from graph_utils import create_graph, analyze_common_friends, recommend_friendships
from visualization import visualize_graph

# Load the JSON dataset
with open('data/dataset.json', 'r') as file:
    data = json.load(file)

# Create the graph
G = create_graph(data)

# Visualize the graph
visualize_graph(G)

# Analyze and recommend friendships for a sample user (id 1)
user_id = 1
direct_friends, common_friends = analyze_common_friends(G, user_id)
recommendations = recommend_friendships(G, user_id)

print("Direct friends:", direct_friends)
print("Common friends:", common_friends)
print("Friendship recommendations:", recommendations)
