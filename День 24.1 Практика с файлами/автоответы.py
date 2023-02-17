name_file = './Input/Names/invited_names.txt'
string = 'example.docx'
way_starting_letter = './Input/Letters/starting_letter.txt'
way_answer_letter = './Output/ReadyToSend/answer_'
end_way_starting_letter = '.docx'

with open(name_file, 'rt', encoding='utf-8') as file:
    text_name = file.readlines()
    list_name = [i.strip() for i in text_name]

with open(way_starting_letter, 'rt', encoding='utf-8') as letter:
    text = letter.read()


for i in list_name:
    answer_letter = way_answer_letter + i + end_way_starting_letter
    with open(answer_letter, 'w', encoding='utf-8') as answer:
        new_line = text
        new_line = new_line.replace('[name]', i)
        answer.writelines(new_line)
