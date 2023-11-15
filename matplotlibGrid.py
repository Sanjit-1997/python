import numpy as np
import matplotlib.pyplot as plt
xpoints=np.array([5,12,36,100])
ypoints=np.array([12,24,60,20])
plt.plot(xpoints, ls='-')
plt.plot(ypoints,ls=':')
plt.xlabel('grade')
plt.ylabel('no.of_student')
plt.grid()
plt.show()
