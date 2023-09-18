import numpy as np
a=np.array(('love'))
b=np.array(('python'))
c=np.char.add(a,b)
print(c)
print(np.char.multiply(b,2))
print(np.char.center(b,11,fillchar='x'))
d='learn python'
print(np.char.capitalize(d))
