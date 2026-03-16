""" 
================================================
           Advanced Tuples in Python
================================================

Concepts Covered
----------------
1. Tuple unpacking
2. Star unpacking
3. Nested tuples
4. Loop unpacking
5. Tuple as dictionary key
6. Functions returning tuples
7. Swapping variables

Author: Mohammad Faizan
Date  : 16/03/2026
"""

print("\n==Tuple unpacking example==")

point = (10, 20)

x, y = point

print("x: ", x)
print("y: ", y)


#---------------------------------------------------


person = ("Faizan", 25, "Python Developer")
print("\n==Person Tuple Unpacking==")

name, age, job = person

print("Name: ",name)
print("Age: ",age)
print("Job: ", job)

#---------------------------------------------------

print("\n===========")
numbers = (1,2,3,4,5,6)

first, second, *rest = numbers

print("First: ", first)
print("Second: ", second)
print("Rest: ", rest)

#----------------------------------------------------

nums = (10,20,30,40,50,60,70)

print("\n== tuple  unpacking first, *middle, and last ==")

first, *middle, last = nums

print("First: ",first)
print("Middle: ",middle)
print("Last: ", last)


#---------------------------------------------------------

# Loop tuple unpacking

pairs = ((1,2), (3,4), (5,6))

print("\n==unpacking tuple using loop==")
for pair in pairs:
    print(pair[0], pair[1])

# -------------or pythonic way ------------------

print("\n == pythonic way == ")
for a,b in pairs:
    print(a, b)    
    
#----------------------------------------------------

students  = [
    ("faizan", 90),
    ("Sohan", 86),
    ("Sapna",97)
]

print("\n== unpack student data example ==")
for name, marks in students:
    print(name, marks)
    
    
#----------------------------------------------------------
# Ignore unwanted values using _

emp = ("Faizan", 25, "python backend")


name, _, job = emp

print("\n Ignore unwanted values using _")
print("name: ",name)
print("job: ",job)


#=======================================================
# Nested Tuple 
#======================================================

data = (
    (10, 20),
    (30, 40),
    (50, 60)
)

print("\n==Nested Tuple Example==")
print(data[0][1]) # 20
print(data[1][1]) # 40
print(data[2][1]) # 60

#---------------------------------------------------------
# using loop

print("\n== Nested Loop Example == ")
for pair in data:
    for val in pair:
        print(val)


# --------------------------------------------------------

# add total marks of students
students =  (
    ("Ali", 85),
    ("Sana", 98),
    ("John", 87)
    
)

total = 0
print("\n==Total marks of students==")
for name, marks in students:
    total += marks
    
print(total)

#========================================================================
#    Tuple as dictionary key
#=======================================================================

scores = {
    ("Ali", "Math"): 90,
    ("Ali", "Physics"): 85,
    ("Sara", "Math"): 95
}

print("\n ==tuple as dictionary example==")

print("Physics: ",scores[("Ali", "Physics")])


locations = {
    (28.61, 77.20): "Delhi",
    (19.07, 72.87): "Mumbai"
}
print("\n == tuple as dictionary example == ")
for coord, city in locations.items():
    print(f"{coord} -> {city}")


#================================================
# Returning Multiple Values From Function
#====================================================

"""
Python functions often return tuples automatically.
"""
#------------------------------------------------------------
    
def get_user():
   
    
    return "Faizan", 25

name, age = get_user()

print("Name: ",name)
print("Age: ",age)

print(type(get_user()))

#---------------------------------------------------------------

def calculate(a,b):
    add  = a + b
    sub = a - b
    return add, sub

add_result, sub_result = calculate(50,20)

print("Add: ", add_result)
print("sub: ", sub_result)

#------------------------------------------------------------------

def login():
    status = True
    message = "Login Successful"
    
    return status, message

status, message = login()

print("Status: ",status)
print("Message: ",message)


#-----------------------------------------------------------------

print("\n======")

def divide(a, b):
    
    if b == 0:
        return False, "Can not divide by zero"
    return True , a/b 

success, result = divide(50,2)

if success:
    print("Result:", result)
else:
    print("Error: ", result)
    
#---------------------------------------------------
# igonre value (-)

def get_coordinates():
    return 10, 20

x, _ = get_coordinates()
print("\nignore unwanted value using _")
print("x: ",x)

#----------------------------------------------------
# find min, max in the tuple

def find_min_max(nums):
    
    return min(nums), max(nums)

nums = [3, 7, 11, 1, 10]

minimum , maximum = find_min_max(nums)

print("Minimum Number: ", minimum)
print("Maximum Number: ", maximum)





#=====================================================
# Swapping variable 
#====================================================

print("\n==variable swapping example==")
a = 10
b = 20

print("\n==before Swapping==")
print("a: ",a)
print("b: ",b)
a, b = b, a

print("\n==After swapping==")

print("a: ", a)
print("b: ",b)

#============================================================
if __name__ == "__main__":
    print("\nAdvanced tuple module executed successfully.")