"""
1. Доповніть програму-банкомат наступним функціоналом:
   - Домашнє завдання №14: Переписати останню версію банкомата з використанням ООП
"""



import sqlite3
import datetime
import json
from collections import Counter
import requests


conn = sqlite3.connect('atm.db')
cur = conn.cursor()


def create_db():
    conn = sqlite3.connect('atm.db')
    cur = conn.cursor()
    if input('Would you like to create database? (yes/no)') == 'yes':
        fop = open('atm.db', 'w')
        fop.close()
        cur.execute("""CREATE TABLE IF NOT EXISTS users(
               user_id INT PRIMARY KEY,
               username TEXT,
               password TEXT,
               balance INT,
               status TEXT)""")

        cur.execute("""CREATE TABLE IF NOT EXISTS denominations (
               denomination INT PRIMARY KEY,
               count INT)""")

        cur.execute("""CREATE TABLE IF NOT EXISTS transactions (
              transaction_id INT PRIMARY KEY,
              operation TEXT,
              username TEXT)""")

        users = [('1', 'user1', 'user1', '1500', 'Active'),
                 ('2', 'user2', 'user2', '1500', 'Active'),
                 ('3', 'admin', 'admin', '0', 'Collector')
                 ]
        denominations = [(10, 100),
                         (20, 100),
                         (50, 100),
                         (100, 100),
                         (200, 100),
                         (500, 100),
                         (1000, 100)
                         ]
        cur.executemany("""INSERT INTO users VALUES(?,?,?,?,?);""", users)
        cur.executemany("""INSERT INTO denominations VALUES(?,?);""", denominations)
        cur.execute("""CREATE TABLE IF NOT EXISTS transactions (
                   id INT PRIMARY KEY,
                   operations TEXT)
                   """)
        conn.commit()


def password_validator():
    password_1 = input('Input your new password here: ')
    password_2 = input('Repeat new password: ')
    if password_1 == password_2:
        return password_1
    else:
        return password_validator()


def elements_counter(some_list):
    counter = Counter()
    for element in some_list:
        counter[element] += 1
    return counter.most_common()


class User(object):
    conn = sqlite3.connect('atm.db')
    cur = conn.cursor()

    def __init__(self, username):
        user = cur.execute(f"SELECT * FROM users WHERE username='{username}'").fetchone()
        self.__user = user
        self.__username = self.__user[1]
        self.__password = self.__user[2]
        self.__balance = self.__user[3]
        self.__status = self.__user[4]

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_balance(self):
        return int(self.__balance)

    def get_status(self):
        return self.__status

    def change_balance(self, change):
        new_balance = self.__balance + change
        cur.execute(f"UPDATE users SET balance = {new_balance} WHERE username = '{self.__username}'")
        conn.commit()

    def change_password(self, new_password):
        cur.execute(f"UPDATE users SET password = '{new_password}' WHERE username = '{self.__username}'")
        conn.commit()

    def block(self):
        cur.execute(f"UPDATE users SET status = 'Blocked' WHERE username = '{self.__username}'")
        conn.commit()

    def unblock(self):
        cur.execute(f"UPDATE users SET status = 'Active' WHERE username = '{self.__username}'")
        conn.commit()


class Storage(object):
    conn = sqlite3.connect('atm.db')
    cur = conn.cursor()

    def __init__(self):
        atm = cur.execute('SELECT * FROM denominations;').fetchall()
        self.__denominations = {
            atm[0][0]: int(atm[0][1]),
            atm[1][0]: int(atm[1][1]),
            atm[2][0]: int(atm[2][1]),
            atm[3][0]: int(atm[3][1]),
            atm[4][0]: int(atm[4][1]),
            atm[5][0]: int(atm[5][1]),
            atm[6][0]: int(atm[6][1]),
        }

    def get_denominations(self):
        return self.__denominations

    def change(self, new_values: dict):
        for value in new_values:
            cur.execute(f"UPDATE denominations SET count = '{new_values[value]}' WHERE denomination = '{value}'")
        conn.commit()


class NegativeMeaning(Exception):
    pass


