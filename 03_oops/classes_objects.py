""" 
Class  Vs Object

A class is a blueprint, and an object is an instance of that class.

 #===========================
 Author: Mohammad Faizan
 Date: 05/04/2026
 #===========================
"""
#===============================================
# Basic Code Example 
#===============================================

class Student:     # class Student: → blueprint
    def __init__(self, name:str, marks:int):   #  __init__() → constructor (special functon that runs when object is created.) 
        self.name = name               # self → refers current object (means store name inside the object)
        self.marks = marks
        
    def show(self):      # Methods (Functions inside class)
        return f"Name: {self.name}, Marks: {self.marks}"
        
        

# =========================================================
# Task 1: Car Class
# =========================================================

class Car:
    def __init__(self, name: str, speed: int):
        if speed < 0:
            raise ValueError("speed must be positive")
        self.name = name
        self.speed = speed

    def show(self) -> str:
        return f"Brand: {self.name}, Speed: {self.speed} km/h"



# =========================================================
# Task 2: Mobile Class
# =========================================================

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

# =========================================================
# Task 3: Employee Class
# =========================================================

class Employee:
    def __init__(self, name: str, salary: int):
        if salary < 0:
            raise ValueError("Salary cannot be negative")

        self.name = name
        self.salary = salary

    def yearly_salary(self) -> int:
        return self.salary * 12

#======================================================================
if __name__ == "__main__":

    print("\n--- Class vs Object Example ---")

    s1 = Student("Ashu", 99)
    print(s1.show())

    c1 = Car("BMW", 150)
    print(c1.show())

    m1 = Mobile("iPhone", 100000)
    m1.apply_discount(12)
    print(f"Final Price: {m1.price}")

    e1 = Employee("Faizan", 66000)
    print(f"Yearly Salary: {e1.yearly_salary()}")


