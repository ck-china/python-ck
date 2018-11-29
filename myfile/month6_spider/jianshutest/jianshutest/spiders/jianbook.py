# -*- coding: utf-8 -*-
import scrapy,re,json
from jianshutest.items import JianBookArc,JianAdmin


class JianbookSpider(scrapy.Spider):
    name = 'jianbook'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://jianshu.com/']

    def parse(self, response):
        result=response.xpath("//div[@class='recommend-collection']/a")[0:7]
        for i in result:
            urls=response.urljoin(i.xpath("./@href").extract()[0])
            arc_type=i.xpath('./div/text()').extract()[0]
            # i=response.urljoin(i)
            yield scrapy.Request(url=urls,callback=self.parse_list,meta={'arc_type':arc_type,'flag':True})









    def parse_list(self,response):
        arc_list=response.xpath("//ul[@class='note-list']/li/a/@href").extract()

        # https://www.jianshu.com/collections/13/side_list
        # https://www.jianshu.com/collections/83/side_list
        # 从scrapy标签里获取id构建请求url
        pattern=re.compile(r'<script\stype="application/json"\sdata-name="collection".*?{"id":(\d+),',re.S)
        adminfo_list=re.findall(pattern,response.text)[0]
        adm_url="https://www.jianshu.com/collections/%s/side_list"%adminfo_list
        yield scrapy.Request(url=adm_url,callback=self.parse_admins,meta={'arc_type':response.meta['arc_type']})
        for arc in arc_list:
            new_url='https://www.jianshu.com'+arc
            yield scrapy.Request(url=new_url,callback=self.parse_info,meta={'arc_type':response.meta['arc_type']})
        next_flag=response.xpath('//ul[@class="note-list"]/@infinite-scroll-url').extract()[0]+'&page='
        if response.meta['flag']:
            next_url='https://www.jianshu.com'+next_flag+'2'
            flag=False

        else:
            flag=False
            pattern=re.compile(r'.*?page=(\d+)')
            page=int(re.findall(pattern,response.url)[0])+1
            next_url='https://www.jianshu.com'+next_flag+str(page)
        yield scrapy.Request(url=next_url, callback=self.parse_list,meta={'arc_type': response.meta['arc_type'], 'flag': flag})




        #下一页请求url
        # https://www.jianshu.com/c/fcd7a62be697?order_by=added_at&page=2
        # https://www.jianshu.com/c/fcd7a62be697?order_by=added_at&page=3



    def parse_admins(self,response):
        adm_infos=json.loads(response.text)['editors']
        for adm in adm_infos:
            admins = JianAdmin()
            admins['admin_name']=adm['nickname']
            admins['admin_img']=adm['avatar_source']
            admins['arc_type']=response.meta['arc_type']
            yield  admins

    def parse_info(self,response):
        item=JianBookArc()
        item['arc_type']=response.meta['arc_type']
        item['title'] = response.xpath("//h1/text()").extract()[0]
        item['content'] =''.join(response.xpath("//div[@class='show-content']//p/text()").extract()).replace(" ",'').replace('\n','').replace('\u200b','').replace('\xa0','')
        item['pub_time'] =response.xpath("//span[@class='publish-time']/text()").extract()[0]
        item['font_count'] =response.xpath("//span[@class='wordage']/text()").extract()[0]
        pattern=re.compile(r'<script\stype="application/json".*?data-name="page-data">(.*?)</script>',re.S)
        author_info=re.findall(pattern,response.text)[0]
        infos=json.loads(author_info)
        item['reads'] =''
        if infos['note']['views_count'] is not None:
            item['reads'] =infos['note']['views_count']
        item['argments'] =''
        if infos['note']['comments_count'] is not None:
            item['argments']=infos['note']['comments_count']
        item['likes'] =''
        if infos['note']['likes_count'] is not None:
            item['likes']=infos['note']['likes_count']
        item['admirs'] =''
        if infos['note']['total_rewards_count'] is not None:
            item['admirs']=infos['note']['total_rewards_count']
        item['author_name'] = infos['note']['author']['nickname']
        item['aut_fonts'] =infos['note']['author']['total_wordage']
        item['auth_fans'] = infos['note']['author']['followers_count']
        item['auth_likes'] = infos['note']['author']['total_likes_count']
        item['auth_diary']=''
        if len(response.xpath('//div[@class="signature"]/text()').extract()) > 0:
            item['auth_diary'] = response.xpath('//div[@class="signature"]/text()').extract()[0].replace('\n','')
        yield item
        # < script
        # type = "application/json"
        # data - name = "page-data" > {"user_signed_in": false, "locale": "zh-CN", "os": "linux", "read_mode": "day",
        #                              "read_font": "font2",
        #                              "note_show": {"is_author": false, "is_following_author": false,
        #                                            "is_liked_note": false, "follow_state": 0,
        #                                            "uuid": "18b04733-093b-49eb-838b-7e58707a9d57"},
        #                              "note": {"id": 36208962, "slug": "af40b5e7d916", "user_id": 8193394,
        #                                       "notebook_id": 28691631, "commentable": true, "likes_count": 3,
        #                                       "views_count": 129, "public_wordage": 2672, "comments_count": 4,
        #                                       "featured_comments_count": 0, "total_rewards_count": 0,
        #                                       "is_author": false, "paid_type": "free", "paid": false,
        #                                       "paid_content_accessible": false,
        #                                       "author": {"nickname": "茶香悠悠2018", "total_wordage": 545881,
        #                                                  "followers_count": 85, "total_likes_count": 299}}} < / script >