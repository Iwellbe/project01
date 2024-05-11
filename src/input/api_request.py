import requests
import json
from config import API_PARAMS


def get_news():
    response = requests.get('https://whyta.cn/api/tx/generalnews', params=API_PARAMS)
    if response.status_code == 200:
        return response.json()['result']['newslist']
    else:
        print('API请求失败，状态码：', response.status_code)
        return None
