from tkinter import *

K = 1.60934


def calculate():
    mill = wind_input.get()
    result = round(float(mill) * K, 2)
    label_answer.config(text=result)


# Рабочая область
window = Tk()
window.title('Перевод из миль в км')  # Название
window.minsize(width=300, height=200)  # Размеры экрана
window.config(padx=50, pady=50)  # Устанавливаем отступ от границ

# Кнопка расчёта
boot_calcul = Button(text='Рассчитать', command=calculate)
boot_calcul.grid(row=2, column=1)
boot_calcul.config(padx=20, pady=20)  # Устанавливаем отступ от границ кнопки

# Ярлык миль
label_mill = Label(text='Мили')
label_mill.grid(row=0, column=2)
label_mill.config(padx=20, pady=20)  # Устанавливаем отступ от границ ярлыка

# Ярлык км
label_km = Label(text='Км')
label_km.grid(row=1, column=2)
label_km.config(padx=20, pady=20)  # Устанавливаем отступ от границ ярлыка

# Ярлык перевода (текст)
label_text = Label(text='равняется =')
label_text.grid(row=1, column=0)
label_text.config(padx=20, pady=20)  # Устанавливаем отступ от границ ярлыка

# Ярлык результат (цифра в км)
label_answer = Label(text='0')
label_answer.grid(row=1, column=1)
label_answer.config(padx=20, pady=20)  # Устанавливаем отступ от границ ярлыка

# Окошко ввода миль
wind_input = Entry(width=7)
wind_input.grid(row=0, column=1)

window.mainloop()  # Функция чтобы экран не закрывался
