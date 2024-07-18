# import my_math
# # from my_math import add (from절 이용해서 작성)

# print(my_math.add(1, 2))
# # print(add(1, 2))

from my_package.math import my_math # my_package 안에 math 서브 패키지 안의 my_math 모듈을 불러옴
from my_package.statistics import tools

print(my_math.add(3, 4))
print(tools.mod(1, 2))
