def knap_max_profit(weights, costs, capacity):
    num_items = len(weights)
    table = [[0] * (capacity + 1) for _ in range(num_items + 1)]
    for i in range(1, num_items + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] <= j:
                table[i][j] = max(costs[i - 1] + table[i - 1][j - weights[i - 1]], table[i - 1][j])
            else:
                table[i][j] = table[i - 1][j]
    selected_items = []
    total_weight = capacity
    for i in range(num_items, 0, -1):
        if table[i][total_weight] != table[i - 1][total_weight]:
            selected_items.append(i - 1)
            total_weight -= weights[i - 1]
    return table[num_items][capacity], selected_items

# User input for weights, costs, and capacity
weights = list(map(int, input("Enter the weights of coffee beans (space-separated): ").split()))
costs = list(map(int, input("Enter the costs of coffee beans (space-separated): ").split()))
capacity = int(input("Enter the capacity: "))

max_profit, selected_items = knap_max_profit(weights, costs, capacity)
print("Maximum Profit:", max_profit)
print("Selected Coffee Beans (index): ", selected_items)
print("Selected Coffee Beans (weights): ", [weights[i] for i in selected_items])
print("Selected Coffee Beans (cost): ", [costs[i] for i in selected_items])