# import matplotlib.pyplot as plt
# import numpy as np

# # Data
# xPoints  = np.array([0,3,6])
# yPoints1 = np.array([1,55,788])
# yPoints2 = np.array([154,705,981])

# # New Figure
# plt.figure(figsize=(8,5))

# # First plot
# plt.plot(xPoints, yPoints1, color="red", linestyle='--', marker='o', markersize=8, label='Line 1')

# # Second plot
# plt.plot(xPoints, yPoints2, color="green", marker="x", markersize=8, label='Line 2')

# # Title, labels, grid
# plt.title("Shaon's Matplotlib Graph")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.grid(True)

# # Legend
# plt.legend()

# # Show Plot

# for i,j in zip(xPoints,yPoints1):
#     plt.text(i,j,f'({i},{j})')

# for i,j in zip(xPoints,yPoints2):
#     plt.text(i,j,f'({i},{j})')

# plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.array([0,3,6])
y1 = np.array([1,55,788])
y2 = np.array([154,705,981])

# Create Figure
plt.figure(figsize=(10,6))

# Line plots
plt.plot(x, y1, color='red', linestyle='--', marker='o', markersize=8, label='Line 1')
plt.plot(x, y2, color='green', linestyle='-', marker='x', markersize=8, label='Line 2')

# Optionally add scatter for emphasis
plt.scatter(x, y1, color='red', s=80)
plt.scatter(x, y2, color='green', s=80)

# Annotations
for i,j in zip(x,y1):
    plt.text(i, j+20, f'({i},{j})')  # +20 for offset
for i,j in zip(x,y2):
    plt.text(i, j+20, f'({i},{j})')

# Title, labels, grid, legend
plt.title("Shaon's Combined Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.legend()
plt.xlim(0,7)     # optional x-range
plt.ylim(0,1000)  # optional y-range

# Show all on one page
plt.show()
