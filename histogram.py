import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)

plt.figure(figsize=(10,6))
plt.suptitle("Histogram Example", fontsize=16, fontweight="bold")

plt.subplot(1,2,1)
plt.hist(x)
plt.title("Default Histogram")

plt.subplot(1,2,2)
plt.hist(x, bins=15, color='skyblue', edgecolor='black')
plt.title("Customized Histogram (bins=15)")

plt.tight_layout()
plt.show()
