'===============Функции==============='
# функции - именнованный блок кода, который может принимать аргументы и возвращать результат

# def my_sum(x, y): # x, y = параметры
#     return x + y

# res = my_sum(5, 2) # 5, 2 = аргументы
# print(res)

# res2 = my_sum(10, 23)
# print(res2)


# def my_len(posl):
    # count = 0
    # for i in posl:
        # count += 1 # count = count + 1
    # print(count)

# res1 = my_len([34, 1, 34, 2, 2])  # 5
# print(res1)
# res2 = my_len('hello world') # 11
# print(res2)
# res3 = my_len({12, 2, 32, 2, 12, 1}) # 4
# print(res3)



'==============Виды параметров==========='
# 1. обязательные
# 2. необязательные

# 3. с дефолтом(со значением по умолчанию)
# 4. *args - все позиционные аргументы, которые не попали в обязательные и с дефолтом)
# 5. **kwargs - все лишние именнованные аргументы

# def func_(x, y, z=4):
#     return x + y + z

# print(func_(10, 5))

'==========Виды аргументов==========='
# 1. позиционные (по позиции)
# 2. именнованные (по названию (параметр=аргумент))

# def add_or_add_10(num1, num2=10):
#     return num1 + num2 

# print(add_or_add_10(5, 2)) # 7
# print(add_or_add_10(40)) # 50

# def func(a, b=10, *args, **kwargs):
#     print(a)
#     print(b)
#     print(args)
#     print(kwargs)

# func(10)
# func(20, 30)
# func(b=30, a=40)
# func('hi', 50, True, False, 'hi', 12, 34)
# func(40, 50, 60, 70, hello=11, hi=10)



'================Lambda===================='
# lambda - анонимная функция, которая записывается в одну строку

# lambda_func = lambda x, y: x ** y
# print(lambda_func(5, 2))


# def func_(x):
#     return x ** 3

# print(func_(5))
# print(func_(1))

# from file import func

# print(func(10))


#1
# def cwcwcw():
    # num1 = int(input('Введите число: '))
    # num2 = int(input('Введите число: '))
    # str = input('Введите операцию: ')
    # if str.lower == 'сложение' or '+':
        # return num1 + num2
    # elif str.lower == 'вычетание' or '-':
        # return num1 - num2
    # elif str.lower == 'уможение' or '*':
        # return num1 * num2
    # elif str.lower == 'деление' or '/':
        # return num1 / num2
# print(cwcwcw())


# 1. Напишите программу на функциях. Вы у пользователя спрашиваете что он хочет сделать 

# 1.Войти
# 2.Зарегистрироваться

# Смотря от того что введет пользователь, вы должны его зарегестрировать или залогинить




# Регистрация:
# Вы запрашиваете username, password1, password2
# После того как пользователь введет данные, вам нужно сохранить эти данные в переменную users

# Логин:
# Запросить username, если такой username есть, запросить пароль и проверить правильно ли ввел этот пароль
# Если такого username нет в users то нужно сказать ему такого пользователя нет в базе



# Напишите калькулятор на функциях. Вы должны запросить у пользователя num1, num2, операци. И вернуть результат 

# users = [
    # {'username':'katana', 'password1':'205221sula', 'password2':'205221sula'}
    # ]
# 
# def menu():
    # # choice = input('Что вы хотите сделать?\n1.Войти\n2.Зарегестрироваться\n')
    # # return choice
# 
# # def register(users):
    # # username = input('Введите логин: ')
    # # password1 = input('Введите пароль: ')
    # # password2 = input('Подтвердите пароль')
    # # users.append({"username":username, "password1":password1, 'password2':password2})
    # # print('Вы зарегестрировались')
# 
# # def login(users):
    # # username = input('Введите логин: ')
    # # for user in users:
        # # if user['username'] == username:
            # # password = input('Введите пароль: ')
            # # if password == user['password1']:
                # # print('Вы успешно вошли')
            # # else:
                # # print('Не верный пароль')
            # # break
    # else:
        # # print('Такого пользователя не существует')
# 
# 
# 
# choice = menu()
# # if choice == '1':
    # # login(users)
# # elif choice == '2':
    # # register(users)