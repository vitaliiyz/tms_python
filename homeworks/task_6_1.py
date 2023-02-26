class Human:
    def __init__(self, sex, name, age):
        self._sex = sex
        self._name = name
        self._age = age

    @property
    def sex(self):
        return self._sex

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @sex.setter
    def sex(self, sex):
        self._sex = sex

    @name.setter
    def name(self, name):
        self._name = name

    @age.setter
    def age(self, age):
        self._age = age

    def describe_yourself(self):
        print(f"My name is {self.name}, I'm {self.age}, {self.sex}.")

    @staticmethod
    def describe_profession(position, profession):
        print(f"I'm {position} {profession}.")


man = Human("female", "Vita", "24")
man.describe_yourself()
man.age = 25
man.sex = "male"
man.name = "Vitali"
man.describe_yourself()
man.describe_profession("Middle", "QA")


class Smartphone:
    def __init__(self, brand, model, cost):
        self._brand = brand
        self._model = model
        self._cost = cost

    @property
    def brand(self):
        return self._brand

    @property
    def model(self):
        return self._model

    @property
    def cost(self):
        return self._cost

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @model.setter
    def model(self, model):
        self._model = model

    @cost.setter
    def cost(self, cost):
        self._cost = cost

    def get_phone_descr(self):
        return f"{self.brand} {self.model}. Cost: {self.cost}"

    @staticmethod
    def send_message(text, recipient):
        print(f"\"{text}\" message has been sent to {recipient}!")


iphone = Smartphone("Appl", "IPhone 11", 500)
print(iphone.get_phone_descr())
iphone.brand = "Apple"
iphone.model = "IPhone 14 Pro"
iphone.cost = 1500
print(iphone.get_phone_descr())
iphone.send_message("How are you doing?", "Nick")


class Developer:
    def __init__(self, lang, position, company):
        self._lang = lang
        self._position = position
        self._company = company

    @property
    def lang(self):
        return self._lang

    @property
    def position(self):
        return self._position

    @property
    def company(self):
        return self._company

    @lang.setter
    def lang(self, lang):
        self._lang = lang

    @position.setter
    def position(self, pos):
        self._position = pos

    @company.setter
    def company(self, comp):
        self._company = comp

    def write_code(self):
        print(f"{self.position} {self.lang} developer at {self.company} is writing code...")

    def change_job(self, new_lang, company):
        self.lang = new_lang
        self.company = company

        print(f"{self.position} developer has changed his job. Now he's working at {self.company} on {self.lang}")


dev = Developer("Java", "Junior", "Google")
dev.write_code()
dev.change_job("Python", "Meta")
dev.write_code()


class Hotel:
    def __init__(self, name, location, rooms):
        self._name = name
        self._location = location
        self._rooms = rooms

    @property
    def name(self):
        return self._name

    @property
    def location(self):
        return self._location

    @property
    def rooms(self):
        return self._rooms

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @location.setter
    def location(self, new_location):
        self._location = new_location

    @rooms.setter
    def rooms(self, new_rooms):
        self._rooms = new_rooms

    def check_avail(self, requested_rooms):
        if requested_rooms > self.rooms:
            print(f"Unfortunately, we have no {requested_rooms} room(s) in our hotel.")
        else:
            print(f"{requested_rooms} room(s) available now.")

    def get_hotel_descr(self):
        print(f"Name: {self.name}\nLocation: {self.location}\nAvailable number of rooms {self.rooms}")


hotel_1 = Hotel("Vitali resort & Spa", "Barcelona", 5)
hotel_1.get_hotel_descr()
hotel_1.check_avail(6)
hotel_1.check_avail(5)


class Car:
    def __init__(self, brand, model, fuel):
        self._brand = brand
        self._model = model
        self._fuel = fuel

    @property
    def brand(self):
        return self._brand

    @property
    def model(self):
        return self._model

    @property
    def fuel(self):
        return self._fuel

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @model.setter
    def model(self, model):
        self._model = model

    @fuel.setter
    def fuel(self, fuel):
        self._fuel = fuel

    def drive(self):
        print(f"You're driving {self.brand} {self.model} {self.fuel} now.")

    def fill_car(self, fuel):
        if fuel != self.fuel:
            print(f"You've chosen wrong fuel! Please, use {self.fuel} instead of {fuel}...")
        else:
            print(f"Your {self.model} has been filled!")


audi = Car("Audi", "A6", "Petrol")
audi.drive()
audi.fill_car("Diesel")
audi.fill_car("Petrol")
