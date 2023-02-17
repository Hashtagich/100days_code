from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
BG_TRUE = 'green'
BG_FALSE = 'red'
NAME_PNG_TRUE = 'images/true.png'
NAME_PNG_FALSE = 'images/false.png'
COLOR_TEXT_SCORE = 'white'
FONT_TEXT_QUESTION = ('Arial', 20, 'italic')
FONT_TEXT_SCORE = ('Arial', 12, 'italic')
Milliseconds = 2000


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Холст с текстом (вопросом)
        self.canvas = Canvas(width=300, height=250, bg=COLOR_TEXT_SCORE)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Что-то",
            fill=THEME_COLOR,
            font=FONT_TEXT_QUESTION)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=50, pady=50)

        # Кнопки
        self.true_png = PhotoImage(file=NAME_PNG_TRUE)
        self.true_button = Button(image=self.true_png, highlightthickness=0, command=self.push_true)
        self.true_button.grid(row=2, column=1)

        self.false_png = PhotoImage(file=NAME_PNG_FALSE)
        self.false_button = Button(image=self.false_png, highlightthickness=0, command=self.push_false)
        self.false_button.grid(row=2, column=0)

        # Ярлыки
        self.score_lab = Label(text=f'Результат: 0', bg=THEME_COLOR, fg=COLOR_TEXT_SCORE,
                               font=FONT_TEXT_SCORE, justify=LEFT)
        self.score_lab.grid(row=0, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg=COLOR_TEXT_SCORE)
        if self.quiz.still_has_questions():
            self.score_lab.config(text=f'Результат: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='Вопросы закончились. \nИгра окончена!')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def push_true(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def push_false(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg=BG_TRUE)
        else:
            self.canvas.config(bg=BG_FALSE)
        self.window.after(Milliseconds, self.get_next_question)
