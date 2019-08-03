# -*- coding: utf-8 -*-
import scrapy
import re
import random
import json
import time
from ..items import BaidumusicItem

class BaidumusicSpider(scrapy.Spider):
    name = 'baidumusic'
    allowed_domains = ['music.taihe.com']
    start_urls = ['http://music.taihe.com/artist']

    '''自定义地址'''
    host = 'http://music.taihe.com'

    def parse(self, response):
        '''获取所有歌手的名字，以及对应的歌手页面链接'''
        singer_names = response.xpath('//div[@class="main-body "]/ul/li[position()>1]/ul/li/a/@title').extract()
        singer_links = response.xpath('//div[@class="main-body "]/ul/li[position()>1]/ul/li/a/@href').extract()
        for name ,link in zip(singer_names,singer_links):
            item = BaidumusicItem()
            item['singer_name'] = name
            url = self.host + link
            yield scrapy.Request(
                url,
                meta={'item':item},
                callback=self.parse_singer
            )

    '''@staticmethod 静态方法只是名义上归属类管理，但是不能使用类变量和实例变量，是类的工具包放在函数前（该函数不传入self或者cls），所以不能访问类属性和实例属性
        random.random()方法返回一个随机数，其在0至1的范围之内'''
    @staticmethod
    def _r():
        return str(random.random())

    '''解析每一个歌手页面'''
    def parse_singer(self,response):
        item = response.meta['item']
        '''歌手简介'''
        if response.xpath('//div[@class="artist-detail-box fl"]/p[@class="introduce"]/span[@class="words overdd"]/text()') != []:
            item['singer_introduce'] = response.xpath('//div[@class="artist-detail-box fl"]/p[@class="introduce"]/span[@class="words overdd"]/text()').extract_first().replace(' ','')
        else:
            item['singer_introduce'] = 'null'

        '''获取歌手的所有专辑'''
        '''歌手的id'''
        id = response.url.strip('/').rsplit('/',1)[1]
        # url = 'http://music.taihe.com/data/user/getalbums?\start={}&size=12&ting_uid={}&order=time\&.r={}'
        '''专辑总数:
        先获取page-navigator-hook(page-navigator page-navigator-new)括号内容时有时无有
        pageNavigator:{ 'total':30, 'size':12, 'start':0, 'show_total':0, 'focus_neighbor':0 } }
        再用正则表达式匹配'''
        html = response.xpath('//div[@class="page_navigator-box"]/div/@class').extract()[1]
        total = re.compile("page.*?pageNavigator:{ 'total':(.*?),.*?}",re.S).findall(html)[0]
        ''' 判断该歌手是否发行过专辑'''
        if int(total) == 0:
            print("该歌手没有发行过专辑")
            yield item
        elif int(total) <= 12:
            url = 'http://music.taihe.com/data/user/getalbums?start=0&size=12&ting_uid={}&order=time&.r={}'.format(id,self._r())
            yield scrapy.Request(
                url,
                meta={'item':item},
                callback=self.get_album
            )
        else:
            for start in range(0,int(total),12):
                url = 'http://music.taihe.com/data/user/getalbums?start={}&size=12&ting_uid={}&order=time\&.r={}'.format(start,id,self._r())
                yield scrapy.Request(
                    url,
                    meta={'item':item},
                    callback=self.get_album
                )

    '''获取该歌手的每一张专辑'''
    def get_album(self,response):
        time.sleep(0.2)
        item = response.meta['item']
        json_html = json.loads(response.text)
        html = json_html['data']['html']
        '''获取的是一个类似于html的一个含有很多标签的字符串，利用xpath或者正则表达式匹配出字符串中的专辑的信息'''
        p = re.compile('<div class="album-name overdd">.*?<a href="(.*?)".*?>(.*?)</a>.*?<span class="publishtime">(.*?)</span>',re.S)
        albums_info = p.findall(html)
        '''获取每张专辑的链接，专辑名称，专辑发行时间'''
        for album_info in albums_info:
            ''' album_link = /album/602125378 '''
            item = item.copy()
            album_link = album_info[0].strip()
            item['album_name'] = album_info[1].strip()
            item['album_publishtime'] = album_info[2].strip()
            url = self.host + album_link
            yield scrapy.Request(
                url,
                meta={'item':item},
                callback=self.parse_album
            )

    '''解析每一张专辑'''
    def parse_album(self,response):
        item = response.meta['item']
        '''专辑发行公司'''
        if response.xpath('//div[@class="base-info-cont"]/ul[@class="c6"]/li[3]/text()') != []:
            item['company'] = response.xpath('//div[@class="base-info-cont"]/ul[@class="c6"]/li[3]/text()').extract_first()[5:]
        else:
            item['company'] = 'null'
        '''专辑介绍'''
        if response.xpath('//div[@class="base-info-cont"]/ul/li[@class="pr album-desc-box"]/p/span[@class="description"]/text()').extract_first() != '该专辑暂时没有介绍，我们正在努力填充':
            item['album_introduce'] = response.xpath('//div[@class="base-info-cont"]/ul/li[@class="pr album-desc-box"]/p/span[@class="description"]/text()').extract_first()
        else:
            item['album_introduce'] = 'null'
        song_list = response.xpath('//div[@class="song-list-wrap"]/ul//li/div[@class="songlist-inline songlist-title"]/span/a/@title').extract()
        for song in song_list:
            item=item.copy()
            item['song'] = song
            yield item


