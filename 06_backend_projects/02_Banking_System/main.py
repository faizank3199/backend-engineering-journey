"""
=======================================================================================
             Banking Backend System with Transaction Management (Python)
=======================================================================================

Features:
- Create Account
- Deposit / Withdraw
- Transfer Money
- Transaction History
- Balance Checking

Tech:
- Python
- Modular Functions
- File Separation

Author: Mohammad Faizan
===============================================================================
"""



from services.account import create_account
from services.transactions import deposit, withdraw
from services.history import transaction_history
from services.balance import check_balance
from services.transactions import transfer_money

def get_account_and_amount():
    try:
        acc_num = int(input("Enter Account Number: ")) 
        amount = float(input("Enter Amount: "))
        return acc_num, amount
    except ValueError:
        print("Invalid input")
        return None, None

def menu():
    while True:
        print("\n Bank Menu")
        print("1. Create Account")
        print("2. Deposit")
        print("3. withdraw")
        print("4. Check Balance")
        print("5. Transactions History")
        print("6. Trannsfer Money")
        print("7. Exit")
        
        try:
            choice = int(input("Choice the number 1 to 7: "))
            if choice not in range(1, 8):
                raise ValueError
        except ValueError:
            print("Invalid choice. Enter number between 1–7")
            continue
        
        if choice == 1:
            name = input("Enter Name: ")
            mob_num = input("Enter Mobile Number: ")
            account_num = int(input("Enter the Account Number: "))
            balance = float(input("Enter Initial Balance: "))
            print(create_account(name, mob_num, account_num, balance))
            
        elif choice == 2:
            acc_num, amount = get_account_and_amount()
            if acc_num is None:
                continue
            print(deposit(acc_num, amount))
        
        elif choice == 3:
            acc_num, amount = get_account_and_amount()
            if acc_num is None:
                continue
            print(withdraw(acc_num, amount))
        
        elif choice == 4:
            try:
                acc_num = int(input("Enter Account Number: "))
            except ValueError:
                print("Invalid input")
                continue
            print(check_balance(acc_num))
        
        elif choice == 5:
            try:
                acc_num = int(input("Enter Account Number: "))
            except ValueError:
                print("Invalid input")   
                continue 
            print(transaction_history(acc_num))
            
        elif choice == 6:
            try:
                sender = int(input("Enter Sender Account Number: "))
                receiver = int(input("Enter Receiver Account Number: "))
                amount = float(input("Enter Amount: "))
                
                print(transfer_money(sender, receiver, amount))
            except ValueError:
                print("Invalid input")
                continue
            
        elif choice == 7:
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()