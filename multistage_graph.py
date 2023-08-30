def shortest_path_multistage(graph, stages):
    n = len(graph)
    dp = [0] * n

    for stage in range(len(stages) - 2, -1, -1):
        for node in range(n):
            if stages[node] == stage:
                min_cost = float('inf')
                for neighbor, cost in graph[node]:
                    min_cost = min(min_cost, cost + dp[neighbor])
                dp[node] = min_cost

    return dp[0]

n = int(input("Enter the number of nodes in the graph: "))
graph = {i: [] for i in range(n)}

m = int(input("Enter the number of edges: "))
for _ in range(m):
    start, end, cost = map(int, input("Enter start, end, and cost: ").split())
    graph[start].append((end, cost))

stages = []
for i in range(n):
    stage = int(input(f"Enter the stage of node {i}: "))
    stages.append(stage)

result = shortest_path_multistage(graph, stages)
print("Minimum cost/path:", result)

'''
Output:
Enter the number of edges: 7
Enter start, end, and cost: 0 1 2
Enter start, end, and cost: 0 2 1
Enter start, end, and cost: 1 3 3
Enter start, end, and cost: 1 4 5
Enter start, end, and cost: 2 3 1
Enter start, end, and cost: 2 4 2
Enter start, end, and cost: 3 5 6
Enter the stage of node 0: 0  
Enter the stage of node 1: 1
Enter the stage of node 2: 1
Enter the stage of node 3: 2
Enter the stage of node 4: 2
Enter the stage of node 5: 3
Minimum cost/path: 10
'''