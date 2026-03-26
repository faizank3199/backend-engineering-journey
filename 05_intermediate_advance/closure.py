"""
Closure in Python:

A closure is a function that remembers variables from its outer
function even after the outer function has finished execution.

Name : Mohammad Faizan
Date : 12/03/2026
"""

"""
Python Closures Examples
Author : Mohammad Faizan
Date   : 12/03/2026
"""

# ==============================
# 1. Simple Closure Example
# ==============================
def simple_closure():
    hello = "good morning"
    
    def inner():
        print(hello)
        
    return inner

# ==============================
# 2. Update Outer Variable
# ==============================
def update_variable_closure():
    x = 10
    def update_x():
        nonlocal x
        x += 10
        print("Update Value:", x)
    return update_x

# ==============================
# 3. Parameterized Closures
# ==============================
def add(x: int):
    def number(y: int):
        """Return sum of x and y"""
        return x + y
    return number

def multiplier(x: int):
    def number(y: int):
        """Return product of x and y"""
        return x * y
    return number

# ==============================
# 4. State-Preserving Closures
# ==============================
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return f"Count: {count}"
    return increment

def request_counter():
    count = 0
    def handle_request():
        nonlocal count
        count += 1
        return f"Request Number {count}"
    return handle_request

def login_attempt():
    attempt = 0
    def login():
        nonlocal attempt
        attempt += 1
        return f"Attempt: {attempt}"
    return login

# ==============================
# 5. Rate Limiter
# ==============================
def rate_limiter(limit: int):
    request = 0
    def allow_request():
        nonlocal request
        if request >= limit:
            return "Too many requests. Not allowed"
        request += 1
        return f"Request {request} allowed"
    return allow_request

def user_rate_limiter(limit: int):
    users = {}
    def allow_request(user: str):
        nonlocal users
        if user not in users:
            users[user] = 0
        if users[user] >= limit:
            return f"{user} blocked"
        users[user] += 1
        return f"{user} request {users[user]} allowed"
    return allow_request


# ==============================
# Example Run
# ==============================
if __name__ == "__main__":
    print("\n--Simple Closure Example--")
    func = simple_closure()
    func()

    print("\n--Update Variable Example--")
    add_10 = update_variable_closure()
    add_10()
    add_10()

    print("\n--Customized Addition--")
    func_add = add(19)
    print("19 + 20 =", func_add(20))

    print("\n--Customized Multiplier--")
    double = multiplier(2)
    triple = multiplier(3)
    print("Double 20:", double(20))
    print("Triple 20:", triple(20))

    print("\n--Counter Closure Example--")
    c = counter()
    print(c())
    print(c())
    print(c())

    print("\n--Rate Limiter Example--")
    api = rate_limiter(3)
    print(api())
    print(api())
    print(api())
    print(api())

    print("\n--User Rate Limiter Example--")
    api_user = user_rate_limiter(3)
    print(api_user("user1"))
    print(api_user("user1"))
    print(api_user("user2"))
    print(api_user("user1"))
    print(api_user("user2"))