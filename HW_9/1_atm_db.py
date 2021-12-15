'''
Перепишіть програму-банкомат на використання бази даних для збереження всих даних.
Використовувати БД sqlite3 та натівний Python.
Дока з прикладами: https://docs.python.org/3/library/sqlite3.html
Туторіал (один із): https://www.sqlitetutorial.net/sqlite-python/
Для уніфікації перевірки, в базі повинні бути 3 користувача:
  ім'я: user1, пароль: user1
  ім'я: user2, пароль: user2
  ім'я: admin, пароль: admin (у цього коритувача - права інкасатора)
'''

import sqlite3 
import json
import os
import random
 
def check_user():
    tries = 0
    while tries < 3:
        atm_database = 'ATM_database.db'
        with sqlite3.connect(atm_database) as db:
            cursor = db.cursor()
        username = input('Input username: ')
        password = input('Input password: ')
        find_user = ('SELECT * FROM users WHERE username = ?')
        cursor.execute(find_user, [username])
        result_find_user = cursor.fetchone()
        find_password = ('SELECT * FROM users WHERE password = ?')
        cursor.execute(find_password, [password])
        result_find_password = cursor.fetchone()
        if  result_find_user:  # проверка пароля юзера
            result_find_user = result_find_user[0]
            if  result_find_password:  
                result_find_password = result_find_password[0]
                print('You are  entered into the atm system!\n')
                if username == 'admin':
                    atm_collection(username)  # переход в инкасацию админом
                return username # возвращение к меню атм
            else:
                print('You have input incorrect password !')
                tries += 1
        else:
            print('You have input incorrect username !')
            tries += 1
    print('Sorry, you entered incorrect data three times.\nYour card is be blocked !')
    return False
 
 
def atm_collection(user):
    while True:
        selection = int(input('''Input the operation: 
    1. Check the balance
    2. Increased the ATM
    3. Exit

Your choice: '''))
        if selection == 1:
            print('Check the balance')
            operation = "check balance ATM"
            print(f'There are {check_balance_ATM(operation)} $ in ATM\n')
        elif selection == 2:
            print('Increased the ATM')
            load_atm(user)
        elif selection == 3:
            print('Exit!\nATM system finished work!')
            break
        else:
            print('Incorret choise! Please, try agane!')
    else:
        print('ATM system finished work!')
 
 
def get_money(money):  # нахождения списка банкнот,которае есть в атм
    real_banknotes = []
    lst_banknotes = []
    with open('admin_balance.json', 'r', encoding='utf-8') as g:
        real_banknotes = json.load(g)
        for actual_balance in real_banknotes:
            if real_banknotes[actual_balance] != 0:
                lst_banknotes.append(actual_balance)
        lst_banknotes = list(map(int, lst_banknotes))
    INF = 10 ** 10
    F = [INF] * (money + 1)
    F[0] = 0
    for k in range(1, money + 1):
        for i in range(len(lst_banknotes)):
            if k - lst_banknotes[i] >= 0 and F[k - lst_banknotes[i]] < F[k]:
                F[k] = F[k - lst_banknotes[i]]
        F[k] += 1
    result_banknotes = []
    k = money
    while k != 0:
        for i in range(len(lst_banknotes)):
            if k - lst_banknotes[i] >= 0 and F[k] == F[k - lst_banknotes[i]] + 1:
                result_banknotes.append(lst_banknotes[i])
                k -= lst_banknotes[i]
    return result_banknotes[:]
 
 
def check_enough_banknotes_atm(money):  # проверка наявности необходимыхбанкнот в атм,  money = 400
    lst_banknotes =  get_money(money)  # поверка через get_money [100,100,100,100] если нет 200-х
    dict_number_banknotes = {str(i): lst_banknotes.count(i) for i in lst_banknotes}  # для изымания банкнот из словаря-баланса атм
    user = 'admin'
    user_file = user + "_balance.json"  # сагрузка всего словаря-баланса атм
    with open(user_file, "r") as f:
        dict_admin_balance =  json.load(f) 
    result_dict = {key: dict_admin_balance[key]-dict_number_banknotes[key] for key in dict_admin_balance if key in dict_number_banknotes}  # перевірка на залишення в банкоматі коштів при знятті грошей, наприк. {'20': 0, '100': 49, '500': 49}
    return all(value >= 0 for value in result_dict.values())
 
 
def check_balance_ATM(operation):
    user = 'admin'
    user_file = user + "_balance.json"
    with open(user_file, "r") as f:
        admin_balance =  json.load(f)
    all_money = (sum(int(bancknote) * value for bancknote, value in admin_balance.items()))  
    if operation == "check balance ATM":  # проверка баланса АТМ
        print(f'In ATM there are {all_money} $', '\n')
        print('Now in ATM there are: ')
        for bancknote, value in admin_balance.items():
            print(f"Banknotes {bancknote} $ - {value} pcs.")
        add_transaction(user, operation, all_money)  # в файл транзакции по админу
    return all_money  # возврат всех наявных денег в атм
 
 
