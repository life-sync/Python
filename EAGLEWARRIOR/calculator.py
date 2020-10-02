class Simple_arthimetic_Operation:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        
    def add(self):
        print(self.num1 + self.num2)


    def sub(self):
        print(self.num1 - self.num2)


    def mul(self):
        print(self.num1 * self.num2)


    def div(self):
        print(self.num1 / self.num2)
        
    def mod(self):
        print(self.num1 % self.num2)
        
    def expo(self):
        print(self.num1 ** self.num2)
        
    def floor(self):
        print(self.num1 // self.num2)

if __name__=='__main__':
    a = float(input("Enter the first number"))
    b = float(input("Enter the second number "))
    op = input("Enter the arthemetic operation you want to perform ")
    calculator=Simple_arthimetic_Operation(a,b)
    if op == "+":
        calculator.add()
    elif op == "-":
        calculator.sub()
    elif op == "*":
        calculator.mul()
    elif op == "/":
        calculator.div()
    elif op=="%":
        calculator.mod()
    elif op=="**":
        calculator.expo()
    elif op=="//":
        calculator.floor()

