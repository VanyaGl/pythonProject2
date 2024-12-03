
matrix = []
with open('GlushkoIvanEvgenevich_UB42_vvod.txt', 'r') as file:
    for line in file:
        row = list(map(int, line.split()))
        matrix.append(row)


# Инициализируем переменные для хранения максимальной и минимальной суммы элементов строк
max_sum = float('-inf')
min_sum = float('inf')
max_row_index = -1
min_row_index = -1

# Перебираем все строки матрицы
for i, row in enumerate(matrix):

    row_sum = sum(row)

   
    if row_sum > max_sum:
        max_sum = row_sum
        max_row_index = i
    if row_sum < min_sum:
        min_sum = row_sum
        min_row_index = i

# Записываем результаты в файл vivod.txt
with open('GlushkoIvanEvgenevich_UB42_vivod.txt', 'w') as file:
    file.write(f"Строка с наибольшей суммой: {matrix[max_row_index]}, Сумма: {max_sum}\n")
    file.write(f"Строка с наименьшей суммой: {matrix[min_row_index]}, Сумма: {min_sum}\n")






