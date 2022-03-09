# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags

def currency(value):
    return value.replace('$', '').strip()

def clean_date(value):
    return value.replace('(','').replace(')','').replace('/','-').replace(' ','')

def arrange(value):
    string = value

    y = string[-4:]
    d = string[:5]
    string = y + '-' + d
    return string

class ScrapeItem(scrapy.Item):

    name = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    publication_date = scrapy.Field(input_processor = MapCompose(remove_tags, clean_date, arrange), output_processor = TakeFirst())
    author = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    price = scrapy.Field(input_processor = MapCompose(remove_tags, currency), output_processor = TakeFirst())
