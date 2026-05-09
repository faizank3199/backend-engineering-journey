from services.account import get_account

def transaction_history(account_num: int):
    
    account = get_account(account_num)
    
    if not account:
        return f"Account not found"
    
    return "\n".join(account['transactions'])