class Car:
    def __init__(self, brand, model, year, speed=0):
        self._brand = brand
        self._model = model
        self._year = year
        self._speed = speed

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value

    def acceleration(self):
        self.speed += 5

    def deceleration(self):
        self.speed -= 5

    def stop(self):
        self.speed = 0

    def show_speed(self):
        print(self.speed)

    def turn_around(self):
        if self.speed != 0:
            self.speed *= -1


car = Car("Audi", "A8 D4", "2017")
car.show_speed()
car.acceleration()
car.acceleration()
car.show_speed()
car.deceleration()
car.show_speed()
car.turn_around()
car.show_speed()
car.stop()
car.show_speed()
