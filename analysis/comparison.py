import time
import matplotlib.pyplot as plt
from resolution import resolution
from davisputnam import davis_putnam
from davisputnamloglov import davis_putnam_ll

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

times = {"Resolution": [], "Davis-Putnam": [], "DPLL": []}
num_runs = 100000

for _ in range(num_runs):
    input_copy = [list(clause) for clause in running_example]

    # Resolution
    start = time.time()
    _ = resolution(input_copy)
    end = time.time()
    times["Resolution"].append((end - start))

    # Davis-Putnam
    input_copy = [set(clause) for clause in running_example]
    start = time.time()
    _ = davis_putnam(input_copy)
    end = time.time()
    times["Davis-Putnam"].append((end - start))

    # DPLL
    input_copy = [set(clause) for clause in running_example]
    start = time.time()
    _ = davis_putnam_ll(input_copy)
    end = time.time()
    times["DPLL"].append((end - start))

import numpy as np

def moving_average(data, window_size=50):
    return np.convolve(data, np.ones(window_size)/window_size, mode='valid')

plt.figure(figsize=(10, 6))
plt.plot(range(1, len(moving_average(times["Resolution"])) + 1), moving_average(times["Resolution"]), linestyle='-', color='red', label="Resolution")
plt.plot(range(1, len(moving_average(times["Davis-Putnam"])) + 1), moving_average(times["Davis-Putnam"]), linestyle='-', color='blue', label="Davis-Putnam")
plt.plot(range(1, len(moving_average(times["DPLL"])) + 1), moving_average(times["DPLL"]), linestyle='-', color='green', label="DPLL")

plt.title("Execution Time Moving Average (Window = 50 runs)")
plt.xlabel("Run Number")
plt.ylabel("Execution Time (s)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
