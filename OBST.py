def optimal_bst(keys, freq):
    n = len(keys)
    cost = [[0] * n for _ in range(n)]

    for i in range(n):
        cost[i][i] = freq[i]

    for length in range(2, n+1):
        for i in range(n - length + 1):
            j = i + length - 1
            cost[i][j] = float('inf')
            freq_sum = sum(freq[i:j+1])

            for k in range(i, j+1):
                left_cost = cost[i][k - 1] if k > i else 0
                right_cost = cost[k + 1][j] if k < j else 0
                temp_cost = left_cost + right_cost + freq_sum

                if temp_cost < cost[i][j]:
                    cost[i][j] = temp_cost

    return cost[0][n-1]

n = int(input("Enter the number of keys: "))
keys = []
freq = []

for i in range(n):
    key = int(input(f"Enter key {i+1}: "))
    keys.append(key)
    freq_value = int(input(f"Enter frequency for key {i+1}: "))
    freq.append(freq_value)

result = optimal_bst(keys, freq)
print("Minimum cost of optimal BST:", result)


''' 
Output:
Enter the number of keys: 4
Enter key 1: 10
Enter frequency for key 1: 34
Enter key 2: 20
Enter frequency for key 2: 50
Enter key 3: 30
Enter frequency for key 3: 16
Enter key 4: 40
Enter frequency for key 4: 9
Minimum cost of optimal BST: 177
'''
