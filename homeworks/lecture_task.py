from functools import reduce

# 1 task
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

print(list(map(lambda x: round(x ** 2, 3), my_floats)))

# 2 task
my_names = ["олимпиада", "закат", "программа", "python", "код"]

print(list(filter(lambda x: len(x) < 7, my_names)))

# 3 task
my_numbers = [2, 7, 10, 21, 8]

print(reduce(lambda x, y: x * y, my_numbers))
