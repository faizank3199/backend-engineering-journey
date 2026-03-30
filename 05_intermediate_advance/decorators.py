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


# ============================================================
# 1. Basic Decorator
# ============================================================
def my_decorator(func):
    """Decorator to log function execution start and end."""

    @wraps(func)
    def wrapper():
        print("[INFO] Function started")
        result = func()
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
def add(a, b):
    """Returns sum of two numbers."""
    return a + b


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
    for _ in range(5):
        add(10, 20)