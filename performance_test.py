import time
import os
import glob
from knapsack_algorithms import knapsack_dp, knapsack_brute_force, load_data

def measure_execution_time(algorithm, capacity, items):
    start_time = time.time()
    result = algorithm(capacity, items)
    end_time = time.time()
    return end_time - start_time, result

def test_algorithm_performance(measure_bf=True):
    results = {
        'size_tests': {'n': [], 'dp_time': [], 'bf_time': []},
        'capacity_tests': {'c': [], 'dp_time': [], 'bf_time': []}
    }

    if not measure_bf:
        print("Brute force measurements disabled.")
    
    print("Testing performance with varying problem size...")
    size_files = sorted(glob.glob('data/size_test_*.txt'))
    for filename in size_files:
        capacity, items = load_data(filename)
        n = len(items)
        
        dp_time, dp_result = measure_execution_time(knapsack_dp, capacity, items)
        if measure_bf:
            bf_time, bf_result = measure_execution_time(knapsack_brute_force, capacity, items)
        else:
            bf_time, bf_result = None, None
        
        results['size_tests']['n'].append(n)
        results['size_tests']['dp_time'].append(dp_time)
        results['size_tests']['bf_time'].append(bf_time)
        
        if measure_bf:
            print(f"n={n}: DP={dp_time:.6f}s, BF={bf_time:.6f}s")
        else:
            print(f"n={n}: DP={dp_time:.6f}s")
    
    print("\nTesting performance with varying capacity...")
    capacity_files = sorted(glob.glob('data/capacity_test_*.txt'))
    for filename in capacity_files:
        capacity, items = load_data(filename)
        
        dp_time, dp_result = measure_execution_time(knapsack_dp, capacity, items)
        if measure_bf:
            bf_time, bf_result = measure_execution_time(knapsack_brute_force, capacity, items)
        else:
            bf_time, bf_result = None, None
        
        results['capacity_tests']['c'].append(capacity)
        results['capacity_tests']['dp_time'].append(dp_time)
        results['capacity_tests']['bf_time'].append(bf_time)
        
        if measure_bf:
            print(f"C={capacity}: DP={dp_time:.6f}s, BF={bf_time:.6f}s")
        else:
            print(f"C={capacity}: DP={dp_time:.6f}s")
    
    results['measure_bf'] = measure_bf
    return results

def display_results_table(results):
    print("\n" + "="*70)
    print("PERFORMANCE TEST RESULTS")
    print("="*70)
    measure_bf = results.get('measure_bf', True)
    
    print("\nSize Tests (varying n, fixed C=100):")
    print("-" * 40)
    if measure_bf:
        print(f"{'n':<5} {'DP_time(s)':<12} {'BF_time(s)':<12} {'Ratio':<10}")
    else:
        print(f"{'n':<5} {'DP_time(s)':<12}")
    print("-" * 40)
    for i in range(len(results['size_tests']['n'])):
        n = results['size_tests']['n'][i]
        dp_t = results['size_tests']['dp_time'][i]
        bf_t = results['size_tests']['bf_time'][i]
        if measure_bf and bf_t is not None:
            ratio = bf_t / dp_t if dp_t > 0 else 0
            print(f"{n:<5} {dp_t:<12.6f} {bf_t:<12.6f} {ratio:<10.1f}")
        else:
            print(f"{n:<5} {dp_t:<12.6f}")
    
    print("\nCapacity Tests (varying C, fixed n=15):")
    print("-" * 40)
    if measure_bf:
        print(f"{'C':<5} {'DP_time(s)':<12} {'BF_time(s)':<12} {'Ratio':<10}")
    else:
        print(f"{'C':<5} {'DP_time(s)':<12}")
    print("-" * 40)
    for i in range(len(results['capacity_tests']['c'])):
        c = results['capacity_tests']['c'][i]
        dp_t = results['capacity_tests']['dp_time'][i]
        bf_t = results['capacity_tests']['bf_time'][i]
        if measure_bf and bf_t is not None:
            ratio = bf_t / dp_t if dp_t > 0 else 0
            print(f"{c:<5} {dp_t:<12.6f} {bf_t:<12.6f} {ratio:<10.1f}")
        else:
            print(f"{c:<5} {dp_t:<12.6f}")

def save_results_to_file(results):
    with open('performance_results.txt', 'w') as f:
        f.write("Performance Test Results\n")
        f.write("=" * 70 + "\n\n")
        
        measure_bf = results.get('measure_bf', True)
        f.write("Size Tests (varying n, fixed C=100):\n")
        f.write("-" * 40 + "\n")
        if measure_bf:
            f.write(f"{'n':<5} {'DP_time(s)':<12} {'BF_time(s)':<12} {'Ratio':<10}\n")
        else:
            f.write(f"{'n':<5} {'DP_time(s)':<12}\n")
        f.write("-" * 40 + "\n")
        for i in range(len(results['size_tests']['n'])):
            n = results['size_tests']['n'][i]
            dp_t = results['size_tests']['dp_time'][i]
            bf_t = results['size_tests']['bf_time'][i]
            if measure_bf and bf_t is not None:
                ratio = bf_t / dp_t if dp_t > 0 else 0
                f.write(f"{n:<5} {dp_t:<12.6f} {bf_t:<12.6f} {ratio:<10.1f}\n")
            else:
                f.write(f"{n:<5} {dp_t:<12.6f}\n")
        
        f.write("\nCapacity Tests (varying C, fixed n=15):\n")
        f.write("-" * 40 + "\n")
        if measure_bf:
            f.write(f"{'C':<5} {'DP_time(s)':<12} {'BF_time(s)':<12} {'Ratio':<10}\n")
        else:
            f.write(f"{'C':<5} {'DP_time(s)':<12}\n")
        f.write("-" * 40 + "\n")
        for i in range(len(results['capacity_tests']['c'])):
            c = results['capacity_tests']['c'][i]
            dp_t = results['capacity_tests']['dp_time'][i]
            bf_t = results['capacity_tests']['bf_time'][i]
            if measure_bf and bf_t is not None:
                ratio = bf_t / dp_t if dp_t > 0 else 0
                f.write(f"{c:<5} {dp_t:<12.6f} {bf_t:<12.6f} {ratio:<10.1f}\n")
            else:
                f.write(f"{c:<5} {dp_t:<12.6f}\n")

if __name__ == "__main__":
    if not os.path.exists('data'):
        print("No test data found. Please generate data first.")
    else:
        results = test_algorithm_performance()
        display_results_table(results)
        save_results_to_file(results)
        print("\nResults saved to performance_results.txt")