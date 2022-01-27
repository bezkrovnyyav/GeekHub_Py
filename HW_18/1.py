# Використовуючи бібліотеку requests написати скрейпер для отримання статей / записів із АПІ
#
# Документація на АПІ:
# https://github.com/HackerNews/API
#
# Скрипт повинен отримувати із командного рядка одну із наступних категорій:
# askstories, showstories, newstories, jobstories
#
# Якщо жодної категорії не указано - використовувати newstories.
# Якщо категорія не входить в список - вивести попередження про це і завершити роботу.
#
# Результати роботи зберегти в CSV файл. Зберігати всі доступні поля. Зверніть увагу - інстанси різних типів мають різний набір полів.
#
# Код повинен притримуватися стандарту pep8.
# Перевірити свій код можна з допомогою ресурсу http://pep8online.com/
#
# Для тих, кому хочеться зробити щось "додаткове" - можете зробити наступне: другим параметром cкрипт може приймати
# назву HTML тега і за допомогою регулярного виразу видаляти цей тег разом із усим його вмістом із значення атрибута "text"
# (якщо він існує) отриманого запису.
#  ваш скрипт повинен запускатись командою, наприклад, python 1.py askstories

import csv
import requests
import sys
import datetime

from tqdm import tqdm


class HackerNews(object):

    def __init__(self):
        self.categories = ['askstories', 'showstories', 'newstories', 'jobstories']
        self.create_date = datetime.datetime.today()


    def create_url(self, user_input):
        if user_input == '':
            return f'https://hacker-news.firebaseio.com/v0/{self.categories[2]}.json'
        elif user_input in self.categories:
            return f'https://hacker-news.firebaseio.com/v0/{user_input}.json'
        else:
            print("There is no such category!")
            exit()


    def create_news_csv(self, category_news):

        article_dicts_list = []
        article_filds = []

        category_url = self.create_url(category_news)
        category_articles = requests.get(url=category_url).json()
        for article in tqdm(category_articles):
            article_on_id = f'https://hacker-news.firebaseio.com/v0/item/{article}.json'
            request_article_dict = requests.get(url=article_on_id).json()
            article_dicts_list.append(request_article_dict)
            for key in request_article_dict.keys():
                if key not in article_filds:
                    article_filds.append(key)
                    
        filename = f'{category_news}_news_{self.create_date.strftime("%Y_%m_%d")}.csv'
        with open(filename, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=article_filds, restval='None')
            writer.writeheader()
            writer.writerows(article_dicts_list)

if len(sys.argv) == 1:
    category_news = ''
else:
    category_news = sys.argv[1]

news = HackerNews()
news.create_news_csv(category_news)
