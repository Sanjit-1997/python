import numpy as np
import matplotlib.pyplot as plt
first=np.array([5,15,23,89])
plt.subplot(3,1,1)
plt.plot(first)
second=np.array([50,104,201,55])
plt.subplot(3,1,2)
plt.plot(second)
third=np.array([22,44,88,176])
plt.subplot(3,1,3)
plt.plot(third)
plt.show()
