'''Написати скрипт, який буде приймати від користувача назву валюти і початкову дату.
   - Перелік валют краще принтануть.
   - Також не забудьте указати, в якому форматі коритувач повинен ввести дату.
   - Додайте перевірку, чи введена дата не знаходиться у майбутньому ;)
   - Також перевірте, чи введена правильна валюта.
   Виконуючи запроси до API архіву курсу валют Приватбанку, вивести інформацію про зміну
   курсу обраної валюти (Нацбанк) від введеної дати до поточної.
'''

import requests
import datetime as dt
from time import sleep
import json


def rate_archive():
    # ввод информации от пользователя и проверка актуальности даты.
    print('Available currency: USD, EUR, RUB')
    currency = input('Select the currency you want to see: ')

    if currency not in ['USD', 'usd', 'Usd', 'EUR', 'eur', 'Eur', 'RUB', 'rub', 'Rub']:
        print("There is no other currency fo displaying")
        return

    moment = input('Enter date in format dd.mm.yyyy: ')
    date_now = dt.datetime.now()
    try:
        moment_format = dt.datetime.strptime(moment, "%d.%m.%Y")
    except ValueError:
        print('Rong format')
        return

    delta = dt.timedelta(days=1)

    if moment_format > date_now:
        print("IT can not be displayed the curenncy exchange rate of the future")
        return

    new_moment = moment
    new_moment_format = moment_format
    nbu = 0

    print(f'Currency: {currency}')
    while new_moment_format < date_now:
        url = 'https://api.privatbank.ua/p24api/exchange_rates?json&date=' + f'{new_moment}'
        response = requests.get(url)
        rate = json.loads(response.text)['exchangeRate']

        for r in rate:
            if 'currency' not in [i for i in r.keys()]:
                continue
            elif r['currency'] == currency.upper():
                print(f'Date: {new_moment}')
                if nbu == 0:
                    print(f'NBU: {r["saleRateNB"]}     ------')
                else:
                    print(f'NBU: {r["saleRateNB"]}     {float(r["saleRateNB"]) - nbu}')
                print('-' * 30)
                nbu = float(r["saleRateNB"])
                sleep(1)

        next_day = new_moment_format + delta
        new_moment_format = next_day
        temp = str(dt.datetime.date(new_moment_format)).split('-')
        new_moment = f'{temp[2]}.{temp[1]}.{temp[0]}'
    exit()

def run_rate_archive():
    while True:
        yield rate_archive()
