# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#管道文件，一般在这里做数据筛选，和持久化
from scrapy.contrib.pipeline.images import ImagesPipeline
import scrapy
from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings
import os
import pymysql
from testproject.items import book_list,book_info
image_store = get_project_settings().get('IMAGES_STORE')
class getimg(ImagesPipeline):
    def get_media_requests(self, item, info):
        if isinstance(item,book_list):
            imageurl = item['image']
            yield scrapy.Request(imageurl)
        else:
            return item

    def item_completed(self, results, item, info):
        print(results)
        paths = [subdict['path'] for status,subdict in results if status]

        if not paths:
            raise DropItem('图片没有下载，成功')
        else:
            os.rename(image_store+'/'+paths[0],image_store+'/'+item['title']+'.jpg')
            item['localsPath'] = image_store+'/'+item['title']+'.jpg'
        return item
    #需要判断item是哪个类的实例对象   有点没弄明白

class TestprojectPipeline(object):
    def __init__(self, host, user, pwd, db):
        self.client = pymysql.Connect(host, user, pwd, db, charset='utf8')
        self.cursor = self.client.cursor()

    @classmethod
    def from_crawler(cls, crawler):
        host = crawler.settings['MYSQL_HOST']
        user = crawler.settings['MYSQL_USER']
        pwd = crawler.settings['MYSQL_PWD']
        db = crawler.settings['MYSQL_DB']
        return cls(host, user, pwd, db)

    def process_item(self, item, spider):
        data = dict(item)
        sql, parmars = item.insert_db_by_data(data)

        try:
            self.cursor.execute(sql, parmars)
            self.client.commit()
        except Exception as err:
            self.client.rollback()
            print(err)

        return item

    def close_spider(self, spider):

        self.cursor.close()
        self.client.close()


