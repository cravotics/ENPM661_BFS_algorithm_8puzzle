8-Puzzle Solver README 

Project - 1 
Uid - jagkrish

This project implements a Breadth-First Search (BFS) algorithm to solve the 8-puzzle problem, where the goal is to move tiles in a 3X3 grid to achieve a target configuration and back track from goal to start node to find the path.

Prerequisites:

1) Before running the code ensure that Python and following libraries in python are available and properly installed.

2) File name: proj1_sai_jagadeesh_muralikrishnan.py

Libraries Used:

1) numpy: Used for array manipulations and comparisons.

import numpy as np

2) queue: Provides the Queue data structure for BFS implementation to execute FIFO algorithm.

from queue import Queue

Check Output Files: After successful execution, check the project directory for the following output files:

1) Nodes.txt: Contains all explored states in a flattened format.
2) NodesInfo.txt: Includes detailed information about each explored node, such as its index, parent node index, and state.
3) nodePath.txt: Lists the states from the start to the goal in the solution path in a column flattened format.

States:

I have used start_node and goal node as following but feel free to change nodes to test different start states at line 115.

My intially defined start state :  
start_node = [
    [8, 6, 7],
    [2, 5, 4],  
    [3, 0, 1]
]

My intially defined goal state :  
goal_node = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]  
]

Optional: Check the terminal to know how many steps it too to reach from start node to goal node.
