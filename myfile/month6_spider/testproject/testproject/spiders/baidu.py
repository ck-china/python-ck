# -*- coding: utf-8 -*-
import scrapy,re,requests,json
from testproject.items import book_list,book_info

class BaiduSpider(scrapy.Spider):
    #爬虫名称
    name = 'baidu'
    #在这里设置爬虫允许爬取的域，可以是多个
    allowed_domains = ['qidian.com']
    #我们在这里设置爬虫的起始url
    start_urls = ['https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=1']




    #解析的方法（回调方法）
    def parse(self, response):
        print(response.status,'---------------')
        book_list=response.xpath('//ul[@class="all-img-list cf"]/li')
        for book in book_list:
            book_url="https:"+book.xpath('.//div[@class="book-mid-info"]/h4/a/@href').extract()[0]
            print(book_url)

            yield scrapy.Request(url=book_url,callback=self.parse_book_info)
            # yield scrapy.Request(url=book_url+ "#Catalog",dont_filter=True, callback=self.parse_book_chapter)


    def parse_book_info(self,response):
        lists=book_list()
        lists['title'] = response.xpath('//h1/em/text()').extract()[0]
        lists['image']='https:'+response.xpath('.//div[@class="book-img"]/a/img/@src').extract()[0].replace('\r','')
        # https: // book.qidian.com / ajax / comment / index?_csrfToken = ALTVXHG5VYEKGTIEGXd2HQvam1OoJYDI0xPAZohQ & bookId = 1004608738 & pageSize = 15
        result=requests.get("https://book.qidian.com/ajax/comment/index?_csrfToken=ALTVXHG5VYEKGTIEGXd2HQvam1OoJYDI0xPAZohQ&bookId=%s&pageSize=15"%get_num(response.url))
        infos=json.loads(result.text)
        lists['pingfen']=infos['data']['rate']
        lists['tages']=''.join(response.xpath(".//p[@class='tag']/a/text()").extract())
        lists['content']=''.join(response.xpath(".//div[@class='book-intro']/p/text()").extract()).replace(' ','').replace('\r','').replace('\u3000','')
        # print(lists)
        yield lists
        # yield scrapy.Request(url=response.url+"#Catalog",callback=self.parse_book_chapter)


    def parse_book_chapter(self,response):
        volume_list=response.xpath("//div[@class='volume-wrap']/div[@class='volume']")
        for volume in volume_list:
            isvip=volume.xpath("./h3/span/text()").extract()[0].replace(' ',"")
            if isvip ==  '免费':
                chapter_lists=volume.xpath(".//ul[@class='cf']/li/a/@href").extract()
                for chapter in chapter_lists:

                    chapter_url='https:'+chapter
                    # print(chapter_url,'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                    yield scrapy.Request(url=chapter_url,callback=self.chapter_infos)


    def chapter_infos(self,response):
        books=book_info()
        books['chapter_title']=response.xpath("//div[@class='text-head']/h3/text()").extract()[0]
        books['book_name']=response.xpath('//div[@class="info fl"]/a[1]/text()').extract()[0]
        books['font_count']=response.xpath('//span[@class="j_chapterWordCut"]/text()').extract()[0]
        books['pub_time']=response.xpath('//span[@class="j_updateTime"]/text()').extract()[0]
        books['content']=''.join(response.xpath('//div[@class="read-content j_readContent"]/p/text()').extract()).replace('\u3000','').replace('\n','').replace(' ','')
        yield books




def get_num(urls):
    pattern = re.compile('.*?/(\d*)')
    result = re.findall(pattern,urls)
    return result[-1]