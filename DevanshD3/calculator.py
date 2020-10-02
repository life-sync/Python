num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("which operation would you like to do +,-,*,/")

sym = input() 
print("the answer is:")
if sym == "+":
    print(num1+num2)

if sym == "-":
    print(num1-num2)

if sym == "*":
    print(num1*num2)

if sym == "/":
    print(num1/num2)