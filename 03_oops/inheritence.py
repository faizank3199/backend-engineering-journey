""" 
Inheritance:
 A class can use methods and properties of another class.
 
 
 
 
 Author: Mohammad Faizan
 Date: 11/04/2026
 
"""

#================================
#        Basic Example
#================================

class Animal:
    def speak(self):
        return "Animal speak"
    
class Dog(Animal):     # Dog inherits the Animal 
    def bark(self):
        return "Dog Barks"
    
#======================================
#     Inheritance + Method Overriding
#======================================



if __name__ == "__main__":
    d=Dog()
    print("\n--Basic Inheritance Example--")
    print(d.speak())   #    Dog gets speak() automatically , from parents
    print(d.bark())    # from child
    

    
    



    