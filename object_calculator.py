class Calculator:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    @property
    def number_1(self):
        return self.__a

    @number_1.setter
    def number_1(self, a):
        self.__a = int(a)

    @property
    def number_2(self):
        return self.__b

    @number_2.setter
    def number_2(self, b):
        self.__b = int(b)

    def plus(self):
        self.print_result('Сумма', self.__a + self.__b)

    def minus(self):
        self.print_result('Разность', self.__a - self.__b)

    def print_result(self, action, result):
        print(f'{action}: {self.__a} и {self.__b} = ', result)


z = Calculator(2, 3)
z.plus()
z.minus()