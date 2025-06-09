from itertools import combinations

def knapsack_dp(capacity, items):
    n = len(items)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        value, weight = items[i-1]
        for w in range(capacity + 1):
            if weight <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight] + value)
            else:
                dp[i][w] = dp[i-1][w]
    
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i-1)
            w -= items[i-1][1]
    
    return dp[n][capacity], selected_items

def knapsack_brute_force(capacity, items):
    n = len(items)
    best_value = 0
    best_combination = []
    
    for r in range(n + 1):
        for combination in combinations(range(n), r):
            total_weight = sum(items[i][1] for i in combination)
            total_value = sum(items[i][0] for i in combination)
            
            if total_weight <= capacity and total_value > best_value:
                best_value = total_value
                best_combination = list(combination)
    
    return best_value, best_combination

def load_data(filename):
    with open(filename, 'r') as f:
        first_line = f.readline().strip().split()
        capacity = int(first_line[0])
        n = int(first_line[1])
        
        items = []
        for _ in range(n):
            line = f.readline().strip().split()
            value = int(line[0])
            weight = int(line[1])
            items.append((value, weight))
    
    return capacity, items

def print_solution(algorithm_name, value, items_indices, items):
    print(f"\n{algorithm_name} Solution:")
    print(f"Maximum value: {value}")
    print(f"Selected items:")
    total_weight = 0
    for idx in items_indices:
        value_item, weight_item = items[idx]
        total_weight += weight_item
        print(f"  Item {idx+1}: value={value_item}, weight={weight_item}")
    print(f"Total weight: {total_weight}")