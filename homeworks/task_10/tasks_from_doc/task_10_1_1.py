class MyOpen:
    def __init__(self, file_name: str, method: str):
        self._file_name = file_name
        self._method = method
        self._file = None

    @property
    def file_name(self):
        return self._file_name

    @property
    def method(self):
        return self._method

    @property
    def file(self):
        return self._file

    @file.setter
    def file(self, value):
        self._file = value

    def __enter__(self):
        self.file = open(self.file_name, self.method)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.file.close()


with MyOpen("tasks_from_doc/file.txt", "w+") as f:
    f.write("Hello, Daniel!\n")
    f.write("How are you doing?\n")
    f.write("What are you doing next weekend?")
    f.seek(0)
    print(f.read())
