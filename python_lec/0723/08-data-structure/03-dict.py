# clear
person = {'name': 'Alice', 'age': 25}
person.clear()
print(person)


# get
person = {'name': 'Alice', 'age': 25}
print(person.get('name'))
print(person.get('country'))
print(person.get('country', 'Unknown'))
# print(person['country']) # 9번째 줄과 동일한 코드, 키가 없어 KeyError 발생


# keys
person = {'name': 'Alice', 'age': 25}
print(person.keys())
for item in person.keys():
    print(item)


# values
person = {'name': 'Alice', 'age': 25}
print(person.values())
for item in person.values():
    print(item)


# items
person = {'name': 'Alice', 'age': 25}
print(person.items()) # dict_items([('name', 'Alice'), ('age', 25)])
for key, value in person.items():
    print(key)
    print(value)


# pop
person = {'name': 'Alice', 'age': 25}
print(person.pop('age'))
print(person)
print(person.pop('country', None))
# print(person.pop('country'))


# setdefault
person = {'name': 'Alice', 'age': 25}
print(person.setdefault('country', 'KOREA'))
print(person)


# update
person = {'name': 'Alice', 'age': 25}
other_person = {'name': 'Jane', 'gender': 'Female'}

person.update(other_person)
print(person)

person.update(age=100, country = "KOREA")
print(person)


