import math


def dy_dx(x, y):
    return x + math.cos(y / math.sqrt(5))


def euler_method(dy_dx, x0, y0, xn, n):
    x_values = [x0]
    y_values = [y0]
    i = x0
    while i <= xn:
        x = x_values[-1]
        y = y_values[-1]
        y_prime = dy_dx(x, y)
        x_new = x + n
        y_new = y + n * y_prime
        x_values.append(x_new)
        y_values.append(y_new)
        i += n
    return x_values, y_values


x0 = 1.8
y0 = 2.6
xn = 2.8
n = 0.1

x_values, y_values = euler_method(dy_dx, x0, y0, xn, n)

# Виведемо результати
for x, y in zip(x_values, y_values):
    print(f"x = {x}, y = {y}")
