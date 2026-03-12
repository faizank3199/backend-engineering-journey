# =====================================================
#                 Python Lists
# =====================================================

"""
==================================================================
Lists in Python

A list is an ordered and mutable data structure
that can store multiple values.

Properties:
- Ordered
- Mutable (elements can be modified)
- Allows duplicates
- Can store mixed data types

Topics Covered:
- Creating lists
- Indexing
- Negative indexing
- Slicing
- List methods
- Iteration
- List comprehension
- Nested lists

List Methods Covered:
- len()
- append()
- insert()
- extend()
- remove()
- pop()
- sort()
- sorted()
- reverse()

Author : Mohammad Faizan
Date   : 10/03/2026
==================================================================
"""

# ---------------------------------------------------
# Creating Lists

numbers = [10, 20, 30, 10, 50]
fruits = ["Apple", "Orange", "Mango"]
data = ["Faizan", 10, 10.5, True]

print("\n--- Creating Lists ---")
print(numbers)
print(fruits)
print(data)


# ---------------------------------------------------
# Modifying List Elements (Lists are mutable)

print("\n--- Mutable List Example ---")

nums = [10, 20, 30]
nums[1] = 40
print(nums)


# ---------------------------------------------------
# Accessing Elements (Indexing)

print("\n--- Indexing Example ---")

fruits = ["Apple", "Orange", "Mango"]

print(fruits[0])   # Apple
print(fruits[1])   # Orange


# ---------------------------------------------------
# Negative Indexing

print("\n--- Negative Indexing Example ---")

numbers = [10, 20, 30, 10, 50]

print(numbers[-1])   # 50
print(numbers[-2])   # 10
print(numbers[-4])   # 20


# ---------------------------------------------------
# List Slicing
# Format: [start:end:step]

print("\n--- Slicing Example ---")

numbers = [10, 20, 30, 10, 50]

print(numbers[2:])      # [30,10,50]
print(numbers[:2])      # [10,20]
print(numbers[1:4])     # [20,30,10]
print(numbers[::2])     # [10,30,50]
print(numbers[:3:3])    # [10]


# ---------------------------------------------------
# Negative Slicing

print("\n--- Negative Slicing Example ---")

numbers = [10, 50, 30, 20, 40, 60]

print(numbers[::-1])       # reverse list
print(numbers[:-4:-1])     # [60,40,20]
print(numbers[-5:-2])      # [50,30,20]


# ===================================================
# List Methods
# ===================================================

# ---------------------------------------------------
# len()

print("\n--- Length of List ---")

numbers = [10, 20, 30, 10, 50]
print(len(numbers))


# ---------------------------------------------------
# append()

print("\n--- Append Example ---")

numbers = [10, 20, 30, 10, 50]
numbers.append(40)     # add element at the end
print(numbers)


# ---------------------------------------------------
# insert()

print("\n--- Insert Example ---")

nums = [1, 2, 3, 5]
nums.insert(3, 4)      # insert 4 at index 3
print(nums)


# ---------------------------------------------------
# extend()

print("\n--- Extend Example ---")

nums1 = [1, 2, 3, 4]
nums2 = [4, 5, 6, 7]

nums1.extend(nums2)    # add list into another list
print(nums1)


# ---------------------------------------------------
# remove()

print("\n--- Remove Example ---")

numbers = [1, 2, 3, 4, 5]
numbers.remove(3)      # remove value
print(numbers)


# ---------------------------------------------------
# pop()

print("\n--- Pop Example ---")

numbers = [1, 2, 3, 4, 5]

numbers.pop()          # remove last element
print(numbers)

numbers.pop(3)         # remove element at index 3
print(numbers)


# ---------------------------------------------------
# sort()

print("\n--- Sort Example ---")

lis = [30, 10, 20, 50, 40, 60, 40]

lis.sort()             # modifies original list
print(lis)


# ---------------------------------------------------
# sorted()

print("\n--- Sorted Example ---")

lis1 = [30, 10, 20, 50, 40, 60, 40]

new_list = sorted(lis1)    # creates new sorted list
print(new_list)


# ---------------------------------------------------
# reverse()

print("\n--- Reverse Example ---")

num = [1, 2, 3, 4, 5]

num.reverse()              # reverse list in place
print(num)


# ===================================================
# Membership Operator
# ===================================================

print("\n--- Membership Example ---")

numbers = [10, 20, 30, 40]

