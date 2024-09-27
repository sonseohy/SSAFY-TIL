import requests
from pprint import pprint

# 문제3. B번에서 얻는 결과를 활용하여, KEY 값들을 한글로 변경한 딕셔너리를 반환하도록 구성합니다.
# KEY 에 해당하는 한글 KEY 값들은 다음과 같습니다.
    # feels_like : '체감온도',
    # humidity : '습도',
    # pressure : '기압',
    # temp : '온도',
    # temp_max : '최고온도',
    # temp_min : '최저온도',
    # description : '요약',
    # icon : '아이콘',
    # main : '핵심’
    # id : ‘식별자’

def get_weather(api_key):
    city = "Seoul,KR"
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    # 요구사항에 맞도록 이곳의 코드를 수정합니다.
   
    weather_data = requests.get(url).json()
    result = {}
    main_dict = {}
    weather_dict = {}

    main_dict={
        '온도':weather_data['main']['temp'],
        '최고온도':weather_data['main']['temp_max'],
        '최저온도':weather_data['main']['temp_min'],
        '체감온도':weather_data['main']['feels_like'],
        '습도':weather_data['main']['humidity'],
        '기압':weather_data['main']['pressure']
        }
    weather_dict={
        '식별자':weather_data['weather'][0]['id'],
        '아이콘':weather_data['weather'][0]['icon'],
        '요약':weather_data['weather'][0]['description'],
        '핵심':weather_data['weather'][0]['main']
    }

    result = {'기본':main_dict, '날씨':[weather_dict]}

    return result


# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # 여러분의 OpenWeatherMap API 키를 설정하세요
    api_key = '898b69758d9c650d6704b8d28ee6f81c'

    result = get_weather(api_key)
    pprint(result)
