"""
=================================================
                PYTHON ITERATORS
=================================================

An iterator is an object that:

 - Stores its current state
 - Produces values one at a time
 - Remembers where it stopped
 - Implements the iterator protocol

Iterator Protocol:
------------------
1. __iter__()  -> Returns the iterator object
2. __next__()  -> Returns the next value

Topics Covered:
---------------
1. Simple Iterator
2. Custom Counter Iterator
3. Reverse Counter Iterator (5 → 1)
4. Even Number Iterator
5. Configurable Even Number Iterator
6. Reverse String Iterator
7. Infinite Iterator

Author:
-------
Mohammad Faizan

Goal:
-----
Understand how Python iterators work internally and
how custom iterators can be built from scratch.

=================================================
"""

# =================================================
# 1. Simple Iterator
# =================================================

numbers = [120, 343, 232]

iterator = iter(numbers)


# =================================================
# 2. Custom Counter Iterator
# =================================================

class Counter:
    """
    Iterator that counts from 1 to limit.
    """

    def __init__(self, limit: int):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.current <= self.limit:
            value = self.current
            self.current += 1
            return value

        raise StopIteration


counter = Counter(10)


# =================================================
# 3. Reverse Counter Iterator
# =================================================

class ReverseCounter:
    """
    Iterator that counts backwards.

    Example:
        5, 4, 3, 2, 1
    """

    def __init__(self, start: int):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):

        if self.current >= 1:
            value = self.current
            self.current -= 1
            return value

        raise StopIteration


reverse_counter = ReverseCounter(5)


# =================================================
# 4. Even Number Iterator
# =================================================

class EvenIterator:
    """
    Iterator that returns even numbers
    from 2 up to a given limit.
    """

    def __init__(self, limit: int):
        self.limit = limit
        self.current = 2

    def __iter__(self):
        return self

    def __next__(self):

        if self.current <= self.limit:
            value = self.current
            self.current += 2
            return value

        raise StopIteration


even_numbers = EvenIterator(10)


# =================================================
# 5. Configurable Even Number Iterator
# =================================================

class EvenRangeIterator:
    """
    Iterator that returns even numbers
    between a start value and limit.

    Example:
        EvenRangeIterator(2, 20)
    """

    def __init__(self, start: int, limit: int):
        
        if start % 2 != 0:
            start += 1
        self.current = start
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):

        if self.current <= self.limit:
            value = self.current
            self.current += 2
            return value

        raise StopIteration


even_range = EvenRangeIterator(2, 20)

#================================================
#  6. Reverse String Iterator
#================================================

class ReverseStrIterator:

    def __init__(self, s):
        self.string = s
        self.index = len(s) - 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.index >= 0:
            char = self.string[self.index]
            self.index -= 1
            return char

        raise StopIteration

rev = ReverseStrIterator("hello")

#================================================
# 7. Infinite Iterator
#================================================

# Infinite Iterator

class InfiniteIterator:
    """ 
    Infinite iterator.
    Generates numbers forever until
    the consumer manually stops iteration. 
    """
    def __init__(self, start: int):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        number = self.current
        self.current +=1
        return number
infinite = InfiniteIterator(1)


# =================================================
# Main Execution
# =================================================

if __name__ == "__main__":

    print("\n=== Simple Iterator ===")
    print(next(iterator))

    for number in iterator:
        print(number)

    print("\n=== Counter Iterator ===")
    for value in counter:
        print(value)

    print("\n=== Reverse Counter Iterator ===")
    for value in reverse_counter:
        print(value)

    print("\n=== Even Number Iterator ===")
    for value in even_numbers:
        print(value)

    print("\n=== Even Range Iterator ===")
    for value in even_range:
        print(value)
        
    print("\n=== Reverse String Iterator ===")
    for r in rev:
        print(r)
        
    print("\n=== Infinite Iterator ===")
    for i in infinite:
        if i == 10:
            break
        print(i)
  