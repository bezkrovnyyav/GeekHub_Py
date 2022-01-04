'''
2. Створити клас Person, в якому буде присутнім метод __init__ який буде приймати * аргументів,
які зберігатиме в відповідні змінні. Методи, які повинні бути в класі Person - show_age, print_name, show_all_information.
   - Створіть 2 екземпляри класу Person та в кожному з екземплярів створіть атребут profession.
'''

class Person(object):
   def __init__(self, name, surname, age):
      self.name = name
      self.surname = surname
      self.age = age
   
   def print_name(self):
      return self.name

   def print_surname(self):
      return self.surname

   def show_age(self):
      return self.age

   def show_all_information(self):
      return self.__dict__

person_1 = Person('Sonia', 'Laska', 25)
person_2 = Person('Andrii', 'Bezkrovnyi', 28)

print(person_1.show_all_information())
print(person_2.show_all_information())
