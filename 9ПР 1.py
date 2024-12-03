
def sum_of_digits(n):

    if n == 0:
        return 0
    else:

        last_digit = n % 10

        remaining_number = n // 10

        return last_digit + sum_of_digits(remaining_number)

N = int(input("Введите натуральное число: "))
result = sum_of_digits(N)
print("Сумма цифр числа:", result)



