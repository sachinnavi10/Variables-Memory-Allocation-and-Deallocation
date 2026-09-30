# Functions

## 1. Why functions?

```python
print("Sachin")
print("BGM")
print("Arun")
print("Darshan")
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