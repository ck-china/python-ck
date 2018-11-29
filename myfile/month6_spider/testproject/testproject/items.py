# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
#类似于django的models,我们一班在这里定义字段

class TestprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class book_list(scrapy.Item):
    title=scrapy.Field()
    image=scrapy.Field()
    pingfen=scrapy.Field()
    tages=scrapy.Field()
    content=scrapy.Field()
    localsPath=scrapy.Field()

    def insert_db_by_data(self, subdict):
        sql, data = sql_info(subdict, 'book_list')

        return sql, data


class book_info(scrapy.Item):
    chapter_title=scrapy.Field()
    book_name=scrapy.Field()
    font_count=scrapy.Field()
    pub_time=scrapy.Field()
    content=scrapy.Field()

    def insert_db_by_data(self, subdict):
        sql, data = sql_info(subdict, 'capter')

        return sql, data

def sql_info(subdict,tablename):

    sql = """
                INSERT INTO %s(%s)
                VALUES (%s)
                """ % (tablename,','.join(subdict.keys()), ','.join(['%s'] * len(subdict)))

    data = [value for value, key in subdict.items()]

    return sql,data