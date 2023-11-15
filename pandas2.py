import matplotlib.pyplot as plt
No_student=[1,2,3,4,5,6,7,8,9,10]
mark=[20,12,30,23,22,15,25,26,24,16]
previous_mark=[23,24,25,26,11,14,13,18,19,20]
plt.scatter(No_student,mark,color='red',label='currentmark')
plt.scatter(No_student,previous_mark)
plt.title("Mark Review")
<Axes: xlabel='no.of student'>
plt.show()

