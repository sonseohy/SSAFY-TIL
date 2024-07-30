# 할당
# 가변 데이터
a = [1, 2, 3, 4]
b = a
b[0] = 100

print(a)
print(b)

# 불변 데이터 : 불변의 값은 재할당이 이루어짐
a = 20
b = a
b = 10 # 재할당

print(a)
print(b)

# 얕은 복사
a = [1, 2, 3]
b = a[:]
c = a.copy()

b[0] = 100
c[0] = 999
print(a)
print(b)
print(c)

# 얕은 복사의 한계
a = [1, 2, [3, 4, 5]]
b = a[:]

b[0] = 999
b[2][1] = 100

print(a)   # [1, 2, [3, 100, 5]]
print(b)   # [999, 2, [3, 100, 5]]

# 깊은 복사
import copy

a = [1, 2, [3, 4, 5]]
b = copy.deepcopy(a)

b[2][1] = 100

print(a)
print(b)