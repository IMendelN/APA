import matplotlib.pyplot as plt
import networkx as nx

def visualize_graph(G):
    pos = nx.spring_layout(G)  # Position nodes
    edges = G.edges(data=True)
    weights = [edge[2]['weight'] for edge in edges]

    # Draw the graph
    nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=10, font_weight="bold")
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): round(d['weight'], 2) for u, v, d in edges})
    nx.draw_networkx_edges(G, pos, width=[w / max(weights) * 5 for w in weights], edge_color=weights, edge_cmap=plt.cm.Blues)
    plt.show()
