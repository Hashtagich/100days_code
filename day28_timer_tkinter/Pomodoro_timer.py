if __name__ == "__main__":

    from tkinter import *
    from math import floor

    PINK = '#e2979c'
    RED = '#e7905b'
    GREEN = "#9bdeac"
    YELLOW = '#f7f5dd'
    TIMER_MILLISECONDS = 1000  # микросекунды
    FONT_NAME = ('Courier', 35, 'bold')
    TIME_WORK = 25  # 25 минут работы на каждую сессию (4 сессии)
    TIME_BREAK = 5  # 5 минут перерыв (первые 3 сессии)
    TIME_BREAK_FINISH = 20  # 20 минут перерыв (4-ая сессии)
    PARAMETERS_FONT_LABEL = ('Courier', 35, 'bold')
    PARAMETERS_FONT_BUTTON = ('Courier', 14, 'bold')
    PARAMETERS_FONT_SES = ('Courier', 18, 'bold')

    name_file_pomodoro = 'tomato.png'
    reps = 0
    timer = ''


    def push_reset():
        window.after_cancel(timer)
        label_task.config(text='')
        canvas.itemconfig(timer_text, text=f'00:00')
        label_info.config(text='Таймер')


    def push_start():
        global reps
        work_sec = TIME_WORK * 60
        break_sec = TIME_BREAK * 60
        long_break_sec = TIME_BREAK_FINISH * 60

        reps += 1

        if reps % 8 == 0:
            label_info.config(text='Время для долгого перерыва', bg=YELLOW, fg=RED, highlightthickness=0)
            count_down(long_break_sec)
        elif reps % 2 == 0:
            label_info.config(text='Время для небольшого перерыва', bg=YELLOW, fg=PINK, highlightthickness=0)
            count_down(break_sec)
        else:
            label_info.config(text='Пора работать', bg=YELLOW, fg=GREEN, highlightthickness=0)
            count_down(work_sec)


    def count_down(count):
        count_min = floor(count / 60)
        if 10 > count_min:
            count_min = f'0{count_min}'

        count_sec = count % 60
        if 10 > count_sec:
            count_sec = f'0{count_sec}'

        canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
        if count > 0:
            global timer
            timer = window.after(TIMER_MILLISECONDS, count_down, count - 1)
        else:
            push_start()
            mark = ''
            work_ses = floor(reps/2)
            for _ in range(work_ses):
                mark += '✔'
            label_task.config(text=mark)


    # Рабочая область
    window = Tk()
    window.title('Pomodoro timer')  # Название
    window.config(padx=50, pady=50, bg=YELLOW)  # Устанавливаем отступ от границ

    # Холст для заливки и наложения изображений
    canvas = Canvas(width=210, height=230, bg=YELLOW, highlightthickness=0)
    tomato_img = PhotoImage(file=name_file_pomodoro)
    canvas.create_image(105, 115, image=tomato_img)
    timer_text = canvas.create_text(103, 130, text='00:00', fill='white', font=FONT_NAME)
    canvas.grid(row=1, column=1)

    # Ярлык таймера, текст будет менять через функцию push_start
    label_info = Label(text='Таймер', font=PARAMETERS_FONT_LABEL, bg=YELLOW, fg=GREEN, highlightthickness=0)
    label_info.grid(row=0, column=1)
    label_info.config(padx=20, pady=20)

    # Ярлык выполнения сессий
    label_task = Label(font=PARAMETERS_FONT_SES, bg=YELLOW, fg=GREEN, highlightthickness=0)
    label_task.grid(row=3, column=1)
    label_task.config(padx=20, pady=20)

    # Кнопка Старт
    button_start = Button(text='Старт', font=PARAMETERS_FONT_BUTTON, command=push_start, highlightthickness=0)
    button_start.grid(row=2, column=0)

    # Кнопка Сброс
    button_reset = Button(text='Сброс', font=PARAMETERS_FONT_BUTTON, command=push_reset, highlightthickness=0)
    button_reset.grid(row=2, column=2)

    window.mainloop()
