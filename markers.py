import matplotlib.pyplot as plt
import numpy as np


ypoints = np.array([3, 8, 1, 10])


plt.figure(figsize=(14,10))
plt.suptitle("Matplotlib Markers", fontsize=16, fontweight="bold")


plt.subplot(2,2,1)
markers = ['o','*','.','x','X','+','P','s','D','d','p','H','h','v','^','<','>','1','2','3','4','|','_']
for i, m in enumerate(markers):
    plt.plot(ypoints + i*2, marker=m, label=m)
plt.title("Marker Shapes")
plt.legend(ncol=6, fontsize=8)
plt.grid(True)


plt.subplot(2,2,2)
plt.plot(ypoints, 'o-', label="Solid (-)")
plt.plot(ypoints+2, 'o:', label="Dotted (:)")
plt.plot(ypoints+4, 'o--', label="Dashed (--)")
plt.plot(ypoints+6, 'o-.', label="DashDot (-.)")
plt.title("Line Styles")
plt.legend()
plt.grid(True)


plt.subplot(2,2,3)
plt.plot(ypoints, marker='o', ms=10, label="ms=10 (small)")
plt.plot(ypoints+3, marker='o', ms=20, label="ms=20 (large)")
plt.plot(ypoints+6, marker='o', ms=20, mec='r', mfc='w', label="red edge, white fill")
plt.plot(ypoints+9, marker='o', ms=20, mec='#4CAF50', mfc='#4CAF50', label="custom green")
plt.title("Marker Size & Colors")
plt.legend()
plt.grid(True)


plt.subplot(2,2,4)
plt.plot(ypoints, marker='o', ms=20, mec='r', mfc='r', label="Red edge & fill")
plt.plot(ypoints+3, marker='o', ms=20, mec='b', mfc='y', label="Blue edge, Yellow fill")
plt.plot(ypoints+6, marker='o', ms=20, mec='hotpink', mfc='hotpink', label="Hotpink")
plt.title("Marker Edge & Face Colors")
plt.legend()
plt.grid(True)


plt.tight_layout()
plt.show()
