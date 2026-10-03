def add(a, b): return a + b
def subract (a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    return a / b

try:
    op = input("Operation (+, -, *, /): ")
    x = float(input("Number 1:"))
    y = float(input("Number 2:"))

    if op == "+": print(add(x,y))
    elif op == "-": print(subract(x,y))
    elif op == "*": print(multiply(x,y))
    elif op == "/": 
        if y == 0: print("Cannot divide by zero.")
        else: print(divide(x,y))
    else: print("Invalid operation.")
except ValueError:
    print("Invalid input. Use numbers")