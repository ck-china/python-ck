# Scrapy settings for example project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
SPIDER_MODULES = ['example.spiders']
NEWSPIDER_MODULE = 'example.spiders'

USER_AGENT = 'scrapy-redis (+https://github.com/rolando/scrapy-redis)'
#指定scrpy_redis的过滤器组键，不再使用scrapy框架默认的过滤器组键
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#指定scrapy_redis额调度器组键，不再使用scrapy框架默认的调度器组键
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
#设置为True表示允许暂停和恢复(会保持爬虫的爬取状态，下次恢复后接着之前的继续爬取)
SCHEDULER_PERSIST = True
#scrapy的三种request队列模式


#一般都是使用这一中，是默认的队列模式，有自己的优先级顺序
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
#启用了队列的形式，先进先出，相当于一个堆结构
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
#相当于栈的结构，先进的后出
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

#默认激活了scrapy_redis的管道文件，将item数据往redis数据库里存储
ITEM_PIPELINES = {
    'example.pipelines.ExamplePipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,
}

#日志等级为DEBUG模式
LOG_LEVEL = 'DEBUG'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.
DOWNLOAD_DELAY = 1

#指定redis的相关配置
#指定要存储的redis的主机ip
REDIS_HOST='127.0.0.1'
#指定要存储的redis的端口号
REDIS_PORT=6379