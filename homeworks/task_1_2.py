from math import sqrt


# Task 1
def sum_dif_mul(x, y):
    print("Sum:", x + y)
    print("Difference:", x - y)
    print("Multiplication:", x * y)


sum_dif_mul(10, 20)


# Task 2
def math_operation(x, y):
    result = (abs(x) - abs(y)) / (1 + abs(x * y))
    print("Result:", result)


math_operation(-20, 5)


# Task 3
def cube(x):
    vol = x ** 3
    area = 6 * (x ** 2)

    print("Volume:", vol)
    print("Area:", area)


cube(5)


# Task 4
def arith_geo_mean(x, y):
    arith_mean = (x + y) / 2
    geo_mean = (x + y) ** 0.5

    print("Arithmetic mean:", arith_mean)
    print("Geometric mean:", geo_mean)


arith_geo_mean(6, 3)


# Task 5
def right_triangle(x, y):
    hypotenuse = sqrt(pow(x, 2) + pow(y, 2))
    area = 0.5 * (x * y)

    print("Hypotenuse:", hypotenuse)
    print("Area:", area)


right_triangle(3, 4)
