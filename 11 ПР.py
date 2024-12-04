root.mainloop()
import tkinter as tk
from tkinter import messagebox, filedialog, ttk

# Функция для выполнения операций калькулятора
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()
        if operation == '+':
            result.set(num1 + num2)
        elif operation == '-':
            result.set(num1 - num2)
        elif operation == '*':
            result.set(num1 * num2)
        elif operation == '/':
            result.set(num1 / num2)
    except ValueError:
        result.set("Ошибка")

# Функция для обработки нажатия кнопки на второй вкладке
def show_selection():
    selected = []
    if check_var1.get():
        selected.append(1)
    if check_var2.get():
        selected.append(2)
    if check_var3.get():
        selected.append(3)
    messagebox.showinfo("Выбор", f"Вы выбрали {', '.join(map(str, selected))} вариант(ы)")

# Функция для загрузки текстового файла на третьей вкладке
def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("Текстовые файлы", "*.txt")])
    if file_path:
        messagebox.showinfo("Загрузка файла", f"Файл {file_path} загружен")

# Создание основного окна
root = tk.Tk()
root.title("Глушко Иван Евгеньевич")

# Создание вкладок
tab_control = tk.ttk.Notebook(root)

# Первая вкладка - калькулятор
tab1 = tk.ttk.Frame(tab_control)
tab_control.add(tab1, text='Калькулятор')

tk.Label(tab1, text="Число 1:").grid(row=0, column=0, padx=10, pady=10)
entry_num1 = tk.Entry(tab1)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(tab1, text="Операция:").grid(row=1, column=0, padx=10, pady=10)
operation_var = tk.StringVar(value='+')
operation_menu = tk.OptionMenu(tab1, operation_var, '+', '-', '*', '/')
operation_menu.grid(row=1, column=1, padx=10, pady=10)

tk.Label(tab1, text="Число 2:").grid(row=2, column=0, padx=10, pady=10)
entry_num2 = tk.Entry(tab1)
entry_num2.grid(row=2, column=1, padx=10, pady=10)

calculate_button = tk.Button(tab1, text="Вычислить", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

result = tk.StringVar()
result_label = tk.Label(tab1, textvariable=result)
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Вторая вкладка - чекбоксы
tab2 = tk.ttk.Frame(tab_control)
tab_control.add(tab2, text='Чекбоксы')

check_var1 = tk.BooleanVar()
check_var2 = tk.BooleanVar()
check_var3 = tk.BooleanVar()

check1 = tk.Checkbutton(tab2, text="Вариант 1", variable=check_var1)
check1.grid(row=0, column=0, padx=10, pady=10)

check2 = tk.Checkbutton(tab2, text="Вариант 2", variable=check_var2)
check2.grid(row=1, column=0, padx=10, pady=10)

check3 = tk.Checkbutton(tab2, text="Вариант 3", variable=check_var3)
check3.grid(row=2, column=0, padx=10, pady=10)

show_button = tk.Button(tab2, text="Показать выбор", command=show_selection)
show_button.grid(row=3, column=0, pady=10)

# Третья вкладка - загрузка файла
tab3 = tk.ttk.Frame(tab_control)
tab_control.add(tab3, text='Загрузка файла')

load_button = tk.Button(tab3, text="Загрузить файл", command=load_file)
load_button.grid(row=0, column=0, pady=10)

# Добавление вкладок в основное окно
tab_control.pack(expand=1, fill='both')

# Запуск основного цикла
