"""
=============================================
              Sets in Python
=============================================



Description:
Comprehensive guide to Python Sets with:
- Creation
- Methods
- Operations
- Backend use cases
- Practice problems

Author: Mohammad Faizan
Date: 2026
"""

# =============================================
# BASIC SET EXAMPLE
# =============================================

print("\n== Set Example ==")
numbers = {1, 2, 3, 4, 5}
print(numbers)


# =============================================
# 1. CREATING SETS
# =============================================

# String Set
fruits = {"Apple", "Banana", "Mango", "Orange"}

# Integer Set
nums = {1, 2, 3, 4, 5}

# Mixed Data (only hashable allowed)
mixed = {"Welcome", (1, 2, 3), 5, 6}

# Empty Set
print("\n== Empty Set ==")
empty_set = set()
print(type(empty_set))  # set

# From List → Removes duplicates
print("\n== List to Set ==")
nums_list = [1, 2, 2, 3, 3, 4]
unique_nums = set(nums_list)
print(unique_nums)

# From String
print("\n== String to Set ==")
text = "Hello"
print(set(text))

# From Tuple
print("\n== Tuple to Set ==")
tup = (1, 2, 2, 3)
print(set(tup))

# Hashable Example
valid_set = {(1, 2), (3, 4)}
print(valid_set)


# =============================================
# 2. SET METHODS
# =============================================

print("\n== Add ==")
s = {1, 2, 3}
s.add(4)
print(s)

print("\n== Update ==")
s.update([5, 6])
print(s)

print("\n== Remove ==")
s.remove(6)
print(s)

print("\n== Discard (Safe Remove) ==")
s.discard(10)  # No error

print("\n== Pop (Random Remove) ==")
s.pop()
print(s)

print("\n== Clear ==")
s.clear()
print(s)


# =============================================
# 3. BACKEND EXAMPLE
# =============================================

print("\n== Backend Use Case ==")
users = {"Faizan", "Rohan"}
users.update(["Ali", "Ram", "John"])
print(users)


# =============================================
# 4. SET OPERATIONS
# =============================================

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# ---------------------------------------------
# UNION
# ---------------------------------------------
print("\n== Union ==")
print(set_a | set_b)
print(set_a.union(set_b))

# Backend: Merge Users
db_users = {"Sohan", "Radhika"}
api_users = {"Ali", "John"}
print(db_users | api_users)

# ---------------------------------------------
# INTERSECTION
# ---------------------------------------------
print("\n== Intersection ==")
print(set_a & set_b)

user1 = {"Faizan", "Ali", "John"}
user2 = {"John", "Shyam", "Faizan"}
print(user1 & user2)

# ---------------------------------------------
# DIFFERENCE
# ---------------------------------------------
print("\n== Difference ==")
print(set_a - set_b)
print(set_b - set_a)

# Backend: Remove blocked users
all_users = {"Faizan", "Ali", "John"}
blocked = {"Ali"}
print(all_users - blocked)

# ---------------------------------------------
# SYMMETRIC DIFFERENCE
# ---------------------------------------------
print("\n== Symmetric Difference ==")
print(set_a ^ set_b)

db = {"Faizan", "John", "Ali"}
api = {"Ali", "John", "Alex"}
print(db ^ api)


# =============================================
# 5. PRACTICE PROBLEMS
# =============================================

print("\n== Practice ==")

# Unique elements
a = {1, 2, 3}
b = {3, 4, 5}
print(a ^ b)

# Unique characters
s1 = "abc"
s2 = "bcd"
print(set(s1) ^ set(s2))

# Compare Lists
l1 = [1, 2, 3]
l2 = [3, 4, 5]
print(set(l1) ^ set(l2))

# Alternative
result = (set(l1) - set(l2)) | (set(l2) - set(l1))
print(result)


# =============================================
# 6. ADVANCED (COUNTER)
# =============================================

from collections import Counter

print("\n== With Duplicates (Counter) ==")

a = [1, 2, 2, 3]
b = [2, 3, 4]

c1 = Counter(a)
c2 = Counter(b)

result = list((c1 - c2) + (c2 - c1))
print(result)