import re
import matplotlib.pyplot as plt
import os

folder = "test_results"

x = []
y = []
for filename in os.listdir(folder):
    file_num = int(filename[16:].split(",")[0]) 
    filepath = os.path.join(folder, filename)

    if not os.path.isfile(filepath):
        continue

    colors = []
    timeouts = 0
    with open(filepath) as f:
        for line in f:
            match = re.match(r"SER(\d+): ([0-9.]+)", line)
            if match:
                ser_index = int(match.group(1))
                time_val = float(match.group(2))
                timeouts += int(time_val/30.0)
                colors.append("blue")

    x.append(file_num)
    y.append(timeouts)
x, y, colors = zip(*sorted(zip(x, y, colors)))
plt.plot(x, y, alpha=0.6, label=filename)
plt.scatter(x, y, c=colors, s=2)
plt.xlabel("Amount of variables")
plt.ylabel("Amount of timeouts")
plt.title("Timeouts per amount of variables")
plt.grid(True)

import matplotlib.patches as mpatches
blue_patch = mpatches.Patch(color='blue', label='No timeout')
red_patch = mpatches.Patch(color='red', label='Timeout (> 60s)')
plt.legend()

plt.savefig("plot.png")
plt.show()
