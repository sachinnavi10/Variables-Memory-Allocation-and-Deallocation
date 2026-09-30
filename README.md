# Variables, Memory Allocation, and Deallocation

Variables let a program give names to values so it can store state, calculate results, and pass data between functions. In both Node.js and Python, a variable is best understood as a name bound to a value. It is not necessarily a box that contains the value itself.

```javascript
let first = { score: 10 };
let second = first;
second.score = 20;
console.log(first.score); // 20: both names refer to the same object
```

```python
first = {"score": 10}
second = first
second["score"] = 20
print(first["score"])  # 20: both names refer to the same object
```

## Scope and lifetime

Two different lifetimes are useful to distinguish:

- Name lifetime: how long a name can be accessed in its scope. A local name usually cannot be used after its function returns.
- Object lifetime: how long the value remains in memory. An object may outlive the function that created it if another reference still points to it, such as a global variable or a closure.

There is no general expiry timer for variables. When an object is no longer reachable by the program, it becomes eligible for memory reclamation. The runtime controls when reclamation occurs, so becoming unreachable does not always mean memory is released at that exact moment.

```python
def make_list():
    values = [1, 2, 3]
    return values

items = make_list()  # The list stays alive because `items` refers to it.
```

## Memory allocation in Node.js

Node.js runs JavaScript using the V8 engine.

- Function calls create execution contexts. The engine manages local bindings and may use stack-like storage, registers, or optimized representations. The language does not guarantee that every local variable occupies a literal stack slot.
- Objects, arrays, and functions are generally allocated in memory managed by V8, commonly described as the heap. Primitive values may use engine-specific representations.
- V8's garbage collector finds objects that are no longer reachable from program roots, such as active execution contexts, global values, and retained closures. It can reclaim those objects.
- V8 uses a generational garbage collector. Many short-lived objects are collected in a young generation; objects that survive may be moved to an older generation and collected differently.
- JavaScript code does not control the exact time garbage collection runs.

A closure can keep a function's local state alive after the function returns:

```javascript
function makeCounter() {
    let count = 0;
    return () => ++count;
}

const next = makeCounter(); // `count` remains reachable through `next`.
console.log(next()); // 1
```

## Python variables, objects, and built-in types

### 1. What is a variable in Python?

A variable is a name bound to an object. It is not a box that contains the object itself.

```python
x = 10
```

Conceptually, x refers to the integer object 10. Assignment binds the name x to that object.

### Important idea

- variables are references to objects
- the object exists in memory
- the variable name is a way to access the object

```python
first = {"score": 10}
second = first
second["score"] = 20
print(first["score"])   # 20
```

Both names refer to the same dictionary object.

---

## 2. Everything in Python is an object

Python's data model represents values as objects. Objects have an identity, a type, and a value.

```python
x = 10
name = "Sachin"
marks = 85.5
numbers = [10, 20, 30]
```

Conceptually:

- `x` -> integer object
- `name` -> string object
- `marks` -> float object
- `numbers` -> list object

Every Python object has:

- identity
- type
- value

```python
x = 10
print(id(x))
print(type(x))
print(x)
```

Explanation:

- `id(x)` gives the object's identity
- `type(x)` gives the object's type
- `x` gives the current value

So an object has:

- identity = where it is stored in memory
- type = what kind of object it is
- value = the actual data

---

### 3. Built-in data type categories

- Numeric: `int`, `float`, `complex`
- Boolean: `bool`
- Text: `str`
- Sequences: `list`, `tuple`, `range`
- Sets: `set`, `frozenset`
- Mapping: `dict`
- Binary: `bytes`, `bytearray`, `memoryview`
- Special value: `None` (whose type is `NoneType`)

---

### 4. Numeric types

```python
age = 25             # int
count = -10          # int
price = 99.0         # float
percentage = 88.75   # float
z = 3 + 4j           # complex
```

---

## 5. Boolean

```python
is_active = True
is_logged_in = False
```

Examples:

```python
print(bool(0))         # False
print(bool(1))         # True
print(bool(""))       # False
print(bool("hello"))  # True
```

---

## 6. Strings

A string is an immutable sequence of characters.

```python
name = "Sachin"
print(name[0])
print(name[1])
```

Strings are immutable, which means you cannot change a character directly after creation.

---

## 7. Lists

```python
numbers = [10, 20, 30]
data = [10, "python", 25.5, True]
```

Properties:

- ordered
- mutable
- allows duplicates
- can contain different types

---

## 8. Tuples

```python
point = (10, 20)
```

Properties:

- ordered
- immutable
- allows duplicates

---

## 9. Sets

```python
numbers = {10, 20, 20, 30}
print(numbers)
```

Output:

```python
{10, 20, 30}
```

Properties:

- unique elements
- mutable
- no positional indexing

---

## 10. Dictionaries

```python
student = {
    "id": 101,
    "name": "Sachin",
    "marks": 85
}
```

A dictionary stores data in key-value pairs.

```python
print(student["name"])   # Sachin
print(student["marks"])  # 85
```

---

## 11. None

```python
result = None
```

`None` represents the absence of a value.

Important:

