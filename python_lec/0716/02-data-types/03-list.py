my_list_1 = []
my_list_2 = [1, 'a', 3, 'b', 5]
my_list_3 = [1, 2, 3, 'Python', ['hello', 'world', '!!!']]
my_list = [1, 'a', 3, 'b', 5]

# 인덱싱
print(my_list[1])  # a

# 슬라이싱
print(my_list[2:4])  # [3, 'b']
print(my_list[:3])  # [1, 'a', 3]
print(my_list[3:])  # ['b', 5]
print(my_list[0:5:2])  # [1, 3, 5]
print(my_list[::-1])  # [5, 'b', 3, 'a', 1]

# 길이
print(len(my_list))  # 5

# 중첩된 리스트
my_list = [1, 2, 3, ['python', 'hello', 100]]
print(len(my_list)) # 4
print(my_list[3][1]) # 'hello'
print(my_list[3][1][-1]) # 'o'
print(len(my_list[3])) # 내부 리스트의 개수 세는 방법

# 리스트는 가변
my_list = [1, 2, 3]
my_list[0] = 100 # 0번째 요소를 100으로 바꿈
print(my_list)