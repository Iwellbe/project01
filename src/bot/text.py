import mysql.connector
from zhipuai import ZhipuAI

# 连接到数据库
conn = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password ='root',
    database = 'news_python'
)

# 创建一个游标对象
cursor = conn.cursor()

# 执行SQL查询
cursor.execute("SELECT title FROM news WHERE title LIKE '%AI%'")

# 获取查询结果
results = cursor.fetchall()

# 遍历结果并打印
for row in results:
    print(row)

# 关闭游标和连接
cursor.close()
conn.close()


client = ZhipuAI(api_key="021ea599b280e0913385d738fe24712f.AnGPa1vuO8nvGHhU") # 填写您自己的APIKey
response = client.chat.completions.create(
    model="glm-4",  # 填写需要调用的模型名称
    messages=[
        {"role": "user", "content": "作为一名营销专家，请为智谱开放平台创作一个吸引人的slogan"},
        {"role": "assistant", "content": "当然，为了创作一个吸引人的slogan，请告诉我一些关于您产品的信息"},
        {"role": "user", "content": "智谱AI开放平台"},
        {"role": "assistant", "content": "智启未来，谱绘无限一智谱AI，让创新触手可及!"},
        {"role": "user", "content": "创造一个更精准、吸引人的slogan"}
    ],
)
print(response.choices[0].message)

