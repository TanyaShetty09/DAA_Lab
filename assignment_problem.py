import numpy as np
from scipy.optimize import linear_sum_assignment

n = int(input("Enter the number of agents/tasks: "))

cost_matrix = []
for i in range(n):
    row = list(map(int, input(f"Enter cost/benefit for agent {i+1} (space-separated values): ").split()))
    cost_matrix.append(row)

cost_matrix = np.array(cost_matrix)

row_indices, col_indices = linear_sum_assignment(cost_matrix)

total_cost = cost_matrix[row_indices, col_indices].sum()

print("Optimal Assignment:")
for i in range(n):
    print(f"Agent {i+1} -> Task {col_indices[i] + 1}")

print("Total Cost/Benefit:", total_cost)


'''Output:
Enter the number of agents/tasks: 4
Enter cost/benefit for agent 1 (space-separated values): 3 1 4 2
Enter cost/benefit for agent 2 (space-separated values): 6 7 8 5
Enter cost/benefit for agent 3 (space-separated values): 9 11 10 12
Enter cost/benefit for agent 4 (space-separated values): 15 13 14 16
Optimal Assignment:
Agent 1 -> Task 2
Agent 2 -> Task 4
Agent 3 -> Task 1
Agent 4 -> Task 3
Total Cost/Benefit: 29
'''