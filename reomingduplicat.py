list=[4,4,6,3,6,6,2,6,8]
list2=[]
for number in list:
    if(number not in list2):
        list2.append(number)

print(list2)
