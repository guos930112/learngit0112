# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import pymongo
# from fake_useragent import UserAgent
from datetime import datetime
class ExamplePipeline(object):
    def process_item(self,item,spider):
        item['crawled']=datetime.utcnow() #爬取的时间
        item['spider']=spider.name+'_windows_' #爬虫的名称，#mycrawler_redis
        # "crawled": "2018-12-21 12:59:57", "spider": "sina1_windows_"
        return item
class SinaPipeline(object):
    def open_spider(self,spider):
        self.file=open('新浪.json','w',encoding='utf-8')
    def close_spider(self,spider):
        self.file.close()
    def process_item(self, item, spider):
        tiezi_url = item['tiezi_url']
        # http://eladies.sina.com.cn/beauty/chanpinku/magic/23731.shtml
        # -> sports_sina_com_cn_basketball_cba_2018-12-20_doc-ihmutuee1161116.txt
        tiezi_save_name = tiezi_url[7:tiezi_url.rfind('.')].replace('.','_').replace('/','_')+'.txt'
        # print('tiezi_save_name==============',tiezi_save_name)
        tiezi_path = item['save_path']+'/'+tiezi_save_name
        item['tiezi_path']=tiezi_path
        with open(tiezi_path,'w',encoding='utf-8') as f:
            f.write(item['tiezi_content'])
        self.file.write(json.dumps((dict(item)),ensure_ascii=False)+'\n')
        return item
# 把数据存入Mongodb中，这个管道文件一定要在settings中配置上不然mongodb中没有数据--->count()
class SinaMongodbPipeline(object):
    def open_spider(self,response):
        self.client = pymongo.MongoClient(host='127.0.0.1',port=27017)
        db_name = self.client['Sina']
        self.sheet_name = db_name['sina_items']
    def close_spider(self,spider):
        self.client.close()
    def process_item(self,item,spider):
        item_dict = dict(item)
        self.sheet_name.insert(item_dict)
        return item

