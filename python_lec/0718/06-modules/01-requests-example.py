import requests

url = 'https://random-data-api.com/api/v2/users'
response = requests.get(url).json() # 요청 보내고 데이터 받고 받은 데이터 정리까지 해주는 코드

print(response)
