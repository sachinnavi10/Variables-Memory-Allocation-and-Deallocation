# Language Comparison: JavaScript, Node.js, Python, and Java

This guide explains how these languages handle variables, objects, functions, and memory, using simple words and examples.

> **Note:** JavaScript and Python are languages. **Node.js is a program that runs JavaScript**, often on servers. It uses the V8 JavaScript engine and adds tools for working with files, networks, and other services.

## 1. Declaring variables

| Language | Example | Meaning |
| --- | --- | --- |
| JavaScript | `let count = 1;` | Makes a variable that can be changed |
| JavaScript | `const settings = {};` | The name cannot point to a different value, but the object can still be changed |
| JavaScript | `var count = 1;` | An older way to make a variable |
| Python | `count = 1` | Gives a name to a value |
| Java | `int count = 1;` | Makes a variable and states its type |

Python does not need a special word to make a variable. A name can refer to values of different types:

```python
value = 10
value = "ten"
```

In JavaScript, `const` protects the name, not the object:

```javascript
const user = { name: "Ari" };
user.name = "Sam"; // Allowed: the object changes.
// user = {};      // Error: the name cannot point to a new object.
```

## 2. Static and dynamic types

- **Java uses static types:** Java checks many type rules before the program runs. An `int` variable cannot hold text.
- **JavaScript and Python use dynamic types:** Types are checked while the program runs. A name can refer to a number and later to text.
- All three languages have types. They mainly differ in when and how they check them.

```javascript
let value = 10;
value = "ten"; // Allowed
```

```java
int value = 10;
// value = "ten"; // Error: text cannot be stored in an int.
```

## 3. Basic values and objects

- **JavaScript:** Numbers, strings, and true/false values are basic values. Arrays, functions, and objects are objects.
- **Python:** Every value is an object, including numbers, strings, and lists.
- **Java:** Types such as `int` and `boolean` are basic types. Arrays and class instances are objects.

These differences affect how values are compared, changed, and passed to functions. They do not tell us exactly where a value is kept in memory.

## 4. Variables, objects, and references

A variable is a name for a value. For an object, the value acts like a link to that object. Giving the value to another name usually copies the link, not the whole object.

```javascript
const first = { score: 5 };
const second = first;
second.score = 9;
console.log(first.score); // 9: both names point to the same object.
```

To copy an object in JavaScript, you can use `{ ...first }`. This only makes a shallow copy: objects inside it are still shared.

### What does `a == b` mean?

It depends on the language:

- **JavaScript:** `==` may change types before comparing. `===` compares without that type change. For objects, both check if the two values point to the same object.
- **Python:** `==` usually checks whether values are equal. `is` checks whether two names point to the same object.
- **Java:** `==` compares basic values, but for objects it checks whether two references point to the same object. Use `.equals()` to compare object contents when that class supports it.

```javascript
console.log(3 == "3");  // true: JavaScript changes a type for the comparison.
console.log(3 === "3"); // false: number and text are different types.
console.log({} === {}); // false: these are two different objects.
```

```python
a = [1, 2]
b = [1, 2]
print(a == b)  # True: same contents
print(a is b)  # False: different list objects
```

```java
String a = new String("hi");
String b = new String("hi");
System.out.println(a == b);      // false: different objects
System.out.println(a.equals(b)); // true: same text
```

## 5. Changeable and unchangeable values

An **unchangeable** value cannot be changed after it is made. A **changeable** object can be updated.

| Language | Unchangeable examples | Changeable examples |
| --- | --- | --- |
| JavaScript | strings, numbers, true/false values | arrays, objects, `Map`, `Set` |
| Python | strings, integers, many tuples | lists, dictionaries, sets |
| Java | `String`, `Integer` | arrays, most lists and other collections |

Changing a variable is not the same as changing an object. For example, adding text creates a new string, while adding an item changes a list:

```python
text = "hi"
text += "!"        # Makes a new string.
items = [1, 2]
items.append(3)    # Changes the existing list.
```

JavaScript and Java strings also cannot be changed in place. Arrays can be changed:

```javascript
let text = "hi";
text += "!";       // Makes a new string value.
const items = [1, 2];
items.push(3);     // Changes the array.
```

```java
String text = "hi";
text = text + "!"; // Makes a new String and stores it in text.
int[] items = {1, 2};
items[0] = 9;      // Changes the array.
```

## 6. Stack and heap memory

Think of memory in two broad areas:

- The **stack** keeps track of active function and method calls, including their local work.
- The **heap** holds objects and other data that may need to live beyond one function call.

The saying **“variables are on the stack, objects are on the heap”** is too simple:

