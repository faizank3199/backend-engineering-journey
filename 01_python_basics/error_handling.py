"""
=========================================
        ERROR HANDLING IN PYTHON
=========================================

Topics Covered:
- Types of errors
- try / except
- multiple except
- else
- finally
- raise
- custom exceptions

Author: Mohammad Faizan
Date : 03/04/2026
=========================================
"""

"""
==================================================
            ERROR HANDLING IN PYTHON
==================================================

Covers:
- Built-in exceptions
- try / except / else / finally
- Raising exceptions
- Custom exceptions
- Backend-style examples

Author: Mohammad Faizan
==================================================
"""

# ==========================================
# 1. BASIC TRY / EXCEPT
# ==========================================

def safe_division(a: float, b: float) -> float:
    """
    Safely divides two numbers.
    Raises ValueError if denominator is zero.
    """
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a / b


# ==========================================
# 2. CUSTOM EXCEPTIONS
# ==========================================

class InsufficientBalanceError(Exception):
    """Raised when withdrawal amount exceeds balance."""
    pass


class AuthenticationError(Exception):
    """Raised when login credentials are invalid."""
    pass


# ==========================================
# 3.ATM EXAMPLE (Backend Style)
# ==========================================

class BankAccount:
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        if amount > self.balance:
            raise InsufficientBalanceError(
                f"Insufficient funds. Available balance: {self.balance}"
            )

        self.balance -= amount
        return self.balance


# ==========================================
# 4. AUTHENTICATION EXAMPLE
# ==========================================

def login(username: str, password: str) -> str:
    """
    Simulates login validation.
    """

    if username != "admin":
        raise AuthenticationError("User not found.")

    if password != "1234":
        raise AuthenticationError("Invalid password.")

    return "Login successful."


# ==========================================
# 5. FILE HANDLING WITH FINALLY
# ==========================================

def read_file(filename: str) -> str:
    file = None
    try:
        file = open(filename, "r")
        return file.read()
    except FileNotFoundError:
        raise FileNotFoundError("The requested file does not exist.")
    finally:
        if file:
            file.close()


# ==========================================
# 6. TEST BLOCK
# ==========================================

if __name__ == "__main__":

    print("=== Safe Division ===")
    try:
        print(safe_division(10, 2))
        print(safe_division(10, 0))
    except ValueError as e:
        print("Error:", e)

    print("\n=== ATM Example ===")
    account = BankAccount("Faizan", 1000)

    try:
        print("Remaining balance:", account.withdraw(1500))
    except InsufficientBalanceError as e:
        print("Transaction Failed:", e)

    print("\n=== Login Example ===")
    try:
        print(login("admin", "1111"))
    except AuthenticationError as e:
        print("Login Failed:", e)