class Authentication(object):

    def __init__(self, login):
        self.login = login

    @staticmethod
    def finish(arg=None):
        print('Thank you, good luck!')
        exit()

    def block(self):
        user = User(self.login)
        if user.get_status() == 'Collector':
            self.finish(self.login)
        else:
            user.block()
            print('Your account was blocked')
            self.finish(self.login)

    def unblock(self):
        user = User(self.login)
        print('To unlock your account, answer the secret question: ')
        answer = input('What is the best programming language is the best? ')
        if answer == 'python' or 'Python':
            user.unblock()
            print('Account unlocked!')
            atm = ATM()
            atm.start()
        else:
            print('Sorry, answer is incorrect, try again later!')

    def authenticate(self):
        user = User(self.login)
        for attempt in range(3):
            if user.get_password() == input(f'Input your password, you have {3 - attempt} attempts '):
                return True
            else:
                if attempt != 2:
                    print(f'Incorrect password, try again, you have {2 - attempt} attempts ')
                else:
                    print('Too many attempts')
                    self.block()


class CollectorsChoices(object):

    def __init__(self, login):
        self.login = login

    def incasation(self):
        menu = Menu(self.login)
        atm = Storage()
        money_in = atm.get_denominations()
        addmoney = money_in.copy()
        for denomination in money_in:
            add = int(input(f'Print count denomination {denomination}: '))
            if add < 0:
                raise NegativeMeaning('You can`t add negative count of money :)')
            addmoney[denomination] += add
        atm.change(addmoney)
        print('Money loaded successfully!')
        menu.collectors_menu()


    def checking_denominations(self):
        atm = Storage()
        menu = Menu(self.login)
        money_in = atm.get_denominations()
        for denomination in money_in:
            print(f'{denomination}: {money_in[denomination]}')
        menu.collectors_menu()


    def change_password(self):
        menu = Menu(self.login)
        new_password = password_validator()
        user = User(self.login)
        user.change_password(new_password)
        print('Your password was changed!')
        if input('Do you want to continue? (yes/no)') == 'yes':
            menu.collectors_menu()
        else:
            ATM.finish(self)


class UserChoices(object):
    def __init__(self, login):
        self.login = login
        self.menu = Menu(login)
    def show_balance(self):
        user = User(self.login)
        print(user.get_balance())
        if input('Do you want to continue (print yes or no)') == 'yes':
            self.menu.menu()
        else:
            ATM.finish(self.login)


    def add_money(self):
        menu = Menu(self.login)
        user = User(self.login)
        summ = int(input('Input the amount you want to add '))
        old_balance = user.get_balance()
        if summ < 0:
            raise NegativeMeaning()
        user.change_balance(summ)
        user = User(self.login)
        new_balance = user.get_balance()
        transaction = {'transaction': f'adding {summ}',
                        'date': str(datetime.datetime.now()),
                        'balance_before': old_balance,
                        'balance_after': new_balance}
        transaction = json.dumps(transaction)
        cur.execute("INSERT INTO transactions (operation, username)  VALUES (?, ?)", (transaction, self.login))
        conn.commit()
        print(f'Thank your for using our ATM, you add {summ}, and now your balance is {new_balance}')
        if input('Do you want to continue (print yes or no) ') == 'yes':
            menu.menu()
        else:
            ATM.finish()


    def withdraw_money(self):
        menu = Menu(self.login)
        user = User(self.login)
        atm = Storage()
        money_in = atm.get_denominations()
        summ_in = 0
        for denomination in money_in:
            if int(money_in[denomination]) != 0:
                print(f'{denomination}', end=' ')
                summ_in += int(money_in[denomination]) * int(denomination)
        print(f'\nYou can take {summ_in}')
        print(f'You have {user.get_balance()} on your account')
        summ = int(input('Input the amount you want to withdraw '))
        if summ <= 0:
            raise NegativeMeaning()
        if summ_in < summ:
            print(f'ATM doesn`t have enough money')
            if input('do you want to continue (print yes or no)') == 'yes':
                menu.menu()
            else:
                ATM.finish()
        old_balance = user.get_balance()
        if summ > old_balance:
            print(f'You don`t have enough money on the balance')
            if input('do you want to continue (print yes or no)') == 'yes':
                menu.menu()
            else:
                ATM.finish()
        denominations_give = []
        money_after_give = money_in.copy()
        summ_to_give = summ
        iterlist = list(money_in.keys())
        iterlist.sort(key=lambda x: int(x), reverse=True)
        while summ_to_give > 0:
            for denomination in iterlist:
                if int(money_after_give[denomination]) != 0 and summ_to_give % int(denomination) == 0:
                    summ_to_give -= int(denomination)
                    denominations_give.append(int(denomination))
                    money_after_give[denomination] -= 1
                else:
                    continue
                break
            else:
                print('ATM can`t give you that summ')
                if input('do you want to continue (print yes or no)') == 'yes':
                    menu.menu()
                else:
                    ATM.finish()
                    break
        user.change_balance(-summ)
        user = User(self.login)
        new_balance = user.get_balance()
        transaction = {'transaction': f'withdrawing {summ}',
                        'date': str(datetime.datetime.now()),
                        'balance_before': old_balance,
                        'balance_after': new_balance}
        transaction = json.dumps(transaction)
        cur.execute("INSERT INTO transactions (operation, username)  VALUES (?, ?)", (transaction, self.login))
        conn.commit()
        print(f'You received')
        for element in elements_counter(denominations_give):
            print(f'{element[0]} - {element[1]} bills')
        print(f'Thank your for using our ATM, you withdraw {summ}, and now your balance is {new_balance}')
        atm.change(money_after_give)
        if input('Do you want to continue (print yes or no) ') == 'yes':
            menu.menu()
        else:
            ATM.finish()

    def change_password(self):
        menu = Menu(self.login)
        new_password = password_validator()
        user = User(self.login)
        user.change_password(new_password)
        print('Your password was changed!')
        if input('Do you want to continue? (yes/no)') == 'yes':
            menu.menu()
        else:
            ATM.finish()


