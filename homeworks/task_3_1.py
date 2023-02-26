from math import floor

# Task 1

num = int(input("Enter a number: "))

if num % 1000 == 0:
    print("millennium")

# Task 2

qty = int(input("Enter a quantity of guests: "))

if qty > 50:
    print("Restaurant")
elif 20 <= qty <= 50:
    print("Cafe")
else:
    print("Home")

# Task 3

str_1 = input("Enter a string: ")

if len(str_1) >= 10:
    str_2 = f'{str_1}!!!'
    print(str_2)
else:
    print(str_1[1])

# Task 4

str_3 = input("Enter a string: ")

avg_len = floor(len(str_3) / 2)

avg_smbl = str_3[avg_len]

if avg_smbl == str_3[0]:
    new_str = str_3[1:-1]
    print(new_str)
