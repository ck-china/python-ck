# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JianBookArc(scrapy.Item):
    arc_type=scrapy.Field()
    title=scrapy.Field()
    content=scrapy.Field()
    pub_time=scrapy.Field()
    font_count=scrapy.Field()
    reads=scrapy.Field()
    argments=scrapy.Field()
    likes=scrapy.Field()
    admirs=scrapy.Field()
    author_name=scrapy.Field()
    aut_fonts=scrapy.Field()
    auth_fans=scrapy.Field()
    auth_likes=scrapy.Field()
    auth_diary=scrapy.Field()
    def colname(self):
        return 'arc_collection'


class JianAdmin(scrapy.Item):
    admin_name=scrapy.Field()
    admin_img=scrapy.Field()
    arc_type=scrapy.Field()
    def colname(self):
        return 'adm_list'
