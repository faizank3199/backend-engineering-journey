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

----------------------------------------------
Author : Mohammad Faizan
Date   : 30/03/2026
----------------------------------------------
"""

from functools import wraps
from datetime import datetime
import time


# ============================================================
# 1. Basic Decorator
# ============================================================
def my_decorator(func):
    """Decorator to log function execution start and end."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("[INFO] Function started")
        result = func(*args, **kwargs)
        print("[INFO] Function ended")
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
def add_numbers(a, b):
    """Returns sum of two numbers."""
    return a + b


#===========================================================
#  5. Multiple Decorator 
#===========================================================

def logging(func):
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
@logging
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

def validate(expected_type):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, expected_type):
                    raise TypeError(f"[ERROR] Expected {expected_type.__name__}, got {type(arg).__name__} ")
                
            for key, value in kwargs.items():
                if not isinstance(value, expected_type):
                    raise TypeError(f"[ERROR] '{key}' must be {expected_type.__name__}), got {type(value).__name__}")
                
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
        
@logger
@validate(int)
@timer
def multiply_numbers(a, b):
    return a * b

        
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
        add_numbers(10, 20)
        
    print("\n--Multiple decorator--") 
    api()
    
    print("\n--logging + validations + time taken--")
    multiply_numbers(10, 30)

    