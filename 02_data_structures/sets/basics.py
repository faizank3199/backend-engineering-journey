""" 
=============================================
       Sets in python 
=============================================

Sets:
 A set is an unordered collection of unique elements
 
 Properties:
  - No duplicate allow
  - No Indexing 
  - Fast membership check
  - Mathmetical operations (union, intersections etc)

"""
print("\n== Set Example ==")
number = { 1, 2, 3, 4, 5}
print(number)

#====================================================
# 1. Creating set
#====================================================

# set of string

s1 = {"Apple", "Banana","Mango", "Orange"}

# set of integer 

s2 = { 1, 2, 3, 4, 5}

# set of mixed data

s3 = {"Welcome", "to", "simple learn", (1, 2, 3), 5, 6}

#--------------------------------------------------------
# Empty set

print("\n== Empty set example ==")
empty_set = set()
print(type(empty_set))

# a = {}   its a dictionary not a set

#----------------------------------------------------------

# from list to set 

nums = [1,2,2,3,3,4,5]
print("\n ==List to set ==")
unique_nums = set(nums)    # Automatically remove duplicate
print(unique_nums)

# from string

s = "Hello"

print("\n == String to set ==")
unique_chars = set(s)
print(unique_chars)

# from tuple to set

print("\n == tuple to set ==")
tup = (1, 2, 3, 4, 4, 5,5)
result = set(tup)
print(result)

#---------------------------------------
# only hashable element allowed 

# my_set = {[1, 2], [3, 4]}   # error

# becouse list are mutable

my_set = {(1, 2), (3, 4) }
print(my_set)

# tupple are allowed becouse they are immutable 

#=========================================================
# Methods in set
#=========================================================

# adding element ( add() )

print("\n == method add() example ==")
numbers = {1, 2, 3, 4}
numbers.add(5)
print(numbers)

numbers.add(2) # not duplicate allowed output will same

# adding multiple element ( update() )

a = {1, 2}
print("\n== Adding multiple element ==")
a.update([3, 4, 5, 6, 7])
print(a)

