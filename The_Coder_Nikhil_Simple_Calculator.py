if __name__ == '__main__':
    print("Welcome To Simple Calculator\n"
          "Press 1 : Addition\n"
          "Press 2 : Subtraction\n"
          "Press 3 : Multiplication\n"
          "Press 4 : Division\n"
          "Press 0 : To Exit")
    choice = int(input())
    if choice == 0:
        exit()
    elif choice == 1:
        print(int(input("What Is Your First Number ? ")) + int(input("What Is Your Second Number ? ")))
    elif choice == 2:
        print(int(input("What Is Your First Number ? ")) - int(input("What Is Your Second Number ? ")))
    elif choice == 3:
        print(int(input("What Is Your First Number ? ")) * int(input("What Is Your Second Number ? ")))
    else:
        print(int(input("What Is Your First Number ? ")) / int(input("What Is Your Second Number ? ")))