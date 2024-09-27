import json
from pprint import pprint


def book_info(book, categories):
    pass
    # 여기에 코드를 작성합니다.
    new_dict =  {}
    info = ['id', 'title', 'author', 'priceSales', 'description', 'cover', 'categoryId']
    for key in info:
        new_dict[key] = book[key]

    lst = []
    for num in new_dict['categoryId']:
        for c in categories:
            if num == c['id']:
                lst.append(c['name'])
    new_dict['categoryName'] = lst
    new_dict.pop('categoryId')
    return new_dict


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(book_info(book, categories_list))
