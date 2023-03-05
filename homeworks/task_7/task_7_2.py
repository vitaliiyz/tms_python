from car_exceptions import NegativeSpeedError, SpeedingError


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
        if self.speed >= 60:
            raise SpeedingError("Maximum allowed driving speed is 60 km/h")
        self.speed += 5

    def deceleration(self):
        if self.speed < 5:
            raise NegativeSpeedError("Car speed cannot be less than 0")
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

try:
    car.deceleration()
except NegativeSpeedError as e:
    print(e)

car.show_speed()

car.acceleration()
car.acceleration()
car.acceleration()
car.acceleration()
car.acceleration()
car.acceleration()
car.acceleration()
car.acceleration()
car.acceleration()
car.acceleration()
car.acceleration()
car.acceleration()
car.show_speed()

try:
    car.acceleration()
except SpeedingError as e:
    print(e)

car.show_speed()
