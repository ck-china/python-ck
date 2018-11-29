# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    #设置起始url，内部是如何发起请求的？

    start_urls = ['https://hr.tencent.com/position.php?keywords=&lid=2156&tid=87&start=0#a']

    #自定义settings.py 中的参数
    custom_settings = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0"
    }



#自定义回调方法

    def start_requests(self):
        #使用场景为：  当访问某个网站时，必须登录以后，才可以获取数据
        #这时候我们需要重写start_requests,在这个方法里可以模拟登录，获取  cookies

        for url in self.start_urls:
            yield  scrapy.Request(url=url,dont_filter=True,callback=self.customers_parse)


    def customers_parse(self,response):
        print(response.status)

    # def parse(self, response):
    #     pass
