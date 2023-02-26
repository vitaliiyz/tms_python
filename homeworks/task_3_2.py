# Task 1

two_words = input("Enter 2 words: ")

list_two_words = two_words.split(" ")

format_1 = f'!{list_two_words[1]} ! {list_two_words[0]}!'
format_2 = '!%s ! %s!' % (list_two_words[1], list_two_words[0])
format_3 = '!{} ! {}!'.format(list_two_words[1], list_two_words[0])

print(format_1, format_2, format_3, sep="\n")


# Task 2

def greeting():
    name = input("Enter user's name: ")
    age = input("Enter user's age: ")

    if age.isdigit() and int(age) > 0:
        age = int(age)

        if 0 < age < 10:
            print("Привет, шкет", name)
        elif 10 <= age <= 18:
            print("Как жизнь,", name, end="?\n")
        elif 18 < age < 100:
            print("Что желаете,", name, end="?\n")
        else:
            print(name, ", вы лжете - в наше время столько не живут...", sep="")
    else:
        print("Ошибка, повторите ввод")


# Task 3

# while True:
greeting()

# Task 4

x = int(input("Введите целое число: "))
for_sum = 0

for i in range(1, x + 1):
    for_sum += i ** 3

print(for_sum)

while_sum = 0
i = 1
while i <= x:
    while_sum += i ** 3
    i += 1

print(while_sum)
