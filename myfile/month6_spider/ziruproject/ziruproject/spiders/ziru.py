# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ZiruSpider(CrawlSpider):
    name = 'ziru'
    allowed_domains = ['ziroom.com']
    start_urls = ['http://www.ziroom.com/z/nl/z2.html?qwd=&p=1']

    rules = (
        Rule(LinkExtractor(allow=r'.*?qwd=&p=\d+',restrict_xpaths=('//div[@id="page"]',)),callback='parse_data', follow=True),
    )

    def parse_start_url(self, response):
        print(response.status)

    def parse_data(self,response):
        roomlist=response.xpath("//ul[@id='houseList']/li[@class='clearfix']")
        for room in roomlist:
            img=room.xpath(".//div[@class='img pr']/a/img/@src").extract()[0]
            title=room.xpath(".//div[@class='txt']/h3/a/text()").extract()[0]
            address=room.xpath(".//div[@class='txt']/h4/a/text()").extract()[0]
            content=','.join(room.xpath(".//div[@class='txt']/div[@class='detail']/p/span/text()").extract())

            print(content)