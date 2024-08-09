def powerset(k, middle_sum): # middle_sum 합이 10이 넘어가면 밑의 가지는 계산하지 않기 위해 중간까지의 합을 밑으로 내려주어 10이 넘는지 안넘는지 확인
    if k == N:
        #print(c)    # 각각의 값이 정해졌을때(그래프의 가장 밑에 도달했을때) 출력해야함 (함수 밖이나 함수 끝에서 출력하는 것 의미 없음)
        # sumV = 0
        # for i in range(N):
        #     if c[i]:
        #         sumV += numbers[i]
        if middle_sum == 10:
            for i in range(N):
                if c[i]:
                    print(numbers[i], end=' ')
            print()

        return      # return을 써 주어야 함, return을 쓰고 싶지않으면 if-else로

    if middle_sum > 10:
        return

    c[k] = 1
    powerset(k+1, middle_sum + numbers[k]) # 포함안되는 얘들의 합을 내는 방법 powerset(k+1, middle_sum + numbers[k] , notS)
    c[k] = 0
    powerset(k+1, middle_sum) # powerset(k+1, middle_sum, numbers[k]+notS)

    '''
    c[k] = 0
    powerset(k+1)
    c[k] = 1
    powerset(k+1)
    
    # 이미 합이 10이 넘는 가지는 계산할 필요 없음
    # 따라서 다 1로 채우고 하나씩 빼면서 하는게 효율적
    # 1과 0의 숫자를 바꾸는 것 만으로도 효율 up
    c[k] = 1
    powerset(k+1)
    c[k] = 0
    powerset(k+1)
    '''


N = 10
numbers = [1, 2 ,3, 4, 5, 6, 7, 8, 9, 10]
c = [-1] * N
powerset(0, 0)