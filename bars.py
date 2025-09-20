import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.figure(figsize=(12,6))
plt.suptitle("Matplotlib Bar Examples", fontsize=16, fontweight="bold")

plt.subplot(2,2,1)
plt.bar(x, y)
plt.title("Vertical Bars")

plt.subplot(2,2,2)
plt.barh(x, y)
plt.title("Horizontal Bars")

plt.subplot(2,2,3)
plt.bar(x, y, color="hotpink", width=0.5)
plt.title("Colored Bars with Width 0.5")

plt.subplot(2,2,4)
plt.barh(x, y, color="#4CAF50", height=0.1)
plt.title("Colored Horizontal Bars with Height 0.3")

plt.tight_layout()
plt.show()
