import pandas

names_file_squirrels = '2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv'
data = pandas.read_csv(names_file_squirrels)


gray_squirrels_count = len(data[data['Primary Fur Color'] == 'Gray'])
black_squirrels_count = len(data[data['Primary Fur Color'] == 'Black'])
red_squirrels_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
data_dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    ' Count': [gray_squirrels_count, red_squirrels_count, black_squirrels_count]

}

df = pandas.DataFrame(data_dict)
df.to_csv('squirrels_count.csv')

