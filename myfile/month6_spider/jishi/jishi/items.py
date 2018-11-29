# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JishiItem(scrapy.Item):
    title=scrapy.Field()
    scoure=scrapy.Field()
    comment=scrapy.Field()
    content=scrapy.Field()
    season=scrapy.Field()
    all_arg=scrapy.Field()
    new_list=scrapy.Field()
    user_list=scrapy.Field()
