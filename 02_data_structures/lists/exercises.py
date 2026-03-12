# =====================================================
#                 List Exercises
# =====================================================

"""

Practice Problems for Python Lists.

Topics:
- Searching
- Filtering
- Aggregation
- List Comprehension
- Backend-style data handling

These exercises help build strong list manipulation
skills required for backend development.

Author : Mohammad Faizan
Date   : 12/03/2026
""" 

"""
 =====================================================
               Basic List Problems
 =====================================================
"""
# ----------------------------------------------------
# 1. Cart Example
# Create an empty list and add items to the cart.
# Remove an item and insert another item.

print("\n--- Cart Example ---")

cart = []

cart.append("Mouse")
cart.append("Laptop")
cart.append("Mobile")
cart.append("Mobile")

print("Cart items:", cart)

# remove Mobile
cart.remove("Mobile")
print("After removing Mobile:", cart)

# insert Bag at index 1
cart.insert(1, "Bag")
print("After inserting Bag:", cart)


# ----------------------------------------------------
# 2. Find the Largest Number in a List

print("\n--- Largest Number Example ---")

numbers = [10, 25, 7, 99, 34]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number:", largest)
# ----------------------------------------------------
# 3. Find Smallest Element

print("\n--- Smallest Element ---")

numbers = [10, 20, 5, 99, 45]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest:", smallest)


# ----------------------------------------------------
# 4. Second Largest Number

print("\n--- Second Largest ---")

numbers = [10, 20, 5, 99, 45]

numbers.sort()

print("Second largest:", numbers[-2])


# ----------------------------------------------------
# 5. Reverse a List

print("\n--- Reverse List Example ---")

numbers = [1, 2, 3, 4, 5]

# Using slicing
reversed_list = numbers[::-1]
print("Reversed list (slicing):", reversed_list)

# Using reverse()
numbers.reverse()
print("Reversed list (reverse method):", numbers)


# ----------------------------------------------------
# 6. Remove Duplicates

print("\n--- Remove Duplicates Example ---")

numbers = [1, 2, 2, 3, 3, 4, 5]

unique_numbers = list(set(numbers))

print("Unique numbers:", unique_numbers)


# ----------------------------------------------------
# 7. Count Occurrences

print("\n--- Count Occurrences Example ---")

letters = ["a", "b", "a", "c", "a"]

count_letter = letters.count("a")

print("Count of 'a':", count_letter)


# ----------------------------------------------------
# 8. Sum of List Elements

print("\n--- Sum of List Example ---")

numbers = [10, 20, 30, 40]

# Using built-in function
sum_of_list = sum(numbers)
print("Sum using sum():", sum_of_list)

# Using loop
total = 0
for num in numbers:
    total += num

print("Sum using loop:", total)


# ----------------------------------------------------
# 9. Print Names with Index

print("\n--- Index with Name Example ---")

names = ["Faizan", "Rahul", "Sara", "Ashu"]

for index, name in enumerate(names):
    print(f"index {index} -> {name}")


# ----------------------------------------------------
# 10. Access List Using While Loop

print("\n--- While Loop Example ---")

numbers = [1, 3, 4, 5, 1, 3]

i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1


# ----------------------------------------------------
# 11. Find Even Numbers

print("\n--- Even Numbers Example ---")

numbers = [1,2,3,4,5,6,7,8,9,10]

even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print("Even numbers:", even_numbers)


# ----------------------------------------------------
# 12. Normalize Emails (Backend Example)

print("\n--- Email Normalization Example ---")

emails = ["FaiZan@113gmail.Com", "Ashu@123gmail.com"]

for email in emails:
    print(email.lower())


# ----------------------------------------------------
# 13. Pagination Example (Common in APIs)

print("\n--- Pagination Example ---")

data = [1,2,3,4,5,6]

page_1 = data[:3]
page_2 = data[3:6]

print("Page 1:", page_1)
print("Page 2:", page_2)


# ----------------------------------------------------
# 14. Find Common Elements Between Two Lists

print("\n--- Common Elements Example ---")

