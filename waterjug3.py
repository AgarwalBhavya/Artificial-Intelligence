initial_state = [0,0]  # our initial state and goal state here
goal_state = [[2,0],[2,1],[2,2],[2,3]]

def is_goal_state(state):# our logic to check if a state is the goal state
    if state in goal_state:
            return 1

def water_jug_successor_state(state): # our logic to generate successors of a state for Water Jug Problem
    new=[]

    s=state.copy()
    if s[0]!=4 :    #fill jug A
        s[0]=4     
        new.append([s[0],s[1]])
    
    s=state.copy()
    if s[1]!=3 :    #fill jug B
        s[1]=3     
        new.append([s[0],s[1]])

    s=state.copy()
    if ( s[0]!=0 ) and ( s[1]!=3 ) : #transfer water from s[0] to s[1]
        space_in_B = 3-s[1]
        if s[0]>=space_in_B:
            s[0]-=space_in_B
            s[1]+=space_in_B
        else :
            s[1]+=s[0]
            s[0]=0
        new.append([s[0],s[1]])

    s=state.copy()
    if ( s[1]!=0 ) and ( s[0]!=4 ) : #transfer water from s[1] to s[0]
        space_in_A = 4-s[0]
        if s[1]>=space_in_A:
            s[1]-=space_in_A
            s[0]+=space_in_A
        else :
            s[0]+=s[1]
            s[1]=0
        new.append([s[0],s[1]])

    s=state.copy()
    if s[0]!=0 : # empty jug s[0] : set value of s[0] to 0
        s[0]=0
        new.append([s[0],s[1]])

    s=state.copy()
    if s[1]!=0 :  #empty jug s[1] : set value of s[1] to 0
        s[1]=0
        new.append([s[0],s[1]])

    return new

def dfs(E,i):
    print("S",i,"=>",E)
    i+=1
    if is_goal_state(E):
        return E  # Goal state found, return it

    for successor in water_jug_successor_state(E):
        if successor not in visited :
            visited.append(successor)
            result = dfs(successor,i)  # Recursively call DFS with successor as the initial state
            if result:
                return result  # Success found, propagate it up

    return None  # Success not found ( Back-Tracking )

visited=[[0,0]]
i=1
goal = dfs(initial_state,i)
if goal:
    print("SUCESS !! Goal state found:", goal)
else:
    print("FAILURE !! Goal state not found.")