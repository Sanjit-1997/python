unit =int(input("Enter the unit"))
if(unit < 100):
 charge=3*unit
elif(unit<200):
 charge=(100*3)+((unit-100)*5)
elif(unit<=300):
 charge=(100*3)+(100*5)+((unit-200)*7)
else:
 charge=1500+((unit-300)*10.50)
Bill= charge
print("Your electric bill is %.2f" %Bill)
# %.2f is use for type casting in floating value
