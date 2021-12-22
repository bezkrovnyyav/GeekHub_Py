"""Перепишіть програму-банкомат на використання бази даних для збереження всих даних.
Використовувати БД sqlite3 та натівний Python.
Дока з прикладами: https://docs.python.org/3/library/sqlite3.html
Туторіал (один із): https://www.sqlitetutorial.net/sqlite-python/
Для уніфікації перевірки, в базі повинні бути 3 користувача:
  ім'я: user1, пароль: user1
  ім'я: user2, пароль: user2
  ім'я: admin, пароль: admin (у цього коритувача - права інкасатора)

   """

import requests
import json
import sqlite3

class InsufficientBanknotes(Exception):
    pass


class InsufficientFunds(Exception):
    pass


class NegativeFunds(Exception):
    pass


class WrongOperationError(Exception):
    pass


class NoSuchBanknote(Exception):
    pass

def login_pword_check(login, pword):
    login_accepted = False
    incasation = False
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    is_account_exists = cur.execute('select is_incasator from user_logs where user_login=? and user_password=?', (login, pword)).fetchone()
    con.close()
    if is_account_exists:
        login_accepted = True
        if is_account_exists[0] == 1:
            incasation = True
    return login_accepted, incasation

def add_transaction(login, operation, funds):
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    cur.execute(f'insert into {login}_transactions(operation, funds) values(?, ?)', (operation, funds))
    con.commit()
    con.close()
    return

def check_balance(login):
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    user_id = cur.execute('select id from user_logs where user_login=?', (login,)).fetchone()
    user_balance = cur.execute('select user_balance from balance where id=?', (user_id[0],)).fetchone()
    con.close()
    return f'Текущий баланс пользователя {login} = {user_balance[0]}'

#trubl
def drop_balance(login):
    print('3 - Снятие баланса')
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    try:
        # Получение всех банкнот из таблицы
        total_banknotes = cur.execute('SELECT banknote_value, banknote_total FROM banknotes').fetchall()
        total_banknotes_dict = {total_banknotes[i][0]: total_banknotes[i][1] for i in range(len(total_banknotes))}
        print(f'{"-" * 40}\nДоступные купюры:')
        print('\n'.join(f'{key} = {total_banknotes_dict[key]}' for key in total_banknotes_dict))
        dropped_funds = int(input('Введите количество средств для снятия: '))


        user_id = cur.execute('select id from user_logs where user_login=?', (login,)).fetchone()
        user_funds = cur.execute('select user_balance from balance where id=?', (user_id[0],)).fetchone()[0]
        if dropped_funds < 0:
            raise NegativeFunds()
        if dropped_funds > user_funds:
            raise InsufficientFunds()


        # Банкноты, которые будут подсчитыватся для вывода пользователю. Все начинают с 0, в дальнейшем выведутся
        # все, которые не 0
        dropped_banknotes = {10: 0, 20: 0, 50: 0, 100: 0, 200: 0, 500: 0, 1000: 0}

        # Сразу проверка, ошибка если сумма всех банкнот меньше суммы, затребованой пользователем
        if dropped_funds > sum([total_banknotes[i][0] * total_banknotes[i][1] for i in range(len(total_banknotes))]):
            raise InsufficientBanknotes

        dropped_funds_local = dropped_funds
        funds_avaliable_in_banknotes = 0

        # Цикл для проверки, можно ли снять по присутствующим в файле банкнотам нужную сумму
        while True:
            # Счётчик неудачных попыток отнять банкноту для суммы.
            # Если = 3, ошибка "недостаточно банкнот"
            failed_drop = 0
            for banknote in sorted(total_banknotes_dict.keys(), reverse=True):
                if dropped_funds_local // int(banknote) > 0 and int(total_banknotes_dict[banknote]) > 0:
                    # Убираем одну банкноту из дикта
                    total_banknotes_dict[banknote] -= 1
                    # Добавляем банкноту в дикт для вывода
                    dropped_banknotes[banknote] += 1
                    # Сумма средств для проверки сходства с запрошенной суммой
                    funds_avaliable_in_banknotes += int(banknote)
                    # Локальная переменная запрошенной суммы для вычитания
                    # Способствует завершению цикла while, если она <10
                    dropped_funds_local -= int(banknote)
                else:
                    failed_drop += 1
            if funds_avaliable_in_banknotes != dropped_funds and failed_drop == 3:
                raise InsufficientBanknotes()
            if dropped_funds_local < 10:
                break

        # Вносим изменения в базу, хранящую банкноты
        total_banknotes = [(total_banknotes_dict[key], key) for key in total_banknotes_dict]
        print(f'{total_banknotes}')
        cur.executemany('UPDATE banknotes SET banknote_total=? WHERE banknote_value=?', total_banknotes)

        # Вносим изменения в баланс
        user_id = cur.execute('select id from user_logs where user_login=?', (login,)).fetchone()
        user_funds = cur.execute('select user_balance from balance where id=?', (user_id[0],)).fetchone()
        cur.execute('UPDATE balance SET user_balance=? WHERE id=?', (user_funds[0] - dropped_funds, user_id[0]))
        con.commit()
        con.close()

        # Добавляем транзакцию
        add_transaction(login, 'drop', dropped_funds)
        result = ''
        for key in dropped_banknotes.keys():
            if dropped_banknotes[key] > 0:
                result += f'\n{dropped_banknotes[key]} банкнот по {key}'
        return f'Со счёта пользователя {login} было снято {dropped_funds} $ {result}'

    except NegativeFunds:
        return 'Вы ввели некорректную сумму! Возврат в главное меню'
    except InsufficientFunds:
        return 'Недостаточно средств! Возврат в главное меню'
    except ValueError:
        return 'Ошибка ввода! Возврат в главное меню'
    except InsufficientBanknotes:
        return 'В банкомате недостаточно средств! Возврат в главное меню'

