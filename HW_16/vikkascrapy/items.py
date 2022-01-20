# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class VikkaScrapyItem(scrapy.Item):
	
	news_title = scrapy.Field()
	news_description = scrapy.Field()
	tags_string = scrapy.Field()
	news_url = scrapy.Field()
	news_date = scrapy.Field()
