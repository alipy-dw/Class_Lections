'==============Ассоциация============='
# Ассоциация - это принцип ООП, в котором два класса связаны друг с другом

'композиция' # сильная связь
'агрегация' # слабая связь

class Battery:
    _power = 100

    def charge(self):
        if self._power < 100:
            self._power = 100


class IPhone:
    def __init__(self, color):
        self.color = color 
        self.battery = Battery()

class Nokia:
    def __init__(self, color, a):
        self.color = color 
        self.battery = a

# Композиция(сильная связь), при удалении IPhone удалится батарейка тоже
iphone = IPhone('Красный')
# del iphone 


# Агрегация(слабая связь), при удалении Nokia, батарейка не удалится
battery_for_nokia = Battery()
nokia = Nokia('Синий', battery_for_nokia)
# del nokia 


iphone.battery._power = 50
iphone.battery.charge()
print(iphone.battery._power)

nokia.battery._power = 50
nokia.battery.charge()
print(nokia.battery._power)