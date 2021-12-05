'''
1. Програма-світлофор.
   Створити програму-емулятор світлофора для авто і пішоходів.
   Після запуска програми на екран виводиться в лівій половині - колір автомобільного, а в правій - пішохідного світлофора.
   Кожну секунду виводиться поточні кольори. Через декілька ітерацій - відбувається зміна кольорів - логіка така сама як і в звичайних світлофорах.
   Приблизний результат роботи наступний:
      Red        Green
      Red        Green
      Red        Green
      Red        Green
      Yellow     Green
      Yellow     Green
      Green      Red
      Green      Red
      Green      Red
      Green      Red
      Yellow     Red
      Yellow     Red
      Red        Green
      .......
'''

from time import sleep

traffic_lights = ['Red', 'Green', 'Yellow']
try: 
    while True:
        for i in range(4):
            print(f'{traffic_lights[0]}        {traffic_lights[1]}')
            sleep(1)
 
        for i in range(2):
            print(f'{traffic_lights[2]}        {traffic_lights[1]}')
            sleep(1)
 
        for i in range(4):
            print(f'{traffic_lights[1]}        {traffic_lights[0]}')
            sleep(1)
 
        for i in range(2):
            print(f'{traffic_lights[2]}        {traffic_lights[0]}')
            sleep(1)

except KeyboardInterrupt:
	print('The traffic lights are stoped')
        