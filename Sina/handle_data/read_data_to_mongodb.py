import redis
import pymongo
import json
import time
# 读取redis数据库的数据
# 写入到mongodb数据库中，写入的时候要是字段
redis_client = redis.StrictRedis(host='192.168.18.53',port=6379,db=0)
mongodb_client = pymongo.MongoClient(host='localhost',port=27017)
#创建mongodb数据库
db_name=mongodb_client['sina']
#创建表
sheet_name=db_name['sina_items']
while True:
    # time.sleep(1)
    # blpop 先进入先被取出
    source,data = redis_client.blpop(['sina1:items']) # sina1:items和redis中键的名字一样，取出来的是元组
    # print('source=========',source) # source========= b'sina1:items'
    # print('data=========',data)
    # print(type(data)) # <class 'bytes'>
    # 把data转换成字典
    dict_data = json.loads(data.decode('utf-8'),encoding='utf-8')
    print(type(dict_data))  # <class 'dict'>
    # 插入的是字典,因为mongodb中就是以键值对的形式存在的
    sheet_name.insert(dict_data)

