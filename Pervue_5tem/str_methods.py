'========================Str методы======================'
str1 = 'Hello'
# res1 = str1.lower() # Hello -> hello
# print(res1) 
# print(str1.upper()) # Hello -> HELLO

# print(dir(str1))

str2 = 'hello'
# print(str2.swapcase()) # hELlO WoRlD
# print(str2.capitalize()) # Hello world
# print(str2.title()) # Hello World
# print(str2.replace('L', 'K', 3))

# print(str2.islower()) # False
# print(str2.isupper()) # True

str3 = 'hello'
# print(str3.isalpha()) # True
# print(str3.isdigit()) # False


str4 = '123'
# print(str4.isalnum()) # True
# 
# str5 = 'hello world222'
# print(str5.count('l')) # 3


'=======================BooleanType, NoneType========================'
a = True # истина (да)
b = False # ложь (нет)
c = None # пустота

# print(bool(1)) # True
# print(bool(0)) # False
# print(bool(None)) # False
# print(bool('hello')) # True
# print(bool(' ')) # True
# print(bool('')) # False
# print(bool(-15)) # True

'=================Логические и условные операторы======================='
# логические операторы - выражения, которые возвращают True или False

'равенство'
10 == 5 # False
10 == 10 # True

'не равно'
10 != 5 # True
10 != 10 # False

'больше'
34 > 10 # True
20 > 20 # False
10 > 12 # False

'меньше'
23 < 10 # False
10 < 10 # False
10 < 24 # True

'больше или равно'
10 >= 5 # True
10 >= 10 # True
2 >= 5 # False

'меньше или равно'
23 <= 4 # False
23 <= 23 # True
23 <= 100 # True

# print(5 == int('5')) 

'=====================And, Or, Not=================================='
# and - и
# or - или
# not - не

x = 5
y = 6
'AND'
#True      #True
x == 5 and y == 6 # True

#True   и   #False
x == 5 and y < 3  # False

#False   и  #False
x >= 20 and y == -23  # False

'OR'
#False или True
x > 10 or y == 6 # True

#True     #True
x == 5 or y == 6 # True

#False    #False
x == 13 or y == 23 # False

'NOT'
not True # False
not False # True

not 20 > 10 # False

x=12
y=4

# print(not x == 12 or y > 12 and x != 12 or y > 3) # True


# if условие1:
#     действие1
# elif условие2:
#     действие2
# elif условие3:
#    действие3
# else:
#     действие3



# pogoda = input('Какая погода? ') 

# if pogoda == 'дождь':
#     print('взять зонтик')
# elif pogoda == 'снег':
#     print('взять шапку')
# elif pogoda == 'солнечно':
#     print('взять очки')
# else:
#     print('такой погоды нет')



# запросите число у пользователя, проверьте какое это число + либо - либо 0 и выведите сообщение исходя от этого


x = int(input('Enter num: ')) #'12'
if x > 0:
    print(f'Число - {x}: положительное')
elif x < 0:
    print(f'Число - {x}: отрицательное')
else:
    print('Это ноль')





