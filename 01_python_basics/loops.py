"""
#=========================================
   loops in python 
#=========================================


This module covers:
- for loops
- while loops
- break / continue
- backend-style examples

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