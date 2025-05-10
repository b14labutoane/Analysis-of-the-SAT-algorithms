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
    return (end - begin) * 1_000_000

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
