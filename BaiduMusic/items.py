# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaidumusicItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #歌手名字
    singer_name = scrapy.Field()
    #歌手介绍
    singer_introduce = scrapy.Field()
    #歌手专辑
    album_name = scrapy.Field()
    #专辑介绍
    album_introduce = scrapy.Field()
    #专辑所属歌曲
    song = scrapy.Field()
    #专辑发行时间
    album_publishtime = scrapy.Field()
    #专辑发行公司
    company = scrapy.Field()


