class MyTime:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds

    @classmethod
    def init_from_string(cls, time_string: str):
        hours, minutes, seconds = map(int, time_string.split(":"))
        return cls(hours, minutes, seconds)

    @classmethod
    def init_from_obj(cls, my_time_obj: 'MyTime'):
        return cls(my_time_obj.hours, my_time_obj.minutes, my_time_obj.seconds)

    @classmethod
    def init_without_parameters(cls):
        print("Warning: There are no any parameters for this class...")

    @property
    def hours(self):
        return self._hours

    @property
    def minutes(self):
        return self._minutes

    @property
    def seconds(self):
        return self._seconds

    @hours.setter
    def hours(self, value):
        self._hours = value

    @minutes.setter
    def minutes(self, value):
        self._minutes = value

    @seconds.setter
    def seconds(self, value):
        self._seconds = value

    def get_time_in_seconds(self):
        minutes = self.hours * 60 + self.minutes
        seconds = minutes * 60 + self.seconds
        return seconds

    def __eq__(self, other):
        return self.get_time_in_seconds() == other.get_time_in_seconds()

    def __ne__(self, other):
        return self.get_time_in_seconds() != other.get_time_in_seconds()

    def __ge__(self, other):
        return self.get_time_in_seconds() >= other.get_time_in_seconds()

    def __le__(self, other):
        return self.get_time_in_seconds() <= other.get_time_in_seconds()

    def __lt__(self, other):
        return self.get_time_in_seconds() < other.get_time_in_seconds()

    def __gt__(self, other):
        return self.get_time_in_seconds() > other.get_time_in_seconds()

    def __add__(self, other):
        self.seconds += other.get_time_in_seconds()

    def __sub__(self, other):
        self.seconds -= other.get_time_in_seconds()

    def __mul__(self, other):
        self.seconds *= other.get_time_in_seconds()

    def __str__(self):
        while self.seconds >= 60:
            self.minutes += 1
            self.seconds -= 60

        while self.minutes >= 60:
            self.hours += 1
            self.minutes -= 60

        hours, minutes, seconds = map(str, (self.hours, self.minutes, self.seconds))

        return f"{'0' + hours if len(hours) < 2 else hours}" \
               f":{'0' + minutes if len(minutes) < 2 else minutes}" \
               f":{'0' + seconds if len(seconds) < 2 else seconds}"


time_from_nums = MyTime(60, 121, 122)
print(time_from_nums.__str__())

time_from_str = MyTime.init_from_string("12:59:63")
print(time_from_str.__str__())

time_from_obj = MyTime.init_from_obj(time_from_str)
print(time_from_obj.__str__())

print(time_from_str.__eq__(time_from_obj))
print(time_from_obj.__ge__(time_from_nums))

mh_2 = MyTime.init_without_parameters()

time_from_nums.__add__(time_from_str)
print(time_from_nums.__str__())
