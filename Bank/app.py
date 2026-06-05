from BankClass import Bank
from storage import all_accounts
from Functions import findAccountByAccountNumber

def bankApp():
    while True:
        print('Welcome to Nabil Bank Application')
        print('1. Create Account')
        print('2. Deposit Balance')
        print('3. Withdraw Balance')
        print('4. Show Details')
        print('5. Exit')

        choice = int(input('\nEnter your choice (1 - 5): '))

        if choice == 1:
            y_n = input('Do you really want to create account? (y/n): ')
            if y_n == 'y':
                name = input('Enter your account name: ')
                balance = int(input('Enter your balance amount: '))
        
                if balance >= 100:
                    b = Bank(name, balance)
                    all_accounts.append(b)
                    print('-'*30)
                    print(f'Account created with name {b.account_name} and A/C no. {b.account_number}.')
                    print('-'*30)
                else:
                    print('Please deposit atleast Rs.100 inital balance to create account.')
            else:
                print('Continue with your transaction.')
            
        elif choice == 2:
            y_n = input('Do you really want to deposit amount? (y/n): ')
            if y_n == 'y':
                acc_number = input('Enter your account number: ')
                find_acc = findAccountByAccountNumber(acc_number)
                if find_acc:
                    balance = int(input('Enter your deposit balance amount: '))
                    if balance >= 100:
                        find_acc.deposit(balance)
                    else:
                        print(f'Deposit amount must be more than Rs.100.')
                else:
                    print('Account Number does not match. No account found.')
            else:
                print('Continue with your transaction.')
        elif choice == 3:
            y_n = input('Do you really want to withdraw amount? (y/n): ')
            if y_n == 'y':
                acc_number = input('Enter your account number: ')
                find_acc = findAccountByAccountNumber(acc_number)
                if find_acc:
                    balance = int(input('Enter your withdraw balance amount: '))
                    if balance >= 100:
                        find_acc.withdraw(balance)
                    else:
                        print(f'Withdraw amount must be more than Rs.100.')
                else:
                    print('Account not found!!')
            else:
                print('Continue with your transaction.')
        elif choice == 4:
            y_n = input('Do you really want to withdraw amount? (y/n): ')
            if y_n == 'y':
                acc_number = input('Enter your account number: ')
                find_acc = findAccountByAccountNumber(acc_number)
                if find_acc:
                    find_acc.print_details()
                else:
                    print('Account not found!!')
            else:
                print('Continue with your transaction.')
        elif choice == 5:
            print('Thank you for choosing us.')
            break
        else:
            print('Invalid Input.')