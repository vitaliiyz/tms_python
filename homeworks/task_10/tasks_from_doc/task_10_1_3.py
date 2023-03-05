def file_generator(file_name: str):
    with open(file_name) as file:
        for line in file:
            yield line


generator = file_generator("file.txt")

print(next(generator), end="")
print(next(generator), end="")
print(next(generator), end="")
