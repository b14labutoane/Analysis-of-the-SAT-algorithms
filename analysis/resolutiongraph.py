import time
import matplotlib.pyplot as plt
import pandas as pd

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

filenames = ["clauzemici", "clauzemedii", "clauzemari"]
exec_times_reso = []

def citire_clauze(filename):
    data = pd.read_csv(f"analysis/test_data/{filename}.csv")
    return [set(row) for row in data["Clauze"].apply(eval)]


for f in filenames:
    clauze = citire_clauze(f)
    clona_clauze_reso = [set(c) for c in clauze]

    begin = time.time()
    _ = resolution(clona_clauze_reso)
    end = time.time()

    exec_times_reso.append((end - begin))

print(exec_times_reso)
plt.figure(figsize=(10, 6))
plt.plot(filenames, exec_times_reso, marker='o', linestyle='-', color='blue')
plt.title("Resolution Algorithm Time Variation on Files")
plt.xlabel("File Name")
plt.ylabel("Execution Time (s)")
plt.grid(True)
plt.tight_layout()
plt.show()
