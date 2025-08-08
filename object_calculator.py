class Calculator:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def plus(self):
        self.print_result('Сумма', self.__a + self.__b)

    def minus(self):
        self.print_result('Разность', self.__a - self.__b)

    def print_result(self, action, result):
        print(f'{action}: {self.__a} и {self.__b} = ', result)


z = Calculator(2, 3)
z.plus()
z.minus()