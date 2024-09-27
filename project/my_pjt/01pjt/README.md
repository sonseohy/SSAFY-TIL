### dictionary에서 key 불러오는 함수
- 딕셔너리가 자체적으로 가지고 있는 함수 중 키를 불러오는 함수는 keys()
- a가 딕셔너리라고 할 때, a.keys()는 딕셔너리 a의 key만을 모아 dict_keys 객체를 리턴한다.

### API 요청을 받아 json 파일로 출력하는 코드
- resquests.get(url).json()

### 1_금융/skeleton : problem3 KEY 값들을 한글로 변경한 딕셔너리를 반환
- for문을 사용해 main과 weather 값에 저장된 딕셔너리의 키 값을 key_kor_2 딕셔너리를 사용해 변경하고 싶었으나 실패 : 코드 실행 시 key Error발생 (temp)
```python
def get_weather(api_key):
    city = "Seoul,KR"
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    # 요구사항에 맞도록 이곳의 코드를 수정합니다.

    key_kor_1 = {
        'main' : '기본',
        'weather' : '날씨'
    }
    key_kor_2 = {
        'feels_like' : '체감온도',
        'humidity' : '습도',
        'pressure' : '기압',
        'temp' : '온도',
        'temp_max' : '최고온도',
        'temp_min' : '최저온도',
        'description' : '요약',
        'icon' : '아이콘',
        'main' : '핵심',
        'id' : '식별자',
        'grnd_level' :'지면 기압',
        'sea_level' : '해수면 기압',
    }

    weather_data = requests.get(url).json()
    dict_keys = weather_data.keys()
    result_1 = {}
    result_2 = {}

    for key in dict_keys:
        if key == 'main' or key == 'weather':
            if key in key_kor_1:
                result_1[key_kor_1[key]] = weather_data[key]

    for k in result_1['기본']:
        if k in key_kor_2:
            result_2[key_kor_2[k]] = result_1[k]
    print(result_2)
```
- key_kor_1 : 출력한 첫번재 딕셔너리의 키 값 (main, weather)의 한국어 뜻이 담김
- key_kor_2 : 출력한 첫번재 딕셔너리 main, weather 안에 담긴 딕셔너리들의 한국어 뜻이 담김

### 출력 결과를 txt파일로 확인하는 방법
- $ python (파일명).py > (텍스트파일명).txt
- 출력 결과가 너무 길거나 한글이 깨져보일 때 사용해서 출력 결과 확인
