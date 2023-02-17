from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:

    q = i['question']
    a = i['correct_answer']
    question = Question(q_text=q, q_answer=a)
    question_bank.append(question)


quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f'Your final score was: {quiz.score}/{quiz.question_number}')
# print(question_bank[0].text) принт вопроса ответа
# print(question_bank[0].answer) принт вопроса
