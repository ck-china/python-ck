# -*- coding: utf-8 -*-
import scrapy,re
from scrapy.http import  HtmlResponse
from jobboleproject.items import  JobboleprojectItem

class JobboleSpider(scrapy.Spider):
    #爬虫名称
    name = 'jobbole'
    #设置允许爬取的域
    allowed_domains = ['jobbole.com']
    #设置起始url（目标url）
    start_urls = ['http://blog.jobbole.com/all-posts/page/1/']

    def parse(self, response):
        """
        response :请求的响应结果
        我们一般在这里进行数据的解析，和新url的提取
        """
        #第一步，获取文章的列表，提取文章的详情url，发起请求
        #获取当前页面，其他分页的url，继续发起请求
        print(response.status,'-----')
        articles=response.xpath('//div[@id="archive"]/div[@class="post floated-thumb"]')
        for article in articles:
            #文章的url
            #extract() 将数据转换为unicode编码列表
            article_url=article.xpath(".//a[@class='archive-title']/@href").extract()[0]
            coverImageUrl =article.xpath('.//div[@class="post-thumb"]/a/img/@src').extract_first()
            print('!!!!!!',article_url)


            #根据url构建请求，将request请求对象，给调度器
            yield scrapy.Request(url=article_url,callback=self.parse_article_detail,meta={'coverImageUrl':coverImageUrl})


        # other_page_url=response.xpath('//div[@class="navigation margin-20"]/a/@href').extract()
        # for page_url in other_page_url:
        #     #根据分页的url，构建请求，将构建的请求对象，交给调度器
        #     yield scrapy.Request(url=page_url,callback=self.parse)



    #解析文章详情数据
    def parse_article_detail(self,response):
        #获取传递的参数
        coverImageUrl=response.meta['coverImageUrl']




        # 实例化一个JobboleprojectItem对象,将提取的数据赋值给这个对象
        jobbole_item = JobboleprojectItem()

        # 提取数据

        # 将图片地址赋值给jobbole——item
        jobbole_item['coverImageUrl'] = coverImageUrl

        # 提取标题
        jobbole_item['title'] = response.xpath('//div[@class="entry-header"]/h1/text()').extract_first()
        # 提取时间
        jobbole_item['pubLishTime'] = ''.join(response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract()).replace('.', '').replace(' ', '').replace('\r\n', '')

        # 标签
        jobbole_item['tags'] = ','.join(response.xpath('//p[@class="entry-meta-hide-on-mobile"]/a/text()').extract())
        # 作者
        jobbole_item['author'] = response.xpath('//div[@class="copyright-area"]/a/text()').extract_first()
        # 文章的内容
        # jobbole_item['content'] = ','.join(response.xpath(
        #     '//div[@class="entry"]//text()').extract()
        # ).replace(' ','').replace('\r','').replace('\n','').replace('\t','')
        # 文章的地址
        jobbole_item['articleUrl'] = response.url
        # 点赞量
        votenums = ''.join(response.xpath('//div[@class="post-adds"]/span[1]//text()').extract())
        jobbole_item['vote_nums'] = self.get_num(votenums)
        # 收藏量
        collectnums = ''.join(response.xpath('//div[@class="post-adds"]/span[2]//text()').extract())
        jobbole_item['collectnums'] = self.get_num(collectnums)
        # 评论量
        commentnums = ''.join(response.xpath('//div[@class="post-adds"]/a/span//text()').extract())
        jobbole_item['commentnums'] = self.get_num(commentnums)

        print(jobbole_item)

        yield jobbole_item

    def get_num(self, text):
        print(text)

        pattern = re.compile('\d+', re.S)

        result = re.search(pattern, text)

        if result is None:
            result = 0
        else:
            result = int(result.group())

        return result








