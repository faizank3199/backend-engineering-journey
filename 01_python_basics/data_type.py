#------------------------------------
# DATA TYPES IN THE PYTHON 
#----------------------------------
"""
Topics covered :
1. int 
2. float
3. str
4. bool
5. None
6. type() functions 
7. Mutable vs Immutable (foundation for backend)

Author: Faizan
Date: 2026-02-22
Usage: python data_types.py

"""
#---------------------------------------------
#  1. Integer (int)
#--------------------------------------------

age = 25
year = 2026
negative_num = -5 

print("\nInteger Examples :")
print(f" Age : {age}, type : {type(age)}")
print(f" Year : {year}, type : {type(year)}")
print(f" Negative Number : {negative_num}, type :{type(negative_num)}")


#---------------------------------------------------------------------------
# Arithmetic with integers

print(f"\nArithmatic with integer Examples: ")
print(f" Addition -> {age+5}")
print(f" Multiplications ->, {age * 2}")
print(f" Exponent -> {2 ** 2}")

# Try yourself:
# Multiply age by 3 and subtract 5. Print result.


#-------------------------------------------------------------------------
# 2. Float 
#-------------------------------------------------------------------------

height = 5.6
weight = 56.6

print(f"\nFloat Examples :")
print(f" Height ->  {height}, type : {type(height)}")
print(f" Weight -> {weight}, type  : {type(weight)}")

# ----------------------------------------------------------------------
# Arithmetic with float 
print(f"\nArithmetic with float Examples :")
print(F" Addition -> {height + 0.2}" )
print(f" Division -> {weight/2} ")

# Try yourself:
# Calculate BMI = weight / (height ** 2) and print the result.


#-----------------------------------------------------------------------
# 3. strings (str)
#-----------------------------------------------------------------------

name = "Faizan"
greeting = "hello " + name
multiline = """ This is the multi-line strings 
"""
print(f"\nString Example :")
print(f" Name : {name}, type : {type(name)} ")
print(f" Greeting  : {greeting}, type : {type(greeting)}")
print(f" Multiline : {multiline}, type : {type(multiline)}")

#-----------------------------------------------------------------------
# Common String Method

print("\nCommon String Method Examples")
print(f" Name : {name}, -> {name.lower()}")
print(f" Name : {name}, -> {name.upper()}")
print(f" Name : {name}, -> Length of name : {len(name)}")

# Try yourself:
# Create a string variable with your city name and print it reversed.
# hint (can use slicing or reverse())

#---------------------------------------------
# 4. Boolean (bool)
#----------------------------------------------

is_student = True 
has_job = False

print(f"\n Boolean Examples :")
print(f" Is_student -> {is_student}, type : {type(is_student)}")
print(f" has_job -> {has_job}, type : {type(has_job)}")

# ---------------------------
# Boolean Expressions
print(f"\nBoolean Expressions Examples")
print(" 5 > 3", 5 > 3)
print(" 5 == 3", 5 == 3)

# Try yourself:
# Check if 10 is less than 20 and store result in a variable. Print the variable.



# -----------------------------------
# 5️. NoneType
# -----------------------------------
nothing = None

print("\nNone Example:")
print(" nothing:", nothing, "type:", type(nothing))

# -----------------------------------
# 6️. type() function
# -----------------------------------
print("\nUsing type() function Examples:")
x = 10
print("x =", x, "type:", type(x))
x = 10.5
print("x =", x, "type:", type(x))
x = "Python"
print("x =", x, "type:", type(x))

# --------------------------------------------------------------------------------
# 7️. Mutable vs Immutable (Foundation for Backend)
# -------------------------------------------------------------------------------

# Immutable objects → cannot change after creation
# Examples: int, float, str, tuple, frozenset

print("\n----Immutable Examples----")

a = 10
print(f" a id before change  -> {id(a)}")
a = 20
print(f" a id after change -> {id(a)}")  # new object in the memory 

s = "Faizan"
print(f" s id before change -> {id(s)}")
s += " khan"

print(f" s id after change -> {id(s)}")  # new object in the memory 

# Tuple example
tup = (1, 2, 3)
print(f" Tuple: {tup}, id: {id(tup)}")
# Uncomment the line below to see immutability in action (will raise an error)
# tup[0] = 10

print(f" Tuple remains unchanged: {tup}, id: {id(tup)}")

# Try yourself:
# 1. Create a tuple with 3 numbers
# 2. Try to modify the first element
# 3. Observe the TypeError and note that the id doesn't change

#-------------------------------------------------------------------------------------
# Mutable objects → can change after creation
#-------------------------------------------------------------------------------------

# Examples: list, dict, set

print("\nMutable Examples:")
my_list = [1, 2, 3]
print("my_list id before -> ", id(my_list))
my_list.append(4)
print("my_list id after -> ", id(my_list))   # same object 

my_dict = {"name" : "Faizan"}
print("my_dict id before -> ", id(my_dict))

my_dict["age"]=25
print(" my_dict after adding age ->", my_dict)
print(" my_dict id after -> ", id(my_dict))     # same object 

# Try yourself:
# 1. Create a set of 3 colors
# 2. Add one more color
# 3. Print id before and after


#------------------------------------------------------------------------------------
#  Main Test 
#------------------------------------------------------------------------------------

if __name__ == "__main__":
    print("\ndata_type.py test completed successfully!")
    

    