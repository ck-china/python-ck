# -*- coding: utf-8 -*-

# Scrapy settings for mywebproject project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'mywebproject'

SPIDER_MODULES = ['mywebproject.spiders']
NEWSPIDER_MODULE = 'mywebproject.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'mywebproject (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#针对于cookies的设置，一般情况下，我们不携带cookies，也是反反爬虫的一个手段，默认的设置为True
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False
#是一个telent终端的拓展插件，他能够打印日志信息，监听爬虫的爬取状态信息

# Override the default request headers:
#默认的请求头，针对于全局的
DEFAULT_REQUEST_HEADERS = {
  # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  # 'Accept-Language': 'en',
'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html

#爬虫中间件，我们可以自定义爬虫中间件
#SPIDER_MIDDLEWARES = {
#    'mywebproject.middlewares.MywebprojectSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#下载中间件，一般自定义下载中间键，可以在这里激活，中间件后面的数字代表优先级，数字越小，优先级越大
DOWNLOADER_MIDDLEWARES = {
   # 'mywebproject.middlewares.MywebprojectDownloaderMiddleware': 543,
    'mywebproject.middlewares.RandomProxiesDownloadMiddlewares':520,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#拓展信息
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#在这里激活管道文件，后面的数字表示优先级，数字越小，优先级越高
#ITEM_PIPELINES = {
#    'mywebproject.pipelines.MywebprojectPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html

#自动限速拓展 弥补固定请求间隔的不足
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
PROXIES=[
    {'ip_point':'119.29.119.64:8080','pwd_use':None},
    {'ip_ponit':'27.17.45.90:43411',"pwd_use":None},
    {'ip_point':'124.226.192.215:41193','pwd_use':None},
    {'ip_point':'124.226.192.215:8010','pwd_use':"ck:007"},
]