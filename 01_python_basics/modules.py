"""
=========================================
            PYTHON MODULES
=========================================

Concepts Covered:
1. import
2. from ... import
3. aliasing
4. __name__ == "__main__"
5. creating custom modules

Author: Mohammad Faizan
Date : 05/03/2026
=========================================
"""

# ==========================================
# 1. IMPORT MODULE
# ==========================================

import math

def square_root_example():
    print("Square root of 25:", math.sqrt(25))


# ==========================================
# 2. FROM IMPORT
# ==========================================

from random import randint

def random_number():
    print("Random number between 1 and 10:", randint(1, 10))


# ==========================================
# 3. ALIASING
# ==========================================

import datetime as dt

def show_time():
    now = dt.datetime.now()
    print("Current time:", now)


# ==========================================
# 4. USING YOUR OWN MODULE
# ==========================================

"""
Create another file in the same folder:

utils.py
"""

# Example utils.py
"""
def greet(name):
    return f"Hello, {name}"
"""

# Then import it like this:
# import utils
# print(utils.greet("Faizan"))


# ==========================================
# 5. MAIN FUNCTION
# ==========================================

def main():
    square_root_example()
    random_number()
    show_time()


# ==========================================
# 6. MAIN GUARD
# ==========================================

if __name__ == "__main__":
    main()