# Task 1

a = 10
b = 10
c = 10

print(id(a) == id(b) == id(c))

# Task 2

var_1 = [1, 2]
var_2 = [1, 2]

print(id(var_1) == id(var_2))

# Task 3

print(id(str(a)) == id(float(b)) == id(c))

print(id(tuple(var_1)) == id(tuple(var_2)))

# Task 4

input_str = input("Введите произвольную строку: ")
even_nums = ''
odd_nums = ''

for i in input_str:
    if i.isdigit():
        if int(i) % 2 == 0:
            even_nums = even_nums.split()
            even_nums.append(i)
            even_nums = ''.join(even_nums)
        else:
            odd_nums = odd_nums.split()
            odd_nums.append(i)
            odd_nums = ''.join(odd_nums)

print('Введена строка: "', input_str, sep="", end='"\n\n')

print(even_nums, odd_nums, sep="     ", end="\n!!!")
