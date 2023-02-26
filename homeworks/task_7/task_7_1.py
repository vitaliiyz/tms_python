import math


class Counter:
    def __init__(self, start=0, stop=math.inf):
        self._value = start
        self._stop = stop

    @property
    def stop(self):
        return self._stop

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    def increment(self):
        if self.value < self.stop:
            self.value += 1
        elif self.value == self.stop:
            raise ValueError("Maximal value is reached.")

    def get(self):
        print(self.value)


c1 = Counter(start=42)
c1.increment()
c1.get()

c2 = Counter()
c2.increment()
c2.get()
c2.increment()
c2.get()

c3 = Counter(start=42, stop=43)
c3.increment()
c3.get()
c3.increment()
c3.get()
