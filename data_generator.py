import random
import os

def generate_test_data(n, C, filename):
    items = []
    for _ in range(n):
        weight = random.randint(1, C // 2)
        value = random.randint(1, 100)
        items.append((value, weight))
    
    with open(filename, 'w') as f:
        f.write(f"{C} {n}\n")
        for value, weight in items:
            f.write(f"{value} {weight}\n")

def generate_multiple_datasets():
    if not os.path.exists('data'):
        os.makedirs('data')
    
    base_configs = [
        (10, 50), (15, 75), (20, 100), (25, 125), (30, 150)
    ]
    
    for i, (n, C) in enumerate(base_configs):
        generate_test_data(n, C, f'data/test_{i+1}.txt')
    
    capacity_tests = [(15, c) for c in [100, 500, 1000, 2500, 5000, 7500, 10000, 15000, 20000]]
    for i, (n, C) in enumerate(capacity_tests):
        generate_test_data(n, C, f'data/capacity_test_{i+1}.txt')
    
    size_tests = [(n, 100) for n in range(5, 24, 3)]
    for i, (n, C) in enumerate(size_tests):
        generate_test_data(n, C, f'data/size_test_{i+1}.txt')

if __name__ == "__main__":
    generate_multiple_datasets()
    print("Test data generated successfully!")