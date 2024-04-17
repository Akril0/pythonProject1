import math


# Визначення функції g(x) = sin(x) + 0.25
def g(x):
    return math.sin(x) + 0.25


# Початкове наближення
x0 = 0

# Точність, до якої ми хочемо знайти корінь
epsilon = 1e-6

# Кількість ітерацій
max_iter = 1000

# Початок ітераційного процесу
for i in range(max_iter):
    x1 = g(x0)  # Застосовуємо ітераційну формулу
    print("[", i, "]", x1)
    if abs(x1 - x0) < epsilon:
        break  # Перевіряємо точність
    x0 = x1  # Оновлюємо значення x0 для наступної ітерації

print("Розв'язок:", x1)