def print_board(board):
    for row in board:
        print(" ".join(map(str,row)))

def manhattan_distance(board):
    distance = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != 0:
                target_x, target_y = board[i][j]//3,board[i][j]%3
                distance+= abs(i- target_x) + abs(j- target_y)
    return distance

def get_neighbors(board):
    neighbors = []
    empty_x, empty_y = None, None

    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                empty_x, empty_y = i,j

    moves=[(0,1),(1,0),(0,-1),(-1,0)]

    for move_x, move_y in moves:
        new_x, new_y = empty_x+move_x,empty_y+move_y
        if 0<= new_x<3 and 0<=new_y<3:
            new_board = [row[:] for row in board]
            new_board[empty_x][empty_y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[empty_x][empty_y]
            neighbors.append(new_board)

    return neighbors

def best_first_search(initial_state):
    visited_states = set()
    queue = [(manhattan_distance(initial_state),0,initial_state)]

    while queue:
        queue.sort()
        _,moves,current_state = queue.pop()

        if current_state == goal_state:
            return moves, current_state

        visited_states.add(tuple(map(tuple,current_state)))
        for neighbor in get_neighbors(current_state):
            if tuple(map(tuple,neighbor)) not in visited_states:
                queue.append((manhattan_distance(neighbor),moves+1,neighbor))
    return None

initial_state=[[7,2,4],[5,0,6],[8,3,1]]
goal_state=[[0,1,2],[3,4,5],[6,7,8]]
moves,final_state=best_first_search(initial_state)

if moves not in None:
    print("Solution found in:", moves,"moves:")
    print_board(final_state)
else:
    print("No solution found")

