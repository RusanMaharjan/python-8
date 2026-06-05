import random
class Bank:
    def __init__(self, account_name, initial_balance):
        self.account_name = account_name
        self.initial_balance = initial_balance
        self.account_number = "".join(str(random.randint(0, 9)) for i in range(16))

    # Function to deposit amount
    def deposit(self, amount):
        if amount > 0:
            self.initial_balance += amount
            print('-'*30)
            print(f'Rs.{amount} has been deposited to A/C no. {self.account_number}')
            print('-'*30)
        else:
            print('-'*30)
            print(f'Deposit amount must be more than 0.')
            print('-'*30)

    # Function to withdraw amount
    def withdraw(self, amount):
        if amount < self.initial_balance:
            self.initial_balance -= amount
            print('-'*30)
            print(f'Rs.{amount} has been withdrawn from A/C no. {self.account_number}')
            print('-'*30)
        else:
            print('-'*30)
            print(f'Withdraw amount must be lower than balance amount.')
            print('-'*30)

    # Function to print user details
    def print_details(self):
        print(f'\nAccount Name: {self.account_name}')
        print(f'Account Number: {self.account_number}')
        print(f'Account Balance: {self.initial_balance}')