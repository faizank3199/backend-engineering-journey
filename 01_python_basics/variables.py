# -----------------------------------
# VARIABLES IN PYTHON
#------------------------------------
"""
Python Variables Mastery
------------------------
Topics Covered:
1. Naming conventions
2. Dynamic typing
3. Multiple assignment
4. Memory reference (id())

Author: Faizan
Date: 2026-02-22
"""

# A variable is a name bound to an object in memory
# to a value (object) in memory.

#--------------------------------------------
# 1. Naming Conventions 
#--------------------------------------------
# Good variable names are descriptive , lowercase with underscore for readability 
first_name = "Faizan"             # recommended
age = 25                          # recommended
PI = 3.14159                      # constant, Uppercase by convention

# Avoid using:
# 1.Reserved keywords like 'for','if','class'
# 2.Single letters ( except in loops or maths )
# 3.Special Characters (!,@,#,& , etc.)
# 4.Spaces (use underscores instead )


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
#----------------------------------------
# 2. Dynamic Typing 
#----------------------------------------
# Python is dynamically  typed , variable type  can change at  runtime 
x=40
print(x,type(x))

x="python" # now string
print(x,type(x))

x=40.5     # now float 
print(x,type(x))

#-------------------------------------------
# 3. Multiple assignment 
#-------------------------------------------
# Assign multiple variables in a single line 
a, b, c = 10, 20, 30
print(a,b,c)

# Assign same value in  multiple variables
x = y = z = 100
print(x,y,z)
# swap values without temp variables 
print("before swap :","a->",a, "b->",b)
a, b = b, a
print("after swap :","a->",a,"b->",b)


# -----------------------------------
# 4. MEMORY REFERENCE CONCEPT
# -----------------------------------

# Python stores objects in memory.
# Variables store references to those objects.
# Immutable objects (int, float, str, tuple) create a new object when modified.

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

print(x == y)  # True → values are equal
print(x is y)  # True → same object in memory (small integer caching)

m = [1, 2]
n = [1, 2]

print(m == n)  # True → same values
print(m is n)  # False → different objects

# -----------------------------------
# Mutable Example (List)
# -----------------------------------
# modifying list_a affects memory reference 
list_a = [1, 2, 3]
list_b = list_a

list_a.append(4)

print("list_a:", list_a)
print("list_b:", list_b)
print("Same memory?", id(list_a) == id(list_b))   # True both ids are same


#-------------------------------------
# Main Test 
#-------------------------------------

if __name__=="__main__":
    print("\nvariables.py test completed successfully!")

