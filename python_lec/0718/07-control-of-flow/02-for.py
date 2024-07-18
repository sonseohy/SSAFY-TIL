items = ['apple', 'banana', 'coconut']

for item in items:
    print(item)


country = 'Korea'

for char in country:
    print(char)


for i in range(5):
    print(i)

print(range(5)) # range(0, 5)
print(list(range(5))) # for문에 list를 붙여도 상관 없으나 굳이 바꿀 필요는 없음


my_dict = {
    'x': 10,
    'y': 20,
    'z': 30,
}

for key in my_dict:
    print(key) # 기본적으로 dict를 순환하면 key 값이 출력됨
    print(my_dict[key])


numbers = [4, 6, 10, -8, 5]

for i in range(len(numbers)):
    numbers[i] *= 2

print(numbers)


outers = ['A', 'B']
inners = ['c', 'd']

for outer in outers:
    for inner in inners:
        print(outer, inner)


elements = [['A', 'B'], ['c', 'd']]

for elem in elements:
    for item in elem:
        print(item)