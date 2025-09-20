# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = np.array([1,6,7,9,15])
# ypoints = np.array([34,66,99,112,230])

# plt.plot(xpoints,ypoints,'o')
# plt.show()

# plt.plot(xpoints,ypoints)
# plt.show()

# plt.plot(ypoints)
# plt.grid(True)
# plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.array([1, 6, 7, 9, 15])
y1 = np.array([34, 66, 99, 112, 230])
y2 = np.array([20, 50, 80, 120, 200])

# Figure Size
plt.figure(figsize=(12,6))

# ---- Subplot 1: Scatter + Annotate ----
plt.subplot(1,2,1)  # 1 row, 2 cols, plot 1
plt.scatter(x, y1, color='red', s=80, label='y1 points')  # Scatter
plt.title("Scatter Plot with Annotations")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.grid(True)

# Annotate points
for i, j in zip(x, y1):
    plt.text(i, j+5, f'({i},{j})')  # +5 to lift text above point

plt.legend()

# ---- Subplot 2: Multiple Lines ----
plt.subplot(1,2,2)  # plot 2
plt.plot(x, y1, color='blue', linestyle='-', marker='o', markersize=8, label='Line 1')
plt.plot(x, y2, color='green', linestyle='--', marker='x', markersize=8, label='Line 2')
plt.title("Multiple Lines with Grid & Legend")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.legend()
plt.xlim(0, 20)
plt.ylim(0, 250)

# Annotate points
for i, j in zip(x, y1):
    plt.text(i, j+5, f'{j}')
for i, j in zip(x, y2):
    plt.text(i, j+5, f'{j}')

# Show all plots
plt.tight_layout()  # adjust spacing
plt.show()
