'==============Области видимости=============='
# LEGB - local enclosed global build-in

'==================Build-in==================='
# встроенное пространство имен (list, print, input, string, set, len)

'=================Global==================='
# пространство в файле, в котором мы пишем код
# globals() - это функция, которая показывает переменные и функции внутри глобального пространства(в файле) 
# num = 25 
# str1 = 'hello'
# print(globals())

'===================Local===================='
# локальное пространство - это пространство которое находится внутри функций

# var = 'global'

# def func():
#     var = 'local'
#     print(var)

# print(var)
# func()

# global
# local

'=================Enclosed================='
# замкнутое пространство - которое является локальным, у которого есть внутри локальальное пространство

# var = 'global'

# def func():
#     var = 'enclosed'
#     print(var)

#     def inner_func():
#         var = 'local'
#         print(var)

#     def inner_func_2():
#         ...

#     inner_func()

# func()
# print(var)






'---------------------------------'
# a = 'global'

# def func():
#     print(a)

# func()


# локальное пространство видит переменные из глобального пространства
'----------------------------------'

# def func():
#     a = 'local'

# print(a)

# глобальное пространство не видит переменные из локального пространства





# count = 1

# def increse_count():
#     global count
#     print(count)
#     count = count + 1

# increse_count() # 1
# increse_count() # 2
# increse_count() # 3





# def count(i):
#     counter = 0

#     def increase_counter():
#         nonlocal counter
#         print(counter)
#         counter = counter + 1

#     for elem in range(i): # 0 1 2 3 4 
#         increase_counter()


# count(5)

# 0
# 1
# 2
# 3 
# 4