import math

# Task 1
even_odd = lambda num: print("Четное") if num % 2 == 0 else print("Нечетное")

enter_num = int(input("Введите число: "))

even_odd(enter_num)

# Task 2

some_list = [1, 5, 234, 23, 33, 121212]
map_res = map(lambda i: str(i) if type(i) == int else i, some_list)
print(list(map_res))


# Task 3

# Способ 1
def is_palin(s: str):
    s = s.lower()
    result = False

    if len(s) == 1:
        result = True
    else:
        for i in range(math.floor(len(s) / 2)):
            if s[i] == (s[-1 - i]):
                result = True
            else:
                result = False

    return result


print(is_palin("Арбуз у зубра"))


# Способ 2
def is_palin_recurs(s: str):
    s = s.lower()
    if len(s) <= 1:
        return True
    elif s[0] == s[-1]:
        return is_palin_recurs(s[1:-1])
    else:
        return False


print(is_palin_recurs("Арбуз у зубра"))


# Способ 3
def is_palin_reverse(s: str):
    s = s.lower()
    s_reversed = s[::-1]

    if s == s_reversed:
        return True
    else:
        return False


print(is_palin_reverse("Арбуз у зубра"))

# Фильтрация filter()
words_tuple = ("Шалаш", "Виталий", "Арбуз у зубра", "12321", "2", "22", "qwe", "qwq")

map_result = filter(lambda i: is_palin_recurs(i), words_tuple)

print(tuple(map_result))

print(tuple(filter(lambda x: x.lower() == x[::-1].lower(), words_tuple)))


# Task 5
def analyze_str(s: str):
    try:
        num = int(s)

        if s.isdigit() or (s[0] == "-" and s[1:].isdigit()):
            num = int(num)

            if num < 0:
                return f"Вы ввели отрицательное целое число: {num}"
            elif num > 0:
                return f"Вы ввели положительное целое число: {num}"
            else:
                return f"Вы ввели: {num}"
        else:
            num = float(num)

            if num < 0:
                return f"Вы ввели отрицательное дробное число: {num}"
            else:
                return f"Вы ввели положительное дробное число: {num}"
    except ValueError:
        return f"Вы ввели некорректное число: \"{s}\""


print(analyze_str("-123123213"))
