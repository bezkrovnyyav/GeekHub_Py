# Написати скрипт, який видалить пусті елементи із списка. Список можна "захардкодити"

enter_list = [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), ('d'), '', []]

no_empty_elements_list = list(filter(None, enter_list))
print(f"List without empty elements: {no_empty_elements_list}")