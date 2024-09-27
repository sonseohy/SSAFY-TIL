import json
from pprint import pprint

def books_info(books, categories):
    # 여기에 코드를 작성합니다.
    new_dict =  {}
    lst = []
    books_info = []

    for book in books:
        info = ['author', 'categoryId', 'cover', 'description', 'id', 'priceSales', 'title']
        for key in info:
            new_dict[key] = book[key]
        
        lst.append(new_dict)

        for info in lst:
            c_id = []
            for d in info['categoryId']:
                for c in categories:
                    if d == c['id']:
                        c_id.append(c['name'])
            new_dict['categoryName'] = c_id
        new_dict.pop('categoryId')
        books_info.append(new_dict.copy())

    return books_info


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(books_info(books, categories_list))
