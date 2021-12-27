'''http://quotes.toscrape.com/ - написати скрейпер для збору всієї доступної інформації про записи:
   цитата, автор, інфа про автора... Отриману інформацію зберегти в CSV файл та в базу. Результати зберегти в
   репозиторії. Пагінацію по сторінкам робити динамічною (знаходите лінку на наступну сторінку і берете з неї URL).
   Хто захардкодить пагінацію зміною номеру сторінки в УРЛі - буде наказаний ;)'''

from bs4 import BeautifulSoup
import requests
import csv
import sqlite3
import os


def info_about_author(url_author):
    page_response_author = requests.get(url_author)
    soup_author = BeautifulSoup(page_response_author.text, 'lxml')
    date = soup_author.select_one(".author-born-date").text
    location = soup_author.select_one(".author-born-location").text
    born = f'{date}, {location}'
    all_info = soup_author.select_one(".author-description").text
    return born, all_info

def all_inform_in_page(elements):
    for element in elements:
        quote = element.select_one(".text").text
        author = element.select_one(".author").text
        href = element.select_one("a").get("href")
        url_author = url_start + href
        born, all_info = info_about_author(url_author)
        information = [author, born, quote, all_info]
        all_inform_list.append(information)

def next_page(page):
    n_page = page.select_one("li.next a")
    try:
        n_page.get("href")
        url = url_start + n_page.get("href")
        return url
    except:
        return None

def write_in_csv(information):
    with open(path + 'info.csv', 'a', encoding='utf-8') as file_csv:
        wr = csv.writer(file_csv)
        for inform in information:
            wr.writerow([inform[0], inform[1], inform[2], inform[3][:300]])

def write_in_sqlite3(information):
    for elem in information:
        author_id = cur.execute('SELECT id FROM author WHERE author_name=?', (elem[0],)).fetchone()
        if not author_id:
            cur.execute('INSERT INTO author (author_name, born, all_information) VALUES (?, ?, ?);', (elem[0], elem[1], elem[3]))

    for t in information:
        quote = t[2]
        author_id = cur.execute('SELECT id FROM author WHERE author_name=?', (t[0],)).fetchone()[0]
        cur.execute('INSERT INTO quotes (user_id, quote) VALUES (?, ?);', (author_id, quote))

    con.commit()

def create_table():
    # authors
    cur.execute('''
CREATE TABLE IF NOT EXISTS author (
    id integer NOT NULL PRIMARY KEY,
    author_name text NOT NULL,
    born text NOT NULL,
    all_information text NOT NULL
);
''')
    # quote
    cur.execute('''
CREATE TABLE IF NOT EXISTS quotes (
    user_id integer NOT NULL,
    quote text NOT NULL,
    FOREIGN KEY (user_id) REFERENCES author (id)
);
''')


path = os.path.dirname(os.path.realpath(__file__)) + '/'

con = sqlite3.connect('info.db')
cur = con.cursor()

with open(path + 'info.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)

url_start = 'http://quotes.toscrape.com'
url = url_start
all_inform_list = []
while True:
    page_response = requests.get(url)
    soup = BeautifulSoup(page_response.text, 'lxml')
    elements = soup.select(".quote")

    all_inform_in_page(elements)
    url = next_page(soup)
    # print(url)
    if url == None:
        break

write_in_csv(all_inform_list)

create_table()

write_in_sqlite3(all_inform_list)

