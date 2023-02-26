from time import sleep


class Auto:
    def __init__(self, brand, age, mark, color=None, weight=None):
        self._brand = brand
        self._age = age
        self._mark = mark
        self._color = color
        self._weight = weight

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @staticmethod
    def move():
        print("move")

    def birthday(self):
        self.age += 1

    @staticmethod
    def stop():
        print("stop")


class Track(Auto):
    def __init__(self, brand, age, mark, max_load):
        super().__init__(brand, age, mark)
        self._max_load = max_load

    def move(self):
        print("attention")
        super().move()

    @staticmethod
    def load():
        print("load")
        sleep(1)
        print("load")
        sleep(1)


class Car(Auto):
    def __init__(self, brand, age, mark, max_speed):
        super().__init__(brand, age, mark)
        self._max_speed = max_speed

    @property
    def max_speed(self):
        return self._max_speed

    def move(self):
        super().move()
        print(f"max speed is {self.max_speed}")


track_1 = Track("MAN", 5, "TGS", 10000)
track_2 = Track("Mersedes", 1, "Actros", 12000)

car_1 = Car("Audi", 4, "A6", 230)
car_2 = Car("Volkswagen", 3, "Golf 7", 250)

track_1.move()
track_2.load()
track_1.stop()
track_2.birthday()
print(track_2.age)

car_1.move()
car_2.move()
car_2.birthday()
print(car_2.age)
