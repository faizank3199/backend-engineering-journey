"""
Class And Object

A class is a blueprint, and an object is an instance of that class.

Topics Covered:
 - Class and Object Example
 - Constructor Example
 - Dunder Methods Example
 - Destructor Example
 - Class Method And Instance Method

============================
Author: Mohammad Faizan
============================
"""
#------------------------------------------------
#  Basic Code: Class vs Object
#-------------------------------------------------

class Branch:
    branch_name = "Electrical"       # class variable
    
    def show_branch(self)->str:         # self → refers current object (means store name inside the object)
        """
        Return current branch name
        """
        return self.branch_name
    
    def change_branch(self):    # Methods (Functions inside class)
        """Change branch for this object"""
        self.branch_name = "Computer Science"
    
"""
===============================================
    Constructor And Destructor 
===============================================

Constructor:
 - Constructor is magic method that automatically run when the object is created. 
 
1. __init__
2. __str__
3. __new__
4. __repr__
 
""" 

#-----------------------------------------------
# Constructor Example
#------------------------------------------------

class Student:     # class Student: → blueprint
    def __init__(self, name:str, marks:int):#  __init__() → constructor (special function that runs when object is created.) 
        """Constructor initializes object"""
        
        self.name = name               # self → refers current object (means store name inside the object)
        self.marks = marks    # instance variable
        
    def show(self):      # instance Methods (Functions inside class)
        return f"Name: {self.name}, Marks: {self.marks}"
        
#-------------------------------------------
# Task 1: Car Class
#-------------------------------------------

class Car:
    def __init__(self, name: str, speed: int):
        if speed < 0:
            raise ValueError("speed must be positive")
        self.name = name
        self.speed = speed

    def show(self) -> str:
        return f"Brand: {self.name}, Speed: {self.speed} km/h"

#-----------------------------------------------
# Task 2: Mobile Class
#-----------------------------------------------

class Mobile:
    def __init__(self, brand: str, price: int):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.brand = brand
        self.price = price

    def apply_discount(self, discount_percent: float) -> float:
        if not 0 <= discount_percent <= 100:
            raise ValueError("Discount must be between 0 and 100")

        discount = (self.price * discount_percent) / 100
        final_price = self.price - discount
        return final_price

#------------------------------------------------
# Task 3: Employee Class
#-----------------------------------------------

class Employee:
    def __init__(self, name: str, salary: int):
        if salary < 0:
            raise ValueError("Salary cannot be negative")

        self.name = name
        self.salary = salary

    def yearly_salary(self) -> int:
        return self.salary * 12
    
#=================================
#       __str__ Method
#=================================

class Teacher:
    def __init__(self, fname:str, lname:str):
        self.fname = fname
        self.lname = lname
        
    def __str__(self):   # print(obj)
        """User-friendly output"""
        return f"Teacher: {self.fname} {self.lname}"
    
#==================================
#      __repr__ Method
#=================================

class X:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
        
    def __repr__(self):
        """Developer-friendly output"""
        return f"X(name='{self.name}', age={self.age})"

#====================================
#         __new__ Method 
#====================================

class Demo:
    def __new__(cls):
        print("Object Created (__new__)")
        return super().__new__(cls)
    def __init__(self):
        print("Object Initialized (__init__)")
        

#=====================================================    
"""
Destructor:
 -  A destructor is a special method that is called 
    when an object is about to be destroyed (garbage collected).
"""
        
#--------------------------------------------
#   Destructor Example (Backend-style)
#--------------------------------------------

class APIClient:
    def __init__(self, APIkey:str):
        self.APIkey = APIkey
        self.connected = True
        print("API client connected")
        
    def send_request(self):
        if self.connected:
            print(f"sending request using APIkeys: {self.APIkey}")
        else:
            print("Connection Closed")
            
    def close(self):
        if self.connected:
            print("API client connection closed")
            self.connected=False
            
    def __del__(self):
        """Destructor (not always reliable in real-world apps)"""
        if self.connected:
            print("Destructor: Closing API connection automatically")
            self.close()
            
#=====================================================
if __name__ == "__main__":
    
    b1 = Branch()
    print("\n--Basic Example Of Class vs Object--")
    b1.change_branch()
    print("Branch Changed:", b1.show_branch())
    
    print("\n--- Class vs Object Example ---")

    s1 = Student("Ashu", 99)
    print("\n--Basic Code Example of Constructor--")
    print(s1.show())

    c1 = Car("BMW", 150)
    print("-- Task 1 --")
    print(c1.show())

    m1 = Mobile("iPhone", 100000)
    final_price = m1.apply_discount(12)
    print("-- Task 2 --")
    print(f"Final Price: {final_price}")

    e1 = Employee("Faizan", 66000)
    print("-- Task 3 --")
    print(f"Yearly Salary: {e1.yearly_salary()}")

    u1 = Teacher("Faizan", "Mansury")
    print("\n-- __str__ Method Example --")
    print(u1)
    
    x = X("Ashu Mansury", 24)
    print("\n-- __repr__ Method Example --")
    print(x)
    
    print("\n-- __new__ Method --")
    d = Demo()
    
    print("\n-- APIClient Destructor Example --")
    client = APIClient("ABC123XYZ")
    client.send_request()
    
