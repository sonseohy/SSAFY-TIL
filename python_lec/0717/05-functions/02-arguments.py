# 1. Positional Arguments
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet('Marry', 20)
greet(20, 'Marry') 
# greet('Marry') : TypeError : 요구하는 위치인자 1개가 빠짐


# 2. Default Argument Values
def greet(name, age=20):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet('Bob')
greet('Charlie', 40)


# 3. Keyword Arguments
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet(name='Dave', age=35)
greet(age=35, name='Dave')
# greet(age=35, 'Dave')  #  positional argument follows keyword argument


# 4. Arbitrary Argument Lists
def calc_sum(*args):
    print(args)
    print(type(args))

calc_sum(1, 100, 5000, 30)

def calc_sum(params, *args): # 위치인자와 함께 사용하려면 임의의 인자 앞에 써줘야함, (*args, params)는 안됨
    print(args)
    print(type(args))

calc_sum(1, 100, 5000, 30) # 튜플로 묶이는 값은 1을 제외한 (100, 5000, 30)


# 5. Arbitrary Keyword Argument Lists
def print_info(**kwargs):
    print(kwargs)

print_info(name='Eve', age=30) # 임의의 키워드 인자이므로 값을 넣어줄 때도 키워드 인자 방식으로 넣어줌


# 인자의 모든 종류를 적용한 예시
def func(pos1, pos2, default_arg='default', *args, **kwargs):
    print('pos1:', pos1)
    print('pos2:', pos2)
    print('default_arg:', default_arg)
    print('args:', args)
    print('kwargs:', kwargs)


func(1, 2, 3, 4, 5, 6, key1='value1', key2='value2')
