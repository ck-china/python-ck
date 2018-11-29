# -*- coding: utf-8 -*-
import scrapy,re,time,requests
from lxml import etree
from jishi.items import JishiItem

class LvyouSpider(scrapy.Spider):
    name = 'lvyou'
    allowed_domains = ['baidu.com']
    start_urls = ['https://lvyou.baidu.com/scene/t-all_s-all_a-all_l-all']

    def parse(self, response):
        li_list=response.xpath('//ul[@class="filter-result"]/li')
        for li in li_list:
            li_url='https://lvyou.baidu.com'+li.xpath('.//div[@class="img-wrap"]/a/@href').extract()[0]
            yield scrapy.Request(url=li_url,callback=self.parse_data)

        other_page=response.xpath("//span[@class='pagelist']/a/@href").extract()
        for page in other_page:
            yield scrapy.Request(url='https://lvyou.baidu.com/scene/t-all_s-all_a-all_l-all'+page,callback=self.parse)





    def parse_data(self,response):
        obj=JishiItem()

        obj['title']=response.xpath('//div[@class="dest-name "]/span/a/text()').extract()[0]
        obj['scoure']=response.xpath('//div[@class="main-score"]/text()').extract()[1]
        obj['comment']=response.xpath('//div[@class="main-score"]/a/text()').extract()[0]
        obj['content']=''.join(response.xpath('//div[@class="main-desc"]/p/text()').extract()).replace(' ','').replace('\n','')
        obj['season']=''.join(response.xpath('//div[@class="main-intro"]/span/span/text()').extract()).replace(' ','').replace('\n','')
        obj['all_arg']='https://lvyou.baidu.com'+response.xpath('//div[@class="main-score"]/a/@href').extract()[0]

        all_img='https://lvyou.baidu.com'+response.xpath('//span[@class="pic-count"]/a/@href').extract()[0]
        result=requests.get(all_img)
        result=etree.HTML(result.text)
        pics=result.xpath('//ul[@id="photo-list"]/li/a/img/@src')[0:10]

        obj['new_list']=",".join(["https:"+i for i in pics])

        arg_list=response.xpath('//div[@class="remark-list"]/div')
        user_list=[]
        for i in arg_list:
            user_dict={}
            user_dict['user']='https:'+i.xpath('//div[@class="ri-avatar-wrap"]/a/img/@src').extract()[0]
            user_dict['pub_time']=i.xpath(".//div[@class='ri-header']/div[@class='ri-time']/text()").extract()[0].replace('\n','')
            user_dict['comment']=''.join(i.xpath(".//div[@class='ri-body']/div[@class='ri-remarktxt']/text()").extract()).replace(' ','').replace('\n','')
            user_dict['views']=i.xpath(".//a[@class='ri-dig ri-dig-available']/span/text()").extract()[0]
            user_dict['com']=i.xpath(".//a[@class='ri-comment']/span/text()").extract()[0]
            user_list.append(user_dict)
        obj['user_list']=user_list
        yield obj


