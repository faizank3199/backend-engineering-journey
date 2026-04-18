"""
========================================
 Message Passing System in Python (OOP)
========================================

This project demonstrates how objects communicate
with each other using message passing.

---------------------------
Author: Mohammad Faizan
---------------------------

"""
#============================
# Basic Example
#============================

from datetime import datetime

class Student:
    """ Represent a student who send a message to a teacher."""
    def send_msg(self, teacher):
        return teacher.receive("Good Morning")
    
class Teacher:
    """ represent a teacher who receive the message"""
    def receive(self, message):
        return f"Message received, {message}"
    
t = Teacher()
s = Student()

#=======================================
#        Message Passing Example
#======================================= 

class User:
    def __init__(self, name):
        """
        Represents a user in a messaging system.
        Attributes:
                  name (str): Name of the user
                  inbox (list): Stores received messages
        """
        self.name = name
        self.inbox = []
        
    def send_message(self, receiver, message):
        """
        Sends a message to another user.
        Args:
            receiver (User): The user receiving the message
            message (str): The message content
        """
        
        print(f"{self.name} -> {receiver.name}: {message}")
        receiver.receive_message(self.name, message)
        
    def receive_message(self, sender_name, message):
        """
        Receives a message and stores it in inbox.
        Args:
            sender_name (str): Name of sender
            message (str): Message content
        """
        timestamp = datetime.now()
        self.inbox.append((sender_name, message, timestamp))
        
    def show_inbox(self):
        """Displays all received messages."""
        
        print(f"\nInbox of {self.name}")
        
        if not self.inbox:
            print(f"No message yet")
        else:
            for sender, msg, time in self.inbox:
                formatted_time = time.strftime("%d-%m-%Y %H:%M")
                print(f"[{formatted_time}] from {sender}: {msg}")

u1 = User("Ashu")
u2 = User("Kaif")
u3 = User("Shuaib")

#======================================
# Main Execution
#======================================

if __name__ == "__main__":
    
    print("\n--Basic Message Passing Example--")
    print(s.send_msg(t))

    print("\n-- Message Passing System --")
    u1.send_message(u2, "hyi, good morning ")
    u2.send_message(u1, "good to see you , say whats a plan for movie")
    u1.send_message(u2, "ok, i suppose that...also, we have to discuss with shuaib")
    u2.send_message(u3, "Hii would u like to watch movie with us")
    u3.send_message(u2, "Hmm... if i free on sunday,  i will be there , ")

    u1.show_inbox()
    u2.show_inbox()
    u3.show_inbox()