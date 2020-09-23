from scipy.optimize import golden


a = 5
b = 7


def f(x):
    return (x + a)**2 - b


def g(x):
    return abs(f(x))


print(f'min f = {golden(f)}, \nmin g = {golden(g)}')



# График функций в диапазоне [10, - 10]
# y = f(x) f(x) = (x + a) ** 2 - b
