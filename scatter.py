import matplotlib.pyplot as plt
import numpy as np


x1 = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y1 = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

x2 = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y2 = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])

plt.figure(figsize=(14,6))
plt.scatter(x1, y1, color='hotpink', label='Day 1')
plt.scatter(x2, y2, color='#88c999', label='Day 2')
plt.legend()
plt.title("Scatter Plot of Car Age vs Speed")
plt.xlabel("Car Age")
plt.ylabel("Speed")
plt.grid(True)
plt.show()


colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])
plt.figure(figsize=(10,6))
plt.scatter(x1, y1, c=colors)
plt.title("Scatter with Custom Colors")
plt.show()


color_vals = np.array([0,10,20,30,40,45,50,55,60,70,80,90,100])
plt.figure(figsize=(10,6))
plt.scatter(x1, y1, c=color_vals, cmap='viridis')
plt.colorbar()
plt.title("Scatter with Colormap")
plt.show()


sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
plt.figure(figsize=(10,6))
plt.scatter(x1, y1, s=sizes, alpha=0.2)
plt.title("Scatter with Sizes and Transparency")
plt.show()


x_rand = np.random.randint(100, size=100)
y_rand = np.random.randint(100, size=100)
colors_rand = np.random.randint(100, size=100)
sizes_rand = 10 * np.random.randint(100, size=100)

plt.figure(figsize=(12,6))
plt.scatter(x_rand, y_rand, c=colors_rand, s=sizes_rand, alpha=0.5, cmap='nipy_spectral')
plt.colorbar()
plt.title("Combined Scatter: Color, Size & Alpha")
plt.show()
