# super 사용 전
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email


class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        self.name = name
        self.age = age
        self.number = number
        self.email = email
        self.student_id = student_id



# super 사용 예시 - 단일 상속
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email

class Student(Person):
    def __init__(self, name, age, number, email, student_id, gpa): # 상속을 받더라도 생성자 함수 인자로 상속하는 생성자 함수 인자를 모두 작성해줘야 함
        super().__init__(name, age, number, email) # init의 인자는 self를 제외한 나머지 인자를 써주어야 함
        self.student_id = student_id
        self.gpa = gpa




# super 사용 예시 - 다중 상속
class ParentA:
    def __init__(self):
        self.value_a = 'ParentA'

    def show_value(self):
        print(f'Value from ParentA: {self.value_a}')


class ParentB:
    def __init__(self):
        self.value_b = 'ParentB'

    def show_value(self):
        print(f'Value from ParentB: {self.value_b}')


class Child(ParentA, ParentB):
    def __init__(self):
        super().__init__() # child는 생성될 때 인스턴스 변수 2개를 가짐 (value_c와 ParentA의 value_a)
        self.value_c = 'Child'

Child1 = Child()
print(Child1.value_a)
print(Child1.value_c)