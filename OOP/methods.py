# '==============Виды методов==============='
# # существует 3 вида методов
# '1) instance methods - обычное методы, которые принимают первым аргументом 
# self (ссылку на обьект). Нужны они для работы с аттрибутами обьекта'

# class A: 
#     def instance_method(self):
#         print('метод обьетка')
#         print('первый аргумент:', self)

# obj_a = A()
# obj_a.instance_method() 

# '2) class methods - методы, которые принимают первым агрументом cls (ссылка на класс). 
# Нужны они для создания обьекта или изменения аттрибута класса. 
# Для создания метода класса нужно задекорировать его в classmethod'

# class B:
#     @classmethod
#     def class_method(cls):
#         print('класс метод')
#         print('первый аргумент:', cls)


# class C:
#     counter = 0

#     # def __init__(self):
#     #     self._inc_counter()

#     @classmethod
#     def _inc_counter(cls):
#         cls.counter += 1

# obj1 = C()
# obj1._inc_counter()
# obj2 = C()
# obj2._inc_counter()
# obj3 = C()
# obj3._inc_counter()
# print(obj1.counter)


# class Pizza:
#     def __init__(self, r, *ing):
#         self.r = r 
#         self.ing = ing

#     def cook(self):
#         print(f'Готовится пицца размером {self.r*2} см')
#         print(f'Ингридиенты: {self.ing}')

#     @classmethod
#     def four_cheeze(cls, r):
#         pizza = cls(r, 'Моцарелла', 'Дор блю', 'Голландский', 'Чеддер')
#         return pizza 
    
# pizza1 = Pizza(15, 'Пеперони', 'Моцарелла')
# pizza2 = Pizza.four_cheeze(20)

# for i in [pizza1, pizza2]:
#     i.cook()


'3) static methods - просто функции внутри класса, которые не взаимодействуют ни с классом, '
'ни с обьектом. Находятся они внутри класса лишь потому, что они используются только '
'внутри класса и вне они в целом безполезны. Чтобы создать static метод, нужно его '
'задекорировать staticmethod'

class D:
    @staticmethod
    def hello():
        print(2 * 2)

obj_d = D()
obj_d.hello()
D.hello()


class Cylinder:
    def __init__(self, diameter, hight):
        self.di = diameter
        self.h = hight
        self.area = self.get_area(diameter, hight)
    
    @staticmethod
    def get_area(di, h):
        from math import pi 
        circle = pi * (di / 2) ** 2
        side = pi * di * h 
        area = circle * 2 + side 
        return round(area, 2)
    
cylinder1 = Cylinder(4, 10)
print(cylinder1.area)