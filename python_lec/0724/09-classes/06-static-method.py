class StringUtils:
    # 생성자 메서드를 쓰지 않으면 파이썬 내부에서 아래의 형태로 만들어주긴 하나 내용이 없어도 아래와 같이 써놓는 것을 권장
    def __init__(self):
        pass
    
    @staticmethod
    def reverse_string(string):
        return string[::-1]

    @staticmethod
    def capitalize_string(string):
        return string.capitalize()

text = 'hello, world'
result1 = StringUtils.reverse_string(text)
print(result1)
result2 = StringUtils.capitalize_string(text)
print(result2)