print(20 in numbers)   # True
print(100 in numbers)  # False


# ===================================================
# Iterating Through a List
# ===================================================

print("\n--- Iteration Example ---")

numbers = [10, 20, 30, 40]

for num in numbers:
    print(num)


# ---------------------------------------------------
# Iteration with index

print("\n--- Loop with Index ---")

numbers = [10, 20, 30, 40]

for i in range(len(numbers)):
    print(f"index - {i}, value - {numbers[i]}")


# ---------------------------------------------------
# enumerate()

print("\n--- Enumerate Example ---")

numbers = [10, 20, 30, 40, 50]

for i, val in enumerate(numbers):
    print(f"index - {i}, value - {val}")


# ===================================================
# List Comprehension
# ===================================================

print("\n--- List Comprehension Example ---")

squares = [x * x for x in range(6)]

print(squares)


# ===================================================
# Backend Style Example
# ===================================================

print("\n--- Backend Style Example ---")

users = [
    {"name": "Faizan", "age": 22},
    {"name": "Ali", "age": 25},
    {"name": "Sara", "age": 21}
]

for user in users:
    print(f"{user['name']} -> {user['age']}")


# ===================================================
# Nested Lists
# ===================================================

# A nested list is a list that contains other lists
# matrix[row][column]

print("\n--- Nested List Example ---")

users = [
    ["Faizan", 22],
    ["Rahul", 25],
    ["Ammir", 24]
]

print(users[0][0])  # Faizan
print(users[2][1])  # 24


# ---------------------------------------------------
# Nested list using loop

print("\n--- Nested List Using Loop ---")

for user in users:
    print(f"name - {user[0]}, age - {user[1]}")
    
#------------------------------------------------------
# add new user in users and update nested value
users = [
    ["Faizan", 22],
    ["Rahul", 25],
    ["Ammir", 24]
]
print("\n--Nested list update example--")
users.append(["admin",24])
for user in users:
    print(user)
    
#update nested value
print("\n--update nested value example--")
users[3][1] = 26
print(users)



# ---------------------------------------------------
# Filter example

print("\n--- Age > 22 Example ---")

for user in users:
    if user[1] > 22:
        print(user)
        
#-------------------------------------------------------

#=================================================================
# Shallow copy and deep copy
#=================================================================
"""
 shallow copy -
 A shallow copy creats a new outer object, but the inner inner object
 shared between the origanl and the copy.
 
 - outer list is new 
 - inner elements refrence the same memory
 
"""
# safe for id list 
a = [1,2,3,4]
print("\n-Example of shallow copy--")
b = a.copy()
b.append(5)
print("origanl: ",a)
print("Copy: ",b)

# shallow copy problem with nested list

a = [
    [10,20],
    [20,30]
]
print("\n--Shallow copy problem with nested list example--")
b=a.copy()      
b[1][1]= 99
                 # origanl will also change 
print("Orignal: ",a)      
print("Copy: ",b)

"""
- Becouse .copy() only copies outer list but inner list refrence same 
- So outer list become new list 
- But inner list refrence same
- Both list point he same inner object

- When Shallow copy is safe:
  - Shallow copy is fine when elements are immutable
  - like, integers can not change -> safe 
    
- When It Becomes Dangerous: 
  -When objects are nested:
    - list inside list
    - dict inside dict
    - objects inside objects
Then change affect both copies.    

"""
#==========================================================================================

"""
Deep Copy- 

Deep copy creats a completly new object, and also nested objects inside it are also copied.
So, the copy becomes fully indipendent form the orignal.
outer object -> new
inner object -> new 

"""

import copy

orignal  = [
    [1,2,3],
    [1,2,3]
]
print("\n--Deep Copy Example--")
deep_copy  = copy.deepcopy(orignal)

deep_copy[0][2] = 4

print("Orignal: ",orignal)
print("Deep Copy: ", deep_copy)

# With dictionary

user1 = {
    "name" : "Faizan",
    "skills" : ["Python", "FastApi"]
}
print("\n--Deep Copy With Dictionary Example--")
user2 = copy.deepcopy(user1)

user2["skills"].append("Docker")

print("Orignal: ",user1)
print("Deep Copy: ",user2)   # only user2 changed

"""
Deep Copy is  used when working with nested data structures:
- lists inside lists
- Dictionaries inside dictionaries
- Objects inside objects
- JSON-like structures (common in backend)
    
"""

