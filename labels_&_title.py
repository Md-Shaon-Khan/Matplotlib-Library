import numpy as np
import matplotlib.pyplot as plt

# --- Data ---
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])


font_title = {'family': 'serif', 'color': 'blue', 'size': 20}
font_labels = {'family': 'serif', 'color': 'darkred', 'size': 15}


plt.figure(figsize=(12, 6))
plt.suptitle("Matplotlib Labels & Title", fontsize=16, fontweight="bold")


plt.subplot(2,2,1)
plt.plot(x, y, marker='o')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.title("Simple Labels")
plt.grid(True)


plt.subplot(2,2,2)
plt.plot(x, y, marker='s', color='green')
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.grid(True)


plt.subplot(2,2,3)
plt.plot(x, y, marker='^', color='orange')
plt.title("Sports Watch Data", fontdict=font_title)
plt.xlabel("Average Pulse", fontdict=font_labels)
plt.ylabel("Calorie Burnage", fontdict=font_labels)
plt.grid(True)


plt.subplot(2,2,4)
plt.plot(x, y, marker='d', color='purple')
plt.title("Sports Watch Data", loc='left', fontdict=font_title)
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.grid(True)


plt.tight_layout(rect=[0, 0, 1, 0.95]) 
plt.show()
