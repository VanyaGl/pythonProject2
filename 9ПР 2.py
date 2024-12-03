# Функция для проверки, является ли число простым с использованием рекурсии.
def is_prime(n, divisor=2):
    # Если число меньше 2, оно не является простым.
    if n < 2:
        return False


    if n % divisor == 0:
        return False

    # простым.
    if divisor * divisor > n:
        return True

    # Рекурсивно вызываем функцию с увеличенным делителем.
    return is_prime(n, divisor + 1)

.
n = int(input("Введите натуральное число: "))

# Проверяем, является ли число n простым с помощью функции is_prime.
if is_prime(n):
    ".
    print("yes")
else:
    .
    print("no")





