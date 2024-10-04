# requests 모듈은 정적인 부분만 다운로드 가능
# 정적이다? 서버가 이미 가지고 있는 데이터만
# 따라서 동적인 컨텐츠를 다운로드 받을 수 없다
# (탕수육이라는 결과를 통해서 변경되는 부분)
# 그럼 어떡해?
# 동적인 컨텐츠를 받을 수 있는 방법 : selenium
# selenium : 개발자들이 동적 웹 테스트를 위해서 많이 사용

from bs4 import BeautifulSoup
import requests

def crawling_basic():
    # 가져올 url 문자열로 입력
    url = 'https://www.google.com/search?q=%ED%83%95%EC%88%98%EC%9C%A1&oq=%ED%83%95%EC%88%98%EC%9C%A1&gs_lcrp=EgZjaHJvbWUqEAgAEAAYgwEY4wIYsQMYgAQyEAgAEAAYgwEY4wIYsQMYgAQyDQgBEC4YgwEYsQMYgAQyBwgCEAAYgAQyBwgDEAAYgAQyBwgEEAAYgAQyBwgFEAAYgAQyBwgGEAAYgAQyBwgHEAAYgAQyBwgIEAAYgAQyBwgJEAAYgATSAQgxNzQ1ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8'  

    # requests의 get함수를 이용해 해당 url로 부터 html이 담긴 자료를 받아옴
    response = requests.get(url)

    # 우리가 얻고자 하는 html 문서가 여기에 담기게 됨
    html_text = response.text

    print(html_text)

    with open('soup.txt', 'w', encoding='utf-8') as file:
        file.write(html_text)
        
crawling_basic()
