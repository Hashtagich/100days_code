print("Добро пожаловать в мини-квест Остров сокровищ")
print("Ваша задача найти сокровища")
way = input("Куда Вы повернёте налево или направо\n")
if way == "налево":
    water = input("Вы достигли края берега. Что Вы сделаете поплывёте или подождёте лодку?\n")
    if water == "поплыву":
        print("Gave over")
    else:
        door = input("Перед Вами 3 двери, какую выберете? Желтую, красную или зелёную\n")
        if door == "зелёную":
            print("вы победили")
        elif door == "красную":
            print("Gave over")
        elif door == "желтую":
            print("Gave over")
        else:
            print("Gave over")
else:
    print("Gave over")
