import json
from pprint import pprint


def book_info(book):
    pass
    # 여기에 코드를 작성합니다.
    new_dict =  {}
    info = ['id', 'title', 'author', 'priceSales', 'description', 'cover', 'categoryId']
    for key in info:
        new_dict[key] = book[key] 
    return new_dict


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    pprint(book_info(book))
