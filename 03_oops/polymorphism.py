""" 
Polymorphism:
 - Polymorphism allows the same function/method name 
  to behave differently depending on the object or data.

Author: Faizan
"""

#===================================
#   Payment System (Example)
#===================================

class Payment:
    def pay(self):
        return f"Processing Payment"
    
class UpiPay(Payment):
    def pay(self):
        return f"Paid via UPI"
    
class CardPay(Payment):
    def pay(self):
        return f"Paid via Card"
    
#====================================
#  Notification Example
#====================================

class Notification:
    def send(self, message ):
        pass
    
class SMSNotification(Notification):
    def send(self, message):
        return f"SMS: {message} "
    
class EmailNotification(Notification):
    def send(self,message):
        return f"Email: {message}"
    
class WhatsAppNotification(Notification):
    def send(self, message):
        return f"WhatsApp: {message}"
    
class PushNotification(Notification):
    def send(self, message):
        return f"Push: {message}"
    
class NotificationsService:
    def send_notifications(self, notification: Notification, message):
        return notification.send(message)
    
#==================================
#    Operator overlaoding
#==================================

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"{self.x}, {self.y}"
    

#===================================
#        Main Execution
#===================================
   
   
if __name__ == "__main__":
    
    
    payments = [UpiPay(), CardPay()]
    print("\n--Polymorphism Payment System Example--")
    for p in payments:
        print(p.pay())    
        
    # usage
    service = NotificationsService()
    print("\n--Notification Example--")
    print(service.send_notifications(EmailNotification(), "Hello"))
    print(service.send_notifications(SMSNotification(), "Helo"))
    print(service.send_notifications(WhatsAppNotification(), "Helo"))
    print(service.send_notifications(PushNotification(), "Helo"))    
    
    p1 = Point(10,45)
    p2 = Point(10,45)
    print("\n--Operator Overloading--")
    print(p1+p2)
    