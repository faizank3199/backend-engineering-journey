""" 
Abstractions:
 - Abstraction means hiding internal implementation and showing only essential functionality.
 
 Topic Covered:
 - Basic Examples
 - Payment Gateway System Example
 - Notification System Example
 
 =====================
 Author: Mohammad Faizan
"""
#=================================
#   Basic Example
#=================================

from abc import ABC, abstractmethod

class Payment(ABC):
    
    @abstractmethod
    def pay(self, amount):
        pass
    
    
class UPI(Payment):
    def pay(self, amount):
        return f"{amount} paid via UPI"
    
class Card(Payment):
    def pay(self, amount):
        return f"{amount} paid via Card"
    
#====================================
#  Payment Gateway System Example
#====================================

class PaymentGateway(ABC):
    
    @abstractmethod
    def process_payment(self, amount):
        pass
    
class Razorpay(PaymentGateway):
    def process_payment(self, amount):
        return f"Processing {amount} via Razorpay"


class Stripe(PaymentGateway):
    def process_payment(self, amount):
        return f"Processing {amount} via Stripe"

# Service layer 
class PaymentService:
    def make_payment(self, gateway: PaymentGateway, amount: float) -> str:
        if amount <= 0:
            raise ValueError("Amount must be positive")
        return gateway.process_payment(amount)
       
service = PaymentService() 


#========================================
#  Notification System 
#========================================

class Notification(ABC):
    
    @abstractmethod
    def send(self, message):
        pass
    
class SMS(Notification):
    def send(self, message):
        return f"{message}, sent via SMS"
    
class Email(Notification):
    def send(self, message):
        return f"{message}, sent via Email"
    
notifications: list[Notification] = [SMS(), Email()]
 #Service layer
def process_notifications(notifiers:list[Notification], message:str):
    for notifier in notifiers:
        print(notifier.send(message))

        
#=========================================
# Main Function
#========================================

if __name__ == "__main__":
    
    p1 = UPI()
    p2 = Card()
    print("\n--Abstraction Basic Example--")
    print(p1.pay(1000))
    print(p2.pay(2000))  
    
    print("\n--Payment System Gateway Example--")
    print(service.make_payment(Razorpay(), 2300))
    print(service.make_payment(Stripe(), 3400))
    
    
    print("\n--Notification System Example--")
    process_notifications(notifications, "Hello User")
    
    