import networkx as nx
from datetime import datetime

def create_graph(data):
    G = nx.Graph()

    # Adding nodes (users)
    for user in data['usuarios']:
        G.add_node(user['id'], name=user['nome'])

    # Function to calculate the duration of friendship in years
    def calculate_duration(start_date):
        start = datetime.strptime(start_date, "%Y-%m-%d")
        today = datetime.now()
        return (today - start).days / 365

    # Adding edges (friendships) with weights
    for friendship in data['amizades']:
        user1, user2 = friendship['usuario1_id'], friendship['usuario2_id']
        friendship_duration = calculate_duration(friendship['data_inicio'])
        
        # Calculate the number of messages between users
        messages = sum(1 for m in data['mensagens'] if 
                       (m['remetente_id'] == user1 and m['destinatario_id'] == user2) or 
                       (m['remetente_id'] == user2 and m['destinatario_id'] == user1))
        
        # Calculate common friends
        friends_user1 = {f['usuario2_id'] for f in data['amizades'] if f['usuario1_id'] == user1}
        friends_user2 = {f['usuario2_id'] for f in data['amizades'] if f['usuario1_id'] == user2}
        common_friends = len(friends_user1.intersection(friends_user2))

        # Edge weight
        weight = messages + 0.5 * friendship_duration + 2 * common_friends
        G.add_edge(user1, user2, weight=weight)
    
    return G

def analyze_common_friends(G, user_id):
    friends = list(G.neighbors(user_id))
    common_friends_count = {}

    for friend in friends:
        friends_of_friend = set(G.neighbors(friend))
        common_friends_count[friend] = len(set(friends).intersection(friends_of_friend))

    return friends, common_friends_count

def recommend_friendships(G, user_id):
    direct_friends = set(G.neighbors(user_id))
    recommendations = []

    for user in G.nodes:
        if user != user_id and user not in direct_friends:
            common_friends = direct_friends.intersection(set(G.neighbors(user)))
            affinity = len(common_friends)
            if affinity > 0:
                recommendations.append((user, affinity))

    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations
