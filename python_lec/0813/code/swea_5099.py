T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    Ci = [0] + list(map(int, input().split()))

    pan = [0] * N
    new_pizza = 1  # 피자를 빼고 다시 새로 넣는 피자 변수

    while pan:
        pizza = pan.pop(0)   # 피자를 뺀 뒤
        Ci[pizza] //= 2     # 치즈양 계산

        if Ci[pizza] == 0:
            if new_pizza <= M:
                pan.append(new_pizza)
                new_pizza += 1
        else:
            pan.append(pizza)

    print(f'#{test_case} {pizza}')