1. Each language and runtime can store things differently.
2. A local variable might hold a basic value or a link to an object.
3. The local link may be part of a function call, while the object it points to is elsewhere.
4. If a function returns an object or a saved function uses a local value, that data may need to stay alive after the call ends.
5. The runtime may move or store values in other ways to make the program faster.

Stack and heap are useful ideas, but they do not tell us the exact place of every value.

## 7. What happens during a function call?

When a function or method runs, the program generally:

1. Keeps track of the new call.
2. Makes its inputs (parameters) and local variables available.
3. Runs its instructions. It may make objects or call more functions.
4. Gives back a result, if there is one.
5. Finishes the call and removes its ordinary local work.

An object made inside a function can stay alive if the function returns it or saves it somewhere:

```python
def make_list():
    local = [1, 2]
    return local

saved = make_list()
print(saved) # [1, 2]
```

The list can still be used because `saved` points to it.

## 8. Functions in each language

- **JavaScript and Python:** Functions can be saved in variables, sent to other functions, and returned from functions.
- **Java:** Methods belong to classes or objects. Java lambdas can be used where a function-like value is needed.

```javascript
const double = x => x * 2;
function apply(fn, value) {
  return fn(value);
}
console.log(apply(double, 4)); // 8
```

```python
def double(x):
    return x * 2

def apply(fn, value):
    return fn(value)

print(apply(double, 4)) # 8
```

```java
import java.util.function.Function;

Function<Integer, Integer> doubleValue = x -> x * 2;
System.out.println(doubleValue.apply(4)); // 8
```

## 9. How values are sent to functions

When a function is called, it gets the value given to it.

- **JavaScript:** The function gets a copy of the value. If that value points to an object, both the caller and function can see the same object.
- **Python:** The function gets access to the same object. Changing a shared list or object can be seen by the caller.
- **Java:** The function gets a copy of the value. For an object, that value is a link to the same object.

In all three, changing a shared object can affect what the caller sees. But giving the function's local parameter a new value does not change the caller's variable.

```javascript
function update(item) {
  item.count++;        // Changes the shared object.
  item = { count: 0 }; // Changes only the local name.
}
const data = { count: 1 };
update(data);
console.log(data.count); // 2
```

```python
def update(items):
    items.append(3)    # Changes the shared list.
    items = ["new"]    # Changes only the local name.

values = [1, 2]
update(values)
print(values) # [1, 2, 3]
```

```java
static void update(int[] values) {
    values[0] = 9;         // Changes the shared array.
    values = new int[]{0}; // Changes only the local name.
}
```

So it is misleading to say “Java passes objects by reference.” Java copies the reference value; it does not give the function the caller's variable.

## 10. Saved functions (closures)

A **closure** is a function that can still use values from the place where it was made.

- **JavaScript:** A returned function can keep using a variable from its outer function.
- **Python:** A nested function can use a variable from the function around it. `nonlocal` lets it change that variable.
- **Java:** A lambda can use a local variable if that variable is not later given a new value. The object it points to may still be changed.

```javascript
function makeCounter() {
  let count = 0;
  return () => ++count;
}
const next = makeCounter();
console.log(next()); // 1
console.log(next()); // 2
```

```python
def make_counter():
    count = 0
    def next_count():
        nonlocal count
        count += 1
        return count
    return next_count

next_count = make_counter()
print(next_count()) # 1
```

The saved function can keep its needed values after the original function ends. If the program keeps that saved function, those values must also stay available.

## 11. Garbage collection

Garbage collection is a way for the runtime to clean up objects the program can no longer use. It does not always happen right away.

An object may be cleaned up when nothing in the running program can reach it anymore. The exact rules and timing depend on the runtime.

- JavaScript's `delete` removes an object property. It does not directly free the object.
- Python's `del` removes a name or item. Other names may still point to the object.
- Java has no general `delete` command for objects. The runtime cleans up objects that are no longer in use.

Files, network connections, and similar resources should be closed directly using the language's resource tools. Do not wait for garbage collection to close them.

## 12. How garbage collection differs

| Runtime | Simple description |
| --- | --- |
| JavaScript in V8, including Node.js | Looks for objects the program can still reach and cleans up objects it cannot reach |
| CPython | Counts references to objects and also checks for some unreachable object cycles |
| Java on the JVM | Looks for objects the program can still reach and cleans up objects it cannot reach |

These are general descriptions. Other Python runtimes may work differently, and no row promises exactly when cleanup happens.

## 13. Memory leaks can still happen

Garbage collection cannot clean up an object that the program still points to, even if the program no longer needs it. This can happen when:

