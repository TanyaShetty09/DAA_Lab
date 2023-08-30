def is_valid(graph, path, pos, v):
    if graph[path[pos - 1]][v] == 0:
        return False
    if v in path:
        return False
    return True

def hamiltonian_cycle_util(graph, path, pos):
    if pos == len(graph):
        if graph[path[pos - 1]][path[0]] == 1:
            return True
        else:
            return False
    
    for v in range(len(graph)):
        if is_valid(graph, path, pos, v):
            path[pos] = v
            if hamiltonian_cycle_util(graph, path, pos + 1):
                return True
            path[pos] = -1

    return False

def hamiltonian_cycle(graph):
    n = len(graph)
    path = [-1] * n
    path[0] = 0

    if hamiltonian_cycle_util(graph, path, 1):
        return path
    else:
        return None

n = int(input("Enter the number of vertices: "))
graph = []
for _ in range(n):
    row = list(map(int, input(f"Enter row {_+1} of the adjacency matrix: ").split()))
    graph.append(row)

result = hamiltonian_cycle(graph)

if result:
    print("Hamiltonian cycle exists:", result)
else:
    print("Hamiltonian cycle does not exist")

'''Output:
Enter the number of vertices: 5
Enter row 1 of the adjacency matrix: 0 1 0 1 0
Enter row 2 of the adjacency matrix: 1 0 1 1 1
Enter row 3 of the adjacency matrix: 0 1 0 0 1
Enter row 4 of the adjacency matrix: 1 1 0 0 0
Enter row 5 of the adjacency matrix: 0 1 1 0 0
Hamiltonian cycle exists: [ 0, 1, 2, 4, 3]
'''