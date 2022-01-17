# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import CsvItemExporter


class NewsPipeline:
    def open_spider(self, spider):
        self.file = open('temp.csv', 'ab')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.fields_to_export = ['title', 'content', 'tags', 'url']
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        import os
        self.exporter.finish_exporting()
        self.file.close()
        if os.path.exists(f'{spider.date.replace("/", "_")}.csv'):
            os.remove(f'{spider.date.replace("/", "_")}.csv')
        os.rename('temp.csv', f'{spider.date.replace("/", "_")}.csv')
