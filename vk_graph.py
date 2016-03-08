import json
import time
import urllib2


class Node:

    def __init__(self, id):
        self.id = id
        self.connections = []

    def add_connection(self, other_node):
        if other_node.id not in self.connections:
            self.connections.append(other_node.id)

    def __str__(self):
        return str(self.id)


class Graph:

    def __init__(self):
        self.nodes = {}

    def add(self, node):
        self.nodes[node.id] = node

    def get(self, node_id):
        return self.nodes[node_id]

    def add_edge(self, node_id1, node_id2):
        self.get(node_id1).add_connection(self.get(node_id2))
        self.get(node_id2).add_connection(self.get(node_id1))

    def print_graph(self):
        for user_id in self.nodes:
            print('{0} : {1}'.format(user_id, self.nodes[user_id].connections))


def get_friends(user_id):
    print('>> get friends for: {0}'.format(user_id))
    response = None
    try:
        response = urllib2.urlopen('https://api.vk.com/method/friends.get?user_id={0}'.format(user_id)).read()
    except urllib2.HTTPError, err:
        print("HTTPError")
    except urllib2.URLError, err:
        print("URLError")
    friends = json.loads(response)
    if 'response' in friends:
        friends = friends['response']
    else:
        print('>> no response for id: {0}'.format(user_id))
        friends = []
    return friends


def build_user_graph(user_id):
    g = Graph()
    g.add(Node(user_id))
    user_friends = get_friends(user_id)

    for friend_id in user_friends:
        g.add(Node(friend_id))
        g.add_edge(user_id, friend_id)

    for f1_id in user_friends:
        f1_friends = get_friends(f1_id)
        for f2_id in f1_friends:
            if f2_id in user_friends:
                g.add_edge(f2_id, f1_id)
    return g


def dfs(graph):
    raise Error("Not implemented")


def bfs(graph):
    raise Error("Not implemented")


def find_bridges(graph):
    raise Error("Not implemented")

if __name__ == '__main__':
    user_id = 42265807
    g = build_user_graph(user_id)
    g.print_graph()
