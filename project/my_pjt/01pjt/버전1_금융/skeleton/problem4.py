import requests
from pprint import pprint

# 문제4. C번의 데이터를 활용하여, 섭씨 온도 데이터를 추가합니다.

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
        '온도 (섭씨)':round(weather_data['main']['temp'] - 273, 2),
        '최고온도':weather_data['main']['temp_max'],
        '최고온도 (섭씨)':round(weather_data['main']['temp_max'] - 273, 2),
        '최저온도':weather_data['main']['temp_min'],
        '최저온도 (섭씨)':round(weather_data['main']['temp_min'] -273, 2),
        '체감온도':weather_data['main']['feels_like'],
        '체감온도 (섭씨)':round(weather_data['main']['feels_like'] -273, 2),
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
