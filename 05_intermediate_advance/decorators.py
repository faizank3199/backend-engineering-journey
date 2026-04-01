"""
==============================================
           DECORATORS IN PYTHON
==============================================

A decorator in Python is a function that adds extra behavior to another
function without modifying its original code.

----------------------------------------------
Topics Covered:
----------------------------------------------
1. Basic Decorator
2. Decorator with Return Value
3. Decorator with Arguments (*args, **kwargs)
4. Function Call Counter using Decorator
5. Multiple Decorator
6. Logging + Validation + Timing Decorator
7. Tag Decorator 
8. RBAC Decorator
9. Retry Decorator

----------------------------------------------
Author : Mohammad Faizan
Date   : 01/04/2026
----------------------------------------------
"""

from functools import wraps
from datetime import datetime
from inspect import signature
import time
import random


# ============================================================
# 1. Basic Decorator
# ============================================================
def my_decorator(func):
    """Decorator to log function execution start and end."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[INFO] Function {func.__name__} started")
        result = func(*args, **kwargs)
        print(f"[INFO] Function {func.__name__} ended")
        return result

    return wrapper


@my_decorator
def greet():
    """Simple function to demonstrate decorator."""
    print("Hello")


# ============================================================
# 2. Decorator with Return Value
# ============================================================
def add_surname(func):
    """Decorator to modify return value by adding surname."""

    @wraps(func)
    def wrapper(name):
        result = func(name)
        return f"{result} Mansury"

    return wrapper


@add_surname
def say_hello(name):
    """Returns the given name."""
    return name


# ============================================================
# 3. Decorator with Arguments (*args, **kwargs)
# ============================================================
def double_result(func):
    """Decorator to double the result of a function."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2

    return wrapper


@double_result
def get_number():
    """Returns a number."""
    return 10


# ============================================================
# 4. Function Call Counter
# ============================================================
def function_counter(func):
    """Decorator to count how many times a function is called."""

    count = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"[INFO] Function '{func.__name__}' called {count} times")
        return func(*args, **kwargs)

    return wrapper


@function_counter
def multiply_numbers(a, b):
    """Returns product of two numbers."""
    return a * b


#===========================================================
#  5. Multiple Decorator 
#===========================================================

def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Logging")
        return func(*args, **kwargs)
    return wrapper

def auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Checking Auth")
        return func(*args, **kwargs)
    return wrapper

@auth
@log_decorator
def api():
    print("Api is running")


#===========================================================
# 6. Logging + Validations + time taken
#==========================================================

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"[INFO] [{timestamp}] Calling {func.__name__} | args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"[INFO] [{end_time}] Function {func.__name__} finished | Result: {result}")
        return result 
    return wrapper


def validate(**type_hints):
    def decorator(func):
        sig = signature(func)

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound = sig.bind(*args, **kwargs)
            bound.apply_defaults()

            for key, expected_type in type_hints.items():
                if key in bound.arguments:
                    value = bound.arguments[key]
                    if not isinstance(value, expected_type):
                        raise TypeError(
                            f"[ERROR] '{key}' must be {expected_type.__name__}, got {type(value).__name__}"
                        )

            return func(*args, **kwargs)
        
        return wrapper
    return decorator

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIMER] Function {func.__name__} took {end - start:.4f} seconds")
        return result 
    return wrapper
        
@timer
@logger
@validate(a=int, b=int)
def add_numbers(a, b):
    return a + b

#================================================================
# 7. Tag Decorator
#================================================================

def format_txt(tag):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"<{tag}> {result} </{tag}>"
        return wrapper
    return decorator

@format_txt("h1")
def get_heading():
    return "Python Backend"

@format_txt("i")
def get_name():
    return "ashu@123"

#===============================================================
# 8. RBAC Decorator 
#===============================================================
def required_role(*allowed_roles):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            
            user = kwargs.get("user")  # 🔥 get from kwargs
            
            if not user:
                raise ValueError("User not provided")

            user_role = user.get("role")
            if not user_role:
                raise ValueError("User role missing")

            if user_role not in allowed_roles:
                raise PermissionError(
                    f"Access Denied: Required {allowed_roles}, got {user_role}"
                )

            return func(*args, **kwargs)

        return wrapper
    return decorator
@required_role("admin", "manager")
def delete_user(*,user):
    return "User Deleted"

#==============================================================
# 9. Retry Decorator
#==============================================================

def retry(attempts, delay, backoff, exceptions = (ValueError,)):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(1, attempts + 1):
                
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    print(f"[ERROR] Attempt {attempt} failed {e} ")
                    if attempt == attempts:
                        raise
                    jitter = random.uniform(0, 1)
                    sleep_time = current_delay + jitter

                    print(f"[INFO] Retrying in {sleep_time:.2f}s")
                    time.sleep(sleep_time)

                    current_delay *= backoff
        return wrapper
    return decorator 

@retry(attempts = 5, delay = 1,  backoff = 2, exceptions = (ValueError,) )
def api_fetching():
    import random
    if random.random() < 0.8:
        raise ValueError("api failed")
    return "data received"

# ============================================================
# Main Execution (Best Practice)
# ============================================================
if __name__ == "__main__":

    print("\n--- 1. Simple Decorator ---")
    greet()

    print("\n--- 2. Decorator with Return Value ---")
    print(say_hello("Faizan"))

    print("\n--- 3. Double Result Decorator ---")
    print(get_number())

    print("\n--- 4. Function Call Counter ---")
    for _ in range(3):
        multiply_numbers(10, 20)
        
        
    print("\n--- 5. Multiple decorator ---") 
    api()
    
    print("\n--- 6. logging + validations + time taken ---")
    add_numbers(10, 30)

    print("\n--- 7. Tag Decorator ---")
    print(get_name())
    print(get_heading())
    
    print("\n--- 8. RBAC Decorator ---")
    admin = {"name": "faizan", "role":"admin"}
    guest = {"name": "Mansury", "role":"guest"}

    print(delete_user(user=admin))
    #print(delete_user(user=guest))
    
    print("\n--- 9. Retry Decorator ---")
    print(api_fetching())