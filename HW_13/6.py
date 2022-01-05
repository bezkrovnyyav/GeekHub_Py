'''
6. Створіть клас в якому буде атребут який буде рахувати кількість створених екземплярів класів.
'''  

class Person(object):

    counter = 0

    def __init__(self, name, age):
        Person.counter += 1
        self.name = name
        self.age = age

person_1 = Person('Andrii', 28)
print(Person.counter)

person_2 = Person('Olia', 25)
print(Person.counter)
