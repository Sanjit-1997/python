import numpy as np
import matplotlib.pyplot as plt
people=[10,20,22,30,35,24,26,85,96,15,74,46,45]
age_group=[0,10,20,30,40,50,60,70,80,90]
plt.hist(people,age_group,rwidth=0.2)
plt.xticks(age_group)
plt.yticks(range(0,5))
plt.show()
