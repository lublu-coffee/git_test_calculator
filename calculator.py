def plus(a, b):
    print(f'Сумма: {a} + {b} = ', a + b)


def minus(a, b):
    print(f'Разность: {a} - {b} = ', a - b)


def multiplication(a, b):
    print(f'Умножение: {a} * {b} = ', a * b)


def deletion(a, b):
    try:
        c = a / b
        print(f'Деление: {a} / {b} = ', c)
    except ZeroDivisionError:
        print("На ноль делить нельзя  !!!!")

def deletion_ostatok(a, b):
    try:
        c = a % b
        print(f'Деление с остатком: {a} % {b} = ', c)
    except ZeroDivisionError:
        print("На ноль делить нельзя  !!!!")


a = int(input('Введите 1 число : '))
b = int(input('Введите 2 число : '))

plus(a, b)
minus(a, b)
multiplication(a, b)
deletion(a, b)