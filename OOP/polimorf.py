'==================Полиморфизм==============='
# полиморфизм - принцип ООП, 
# в котором в разных классах методы называются одинаково, 
# но реализация разная (один интерфейс - разные функционалы)
        
class Animal:
    def voice(self):
        ...
class Dog(Animal):
    def voice(self):
        print('Гав - гав')

class Cat(Animal):
    def voice(self):
        print('Мяу - мяу')

class Duck(Animal):
    def voice(self):
        print('Кря - кря')

objects = [Dog(), Cat(), Duck(), Cat()]
for obj in objects:
    obj.voice()

