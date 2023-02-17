import pandas

name_file_csv = 'nato_phonetic_alphabet.csv'

data = pandas.read_csv(name_file_csv)
nato_dict = {row.letter: row.code for index, row in data.iterrows()}


def nato():
    word_guess = input("Ведите слово: ")
    try:
        result = [nato_dict[i] for i in word_guess.upper()]
    except KeyError:
        print("Вы ввели что-то помимо букв. Введите слово на английском без знаков и цифр.")
        nato()
    else:
        print(result)


nato()
