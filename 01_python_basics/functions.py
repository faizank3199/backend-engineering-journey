"""
------------------------------------------------
functions
------------------------------------------------
Author: Mohammad Faizan
Date: 28/02/2026

Description:
This module demonstrates core Python function concepts
required for backend development.

Topics Covered:
- Parameters
- Return values
- Default arguments
- Keyword arguments
- *args
- **kwargs
- Recursion
- Practical backend-style examples
"""

# ======================================================
# Basic Function
# ======================================================

def greet() -> None:
    """Prints a simple greeting message."""
    print("Hello Faizan")


# ======================================================
# Return Example
# ======================================================

def add_numbers(a: int, b: int) -> int:
    """
    Adds two integers and returns the result.

    :param a: First integer
    :param b: Second integer
    :return: Sum of a and b
    """
    return a + b


# ======================================================
# Default Arguments
# ======================================================

def greet_user(name: str = "Guest") -> str:
    """
    Returns a greeting message.

    :param name: Optional username
    :return: Greeting string
    """
    return f"Hello {name}"


# ======================================================
# Keyword Arguments
# ======================================================

def user_info(name: str, age: int, course: str) -> str:
    """
    Returns formatted user information.
    """
    return f"Name: {name}, Age: {age}, Course: {course}"


# ======================================================
# *args Example
# ======================================================

def total_sum(*numbers: int) -> int:
    """
    Returns the sum of unlimited numbers.
    """
    return sum(numbers)


def average(*numbers: int) -> float:
    """
    Calculates the average of unlimited numbers.
    """
    if not numbers:
        raise ValueError("At least one number must be provided.")

    return sum(numbers) / len(numbers)


# ======================================================
# **kwargs Example
# ======================================================

def create_user(**kwargs) -> dict:
    """
    Simulates dynamic user creation using keyword arguments.
    """
    return kwargs


# ======================================================
# Recursion Examples
# ======================================================

def countdown(n: int) -> None:
    """
    Recursively prints numbers from n to 1.
    """
    if n <= 0:
        return

    print(n)
    countdown(n - 1)


def factorial(n: int) -> int:
    """
    Calculates factorial using recursion.

    :param n: Non-negative integer
    :return: Factorial of n
    """
    if n <= 1:
        return 1

    return n * factorial(n - 1)


def fibonacci(n: int) -> int:
    """
    Returns nth Fibonacci number (recursive version).
    Warning: Inefficient for large n.
    """
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


def sum_of_digits(n: int) -> int:
    """
    Returns sum of digits using recursion.
    """
    if n == 0:
        return 0

    return n % 10 + sum_of_digits(n // 10)


# ======================================================
# Backend-Style Example: Login System
# ======================================================

def login(username: str, password: str) -> str:
    """
    Simulates a simple login system.
    """
    users = {
        "admin": "1234",
        "faizan": "python123"
    }

    if username not in users:
        return "User not found"

    if users[username] != password:
        return "Wrong password"

    return "Login successful"


# ======================================================
# Main Execution Guard
# ======================================================

if __name__ == "__main__":
    print("Running function demonstrations...\n")

    greet()
    print(add_numbers(5, 3))
    print(greet_user())
    print(user_info(name="Faizan", age=23, course="Python"))

    print("Total:", total_sum(1, 2, 3, 4))
    print("Average:", average(10, 20, 30))

    print("Factorial of 5:", factorial(5))
    print("Fibonacci(6):", fibonacci(6))
    print("Sum of digits (1234):", sum_of_digits(1234))

    print(login("faizan", "python123"))