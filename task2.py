import math


# Визначення функції, яку ми інтегруємо
def f(x):
    return math.log(x + 2, 10) / x


# Формула трапецій для обчислення визначеного інтегралу
def trapezoidal_rule(a, b, n):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        result += f(a + i * h)
    result *= h
    return result


# Визначені межі і кількість трапецій
a = 1.2
b = 2
n = 1000  # Збільшіть значення n для отримання більшої точності

# Обчислення інтегралу за допомогою формули трапецій
integral = trapezoidal_rule(a, b, n)
print("Значення інтегралу:", integral)