- A cache keeps growing and never removes old items.
- A global list keeps old data.
- Event listeners are added but never removed.
- A long-running list keeps completed tasks or old requests.
- A saved function keeps large objects it no longer needs.

For example, if each request adds a listener and it is never removed, the program may keep every listener and its data in memory.

## 14. What runs the code?

- **JavaScript** is a programming language. V8 is one program that runs JavaScript; browsers may use other programs.
- **Node.js** runs JavaScript outside the browser and adds tools for servers and system tasks.
- **Python** is a programming language. CPython is its most common program for running Python code.
- **Java** code commonly runs on the Java Virtual Machine, called the JVM.

The language and the program that runs it are not the same thing. For example, JavaScript itself does not include all the server tools that Node.js provides.

## 15. Compiling and running code

The simple idea **“compiled or interpreted”** does not tell the whole story. Many runtimes use a mix of steps:

- **JavaScript / V8:** V8 reads JavaScript and may turn often-used code into machine code while the program runs.
- **CPython:** Python code is turned into bytecode, which the Python runtime runs.
- **Java:** Java code is usually turned into bytecode. The JVM runs it and may turn often-used parts into machine code.

How fast a program runs depends on more than these steps. It also depends on the work being done, the libraries, and the computer.

## 16. Event loops and threads

- **Node.js:** Often uses an event loop to handle many waiting tasks, such as network requests. Heavy calculations can block the event loop and slow other work.
- **Python `asyncio`:** Uses an event loop for tasks that wait for things like network replies. A long calculation can block the loop unless moved elsewhere.
- **Java:** Can use threads to run tasks at the same time. Threads can help with calculations and waiting tasks, but need careful coordination.

In general:

- **I/O work** means waiting for a network, disk, or database. Handling several waits at once can help.
- **CPU work** means doing calculations. Using more cores can help, depending on the runtime and program.

Doing work at the same time does not always mean it runs at the same time on different CPU cores.

## 17. What happens during a web request?

A simple server request often works like this:

1. The server receives a request.
2. It runs a function or method to handle it.
3. The code reads request data and may make objects.
4. It may ask a database or another service for information.
5. It uses the result to make a response, often JSON or text.
6. The server sends the response back.

When the handler ends, its local names are no longer used. Objects can stay alive if another part of the program still points to them.

```javascript
async function getUser(req, res) {
  const user = await database.findUser(req.params.id);
  res.json({ name: user.name });
}
```

Here, `user` is a local name. The user object can stay alive longer if the database code, a cache, or another part of the program keeps it.

## 18. How to think about speed

Instead of asking **“Which language is fastest?”**, ask:

- Is the program mostly doing calculations or waiting for a database or network?
- How much data does it use?
- Does it need to respond quickly, handle many users, or use little memory?
- What computer, runtime, libraries, and system design will it use?

Test the program with work like the real task. A slow database may matter much more than the language.

## 19. How long do variables and objects last?

Keep these ideas separate:

1. **A variable's lifetime:** A local name is usually used while its function is running.
2. **An object's lifetime:** An object can stay usable as long as some part of the program still points to it.
3. **Cleanup time:** When no part of the program points to an object, it may be cleaned up later. The runtime decides when.

An object can live longer than the function that made it. Also, cleanup does not always mean the runtime immediately returns that memory to the computer.

## 20. What happens when this line runs?

The exact steps depend on the values and their types. In general, the program reads `a` and `b`, adds them using that language's rules, then stores the result.

### Python

```python
result = a + b
```

Python checks the values' types and uses the matching addition rule. For numbers it adds them. For lists, it joins them into a new list:

```python
print(2 + 3)        # 5
print([1, 2] + [3]) # [1, 2, 3]
```

### JavaScript

```javascript
let result = a + b;
```

JavaScript follows its `+` rules. It can add numbers or join text:

```javascript
console.log(2 + 3);   // 5
console.log("2" + 3); // "23"
```

### Java

```java
int result = a + b;
```

If `a` and `b` are `int` values, Java adds the numbers and stores the answer in `result`. Java checks that the types make sense before the program runs:

```java
int a = 2;
int b = 3;
int result = a + b; // 5
```

Java integer addition can go beyond the range an `int` can hold. In that case, it wraps around rather than reporting an error.

## Quick recap

- A variable is a name for a value.
- Two names can point to the same object.
- Changing a shared object can be seen through either name.
- In JavaScript, Python, and Java, a function gets the value passed to it. For an object, that value can be a link to a shared object.
- Stack and heap are helpful ideas, but they do not show the exact place where every value is stored.
- Garbage collection cleans up objects that are no longer in use, but not always right away.
- Node.js runs JavaScript; it is not a separate language.