- `None` is not `0`
- `None` is not `False`
- `None` is not `""`
- `None` is not `[]`

They are all different values with different meanings.

---

## 12. Mutable vs Immutable

### Immutable objects

Immutable objects cannot be changed after creation.

Examples:

- `int`
- `float`
- `bool`
- `str`
- `tuple`
- `frozenset`

### Mutable objects

Mutable objects can be changed after creation.

Examples:

- `list`
- `set`
- `dict`
- `bytearray`

---

## 13. Variable rebinding vs mutation

### Immutable example

```python
x = 10
x = 20
```

This looks like `x` changed from `10` to `20`, but actually:

- `x` originally referred to object `10`
- then `x` was rebound to object `20`

The integer `10` was never modified.

### Mutable example

```python
a = [10, 20]
b = a
b.append(30)
print(a)
```

Output:

```python
[10, 20, 30]
```

Both names refer to the same list object, so the list is modified in place.

---

## 14. Memory model: variables and objects

```python
a = 10
b = a
```

This means:

- `a` refers to object `10`
- `b` also refers to the same object `10`

Now:

```python
a = 20
```

Then:

- `a` points to `20`
- `b` still points to `10`

This is because integers are immutable.

---

## 15. `==` vs `is`

### `==`

Checks whether values are equal.

```python
a = [1, 2]
b = [1, 2]
print(a == b)   # True
```

### `is`

Checks whether two references point to the same object.

```python
a = [1, 2]
b = [1, 2]
print(a is b)   # False
```

Even if values are equal, the objects may be different.

---

## 16. Memory allocation and deallocation

### Memory allocation

Memory allocation is the process of reserving space in memory for data.

When a variable is assigned, Python allocates memory for the object it points to.

```python
x = 10
name = "Sachin"
values = [1, 2, 3]
```

### Deallocation

Deallocation means releasing memory that is no longer needed.

```python
x = 10
x = 20
```

The old object `10` is no longer referenced, so Python can reclaim that memory.

---

## 17. Scope and lifetime

There are two important lifetimes:

- name lifetime: how long a variable name is valid in a scope
- object lifetime: how long the object remains alive in memory

```python
def make_list():
    values = [1, 2, 3]
    return values

items = make_list()
```

The list remains alive because `items` still references it.

---

## 18. Reference counting in CPython

CPython mainly uses reference counting.

```python
a = [1, 2, 3]
b = a
```

Now both `a` and `b` reference the same list object.

```python
del b
```

The reference count decreases. The object is still alive as long as another reference exists.

---

## 19. Garbage collection

Garbage collection is automatic memory management that reclaims objects no longer reachable by the program.

Python normally does not require manual `free()` calls.

Example of a cycle:

```python
a = []
a.append(a)
```

This creates a reference cycle. Python's cyclic garbage collector can detect and clean such cycles.

---

## 20. Does `del` immediately destroy the object?

No.

```python
numbers = [1, 2, 3]
b = numbers

del numbers
print(b)
```

This still works because `b` still references the same object.

`del` removes the name, not necessarily the object itself.

---

## 21. When can an object become garbage?

An object becomes garbage when it is no longer reachable.

```python
numbers = [1, 2, 3]
other = numbers

del numbers
del other
```

Now there are no remaining references, so the object becomes eligible for garbage collection.

The exact reclamation time is implementation-dependent.

---

## 22. Conceptual model

```text
VARIABLE -> OBJECT -> MEMORY
```

- A variable is a name that points to an object.
- An object has identity, type, and value.
- Memory is allocated to store objects.
- When objects are no longer referenced, they become garbage.
- Python's garbage collector reclaims memory automatically.

---

## 23. Important interview answer

> In Python, variables are not boxes; they are references to objects. Everything in Python is an object, and objects have identity, type, and value. Memory is allocated for these objects, and when they are no longer reachable, Python reclaims that memory automatically.

---

## 24. Why `del` does not immediately destroy the object

Because `del` removes the name pointing to the object, not the object itself.

The object remains alive while other references still exist.

Only when no references remain is the object considered garbage and later deallocated by Python's memory manager.

```python
a = [1, 2, 3]
b = a
del a
```

`b` still keeps the object alive.

---

## 25. Quick revision points

- Variable = name bound to an object
- Python object = identity + type + value
- Everything is an object
- Mutable objects can change in place
- Immutable objects cannot be changed directly
- `==` compares values
- `is` compares object identity
- `del` removes references, not necessarily the object immediately
- Python manages memory automatically

---

## 26. Example code

```python
x = 10
name = "Sachin"
marks = 85.5
numbers = [10, 20, 30]

print(id(x))
print(type(x))
print(x)

print(name == "Sachin")
print(name is "Sachin")

numbers.append(40)
print(numbers)
```

This code demonstrates:

- object identity
- type checking
- equality comparison
- identity comparison
- mutable list behavior

---

## 27. Conclusion

Python variables are references to objects, not storage boxes. Objects have identity, type, and value. Python uses automatic memory management with reference counting and garbage collection to allocate and free memory efficiently. This is a core concept in Python and is often asked in interviews.
