# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json,scrapy
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings
import pymongo
# import
#自定义图片下载管道
image_store = get_project_settings().get('IMAGES_STORE')
class JobboleImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        #获取图片地址，发起请求
        imageurl=item['coverImageUrl']
        yield scrapy.Request(imageurl)

    def item_completed(self, results, item, info):
        print(results)
        """
        [(True|False,{'url':'图片地址','path':'本地存储路径','checksum':'一个串'}]
        """
        path=[subdict['path'] for status,subdict in results if status]
        if not path:
            #如果图片没下载成功，丢弃
            raise DropItem("图片没有下载成功")
        else:
            print("下载成功")
            item['localImagePath']=image_store+path[0]

        #将item传递给下一个管道
        return item

class JobboleprojectPipeline(object):
    def __init__(self):
        self.file=open('data.json','a')



    def process_item(self, item, spider):
        # 可以在这里执行数据持久化
        # with open('data.json', 'w') as file:
        #     json_data = json.dumps(dict(item),ensure_ascii=False)
        #     file.write((json_data+'\n'))

        json_data = json.dumps(dict(item), ensure_ascii=False)
        self.file.write(json_data+'\n')
        #如果有多个管道，并且有优先级顺序
        #一定要return item，否则，下一个管道无法接收item
        return item
    def open_spider(self,spider):
        '''
        在爬虫开始的时候调用一次，为可选方法
        '''
        print(spider.name,'爬虫开始')
    def close_spider(self,spider):
        '''
        在爬虫结束的时候调用一次，为可选方法

        '''
        self.file.close()
        print((spider.name,'爬虫结束'))
class JobboleprojectPipelinetwo(object):
    def __init__(self):
        self.client=pymysql.connect()
    def process_item(self, item, spider):
        return item

