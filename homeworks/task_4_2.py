from datetime import datetime
from time import sleep

# Task 1

dic_1 = {1: "Hello", 2: "World", 3: "!"}

dic_2 = {value: key for key, value in dic_1.items()}

print(dic_2)


# Task 2

def find_factorial(num):
    if num == 1:
        return num
    else:
        return num * find_factorial(num - 1)


print(find_factorial(4))

# Task 3

num_list = [1, 22, 333, 1, 333, 333, 22, 333, 22]


# print(num_list.count(333))

# Key - значение, value - сколько раз встречается
def count_num(l):
    dic = {}

    for i in num_list:
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1

    return dic


print(count_num(num_list))


# Task 4

def take_time(n):
    for i in range(n):
        yield datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        sleep(1)


list_1 = [i for i in take_time(5)]

print(list_1)
