graph = {0:[1,2], 1:[0,4,3], 2:[0,3], 3:[1,2,4], 4:[3,1]}
visited = set()
def dfs(visited,graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for child in graph[node]:
            dfs(visited,graph,child)
dfs(visited,graph,0)
