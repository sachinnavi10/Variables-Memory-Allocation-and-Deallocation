# Python operators:
# 1. Arithmetic operators: +, -, *, /, //, %, **
# 2. Assignment operators: =, +=, -=, *=, /=, //=, %=, **=
# 3. Comparison operators: ==, !=, >, <, >=, <=
# 4. Logical operators: and, or, not
# 5. Identity operators: is, is not
# 6. Membership operators: in, not in
# 7. Bitwise operators: &, |, ^, ~, <<, >>
# 8. Ternary operator: value_if_true if condition else value_if_false

# Task 1: Return addition, subtraction, multiplication, division, floor division, and remainder.
def calculate(first_number, second_number):

    addition = first_number + second_number
    subtraction = first_number - second_number
    multiplication = first_number * second_number

    if second_number == 0:
        division = "Error: Cannot divide by zero"
        floor_division = "Error: Cannot divide by zero"
        remainder = "Error: Cannot divide by zero"
    else:
        division = first_number / second_number
        floor_division = first_number // second_number
        remainder = first_number % second_number

    return addition, subtraction, multiplication, division, floor_division, remainder


first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

addition, subtraction, multiplication, division, floor_division, remainder = calculate(
    first_number, second_number
)

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Floor division:", floor_division)
print("Remainder:", remainder)
