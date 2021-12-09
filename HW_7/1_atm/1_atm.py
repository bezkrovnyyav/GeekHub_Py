''' 1. Програма-банкомат.
   Створити програму з наступним функціоналом:
      - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль (файл <users.data>);
      - кожен з користувачів має свій поточний баланс (файл <{username}_balance.data>) та історію транзакцій (файл <{username}_transactions.data>);
      - є можливість як вносити гроші, так і знімати їх. Обов'язкова перевірка введених даних (введено число; знімається не більше, ніж є на рахунку).
   Особливості реалізації:
      - файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом);
      - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла;
      - файл з користувачами: тільки читається. Якщо захочете реалізувати функціонал додавання нового користувача - не стримуйте себе :)
   Особливості функціонала:
      - за кожен функціонал відповідає окрема функція;
      - основна функція - <start()> - буде в собі містити весь workflow банкомата:
      - спочатку - логін користувача - програма запитує ім'я/пароль. Якщо вони неправильні - вивести повідомлення про це і закінчити роботу (хочете - зробіть 3 спроби, а потім вже закінчити роботу - все на ентузіазмі :) )
      - потім - елементарне меню типа:
        Введіть дію:
           1. Продивитись баланс
           2. Поповнити баланс
           3. Вихід
      - далі - фантазія і креатив :)
'''

import json
import os

def check_user():
    tries = 0
    while tries < 3:
        file_json = "clients.json"
        
        with open(file_json, "r") as f:
            users_data = json.load(f)
        
        username = input('Input username: ')
        password = input('Input password: ')
        if  any(item.get('username') == username for item in users_data):
            if any(item.get('password') == password for item in users_data):
                print('You have entered the atm system\n')
                return username
            else:
                print('Input correct password!')
                tries += 1
        else:
            print("Input a valid name!")
            tries += 1

    print('Sorry, you entered incorrect data three times.\nYour card is be blocked!')
    return False


def create_transaction(user, operation, money):
    transaction_file = str(user) + "_transactions.json"

    if os.path.isfile(transaction_file):
        with open(transaction_file, "r",encoding="utf-8") as f:
            info = json.load(f)
            number_transaction = info[-1]["Transaction"] + 1
    else:
         number_transaction = 1

    if operation == "deposite":
        money = "+" + str(money)
    elif operation == "withdraw":
        money = "-" + str(money)

    user_info = {"Transaction":number_transaction,
              "Operation":operation,
              "Balance":money}

    if os.path.isfile(transaction_file):
        with open(transaction_file, "r",encoding="utf-8") as f:
            info = json.load(f)

        info.append(user_info)
        with open(transaction_file, "w",encoding="utf-8") as f:
            json.dump(info, f, indent=4, ensure_ascii=False)

    else:
        with open(transaction_file, "w", encoding="utf-8") as f:
            lst = []
            lst.append(user_info)
            json.dump(lst, f, indent=4, ensure_ascii=False)
    return


def check_balance(user, operation):
    user_file = str(user) + "_balance.json"
    with open(user_file, "r") as f:
        balance =  json.load(f)
    
    money = balance["account"]    
    if operation == "deposite" or operation == "withdraw":
        return money
    else:
        create_transaction(user, operation, money)
    return money


def deposite_operation(user, money):
    user_file = str(user) + "_balance.json"
    with open(user_file, "r") as f:
        balance =  json.load(f)
    balance["account"] += money

    with open(user_file, "w") as f:
        json.dump(balance, f)
    
    with open(user_file, "r") as f:
        balance =  json.load(f)
    operation = "deposite"
    create_transaction(user, operation, money)
    return balance["account"]


def withdraw_operation(user, money):
    user_file = str(user) + "_balance.json"
    with open(user_file, "r") as f:
        balance =  json.load(f)
    if balance["account"] - money >= 0:
        balance["account"] -= money

        with open(user_file, "w") as f:
            json.dump(balance, f)

        with open(user_file, "r") as f:
            balance =  json.load(f)
        operation = "withdraw"
        create_transaction(user, operation, money)
        return True



def start():
    user =  check_user()
    if user:
        while True:
            operations = int(input('''Input the operation: 
    1. Check the balance
    2. Replenishment of the balance
    3. Withdraw money
    4. Exit
 Your choice: '''))
            if operations == 1:
                print('Check the balance')
                operation = "check balance"
                print(f'Your balance is {check_balance(user, operation)} $.\n')

            elif operations == 2:
                print('Replenishment of the balance')
                money = input('Input the amount of replenishment of the balance: ')
                if money.isdigit():
                    money = int(money)
                    print(f'Your balance is {deposite_operation(user, money)} $, it increased on the amount {money} $\n')
                else:
                    print('Input the numeric value\n')           
                
            elif operations == 3:
                print('Withdraw money')
                operation = "withdraw"
                money = input('Input the amount of withdrawing of the money: ')
                if money.isdigit():
                    money = int(money)
                    if withdraw_operation(user, money):
                        print(f'Your balance is {check_balance(user, operation)} $, it decreased on the amount {money} $\n')
                    else:
                        print('You have not enough money in your account!\n')                    
                else:
                    print('Input the numeric value!\n')        

            elif operations == 4:
                print('Thank you for your choice!\nATM system finished work!')
                break
            
            else:
                print('Wrong choice! Please try again!')    
        
    else:
        print('ATM system finished work!')

if __name__ == '__main__':
    start()
