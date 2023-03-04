from dataclasses import dataclass


@dataclass
class Data:
    _age: int
    _name: str

    @property
    def age(self):
        return self._age

    @property
    def name(self):
        return self._name

    @staticmethod
    def say_hello():
        print("Hello!")

    def introduce(self):
        print(f"My name is {self.name}, I'm {self.age}")


data = Data(25, "Vitali")
data.say_hello()
data.introduce()
