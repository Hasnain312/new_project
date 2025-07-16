# new_project
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

# User input
print("Select operation: add, subtract, multiply, divide")
operation = input("Enter operation: ").strip().lower()

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if operation == "add":
    print("Result:", add(a, b))
elif operation == "subtract":
    print("Result:", subtract(a, b))
elif operation == "multiply":
    print("Result:", multiply(a, b))
elif operation == "divide":
    print("Result:", divide(a, b))
else:
    print("Invalid operation.")
