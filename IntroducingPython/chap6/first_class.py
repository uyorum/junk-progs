class Person():
    def __init__(self, name):
        self.name = name

hunter = Person('Elmer Fudd')
print('The mighty hunter: ', hunter.name)


class Car():
    def exclaim(self):
        print("I'm a car!")


class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish.")

give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_car.exclaim()
give_me_a_yugo.exclaim()
