def make_sum(pram1, pram2):
    """이것은 두 수를 받아
    두 수의 합을 반환하는 함수입니다.
    >>> make_sum(1, 2)
    3
    """
    return pram1 + pram2

result = make_sum(100, 30)
return_value = print(result) # 130
print(return_value) # None (print함수는 return이 없다는, 반환값이 없다는 의미)
# print는 터미널에 출력을 해 주는 코드일 뿐 값을 리턴해주는 것은 X (리턴과 출력은 다른 개념이라는 것 기억)

def my_func():
    print('hello, world')

result = my_func() # hello, world
# 함수가 호출되어 hello, world가 출력되고 함수 반환값이 없으므로 None이 result로 할당됨
print(result) # None