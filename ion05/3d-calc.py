import math
pie = 22/7
fig = input("For which figure do you want to calculate ?")
if fig == "Cube":
    s = float(input("Enter the length of the side"))
    type = input("What do you want to calculate")
    if type == "LSA":
        print(4*s*s)
    elif type == "TSA":
        print(6*s*s)
    elif type == "Volume":
        print(s**3)
    else:
        print("Invalid Type")
elif fig == "Cuboid":
    l = float(input("Enter the Length"))
    w = float(input("Enter the width"))
    h = float(input("Enter the Height"))
    type = input("What do you want to c")
    if type == "LSA":
        a = 2((h*w)+(h*l))
        print(a)
    elif type == "TSA":
        print(2((h*w)+(h*l)+(l*w)))
    elif type == "Volume":
        print(l*w*h)
    else:
        print("Invalid Type")
elif fig == "Sphere":
    r = float(input("Enter the radius"))
    type = input("What do you want to calculate ?")
    if type == "TSA":
        print(4*pie*r*r)
    elif type == "Volume":
        print((4*pie*r*r*r)/3)
    else:
        print("Invalid Type")


