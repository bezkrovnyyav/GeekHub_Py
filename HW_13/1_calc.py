'''
1. Створити клас Calc, який буде мати атребут last_result та 4 методи. Методи повинні виконувати математичні операції з 2-ма числами, а саме додавання, віднімання, множення, ділення.
   - Якщо під час створення екземпляру класу звернутися до атребута last_result він повинен повернути пусте значення
   - Якщо використати один з методів - last_result повенен повернути результат виконання попереднього методу.
   - Додати документування в клас (можете почитати цю статтю: https://realpython.com/documenting-python-code/ )
'''
class Calc(object):
   last_result = None
    
   def addition(self, num_1, num_2):
      # sum of two numbers
      self.last_result = num_1 + num_2
      return self.last_result

   def subtraction(self, num_1, num_2):
      # subtracting the second number from the first
      self.last_result = num_1 - num_2
      return self.last_result
   
   def division(self, num_1, num_2):
      # first number divides by the second
      try:
         self.last_result = num_1 / num_2
         return self.last_result
      except ZeroDivisionError:
            print('You can not divide by zero!')
   
   def multiplication(self, num_1, num_2):
      # first number divides via the second
      self.last_result = num_1 * num_2
      return self.last_result
   
operation = Calc()
#print(operation.last_result)
#
#print(operation.addition(1, 2))
#print(operation.subtraction(3, 4))
#print(operation.division(5, 0))
#print(operation.division(12, 4))
print(operation.multiplication(8, 9))