import matplotlib
print(matplotlib.__version__)# to check the version of matplotlib
import matplotlib.pyplot as pt
import numpy as np

y=np.array([50,245])
pt.plot(y,'_-.r')
pt.show()
