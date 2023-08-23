string=str(input("Enter the first string"))
string1=str(input("Enter your secound string"))
c=0
length=len(string)
length1=len(string1)
if length==length1:
    for i in string:
        for j in string1:
            if(i==j):
                c+=1
    if c==length:
     print("it is anagram")
    else:
     print("it is not anagram")
                       
