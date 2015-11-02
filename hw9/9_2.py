graph_dir = {'A': ['C', 'D', 'G'],
'N': ['A', 'G'],
'D': ['B'],
'B': ['K'],
'K': ['D'],
'C': ['E', 'D'],
'E': ['N', 'F', 'H'],
'H': ['G'],
'F': ['I'],
'J': ['I'],
'M': ['F', 'L'],
'L': ['M']}

graph_undir = {'A': ['D', 'C', 'N', 'G'],
'N': ['A', 'E', 'G'],
'D': ['A', 'C', 'B', 'K'],
'B': ['D', 'K'],
'K': ['D', 'B'],
'C': ['A', 'D', 'E'],
'E': ['C', 'N', 'F', 'H'],
'H': ['E', 'G'],
'F': ['E', 'M', 'I'],
'J': ['I'],
'M': ['F', 'L'],
'L': ['M'],
'I': ['F', 'J'],
'G': ['A', 'N', 'H']}

def dfs_rec(graph, start, visited=[]):
	visited = visited + [start]
	for node in graph[start]:
		if not node in visited:
			visited = dfs_rec(graph, node, visited)
  	return visited

def dfs_stack(graph, start):
	visited = []	
	stack = [start]
	while stack:
	   	node = stack.pop(0)
		if node not in visited:
			visited = visited + [node]
			stack = graph[node] + stack
	return visited


def bfs(graph, start):
	visited = []
	queue = [start]
	while queue:
		node = queue.pop(0)
		if node not in graph.keys():
			visited.append(node)
		if node not in visited:
			visited = visited + [node]
			queue.extend(x for x in graph[node] if x not in visited)
		rest = [x for x in graph.keys() if x not in visited]
	return visited + rest


print dfs_rec(graph_undir, 'A')
print dfs_stack(graph_undir, 'A')
print bfs(graph_dir, 'A')
print bfs(graph_undir, 'A')


