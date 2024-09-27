import requests
from pprint import pprint

def get_author_books():
    # 여기에 코드를 작성합니다.
    URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'
    api_key = 'ttbbbodong2231550001'

    params = {
        'ttbkey': api_key,
        'Query' : '파울로 코엘료',
        'QueryType': 'Author',
        'MaxResults': 20,
        'start': 1,
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101'
    }
    
    response = requests.get(URL, params=params).json()
    lst = []
    for book in response.get('item'):
        lst.append(book['title'])
    return lst



# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(get_author_books())
