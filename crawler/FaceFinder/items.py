# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TwitterItem(scrapy.Item):
    account = scrapy.Field()
    imageUrl = scrapy.Field()
    tweetUrl = scrapy.Field()
    occurrence = scrapy.Field()
    person_id = scrapy.Field()
    pass