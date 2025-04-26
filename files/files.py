'============Модели и Пакеты==============='
# любой файл с расширением ".py" - модуль

# пакет - это набор модулей (обязательно должен быть файл __init__.py)

'================Работа с файлами=================='
# open - функция которая открывает файл в определенном режиме:
'режимы'
# r - read(только для чтения)
# w - write(только для записи и каждый раз когда вы открываете файл в режиме записи то что было внутри очищается)
# a - append(только для дозаписи, добвляет в конец)
# x - создает файл, но если такой есть то выйдет ошибка
# b - binary (В бинарном виде)

'----------------read----------------'
# file = open('/home/hello/Рабочий стол/Class lections/files/test.txt', 'r')
# # print(file.read())
# # file.seek(0) # перенос каретки на 0 символ
# # print(file.read())
# # print(file.writable())
# # print(file.read(3))
# # print(file.read(3))
# file.seek(0)
# print(file.readlines(12)) #Читает каждую строку и возращает список со строками
# file.seek(0)
# print(file.readline()) #Читает первую строку
# print(file.tell()) 
# file.close()
# print
# (file.closed)
'--------------write-------------------'
# file = open('/home/hello/Рабочий стол/Class lections/files/test.txt', 'w')
#если файла нет - создаст его
# file.write('METALABS\nPython')
# file.writelines(['Hello\n', 'world\n', 'metalabs'])

# writelines - очищает файл и записывает строки но принимает list со строками
 # write - очищает файл и записывает строки, принимает строку 

# file.close()
'--------------append--------------------'
# file = open('/home/hello/Рабочий стол/Class lections/files/test.txt', 'a')
# file.write('\n\tNew line')
# file.writelines('\n\tHeloo')
# file.close()
'-----------------Контекстный менеджер---------------'

with open('/home/hello/Рабочий стол/Class lections/files/test.txt', 'r') as file:
    print(file.read())
    # file.close()
    # print(file.closed)
print('HI')

with open('/home/hello/Рабочий стол/Class lections/files/test.txt', 'r+') as file:
    print(file.read())
    file.write('\nhi')
    

