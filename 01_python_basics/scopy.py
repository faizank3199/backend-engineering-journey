"""
=================================================
  Scope in python 
=================================================
-------------------------------------------------
 Scope where is visible and where is accessible
-------------------------------------------------

Topic covered:
 - local scope 
 - global scope
 - enclosing scope 
 - built-in-scope
 
 Author: Mohammad Faizan
 Date: 03/03/2026
 
"""
#=================================================
# Local scope
#=================================================

def test()->None:
    """
     variable define inside the function and also accessible inside the function
     
    """
    x = 10       # can not access outside the function
    print(x)
    
    

#=================================================
# Global Scope
#================================================


x = 10
def change()-> None:
    """
    Variable define outside the functions but accessible in full file or code
    becouse function varibale can read global variable 
    """
    print(x)
    
 #--------------------------------------------------   
y = 10

def change_local():
    """
    want to change in global varibale in local scope 
    use global keyword in local varible 
    """
    global y
    y = 20

#-----------------------------------------------------

z = 5
def add_5():
    """
    adding global x varibale in local scope  
    
    """
    global z
    z = z + 25
    
#=============================================================
# Enclosing Scope 
#=============================================================


def outer():
    """
    variable between outer functions and inner function
    
    """
    x = 10    # Enclosing variable
    
    def inner():
        print(x)
        
    inner()
    
    
def outer_2():
    """
    to modified enclosing varibale 
    use -> nonlocal keyword
    """
    x = 10
    def inner_2():
        nonlocal x
        x = 20
        inner_2()
        print("modified enclosing variable:",x)
    
outer_2()
    
    
    
    
# ======================================================
# Main Execution Guard
# ======================================================

if __name__ == "__main__":
    print("Running scope demonstrations...\n")
    
    print("---local scope example---")
    test()
    print("---global scope example---")
    change()
    change_local()
    print("Change in global varibale in local scope:\n",y)
    add_5()
    print(" adding global variable in local scope varibale:\n",z)
    print("---Enclosing scope example---")
    outer()
   
    


   