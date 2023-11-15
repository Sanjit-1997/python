import numpy as np
import matplotlib.pyplot as plt

first=np.array([5,15,23,89])
plt.subplot(2,3,1)
plt.plot(first)
plt.title('First')

second=np.array([50,104,201,55])
plt.subplot(2,3,2)
plt.plot(second)
plt.title('Second')

third=np.array([22,44,88,176])
plt.subplot(2,3,3)
plt.plot(third)
plt.title('Third')

fourth=np.array([5,15,23,89])
plt.subplot(2,3,4)
plt.plot(fourth)
plt.title('Fourth')

fifth=np.array([50,104,201,55])
plt.subplot(2,3,5)
plt.plot(fifth)
plt.title('Fifth')

sixth=np.array([22,44,88,176])
plt.subplot(2,3,6)
plt.plot(sixth)
plt.title("Sixth")

plt.suptitle("Practice Subplot")
plt.show()
