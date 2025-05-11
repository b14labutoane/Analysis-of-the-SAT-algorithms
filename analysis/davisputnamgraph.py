import pandas as pd
import matplotlib.pyplot as plt
import time
import os

def simplify_clause(clause):
    for lit in clause:
        if -lit in clause:
            return None
    return frozenset(clause)

def resolvent(c1, c2):
    for lit in c1:
        if -lit in c2:
            new_clause = (c1 | c2) - {lit, -lit}
            return simplify_clause(new_clause)
    return None

def resolution(clauses):
    unique_clauses = set()
    for clause in clauses:
        simp = simplify_clause(clause)
        if simp:
            unique_clauses.add(simp)
    new_clauses = set()
    while True:
        for c1 in unique_clauses:
            for c2 in unique_clauses:
                if c1 != c2:
                    resolv = resolvent(c1, c2)
                    if resolv is None:
                        return "Formula NESAT"
                    if resolv not in unique_clauses and resolv not in new_clauses:
                        new_clauses.add(resolv)
        if not new_clauses:
            return "Formula posibil SAT"
        unique_clauses.update(new_clauses)
        new_clauses = set()

def citire_clauze(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "test_data", f"{filename}.csv")
    data = pd.read_csv(file_path)
    clauses = []
    for clause_str in data["Clauze"]:
        clause_str = clause_str.strip("[]").replace(" ", "")
        literals = clause_str.split(",")
        clause = {int(lit) for lit in literals if lit}
        clauses.append(clause)
    return clauses

def davis_putnam(clauses):
    while True:
        unit_clauses = set()
        for clause in clauses:
            if len(clause) == 1:
                unit_clauses.add(next(iter(clause)))
        literals = {}
        for clause in clauses:
            for lit in clause:
                literals[lit] = literals.get(lit, 0) + 1
        pure_literals = set()
        for lit in literals:
            if -lit not in literals:
                pure_literals.add(lit)
        new_clauses = []
        changed = False
        for clause in clauses:
            if any(lit in unit_clauses for lit in clause):
                changed = True
                continue
            filtered = set()
            for lit in clause:
                if -lit not in unit_clauses and lit not in pure_literals:
                    filtered.add(lit)
            if not filtered:
                return "Formula NESAT"
            if filtered != clause:
                changed = True
            new_clauses.append(filtered)
        if not changed:
            break
        clauses = new_clauses
    return resolution(clauses)

def run_davis_putnam_and_time(filename):
    clauses = citire_clauze(filename)
    if clauses is None:
        return None
    cloned_clauses = [set(c) for c in clauses]
    begin = time.perf_counter_ns()
    davis_putnam(cloned_clauses)
    end = time.perf_counter_ns()
    return (end - begin) / 1000  # Convert to microseconds

def plot_davis_putnam_time(filenames, execution_times):
    plt.plot(filenames, execution_times, marker='s', color='green')
    plt.xlabel("Dataset (CSV File Name)")
    plt.ylabel("Execution Time (microseconds)")
    plt.title("Davis-Putnam Algorithm Performance")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    filenames = ["clauzemici", "clauzemedii", "clauzemari"]
    execution_times = []

    for filename in filenames:
        time_us = run_davis_putnam_and_time(filename)
        if time_us is not None:
            execution_times.append(time_us)
            print(f"File: {filename}, Time: {time_us:.2f} microseconds")
        else:
            print(f"File: {filename}, Skipped due to error")

    if len(execution_times) == len(filenames):
        plot_davis_putnam_time(filenames, execution_times)
    else:
        print("Not enough data to plot.")

running_example = [
    [1, -2, 3], [-1, 4, -5], [2, 3, -4], [-3, -5, 6],
    [5, -6, 7], [-7, 8, -9], [9, -10, 11], [-11, 12, -13],
    [13, -14, 15], [-15, 16], [16], [-16, 17], [-17, -18],
    [18, 19, -20], [-19, 21, 22], [-21, -22, 23], [22, -23, 24],
    [-24, 25, -26], [26, 27, 28], [-27, -28, 29], [30, 31, -32],
    [-30, -31, 33], [-33, 34, 35], [-34, -35, 36], [37, 38, -39],
    [-37, -38, 40], [-40, 41, -42], [42, -43, 44], [-44, -45, 46],
    [45, -46, 47], [-47, 48, -49], [49, -50, 51], [-50, 52, -53],
    [53, -54, 55], [-55, 56, -57], [57, -58, 59], [-59, -60, 61],
    [60, -61, 62], [-62, -63, 64], [63, -64, 65], [-65, 66, -67],
    [67, -68, 69], [-69, -70, 71], [70, -71, 72], [-72, 73, -74],
    [74, -75, 76], [-76, -77, 78], [77, -78, 79], [-79, 80, -81]
]
exec_times_ns = []
for i in range(10):
    clona = [set(c) for c in running_example]
    start = time.time()
    _ = davis_putnam(clona)
    end = time.time()
    exec_times_ns.append(end - start)

# Plotare grafic
plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), exec_times_ns, marker='o', linestyle='-', color='blue')
plt.title("Davis-Putnam Time Variation")
plt.xlabel("Run Number")
plt.ylabel("Execution Time(ms)")
plt.grid(True)
plt.xticks(range(1, 11))
plt.tight_layout()
plt.show()