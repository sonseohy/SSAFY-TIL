T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    cards = list(input().split())

    # 카드를 절반으로 나누어 분류
    # 홀수일 경우 먼저 놓는 카드 c1에 한장이 더 들어가야 하므로 나머지 값을 더해줌
    # ex. N = 7이면 c1은 0 ~ 3까지 4장의 카드, c2는 4 ~ 6까지 3장의 카드가 분류됨
    c1 = cards[:N//2 + N%2]
    c2 = cards[N//2 + N%2:]

    result = []
    for i in range(N//2):       # N // 2의 길이만큼 반복하여 c1과 c2를 pop해 result 리스트에 append
        result.append(c1.pop(0))
        result.append(c2.pop(0))
    if len(c1) != 0:    # 홀수의 경우 c1의 카드 갯수가 많으므로 c1에 카드가 남아있을때 추가로 append
        result.append(c1.pop(0))

    print(f'#{test_case}', *result)

# # test-case 일부 fail
# T = int(input())
#
# for test_case in range(1, T + 1):
#     N = int(input())
#     cards = list(input().split())
#
#     shuffle_cards = cards[N//2 + N%2:]
#
#     for i in range(len(cards)-1, 0, -1):
#         if i % 2 == 0:
#             for k in range(N//2 + N%2):
#                 cards[i] = cards[k]
#                 print(i, cards[k])
#         else:
#             for k in range(N//2):
#                 cards[i] = shuffle_cards.pop()
#                 break
#
#     print(f'#{test_case}', *cards)
