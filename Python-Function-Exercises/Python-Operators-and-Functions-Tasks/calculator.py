# Task 9: Calculate using +, -, *, /, //, %, or ** and handle invalid operators and division by zero.
def calculate(a, operator, b):
    valid_operators = ("+", "-", "*", "/", "//", "%", "**")
    if operator not in valid_operators:
        raise ValueError("Invalid operator. Use +, -, *, /, //, %, or **.")

    if operator in ("/", "//", "%") and b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
    elif operator == "//":
        return a // b
    elif operator == "%":
        return a % b
    else:
        return a ** b

a = int(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /, //, %, **): ")
b = int(input("Enter second number: "))
result = calculate(a, operator, b)
print("Result:", result)