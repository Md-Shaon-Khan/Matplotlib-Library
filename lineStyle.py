import matplotlib.pyplot as plt
import numpy as np


plt.figure(figsize=(14,10))
plt.suptitle("Matplotlib Line Style Examples", fontsize=16, fontweight="bold")


ypoints = np.array([3, 8, 1, 10])


p1 = np.array([3, 8, 1, 10])
p2 = np.array([6, 2, 7, 11])


x1 = np.array([0, 1, 2, 13])
y1 = np.array([3, 8, 10, 140])
x2 = np.array([0, 1, 2, 13])
y2 = np.array([6, 2, 77, 101])



plt.subplot(3,3,1)
plt.plot(ypoints, linestyle='dotted')
plt.title("Dotted Line")


plt.subplot(3,3,2)
plt.plot(ypoints, linestyle='dashed')
plt.title("Dashed Line")


plt.subplot(3,3,3)
plt.plot(ypoints, color='pink')
plt.title("Pink Line")


plt.subplot(3,3,4)
plt.plot(ypoints, linewidth=5)   # smaller width for better view
plt.title("Thick Line (linewidth=5)")


plt.subplot(3,3,5)
plt.plot(p1, label="Line 1")
plt.plot(p2, label="Line 2")
plt.title("Multiple Lines (p1 & p2)")
plt.legend()


plt.subplot(3,3,6)
plt.plot(x1, y1, label="Line 1")
plt.plot(x2, y2, label="Line 2")
plt.title("Lines with X, Y Data")
plt.legend()


plt.tight_layout()
plt.show()
