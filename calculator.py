def plus(a, b):
    print(f'Сумма: {a} + {b} = ', a + b)


def minus(a, b):
    print(f'Разность: {a} - {b} = ', a - b)


def multiplication(a, b):
    print(f'Умножение: {a} * {b} = ', a * b)


a = int(input('Введите 1 число : '))
b = int(input('Введите 2 число : '))

plus(a, b)
minus(a, b)
multiplication(a, b)