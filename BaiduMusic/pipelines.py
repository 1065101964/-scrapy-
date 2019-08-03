# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from .settings import *

class BaidumusicPipeline(object):
    def process_item(self, item, spider):
        print(dict(item))
        return item

'''将数据存入MongoDB数据库'''
class MongoPipeline(object):
    def __init__(self):
        '''创建三个对象'''
        self.conn = pymongo.MongoClient(
            M0NGON_HOST,
            MONGON_PORT
        )
        self.db = self.conn[M0NGON_DB]
        self.myset = self.db[MONGON_SET]

    def process_item(self,item,spider):
        self.myset.insert_one(dict(item))
        return item

    '''爬虫程序结束时执行的函数'''
    def close_spider(self,spider):
        print('执行了close_spider函数')

