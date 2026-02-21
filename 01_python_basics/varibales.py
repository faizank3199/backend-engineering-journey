# -----------------------------------
# VARIABLES IN PYTHON
# -----------------------------------

# A variable is a name bound to an object in memory
# to a value (object) in memory.


# Storing different data types

age = 22                 # Integer
name = "Faizan"          # String
height = 5.7             # Float
is_student = True        # Boolean


# -----------------------------------
# Printing values
# -----------------------------------

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student Status:", is_student)


# -----------------------------------
# Checking data types
# -----------------------------------

print(type(name))        # <class 'str'>
print(type(age))         # <class 'int'>
print(type(height))      # <class 'float'>
print(type(is_student))  # <class 'bool'>


# -----------------------------------
# MEMORY REFERENCE CONCEPT
# -----------------------------------

# Python stores objects in memory.
# Variables store references to those objects.

a = 10
b = a   # b now refers to the same object as a

print(a)  # 10
print(b)  # 10


# Checking memory address using id()
print("Memory address of a:", id(a))
print("Memory address of b:", id(b))

# If both ids are same → they refer to the same object.


# -----------------------------------
# What happens when value changes?
# -----------------------------------

a = 20   # Now 'a' points to a new object

print("New value of a:", a)
print("Value of b:", b)

print("New memory address of a:", id(a))
print("Memory address of b:", id(b))

# Now memory addresses are different.
# Because integers are immutable.

# -----------------------------------
# == vs is
# -----------------------------------

x = 100
y = 100

print(x == y)  # True → same value
print(x is y)  # True → same object (small integer caching)

m = [1, 2]
n = [1, 2]

print(m == n)  # True → same values
print(m is n)  # False → different objects

# -----------------------------------
# Mutable Example (List)
# -----------------------------------

list_a = [1, 2, 3]
list_b = list_a

list_a.append(4)

print("list_a:", list_a)
print("list_b:", list_b)
print("Same memory?", id(list_a) == id(list_b))