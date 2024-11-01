pip install django-environ
API_key 등의 중요 정보는 .env 파일에 따로 빼주기

project 폴더의 settings.py에
import os
import environ
env = environ.Env(DEBUG=(bool, True)) # 앞으로 환경변수 env는 우리가 작성한 파일로 사용하겠다
environ.Env.read_env(env_file=os.path.join(BASE_DIR, '.env')) # env 파일 경로 설정
API_KEY = env('API_KEY')    # .env 파일에 작성된 API_KEY 값을 API_KEY 변수에 대입
.env 파일에 API_KEY='' 작성 시 띄어쓰기 하면 안됨