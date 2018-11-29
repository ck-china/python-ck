# -*- coding: utf-8 -*-
import scrapy


class MiddlewaretestSpider(scrapy.Spider):
    name = 'middlewaretest'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        pass
