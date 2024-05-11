import mysql.connector
from config import DB_CONFIG

def connect_to_db():
    return mysql.connector.connect(**DB_CONFIG)

def insert_news(newslist):
    conn = connect_to_db()
    cursor = conn.cursor()
    
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
    
    conn.commit()
    cursor.close()
    conn.close()
