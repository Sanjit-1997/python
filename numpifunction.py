import numpy as np
a=np.array((1,2,3))
b=np.array((4,5,6))
c=a+b
print(c)
d=10
e=6
print("binary representation of d is:",bin(d))
print("binary representation of e is:",bin(e))
print("bitwise and of d and e is :", np.bitwise_and(d,e))
print("bitwise and of d or e is :", np.bitwise_or(d,e))
