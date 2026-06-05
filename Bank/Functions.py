from storage import all_accounts

def findAccountByAccountNumber(acc_number):
    for accounts in all_accounts:
        if acc_number == accounts.account_number:
            return accounts
    return None