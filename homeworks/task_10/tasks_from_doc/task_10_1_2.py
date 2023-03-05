import random


class Iterator:
    def __init__(self, lst: list):
        self._lst = lst
        self._cursor = 0

    @property
    def lst(self):
        return self._lst

    @property
    def cursor(self):
        return self._cursor

    @cursor.setter
    def cursor(self, new_cursor):
        self._cursor = new_cursor

    def __iter__(self):
        return self

    def __next__(self):
        if self.cursor >= len(self.lst):
            raise StopIteration

        value = self.lst[self.cursor] ** 2
        self.cursor += 2

        return value


iterator = Iterator([random.randint(1, 10) for i in range(5)])
print(iterator.lst)

for i in iterator.lst:
    print(iterator.__next__())
