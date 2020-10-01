import math
fig = input("For which figure do you want to calculate ?")
pie = 22/7
if fig == "Square":
    no1 = float(input("Enter the length of the side "))
    type = input("What do you want to calculate ?")
    if type == "Area":
        print(no1**2)
    elif type =='Perimeter':
        print(4*no1)
    else:
        print("Invalid Type")
if fig == "Rectangle":
    l = float(input("Enter the length"))
    w = float(input("Enter the width"))
    type = input("What do you want to calculate ?")
    if type == "Area":
        print(l*w)
    elif type == "Perimeter":
        print(2*(l+w))
    else:
        print("Invalid Type")
if fig == "Triangle":
    b = float(input("Enter the length of the base"))
    h = float(input("Enter the height"))
    a = (b*h)/2
    print("The area is ",a)
if fig == "Circle":
    r = float(input("Enter the radius of the circle"))
    type = input("What do you want to calculate")
    if type == "Area":
        print(pie*(r**2))
    elif type == "Circumference":
        print(2*pie*r)
    else:
        print("Invalid Type")

