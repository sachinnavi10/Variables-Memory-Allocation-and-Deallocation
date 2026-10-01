# Functions

## 1. Why functions?

```python
print("Sachin")
print("BGM")
print("Virat")
```

Instead of repeating the same code, we can use a function:

```python
def welcome(name):
    print("Welcome", name)

welcome("Sachin")
welcome("BGM")
welcome("Virat")
```

### Problems solved by functions

- code reuse
- less repetition
- better organization
- easier maintenance
- easier testing

---

## 2. What exactly is a function?

A function is a reusable block of code that performs a specific task.

```python
def add(a, b):
    return a + b

result = add(2, 3)
print(result)  # 5
```

---

## 3. Defining vs calling a function

### Definition

```python
def greet():
    print("Hello")
```

This does not execute the function yet.

### Calling

```python
greet()
```

This executes the body of the function.

---

## 4. Function without parameters

```python
def welcome():
    print("Welcome to Nighan2 Lab")

welcome()
```

This is the simplest form of a function.

---

## 5. Function with parameters

```python
def welcome(name):
    print("Welcome", name)

welcome("Sachin")
```

Here:

- `name` is a parameter
- `"Sachin"` is an argument

---

## 6. Multiple parameters

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

---

## 7. Return: the most important concept

Compare these two functions:

```python
def add(a, b):
    print(a + b)
```

and

```python
def add(a, b):
    return a + b
```

### Difference

- `print()` displays the value on the screen
- `return` sends the value back to the caller

```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)  # 30
```

---

## 8. What happens after return?

```python
def test():
    return 10
    print("Hello")
```

The line after `return` is not executed.

`return` exits the function immediately.

---

## 9. Multiple return values

Python allows a function to return multiple values.

```python
def calculate(a, b):
    return a + b, a - b, a * b

x, y, z = calculate(10, 5)
print(x)  # 15
print(y)  # 5
print(z)  # 50
```

This actually returns a tuple.

---

## 10. Default parameters

```python
def greet(name="Sachin"):
    print("Hello", name)

greet()
greet("Virat")
```

Default parameters are useful when a value is optional.

---

## 11. Positional arguments

```python
def student(name, age):
    print(name, age)

student("Sachin", 24)
```

Arguments are passed in order.

---

## 12. Keyword arguments

```python
def student(name, age):
    print(name, age)

student(age=24, name="Sachin")
```

The argument order does not matter when using names.

---

## 13. Positional and keyword arguments

```python
def student(name, age, course):
    print(name, age, course)

student("Sachin", age=24, course="BE")
```

This is valid because:

- `"Sachin"` is a positional argument
- `age=24` is a keyword argument
- `course="BE"` is a keyword argument

But this is invalid:

```python
student(name="Sachin", 24, course="BE")
```

because positional arguments cannot come after keyword arguments.

---

## 14. `*args` (variable number of positional arguments)

```python
def add(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(add(10, 20))
print(add(10, 20, 30))
print(add(10, 20, 30, 40))
```

`*args` collects all positional arguments into a tuple.

---

## 15. `**kwargs` (variable number of keyword arguments)

```python
def student(**details):
    print(details)

student(name="Sachin", age=24, course="BE")
```

`**kwargs` collects keyword arguments into a dictionary.

---

## 16. Combining positional and keyword arguments

```python
def student(name, age, course):
    print(name, age, course)

student("Sachin", age=24, course="BE")
```

Example:

- `"Sachin"` → positional argument
- `age=24` → keyword argument
- `course="BE"` → keyword argument

---

## 17. Local vs global scope

### Local variable

```python
def test():
    x = 10
    print(x)

test()
```

`x` is local to the function.

### Global variable

```python
x = 100

def test():
    print(x)

test()
```

The function can read the global variable.

---

## 18. The `global` keyword

```python
count = 0

def increment():
    global count
    count += 1

increment()
print(count)  # 1
```

`global` allows a function to modify a global variable.

> Avoid using global state unnecessarily; prefer parameters and return values.

---

## 19. Local scope inside function

```python
def test():
    x = 10

test()
print(x)
```

This raises `NameError` because `x` is local to `test()`.

---

## 20. Functions calling other functions

```python
def add(a, b):
    return a + b

def display():
    result = add(10, 20)
    print(result)

display()
```

This is a common pattern in real programs:

`main() -> validate() -> save() -> display()`

---


## Summary

