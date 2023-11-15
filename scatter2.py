import numpy as np
import matplotlib.pyplot as plt
first=np.array([10,25,36,55])
second=np.array([32,56,80,91])
third=np.array([12,24,36,48])
fourth=np.array([22,45,65,34])
c1=np.array([20,30,40,50])
c2=np.array([10,30,60,90])
plt.scatter(first,second, marker="h", c=c1, cmap='viridis')
plt.scatter(third,fourth, marker="*", c=c2, cmap='viridis')
plt.show()
