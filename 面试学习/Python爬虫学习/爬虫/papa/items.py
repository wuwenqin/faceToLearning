# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# 无关紧要
class PapaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class StockItme(scrapy.Item):
    # 存取内容
    Img=scrapy.Field()
    Title = scrapy.Field()
    Alter = scrapy.Field()
    Date = scrapy.Field()
    Creator = scrapy.Field()
    Location = scrapy.Field()
    Format = scrapy.Field()
    Dig = scrapy.Field()