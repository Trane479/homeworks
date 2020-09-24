from fib.fibonacci_gen import fibonacci


amount_of_numbers = int(input('Введите желаемое количество чисел Фибоначчи - '))
print(list(fibonacci(amount_of_numbers)))