"============SOLID==========="
# SOLID - это аббревиатура для 
# набора принципов проектирование, 
# созданных для разработки програмного 
# обеспечения при помощи объектно ориентированных языков

# Принпи SOLID напрлен на содействие на содействие 
# разработки более простого, надежного и обновляемого кода

# S(SRP)
# 1. Single Responsibility Principels
# Принцип единственной обязанности
# ПЕО - требует того, что бы один класс 
# выполнял одну работу (Т.Е не надо создавать оргомный класс который делает все)

# O(OCP) - Open-Closed Principle
# Принцип октрытости\закртости - програмные сущности (классы, модули, функции) 
# должны быть открыты для расширение но закрыты для модификации

# Пример:
class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price 

    def get_discount(self):    
        if self.customer == "simple":
            return '10%'
        elif self.customer == 'vip':
            return '20%'
        elif self.customer == 'premium':
            return '50%'
        # elif self.customer == 'premium+':
            #return '70%' - так нельзя делать

#делай так:
class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price 

class SimpleDiscount(Discount):
    def get_discount(self):
        return f'{self} - 10%'
    
class VipDiscount(Discount):
    def get_discount(self):
        return f'{self} - 20%'
    
class PremiumDiscount(Discount):
    def get_discount(self):
        return f'{self} - 50%'
    
class PremiumPlusPlusDiscount(Discount):
    def get_discount(self):
        return f'{self} - 70%'
    
# L(LSP) - Liskov Substitution Principle
# Главная идея в том, что для любого класса клиент должен иметь возможность использовать любой подкласс этого класса, не замечая разницы между ними. Это означает что клиент полностью изолирован и не подозревает об изменениях в иерархии классов

class Animal:
    def __init__(self, attrs):
        self.attributes = attrs 

    def eat(self):
        print('Вкусно!')

class Cat(Animal):
    def eat(self, amount = 0.1):
        if amount > 0.3:
            print('Кошка сьеала много')
        else:
            print('Кошке вкусно!')

class Dog(Animal):
    def eat(self):
        print('Собаке вкусно!')

pluto = Dog({'name':'Pluto', 'age':3})
goofy = Dog({'name':'Goofy', 'age':2})
buttons = Cat(('Mr.Buttons', 4))

animals = (pluto, goofy, buttons)

attr = {'a':1}

for animal in animals:
    if animal.attributes['age'] > 2:
        print(animal.attributes['name'])

'I (ISP)'
# Interface Segregation Principle
# Принцип разделения интерфейсов

# Создавайте тонкие интерфейсы, которые ориентрированы на клиента. Клиент не должен зависеть от интерфейсов(или же методов которые не используются). Этот принцип устраняет недостатки реализации больших интерфейсов


class Creature:
    def __init__(self, name):
        self.name = name

    def swim(self):
        ...

    def walk(self):
        ...

    def talk(self):
        ...

class Human(Creature):
    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        print(f'{self.name} - умеет плавать')

    def walk(self):
        print(f'{self.name} - умеет ходить')

    def talk(self):
        print(f'{self.name} - умет говорить')


class Fish(Creature):
    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        print(f'{self.name} - умеет плавать')

class Cat(Creature):
    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        print(f'{self.name} - умеет плавать')

    def walk(self):
        print(f'{self.name} - умеет ходить')


human = Human('John Smith')
human.talk()
human.walk()
human.swim()

fish = Fish('Nemo')
fish.swim()
fish.walk()
fish.talk()

cat = Cat('ASD')
cat.walk()
cat.swim()
cat.talk()


class SwimInterface:
    def swim(self):
        ...
    
class WalkInterface:
    def walk(self):
        ...

class TalkInterface:
    def talk(self):
        ...

class Human(SwimInterface, TalkInterface, WalkInterface):
    def __init__(self, name):
        self.name = name

    def swim(self):
        print(f'{self.name} - умеет плавать')

    def walk(self):
        print(f'{self.name} - умеет ходить')

    def talk(self):
        print(f'{self.name} - умет говорить')

# D (DIP)
# Dependecy Inversion Principle
# Принцип инверсии зависимостей
# Зависимость должна быть от абстракций, а не от конкретики.
#  Модули верхних уровней не должны зависеть от модулей нижних уровней. Классы и верхних, и нижних уровней должны зависеть от одних и тех же абстракций.  Абстракции не должны зависеть от деталей. Детали должны зависеть от абстракций

class TerminalPrinter: # norm
    def write(self, msg):
        sys.stderr.write(f"{msg}\n")


class FilePrinter: # norm
    def write(self, msg):
        with open('log.txt', 'a+', encoding='UTF8') as f:
            f.write(f"{msg}\n")


class Logger: # зависит от двух других классов
    def init(self):
        self.prefix = time.strftime('%Y-%b-%d %H:%M:%S', time.localtime()) # можно опять применить OCP


    def log_stderr(self, message): #  вызывает write для конкретно класс
        TerminalPrinter().write(f"{self.prefix} {message}")


    def log_file(self, message): # Тут тоже
        FilePrinter().write(f"{self.prefix} {message}")


logger = Logger()
logger.log_file("Starting the program...")
logger.log_stderr("An error!")

# after

import sys
import time


class TerminalPrinter:
    def write(self, msg):
        sys.stderr.write(f"{msg}\n")


class FilePrinter:
    def write(self, msg):
        with open('log.txt', 'a+', encoding='UTF8') as f:
            f.write(f"{msg}\n")


class Logger:
    def init(self):
        self.format = '%Y-%b-%d %H:%M:%S' # теперь формат можно менять


    def log(self, message, notifier):
        prefix = time.strftime(self.format, time.localtime())
        notifier().write(f"{prefix} {message}")


logger = Logger()
logger.log("Starting the program...", TerminalPrinter)
logger.log("An error!", FilePrinter)
