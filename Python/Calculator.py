def calculate(a, b, op):
    try:
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return a / b
        else:
            return "Invalid Operation"

    except ZeroDivisionError:
        return "Cannot divide by zero"

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operation (+,-,*,/): ")

    result = calculate(a, b, op)
    print(f"Result: {result}")

except ValueError:
    print("Invalid number entered")