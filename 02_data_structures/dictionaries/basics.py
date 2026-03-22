"""
===================================================
            Dictionaries in Python
===================================================

Dictionary:
- A dictionary stores data in key → value pairs.

Topics Covered:
1. Creating Dictionary
2. Access & Modify Dictionary
3. Dictionary Methods
4. Looping through Dictionary
5. Backend Use Case

Author: Mohammad Faizan
Date  : 22/03/2026
"""

# ===================================================
# 1. Creating Dictionary
# ===================================================

print("\n== Creating Dictionary ==")

# Method 1
dict1 = {
    "name": "Ashu",
    "age": 23
}

# Method 2
dict2 = dict(name="Faizan", age=25)

# Method 3 (from list of tuples)
pairs = [("a", 1), ("b", 2)]
dict3 = dict(pairs)

print(dict1)
print(dict2)
print(dict3)


# ===================================================
# 2. Access & Modify Dictionary
# ===================================================

student = {
    "name": "Ashu",
    "marks": 96,
    "is_pass": True
}

print("\n== Access Dictionary ==")
print(student["name"])
print(student["marks"])

# Safe access
print("\n== Safe Access ==")
print(student.get("marks"))
print(student.get("email", "Not Found"))

# Modify value
print("\n== Modify Dictionary ==")
student["is_pass"] = False
print(student)


# ===================================================
# 3. Dictionary Methods
# ===================================================

print("\n== Dictionary Methods ==")

info = {
    "name": "Faizan",
    "age": 24,
    "role": "backend developer"
}

# get()
print("\nget():", info.get("role"))

# update()
info.update({"age": 25, "city": "Delhi"})
print("update():", info)

# Merge dictionaries
a = {"x": 1}
b = {"y": 2}
a.update(b)
print("merge:", a)

# pop()
user = {"name": "Faizan", "age": 25}
user.pop("age")
print("pop():", user)

# popitem()
x = {"a": 1, "b": 2}
x.popitem()
print("popitem():", x)

# setdefault()
user1 = {"name": "Ashu"}
user1.setdefault("age", 23)
print("setdefault():", user1)


# ===================================================
# 4. Loop Through Dictionary
# ===================================================

product = {
    "id": 101,
    "name": "Mobile",
    "price": 25000,
    "stock": "Available"
}

print("\n== Loop Through Keys ==")
for key in product:
    print(key)

print("\n== Access Values via Keys ==")
for key in product:
    print(key, "->", product[key])

print("\n== Loop Through Values ==")
for value in product.values():
    print(value)

print("\n== Loop Through Key-Value ==")
for key, value in product.items():
    print(key, "->", value)


# ===================================================
# 5. Backend Use Case
# ===================================================

users = {
    "u1": {"name": "Faizan", "active": True},
    "u2": {"name": "Rohan", "active": False},
    "u3": {"name": "John", "active": True}
}

print("\n== Backend Use Case ==")

for user_id, data in users.items():
    if data["active"]:
        print(user_id, "->", data["name"])