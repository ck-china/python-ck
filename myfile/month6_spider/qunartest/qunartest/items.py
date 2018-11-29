# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QunartestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    otherinfo=scrapy.Field()  #其他信息
    price=scrapy.Field()  #价格
    historysole=scrapy.Field() #历史成交量
    productid=scrapy.Field()#产品标号
    comments=scrapy.Field()#评论量
    lineInfo=scrapy.Field()#行程路线
    images=scrapy.Field()#景点图片地址
