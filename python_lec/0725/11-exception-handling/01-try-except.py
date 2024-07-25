# try-except
try:
    result = 10 / 0
except ZeroDivisionError: # ZeroDivisionError 쓰지 않아도 실행됨 (모든 예외처리에 대해 반응함)
    print('0으로 나눌 수 없습니다.')

try:
    num = int(input('숫자입력 : '))
except ValueError:
    print('숫자가 아닙니다.')

# 복수 예외처리
try:
    num = int(input('100을 나눌 값을 입력하시오 : '))
    print(100 / num)
except (ValueError, ZeroDivisionError):
    print('제대로 입력하지 않았습니다.')
    

try:
    num = int(input('100을 나눌 값을 입력하시오 : '))
    print(100 / num)
except ValueError:
    print('숫자를 입력하세요')
except ZeroDivisionError:
    print('0으로는 나눌 수 없습니다.')
except: # Value, ZeroDivision Error 외의 에러가 발생했을 때
    print('알 수 없는 에러가 발생했습니다.')