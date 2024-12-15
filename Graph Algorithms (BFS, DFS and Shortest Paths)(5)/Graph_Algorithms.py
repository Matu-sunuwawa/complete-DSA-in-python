
## Graph Algorithm

# content
- Breadth-First-Search
- Depth-First-Search
- Shortest-Path

# Queue vs Stack (Data Structure And Algorithm)
- Queue: FIFO(First In First Out)
- Stack: LIFO(Last In First Out)

# representation of graph in `list` or in `python`
num_nodes = 5
edges = [(0,1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]
num_nodes, len(edges)

# creating class to represent a graph as adjacency list in python

Note: # best way to create empty list:
	l2 = [[] for _ in range(10)]
	RUN: l2

```
class Graph:
	def __init__(self, num_nodes, edges):
		self.num_nodes = num_nodes
		self.data = [[] for _ in range(num_nodes)]
		
		for n1, n2 in edges:
			self.data[n1].append(n2)
			self.data[n2].append(n1)
		
		def __repr__(self):
			return "\n".join(["{}:{}".format(n, neighbors) for n, neighbors in enumerate(self.data)])
		def __str__(self):
			return self.__repr__()
```
graph1 = Graph(num_nodes, edges)
RUN: graph1.data


## BFS(Breadth First Search)

```
def bfs(graph, root):
	queue = []
	discovered = [False] * len(graph.data)
	distance = [None] * len(graph.data) # tracking the distance
	parent = [None] * len(graph.data) # tracking the parent of `destination`
	
	discovered[root] = True
	queue.append(root)
	distance[root] = 0
	idx = 0
	
	while idx < len(queue):
		# dequeue
		current = queue[i]
		idx += 1
		
		# check all edges of current
		for node in graph.data[current]:
			if not discovered[node]:
				distance[node] = 1 + distance[current] # tracking the distance
				parent[node] = current
				discovered[node] = True
				queue.append(node)
				
	return queue, distance, parent
```
RUN: bfs(graph1, 3)
output: [3,1,2,4,0]
output(updated): ([3,1,2,4,0], [2,1,1,0,1], [1,3,3,None,3])

# [3,1,2,4,0] is the nodes
# [2,1,1,0,1] is the distance...i.e, the distance of `3` is `0`, `1` is `1`
# [1,3,3,None,3] is the parent...i.e, the parent of `3` is `None`, `1` is `3`

# BFS Question:
Q# write a program to check if all the nodes in a graph are `connected`.
# Hint:
num_nodes3 = 9
edges3 = [(0,1), (0,3), (1,2), (2,3), (4,5), (4,6), (5,6), (7,8)]
RUN: num_nodes3, len(edges3)

Q# write a program to find the number of connected components?
# Hint: display number of connected components like, (0,1), (0,3), (1,2), (2,3)...4,5), (4,6), (5,6)...(7,8)...so in this case there are `3` connected components.
# Hint: list all the `connected components` in each category.


## DFS(Depth First Search)

# implement DFS:
```
def dfs(graph, root):
	stack = []
	discovered = [False] * len(graph.data)
	
	stack.append(root)
	
	while len(stack) > 0:
		current = stack.pop()
		result.append(current)
		for node in graph.data[current]:
			stack.append(node)
	return result
```

dfs(graph1, 3)
RUN: graph1

# Graph with weights...you can see `DFS(weighted).png`:
num_nodes5 = 9
edges5 = [(0,1,3), (0,3,2), (0,8,4), (1,7,4), (2,7,2), (2,3,6), (2,5,1), (3,4,1), (4,8,8), (5,6,8)]

num_nodes5, len(edges5)

# Directed Graph...you can see `DFS(directed_graph).png`:
num_nodes6 = 5
edges6 = [(0,1), (1,2), (2,3), (2,4), (4,2), (3,0)]
directed6 = True
num_nodes6, len(edges6)

Q# Define a class to represent weighted and directed graphs in Python.
```
class Graph:
	def __init__(self, num_nodes, edges, directed=False, weighted=False):
		self.num_nodes = num_nodes
		self.directed = directed
		self.weighted = weighted
		self.data = [[] for _ in range(num_nodes)]
		self.weight = [[] for _ in range(num_nodes)]
		for edge in edges:
			if self.weighted:
				node1, node2, weight = edge
				self.data[node1].append(node2)
				self.weight(node1).append(weight)
				if not directed:
					self.data[node2].append(node1)
					self.weight[node2].append(weight)
			else:
				node1, node2 = edge
				self.data[node1].append(node2)
				if not directed:
					self.data[node2].append(node1)
		def __repr__(self):
			result = ""
			if self.weighted:
				for i, (nodes, weights) in enumerate(list(zip(self.data, self.weight))):
					result += "{}:{}\n".format(i, zip(nodes, weights))
			else:
				for i, nodes in enumerate(self.data):
					result += "{}:{}\n".format(i, nodes)
			return result
```

graph1 = Graph(num_nodes, edges)
RUN: graph1


# Test using `Graph with weights`:
num_nodes2 = 9
edges2 = [(0,1,3), (0,3,2), (0,8,4), (1,7,4), (2,7,2), (2,3,6), (2,5,1), (3,4,1), (4,8,8), (5,6,8)]

graph2 = Graph(num_nodes2, edges2, weighted=True)
RUN: graph2

# Test using `Directed Graph`:
num_nodes3 = 5
edges3 = [(0,1), (1,2), (2,3), (2,4), (4,2), (3,0)]

graph3 = Graph(num_nodes3, edges, directed=True)
RUN: graph3


## Shortest Paths

Q# write a function to find the length of the shortest path between two nodes in weighted directed graph?

```
def shortest_path(graph, source, target):
	visited = [False] * len(graph.data)
	distance = [float('inf')] * len(graph.data)
	queue = []
	
	distance[source] = 0
	queue.append(source)
	idx = 0
	
	while idx < len(queue) and not visited[target]:
		current = queue[idx]
		visited[current] = True
		idx +=1
		# update the distance of all the neighbors
		update_distances(graph, current, distance, parent)
		
		# find the first unvisited node with the smallest distance
		next_node = pick_next_node(distance, visited)
		if next_node:
			queue.append(next_node)
		
	return distance[target], queue
		
def update_distance(graph, current, distance, parent=None):
	"""Update the distances of the current node's neighbors"""
	neighbors = graph.data[current]
	weights = graph.weight[current]
	for i, node in enumerate(neighbors):
		weight = weight[i]
		if distance[current] + weight < distance[node]:
			distance[node] = distance[current] + weight
			if parent:
				parent[node] = current

def pick_next_node(distance, visited):
	"""pick the next unvisited node at the smallest distance"""
	min_distance = float('inf')
	min_node = None
	for node in range(len(distance)):
		if not visited[node] and distance[node] < min_distance:
			min_node = node
			min_distance = distance[node]
	return min_node
```
num_nodes7 = 6
edges7 = [(0,1,4), (0,2,2), (1,2,5), (1,3,10), (2,4,3), (4,3,4), (3,5,11)]
num_nodes7, len(edges7)

graph7 = Graph(num_nodes7, edges7, weighted=True, directed=True)
RUN: graph7

RUN: shortest_path(graph7, 0, 5)



## Time complexity:
- BFS: O(n+m)
- DFS: O(n+m)
- Shortest Path: O(n**2 + m)









