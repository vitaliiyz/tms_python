from exceptions import NotANumberError


class Calculator:
    def __init__(self):
        self._result = 0

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, new_result):
        self._result = new_result

    def reset(self):
        self.result = 0

        return self.result

    def addition(self, a, b=None):
        try:
            self._is_num(a, b)
        except NotANumberError as e:
            print(e)
            return

        if b is None:
            self.result += a
        else:
            self.result = a + b

        return self.result

    def subtraction(self, a, b=None):
        try:
            self._is_num(a, b)
        except NotANumberError as e:
            print(e)
            return

        if b is None:
            self.result -= a
        else:
            self.result = b + a

        return self.result

    def multiplication(self, a, b=None):
        try:
            self._is_num(a, b)
        except NotANumberError as e:
            print(e)
            return

        if b is None:
            self.result *= a
        else:
            self.result = a * b

        return self.result

    def division(self, a, b=None):
        try:
            self._is_num(a, b)
        except NotANumberError as e:
            print(e)
            return

        if b is None:
            try:
                self.result /= a
            except ZeroDivisionError:
                print("На ноль делить нельзя")
                return
        else:
            try:
                self.result = a / b
            except ZeroDivisionError:
                print("На ноль делить нельзя")
                return

        return self.result

    @staticmethod
    def _is_num(a, b):
        if not (isinstance(a, (int, float))):
            raise NotANumberError("Введено неверное значение")
        elif not (isinstance(b, (int, float)) or b is None):
            raise NotANumberError("Введено неверное значение")


calc = Calculator()

print(calc.addition(1, 1))
print(calc.addition(1.5))
print(calc.addition("a"))

print(calc.multiplication(4))
print(calc.multiplication(3, "a"))
print(calc.multiplication(2, 3))

print(calc.reset())

print(calc.subtraction(3))
print(calc.subtraction(5, 10))
print(calc.subtraction(0))
print(calc.subtraction("1", 2))
print(calc.subtraction(1, 0))

print(calc.division(3))
print(calc.division(5, 10))
print(calc.division(0))
print(calc.division("1", 2))
print(calc.division(1, 0))
print(calc.result)
