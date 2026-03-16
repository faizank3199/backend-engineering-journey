"""
================================================================
                     Tuples in python 
================================================================

A tuple is an ordered and immutable collection of mixed elements.

Topics Covered: 
1. Creating tuples
2. Accessing elements
3. Tuple slicing
4. Tuple immutability
5. Loop through tuple
6. Tuple methods
7. Tuple unpacking
8. Nested tuple
9. Nested loop

--------------------------------
Author: Mohammad Faizan
Date: 16/03/2026

"""

#=================================================================
# 1. Creating  Tuple
#=================================================================

t1 = (1,2,3,4,5)
t2 = ("Faizan", "Ashu","Sara")
t3 = ("John", 10, 3.23, True)

# Empty tupe
empty = ()

# single element tuple

t = (5,)    # without comma python thinks its a number 

#==================================================================
# 2. Accessing of element
#==================================================================

numbers = (10, 20, 30, 40)

print("\n==Accessing of element example")
print(numbers[0])  # 10
print(numbers[1])  # 20
print(numbers[2])  # 30

# Negative index


numbers = (10, 20, 30, 40)

print("\n==Accessing of element example(negative index)")
print(numbers[-1])
print(numbers[-2])


#========================================================
# 3. Tuple slicing
#========================================================
"""
Accessing a specific part of the tuple  
"""
#---------------------------------------------------------
nums = (10, 20, 30, 40, 50, 60)

# [star : end : step]
print("\n==Slicing Example==")
print(nums[0:]) # 10,20, 30, 40, 50, 60
print(nums[2:])  # 30, 40, 50 ,60
print(nums[0:3])   # 10, 20, 30
print(nums[2:5])  # 30, 40, 50
print(nums[0:6:2]) # 10, 30, 50

#---------------------------------------------------------

nums = (10, 20, 30, 40, 50, 60)


print("\n==Negative slicing Example==")
print(nums[::-1])  # reverse the tuple
print(nums[-2::])  # 50, 60
print(nums[-4:-6:-1])  # 30, 20
print(nums[-2:-6:-1])  # 50, 40, 30, 20
print(nums[-5:-1:])     # 20, 30, 40, 50
print(nums[-5::-1])     # 20, 10


#==================================================
# 4. Tuple immutability
#==================================================

"""
number = (10, 29, 39)

number[1] = 9  

TypeError: 
becouse Tuple are safe , for fixed data

 """
 

tup_1 = (1,2,3, [10,40])

print("\n==Tuple immutability Example==")
print(id(tup_1))

tup_1[3][0] = 30    # changing in list,  not in tuple 
                   
print(tup_1)
print(id(tup_1))

"""
A tuple is immutable, but it can contain mutable objects like lists.
"""
#------------------------------------------------------------------

config = ("localhost", 5432, ["read", "write"])

config[2].append("delete")

print(config)

#=========================================
# 5. Looping on tuple 
#=========================================

tup = (1,2,3,4,5,6)

print("\n==tuple looping example==")
for i in tup:
    print(i)

#------------------------------------


fruits = ("Apple","Mango","Banana")

print("\n=========")
for fruit in fruits:
    print(fruit)
    

nums = (10, 20, 30, 40)

print("\n==loop using range example==")
for i in range(len(nums)):
    print(f"{i}. {nums[i]}")
    
#--------------------------------------

    
# enumerate()

nums = (12, 45, 56, 34, 23)

print("\n==loop using enumerate example==")

for index,value in enumerate(nums):
    print(index,"-", value)
    
    

  
#-------------------------------------------  


# using while loop

tup2 = (10,20,30,40,50,60)

print("\n==while loop example==")
i = 0
while i < len(tup2):
    print(f"{i} - {tup2[i]}")
    i +=1
    

#========================================================
# 6. Tuple Method 
#========================================================

"""
count() :
 - count() method returns how many times a specific value appears in a tuple.
 - If value not present return 0
 
"""
numbers = (1,2,3,4,2,2,2,5,5)

print("\n== count method example==")
print("Count of 2: ",numbers.count(2))

# count string

name = ("Faizan","Sonu","Rohan","Rohan")

print("Count of Rohan:", name.count("Rohan"))  

#-------------------------------------------------------------

""" 
Index() Method :
 - Its return position of  index of the first occurence in the tupe
 - its return ValueError if index not found
 
"""
numbers = (10, 20, 30, 40, 50)
print("\n== Tuple index example==")
print("Index of the element: ", numbers.index(40))

roles = ("admin","user","editor")

print("Index of the admin: ",roles.index("editor"))

# len()
print("Length of roles: ",len(roles))

# max(),min()

print("Maximum number in the tuple: ",max(numbers))

print("Minimum number in the tuple: ",min(numbers))

#====================================================================
# 7. Tuple Unpacking
#====================================================================

num = (1,2,3)

a, b, c = num
print("\n== Tuple Basic Unpacking ==")
print("a -", a)
print("b -", b)
print("c -",c )

user = ("Faizan", 25, "Backend Developer")

name, age, role = user

print("Name: ", name)
print("Age: ",age)
print("role: ",role)
#-----------------------------------------------------------------------

print("\n==Tuple unpacking in loop==")

pairs = ((1,2),(3,4),(5,6))

for a, b in pairs:
    print(a, b)

#====================================================================
# 8. Nested tuple
#====================================================================
"""
Nested Tuple:
 - Nested tuple means tuple inside tuple. 
 
"""
print("\n==Nested Tuple example==")
data = ((1,2),(3,4),(5,6))
print(data)

print("\n== Accessing Element Example ==")
# Accessing Nested Tuple 

print(data[0])  # (1, 2)
print(data[1])  # (3, 4)
print(data[2])  # (5, 6)

# Accessing Inner Element

print("\n== Accessing Inner Element ==")
print(data[0][1])    # 2
print(data[1][0])    # 3
print(data[2][1])    # 6

#=====================================================================
# 9. Nested loop
#=====================================================================

""" 
A Nested loop is loop inside another loop
 
"""
pairs =  ((1,2),(3,4),(5,6))

print("\n== NEsted Loop Example ==")
for pair in pairs:
    for num in pair:
        print(num)