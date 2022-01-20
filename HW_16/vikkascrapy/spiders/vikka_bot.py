import scrapy
import datetime

from bs4 import BeautifulSoup
from datetime import date
from vikkascrapy.items import VikkaScrapyItem

class VikkaBotSpider(scrapy.Spider):
	
	name = 'news'
	allowed_domains = ['www.vikka.ua']
	start_urls = ['http://www.vikka.ua/']
	entered_date = input("Input date in format yyyy/mm/dd: ")
	counter = 1

	def start_requests(self):
		today_date = date.today()
		formated_today_date = today_date.strftime("%Y/%m/%d")
		year, month, day = self.entered_date.split('/')

		isValidDate = True
		try:
			datetime.datetime(int(year), int(month), int(day))
		except ValueError:
			isValidDate = False

		date_result = "2014/01/02" < self.entered_date < formated_today_date
		if date_result == True and isValidDate == True:
			date_news_url = f"https://www.vikka.ua/{self.entered_date}/"
			yield scrapy.Request(
				url = date_news_url,
				callback =self.parse_news_list
				)
		else:
			print("Pleas, input the correct date")
		
	def parse_news_list(self, response):
		soup = BeautifulSoup(response.text, "lxml")
		news_for_day = soup.select(".item-cat-post")
		for news in news_for_day:
			news_data = news.select_one("a[href]")
			news_link = news_data.get('href')
			yield scrapy.Request(
				url = news_link,
				callback =self.parse_news
				)

		
		next_a_section = soup.select_one('a.next.page-numbers')
		next_link  = next_a_section.get('href')
		if next_link is not None:
			yield scrapy.Request(
				url = next_link,
				callback =self.parse_news_list
				)

	def parse_news(self, response):
		item = VikkaScrapyItem()
		soup = BeautifulSoup(response.text, "lxml")
		news_url = response.url
		news_title_parsed = soup.select_one(".post-title")
		news_title_text = news_title_parsed.text
		
		news_description = soup.select_one(".entry-content")
		news_description_text = news_description.text

		news_tags_parsed = soup.select(".entry-tags li a")
		tags_string = ""
		
		if len(news_tags_parsed) > 0: 
			for line in news_tags_parsed:
				tags_text_parsed = line.text
				tag = "#" + tags_text_parsed + ","
				tags_string += tag

		item["news_title"] = news_title_text
		item["news_description"] = news_description_text
		item["tags_string"] = tags_string
		item["news_url"] = news_url
		item["news_date"] = self.entered_date

		yield item
		

			    





    		







