import numpy as np
import matplotlib.pyplot as plt


x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])


plt.figure(figsize=(14,10))
plt.suptitle("Matplotlib Grid", fontsize=16, fontweight="bold")


plt.subplot(2,2,1)
plt.plot(x, y, marker='o')
plt.title("Default Grid (both axes)")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.grid(True)


plt.subplot(2,2,2)
plt.plot(x, y, marker='s', color='green')
plt.title("Grid on X-axis")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.grid(axis='x')


plt.subplot(2,2,3)
plt.plot(x, y, marker='^', color='orange')
plt.title("Grid on Y-axis")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.grid(axis='y')


plt.subplot(2,2,4)
plt.plot(x, y, marker='d', color='purple')
plt.title("Custom Grid Lines")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.grid(color='green', linestyle='--', linewidth=0.9)


plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
