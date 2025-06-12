import os
import glob
from data_generator import generate_test_data, generate_multiple_datasets
from knapsack_algorithms import knapsack_dp, knapsack_brute_force, load_data, print_solution
from performance_test import test_algorithm_performance, save_results_to_file, display_results_table

os.system('cls' if os.name=='nt' else 'clear')

def display_menu():
    print("\n" + "="*50)
    print("KNAPSACK PROBLEM SOLVER")
    print("="*50)
    print("1. Generate test data")
    print("2. Solve single problem")
    print("3. Run performance tests")
    print("4. List available data files")
    print("5. Exit")
    print("-"*50)

def generate_data_menu():
    os.system('cls' if os.name=='nt' else 'clear')
    while True:
        print("\nData Generation Options:")
        print("1. Generate single dataset")
        print("2. Generate multiple test datasets")
        
        choice = input("Enter choice (1-2): ").strip()
        os.system('cls' if os.name=='nt' else 'clear')
        
        if choice == '1':
            while True: 
                try:
                    n = int(input("Enter number of items: "))
                    C = int(input("Enter knapsack capacity: "))
                    filename = input("Enter filename (e.g., custom_test.txt): ")

                    if not os.path.exists('data'):
                        os.makedirs('data')

                    generate_test_data(n, C, f'data/{filename}')
                    os.system('cls' if os.name=='nt' else 'clear')
                    print(f"Data generated successfully: data/{filename}")
                    break
                except ValueError:
                    print("Invalid input. Please enter valid numbers.")
                    continue
            break

        elif choice == '2':
            generate_multiple_datasets()
            print("Multiple test datasets generated successfully!")
            break
        
        else:
            print("Invalid choice. Please enter 1 or 2.")

def solve_problem_menu():
    os.system('cls' if os.name=='nt' else 'clear')

    data_files = glob.glob('data/*.txt')
    if not data_files:
        print("No data files found. Please generate data first.")
        return
    
    print("\nAvailable data files:")
    for i, filename in enumerate(data_files, 1):
        print(f"{i}. {filename}")
    while True:
        try:
            choice = int(input(f"Select file (1-{len(data_files)}): ")) - 1
            
            if 0 <= choice < len(data_files):
                os.system('cls' if os.name=='nt' else 'clear')
                filename = data_files[choice]
                capacity, items = load_data(filename)

                print(f"\nLoaded: {filename}")
                print(f"Capacity: {capacity}")
                print(f"Number of items: {len(items)}")

                print("\nSolving with Dynamic Programming...")
                dp_value, dp_items = knapsack_dp(capacity, items)
                print_solution("Dynamic Programming", dp_value, dp_items, items)

                if len(items) <= 20:
                    print("\nSolving with Brute Force...")
                    bf_value, bf_items = knapsack_brute_force(capacity, items)
                    print_solution("Brute Force", bf_value, bf_items, items)
                else:
                    print("\nSkipping Brute Force (too many items - would take too long)")
                break
            else:

                print("Invalid selection.")
        except (ValueError, IndexError):
            print("Invalid input.")

def list_data_files():
    os.system('cls' if os.name=='nt' else 'clear')
    data_files = glob.glob('data/*.txt')
    if not data_files:
        print("No data files found.")
        return
    
    print("\nAvailable data files:")
    for filename in data_files:
        try:
            capacity, items = load_data(filename)
            print(f"{filename}: n={len(items)}, C={capacity}")
        except:
            print(f"{filename}: (corrupted or invalid format)")

def run_performance_tests():
    os.system('cls' if os.name=='nt' else 'clear')
    if not os.path.exists('data'):
        print("No test data found. Please generate data first.")
        return
    
    print("Running performance tests...")
    results = test_algorithm_performance()
    display_results_table(results)
    save_results_to_file(results)
    print("\nResults saved to performance_results.txt")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            generate_data_menu()
        
        elif choice == '2':
            solve_problem_menu()
        
        elif choice == '3':
            run_performance_tests()
        
        elif choice == '4':
            list_data_files()
        
        elif choice == '5':
            print("Goodbye!")
            break
        
        else:
            os.system('cls' if os.name=='nt' else 'clear')
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()