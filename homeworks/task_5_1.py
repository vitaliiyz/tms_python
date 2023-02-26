import datetime
from time import sleep


# Task 1

def timestamp(func):
    def wrapper(*args, **kwargs):
        time_1 = datetime.datetime.now()

        run_func = func(*args, **kwargs)

        time_2 = datetime.datetime.now()
        print(f"Function execution time: {time_2 - time_1}")
        return run_func

    return wrapper


@timestamp
def to_do(a, b):
    sleep(3)
    return a + b


sum_num = to_do(1, 2)

print("Result:", sum_num)

# Task 2

is_started_with = lambda str_, sym_: True if str_[0] == sym_ else False

str_1 = input("Введите строку: ")
sym_1 = input("Введите символ: ")

print(f"Да, строка начинается с символа: \"{sym_1}\"" if is_started_with(str_1,
                                                                         sym_1) else f"Нет, строка начинается с символа: \"{str_1[0]}\"")

# Task 3

is_digit = lambda str_: True if str_.isdigit() else False

str_2 = input("Введите строку: ")

print("Данная строка является числом" if is_digit(str_2) else "Данная строка НЕ является числом")

# Task 4

list_1 = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

# list_2 = [i for i in list_1 if i % 19 == 0 or i % 13 == 0]

find_num = filter(lambda i: i % 19 == 0 or i % 13 == 0, list_1)

print(list(find_num))
