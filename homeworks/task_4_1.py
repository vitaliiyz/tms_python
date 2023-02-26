# Написать 12 функций по переводу:

# Дюймы в сантиметры
cm_in_inch = 0.393701


def inch_to_cm(inch):
    return inch / cm_in_inch


print(inch_to_cm(30))


# Сантиметры в дюймы
def cm_to_inch(cm):
    return cm * cm_in_inch


print(cm_to_inch(3))

# Мили в километры
km_in_mile = 1.60934


def mile_to_km(mile):
    return mile * km_in_mile


print(mile_to_km(3))


# Километры в мили
def km_to_mile(km):
    return km / km_in_mile


print(km_to_mile(3))

# Фунты в килограммы
kg_in_pound = 0.453592


def pound_to_kg(pound):
    return pound * kg_in_pound


print(pound_to_kg(2))


# Килограммы в фунты
def kg_to_pound(kg):
    return kg / kg_in_pound


print(kg_to_pound(2))

# Унции в граммы
g_in_ounce = 28.3495


def ounce_to_g(ounce):
    return ounce * g_in_ounce


print(ounce_to_g(3))


# Граммы в унции
def g_to_ounce(g):
    return g / g_in_ounce


print(g_to_ounce(50))

# Галлон в литры
l_in_gallon = 3.78541


def gallon_to_l(gallon):
    return gallon * l_in_gallon


print(gallon_to_l(3))


# Литры в галлоны
def l_to_gallon(l):
    return l / l_in_gallon


print(l_to_gallon(5))

# Пинты в литры
l_in_pint = 0.473176


def pint_to_l(pint):
    return pint * l_in_pint


print(pint_to_l(2))


# Литры в пинты
def l_to_pint(l):
    return l / l_in_pint


print(l_to_pint(2))

# Программа для пользователя
all_swaps = {}  # все функции перевода
all_names = {}  # все названия функций перевода


def add_new_swap(func, name):
    key_num = len(all_swaps) + 1

    all_swaps[f"{key_num}"] = func
    all_names[f"{key_num}"] = name


add_new_swap(inch_to_cm, "Дюймы в сантиметры")
add_new_swap(cm_to_inch, "Сантиметры в дюймы")
add_new_swap(mile_to_km, "Мили в километры")
add_new_swap(km_to_mile, "Километры в мили")
add_new_swap(pound_to_kg, "Фунты в килограммы")
add_new_swap(kg_to_pound, "Килограммы в фунты")
add_new_swap(ounce_to_g, "Унции в граммы")
add_new_swap(g_to_ounce, "Граммы в унции")
add_new_swap(gallon_to_l, "Галлон в литры")
add_new_swap(l_to_gallon, "Литры в галлоны")
add_new_swap(pint_to_l, "Пинты в литры")
add_new_swap(l_to_pint, "Литры в пинты")


def show_func_names():
    for key, name in all_names.items():
        print(f"{key} - {name}")


def enter_value():
    entered_value = input("Введите значение, которое хотите конвертировать: ")

    if entered_value.isdigit():
        return int(entered_value)
    else:
        try:
            float(entered_value)
            return float(entered_value)
        except ValueError:
            return False


def swap():
    while True:
        print("\nВведите значение в зависимости от желаемой конвертации, где: ")
        show_func_names()
        user_value = input("Ваше значение (введите 0 для выхода из программы): ")

        if user_value not in all_swaps and user_value != "0":
            print("Введено неверное значение...")
            continue
        elif user_value == "0":
            break

        entered_value = enter_value()

        if not entered_value:
            print("Введено неверное значение...")
            continue

        swap_func = all_swaps.get(user_value)
        print("Результат:", swap_func(entered_value), end="\n\n")


swap()
