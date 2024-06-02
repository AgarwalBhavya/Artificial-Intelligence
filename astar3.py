# A STAR SEARCH
graph = {
        'A': {'S': 140, 'T': 118, 'Z': 75}, 'S': {'F': 99, 'R': 80, 'A': 140, 'O': 151},
        'T': {'L': 111, 'A': 118}, 'Z': {'A': 75, 'O': 71},
        'F': {'B': 211, 'S': 99}, 'R': {'P': 97, 'C': 146, 'S': 80},
        'O': {'S': 151, 'Z': 71}, 'L': {'T': 111, 'M': 70},
        'B': {'G': 90, 'U': 85, 'F': 211}, 'P': {'B': 101, 'C': 138, 'R': 97},
        'C': {'P': 138, 'R': 146, 'D': 120}, 'M': {'D': 75, 'L': 70},
        'G': {'B': 90}, 'U': {'B': 85, 'H': 98, 'V': 142},
        'D': {'C': 120, 'M': 75}, 'H': {'U': 98, 'E': 86},
        'V': {'U': 142, 'I': 92}, 'E': {'H': 86},
        'I': {'V': 92, 'N': 87}, 'N': {'I': 87}
        }

hf = {
        'A': 366, 'B': 0, 'C': 160, 'D': 242,
        'E': 161, 'F': 176, 'G': 77, 'H': 151,
        'I': 226, 'L': 244, 'M': 241, 'N': 234,
        'O': 380, 'P': 100, 'R': 193, 'S': 253,
        'T': 329, 'U': 80, 'V': 199, 'Z': 374
        }
def astar_search(graph, start, goal, hf):
    def priority(item):
        front, path, gn = item
        return gn + hf[front]

    open = [(start, [start], 0)]
    closed = set()

    while open:
        open.sort(key=priority)
        front, path, gn = open.pop(0)

        if front == goal:
            return path

        if front in closed:
            continue

        closed.add(front)

        for child, gn in graph[front].items():
            if child not in closed:
                fn = gn + hf[child]
                new_path = path + [child]
                open.append((child, new_path, gn))
    return 0
start = input("Enter the starting point of journey: ")
goal = input("Enter the destination point of journey: ")
if start in graph and goal in graph:
        path = astar_search(graph, start, goal, hf)
        if path:
            print("Shortest path:", path)
            total_cost = sum(graph[path[i]][path[i + 1]] for i in range(len(path) - 1))
            print("Total cost:", total_cost)
        else:
            print("No path found")