def check_banknote(user, banknote):  # перевіряє та повертає кількість банкнот зазначеного номіналу
    user_file = user + "_balance.json"
    with open(user_file, "r") as f:
        admin_balance =  json.load(f)
    banknote = str(banknote)  # json ключі str типа
    return admin_balance[banknote]
 
 
def add_cash_to_atm(user, banknote, number):
    user_file = user + "_balance.json"
    with open(user_file, "r") as f:
        admin_balance =  json.load(f)
    banknote = str(banknote)  # json ключі str типа
    admin_balance[banknote] += number
    with open(user_file, "w") as f:
        json.dump(admin_balance, f)
    with open(user_file, "r") as f:
        balance =  json.load(f)
    operation = "load ATM"
    banknote = int(banknote)  # числовые данные
    money = banknote * number  # сумма пополнения указаного номинала
    add_transaction(user, operation, money)
    print(f'It is loaded at ATM {number} banknotes: {banknote} $ Всього завантажено {money} $\n')
 
 
def load_atm(user):
    banknote = input('Input the denomination of banknotes ($ 20, 50, 100, 200, 500 or 1000 $) : ')
    if banknote.isdigit():
        banknote = int(banknote)
        if banknote in [20, 50, 100, 200, 500, 1000]:
            number = input('Input denomination of banknotes: ')
            if number.isdigit():
                number = int(number)
                if 0 < number < 100:
                    banknotes_in_atm  = check_banknote(user, banknote)
                    if number + banknotes_in_atm <= 100:
                        add_cash_to_atm(user, banknote, number)  # внести деньги 
                    else:
                         print(f'In ATM there is {banknote} $ in quantity {banknotes_in_atm} pcs. \n\
You can put this banknote in quantity {100 - banknotes_in_atm} pcs.')
                else:
                    print('You can load from 1 to 100 banknotes in the ATM. Input the correct number.')        
            else:
                print('Input only a numeric value!\n')
        else:
            print('The ATM does not support this denomination!')
    else:
        print('Input only a numeric value!\n')        
 
 
