def astar(start, goal, heuristic):
    def calculate_f(node):
        return node[1] + node[2]
    open_set=[]
    closed_set=set()
    came_from={}

    start_node=(start,0,heuristic[start])
    open_set.append(start_node)

    while open_set:
        open_set.sort(key=calculate_f)
        current_node=open_set.pop()

        if current_node[0] == goal:
            path= []
            print(f"The minimum distance from{start} to {goal} is ={current_node[1]}")
            while current_node:
                path.append(current_node[0])
                current_node = came_from.get(current_node[0])
            return list(reversed[path])
        closed_set.add(current_node[0])

        for neighbor in generate_neighbors[current_node[0]]:
            if neighbor[0] in closed_set:
                continue

            gval = current_node[1] + neighbor[1]
            hval = heuristic[neighbor[0]]
            fval = gval + hval
            neighbor_node = (neighbor[0],gval,hval)

            for i,open_node in enumerate(open_set):
                if neighbor_node[0] == open_node[0] and neighbor_node[1] >=open_node[1]:
                    break
                else:
                    open_set.append(neighbor_node)
                    came_from[neighbor[0]] = current_node[0]
                    return None

heuristic = {"A":366,"B":0,"C":160,"D":242,"E":161,"F":176,"G":77,"H":151,"I":226,"L":244,"M":241,"N":234,"O":380,"P":100,"R":193,"S":253,"T":329,"U":80,"V":199,"Z":374}
generate_neighbors={"A":[["Z",75],["T",118],["S",140]],"B":[["F",211],["U",85],["G",90],["P",101]],"C":[["D",120],["R",146],["P",138]],"D":[["M",75],["C",120]],"E":[["H",86]],"F":[["S",99],["B",211]],"G":[["B",90]],"H":[["U",98],["E",86]],"I":[["N",87],["V",92]],"L":[["M",70],["T",118]],"M":[["D",75],["L",70]],"N":[["I",87]],"O":[["Z",71],["S",151]],"P":[["R",97],["B",101],["C",138]],"R":[["S",80],["P",97],["C",146]],"S":[["A",140],["O",151],["F",99],["R",80]],"T":[["A",118],["L",111]],"U":[["B",85],["H",98],["V",142]],"V":[["I",92],["U",142]],"Z":[["A",75],["O",71]]}

path = astar("A","B",heuristic)
if path:
    print("Path found:",path)
else:
    print("No path found.")