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

print(numbers[::-1])       # Reverse list
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
# Iterating Through a List
# ===================================================

print("\n--- Iteration Example ---")

numbers = [10, 20, 30, 40]

for num in numbers:
    print(num)


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
    print(user["name"])