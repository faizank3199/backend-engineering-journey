from services.account import get_account
from services.account import accounts

def check_balance(account_num:int):
    
    account = get_account(account_num)
    
    if not account:
         return "Account Not Found"
    
    return f"Total Balance: {account['balance']}"


   