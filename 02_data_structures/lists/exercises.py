# =====================================================
#                 List Exercises
# =====================================================

"""
Practice problems to master Python lists.

Author : Mohammad Faizan
Date   : 11/03/2026
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

largest_number = numbers[0]

for num in numbers:
    if num > largest_number:
        largest_number = num

print("Largest number:", largest_number)


# ----------------------------------------------------
# 3. Reverse a List

print("\n--- Reverse List Example ---")

numbers = [1, 2, 3, 4, 5]

# Using slicing
reversed_list = numbers[::-1]
print("Reversed list (slicing):", reversed_list)

# Using reverse()
numbers.reverse()
print("Reversed list (reverse method):", numbers)


# ----------------------------------------------------
# 4. Remove Duplicates

print("\n--- Remove Duplicates Example ---")

numbers = [1, 2, 2, 3, 3, 4, 5]

unique_numbers = list(set(numbers))

print("Unique numbers:", unique_numbers)


# ----------------------------------------------------
# 5. Count Occurrences

print("\n--- Count Occurrences Example ---")

letters = ["a", "b", "a", "c", "a"]

count_letter = letters.count("a")

print("Count of 'a':", count_letter)


# ----------------------------------------------------
# 6. Sum of List Elements

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
# 7. Print Names with Index

print("\n--- Index with Name Example ---")

names = ["Faizan", "Rahul", "Sara", "Ashu"]

for index, name in enumerate(names):
    print(f"index {index} -> {name}")


# ----------------------------------------------------
# 8. Access List Using While Loop

print("\n--- While Loop Example ---")

numbers = [1, 3, 4, 5, 1, 3]

i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1


# ----------------------------------------------------
# 9. Find Even Numbers

print("\n--- Even Numbers Example ---")

numbers = [1,2,3,4,5,6,7,8,9,10]

even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print("Even numbers:", even_numbers)


# ----------------------------------------------------
# 10. Normalize Emails (Backend Example)

print("\n--- Email Normalization Example ---")

emails = ["FaiZan@113gmail.Com", "Ashu@123gmail.com"]

for email in emails:
    print(email.lower())


# ----------------------------------------------------
# 11. Pagination Example (Common in APIs)

print("\n--- Pagination Example ---")

data = [1,2,3,4,5,6]

page_1 = data[:3]
page_2 = data[3:6]

print("Page 1:", page_1)
print("Page 2:", page_2)


# ----------------------------------------------------
# 12. Find Common Elements Between Two Lists

print("\n--- Common Elements Example ---")

list1 = [1,2,3,4]
list2 = [3,4,5,6]

common_elements = []

for num in list1:
    if num in list2:
        common_elements.append(num)

print("Common elements:", common_elements)

#-----------------------------------------------------
# 10. Rotate list by one position

numbers = [1, 2, 3, 4, 5]

rotated = numbers[-1:]+ numbers[:-1] 

print("Rotated list:", rotated)