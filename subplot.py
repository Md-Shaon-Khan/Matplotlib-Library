import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
y2 = np.array([10, 20, 30, 40])

plt.figure(figsize=(14,8))
plt.suptitle("Multiple Subplots Examples", fontsize=16, fontweight='bold')

plt.subplot(1, 2, 1)
plt.plot(x, y1, marker='o', color='blue')
plt.title("SALES")
plt.xlabel("Quarter")
plt.ylabel("Units Sold")

plt.subplot(1, 2, 2)
plt.plot(x, y2, marker='s', color='green')
plt.title("INCOME")
plt.xlabel("Quarter")
plt.ylabel("Revenue ($)")

plt.figure(figsize=(8,6))
plt.suptitle("Stacked Plots Example", fontsize=16, fontweight='bold')

plt.subplot(2, 1, 1)
plt.plot(x, y1, color='purple', linestyle='--')
plt.title("SALES")
plt.xlabel("Quarter")
plt.ylabel("Units Sold")

plt.subplot(2, 1, 2)
plt.plot(x, y2, color='orange', linestyle='-.')
plt.title("INCOME")
plt.xlabel("Quarter")
plt.ylabel("Revenue ($)")

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()

plt.figure(figsize=(14,8))
plt.suptitle("2x3 Grid Subplots Example", fontsize=16, fontweight='bold')

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.plot(x, y1 if i % 2 == 0 else y2)
    plt.title(f"Plot {i+1}")

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
