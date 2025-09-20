import matplotlib.pyplot as plt
import numpy as np

y = np.array([323, 225, 125, 190])
labels = ["Apples", "Bananas", "Cherries", "Dates"]
explode = [0.2, 0.1, 0.1, 0.1]
colors = ["#D4CE28", "hotpink", "b", "#93A393"]

plt.figure(figsize=(8,8))

plt.pie(
    y,
    labels=labels,        
    startangle=90,        
    explode=explode,       
    shadow=True,           
    colors=colors,        
    autopct='%1.1f%%'    
)

plt.legend(title="Four Fruits:")  
plt.title("Fruit Distribution Pie Chart")
plt.show()
