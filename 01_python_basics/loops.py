"""
#=========================================
   loops in python 
#=========================================


This module covers:
- for loops
- while loops
- break / continue
- backend-style examples
- pattern using while and for loop

Author: Mohammad Faizan
DAte : 26/02/2026
----------------------------------------
#================================================
# A loop is used to execute code multiple times.
#================================================

Python has:

 1. for loop
 2. while loop
 3. break
 4. continue
 5. pass
 6. Nested loops

"""



# ----------------------------------------
# 1. Basic For Loop
# ----------------------------------------
def basic_for_loop():
    print("Basic for loop:")
    for i in range(5):
        print(i)
    print("-" * 30)


# ----------------------------------------
# 2. While Loop
# ----------------------------------------
def basic_while_loop():
    print("Basic while loop:")
    count = 0
    while count < 3:
        print("Count:", count)
        count += 1
    print("-" * 30)


# ----------------------------------------
# 3. Break Example
# ----------------------------------------
def break_example():
    print("Break example:")
    for i in range(5):
        if i == 3:
            break
        print(i)
    print("-" * 30)


# ----------------------------------------
# 4. Continue Example
# ----------------------------------------
def continue_example():
    print("Continue example (print odd numbers only):")
    for i in range(6):
        if i % 2 == 0:
            continue
        print(i)
    print("-" * 30)


# ----------------------------------------
# 5. Nested Loop (Grid Example)
# ----------------------------------------
def nested_loop_example():
    print("Nested loop (grid):")
    for i in range(2):
        for j in range(3):
            print(f"({i},{j})", end=" ")
        print()
    print("-" * 30)


# ----------------------------------------
# 6. Backend Example – Order Processing
# ----------------------------------------
def backend_example():
    print("Backend-style example (Total Revenue Calculation):")
    
    orders = [
        {"id": 1, "amount": 500},
        {"id": 2, "amount": 1200},
        {"id": 3, "amount": 300}
    ]

    total = 0
    for order in orders:
        total += order["amount"]

    print("Total Revenue:", total)
    print("-" * 30)
    
#---------------------------------------------
# 7. pattern (using while loop)
#--------------------------------------------

#---------------------------------------------
# left aligned  right triangle
#-----------------------------------------------

def left_aligned_triangle(rows: int = 7) -> None:
    """
    Prints a left-aligned right triangle pattern.

    Args:
        rows (int): Number of rows in the triangle.
    """
    i = 1

    while i <= rows:
        j = 1
        while j<=rows:
            if j <= i:
                print("*", end=" ")
            else:
                print(" ", end = " ")
            j += 1

        print()  # Move to next line
        i += 1
        
#----------------------------------------------
#  right aligned triangle 
#----------------------------------------------

print("---right aligned triangle----")
def right_aligned_triangle(rows: int = 7) -> None:
    """
    Prints a right-aligned right triangle pattern.

    Args:
        rows (int): Number of rows in the triangle.
    """
    i = 1


    while i <= rows:
        j = 1
        while j<=rows:
            if j >= i:
                print("*", end=" ")
            else:
                print(" ", end = " ")
            j += 1

        print()  # Move to next line
        i += 1
        
#--------------------------------------------------
#   pyramid pattern
#---------------------------------------------------

def pyramid(rows: int=7)->None:
    """
    print a star centered pyramid pattern

    Args:
        rows (int): Number of the rows in the pyramid
    """
    i = 1
    total_columns = 2 * rows - 1   # dynamic column calculation

    while i <= rows:
        j = 1
        while j <= total_columns:
            if j >= rows - (i - 1) and j <= rows + (i - 1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
            j += 1
        print()
        i += 1
        
#---------------------------------------------------
#    N-pattern using while loop
#---------------------------------------------------

def n_star(rows: int = 7)-> None:
    """
    prints a N star pattern.
    
    args:
        rows (int): Number of rows in the triangle
    """
    i = 1
    while i <= rows:
        j = 1
        while j <= rows:
            if j == 1 or j == i or j == rows:
                print("*", end = " ")
            else:
                print(" ", end = " ")
            j += 1
        print()
        i += 1
        
#=====================================================
#      pattern using for loop
#======================================================

#-----------------------------------------------------
#   Z pattern using for loop
#-----------------------------------------------------

def z_pattern(rows: int=9)-> None:
    """
    prints a Z-star pattern 
    args:
        rows(int): Number of rows in the triangle
    """
    for i in range(1,rows+1):
        for j in range(1,rows+1):
            if i==1 or i== rows or j == rows + 1 - i:
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print()
        
#--------------------------------------------------------
# Number left aligned triangle
#-------------------------------------------------------
def number_left_aligned_triangle(rows: int = 9) -> None:
    """
    Prints a left-aligned number triangle where
    each row contains the row number repeated.

    Example (rows = 5):

    1
    2 2
    3 3 3
    4 4 4 4
    5 5 5 5 5
    """
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(i, end=" ")
        print()

        
#--------------------------------------------------------
#  Continous number left aligned triangle
#-------------------------------------------------------
def continuous_number_triangle(rows: int = 5) -> None:
    """
    Prints a left-aligned triangle with continuous numbers.

    Example (rows = 4):

    1
    2 3
    4 5 6
    7 8 9 10
    """
    num = 1

    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(num, end=" ")
            num += 1
        print()

# ----------------------------------------
# 7. Main Execution Block
# ----------------------------------------
if __name__ == "__main__":
    basic_for_loop()
    basic_while_loop()
    break_example()
    continue_example()
    nested_loop_example()
    backend_example()
    print("---left aligned triangle----")
    left_aligned_triangle()
    print("---right aligned triangle----")
    right_aligned_triangle()
    print("----Centered pyramid star pattern")
    pyramid()
    print("--- N-pattern using star---")
    n_star()
    print("----Z pattern Using for loop----")
    z_pattern()
    print("---number left aligned triangle---")
    number_left_aligned_triangle()
    print("---continuous number triangle---")
    continuous_number_triangle()