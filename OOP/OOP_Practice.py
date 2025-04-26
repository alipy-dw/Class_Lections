#2
# class Student:
#     def __init__(self, name, grade):
#         self.__name = name
#         self.__grade = grade

#     @property  
#     def grade(self):
#         return self.__grade
    
#     @grade.setter
#     def grade(self,grade):
#         if self.__grade < 100:
#             self.__grade = grade
#         elif self.__grade > 0:
#             self.grade = grade
#         else:
#             print("Недопустимое значение!")
        


# obj = Student('katana', 21)
# print(obj.grade)
# obj.grade = 100
# print(obj.grade)

#3
from math import pi
class Shape:
    def area():
        pass

class Rectangle(Shape):
    def area(self, width, width2):
        print(f'Площадь прямоугольника - {width * width2}')


class Circle(Shape):
    def area(self, radius):
        print(f'Площадь круга - {pi * radius ** 2}')