import tkinter


def button_click():  # Функция для кнопки, срабатывает при нажатии
    word = wind_input.get()
    first_label.config(text=word)


# Рабочая область
window = tkinter.Tk()
window.title('Первая графическая программа')  # Название
window.minsize(width=500, height=300)  # Размеры экрана
window.config(padx=20, pady=20)  # Устанавливаем отступ от границ, на ярлыки, кнопки и прочее можно также использовать
# личные отступы от них индивидуально

# Лейбл
first_label = tkinter.Label(text='Тест лейбла', font=('Arial', 10, 'bold'))  # Создаём лейбл присваивая ему св-ва класса
first_label.grid(row=0, column=0)  # Отображаем на экране

# Кнопка
button = tkinter.Button(text='Не нажимай!', command=button_click)  # Создаём кнопку присваивая ей свойства класса
button.grid(row=1, column=1)  # Отображаем на экране

# Окошко ввода
wind_input = tkinter.Entry(width=10)  # Создаём окошко ввода присваивая ему свойства класса
wind_input.grid(row=2, column=3)  # Отображаем на экране

# Кнопка_2
button_2 = tkinter.Button(text='Хочешь? Нажми.', command=button_click)  # Создаём кнопку присваивая ей свойства класса
button_2.grid(row=0, column=2)  # Отображаем на экране

window.mainloop()  # Функция чтобы экран не закрывался
