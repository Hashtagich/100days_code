from tkinter import Tk, Button, Canvas, PhotoImage
from pandas import *
from random import choice

BG_COLOR = '#B1DDC6'
FONT_TITLE = ('Arial', 40, 'italic')
FONT_WORD = ('Arial', 60, 'bold')
IMAGE_CARD_BACK = 'images/card_back.png'
IMAGE_CARD_FRONT = 'images/card_front.png'
IMAGE_RIGHT = 'images/right.png'
IMAGE_WRONG = 'images/wrong.png'
CSV_FILE_START = 'data/french_words.csv'
CSV_FILE_WORD_TO_LEARN = 'Слова для запоминания.csv'
MILLISECOND = 5000

language_1 = 'French'
language_2 = 'English'
next_dict = {}
to_learn = {}


def next_card():
    global next_dict, flip_time
    window.after_cancel(flip_time)
    next_dict = choice(to_learn)
    next_word = next_dict[language_1]
    canvas.itemconfig(card_title, text=language_1, fill='black')
    canvas.itemconfig(card_word, text=next_word, fill='black')
    canvas.itemconfig(card_bg, image=front_card)
    flip_time = window.after(MILLISECOND, func=flip_card)


def flip_card():
    next_word = next_dict[language_2]
    canvas.itemconfig(card_title, text=language_2, fill='white')
    canvas.itemconfig(card_word, text=next_word, fill='white')
    canvas.itemconfig(card_bg, image=back_card)


def i_know():
    to_learn.remove(next_dict)
    data_s = DataFrame(to_learn)
    data_s.to_csv(CSV_FILE_WORD_TO_LEARN, index=False)
    next_card()


try:
    data = read_csv(CSV_FILE_WORD_TO_LEARN)
except FileNotFoundError:
    first_data = data = read_csv(CSV_FILE_START)
    to_learn = first_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')

window = Tk()  # Рабочая область
window.title('Карточки на запоминание слов')
window.config(padx=50, pady=50, bg=BG_COLOR)

flip_time = window.after(MILLISECOND, func=flip_card)

canvas = Canvas(width=800, height=526)  # Холст для заливки и наложения изображений
front_card = PhotoImage(file=IMAGE_CARD_FRONT)
back_card = PhotoImage(file=IMAGE_CARD_BACK)
card_bg = canvas.create_image(400, 263, image=front_card)
card_title = canvas.create_text(400, 150, text='', font=FONT_TITLE)
card_word = canvas.create_text(400, 263, text='', font=FONT_WORD)
canvas.config(bg=BG_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Кнопки
wrong = PhotoImage(file=IMAGE_WRONG)  # кнопка "Не верно"
wrong_button = Button(image=wrong, bg=BG_COLOR, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right = PhotoImage(file=IMAGE_RIGHT)  # кнопка "Верно"
right_button = Button(image=right, bg=BG_COLOR, highlightthickness=0, command=i_know)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
