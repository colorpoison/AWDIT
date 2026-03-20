import re
import matplotlib.pyplot as plt
import os

folder = "test_results"

for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)

    if not os.path.isfile(filepath):
        continue

    x = []
    y = []
    colors = []
    #timeouts = 0
    with open(filepath) as f:
        for line in f:
            match = re.match(r"SER(\d+): ([0-9.]+)", line)
            if match:
                ser_index = int(match.group(1))
                time_val = float(match.group(2))
                #timeouts += int(time_val/30.0)

                if time_val >= 3.0:
                    x.append(ser_index)
                    y.append(3.0)
                    colors.append("red")
                else:
                    x.append(ser_index)
                    y.append(time_val)
                    colors.append("blue")

    if not x:
        continue

    x, y, colors = zip(*sorted(zip(x, y, colors)))

    # Line per file
    plt.plot(x, y, alpha=0.6, label=filename)

    # Optional: scatter points
    plt.scatter(x, y, c=colors, s=2)

plt.xlabel("Part of the transactions that are SER")
plt.ylabel("Time (seconds)")
plt.title("Execution Time per amount of SER transactions")
plt.grid(True)

import matplotlib.patches as mpatches
blue_patch = mpatches.Patch(color='blue', label='No timeout')
red_patch = mpatches.Patch(color='red', label='Timeout (> 60s)')
plt.legend()

plt.savefig("plot.png")
plt.show()
