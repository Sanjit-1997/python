import numpy as np
import matplotlib.pyplot as plt
data=np.random.normal(25,10,50)
plt.hist(data, alpha=1, color='r',histtype='stepfilled')

plt.show()
