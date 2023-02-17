from turtle import Turtle, Screen
import pandas

FONT_NAME_STATES = ("Arial", 8, "normal")

answer_list = []
states_list = []
name_image = 'blank_states_img.gif'
name_csv_file = '50_states.csv'
name_txt_file = 'Кол-во не угаданных штатов.txt'
name_finish_csv_file = 'Кол-во не угаданных штатов.csv'
data = pandas.read_csv(name_csv_file)
all_states_list = data['state'].to_list()


def write_word(word, position_x_y):  # функция отображения штат на карте по заданным координатам
    t_writer.goto(position_x_y)
    t_writer.write(word, align="center", font=FONT_NAME_STATES)


def title_state():
    new_state = screen.textinput(title=f'{len(states_list)}/50 Штатов угадано.', prompt='Введите другой штат').title()
    return new_state


def return_position_state(name_state):
    www = data[data['state'] == name_state]
    x_position, y_position = int(www.x), int(www.y)
    return x_position, y_position


def game_over_txt():
    answer_list.append("Не угаданные штаты\n")
    for i in all_states_list:
        if i not in states_list:
            answer_list.append(i + '\n')

    with open(name_txt_file, 'w', encoding='utf-8') as file:
        file.writelines(answer_list)


def game_over_csv():
    for i in states_list:
        all_states_list.remove(i)

    dict_state = {"State": all_states_list}
    export_file = pandas.DataFrame(dict_state)
    export_file.to_csv(name_finish_csv_file)


t_map = Turtle()
t_writer = Turtle()
screen = Screen()

screen.title('U.S. States Game')
screen.addshape(name_image)
t_map.shape(name_image)
t_writer.hideturtle()
t_writer.penup()

user_word = screen.textinput(title=f'Викторина на запоминание штатов.', prompt='Введите штат').title()
# Начало игры, запрос штата и отображение его на карте
if user_word in all_states_list:
    position = return_position_state(user_word)
    states_list.append(user_word)
    write_word(user_word, position)
# Запуск цикла и прекращение только при вводе 'exit' или при заполнении карты 50 штатами
while len(states_list) != 50:
    state_user = title_state()
    if state_user == 'Exit'.title():
        break
    elif state_user not in states_list and state_user in all_states_list:
        position = return_position_state(state_user)
        states_list.append(state_user)
        write_word(state_user, position)
    else:
        continue
# После цикла запрос в каком формате сохранить файл со штатами, что не назвали
answer = screen.textinput(title='Формат документа', prompt='В каком формате сохранить документ "csv" или "txt"?')

if answer.lower() == 'csv':
    game_over_csv()
else:
    game_over_txt()

screen.exitonclick()
