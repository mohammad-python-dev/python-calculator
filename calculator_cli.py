def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def get_operation():
    while True:
        op = input("Choose operation (+, -, *, /): ")
        if op in ["+", "-", "*", "/"]:
            return op
        print("Invalid operation.")

def calculate(a, op, b):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            raise ZeroDivisionError
        return a / b

print("=== Python Calculator ===")
a = get_number("Enter first number: ")
op = get_operation()
b = get_number("Enter second number: ")

try:
    result = calculate(a, op, b)
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
