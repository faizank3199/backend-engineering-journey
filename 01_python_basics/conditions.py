#===================================
# Conditions in python 
#===================================

"""
----------------------------------
 Topics Covered:
1. if / elif / else
2. Nested conditions
3. Ternary operator
4. match-case (Python 3.10+)

Backend Relevance:
- Role checking
- Status handling
- API response decisions
- Validation logic

Author: Mohammad Faizan
Date : 24/02/2026
----------------------------------
"""

#====================================================
# Conditions allow your program to make decisions.
# A condition checks:
#         Is something TRUE or FALSE?

#  Real life examples:
#  If age ≥ 18 → allow voting
#  If password correct → login
#=====================================================

#--------------------------------
#  Python Uses: 
#--------------------------------
#  1. if
#  2. elif 
#  3. else
#--------------------------------

#=================================
# 1. if 
#=================================

# Basics Syntax :
# if condition:
    # code runs if condition is True
     

print("----if condition example----")

age = 20

if age >= 18:                  # conditions True so print runs 
    print("You are an adult")
 
# what if conditions is false 
age = 15

if age >= 18:                  # conditions False so nothing print 
    print("You are an adult")
  
 #-----------------------------------   
 #  if (with Boolean Values)
 #--------------------------------
 
is_logged_in = True 
if is_logged_in:
    print(" welcome user ")
    
is_logged_in = False     # nothing print 

#---------=---------------------------
# if (with operator)
#-------------------------------------
number = 10

if number == 10:
    print("Number is 10")
    
# ------------------------------------
# Api example 
#------------------------------------
status_code  = 200
if status_code == 200:
    print(" request successful ")
    
temprature = 55
if temprature > 30:
    print("Hot Weather")
    
    
print("----if else conditions examples-----")

#=================================
# if (with and Operator)
#==================================

# both conditions needs to be True 

age = 20
has_id = True 

if age >= 18 and has_id:    # condition True ,has_id = True , True and True is True 
    print("Entry allowed ")
    

age = 20
has_id = False

if age >= 18 and has_id:    # condition True has_id = False , True and False
    print("Entry allowed ")
    
#=========================================
# if ( with or Operator)
#==========================================

# only ONE condition needs to be True

is_admin = True
is_editor = False

if is_admin or is_editor:
    print("Access Granted")
    
    
#==========================================
#  if (with not Operator)
#==========================================

is_logged_in=False

if not is_logged_in:                  # not False -> True
    print(" Please login first ")


#=========================================    
#  2. elif and else
#==========================================

# Basics Syntax :
# if condition:
    # code runs if condition is False
    
# else:
     # code run if condition is True  
     
temprature = 30

if temprature > 30:
    print("Hot Weather")
    
else:
    print("Normal Wearher")
     

temprature = 45

if temprature > 40:
    print("Very hot")
    
elif temprature > 30:
    print("hot")
    
else:
    print("normal")
    

#-------------------------------
# Login system examples 
#--------------------------------
print("----Login system example----")
stored_username = "faizan"
stored_password = "1234"

user_name = input("enter the user name:")
password = input("enter the password:")

if stored_password == password and stored_username == user_name:
    print("Login Successfull")
else:
    print("Invalid Credentials")
    
#-----------------------------------------

role = "editor"

if role == "editor" or role == "admin":
    print("You can edit the content")
    
else:
    print("Read only access")    


#------------------------------------------

is_logged_in  = True
is_admin = False
is_varified = True 

if is_logged_in and (is_admin or is_varified):
    print("Access to dashboard")
    
else:
    print("Access denied")
    
    
#----------------------------------------------
age = 22
has_license = True 

if age >= 18 and has_license:
    print("You can access the system")
else:
    print("Access denied to system")
    
    
#---------------------------------------------   
age >= 18
has_license = True
is_verified = True

if age >=18 and has_license and is_verified:
    print("You can access the sytem")
    
else:
    print("Access denied to the system")
    
    
# =========================================
# Role Based Access System (mini exercise)
#==========================================

is_logged_in = True
role = "admin"

if not is_logged_in:
    print("Please login first")

elif role == "admin":
    print("Full Access")

elif role == "editor":
    print("Edit Access")

elif role == "viewer":
    print("Limited Access")

else:
    print("Invalid Role")
    

#==========================================
# 2.  Nested Conditions
#==========================================

# An if inside another if

# syntax 
#        if condition1:
#             if condition2:
#                       code

#--------------------------------------------

print("----simple nested example----")

is_logged_in = True
is_email_verified = True
role = "admin"

if is_logged_in:
    if is_email_verified:
        if role == "admin":
            print("Wekcome to admin dashboard")
        else:
            print("Access denied : you are  not admin ")
            
    else:
        print("Please verified your email")
        
else:
    print("Please login first")
    
#---------------------------------------------
print("----simple nested example 2----")

is_logged_in = True
is_email_verified = True
role = "editor"

if is_logged_in:
    if is_email_verified:
        if role == "admin":
            print("Welcome to Admin Dashboard")
        elif role == "editor":
            print("Editor Panel")
        else:
            print("Limited Access")
    else:
        print("Please verify email")
else:
    print("Login Required")

#-------------------------------------------------
print("---Input-Based Nested Example---")

is_logged_in = input("Are you logged in (yes/no): ").lower()
is_email_verified = input("Is your email verified (yes/no): ").lower()
role = input("Enter your role (admin/editor/viewer): ").lower()

if is_logged_in == "yes":
    if is_email_verified == "yes":
        if role == "admin":
            print("Welcome to Admin Dashboard")
        elif role == "editor":
            print("Editor Panel Access")
        elif role == "viewer":
            print("Limited Access")
        else:
            print("Invalid Role")
    else:
        print("Please verify your email")
else:
    print("Login Required")
    
#--------------------------------------------------------
#   Convert "yes/no" to Boolean
#--------------------------------------------------------
print("----yes no to Boolean----")

# Convert directly to Boolean
is_logged_in = input("Are you logged in (yes/no): ").lower() == "yes"
is_email_verified = input("Is your email verified (yes/no): ").lower() == "yes"
role = input("Enter your role (admin/editor/viewer): ").lower()


if not is_logged_in:
    print("Login Required")

elif not is_email_verified:
    print("Please verify your email")

elif role == "admin":
    print("Welcome to Admin Dashboard")

elif role == "editor":
    print("Editor Panel Access")

elif role == "viewer":
    print("Limited Access")

else:
    print("Invalid Role")