- A function is a reusable block of code.
- It helps in code reuse and organization.
- Parameters are values passed into a function.
- `return` sends data back to the caller.
- Functions can have default values, `*args`, and `**kwargs`.
- Variables inside a function are local unless declared `global`.

---

## Example recap

```python
def greet(name="Sachin"):
    return "Hello, " + name

print(greet())
print(greet("Virat"))
```

Output:

```python
Hello, Sachin
Hello, Virat
```

## 21. Function calling flow
Python first executes the function definition, which creates a function object. When the call happens, the argument values are bound to the parameters, the function body runs, and `return` sends the result back to the caller.

```python
def multiply(a, b):
    return a * b

result = multiply(5, 4)
print(result)  # 20
```
Here, `5` is assigned to `a`, `4` is assigned to `b`, and the returned value is assigned to `result`.

---
## 22. Functions are objects
A function can be assigned to another name. Calling that name calls the same function; parentheses are used to call it, not when assigning it.

```python
def greet():
    print("Hello")

x = greet
x()  # Hello
```
`x` now refers to the function object `greet`.

---
## 23. Passing a function to another function

Since functions are objects, they can be passed as arguments. A function that accepts or returns another function is called a higher-order function.

```python
def square(x):
    return x * x

def process(function, value):
    return function(value)

print(process(square, 5))  # 25
```
Pass `square` without parentheses so `process` receives the function itself. `square` is called inside `process`.

---
## 24. Lambda functions

A `lambda` expression creates a small anonymous function. It contains one expression and returns that expression's value.

```python
square = lambda x: x * x
print(square(5))  # 25
```

For named operations, a `def` function is usually clearer. Lambdas are often used for short operations, such as transforming values with `map`:

```python
numbers = [1, 2, 3, 4]
result = list(map(lambda x: x * 2, numbers))
print(result)  # [2, 4, 6, 8]
```

`map` applies the function to each item; `list` collects its results into a list.

---
## 25. Recursion

A recursive function calls itself. It needs a base case to stop, and each recursive call should move toward that case.

```python
def countdown(n):
    if n == 0:
    return
    print(n)
    countdown(n - 1)

countdown(5)
```
This prints `5` through `1`. The `n == 0` base case stops the recursion.

---
## 26. Function documentation

A docstring is a string literal at the start of a function body that describes the function. It can be read through `__doc__` or displayed with `help()`.

```python
def add(a, b):
    """Return the sum of two numbers."""
    return a + b

print(add.__doc__)
help(add)
```

Clear docstrings make functions easier for other developers and tools to understand.

---
## 27. Type hints

Type hints document the expected types of parameters and return values. The return annotation goes before the colon.

```python
def add(a: int, b: int) -> int:
    return a + b

print(add(2, 3))  # 5
```

Python generally does not enforce these annotations at runtime. Editors, type checkers, and other tools can use them to help detect mistakes.

---
## 28. A practical program: electricity bill

This example charges 2 per unit for the first 100 units, 4 per unit for the next 100, and 6 per unit above 200. It also adds a fixed charge of 100.

```python
def calculate_bill(units):
    if units < 0:
        raise ValueError("Units cannot be negative")

    if units <= 100:
        amount = units * 2
    elif units <= 200:
        amount = 100 * 2 + (units - 100) * 4
    else:
        amount = 100 * 2 + 100 * 4 + (units - 200) * 6

    return amount + 100

def electricity_bill():
    units = int(input("Enter units: "))
    bill = calculate_bill(units)
    print("Bill:", bill)

electricity_bill()
```
`calculate_bill` handles the calculation, while `electricity_bill` handles input and display. Separating these responsibilities makes the calculation easier to reuse and test without interactive input, and keeps the program easier to read and maintain.

---
## 29. Function design

A well-designed function commonly has three parts:

- **Input:** parameters or other data the function receives.
- **Processing:** the work it performs.
- **Output:** a returned result or another clearly defined effect.

For example, `calculate_bill(units)` receives units, calculates a total, and returns the bill amount.

---

## 30. Avoid giant functions

### Bad: one giant function

Putting the whole student system in one function gives it too many responsibilities:

```python
def student_system():
    # 200 lines of code
    # input
    # validation
    # calculation
    # database operations
    # printing
    pass
```

### Better: split the work into focused functions

```python
def get_student():
    pass

def validate_student(student):
    pass

def calculate_result(student):
    pass

def save_result(result):
    pass

def display_result(result):
    pass
```

Each function has one clear responsibility, making the program easier to understand, test, and maintain. This improves organization and reliability, not necessarily speed.

---