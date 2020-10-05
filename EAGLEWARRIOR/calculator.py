# Simple calculator in Python
i=int(input("Enter 1st number : "))
v=int(input("Enter 2nd number : "))
o=input("Enter operator(+,-,*,/,**,%): ")

if o=="+":
    print("Your aanswer is:", i+v)    
elif o=="-":
    print("Your answer is:", i-v)
elif o=="/":
     print("Your answer is:", i/v)
elif o=="*":
     print("Your answer is:", i*v)
elif o=="**":
     print("Your answer is:", i**v)
elif o=="%":
     print("Your answer is:", i%v)
elif o=="//":
    print("Your answer is:", i//v)
else :
    print("Invalid operation")
