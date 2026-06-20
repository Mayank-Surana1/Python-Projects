graph = {  # Define the graph with nodes and their edges (node: [(neighbor, cost), ...])
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 5)],
    'C': [('F', 2)],
    'D': [('G', 4)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

h = {  # Define heuristic values (h) for each node - estimated cost to reach goal 'G'
    'A': 6,
    'B': 5,
    'C': 3,
    'D': 4,
    'E': 1,
    'F': 2,
    'G': 0
}

open = [('A', 0)]  # Initialize open list with starting node 'A' and its cost (0)
parent = {'A': None}  # Track the parent of each node for path reconstruction
g = {'A': 0}  # Store the actual cost (g value) from start to each node

while open:  # Main A* algorithm loop - continue while there are nodes to explore
    open.sort(key=lambda x: x[1] + h[x[0]])  # Sort open list by f(n) = g(n) + h(n) and explore the node with lowest f value
    n, _ = open.pop(0)  # Pop the node with the lowest f value from the open list

    if n == 'G':  # Check if we reached the goal node 'G'
        path = []  # Reconstruct the optimal path by backtracking through parent pointers
        while n:
            path.append(n)  # Add current node to path
            n = parent[n]  # Move to parent node
        path.reverse()  # Reverse path to get start-to-goal order
        print("Optimal Path:", path)  # Print the optimal path found
        print("Cost:", g['G'])  # Print the total cost of the optimal path
        break  # Exit the algorithm as goal is found

    for v, c in graph[n]:  # Explore all neighbors of the current node
        ng = g[n] + c  # Calculate the cost to reach neighbor v through current node n
        if v not in g or ng < g[v]:  # If neighbor not visited or a cheaper path is found
            g[v] = ng  # Update the cost to reach neighbor v
            parent[v] = n  # Set current node n as parent of neighbor v
            open.append((v, ng))  # Add neighbor v to open list for exploration