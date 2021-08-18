# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AssignoneItem(scrapy.Item):
    # define the fields for your item here like:
    country_name = scrapy.Field()
    total_cases = scrapy.Field()
    new_cases = scrapy.Field()
    total_deaths = scrapy.Field()
    total_recovered = scrapy.Field()
    active_cases = scrapy.Field()
