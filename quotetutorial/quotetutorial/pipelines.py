# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# Scraped data -> Item Containers -> Json/Csv files
# Scraped data -> Item Containers -> Pipeline -> SQL/Mongo Database


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class QuotetutorialPipeline:
    def process_item(self, item, spider):
        print("Pipeline :" + item['title'][0])
        return item
