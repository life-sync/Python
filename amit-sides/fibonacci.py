import argparse

def calculate_fibonacci_number(index):
    if not hasattr(calculate_fibonacci_number, "dynamic_memory"):
         calculate_fibonacci_number.dynamic_memory = [0, 1]
    if len(calculate_fibonacci_number.dynamic_memory) > index:
        return calculate_fibonacci_number.dynamic_memory[index]
    
    calculate_fibonacci_number.dynamic_memory.append(calculate_fibonacci_number(index - 1) + calculate_fibonacci_number(index - 2))
    return calculate_fibonacci_number.dynamic_memory[index]
    

def main():
    parser = argparse.ArgumentParser(description="Fibonacci  Series Calculator",
                                     epilog="A program to calculate the n'th number in the Fibonacci series, using dynamic programing.")
    parser.add_argument("index", type=int,
                        help="The index of the number in the series: F[index].")
	
    args = parser.parse_args()
    
    if args.index < 0:
        print("Error: Index must be larger or equal to zero")
        return
    
    number = calculate_fibonacci_number(args.index)
    print(f"The {args.index}'th fibonacci number is: {calculate_fibonacci_number(args.index)}")
    

if __name__ == "__main__":
    main()