""" 
=============================================
         Advanced Sets
=============================================

Topic covered:
  1. Set Comprehensions
  2. Frozen set (Immutable)
  3. Set Operations
  4. Problems
  5. Subset & Superset
  6. Disjoint
  
  
Author : Mohammad Faizan
Date : 20/03/2026

"""
#==========================================
#  1. Sets Comprehensions
#==========================================

nums =  [1,2,3,4,5,6]
print("\n == set comprehensions example ==")
print("== Square the each element ==")
squares = { x * x for x in nums}
print(squares)

# remove duplicates

numbers = [1,2,2,3,3,4,5,6]
print(" == Remove Duplicate ==")
unique_nums = {x for x in nums}
print(unique_nums)

# with strings

s = "backenddeveloper"
print("== Unique Characters ==")
unique_chrs = {ch for ch in s}
print(unique_chrs)



# set comprehensions with conditions
#----------------------------------------

# Even with range 
evens = { x for x in range(10) if x % 2 == 0}

print("== Even with range ==")
print(evens)

# Square only even numbers

nums = [1,2,3,4,5,6,7,8,9,10,11,12]
print("== squares only even ==")
even_squares = {x*x for x in nums if x % 2 == 0}
print(even_squares)


# Filter how many users active

users  = [
    {"name":"Faizan", "Active": True},
    {"name":"Rohan", "Active":False},
    {"name":"John", "Active":True}
]
print("== Filter Active Users ==")
active_users = {user["name"] for user in  users if user["Active"]}
print(active_users)

# unique vowels 
s  = "programming"
print("== Unique Vowels ==")
unique_vowels = { ch for ch in s if ch in "aeiou"}
print(unique_vowels)
 
# Filter numbers > 10

nums = [5, 2, 7, 10, 15, 20, 30, 40]

greater_10 = {x for x in nums if x > 10}
print(greater_10)

#=======================================
#  2.  Frozen Set (immutable)
#=======================================

""" 
A frozen set is -
 - Immutable (can not change)
 - Hashable (can be used as dictionary key)
 
"""

nums  = [1, 2, 3, 4, 5]
print("\n== Frozen set Example ==")
fs  = frozenset(nums)
print(fs) 

#---------------------------------------------

# Ex. use as dictionary

data = {
    frozenset([1, 2]) : "Group A",
    frozenset([3, 4]) : "Group B"
}
print(data)

# use case
print("== Dictionary Use Case ==")
user_roles = {
    frozenset(["read", "write"]):"Editor",
    frozenset(["read"]):"viewer"
}
current_user = frozenset(["read", "write"])
print(user_roles[current_user])

#================================================
#  3. Set Operations 
#================================================

a = frozenset([1,2,3])
b = frozenset([3,4,5])
print("\n== frozenset union example ==")
print(a|b)
print("== frozenset intersections example ==")
print(a&b)
print("== frozenset difference example ==")
print(a-b)

#================================================
# 4. Problems 
#================================================

arr = [[1, 2], [2, 1], [1, 2]]
print("== frozenset comprehensions example ==")
unique = {frozenset(x) for x in arr}
print(unique)

# Remove duplicate from group

group = [
    ["a", "b"],
    ["b", "a"],
    ["c", "a"],
    ["c", "d"]
]
print("== grouping problem ==")
unique_ch = {frozenset(ch) for ch in group}
print(unique_ch)

# Graph edge duplications

edges = [(1, 2), (2, 1), (3, 4)]
print("graph edges duplications")
unique_edges = {frozenset(edge) for edge in edges}
print(unique_edges)


#===================================================
# 5. Subset & Superset
#===================================================

"""
Subset : 
 - All element of A are present in B.
  
"""

a = {1, 2}
b = {1, 2, 3, }
print("\n== Subset Example ==")
print(a.issubset(b))
print("== Subset (Alternate method) ==")
print(a < b)

# proper subset
print("== proper subset example ==")
c = {1, 2}
d = {1, 2, 3}
print( c < d)

#--------------------------------------------------------
# Superset
#---------------------------------------------------------

"""
Superset:
 - B contains all element of A 
 
"""

set_a = {1, 2}
set_b = {1, 2, 3, 4}
print("\n== Superset Example ==")
print(set_b.issuperset(set_a))
# Alternate Method 
print("Alternate method")
print(b >= a)

# Proper superset
set_b = {1, 2, 3, 4}
set_a = {1, 2}
print("== proper superset ==")
print(b > a)

# check permission

user_perm = {"read", "write"}
required = {"read"}
print("== check permission ==")
print(required.issubset(user_perm))

# which is superset of a

a1 = {1, 2}
b1 = {1, 2, 3}
c1 = {1, 2, 3, 4}
print("== Check which is superset of a ? ==")
print(b.issuperset(a))
print(c.issuperset(a))

#========================================================
#  6. Disjoint Set
#========================================================

""" 
disjoint:
 - Two set are disjoint if, they have no comman elements
"""

a = {1, 2}
b = {3, 4}
print("\n==disjoint example ==")
print(a.isdisjoint(b))

# permission conflict check

user_roles = {"admin", "editor"}
restricted = {"baned", "blocked"}
print("== disjoint permission conflict check ==")
print(user_roles.isdisjoint(restricted))


 
