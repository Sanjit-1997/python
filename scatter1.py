import numpy as np
import matplotlib.pyplot as plt
first=np.array([10,25,36,55])
second=np.array([32,56,80,91])
third=np.array([12,24,36,48])
fourth=np.array([22,45,65,34])
plt.scatter(first,second, marker="h", c="r")
plt.scatter(third,fourth)
plt.show()
