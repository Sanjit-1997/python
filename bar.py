import numpy as np
import matplotlib.pyplot as plt

name=np.array(["sanjit","shivam","Irshad","ajith"])
mark=np.array([100,90,80,100])

plt.subplot(1,2,1)
plt.bar(name,mark, color='r',width=0.5)

plt.subplot(1,2,2)
plt.barh(name,mark, color='b', height=0.2)

plt.show()
