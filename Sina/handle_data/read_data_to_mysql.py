import redis
import time
import json
# 导入模块
import pymysql
#下载安装pip install pymysql
# 以下操作前提：有一个MySQL数据库，并且已经启动；有可以连接该数据库的用户名和密码
# 有一个有权限操作的database
# 创建连接
redis_client = redis.StrictRedis(host='192.168.18.53',port=6379)
conn = pymysql.Connection(host='localhost',port=3306,user='root',password='root',database='sina',charset='utf8')
#创建游标
cursor = conn.cursor()
while True:
    #blpop 先进入先被取出
    source,data = redis_client.blpop(['sina1:items'])
    #把data转换成字典
    item = json.loads(data.decode('utf-8'),encoding='utf-8')
    #插入的是字典
    params = (item['parent_url'],item['parent_title'],item['sub_title'],item['sub_url'],
              item['save_path'],item['tiezi_url'],item['tiezi_title'],item['tiezi_content'],
              item['crawled'],item['spider'])
    print(params)
    #要执行的SQL语句,使用execute方法执行SQL INSERT语句
    sql="INSERT INTO sina_items(parent_url,parent_title,sub_title,sub_url,save_path,tiezi_url,tiezi_title,tiezi_content,crawled,spider) VALUES ('%s', '%s', '%s', '%s', '%s','%s','%s','%s','%s','%s')" % params
    print(sql)
    cursor.execute(sql)
    # # 将数据提交到数据库，否则数据就没有添加到表中
    conn.commit()
# #关闭游标
# cursor.close()
# #断开连接
# conn.close()
# 判断帖子链接是否有重复的sql语句
# select tiezi_url,count(*) as count from sina_items group by tiezi_url having count>1;