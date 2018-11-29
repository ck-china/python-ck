# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo



class JishiPipeline(object):
    def open_spider(self,spider):
        self.client=pymongo.MongoClient("127.0.0.1",27017)
        self.db=self.client['baidu']
        self.collection=self.db['lvyou']
        print("开始爬虫")


    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item


    def close_spider(self,spider):
        self.client.close()
        print("爬虫结束")