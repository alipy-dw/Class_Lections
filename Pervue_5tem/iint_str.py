'=======================INT/STR======================'

# int - это целочисленный тип данных
num = 17

# float - это вещественные цисла (тип данных)
num2 = 0.5

# decimal - это вещественное число, но более точнее (тип данных)
num3 = 0.50000000000000

# complex - не проходим

# str - это строковый тип данных
str1 = 'Привет'

str2 = """ Hi """
str3 = ''' Hi '''

# print(str1)

'==================Операции над int/str========================='

num1 = 10
num2 = 5

res = num1 * num2
# print(res)

# print(num1 * num2)


# res = num1 + num2  # 13
# res = num1 - num2  # 7

res1 = num1 / num2 # вещественное деление 

res2 = num1 // num2 # целочисленное деление
# print(res1, res2)


x = 5
y = 3

result1 = x ** y  # 5^3 = 5 * 5 * 5 = 125
result2 = y ** x  # 3^5 = 3 * 3 * 3 * 3 * 3 = 243
# print(result1, result2)   


x = 10
y = 3

# print(x % y) # 1
# print(10 % 5) # 0


# x = 81
# print(x ** 0.5) # нашли кв корень через формулу

# from math import sqrt
# # из файла импортируй это

# print(sqrt(x)) # нашли кв корень через функцию sqrt 

# pow 
# 1) возводит в степень
# 2) находит отстаток
# print(pow(5, 3, 2)) # (5 ** 3) % 2 = 1 


str1 = 'metalabs '
num1 = 100

# print(str1 + num1) # error
# print(str1 * num1) # выйдет 100 раз metalabs

# str1 = 'hello'
# str2 = 'world'
# print(str1 + str2) # helloworld 

# конкатенация - процесс сложения строк

# name = input('Введите имя: ')
# age = int(input('Введите свой возраст: '))

# print(f'Меня зовут {name} мне {age} лет')
# форматирование - когда внутри строки используем переменные

# print(int('124')) # '124' -> 124 

# print('Привет\nмир!') # \n - переносит строку вниз
# print('Привет\tмир!') # \t - добавляет табуляцию(несколько пробелов)
# print('\tПривет\n\tмир!') 
# экранирование - использование команд внутри строки


# print(len('hello world')) # 11 , кол-во символов в строке

#index - нумерация последовательности, начинается с 0
#         ...-2-1
#'m e t a l a b s'
# 0 1 2 3 4 5 6 7

str1 = 'hello world'
# print(str1[4]) # o
# print(str1[10]) # d
str2 = 'dgsadfhasgdhasgdyshdaasdasdas'
# print(str2[-1])

print(str1[0:5]) # hello
print(str1[::2]) #hlowrd - перепрыгнул

# срезы[start:end:step] - это часть строки
