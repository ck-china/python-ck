# -*- coding: utf-8 -*-
import scrapy,re,json
from scrapy.selector import Selector


class QunarSpider(scrapy.Spider):
    name = 'qunar'
    allowed_domains = ['qunar.com']
    start_urls = ['https://tuan.qunar.com/vc/index.php?category=all_o&limit=0%2C30','https://tuan.qunar.com/vc/index.php?category=all_i&limit=0%2C30','https://tuan.qunar.com/vc/index.php?category=all_r&limit=0%2C30']

    def parse(self, response):
        result = get_infos(response.text)
        result = result.replace('\\"', '"').replace('\\n', '')
        x_result = Selector(text=result)
        # print(type(x_result))
        li_list = x_result.xpath("//ul[@class='cf']/li/a/@href").extract()
        categoryType = re.findall('.*?category=(.*?_.?)', response.url)[0]
        for li in li_list:
            new_url = 'https:' + li.replace(';', '&').replace('&amp', '')
            # print(new_url)
            yield scrapy.Request(url=new_url, callback=self.parse_info, meta={'type': categoryType})


    def parse_info(self,response):
        # with open('detail.html','w') as files:
        #     files.write(response.text)
            # location.href = '//cxly1.package.qunar.com/user/detail.jsp?id=4059071795&rttp=%E5%87%BA%E5%A2%83%E6%B8%B8&dep=5YyX5Lqs&arr=5pmu5ZCJ5bKbLOazsOWbvSznpZ7ku5nljYrlspss5pmu5ZCJ6ZWHLOeah%2BW4neWymyzluIPlkIks5pmu5ZCJLOW4g%2BWQieWymyzmma7lkInnpZ7ku5nljYrlspss54%2BK55Ga5bKb&ftdt=2018-11-04%2C2018-11-04#vid=qb2c_cxly1&func=6Lef5Zui5ri4&pid=4059071795&rid=27973036&vd=5pil6Zuq5Zu96ZmF5a6Y5pa55peX6Iiw5bqX' + window.location.hash;
        detile_url='https:'+response.xpath('.').re("location.href = '(.*?)'")[0]
        yield scrapy.Request(url=detile_url,callback=self.parse_detile)


    def parse_detile(self,response):
        # print(response.status,'!!!')
        # with open('detail.html', 'w') as files:
        #     files.write(response.text)
        title=response.xpath("//div[@class='summary']/h1/text()").extract()[1].replace('\n','')
        otherinfo=''.join(response.xpath("//div[@class='feature-row']/span/text()").extract()).replace('\uf038','')
        price=response.xpath("//var[@id='js-min-price']/text()").extract()[0]
        #动态获取历史交易量 需从当前请求url获取id，后发起请求获取json
        # https://cxly1.package.qunar.com/user/detail/getStatistics.json?pId=4059071795
        # historysole=response.xpath("//em[@class='sales js-sold-count-tip']/var[@class='js-history-sold']/text()").extract()[0]
        #动态获取评论数量，需获取id，发起请求获取json
        productid=response.xpath("//div[@class='order']/ul/li[1]/span/text()").extract()[0]
        print(productid,'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')







def get_infos(htmls):
    pattern=re.compile(r'<script>pageLoader\({"id":"tuan-list","html":(.*?)}\);</script>',re.S)
    result=re.findall(pattern,htmls)
    return result[0]
