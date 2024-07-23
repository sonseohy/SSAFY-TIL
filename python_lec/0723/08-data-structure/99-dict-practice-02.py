# 딕셔너리를 입력받아 value와 key를 뒤집은 결과를 반환하는 함수 `dict_invert()`를 작성하기


# 1. [] 표기법을 사용한 방법
def dict_invert(input_dict):
    result = {}
    for k, v in input_dict.items():
        if v in result:
           result[v].append(k)
        else:
            result[v] = [k]
    return result

# 2. get 메서드를 사용한 방법
def dict_invert(input_dict):
    result = {}
    for k, v in input_dict.items():
        result[v] = result.get(v, []) + [k]

    return result


# # 3. setdefault 메서드를 사용한 방법
def dict_invert(input_dict):
    result = {}
    for k, v in input_dict.items():
        result.setdefault(v, [])
        result[v] = result.get(v) + [k]
        # ver2 : new_dict.setdefault(v, []).append(k)
        # result[v] = result.setdefault(v, []) + [k]도 가능은 함, 위 코드가 제 역할의 코드

    return result


print(dict_invert({1: 10, 2: 20, 3: 30}))  # {10: [1], 20: [2], 30: [3]}
print(
    dict_invert({1: 10, 2: 20, 3: 30, 4: 30})
)  # {10: [1], 20: [2], 30: [3, 4]}
print(dict_invert({1: True, 2: True, 3: True}))  # {True: [1, 2, 3]}
