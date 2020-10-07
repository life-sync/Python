
def fib_series(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[-1] + fib[-2])
    return fib

terms = int(input("Enter Number of Terms: "))
print(fib_series(terms))