class Menu(object):

    def __init__(self, login):
        self.login = login

    def menu(self):
        choice = input('Choose the operation:\n'
                   '1. Withdraw money\n'
                   '2. Add money on your account\n'
                   '3. Check your account\n'
                   '4. For exchange rates \n'
                   '5. For changing password \n'
                   '6. For exit \n'
                   )
        exchange = Exchange(self.login)
        choices = UserChoices(self.login)
        if choice == '1':
            choices.withdraw_money(),
        elif choice == '2':
            choices.add_money(),
        elif choice == '3':
            choices.show_balance(),
        elif choice == '4':
            exchange.today_rate(),
        elif choice == '5':
            choices.change_password(),
        else:
            ATM.finish()


    def collectors_menu(self):
        choice = input('Choose the operation\n'
                   '1. For add money in atm\n'
                   '2. For check denominations in ATM\n'
                   '3. For exit\n'
                   )
        choices = CollectorsChoices(self.login)
        if choice == '1':
            choices.incasation(),
        elif choice == '2':
            choices.checking_denominations(),
        else:
            ATM.finish(),


class Exchange(object):
    def __init__(self, login):
        self.login = login

    def today_rate(self, date=datetime.datetime.now().strftime("%d.%m.%Y")):
        menu = Menu(self.login)
        atm = ATM()
        currency_choices = {'1': 'USD',
                            '2': 'EUR',
                            '3': 'PLN',
                            '4': 'GBP'}
        url = f'https://api.privatbank.ua/p24api/exchange_rates?json&date={date}'
        raw = requests.get(url)
        currencylist = raw.json()['exchangeRate']
        for currency in currency_choices:
            currency = currency_choices[currency]
            for next_currency in currencylist:
                if 'currency' in next_currency.keys():
                    if next_currency['currency'] == currency:
                        print(f'{currency}\n'
                              f'Buy - {next_currency["purchaseRate"]}\n'
                              f'Purchase - {next_currency["saleRate"]}\n'
                              f'Nbu - {next_currency["saleRateNB"]}\n'
                              f'-------------------')
        if input('Do you want to continiue? (yes/no) ') == 'yes':
            menu.menu()
        else:
            atm.finish('')


class ATM(object):
    def start(self):    
            login = input('Hello, please input your login: ')
            try:
                user = User(login)
            except:
                if input('User not found, do you want to continue? (yes/no)') == 'yes':
                    self.start()
                else:
                    self.finish(login)
            else:
                user = User(login)
                auth = Authentication(login)
                user_status = user.get_status()
                menu = Menu(login)
                if user_status == 'Active':
                    if auth.authenticate():
                        menu.menu()
                if user_status == 'Collector':
                    if auth.authenticate():
                        menu.collectors_menu()
                if user_status == 'Blocked':
                    if input('Your account was blocked, do you want to try to unblock? (yes / no )') == 'yes':
                        auth.unblock()
    @staticmethod
    def finish(arg=None):
        print('Thank you, good luck!')
        exit()

if __name__ == '__main__':
    atm = ATM()
    atm.start()
