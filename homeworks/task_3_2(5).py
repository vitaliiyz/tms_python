from random import randint


# Task 5

def guess_number():
    while True:
        print("Игра: угадай число!\n")

        lower_num = input("Введите нижнее значение диапазона: ")

        while not lower_num.isdigit():
            print("Введено неверное значение! Значение должно быть целым числом...")

            if not continue_qstn():
                return

            lower_num = input("Введите нижнее значение диапазона: ")
        else:
            lower_num = int(lower_num)

        upper_num = input("Введите верхнее значение диапазона: ")

        while not upper_num.isdigit() or int(upper_num) <= lower_num:
            print("Введено неверное значение! Значение должно быть целым числом и больше нижнего значения диапазона...")

            if not continue_qstn():
                return

            upper_num = input("Введите верхнее значение диапазона: ")
        else:
            upper_num = int(upper_num)

        rand_int = randint(lower_num, upper_num)

        # print(rand_int

        guess_num = input(f"Попробуйте угадать целое число от {lower_num} до {upper_num}: ")

        while not guess_num.isdigit() or int(guess_num) < lower_num or int(guess_num) > upper_num:
            print(f"Введено неверное значение! Введите значение от {lower_num} до {upper_num}...")

            if not continue_qstn():
                return

            guess_num = input(f"Попробуйте угадать целое число от {lower_num} до {upper_num}: ")
        else:
            guess_num = int(guess_num)

            if guess_num == rand_int:
                print("Поздравляем! Вы выиграли!", end="\n\n")

                if not continue_qstn():
                    return
            else:
                print("Вы проиграли, попробуйте снова! Загаданное число:", rand_int, end="\n\n")

                if not continue_qstn():
                    return


def continue_qstn():
    want_continue = input("Вы хотите продолжить? Напишите \"Да\" или \"Нет\": ")
    if want_continue.lower() == "да" or want_continue.lower() == "\"да\"":
        return True
    else:
        return False


guess_number()
