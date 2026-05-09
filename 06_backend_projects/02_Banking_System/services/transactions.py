from services.account import get_account
from datetime import datetime


def _timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def deposit(account_num: int, amount:float):
    
    account = get_account(account_num)
    
    if not account:
         return "Account Not Found"
    
    if amount <= 0:
        return "Amount must be positive"
            
    account['balance'] += amount
    
    account['transactions'].append(
        f"[{_timestamp()}] | Amount {amount} credited"
    )
        
    return f"[{_timestamp()}] | CREDIT | ₹{amount} | Balance: {account['balance']}"
   
def withdraw(account_num:int, amount:float):
    
    account = get_account(account_num)
    
    if not account:
         return "Account Not Found"
    
    if amount <= 0:
        return "Amount must be positive"
            
    if amount > account['balance']:
        return "Insufficient balance"
            
    account['balance'] -= amount
   
    account['transactions'].append(
        f"[{_timestamp()}] | Amount {amount} debited"
    )
    return f"[{_timestamp()}] | DEBIT | ₹{amount} | Balance: {account['balance']}"

def transfer_money(sender_acc:int, receiver_acc:int,amount:float):

    if amount <= 0:
        return "Amount must be positive"
    
    sender = get_account(sender_acc)
    receiver = get_account(receiver_acc)
    
    if sender is None:
        return f"Sender account {sender_acc} not found"
    
    if receiver is None:
        return f"Receiver account {receiver_acc} not found"
    
    if amount > sender['balance']:
        return "Insufficient Balance" 
    
    sender['balance'] -= amount
    receiver['balance'] += amount

    sender['transactions'].append(
        f"[{_timestamp()}] | TRANSFER OUT | To: {receiver_acc} Amount: ₹{amount} | Balance: {sender['balance']}"
    )
    
    receiver['transactions'].append(
        f"[{_timestamp()}] | TRANSFER IN | From: {sender_acc} Amount: ₹{amount} | Balance: {receiver['balance']}"
    )

    return {
        "status": "success",
        "from": sender_acc,
        "to": receiver_acc,
        "amount": amount
    }