list1 = [1,2,3,4]
list2 = [3,4,5,6]

common_elements = []

for num in list1:
    if num in list2:
        common_elements.append(num)

print("Common elements:", common_elements)

#-----------------------------------------------------
# 15. Rotate list by one position

numbers = [1, 2, 3, 4, 5]

rotated = numbers[-1:]+ numbers[:-1] 

print("Rotated list:", rotated)

#------------------------------------------------------
# 16. count active users 

users = ["active", "inactive", "active","active","inactive"]
print("\n--Active User Count Example--")
print("Active User: ",users.count("active"))

#-----------------------------------------------------------
# 17. Frequency Counter

print("\n--- Frequency Counter ---")

numbers = [1, 2, 2, 3, 3, 3, 4]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Frequency:", frequency)

# ----------------------------------------------------
# 18. Find Index of Element

print("\n--- Find Index ---")

numbers = [10, 20, 30, 40]

index = numbers.index(30)

print("Index of 30:", index)
"""
=========================================================================================
                             Advanced List Problems
======================================================================================== 
"""
# ----------------------------------------------------
# 19. Remove Negative Numbers

print("\n--- Remove Negative Numbers ---")

numbers = [3, -1, 4, -2, 5]

positive = [num for num in numbers if num >= 0]

print("Positive numbers:", positive)


# ----------------------------------------------------
# 20. Convert Strings to Uppercase

print("\n--- Uppercase Names ---")

names = ["faizan", "rahul", "sara"]

upper_names = [name.upper() for name in names]

print("Uppercase:", upper_names)

#------------------------------------------------------

# 21. Split List into Chunks (Pagination Style)

print("\n--- List Pagination ---")

numbers = [1, 2, 3, 4, 5, 6]

chunk_size = 2

chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]

print("Chunks:", chunks)

#-----------------------------------------------------------------
# 22. print square of each element in list

nums = [1,2,3,4,5]
print("\n--List Comprehension Example--")
square = [n * n for n in nums]
print("Square of List:",square)

#-------------------------------------------------------------

# 23. Print squares of only even numbers

nums = [1,2,3,4,5,6,7,8]

print("\n--Filtering Example--")
even_squares = [n * n for n in nums if n % 2 == 0]
print("Square only even number: ",even_squares)
#----------------------------------------------------------------
# 24. print even if number is even else odd

numbers = [1,2,3,4,5,6,7,8]

print("\n--if else example--")
result = ["Even" if n % 2 == 0 else "Odd" for n in numbers]

print(result)
#---------------------------------------------------------------
# Nested list comprehension

# 25. Flatten a nested list
matrix = [[1,2,3], [4,5,6], [7,8,9]]
print("\n--List Flating Example--")
flat =  [x for row in matrix for x in row]
print(flat)

#----------------------------------------------------------------
# 26. clean the emails

emails = ["Ashu@gmail.com","Boy123@Gmail.com"]
print("\n--clean emails example--")

clean = [email.strip().lower() for email in emails] 
print(clean)

#------------------------------------------------------------------
# 27. Filter active user
print("\n--- Filter Active Users ---")

users = [
    {"name": "Faizan", "active": True},
    {"name": "Sara", "active": False},
    {"name": "Ali", "active": True}
]
active_user = [user["name"] for user in users if user["active"]]
print("Active Users: ",active_user)

#---------------------------------------------------------------------
# 28. remove empty values
# print("\n--- Remove Empty Values ---")

data = ["Faizan", "", None, "Rahul", "", "Sara"]

clean = [item for item in data if item]
print("Cleaned: ",clean)

print("\n--- Group Even and Odd Numbers ---")

numbers = [1,2,3,4,5,6]

even = [n for n in numbers if n % 2 == 0]
odd = [n for n in numbers if n % 2 != 0]

print("Even: ",even)
print("Odd: ", odd)

#-----------------------------------------------------------------
# 29. Find top 3 Number

print("\n--- Top 3 Numbers ---")

numbers = [10, 40, 20, 60, 30]

numbers.sort(reverse=True)

print("Top 3 numbers:", numbers[:3])