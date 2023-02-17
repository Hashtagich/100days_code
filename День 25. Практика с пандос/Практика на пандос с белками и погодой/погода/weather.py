import pandas

name_csv_file = 'погода.csv'

data = pandas.read_csv(name_csv_file)
max_temp = data.температура.max()


monday = data[data.день == 'понедельник']
monday_temp = monday.температура
print(273+ int(monday_temp))
