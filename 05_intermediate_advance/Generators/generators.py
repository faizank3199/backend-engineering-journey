
"""
=========================================
          PYTHON GENERATORS
=========================================

A generator is a special function that:

 - Pauses execution using yield
 - Remembers its state
 - Resumes where it left off
 - Produces values lazily (on demand)

-----------------------------------------
Topics Covered
-----------------------------------------
1. Basic Generator
2. Generator Exhaustion
3. next() vs for loop
4. State Persistence
5. yield vs return
6. send() Method
7. Infinite Generator
8. Generator Calculator
9. Yield from
10. Generator Expression
11. File Streaming Generator
12. Generator Pipeline
13. Multi-Service Log Aggregator

Author: Mohammad Faizan
=========================================
"""

import sys


# =========================================
# 1. Basic Generator
# =========================================

def basic_generator():
    """Basic generator example."""

    print("A")
    yield 1

    print("B")
    yield 2

    print("C")
    yield 3


# =========================================
# 2. Generator Exhaustion
# =========================================

def simple_generator():
    """A generator can only be consumed once."""

    yield 1
    yield 2


# =========================================
# 3. next() vs for loop
# =========================================

def numbers():
    """Generate numbers from 1 to 4."""

    yield 1
    yield 2
    yield 3
    yield 4


# =========================================
# 4. State Persistence
# =========================================

def counter():
    """Generators remember state."""

    i = 0

    while i < 3:
        yield i
        i += 1


# =========================================
# 5. yield vs return
# =========================================

def yield_vs_return():
    """Demonstrates yield and return."""

    yield 1
    return 2


# =========================================
# 6. send() Method
# =========================================

def smart_generator():
    """Receive values using send()."""

    value = yield 10
    print("Received:", value)

    value = yield 20
    print("Received:", value)

    yield 30


# =========================================
# 7. Infinite Generator
# =========================================

def infinite_counter():
    """Infinite generator."""

    i = 0

    while True:
        yield i
        i += 1


# =========================================
# 8. Generator Calculator
# =========================================

def calculator():
    """Interactive generator calculator."""

    print("Send me a number")

    num = yield 10
    print("Received:", num)

    result = num + 2
    print("Result:", result)

    num2 = yield result
    print("Received:", num2)

    final = result + num2
    print("Final Result:", final)


# =========================================
# 9. Yield From Example
# =========================================

def frontend_logs():
    yield "Frontend Error"


def backend_logs():
    yield "Backend Error"


def system_logs():
    """Combine generators using yield from."""

    yield from frontend_logs()
    yield from backend_logs()


# =========================================
# Even & Odd Generator
# =========================================

def even_generator(nums):

    for num in nums:
        if num % 2 == 0:
            yield num


def odd_generator(nums):

    for num in nums:
        if num % 2 != 0:
            yield num


def all_numbers():

    numbers_range = range(1, 10)

    print("Even Numbers")
    yield from even_generator(numbers_range)

    print("Odd Numbers")
    yield from odd_generator(numbers_range)


# =========================================
# 10. Generator Expression
# =========================================

def generator_expression_demo():

    return (x * x for x in range(5))


# =========================================
# 11. File Streaming Generator
# =========================================

def read_file(filename):
    """
    Read large files lazily.
    """

    with open(filename, "r") as file:
        for line in file:
            yield line.strip()


# =========================================
# 12. Generator Pipeline
# =========================================

def pipeline_numbers():

    for i in range(10):
        yield i


def even_filter(nums):

    for num in nums:
        if num % 2 == 0:
            yield num


def square_filter(nums):

    for num in nums:
        yield num * num


# =========================================
# 13. Multi-Service Log Aggregator
# =========================================

def auth_logs():

    yield "AUTH : User Login"
    yield "AUTH : Invalid Password"


def database_logs():

    yield "DB : Connection Success"
    yield "DB : Query Failed"


def payment_logs():

    yield "PAYMENT : Payment Success"
    yield "PAYMENT : Payment Failed"


def service_logs():
    """Aggregate logs from multiple services."""

    yield from auth_logs()
    yield from database_logs()
    yield from payment_logs()


# =========================================
# Main Program
# =========================================

if __name__ == "__main__":

    print("\n=== Basic Generator ===")

    gen = basic_generator()

    print(next(gen))
    print(next(gen))
    print(next(gen))

    print("\n=== Generator Exhaustion ===")

    gen = simple_generator()

    print(list(gen))
    print(list(gen))

    print("\n=== next() vs for loop ===")

    for value in numbers():
        print(value)

    print("\n=== State Persistence ===")

    for value in counter():
        print(value)

    print("\n=== StopIteration Example ===")

    gen = counter()

    try:
        while True:
            print(next(gen))
    except StopIteration:
        print("Generator exhausted")

    print("\n=== yield vs return ===")

    gen = yield_vs_return()

    try:
        while True:
            print(next(gen))
    except StopIteration as e:
        print("Returned:", e.value)

    print("\n=== send() Method ===")

    smart = smart_generator()

    print(next(smart))
    print(smart.send(200))
    print(smart.send(400))

    print("\n=== Infinite Generator ===")

    infinite = infinite_counter()

    for value in infinite:
        print(value)

        if value == 3:
            break

    print("\n=== Generator Calculator ===")

    calc = calculator()

    print(next(calc))
    print(calc.send(100))

    try:
        calc.send(200)
    except StopIteration:
        pass

    print("\n=== Yield From Example ===")

    for log in system_logs():
        print(log)

    print("\n=== Even & Odd Generator ===")

    for number in all_numbers():
        print(number)

    print("\n=== Generator Expression ===")

    for value in generator_expression_demo():
        print(value)

    print("\n=== Memory Comparison ===")

    nums_list = [x for x in range(100000)]
    nums_gen = (x for x in range(100000))

    print("List Size :", sys.getsizeof(nums_list))
    print("Generator Size :", sys.getsizeof(nums_gen))

    print("\n=== Generator Pipeline ===")

    pipeline = square_filter(
        even_filter(
            pipeline_numbers()
        )
    )

    for value in pipeline:
        print(value)

    print("\n=== Multi-Service Log Aggregator ===")

    for log in service_logs():
        print(log)

