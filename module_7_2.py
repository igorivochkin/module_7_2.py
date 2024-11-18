# module_7_2.py
from pprint import pprint

def custom_write(file_name,strings):
    string_position = {} # Пустой словарь для возврата
    with open(file_name, 'w', encoding='utf-8') as file: # открыть файл на запись
        for i,s in enumerate(strings,start = 1): # номер стоки и строка
            pos = file.tell() # позиция указателя
            file.write(s + '\n') # записать строку с переносом
            string_position[(i,pos)] = s #формировка словаря
    return string_position #возврат


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
