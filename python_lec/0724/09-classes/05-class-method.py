class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @classmethod
    def number_of_population(cls):
        print(f'인구수는 {cls.count}입니다.')
        print(f'인구수는 {Person.count}입니다.') # 상속으로 인해 하위클래스가 생성될 수 있는데 하위 클래스가 number_of_population을 가져다 쓸 수 있는데 자식 클래스가 number_of_population을 제대로 못 씀


person1 = Person('iu')
person2 = Person('BTS')

Person.number_of_population()