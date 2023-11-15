import numpy as np
import matplotlib.pyplot as plt
data=np.array([30,36,88,23,63])
mylabel=np.array(['apple','mango','orange','grapes','papaya'])
myexplode=[0,0,0.1,0,0]
mycolor=['red','green','k','w','c']
plt.pie(data,labels=mylabel,startangle=90, explode=myexplode, colors=mycolor, shadow=True)
plt.legend(loc='upper left')
plt.show()
