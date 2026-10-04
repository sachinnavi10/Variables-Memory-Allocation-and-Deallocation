# Python Function Exercises: Explanation

This guide explains the functions in the exercise files. Each function can be called directly from Python; most files also include a `main()` function that reads input and displays the result when the file is run as a script.

## 1. Arithmetic operations: `operators.py`

### `calculate(first_number, second_number)`

This function takes two numbers and returns a dictionary containing six arithmetic results:

- Addition: `first_number + second_number`
- Subtraction: `first_number - second_number`
- Multiplication: `first_number * second_number`
- Division: `first_number / second_number`
- Floor division: `first_number // second_number`
- Remainder: `first_number % second_number`

The function checks whether the second number is zero before performing the operations. It raises `ValueError` for zero because this calculator tries to compute division, floor division, and remainder together.

```python
from operators import calculate

results = calculate(10, 3)
print(results["addition"])  # 13
print(results["remainder"])  # 1
```

## 2. Operator-based calculator: `calculator.py`

### `calculate(a, operator, b)`

This function accepts two numbers and an operator string. It supports `+`, `-`, `*`, `/`, `//`, `%`, and `**` (exponentiation), and returns the result of the selected operation.

- An unsupported operator raises `ValueError`.
- `/`, `//`, and `%` with a zero second number raise `ZeroDivisionError`.

```python
from calculator import calculate

print(calculate(2, "**", 3))  # 8
print(calculate(10, "//", 3))  # 3
```

### `main()`

Reads two numbers and an operator from the user, calls `calculate()`, and prints the result. It catches invalid input, unsupported operators, and division-by-zero errors so the program displays an error instead of a traceback.

## 3. Integer properties: `integer_checks.py`

### `check_integer(number)`

Accepts an integer and returns a dictionary with four Boolean values: whether the number is even, odd, divisible by 3, and divisible by 5. A remainder of zero means the number is divisible by that divisor. The function raises `TypeError` if the argument is not an integer; Boolean values are rejected too, even though `bool` is a subclass of `int` in Python.

```python
from integer_checks import check_integer

print(check_integer(15))
# {'even': False, 'odd': True, 'divisible_by_3': True, 'divisible_by_5': True}
```

### `main()`

Reads an integer from the user, calls `check_integer()`, and prints each check as Yes or No. It reports invalid integer input.

## 4. Grade result: `student_result.py`

### `get_result(marks)`

Returns one result string. The highest threshold is checked first so marks of 75 or above receive distinction rather than only pass:

- `marks >= 75`: `"Distinction"`
- `35 <= marks < 75`: `"Pass"`
- `marks < 35`: `"Fail"`

```python
from student_result import get_result

print(get_result(75))  # Distinction
print(get_result(50))  # Pass
print(get_result(34))  # Fail
```

### `main()`

Reads marks, calls `get_result()`, and prints the result. It reports input that cannot be converted to a number.

## 5. Student eligibility: `student_eligibility.py`

### `check_eligibility(marks, attendance_percentage, backlog)`

Returns `"Eligible"` only when all three conditions are true:

1. Marks are at least 60.
2. Attendance is at least 75 percent.
3. `backlog` is `False`.

If any condition fails, it returns `"Not eligible"`. The `and` operator means every requirement must be satisfied.

```python
from student_eligibility import check_eligibility

print(check_eligibility(60, 75, False))  # Eligible
print(check_eligibility(80, 90, True))   # Not eligible
```

### `main()`

Reads marks and attendance as numbers, asks whether there is a backlog, converts the yes/no answer to a Boolean, and displays the result.

## 6. Placement eligibility and category: `placement_eligibility.py`

### `assess_candidate(age, marks, attendance, experience, has_backlog)`

Returns a two-item tuple: `(is_eligible, category)`. `is_eligible` is a Boolean; `category` is a string.

Eligibility is `True` when marks are at least 60, attendance is at least 75 percent, and there is no backlog. Experience determines the category independently:

- `experience == 0`: `"Fresher"`
- `1 <= experience <= 2`: `"Junior"`
- `experience > 2`: `"Experienced"`

Negative age or experience raises `ValueError`. Age is accepted and checked for a non-negative value, but it is not part of the eligibility rule because no age threshold was specified.

```python
from placement_eligibility import assess_candidate

eligible, category = assess_candidate(20, 70, 80, 1, False)
print(eligible, category)  # True Junior
```

### `main()`

Reads the candidate details, turns the yes/no backlog answer into a Boolean, calls `assess_candidate()`, and displays placement eligibility as Yes or No followed by the category.

## 7. Purchase discount: `discount_calculator.py`

### `calculate_discount(purchase_amount)`

Returns `(discount_amount, payable_amount)`, in that order. The discount is calculated from the purchase amount and rounded to two decimal places.

- Amount of Rs. 5,000 or more: 20 percent discount.
- Amount from Rs. 3,000 to less than Rs. 5,000: 10 percent discount.
- Amount below Rs. 3,000: 5 percent discount.
- A negative purchase amount raises `ValueError`.

```python
from discount_calculator import calculate_discount

discount, payable = calculate_discount(5000)
print(discount, payable)  # 1000.0 4000.0
```

### `main()`

Reads the purchase amount, calls `calculate_discount()`, and displays both the discount and final payable amount in rupees.

## 8. Username and password check: `user_validation.py`

### `is_valid_user(username, password)`

Returns `True` only when both values exactly match username `"admin"` and password `"python123"`; otherwise it returns `False`. Both comparisons must match because the function uses `and`.

```python
from user_validation import is_valid_user

print(is_valid_user("admin", "python123"))  # True
print(is_valid_user("admin", "wrong"))      # False
```

These fixed credentials are for the exercise only. Real applications should not store plaintext passwords directly in source code.

### `main()`

Reads a username and password, calls `is_valid_user()`, and prints whether the user is valid.

## 9. Access decision: `access_control.py`

### `check_access(age, has_id, is_employee)`

Returns `"Access granted"` when either condition is true:

- The person is at least 18 **and** has an ID; or
- The person is an employee.

The parentheses make the rule explicit: `(age >= 18 and has_id) or is_employee`. Otherwise, it returns `"Access denied"`.

```python
from access_control import check_access

print(check_access(18, True, False))  # Access granted
print(check_access(16, False, True))  # Access granted: employee rule
print(check_access(16, True, False))  # Access denied
```

### `read_yes_no(prompt)`

Prompts repeatedly until the user enters `yes`, `y`, `no`, or `n`. It returns `True` for yes and `False` for no.

### `main()`

Reads the age, ID status, and employee status, then displays the result from `check_access()`.

## 10. Required-skill lookup: `skills_checker.py`

### `check_skill(skill_name)`

Checks the name against `REQUIRED_SKILLS`, which contains `python`, `sql`, `git`, and `HTML`. It removes surrounding spaces and ignores capitalization. It returns `"Skill available"` for a match and `"Skill not available"` otherwise.

```python
from skills_checker import check_skill

print(check_skill(" html "))  # Skill available
print(check_skill("Java"))    # Skill not available
```

### `main()`

Reads a skill name from the user, calls `check_skill()`, and prints the returned message.

## Running the exercise files

From the project directory, run an individual program with Python. For example:

```bash
python calculator.py
python student_result.py
python placement_eligibility.py
```

The functions can also be imported into another Python file, as shown in the examples above.
