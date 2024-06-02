graph = {0:[1,2], 1:[0,4,3], 2:[0,3], 3:[1,2,4], 4:[3,1]}
def bfs(graph, node):
    visited = set()
    queue = []
    queue.append(node)
    while queue:
        x = queue.pop(0)
        visited.add(x)
        for child in graph[x]:
            if child not in visited:
                queue.append(child)
    print(visited)
bfs(graph,0)

