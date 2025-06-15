import re
import matplotlib.pyplot as plt

def parse_performance_file(path):
    with open(path, 'r') as f:
        lines = [l.strip() for l in f]

    size_section = False
    cap_section  = False
    n_vals, dp_n, bf_n = [], [], []
    C_vals, dp_C, bf_C = [], [], []

    for line in lines:
        if line.startswith("Size Tests"):
            size_section = True
            cap_section = False
            continue
        if line.startswith("Capacity Tests"):
            cap_section = True
            size_section = False
            continue
        if re.match(r'^[-\s]*$', line) or line.startswith(('n','C','//')):
            continue

        parts = re.split(r'\s+', line)
        if size_section and len(parts) >= 4:
            n, dp_t, bf_t, _ = parts
            n_vals.append(int(n))
            dp_n.append(float(dp_t))
            bf_n.append(float(bf_t))
        elif cap_section and len(parts) >= 4:
            C, dp_t, bf_t, _ = parts
            C_vals.append(int(C))
            dp_C.append(float(dp_t))
            bf_C.append(float(bf_t))

    return (n_vals, dp_n, bf_n), (C_vals, dp_C, bf_C)

def plot_results(size_data, cap_data):
    n_vals, dp_n, bf_n = size_data
    fig1, ax1 = plt.subplots(figsize=(6,5))
    ax1.plot(n_vals, dp_n, marker='o', label='DP')
    ax1.plot(n_vals, bf_n, marker='o', label='Brute Force')
    ax1.set_xlabel('Number of items (n)')
    ax1.set_ylabel('Time (s)')
    ax1.set_title('Czas wykonania vs liczba przedmiotów')
    ax1.legend()
    ax1.grid(True)
    plt.tight_layout()
    fig1.savefig('performance_vs_n.png')
    plt.close(fig1)

    C_vals, dp_C, bf_C = cap_data
    fig2, ax2 = plt.subplots(figsize=(6,5))
    ax2.plot(C_vals, dp_C, marker='o', label='DP')
    ax2.plot(C_vals, bf_C, marker='o', label='Brute Force')
    ax2.set_xlabel('Capacity (C)')
    ax2.set_ylabel('Time (s)')
    ax2.set_title('Czas wykonania vs pojemność plecaka')
    ax2.legend()
    ax2.grid(True)
    ax2.set_xlim(10, 10000)
    plt.tight_layout()
    fig2.savefig('performance_vs_C.png')
    plt.close(fig2)

if __name__ == "__main__":
    size_data, cap_data = parse_performance_file("performance_results.txt")
    plot_results(size_data, cap_data)