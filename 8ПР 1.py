# Определяем матрицу, которая представляет собой список списков.
# Каждый внутренний список — это строка матрицы, содержащая числа.
n=int(input('Введите количество строк: '))
m=int(input('Введите количество столбцов: '))
matrix = []
for i in range(n):
    b=[]
    for i in range(m):
        b.append(int(input('Введите элемент матрицы: ')))
    matrix.append(b)


# Инициализируем переменные для хранения максимальной и минимальной суммы элементов строк.
# float('-inf') означает минус бесконечность, а float('inf') — плюс бесконечность.
# Это делается для того, чтобы любая сумма строки была больше max_sum и меньше min_sum при первом сравнении.
max_sum = float('-inf')
min_sum = float('inf')

# Инициализируем переменные для хранения индексов строк с наибольшей и наименьшей суммой.
# -1 используется как начальное значение, чтобы указать, что индексы строк еще не найдены.
max_row_index = -1
min_row_index = -1

# Перебираем все строки матрицы с помощью цикла for.
# enumerate(matrix) позволяет нам получить как индекс строки (i), так и саму строку (row).
for i, row in enumerate(matrix):
    # Вычисляем сумму элементов текущей строки с помощью функции sum().
    # sum(row) складывает все числа в строке row.
    row_sum = sum(row)

    # Проверяем, является ли текущая сумма строки больше, чем max_sum.
    # Если да, то обновляем max_sum и запоминаем индекс текущей строки в max_row_index.
    if row_sum > max_sum:
        max_sum = row_sum
        max_row_index = i

    # Проверяем, является ли текущая сумма строки меньше, чем min_sum.
    # Если да, то обновляем min_sum и запоминаем индекс текущей строки в min_row_index.
    if row_sum < min_sum:
        min_sum = row_sum
        min_row_index = i

# После завершения цикла выводим строки с наибольшей и наименьшей суммой и их суммы.
# matrix[max_row_index] — это строка с наибольшей суммой.
# matrix[min_row_index] — это строка с наименьшей суммой.
print(f"Строка с наибольшей суммой: {matrix[max_row_index]}, Сумма: {max_sum}")
print(f"Строка с наименьшей суммой: {matrix[min_row_index]}, Сумма: {min_sum}")