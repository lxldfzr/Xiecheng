# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiechengItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    hotel_name = scrapy.Field()
    hotel_img = scrapy.Field()
    hotel_address = scrapy.Field()
    hotel_point = scrapy.Field()
    hotel_judgement = scrapy.Field()
    hotel_price = scrapy.Field()
