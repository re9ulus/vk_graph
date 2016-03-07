import json
import time
import urllib2

# TODO: Make separate class for Graph

class Node:

	def __init__(self, id):
		self.id = id
		self.connections = []

	def add_connection(self, other_node):
		if other_node.id not in self.connections:
			self.connections.append(other_node.id)

	def __str__(self):
		return str(self.id)


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
	graph = {}
	graph[user_id] = Node(user_id)
	user_friends = get_friends(user_id)

	for friend_id in user_friends:
		graph[friend_id] = Node(friend_id)
		graph[user_id].add_connection(graph[friend_id])
		graph[friend_id].add_connection(graph[user_id])

	for friend_id in user_friends:
		friends2 = get_friends(friend_id)
		time.sleep(0.2) 
		for f2_id in friends2:
			if f2_id in user_friends:
				graph[f2_id].add_connection(graph[friend_id])
				graph[friend_id].add_connection(graph[f2_id])

	return graph


def print_graph(graph):
	for user_id in graph:
		print('{0} : {1}'.format(user_id, graph[user_id].connections))



if __name__ == '__main__':
	user_id = 42265807
	graph = build_user_graph(user_id)
	print_graph(graph)
