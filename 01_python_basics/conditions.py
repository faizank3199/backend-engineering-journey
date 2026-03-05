"""
========================================================
Conditions in Python
========================================================

Topics Covered:
1. Basic if 
2. Logical Operators (and, or, not)
3. if / elif / else
4. Login system
5. Role-Based Access (example)
6. Nested Conditions
7. Boolean Conversion Input Version 
8. Ternary Operator
9. Match-Case (Python 3.10+)

Backend Relevance:
- Role checking
- Status handling
- API response decisions
- Validation logic

Author: Mohammad Faizan
Date: 24/02/2026
Python Version: 3.10+
========================================================
"""


# ======================================================
# 1. BASIC IF CONDITIONS
# ======================================================

def basic_if_examples():
    print("\n---- Basic if Example ----")

    age = 20
    if age >= 18:
        print("You are an adult")

    age = 15
    if age >= 18:
        print("You are an adult")  # Will not execute


# ======================================================
# 2. LOGICAL OPERATORS
# ======================================================

def logical_operator_examples():
    print("\n---- Logical Operators ----")

    # AND
    age = 20
    has_id = True
    if age >= 18 and has_id:
        print("Entry allowed")

    # OR
    is_admin = True
    is_editor = False
    if is_admin or is_editor:
        print("Access Granted")

    # NOT
    is_logged_in = False
    if not is_logged_in:
        print("Please login first")


# ======================================================
# 3. IF-ELIF-ELSE
# ======================================================

def temperature_example():
    print("\n---- if-elif-else Example ----")

    temperature = 45

    if temperature > 40:
        print("Very Hot")
    elif temperature > 30:
        print("Hot")
    else:
        print("Normal")


# ======================================================
# 4.  LOGIN SYSTEM (example)
# ======================================================

def login_system():
    print("\n---- Login System Example ----")

    stored_username = "faizan"
    stored_password = "1234"

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == stored_username and password == stored_password:
        print("Login Successful")
    else:
        print("Invalid Credentials")


# ======================================================
#  5. ROLE-BASED ACCESS (example)
# ======================================================

def role_based_access():
    print("\n---- Role-Based Access ----")

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


# ======================================================
# 6. NESTED CONDITIONS
# ======================================================

def nested_condition_example():
    print("\n---- Nested Condition Example ----")

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
            print("Please verify your email")
    else:
        print("Login Required")


# ======================================================
# 7. BOOLEAN CONVERSION INPUT VERSION
# ======================================================

def boolean_conversion_example():
    print("\n---- Boolean Conversion Version ----")

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


# ======================================================
# 8. TERNARY OPERATOR
# ======================================================

def check_even_odd(number: int) -> str:
    """
    One-line condition example.
    """
    return "Even" if number % 2 == 0 else "Odd"


# ======================================================
# 9. MATCH-CASE (Python 3.10+)
# ======================================================

def get_http_status_message(status_code: int) -> str:
    """
    Simulates API response handling.
    """
    match status_code:
        case 200:
            return "OK - Request successful"
        case 201:
            return "Created - Resource created"
        case 400:
            return "Bad Request"
        case 401:
            return "Unauthorized"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status Code"


# ======================================================
# MAIN FUNCTION
# ======================================================

def main():
    basic_if_examples()
    logical_operator_examples()
    temperature_example()
    role_based_access()
    nested_condition_example()

    # Commented to avoid blocking automation
    # login_system()
    # boolean_conversion_example()

    print("\nEven/Odd Check:", check_even_odd(7))
    print("HTTP Status:", get_http_status_message(404))


# ======================================================
# ENTRY POINT
# ======================================================

if __name__ == "__main__":
    main()