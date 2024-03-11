from queue import Queue
import numpy as np
#---------------------------------------------Find blank tile----------------------------------#
# Find the blank tile in the current state
def find_blank_tile(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
            
#---------------------------------------------Actions---------------------------------------------#
 # Move the blank tile left, right, up, or down           
def ActionMoveLeft(current_node):
    i, j = find_blank_tile(current_node)
    if j == 0:
        return False, current_node  
    new_node = np.copy(current_node)
    new_node[i][j], new_node[i][j-1] = new_node[i][j-1], new_node[i][j]
    return True, new_node

def ActionMoveRight(current_node):
    i, j = find_blank_tile(current_node)
    if j == 2:
        return False, current_node 
    new_node = np.copy(current_node)
    new_node[i][j], new_node[i][j+1] = new_node[i][j+1], new_node[i][j]
    return True, new_node

def ActionMoveUp(current_node):
    i, j = find_blank_tile(current_node)
    if i == 0:
        return False, current_node  
    new_node = np.copy(current_node)
    new_node[i][j], new_node[i-1][j] = new_node[i-1][j], new_node[i][j]
    return True, new_node

def ActionMoveDown(current_node):
    i, j = find_blank_tile(current_node)
    if i == 2:
        return False, current_node  
    new_node = np.copy(current_node)
    new_node[i][j], new_node[i+1][j] = new_node[i+1][j], new_node[i][j]
    return True, new_node
#---------------------------------------------Possible moves list----------------------------------#
# Get the possible moves for the current node
def get_possible_moves(current_node):
    possible_moves=[]

    status, new_node = ActionMoveLeft(current_node)
    if status:
        possible_moves.append(new_node)

    status, new_node = ActionMoveRight(current_node)
    if status:
        possible_moves.append(new_node)

    status, new_node = ActionMoveUp(current_node)
    if status:
        possible_moves.append(new_node)

    status, new_node = ActionMoveDown(current_node)
    if status:
        possible_moves.append(new_node)

    return possible_moves

#---------------------------------------------Generate path----------------------------------#
# Generate the path to the goal node
def generate_path(goal_node_tuple, parent):
    path = [goal_node_tuple]
    while parent[goal_node_tuple] != None:
        path.append(parent[goal_node_tuple])
        goal_node_tuple = parent[goal_node_tuple]

    path.reverse()
    return path
#---------------------------------------------BFS--------------------------------------------#
#`BFS` function to find the solution path
def bfs(start_node, goal_node):
    to_explore = Queue()
    to_explore.put(start_node)
    explored = set()
    parent = {}
    parent[tuple(map(tuple, start_node))] = None

    
    while not to_explore.empty():
        # Getting the current node from the queue
        current_node = to_explore.get()

        #converting the current_node to a tuple so that it can be added to the set
        current_node_tuple = tuple(map(tuple, current_node))

        #skiping the current node if it has already been explored
        if current_node_tuple in explored:
            continue
        #adding the current node to the set of explored nodes
        explored.add(current_node_tuple)

        #Checking if the current node is the goal node
        if np.array_equal(current_node, goal_node):
            solution_path =  generate_path(current_node_tuple, parent)
            return solution_path, parent, explored
        
        # Add the next nodes to the queue
        for node in get_possible_moves(current_node):
            node_tuple = tuple(map(tuple, node))
            if node_tuple not in explored and node_tuple not in parent:  # Ensure this node's parent hasn't been set before
                parent[node_tuple] = current_node_tuple  # Set the parent
                to_explore.put(node)  # Enqueue the node


    return  None, None, None

#---------------------------------------------Main-----------------------------------------#

# Define the start state of the puzzle, the values can be changed to test different start states
start_node = [
    [8, 6, 7],
    [2, 5, 4],  
    [3, 0, 1]
]

# the goal state of the puzzle
goal_node = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]  
]

# BFS function call with the start and goal states
solution_path, parent, explored = bfs(start_node, goal_node)

# Check if a solution was found
if solution_path:
    print("Solution found! Path to solve the puzzle:")
    count = 0
    for step in solution_path:
        print("\nStep: ", count,"\n")
        print(np.array(step))  
        count += 1
    print("\nTotal steps for goal: ", count-1)    
else:
    print("No solution found.")

#---------------------------------------------Nodes.txt-----------------------------------#
def write_explored_nodes_to_file(explored_nodes, filename="Nodes.txt"):
    with open(filename, "w") as file:
        for node in explored_nodes:
            # Converting the node from a tuple of tuples to a list of lists
            state_as_list = [list(row) for row in node]
            # Flattening the list column-wise
            column_wise_flattened = [state_as_list[j][i] for i in range(len(state_as_list[0])) for j in range(len(state_as_list))]
            file.write(' '.join(map(str, column_wise_flattened)) + "\n")

write_explored_nodes_to_file(explored)
#---------------------------------------------NodesInfo.txt-----------------------------------#

def write_nodes_info_to_file(parent_mapping, start_node, filename="NodesInfo.txt"):
    with open(filename, "w") as file:
        file.write("Node_index\tParent_Node_index\tNode\n")
        node_to_index = {tuple(map(tuple, start_node)): 0}
        Node_Index_i = 1

        for child, parent in parent_mapping.items():
            if child not in node_to_index:
                node_to_index[child] = Node_Index_i
                Node_Index_i += 1

            if parent is not None and parent not in node_to_index:
                node_to_index[parent] = Node_Index_i
                Node_Index_i += 1

            if parent is not None:
                Parent_Node_Index_i = node_to_index[parent]
            else:
                Parent_Node_Index_i = 0
            
            # Converting the node from a tuple of tuples to a list of lists
            state_as_list = [list(row) for row in child]
            # Flattening the list column-wise
            column_wise_flattened = [state_as_list[j][i] for i in range(len(state_as_list[0])) for j in range(len(state_as_list))]
            file.write(f"{node_to_index[child]}\t{Parent_Node_Index_i}\t{' '.join(map(str, column_wise_flattened))}\n")

write_nodes_info_to_file(parent, start_node)

#---------------------------------------------nodePath.txt-----------------------------------#

def write_solution_path_to_file(solution_path, filename="nodePath.txt"):
    with open(filename, "w") as file:
        for state in solution_path:
            # Converting the state from a tuple of tuples to a list of lists
            state_as_list = [list(row) for row in state] 
            # Flattening the list column-wise
            column_wise_flattened = [state_as_list[j][i] for i in range(len(state_as_list[0])) for j in range(len(state_as_list))]
            file.write(' '.join(map(str, column_wise_flattened)) + "\n")

write_solution_path_to_file(solution_path)
            

