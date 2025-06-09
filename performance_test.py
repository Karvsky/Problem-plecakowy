import time
import os
import glob
from knapsack_algorithms import knapsack_dp, knapsack_brute_force, load_data

def measure_execution_time(algorithm, capacity, items):
    start_time = time.time()
    result = algorithm(capacity, items)
    end_time = time.time()
    return end_time - start_time, result

def test_algorithm_performance():
    results = {
        'size_tests': {'n': [], 'dp_time': [], 'bf_time': []},
        'capacity_tests': {'c': [], 'dp_time': [], 'bf_time': []}
    }
    
    print("Testing performance with varying problem size...")
    size_files = sorted(glob.glob('data/size_test_*.txt'))
    for filename in size_files:
        capacity, items = load_data(filename)
        n = len(items)
        
        dp_time, dp_result = measure_execution_time(knapsack_dp, capacity, items)
        bf_time, bf_result = measure_execution_time(knapsack_brute_force, capacity, items)
        
        results['size_tests']['n'].append(n)
        results['size_tests']['dp_time'].append(dp_time)
        results['size_tests']['bf_time'].append(bf_time)
        
        print(f"n={n}: DP={dp_time:.6f}s, BF={bf_time:.6f}s")
    
    print("\nTesting performance with varying capacity...")
    capacity_files = sorted(glob.glob('data/capacity_test_*.txt'))
    for filename in capacity_files:
        capacity, items = load_data(filename)
        
        dp_time, dp_result = measure_execution_time(knapsack_dp, capacity, items)
        bf_time, bf_result = measure_execution_time(knapsack_brute_force, capacity, items)
        
        results['capacity_tests']['c'].append(capacity)
        results['capacity_tests']['dp_time'].append(dp_time)
        results['capacity_tests']['bf_time'].append(bf_time)
        
        print(f"C={capacity}: DP={dp_time:.6f}s, BF={bf_time:.6f}s")
    
    return results

def display_results_table(results):
    print("\n" + "="*70)
    print("PERFORMANCE TEST RESULTS")
    print("="*70)
    
    print("\nSize Tests (varying n, fixed C=100):")
    print("-" * 40)
    print(f"{'n':<5} {'DP_time(s)':<12} {'BF_time(s)':<12} {'Ratio':<10}")
    print("-" * 40)
    for i in range(len(results['size_tests']['n'])):
        n = results['size_tests']['n'][i]
        dp_t = results['size_tests']['dp_time'][i]
        bf_t = results['size_tests']['bf_time'][i]
        ratio = bf_t / dp_t if dp_t > 0 else 0
        print(f"{n:<5} {dp_t:<12.6f} {bf_t:<12.6f} {ratio:<10.1f}")
    
    print("\nCapacity Tests (varying C, fixed n=15):")
    print("-" * 40)
    print(f"{'C':<5} {'DP_time(s)':<12} {'BF_time(s)':<12} {'Ratio':<10}")
    print("-" * 40)
    for i in range(len(results['capacity_tests']['c'])):
        c = results['capacity_tests']['c'][i]
        dp_t = results['capacity_tests']['dp_time'][i]
        bf_t = results['capacity_tests']['bf_time'][i]
        ratio = bf_t / dp_t if dp_t > 0 else 0
        print(f"{c:<5} {dp_t:<12.6f} {bf_t:<12.6f} {ratio:<10.1f}")

def save_results_to_file(results):
    with open('performance_results.txt', 'w') as f:
        f.write("Performance Test Results\n")
        f.write("=" * 70 + "\n\n")
        
        f.write("Size Tests (varying n, fixed C=100):\n")
        f.write("-" * 40 + "\n")
        f.write(f"{'n':<5} {'DP_time(s)':<12} {'BF_time(s)':<12} {'Ratio':<10}\n")
        f.write("-" * 40 + "\n")
        for i in range(len(results['size_tests']['n'])):
            n = results['size_tests']['n'][i]
            dp_t = results['size_tests']['dp_time'][i]
            bf_t = results['size_tests']['bf_time'][i]
            ratio = bf_t / dp_t if dp_t > 0 else 0
            f.write(f"{n:<5} {dp_t:<12.6f} {bf_t:<12.6f} {ratio:<10.1f}\n")
        
        f.write("\nCapacity Tests (varying C, fixed n=15):\n")
        f.write("-" * 40 + "\n")
        f.write(f"{'C':<5} {'DP_time(s)':<12} {'BF_time(s)':<12} {'Ratio':<10}\n")
        f.write("-" * 40 + "\n")
        for i in range(len(results['capacity_tests']['c'])):
            c = results['capacity_tests']['c'][i]
            dp_t = results['capacity_tests']['dp_time'][i]
            bf_t = results['capacity_tests']['bf_time'][i]
            ratio = bf_t / dp_t if dp_t > 0 else 0
            f.write(f"{c:<5} {dp_t:<12.6f} {bf_t:<12.6f} {ratio:<10.1f}\n")

if __name__ == "__main__":
    if not os.path.exists('data'):
        print("No test data found. Please generate data first.")
    else:
        results = test_algorithm_performance()
        display_results_table(results)
        save_results_to_file(results)
        print("\nResults saved to performance_results.txt")