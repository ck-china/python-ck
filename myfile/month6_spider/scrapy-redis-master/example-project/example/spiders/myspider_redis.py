from scrapy_redis.spiders import RedisSpider


class MySpider(RedisSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'myspider_redis'
    allow_domain=['qidian.com']
    redis_key = 'myspider:start_urls'

    # def __init__(self, *args, **kwargs):
    #     # Dynamically define the allowed domains list.
    #     domain = kwargs.pop('domain', '')
    #     self.allowed_domains = filter(None, domain.split(','))
    #     super(MySpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        #step1:获取小说的详情地址链接
        book_list=response.xpath("//ul[@class='all-img-list cf']/li")
        for book in book_list:
            book_url=book.xpath("./")


        #step2:获取当前分页下其他页面的url
