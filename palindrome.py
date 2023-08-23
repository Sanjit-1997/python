word=str(input("enter the string"))#121
len=len(word)
size=len
flag=0
for i in range(0,len//2):
    if (word[i]==word[size-1]):
        size -=1
    else:
        flag=1
        break

if flag==0:
    print("it is palindrome")
else:
    print("it is not palindrome")
    
