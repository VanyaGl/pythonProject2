# Функция для проверки, является ли число простым с использованием рекурсии.
def is_prime(n, divisor=2):
    # Если число меньше 2, оно не является простым.
    if n < 2:
        return False

    # Если число делится на текущий делитель без остатка, оно не является простым.
    if n % divisor == 0:
        return False

    # Если текущий делитель больше или равен квадратному корню из n, число является простым.
    if divisor * divisor > n:
        return True

    # Рекурсивно вызываем функцию с увеличенным делителем.
    return is_prime(n, divisor + 1)

# Вводим натуральное число n с клавиатуры.
with open('GlushkoIvanEvgenevich_UB42_vvod2.txt', 'r', encoding='utf-8') as file:
    n = int(file.read())

# Проверяем, является ли число n простым с помощью функции is_prime.
if is_prime(n):
    # Если число простое, выводим "yes".
    with open(filename, 'w', encoding='utf-8') as file:
        file.write('YES')
else:
    # Если число составное, выводим "no".
    with open('GlushkoIvanEvgenevich_UB42_vivod2.txt', 'w', encoding='utf-8') as file:
        file.write('NO')
