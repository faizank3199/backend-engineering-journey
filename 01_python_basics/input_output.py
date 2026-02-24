#============================
# Input Output in python 
#============================

"""
-------------------------------------------------------
This module demonstrates Python input/output concepts:
1. Taking input from users
2. Using formatted strings (f-strings)
3. Escape sequences (\n, \t, \\, etc.)
4. Mini projects:
   - Age Calculator
   - Interest Calculator

Author: Faizan
Date : 24/02/2026
--------------------------------------------------------
"""

#====================================
# 1. Basics Input and  Output 
#====================================
print(" Welcome to Input/Output Demo!\n")

# input from the user 
name = input(" Enter your name: ")
print(f" hello {name}, welcome to Input/Output demo!\n")  # f-string usage

#=======================================
# 2. Escape Sequences Example  
#=======================================

print(" \nEscape sequence Example :")
print(" New line character -> \\n\n This is on a new line")
print(" Tab character -> \\t\t This is tabbed")
print(" Backslash ->  \\\\ This is backslash\n" )

#==========================================---
# 3. MINI Projects
#=============================================

#=============================================
#  3. (a) Age calculator (mini projects )
#==============================================

print("----Age Calculator----")

birth_year = int(input("Enter the birth year (yyyy) :"))
current_year = int(input(" Enter the current year (yyyy) :"))

# Calculate Age
age = current_year - birth_year

print(f"{name} you are {age} years old.\n") # f-string  to show result 

#====================================================
#  3. (b) Simple Interest Calculator (mini project)
#====================================================

print("-----Simple Interest Calculator-----")
principal = float(input("Enter the Principal amount (rs) :"))
rate = float(input(" Enter the annual interest rate in (%) :"))
time=float(input(" Enter the time period in years :"))

# Simple Interest Formula : P * R * T / 100
simple_interest = ( principal * rate * time ) / 100

print(f" The Simple Interest for {principal} at Rate {rate} for year {time} year is : rs{simple_interest}\n")

#=====================================================
#  3. (c) Compound Interest Calculator 
#=====================================================


print("----- Compound Interest Calculator -----")
principal = float(input(" Enter the principal amount (rs): "))
rate = float(input(" Enter the annual interest rate (in %): "))
time = float(input(" Enter the time period in years: "))
n = int(input(" Enter number of times interest applied per year: "))

# Compound Interest formula: A = P * (1 + R/(100*n))**(n*T)
amount = principal * (1 + rate / (100 * n))**(n * time)
compound_interest = amount - principal

print(f"The Compound Interest for ₹{principal} at {rate}% for {time} years compounded {n} times/year is: rs {compound_interest:.2f}\n")


# -----------------------------
# __main__ Guard
# -----------------------------
# This ensures the module can be imported without running the code immediately.

if __name__ == "__main__":
    print("Module executed directly. All demos above have been run.")