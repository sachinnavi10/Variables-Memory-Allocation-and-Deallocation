x = 10
name = "Sachin"
marks = 85.5
numbers = [10, 20, 30, 40, 50]

# print("x =", x)
# print("name =", name)
# print("marks =", marks)
# print("numbers =", numbers)

print(id(x))
print(type(x))
print(x)

print(id(name))
print(type(name))
print(name)

print(id(marks))
print(type(marks))  
print(marks)

print(id(numbers))
print(type(numbers))        
print(numbers)


# 4.Numeric type
# *int
age = 25
count = -10
print("age =", age)
print("count =", count)

print(type(age))
print(type(count))

# *float
price = 99.50
percentage = 75.25
print("price =", price)
print("percentage =", percentage)

print(type(price))
print(type(percentage))

# *complex
z = 3 + 4j
print("z =", z)
print(type(z))

# 5. Boolean
is_active = True
is_logged_in = False

print(is_active)
print(is_logged_in)
print(type(is_active))
print(type(is_logged_in))   

print(bool(0)) # False
print(bool(1)) # True
print(bool("")) # False
print(bool("1")) # True

# 6.String
name = "Sachin"

print(name)
print(name[0])
print(name[1])

# Strings are immutable in Python, so the following line will raise an error:
# name[0] = "R"

# 7.List
numbers = [10, 20, 30]

print(numbers)

# Ordered
numbers = [10, 20, 30]

print(numbers[0])
print(numbers[1])

# mutable
numbers[0] = 100
print(numbers)

# allow duplicate values
numbers = [10, 20, 30, 10, 20]  
print(numbers)

# can contain different data types
data = [10, "Sachin", 85.5, True]
print(data)

# 8. Tuple
point = (10, 20)
print(point)

# Ordered
point = (10, 20)
print(point[0])
print(point[1])

# Immutable
# point[0] = 100  # This will raise an error

# allow duplicate values
point = (10, 20, 10, 20)    
print(point)

# can contain different data types
data = (10, "Sachin", 85.5, True)
print(data)

# 9. Set
numbers = {10, 20, 20, 30}
print(numbers)

# Unique elements
numbers = {10, 20, 20, 30}
print(numbers)  

# mutable
numbers.add(40)
print(numbers)

# not used for potentially indexed like list or tuple
numbers = {10, 20, 30}
# print(numbers[0])  # This will raise an error since sets are unordered and unindexed

# 10. Dictionary
student = {
    "id": 101,
    "name": "Sachin",
    "marks": 85.5
}
print(student)

# it stores in key value pairs

# 11 none  none represent is absence of value
result = None

print(result)
print(type(result))

# 12. Mutable vs Immutable

# Mutable objects can be changed after creation
numbers = [10, 20, 30]
print(numbers)
numbers[0] = 100
print(numbers)
# Ex: list, set, dict, bytearray

# Immutable objects cannot be changed after creation
point = (10, 20)
print(point)
# point[0] = 100  # This will raise an error
# Ex: int, float, bool, str, tuple, frozenset

# 13. The Object Referenced by a Variable Is Mutable or Immutable
 # A variable itself is not mutable or immutable. The object that the variable refers to is mutable or immutable.
x = 10
x = 20
# It may look like x changed from 10 to 20, but that's not exactly what happened.
# The integer object 10 was not modified.
# Instead: x was rebound to another object, 20.
'''Conceptually:
Before:
x ─────► 10

After:
x ─────► 20'''
# The integer 10 cannot modified
# x was rebound to another object

# 14. Memory Example
a = 10
b = a
# conceptually a ─────► 10 ◄───── b
# Both a and b refer to the same object 10.
# It does not mean that Python created a second 10 object just for b.

# Now, if we change the value of a, it will not affect b:
a = 20
'''Conceptually:
a ─────► 20
b ─────► 10
a is now referring to 20, while b still refers to 10.'''

# 15. Mutable Object Example
a = [10, 20]
b = a

b.append(30)

print(a)
'''out put[10, 20, 30]
Why?
Because a -> [10, 20], b -> [10, 20]
both names reference the same list object
append() modifies that list
'''
def test():
    return 10
print("Hello")