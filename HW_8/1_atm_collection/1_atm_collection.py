'''
1. Доповніть програму-банкомат з попереднього завдання таким функціоналом, як використання банкнот.
   Отже, у банкомата повинен бути такий режим як "інкассація", за допомогою якого в нього можна "загрузити" деяку кількість банкнот (вибирається номінал і кількість).
   Зняття грошей з банкомату повинно відбуватись в межах наявних банкнот за наступним алгоритмом - видається мінімальна кількість банкнот наявного номіналу. P.S. Будьте обережні з використанням "жадібного" алгоритму (коли вибирається спочатку найбільша банкнота, а потім - наступна за розміром і т.д.) - в деяких випадках він працює неправильно або не працює взагалі. Наприклад, якщо треба видати 160 грн., а в наявності є банкноти номіналом 20, 50, 100, 500,  банкомат не зможе видати суму (бо спробує видати 100 + 50 + (невідомо), а потрібно було 100 + 20 + 20 + 20 ).
   Особливості реалізації:
   - перелік купюр: 10, 20, 50, 100, 200, 500, 1000;
   - у одного користувача повинні бути права "інкасатора". Відповідно і у нього буде своє власне меню із пунктами:
     - переглянути наявні купюри;
     - змінити кількість купюр;
   - видача грошей для користувачів відбувається в межах наявних купюр;
   - якщо гроші вносяться на рахунок - НЕ ТРЕБА їх розбивати і вносити в банкомат - не ускладнюйте собі життя, та й, наскільки я розумію, банкомати все, що в нього входить, відкладає в окрему касету.
2. Для кращого засвоєння - перед написанням коду із п.1 - видаліть код для старої програми-банкомату і напишіть весь код наново (завдання на самоконтроль).
   До того ж, скоріш за все, вам прийдеться і так багато чого переписати.
'''

import json
import os

def check_user():
    tries = 0
    while tries < 3:
        file_json = 'clients.json'
        with open(file_json, "r") as f:
            users_data = json.load(f)
        username = input('Input username: ')
        password = input('Input password: ')
        if  any(i.get('username') == username for i in users_data):
            if any(i.get('password') == password for i in users_data):
                print('You are not entered into the atm system!\n')
                if username == 'collection':
                    atm_collection(username)
                return username 
            else:
                print('You have enteres incorrect password !')
                tries += 1
        else:
            print('You have enteres incorrect username !')
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
            print(f'There are {check_balance_ATM(operation)} $ inthe ATM \n')
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


def get_money(money):  
    # finding the minimum possible amount for issuing money using the dynamic programming algorithm
    lst_banknotes = [1000, 500, 200, 100, 50, 20]
    INF = 10 ** 10
    F = [INF] * (money + 1)
    F [0] = 0
    for k in range(1, money + 1):
        for i in range(len(lst_banknotes)):
            if k - lst_banknotes[i] >= 0 and F[k - lst_banknotes[i]] < F[k]:
                F[k] = F[k - lst_banknotes[i]]
        F[k] += 1
    result_banknotes = []
    k = money
    while k != 0:
        for i in range(len(lst_banknotes)):
            if k-lst_banknotes[i] >= 0 and F[k] == F[k - lst_banknotes[i]] + 1:
                result_banknotes.append(lst_banknotes[i])
                k -= lst_banknotes[i]
    return result_banknotes


def check_enough_banknotes_atm(money):  
    # checking the sufficient number of denominations of banknotes in the ATM
    lst_banknotes =  get_money(money)  # [500, 100, 20, 20, 20]
    dict_number_banknotes = {str(i): lst_banknotes.count(i) for i in lst_banknotes}  # {'100': 1, '20': 3, '500': 1}
    collection = 'collection'
    user_file = collection + '_balance.json'  # allmoneyin ATM
    with open(user_file, "r") as f:
        dict_collection_balance =  json.load(f)  # {"20": 60, "50": 50, "100": 50, "200": 50, "500": 50, "1000": 50}
    result_dict = {key: dict_collection_balance[key]-dict_number_banknotes[key] for key in dict_collection_balance if key in dict_number_banknotes}  # all moneyin ATM after withdrawing {'20': 0, '100': 49, '500': 49}
    return all(value >= 0 for value in result_dict.values())


def check_balance_ATM(operation):
    user = 'collection'
    user_file = user + '_balance.json'
    with open(user_file, "r") as f:
        collection_balance =  json.load(f)
    all_money = (sum(int(bancknote) * value for bancknote, value in collection_balance.items()))  
    if operation == 'check balance ATM':  # Output moneu in the ATM
        print(f'In ATM there are {all_money} $', '\n')
        print('Now in ATM there are: ')
        for bancknote, value in collection_balance.items():
            print(f'Banknotes {bancknote} $ - {value} points')
        add_transaction(user, operation, all_money)  # input data to the collection.json
    return all_money  # this is all banknotes in ATM


def check_banknote(user, banknote):  
    #checks the number of banknotes of the specified denomination
    user_file = user + "_balance.json"
    with open(user_file, "r") as f:
        collection_balance =  json.load(f)
    banknote = str(banknote)  
    return collection_balance[banknote]


