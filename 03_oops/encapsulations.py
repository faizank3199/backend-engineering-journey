""" 
Encapsulation:
 - Binding data (variables) and methods (functions) together
 - Restricting direct access using private variables (__)

Topics Covered:
 - Private variables
 - Data protection
 - Controlled access via methods
 - Real-world examples (Bank, User, Student)
 
 =========================
 Author: Mohammad Faizan
 =========================
 
"""

#===============================================
#                 Bank System
#===============================================

class Bank:
    def __init__(self, balance):  
        if balance < 500:
            raise ValueError("Minimum balance must be 500")
            
        self.__balance = balance
        
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        self.__balance += amount
        return self.__balance       # return update balance
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        if amount > self.__balance:
            raise ValueError("Insufficient balance")

        if self.__balance - amount < 500:
            raise ValueError("Minimum balance of 500 must be maintained")
        
        self.__balance -= amount
        return self.__balance       
    
    def get_balance(self):
        return self.__balance
    
#=================================================
#       User Authentication (Encapsulation)
#=================================================

class User:
    def __init__(self, name, password):
        self.name = name
        self.__password = password
    
    def check_password(self, pswd):
        return pswd == self.__password
    
#=================================================
#            Student Result System
#=================================================

class Student:
    def __init__(self, name, marks):
        if not (0 <= marks <= 100):
            raise ValueError("Marks should be between 0 to 100")
        self.name = name
        self.__marks = marks
    
    def get_result(self):
        if self.__marks >= 40:
            return f"{self.name}: Passed"
        else:
            return f"{self.name}: Failed"
        
    def grade(self):
        if self.__marks >= 90:
            return "A"
        elif self.__marks >= 80:
            return "B"
        elif self.__marks >= 70:
            return "C"
        elif self.__marks >= 60:
            return "D"
        elif self.__marks >= 40:
            return "E"
        else:
            return "F"

#=========================================
#        Main Execution
#=========================================

if __name__ == "__main__":
    
    b = Bank(100000)
    print("After deposit:", b.deposit(10000))
    print("After withdraw:", b.withdraw(6000))
    print("Final Balance:", b.get_balance())
    
    u1 = User("Ashu", "ashu@123")
    print("\n--Checking Password Using Encapsulation--")
    print("Logged in" if u1.check_password("ashu@123") else "Invalid Credentials")
    
    s1 = Student("Faizan",92)
    print("\n--Student Result System--")
    print(s1.get_result())
    print("Grade:", s1.grade())
    
    