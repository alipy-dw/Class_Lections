'==============Абстракция================'
# Абстракция - это принцип ооп, в котором мы создаем класс пустышку,
# где задаем названия аттрибутов и методов, для того,
# чтобы в дочерних классах не забыть их переопределить


from abc import ABC, abstractmethod, abstractproperty

class AbstractAnimal(ABC):
    # @abstractproperty
    @property
    @abstractmethod
    def legs(self):
        ...
    
    @abstractmethod
    def voice(self):
        ...

# obj = AbstractAnimal() - НЕЛЬЗЯ

class Dog(AbstractAnimal):
    ...

# obj1 = Dog() # ОШИБКА, ПОТОМУЧТО НУЖНО ПЕРЕОПРЕДЕЛЯТЬ В КЛАССЕ Dog МЕТОД voice И АТТРИБУТ legs

class Dog(AbstractAnimal):
    legs = 4
    
    def voice(self):
        print('гав-гва')

obj2 = Dog()
obj2.voice()