def add_cash_to_atm(user, banknote, number):
    user_file = user + "_balance.json"
    with open(user_file, "r") as f:
        collection_balance =  json.load(f)
    banknote = str(banknote)  # str datain json
    collection_balance[banknote] += number
    with open(user_file, "w") as f:
        json.dump(collection_balance, f)
    with open(user_file, "r") as f:
        balance =  json.load(f)
    operation = "load ATM"
    banknote = int(banknote)  # int data for operations
    money = banknote * number  # amount of replenishment of the specified denomination
    add_transaction(user, operation, money)
    print(f'It is loaded at ATM {number} banknotes: {banknote} $. Total downloaded {money} $\n')


def load_atm(user):
    banknote = input('Input the denomination of banknotes ($ 20, 50, 100, 200, 500 or 1000) : ')
    if banknote.isdigit():
        banknote = int(banknote)
        if banknote in [20, 50, 100, 200, 500, 1000]:
            number = input('input denomination of banknotes: ')
            if number.isdigit():
                number = int(number)
                if 0 < number < 100:
                    banknotes_in_atm  = check_banknote(user, banknote)
                    if number + banknotes_in_atm <= 100:
                        add_cash_to_atm(user, banknote, number)  
                    else:
                         print(f'In ATM there is {banknote} $ in quantity {banknotes_in_atm} points \n\
You can put this banknote in quantity {100 - banknotes_in_atm} points')
                else:
                    print('You can load from 1 to 100 banknotes in the ATM. Input the correct number.')        
            else:
                print('Input only a numeric value!\n')
        else:
            print('The ATM does not support this denomination!')
    else:
        print('Input only a numeric value!\n')        


def add_transaction(user, operation, money):
    transaction_file = user + "_transactions.json"
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
    user_file = user + "_balance.json"
    with open(user_file, "r") as f:
        balance =  json.load(f)
    money = balance["account"]    
    if operation == "deposite" or operation == "withdraw":
        return money
    else:
        add_transaction(user, operation, money)
    return money


def deposite(user, money):
    user_file = user + "_balance.json"
    with open(user_file, "r") as f:
        balance =  json.load(f)
    balance["account"] += money
    with open(user_file, "w") as f:
        json.dump(balance, f)
    with open(user_file, "r") as f:
        balance =  json.load(f)
    operation = "deposite"
    add_transaction(user, operation, money)
    return balance["account"]


def withdraw(user, money):
    # decrise money from the user`s balance
    operation = "withdraw"
    user_file = user + "_balance.json"  
    with open(user_file, "r") as f:
        balance =  json.load(f)
    balance["account"] -= money
    with open(user_file, "w") as f:
        json.dump(balance, f)
    add_transaction(user, operation, money)
    lst_banknotes =  get_money(money)  # debiting the account of the ATM
    dict_number_banknotes = {str(i): lst_banknotes.count(i) for i in lst_banknotes}
    user = 'collection'
    user_file = user + "_balance.json"
    with open(user_file, "r") as f:
        dict_collection_balance =  json.load(f)
    result_dict = {key: dict_collection_balance[key]-dict_number_banknotes[key] for key in dict_collection_balance if key in dict_number_banknotes}
    dict_collection_balance.update(result_dict)  # update collection
    dict_digit = {int(k):v for k, v in dict_collection_balance.items()}
    dict_digit_sorted = dict(sorted(dict_digit.items()))
    dict_collection_balance_str = {str(k):v for k, v in dict_digit_sorted.items()}
    with open(user_file, "w") as f:
        json.dump(dict_collection_balance_str, f)
    add_transaction(user, operation, money)
    return


def start():
    user =  check_user()
    # collection validation 
    if user and user != 'collection': 
        while True:
            selection = int(input('''Input the operation:  
    1. Check the balance
    2. Replenishment of the balance
    3. Withdraw money
    4. Exit
    Your choice: 
    '''))
            if selection == 1:
                print('Check the balance')
                operation = "check balance"
                print(f'Your balance is {check_balance(user, operation)} $\n')
            elif selection == 2:
                print('Replenishment of the balance')
                money = input('Input the amount of replenishment of the balance: ')
                if money.isdigit():
                    money = int(money)
                    if money in [1000, 500, 200, 100, 50, 20]:
                        print(f'Your balance is {deposite(user, money)} $, it increased on the amount {money} $\n')
                    else:
                        print('ATM has only: 20, 50, 100, 200, 500 and 1000 $!\n')
                else:
                    print('Input only a numeric value!\n')    

            elif selection == 3:
                print('Withdraw money')
                operation = "withdraw"
                money = input('Input the amount: ')
                if money.isdigit():
                    money = int(money)
                    if money != 0 and money % 10 == 0 and money not in [10, 30]:
                        if check_balance(user, operation) - money >= 0:
                            if check_balance_ATM(operation) - money >= 0:
                                if check_enough_banknotes_atm(money):
                                    withdraw(user, money)
                                    print(f'There are {check_balance(user, operation)} $ on your account, It has been deducted from it {money} $')
                                    print('Banknotes: ', *get_money(money), '$\n')
                                else:
                                    print('ATM does not have banknotes to issue the specified amount!')
                            else:
                                print('At the moment, the ATM does not have enough funds to issue the specified amount!\n')                
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
        print('ATM system finished work!')

if __name__ =='__main__':
    start()

