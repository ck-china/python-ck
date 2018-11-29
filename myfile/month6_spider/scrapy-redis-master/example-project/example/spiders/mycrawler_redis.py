from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
import scrapy,json
from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.link import Link


class MyCrawler(RedisCrawlSpider):
    #爬虫文件里就两个地方跟单机版爬虫不一样
    #1 继承的类不一样，分布式爬虫继承的是RedisCrawlSpider
    #2 少了一个start_urls参数，多了redis_key，根据这个key从redis数据库里获取爬虫的起始任务


    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'mycrawler_redis'
    allow_domain=['qidian.com']
    redis_key = 'mycrawler:start_urls'

    rules = (
        # follow all links
        Rule(LinkExtractor(), callback='parse_page', follow=True),
    )
    #动态获取要爬取的域，一般不去使用它
    # def __init__(self, *args, **kwargs):
    #     # Dynamically define the allowed domains list.
    #     domain = kwargs.pop('domain', '')
    #     self.allowed_domains = filter(None, domain.split(','))
    #     super(MyCrawler, self).__init__(*args, **kwargs)
    #解析的方法，可以自己写
    def parse_page(self, response):
        return {
            'name': response.css('title::text').extract_first(),
            'url': response.url,
        }
