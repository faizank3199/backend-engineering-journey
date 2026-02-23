#=========================
# OPERATORS IN PYTHON 
#==========================
"""
--------------------------------------------------------------
This module demonstrates all major types of Python operators:

1. Arithmetic Operators
2. Comparison Operators
3. Logical Operators
4. Assignment Operators
5. Identity Operators
6. Membership Operators

Author: Mohammad Faizan
Date : 23/02/2026

"""

# ==============================
#  1. Arithmetic Operators
# ==============================

def arithmetic_operators():
    """
    Arithmetic operators are used to perform mathematical operations.
    """
    a = 10
    b = 3

    print("Arithmetic Operators")
    print("Addition:", a + b)        # 13
    print("Subtraction:", a - b)     # 7
    print("Multiplication:", a * b)  # 30
    print("Division:", a / b)        # 3.333...
    print("Floor Division:", a // b) # 3
    print("Modulus:", a % b)         # 1
    print("Exponent:", a ** b)       # 1000
    print("-" * 40)


# ==============================
#  2. Comparison Operators
# ==============================

def comparison_operators():
    """
    Comparison operators compare two values and return True or False.
    """
    x = 5
    y = 10

    print("Comparison Operators")
    print("Equal:", x == y)          # False
    print("Not Equal:", x != y)      # True
    print("Greater Than:", x > y)    # False
    print("Less Than:", x < y)       # True
    print("Greater or Equal:", x >= y)
    print("Less or Equal:", x <= y)
    print("-" * 40)


# ==============================
#  3. Logical Operators
# ==============================

def logical_operators():
    """
    Logical operators are used to combine conditional statements.
    """
    age = 20
    has_id = True

    print("Logical Operators")
    print("AND:", age >= 18 and has_id)  # True
    print("OR:", age < 18 or has_id)     # True
    print("NOT:", not has_id)            # False
    print("-" * 40)


# ==============================
#  4. Assignment Operators
# ==============================

def assignment_operators():
    """
    Assignment operators assign and modify values.
    """
    num = 5

    print("Assignment Operators")
    num += 2   # num = num + 2
    print("After += :", num)

    num -= 1   # num = num - 1
    print("After -= :", num)

    num *= 3   # num = num * 3
    print("After *= :", num)

    num //= 2  # num = num // 2
    print("After //= :", num)

    print("-" * 40)


# ==================================
#  5. Identity Operators
# ===================================

def identity_operators():
    """
    Identity operators compare memory locations.
    """
    a = [1, 2, 3]
    b = a
    c = [1, 2, 3]

    print("Identity Operators")
    print("a is b:", a is b)         # True (same object)
    print("a is c:", a is c)         # False (different objects)
    print("a is not c:", a is not c) # True
    print("-" * 40)


# ==============================
#  6. Membership Operators
# ==============================

def membership_operators():
    """
    Membership operators check if a value exists in a sequence.
    """
    numbers = [1, 2, 3, 4, 5]

    print("Membership Operators")
    print("3 in numbers:", 3 in numbers)       # True
    print("10 not in numbers:", 10 not in numbers) # True
    print("-" * 40)


# ====================================
# Main Execution Block
# =====================================

if __name__ == "__main__":
    """
    This block runs only when the file is executed directly.
    It does NOT run when imported as a module.
    """

    arithmetic_operators()
    comparison_operators()
    logical_operators()
    assignment_operators()
    identity_operators()
    membership_operators()