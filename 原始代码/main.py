import requests
import json
import mysql.connector
from datetime import datetime


# API请求参数
params = {
    'key': 'c4286facf666',
    'num': 10,
    'page': 0,
    'rand': 0,
    'word': 'AI'
}

# 数据库配置
db_config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'database': 'news_python'
}

# 发起API请求
response = requests.get('https://whyta.cn/api/tx/generalnews', params=params)

if response.status_code == 200:
    data = response.json()
    newslist = data['result']['newslist']
    print(newslist)

    # 连接到数据库
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    # 插入数据
    for item in newslist:
        insert_query = """
        INSERT INTO news (id, ctime, title, source, picUrl, description, url)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (
            item['id'],
            item['ctime'],
            item['title'],
            item['source'],
            item['picUrl'],
            item['description'],
            item['url']
        ))
    
    # 提交事务
    conn.commit()
    
    # 关闭连接
    cursor.close()
    conn.close()
else:
    print('API请求失败，状态码：', response.status_code)