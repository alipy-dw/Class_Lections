'=========================Миксины==========================='
# Миксины - классы, которые будут использоваться для неследование. 
# Но от миксинов не создаются обьекты. Классы помощники

class FlyMixin:
    def fly(self):
        print('я могу летать')

class WalkMixin:
    def walk(self):
        print('Я могу ходить')

class SwimMixin:
    def swim(self):
        print('Я могу плавать')

class Human(WalkMixin, SwimMixin):
    name = 'Человек'

    def talk(self):
        print('я могу говорить')

class Fish(SwimMixin):
    name = 'fish'

class Duck(WalkMixin, SwimMixin, FlyMixin):
    name = 'duck'

objects = [Human(), Fish(), Duck()]

'======================'

for object in objects:
    print(object.name)
    attrs = ['fly', 'swim', 'walk', 'talk']
    for attr in attrs:
        if hasattr(object, attr): # проверяет есть ли у объекта конкретный метод
            method = getattr(object, attr) # получает из str и превращает его в метод
            method()
    print(' ')

obj = Human()
setattr(obj, 'name', 'katana') # меняет данные атрибута и если написать 
# несуществующий атрибут то тот создатся
# print(dir(obj))
print(obj.name)