def add_transaction(user, operation, money):
    user_account = user + '_transactions'
    atm_database = 'ATM_database.db'
    with sqlite3.connect(atm_database) as db:
        cursor = db.cursor()
    # Create a table for user inside 'ATM_database.db' with create some fields: Transaction Operation Balance
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {user_account} (
        Transactions INTEGER PRIMARY KEY AUTOINCREMENT,
        Operation    CHAR    NOT NULL,
        Balance      TEXT    NOT NULL
        );''')
    db.commit ()
    # check user operation
    if operation == "deposite":
        money = "+" + str(money)
    elif operation == "withdraw":
        money = "-" + str(money)
    # work for dict of user_info
    user_info = {'Operation':operation, 'Balance':money}
    user_sql = (f"INSERT INTO {user_account} VALUES (NULL, :Operation, :Balance)")
    cursor.execute(user_sql, user_info)
    db.commit ()
    return
 
 
def check_balance(user, operation):
    atm_database = 'ATM_database.db'
    with sqlite3.connect(atm_database) as db:
        cursor = db.cursor()
    find_balance = ('SELECT account FROM users_balances WHERE username = ?')
    cursor.execute(find_balance, [user])
    balance = cursor.fetchone()
    money = balance[0]  
    if operation == "deposite" or operation == "withdraw" or operation == "user bonus":
        return money
    else:
        add_transaction(user, operation, money)
    return money
 
 
def deposite(user, money):
    operation = "deposite"
    atm_database = 'ATM_database.db'
    with sqlite3.connect(atm_database) as db:
        cursor = db.cursor()
    find_balance = ('SELECT account FROM users_balances WHERE username = ?')
    cursor.execute(find_balance, [user])
    balance = cursor.fetchone()
    balance = balance[0]
    balance += money  # add money to user account
    update_balance = ('UPDATE users_balances SET account = ? WHERE username = ?')
    cursor.execute(update_balance, [balance, user])
    db.commit()
    add_transaction(user, operation, money)
    return balance
 
 
def withdraw(user, money):  
    operation = "withdraw"
    atm_database = 'ATM_database.db'
    with sqlite3.connect(atm_database) as db:
        cursor = db.cursor()
    find_balance = ('SELECT account FROM users_balances WHERE username = ?')
    cursor.execute(find_balance, [user])
    balance = cursor.fetchone()
    balance = balance[0]
    balance -= money  # списание денег у юзера
    update_balance = ('UPDATE users_balances SET account = ? WHERE username = ?')
    cursor.execute(update_balance, [balance, user])
    db.commit()
    add_transaction(user, operation, money)  # запись тразакции user

    lst_banknotes =  get_money(money)  # списание денег у атм
    dict_number_banknotes = {str(i): lst_banknotes.count(i) for i in lst_banknotes}
    user = 'admin'
    user_file = user + "_balance.json"
    with open(user_file, "r") as f:
        dict_admin_balance =  json.load(f)
    result_dict = {key: dict_admin_balance[key]-dict_number_banknotes[key] for key in dict_admin_balance if key in dict_number_banknotes}
    dict_admin_balance.update(result_dict)  # обновление счета админа
    dict_digit = {int(k):v for k, v in dict_admin_balance.items()}  # упорядочить словарь admin_balance.json
    dict_digit_sorted = dict(sorted(dict_digit.items()))
    dict_admin_balance_str = {str(k):v for k, v in dict_digit_sorted.items()}
    with open(user_file, "w") as f:  # обновление admin_balance.json
        json.dump(dict_admin_balance_str, f)
    add_transaction(user, operation, money)  # запись транзакции admin(ATM)
    return 
 
 
def bonus_plus(user):
    operation = "user bonus"
    atm_database = 'ATM_database.db'
    with sqlite3.connect(atm_database) as db:
        cursor = db.cursor()
    find_balance = ('SELECT account FROM users_balances WHERE username = ?')
    cursor.execute(find_balance, [user])
    balance = cursor.fetchone()
    balance = balance[0]
    bonus = int(balance * 0.1)
    balance += bonus  # add bonus to user balance
    update_balance = ('UPDATE users_balances SET account = ? WHERE username = ?')  # update user balance account
    cursor.execute(update_balance, [balance, user])
    db.commit()
    add_transaction(user, operation, bonus)
    return bonus
 
 
def start():
    user =  check_user()
    if user and user != 'admin': # проверка валидности юзераи что он юзер и не админ
        bonus = random.choices([1,0],[0.1,0.9])[0]  # бонус юзеру --> choices модуль random c вероятностью 10%(0.1) для 1(повезло) и 90%(0.9) для 0(неповезло)
        if bonus:
            operation = "user bonus"
            print(f'Nou you get bonus {bonus_plus(user)} $ - 10% of your money.\nThere are {check_balance(user, operation)} $ in your balance\n')
            
        while True:
            selection = int(input('''Input the operation:  
    1. Check the balance
    2. Replenishment of the balance
    3. Withdraw money
    4. Exit
    
    Your choice:'''))
            if selection == 1:
                print('Check the balance')
                operation = "check balance"
                print(f'Your balance has {check_balance(user, operation)} $\n')
            elif selection == 2:
                print('Replenishment of the balance')
                money = input('Input the amount of replenishment of the balance: ')
                if money.isdigit():
                    money = int(money)
                    if money in [1000, 500, 200, 100, 50, 20]:
                        print(f'Your balance has {deposite(user, money)} $, it is increased on the amount {money} $\n')
                    else:
                        print('ATM take only: 20, 50, 100, 200, 500 and 1000 $!\n')
                else:
                    print('Input only a numeric value!\n')    
 
            elif selection == 3:
                print('Withdraw money')
                operation = "withdraw"
                money = input('Input the amount: ')
                if money.isdigit():
                    money = int(money)
                    if money != 0 and money % 10 == 0 and money not in [10, 30]:  # проверка выдачи введенной суммы
                        if check_balance(user, operation) - money >= 0:  # проверка, есть ли введеная сумма для баланса юзера
                            if check_balance_ATM(operation) - money >= 0:  # проверка, есть ли введеная сумма на балансе атм
                                if check_enough_banknotes_atm(money):  # проверка, есть ли достаточное количество банкнот в атм
                                    withdraw(user, money)
                                    print(f'There are {check_balance(user, operation)} $ on your balance, it is decreased on {money} $')
                                    print('Banknotes: ', *get_money(money), '$\n')
                                else:
                                    print(f'There are not banknotes in ATM for withdrawing!')
                            else:
                                print('There are no money for withdrawing at that moment!\n')                
                        else:
                            print('There are not enough money in your account!\n')
                    else:
                        print(f'Input amount, {money} $, ATM cannot issue available denominations of  20, 50, 100, 200, 500 and 1000 $!')                   
                else:
                    print('Input only a numeric value!\n')
   
            elif selection == 4:
                print('\nATM system finished work!')
                break
            else:
                print('Try agane!')    
    else:
        print('\nATM system finished work!')
   
start()