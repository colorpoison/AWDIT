import re
import matplotlib.pyplot as plt

x = []
y = []
colors = []

with open("results.txt") as f:
    for line in f:
        match = re.match(r"SER(\d+): ([0-9.]+)", line)
        if match:
            ser_index = int(match.group(1))
            time_val = float(match.group(2))

            # Clip and assign color
            if time_val > 3.0:
                x.append(ser_index)
                y.append(3.0)          # clipped value
                colors.append("red")   # highlight
            else:
                x.append(ser_index)
                y.append(time_val)
                colors.append("blue")  # normal points

# Sort everything together
x, y, colors = zip(*sorted(zip(x, y, colors)))

# Plot line (optional, in gray for context)
plt.plot(x, y, color="gray", alpha=0.5)

# Plot points with colors
plt.scatter(x, y, c=colors)

plt.xlabel("Part of the transactions that are SER")
plt.ylabel("Time (seconds)")
plt.title("Execution Time per amount of SER transactions")
plt.grid(True)

# Optional: add legend manually
import matplotlib.patches as mpatches
blue_patch = mpatches.Patch(color='blue', label='No timeout')
red_patch = mpatches.Patch(color='red', label='Timeout (> 60s)')
plt.legend(handles=[blue_patch, red_patch])

plt.savefig("plot.png")
plt.show()
