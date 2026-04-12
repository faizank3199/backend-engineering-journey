"""
==============================================
            PYTHON INHERITANCE 
==============================================

Inheritance:
A class can use methods and properties of another class.

Topics Covered:
1. Basic Inheritance
2. Single Level Inheritance
3. Multilevel Inheritance
4. Multiple Inheritance
5. Hierarchical Inheritance
6. Hybrid Inheritance

Author: Mohammad Faizan
Date: 12/04/2026
"""

# ========================================
# Basic Example
# ========================================

class Animal:
    def speak(self):
        return "Animal speaks"


class Dog(Animal):
    def bark(self):
        return "Dog barks"


# ========================================
# 1. Single Level Inheritance
# ========================================

class FatherBasic:
    def home(self):
        return "Home"

    def car(self):
        return "Tata Curvv"

    def bike(self):
        return "Apache"


class Child1(FatherBasic):
    def mobile(self):
        return "iPhone"


# ========================================
# 2. Multilevel Inheritance
# ========================================

class UserBase:
    def login(self):
        return "Login"


class AdminUser(UserBase):
    def access_admin_panel(self):
        return "Accessing admin panel"


class SuperAdminUser(AdminUser):
    def delete_system(self):
        return "System Deleted"


# ========================================
# 3. Multiple Inheritance
# ========================================

class FatherMulti:
    def __init__(self, fname, fage):
        self.fname = fname
        self.fage = fage


class Mother:
    def __init__(self, mname, mage):
        self.mname = mname
        self.mage = mage


class Child(FatherMulti, Mother):
    def __init__(self, cname, cage, fname, fage, mname, mage):
        self.cname = cname
        self.cage = cage

        # NOTE: Direct parent calls (simple approach)
        FatherMulti.__init__(self, fname, fage)
        Mother.__init__(self, mname, mage)

    def show_attr(self):
        print(f"Child: {self.cname}, Age: {self.cage}")
        print(f"Father: {self.fname}, Age: {self.fage}")
        print(f"Mother: {self.mname}, Age: {self.mage}")


# ========================================
# 4. Hierarchical Inheritance
# ========================================

class User:
    def login(self):
        return "User logged in"

    def logout(self):
        return "User logged out"


class Customer(User):
    def place_order(self):
        return "Order placed"


class Admin(User):
    def manage_users(self):
        return "Managing users"


# ========================================
# 5. Hybrid Inheritance (Advanced)
# ========================================

class Parents:
    def __init__(self, p_name, **kwargs):
        super().__init__(**kwargs)
        self.p_name = p_name


class Child_1(Parents):
    def __init__(self, c1_name, **kwargs):
        self.c1_name = c1_name
        super().__init__(**kwargs)


class Child_2(Parents):
    def __init__(self, c2_name, **kwargs):
        self.c2_name = c2_name
        super().__init__(**kwargs)


class Child_3(Child_1, Child_2):
    def __init__(self, c3_name, c1_name, c2_name, p_name):
        super().__init__(
            c1_name=c1_name,
            c2_name=c2_name,
            p_name=p_name
        )
        self.c3_name = c3_name

    def show(self):
        print(f"Parent: {self.p_name}")
        print(f"Child 1: {self.c1_name}")
        print(f"Child 2: {self.c2_name}")
        print(f"Child 3: {self.c3_name}")


# ========================================
# MAIN EXECUTION
# ========================================

if __name__ == "__main__":

    print("\n--- Basic Inheritance ---")
    d = Dog()
    print(d.speak())
    print(d.bark())

    print("\n--- Single Inheritance ---")
    c = Child1()
    print(c.home(), c.mobile())

    print("\n--- Multilevel Inheritance ---")
    sa = SuperAdminUser()
    print(sa.login())
    print(sa.access_admin_panel())
    print(sa.delete_system())

    print("\n--- Multiple Inheritance ---")
    c1 = Child("Ashu", 25, "Harun", 46, "Jasmine", 43)
    c1.show_attr()

    print("\n--- Hierarchical Inheritance ---")
    admin = Admin()
    customer = Customer()
    print(admin.manage_users())
    print(customer.place_order())

    print("\n--- Hybrid Inheritance ---")
    c3 = Child_3("Saif", "Ashu", "Shuaib", "Harun")
    c3.show()

    print("\n--- MRO (Hybrid) ---")
    print(Child_3.__mro__)