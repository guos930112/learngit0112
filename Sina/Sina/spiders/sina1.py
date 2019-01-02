# -*- coding: utf-8 -*-
import scrapy
import os
#分布式的基本爬虫
from scrapy_redis.spiders import RedisSpider

from Sina.items import SinaItem

class Sina1Spider(RedisSpider):
    # 爬虫的名称，用于运行爬虫的：scrapy crawl sina1
    name = 'sina1'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide/']
    # 没有起始路径，靠redis_key对应的值存的是起始路径，在redis数据库中
    redis_key = 'Sina1Spider:start_urls'
    # lpush Sina1Spider:start_urls http://news.sina.com.cn/guide/
    def parse(self, response):
        url = response.url
        print('url=============',url)
        parent_titles = response.xpath('//div[@id="tab01"]/div/h3/a/text()').extract() # //div[@id="tab01"]/div/h3/a/text()
        parent_urls = response.xpath('//div[@id="tab01"]/div/h3/a/@href').extract() # //div[@id="tab01"]/div/h3/a/@href
        sub_titles = response.xpath('//div[@id="tab01"]/div/ul[@class="list01"]/li/a/text()').extract() # //div[@id="tab01"]/div/ul/li/a/text()
        sub_urls = response.xpath('//div[@id="tab01"]/div/ul[@class="list01"]/li/a/@href').extract() # //div[@id="tab01"]/div/ul/li/a/@href
        print(parent_titles)
        for i in range(len(parent_titles)):
            parent_title = parent_titles[i]
            parent_url = parent_urls[i]
            for j in range(len(sub_titles)):
                sub_title = sub_titles[j]
                sub_url = sub_urls[j]
                # print('sub_url=============',sub_url) # http://news.sina.com.cn/china/
                # print('parent_url=============',parent_url) # http://news.sina.com.cn/
                if sub_url.startswith(parent_url):
                    path = './data/'+parent_title+'/'+sub_title
                    if not os.path.exists(path):
                        os.makedirs(path)
                    item = SinaItem()
                    item['parent_title'] = parent_title
                    item['parent_url'] = parent_url
                    item['sub_title'] = sub_title
                    item['sub_url'] = sub_url
                    item['save_path'] = path
                    yield scrapy.Request(sub_url,callback=self.second_parse,meta={'item':item})
    def second_parse(self,response):
        # tiezi_url = response.url
        # print('tiezi_url============',tiezi_url)
        item = response.meta['item']
        links = response.xpath('//a/@href').extract()
        for link in links:
            if link.startswith(item['parent_url']) and link.endswith('.shtml'):
                print('link======', link)
                yield scrapy.Request(link,callback=self.third_parse,meta={'item':item})
    def third_parse(self,response):
        item = response.meta['item']
        tiezi_title = response.xpath('//h1[@class="main-title"]/text()|//h1[@id="artibodyTitle"]/text()').extract()
        tiezi_content = response.xpath('//div[@id="article"]/p/text()|//div[@id="artibody"]/p/text()').extract()
        if tiezi_title:
            tiezi_title = ' '.join(tiezi_title)
        if tiezi_content:
            tiezi_content = ' '.join(tiezi_content)
        if len(tiezi_title)>0 and len(tiezi_content)>0:
            item['tiezi_title']=tiezi_title
            item['tiezi_content']=tiezi_content
            item['tiezi_url'] = response.url
            yield item




