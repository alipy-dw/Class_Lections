'==============Встроенные функции======================'
#map, filter, reduce, zip, enumerate

# zip - соединяет несколько последовательностей (получаем генератор, в котором элементы - tuple)

# list1 = [1,2]
# list2 = ['a', 'b', 'c']
# list3 = [0.1, 5.5, 10.8, 0.5]

# zipped = zip(list2, list3)
# print(dict(zipped))
# for i in zipped:
#     print(i)

# enumerate - нумерует последовательность (по дефолту с 0) (тоже получаем генератор)

enum = enumerate('hello', 45)
# print(list(enum))
# a, b = 1, 2

# for num, elem in enum:
#     print(num, elem)

# map - принимает другую функцию и последовательность (записывает в новую последовательность результат функции, в которую передаются элементы последовательности)

# list1 = ['1', '2', '3', '4']
# mapped = map(int, list1) # (1, 2, 3, 4)
# print(list(mapped)) 

# def func_(x):
#     return x ** 2

# list_1 = [3, 1, 2, 5]

# mapped = list(map(func_, list_1))
# print(mapped)

# print(list(map(lambda x: x ** 2, [1,2,3])))


# filter - возвращает генератор, с элементами, прошедшими фильтрацию (какое-то условие), принимает функцию и последовательность

# list1 = ['hello', 'hi', '123', '3']
# filtered = filter(str.isdigit, list1) #('123', '3')
# print(list(filtered))

# print(list(filter(lambda x: x > 0, range(5))))    

#reduce - принимает функцию и последовательность, возвращает один результат (передоваемая функция должна принимать два аргумента)
# from functools import reduce
# print(reduce(lambda x, y: x + y, [1,2,3,4]))
# print(reduce(lambda x, y: x + y, ['hi','d','a','hello']))

