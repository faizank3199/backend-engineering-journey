


from datetime import datetime

accounts = []

def get_account(account_num:int):
        for acc in accounts:
            if acc['account_num'] == account_num:
                return acc
        return None 

def create_account(name:str , mob_num:str, account_num:int, balance: float=0):
    
    # check if account exists
    if get_account(account_num):
        return f"Account {account_num} already exists"
    
    # create account
    new_account = {
        "name": name,
        "mob_num": mob_num,
        "account_num": account_num,
        "balance" : balance,
        "transactions": []
    }
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_account['transactions'].append(
        f"[{timestamp}] | account:{account_num}, account created"
    )
    accounts.append(new_account)
    
    return f"[{timestamp}]{name} account created successfully"
    

    