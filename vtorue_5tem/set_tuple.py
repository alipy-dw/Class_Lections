'=================================Set(Множества)==========================='
# set - изменяемый, неидексируемый, неупорядоченный, итерируемый - тип данных, который хранит в себе уникальные значение. Множество хранит в себе только неизменяемый тип данных

# list1 = [12, 'hi', [1,2,3], None, True, False, {'a':1, 'b':2}]

set1 = {1, 2, 'a', 'hello'}
print(set1)

'===========================FIFO - LIFO========================'
# FIFO - first in first out

# LIFO - last in first out

'=====================Методы==================='
# print(dir(set))

# add - добавляет элемент в set

# set1 = {3,'hi',True}
# set1.add(4)
# print(set1)


# pop - удаляет элемент случайно
# set2 = {True, 'hello','hi'}
# set2.pop()
# print(set2)


# remove - удаляет элемент по значению
# set3 = {1, 'hello', 'hi'}
# set3.remove('hi')
# print(set3)


# update - расширяет сет
# set4 = {1,2,3}
# set5 = {3,5,6}
# set4.update(set5)
# print(set4) 


# difference - наход разницу в сетах
# set6 = {1,2,3}
# set7 = {3,4,5}

# print(set6.difference(set7)) # {1,2}
# print(set7.difference(set6)) # {4,5}

# print(set6 - set7) # {1,2}
# print(set7 - set6) # {4,5}


# a = set()
# print(type(a))


# list_1 = [1,2,3, 'hi']
# str1 = 'abc'
# set2 = set(str1)
# print(set2)


'==============================Tuple========================'
# tuple - неизменяемый, итерируемый тип данных, которых хранит в себе любой тип данных. 

# list1 = [1,2,3]
# tuple1 = (1, 2, 3, 2, 4, 2)

# print(tuple1.index(3)) # 2

# print(dir(tuple1))
# 
# list1 = [1,2,3]
# list2 = [1,2,3]
# 
# list1 is list2
# 
# '-------------------------'
# 
# tuple1 = (1,2,3)
# tuple2 = (1,2,3)
# 
# 
# tuple1 is tuple2  
# 


# У вас есть list5 = [12, 4, 3, 4, 56, 8, 9, 0, 0, 23, 34]
# вам нужно удалить все похожие элементы и оставить уникальные, в конце должен получится list
# list5 = [12, 4, 3, 4, 56, 8, 9, 0, 0, 23, 34]
# set1 = set(list5)
# list5 = list(set1)
# print(list5)



# count = 0
# while count < 10:
#     count += 1
#     print(count) 

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# 11 dz
# 2 Задание. Вывод только положительных чисел
# (с использованием while)

# Дан список чисел. Напишите программу, которая выводит только положительные числа из списка, используя цикл while. Пропускайте отрицательные числа, не выводя их на экран, с помощью оператора continue.

# list1 = [1,2,-3,4,-5,6]
# count = 0
# while count < len(list1):
#     elem = list1[count]
#     if elem < 0:
#         count += 1
#         continue
#     print(elem)
#     count += 1


# Задание 6: Задача на логику

# Вам дан словарь:

# products = {'apple': 50, 'banana': 30, 'cherry': 60}

# 1. Напишите код, который увеличивает цену каждого продукта на 10%.
# Пример:

# {'apple': 55, 'banana': 33, 'cherry': 66}


# 2. Удалите продукт с наименьшей ценой из словаря.
# 3. Добавьте новый продукт 'orange': 40.
# 4. Напишите цикл, который выводит все продукты с ценой выше 50.



# products = {'apple': 50, 'banana': 30, 'cherry': 60}


# min_elem = min(products.values())


# for k, v in products.items():
#     if v == min_elem:
#         products.pop(k)

# print(dir(set()))


