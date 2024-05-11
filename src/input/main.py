from api_request import get_news
from db_operations import insert_news

def main():
    newslist = get_news()
    if newslist:
        insert_news(newslist)

if __name__ == "__main__":
    main()
