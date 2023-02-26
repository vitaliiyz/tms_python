class Bird:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def _fly(self):
        return f"{self.name} bird can fly"

    def walk(self):
        return f"{self.name} bird can walk"

    def __str__(self):
        return f"{self.name} bird can fly and walk"


class Canary(Bird):
    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        return f"{self.name} bird eats mostly grains"

    def fly(self):
        self._fly()

    def __str__(self):
        return f"{self.name} bird can fly and walk"


class Penguin(Bird):
    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        return f"{self.name} bird can swim"

    def eat(self):
        return f"{self.name} bird mostly eats fish"

    def __str__(self):
        return f"{self.name} can swim"


class SeaGull(Bird):
    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        return f"{self.name} bird eats fish"

    def fly(self):
        super()._fly()

    def swim(self):
        return f"{self.name} can swim"

    def __str__(self):
        return f"{self.name} can swim, fly and walk"


b = Bird("Any")
print(b.walk())

p = Penguin("Penguin")
print(p.swim())
# print(p.fly())
print(p.eat())

c = Canary("Canary")
print(str(c))
print(c.eat())

s = SeaGull("Gull")
print(str(s))
print(s.eat())
print(SeaGull.__mro__)
