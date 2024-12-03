
n=int(input('Введите количество строк: '))
m=int(input('Введите количество столбцов: '))
matrix = []
for i in range(n):
    b=[]
    for i in range(m):
        b.append(int(input('Введите элемент матрицы: ')))
    matrix.append(b)



max_sum = float('-inf')
min_sum = float('inf')


max_row_index = -1
min_row_index = -1


for i, row in enumerate(matrix):

    row_sum = sum(row)

    if row_sum > max_sum:
        max_sum = row_sum
        max_row_index = i


    if row_sum < min_sum:
        min_sum = row_sum
        min_row_index = i


print(f"Строка с наибольшей суммой: {matrix[max_row_index]}, Сумма: {max_sum}")
print(f"Строка с наименьшей суммой: {matrix[min_row_index]}, Сумма: {min_sum}")