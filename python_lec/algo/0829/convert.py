# # 1. 라이브러리 이용해 진수 변환
# i = 10
# b = bin(i)
# o = oct(i)
# h = hex(i)
# print(i, b, type(b), o, h)

# # 2.
# j = 0b1010  # j = 10이라고 쓴 것과 동일함
# print(j)

# 3. standard library의 int() 이용해 진수 변환
j = '10'
j_dec = int(j, 10)  # int(j)
j_bin = int(j, 2)   # int쓰고 뒤에 진수를 써주면 해당 진수로 변환되어 출력됨
j_oct = int(j, 8)
j_hex = int(j, 16)
print(j_dec, type(j_dec))
print(j_bin, type(j_bin))
print(j_oct, type(j_oct))
print(j_hex, type(j_hex))

print(int('1010', 2))
print(int('1A', 16))