# Пополнение баланса юзера
def add_balance(login):
    print('2 - Пополнение баланса')
    try:
        additional_funds = float(input('Введите количество средств для пополнения: '))
        if additional_funds < 0:
            raise NegativeFunds()
        else:
            con = sqlite3.connect('users.db')
            cur = con.cursor()
            user_id = cur.execute('select id from user_logs where user_login=?', (login,)).fetchone()
            user_funds = cur.execute('select user_balance from balance where id=?', (user_id[0],)).fetchone()
            cur.execute('UPDATE balance SET user_balance=? WHERE id=?', (user_funds[0] + additional_funds, user_id[0]))
            con.commit()
            con.close()
            add_transaction(login, 'add', additional_funds)
            return f'Поздравляем! Счёт пользователя {login} был пополнен на {additional_funds} $'

    except NegativeFunds:
        return 'Вы ввели некорректную сумму! Возврат в главное меню'
    except ValueError:
        return 'Вы ввели буквы! Возврат в главное меню'

def check_bankomat_funds():
    result = ''
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    total_banknotes = cur.execute('select banknote_value, banknote_total from banknotes').fetchall()
    con.close()
    for banknote in total_banknotes:
        result += f'Количество банкнот {banknote[0]} = {banknote[1]}\n'
    return result

# Добавление купюр в АТМ
def add_bankomat_funds():
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    print('Изменить кол-во купюр в АТМ')
    try:
        banknotes_value = int(input('Введите купюру: '))
        banknotes_num = int(input('Введите количество купюр: '))
        if banknotes_num < 0:
            raise NegativeFunds()
        else:
            current_banknotes_total = cur.execute('SELECT banknote_total FROM banknotes WHERE banknote_value=?', (banknotes_value,)).fetchone()
            if current_banknotes_total:
                cur.execute('UPDATE banknotes SET banknote_total=? WHERE banknote_value=?', (banknotes_num, banknotes_value))
                con.commit()
                con.close()
                return f'Вы изменили кол-во банкнот {banknotes_value} на {banknotes_num} штук'
            else:
                raise NoSuchBanknote()
    except NegativeFunds:
        return 'Вы ввели некорректную сумму! Возврат в главное меню'
    except ValueError:
        return 'Ошибка ввода! Возврат в главное меню'
    except NoSuchBanknote:
        return 'Такой банкноты не существует! Возврат в главное меню'

# Отображение котировки валют
def show_currency():
    url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
    response = requests.get(url)

    currency = json.loads(response.text)

    print('-' * 30)
    for curr in currency:
        info = f'{curr["ccy"]} -> {curr["base_ccy"]}: buy {curr["buy"]}, sale {curr["sale"]}'
        print(info)
    print('-' * 30)

# Запуск терминала АТМ
def start(login, incasator=False):
    try:
        while True:
            if not incasator:
                user_operation = int(input(f'{"-" * 30}\nДобрый день, {login}! Выберите операцию:'
                                           '\n1. Посмотреть баланс'
                                           '\n2. Пополненить баланса'
                                           '\n3. Снять деньги с баланса'
                                           '\n4. Посмотреть котировки валют на сегодня'
                                           '\n5. Завершение работы АТМ\n'))
                if user_operation in range(1, 6):
                    if user_operation == 1:
                        print(f'{"-" * 30}\n{check_balance(login)}')
                    elif user_operation == 2:
                        print(f'{"-" * 30}\n{add_balance(login)}')
                    elif user_operation == 3:
                        print(f'{"-" * 30}\n{drop_balance(login)}')
                    elif user_operation == 4:
                        show_currency()
                    elif user_operation == 5:
                        print('АТМ завершил работу')
                        return
                else:
                    raise WrongOperationError()
            else:
                print(f'{"-" * 40}\nПриветствую, {login} (инкасатор) Выберите операцию!')
                incas_operation = int(input('1. Проверить наличие купюр\n'
                                            '2. Изменить кол-во купюр в банкомате\n'
                                            '3. Выход\n'))
                if incas_operation in range(1, 4):
                    if incas_operation == 1:
                        print(f'{"-" * 40}\n{check_bankomat_funds()}')
                    if incas_operation == 2:
                        print(f'{"-" * 40}\n{add_bankomat_funds()}')
                    if incas_operation == 3:
                        print('3 - Выход')
                        return
                else:
                    raise WrongOperationError()

    except ValueError:
        return 'error'
    except WrongOperationError:
        return 'Введите правильный номер операции!'

# Проверка логина и пароля
try_counter = 3

while True:
    if try_counter == 0:
        print(f'{"-" * 30}\nВы исчерпали 3 попытки! Закрытие программы.')
        break
    custom_login = input(f'{"-" * 30}\nВведите логин: ')
    custom_password = input('Введите пароль: ')
    access, incasator = login_pword_check(custom_login, custom_password)
    if access:
        start(custom_login, incasator)
        break
    else:
        try_counter -= 1
        print(f'{"-" * 30}\nОшибка ввода логина/пароля. Осталось {try_counter} попыток')


