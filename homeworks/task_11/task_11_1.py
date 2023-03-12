def geom_prog(a_1, q):
    while True:
        yield a_1
        a_1 *= q


def print_result(n, generator):
    for i in range(1, n + 1):
        print(f"a_{i} = {next(generator)}")
        if i == n:
            generator.close()


g = geom_prog(2, 3)
print_result(5, g)
