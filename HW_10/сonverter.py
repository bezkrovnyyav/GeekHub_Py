'''Конвертер валют. Прийматиме від користувача назву двох валют і суму (для першої).
   Робить запрос до API архіву курсу валют Приватбанку (на поточну дату) і виконує
   конвертацію введеної суми з однієї валюти в іншу.
'''

import requests
import json
import datetime as dt

class BadInput(Exception):
    def __init__(self, msg):
        self.msg = msg

def date_format():
    date_now = dt.datetime.now()
    date_now = str(dt.datetime.date(date_now)).split('-')
    now = f'{date_now[2]}.{date_now[1]}.{date_now[0]}'
    return now

def list_of_acceptable_currency(rate):
    acceptable_currency = []
    for i in rate:
        acceptable_currency.append(i['currency'])
    return acceptable_currency

def user_input(acceptable):
    for i in range(1):
        currency_start = input('Что конвертируем: ')
        currency_result = input('Во что конвертируем: ')
        sum_to_convert = input('Какую сумму будем конвертировать: ')  # пофиксить ввод отрицательных чисел
        if currency_start in acceptable and currency_result in acceptable and sum_to_convert.isdigit():
            return currency_start, currency_result, abs(int(sum_to_convert))
        else:
            print('НЕ КОРРЕКТНЫЕ ДАННЫЕ')
    raise BadInput('НЕ КОРРЕКТНЫЕ ДАННЫЕ')


def converter():
    url = 'https://api.privatbank.ua/p24api/exchange_rates?json&date=' + f'{date_format()}'
    response = requests.get(url)
    exchange_rates = json.loads(response.text)
    rate = exchange_rates['exchangeRate'][1:]
    print('Cписок конвертируемых валют:')
    acceptable = list_of_acceptable_currency(rate)
    print(acceptable)

    currancy_start, curransy_result, sum_to_convert = user_input(acceptable)

    if currancy_start == 'UAH':
        for r in rate:
            if r['currency'] == curransy_result:
                convert_result = sum_to_convert / r['purchaseRateNB']
                print(round(convert_result, 2))
    else:
        uah = 0
        for r in rate:
            if r['currency'] == currancy_start:
                uah = sum_to_convert * r['purchaseRateNB']
        for r in rate:
            if r['currency'] == curransy_result:
                convert_result = uah / r['purchaseRateNB']
                print(round(convert_result, 2))


converter()