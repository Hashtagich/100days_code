# Задание №1
fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print('Это происходит потому, что мы просматриваем список фруктов в поисках индекса, который находится '
              'вне диапазона')

    else:
        print(fruit + " pie")


# make_pie(4)

# Задание №2
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0
try:
    for post in facebook_posts:
        total_likes = total_likes + post['Likes']
except KeyError:
    print(f'Likes')
else:
    print(total_likes)
