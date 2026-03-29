"""
=====================================
   MINI PROJETCS USING CLOSURE 
=====================================

MINI PROJECTS COVERED:
- Token Generator
- Function Execution Timer 
- Login Attempt Tracker

Author: Mohammad Faizan
Date  : 29/03/2026
"""

def token_generator(user: str):
    """ generate unique token for a user using closure """
    
    count = 0
    
    def generate():
        nonlocal count
        count +=1
        return f"Token-{user}-{count}"
    
    return generate



#===============================================
#   Function Execution Timer
#===============================================
import time
def function_timer(func):
    """ closure that measure time of a function"""
    
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end  = time.perf_counter()
        print(f"Execute Time: {end - start:.4f} seconds")
        return result
    return wrapper 

def add(a, b):
    time.sleep(1)
    result = a + b
    print("Total: ", result)
    print("Task Finished")
    return result



#================================================
#               Login Attempt Tracker
#================================================

def login_tracker(username: str, password: str, limit:int):
    """ Tracks login attempts and locks account  after limit """
    
    attempts = 0
    
    def login(user: str, pswd: str):
        nonlocal attempts
        
        if attempts >= limit:
            return f"{user} Account Locked"
        
        if username == user and password == pswd:
            attempts = 0
            return f"{user} Login Successful"
        attempts += 1
        
        return f"{user} Invalid Credentials (Attempt: {attempts})"

    return login

#=====================================================================

def main():
    
    print("\n--Token Generator--")
    token = token_generator("user101")

    for _ in range(5):
        print(token())
        
    print("\n--Function Execution Timer")  
    calling_function = function_timer(add)
    calling_function(12, 16)
    
    print("\n--Login Attempts tracker--")
    auth = login_tracker("faizan","faizan@123", 3)
    
    print(auth("faiz", "123"))
    print(auth("ashu", "1234ashu"))
    print(auth("faizan","faizan@123"))            
            
if __name__ == "__main__":
    main()


        