class Person:
    def __init__(self, name):
        # 왼쪽 name : 인스턴스 변수 name
        # 오른쪽 name : 함수(생성자 메서드)의 매개변수 이름 (들어오는 인자 값)
        self.name = name
        print('인스턴스가 생성되었습니다.')

    def greeting(self):
        print(f'안녕하세요 {self.name}입니다.')

person1 = Person('지민') # 생성자 메서드에 초기값(name)이 설정되어 있으면 반드시 작성해줘야 생성됨
person1.greeting() # 내부적으로는 Person.greeting(person1)
