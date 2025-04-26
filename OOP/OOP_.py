'===================OOP===================='
# OOP - object-orientated programing
# ООП - обектно-ориентированное програмирование(Парадигма)

# class - это шаблон
# object(instance, экземпляр) - конечный продукт нашего класса

class Person:
    # переменные внутри класса либо объекта называются атрибутыми
    arms = 2
    legs = 2

    def __init__(self, name, age, prof):
        # __init__ -  метод котороый будет добавлять в объект те аттрибуты который у всех объектов разные 
        # self - это ссылка на объект который только что создался 
        self.name = name
        self.age = age
        self.prof = prof

    # Функции внутри класса (объекта) - методы
    def walk(self):
        print(f'{self.name} Ходит')
    
    def swim(self):
        print(f'{self.name} Плавает')

obj1 = Person('Faha', 16, 'Senior')
obj2 = Person('Adilet', 13, 'Clown')

# print(obj1.name)
# print(obj2.age)
# obj1.walk()
# obj1.swim()
# obj2.swim()

class Calc:
    def add(self, a, b):
        return a + b
    def dif(self, a, b):
        return a - b
    def div(self, a, b):
        return a / b
    def mult(self, a, b):
        return a * b
obj1 = Calc()
print(obj1.add(17, 12))
print(obj1.dif(10, 5))
print(obj1.div(17, 12))
print(obj1.mult(10, 5))