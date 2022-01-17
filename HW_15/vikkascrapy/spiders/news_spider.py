import re
from datetime import datetime

import scrapy
from bs4 import BeautifulSoup

from vikkascrapy.items import NewsItem


class NewsSpider(scrapy.Spider):
    name = 'vikka_news'

    def start_requests(self):
        urls = [
            'https://www.vikka.ua/'
        ]
        for url in urls:
            self.date = self.select_date()
            yield scrapy.Request(url=f"{url}{self.date}/", callback=self.parse)

    def select_date(self):
        while True:
            date = input('Введіть дату, новини якої потрібно показати у форматі: yyуу/mm/dd: ')
            if self.date_validation(date):
                break
            else:
                print('Неправильна дата.')
        return date

    def date_validation(self, date_str):
        check_date = re.sub(r'\d{4}/\d{2}/\d{2}', '', date_str)
        if len(check_date) == 0:
            now = datetime.now()
            date = datetime(*map(int, date_str.split('/')))
            #print('date  ', date)
            return date <= now
        return False

    def parse(self, response, **kwargs):
        soup = BeautifulSoup(response.text, 'lxml')
        news_list = soup.select_one('.cat-posts-wrap')
        for news in news_list:
            info_url = news.select_one('.title-cat-post a').get('href')
            yield scrapy.Request(url=info_url, callback=self.parse_news_info)
        next_page = soup.select_one('.next')
        if next_page is not None:
            yield scrapy.Request(url=next_page.get('href'), callback=self.parse)

    def parse_news_info(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        content = soup.select_one('.entry-content')
        tags_ul = soup.select_one('.entry-tags ul')

        url = response.url
        title = soup.select_one('.post-title').text
        text = self.get_text(content)
        if tags_ul is not None:
            tags = ', '.join([f'#{tag.get_text()}' for tag in tags_ul])

        yield NewsItem(title=title, content=text, tags=tags, url=url)

    def get_text(self, content: BeautifulSoup):
        text_info = ['.']
        for string in content.stripped_strings:
            if text_info[-1][-1] != '.':
                text_info[-1] = f'{text_info[-1]} {string}'
            else:
                text_info.append(string)
        del text_info[0]
        return '\n'.join(text_info)
