'''
import pandas as pd
import time
import matplotlib.pyplot as plt
import os

def simplify_clause(clauza):
    for lit in clauza:
        if -lit in clauza:
            return None
    return frozenset(clauza)

def resolvent(c1, c2):
    for lit in c1:
        if -lit in c2:
            clauza_noua = (c1 | c2) - {lit, -lit}
            return simplify_clause(clauza_noua)
    return None

def resolution(clauze):
    clauze_uni = set()
    for clauza in clauze:
        simp = simplify_clause(clauza)
        if simp:
            clauze_uni.add(simp)
    clauze_noi = set()
    while True:
        for c1 in clauze_uni:
            for c2 in clauze_uni:
                if c1!=c2:
                    resolv = resolvent(c1, c2)
                    if resolv is None:
                        return "Formula NESAT"
                    if resolv not in clauze_uni and resolv not in clauze_noi:
                        clauze_noi.add(resolv)

        if not clauze_noi:
            return "Formula posibil SAT"

        clauze_uni.update(clauze_noi)
        clauze_noi = set()

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

def run_resolution_and_time(filename):
    clauze = citire_clauze(filename)
    if clauze is None:
        return None
    clona_clauze_rez = [set(c) for c in clauze]
    begin = time.time()
    resolution(clona_clauze_rez)
    end = time.time()
    return (end - begin)

def plot_resolution_time(filenames, execution_times):
    plt.plot(filenames, execution_times, marker='o')
    plt.xlabel("Dataset (CSV File Name)")
    plt.ylabel("Execution Time (microseconds)")
    plt.title("Resolution Algorithm Performance")
    plt.grid(True)
    plt.show()

filenames = ["clauzemici", "clauzemedii", "clauzemari"]
execution_times = []

for filename in filenames:
    execution_time = run_resolution_and_time(filename)
    if execution_time is not None:
        execution_times.append(execution_time)
        print(f"File: {filename}, Time: {execution_time:.2f} microseconds")
    else:
        print(f"File: {filename}, Skipped due to error")

if len(execution_times) == len(filenames):
    plot_resolution_time(filenames, execution_times)
else:
    print("Not enough data to plot.")

'''
import time
import matplotlib.pyplot as plt
from itertools import combinations

def simplify_clause(clauza):
    for lit in clauza:
        if -lit in clauza:
            return None
    return frozenset(clauza)

def resolvent(c1, c2):
    for lit in c1:
        if -lit in c2:
            clauza_noua = (c1 | c2) - {lit, -lit}
            return simplify_clause(clauza_noua)
    return None

def resolution(clauze):
    clauze_uni = set()
    for clauza in clauze:
        simp = simplify_clause(clauza)
        if simp:
            clauze_uni.add(simp)
    clauze_noi = set()
    while True:
        for c1 in clauze_uni:
            for c2 in clauze_uni:
                if c1!=c2:
                    resolv = resolvent(c1, c2)
                    if resolv is None:
                        return "Formula NESAT"
                    if resolv not in clauze_uni and resolv not in clauze_noi:
                        clauze_noi.add(resolv)

        if not clauze_noi:
            return "Formula posibil SAT"

        clauze_uni.update(clauze_noi)
        clauze_noi = set()

# Formula CNF
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
exec_times_res = []
for i in range(10):
    input_copy = [list(clause) for clause in running_example]
    start = time.time()
    _ = resolution(input_copy)
    end = time.time()
    exec_times_res.append((end - start))  # în milisecunde

# Plotare grafic
plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), exec_times_res, marker='o', linestyle='-', color='green')
plt.title("Resolution Algorithm Time Variation")
plt.xlabel("Run Number")
plt.ylabel("Execution Time (ms)")
plt.grid(True)
plt.xticks(range(1, 11))
plt.tight_layout()
plt.show()