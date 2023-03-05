def sqare(x):
    return x * x


def cube(x):
    return x ** 3


def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def calculate(f, a, b=0):
    try:
        return f(a, b)
    except TypeError:
        return f(a)


def calculator(operation, argument):
    return operation(argument)


print('-----------')

print(calculator(sqare, 5))
print(calculator(cube, 5))
print(calculator(print, 5))
print(calculate(mul, 2, 3))
print(calculate(add, 3, 4))
print(calculate(cube, 5))
