# 6-1 - 6-3
class Thing():
    pass

print(Thing)

example = Thing()
print(example)


class Thing2():
    letters = 'abc'

print(Thing2.letters)


class Thing3():
    def __init__(self):
        self.name = 'xyz'

# print(Thing3.name)
thing3 = Thing3()
print(thing3.name)

# 6-4 - 6-8
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

hydrogen1 = Element('Hydrogen', 'H', 1)
print(hydrogen1.name, hydrogen1.symbol, hydrogen1.number)

dict = {
    'name': 'Hydrogen',
    'symbol': 'H',
    'number': 1,
    }
hydrogen2 = Element(**dict)
print(hydrogen2.name, hydrogen2.symbol, hydrogen2.number)


class Element2(Element):
    def dump(self):
        print(self.name, self.symbol, self.number)

    def __str__(self):
        return ' '.join([self.name, self.symbol, str(self.number)])

hydrogen3 = Element2(**dict)
hydrogen3.dump()
print(hydrogen3)


class Element3():
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number

hydrogen4 = Element3(**dict)
print(hydrogen4.name)
print(hydrogen4.symbol)
print(hydrogen4.number)

# 6-9
class Laser():
    def does(self):
        return 'disintegrate'


class Claw():
    def does(self):
        return 'crush'


class SmartPhone():
    def does(self):
        return 'ring'


class Robot():
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()

    def does(self):
        return '''Laser does %s
Claw does %s
SmartPhone does %s''' % (self.laser.does(),
                         self.claw.does(),
                         self.smartphone.does())

robot = Robot()
print(robot.does())
