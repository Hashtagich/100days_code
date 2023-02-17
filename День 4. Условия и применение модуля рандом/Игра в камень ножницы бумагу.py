print('Приветствую в игре камень ножницы бумага')
gamer=input("Что вы выберете 'бумага', 'ножницы' или 'камень'?\n")
import random
list_move_pc = ['камень', 'ножницы', 'бумага']
number_in_list = random.randint(0, len(list_move_pc) - 1) # можно прописать number_in_list = random.choice(list_move_pc) и потом print(number_in_list)
print(list_move_pc[numbeinlist])
if gamer==list_move_pc[numbeinlist]:
    print('И у меня ' + list_move_pc[numbeinlist] + ", значит у нас ничья. Спасибо за игру!")
elif (gamer=='бумага' and list_move_pc[numbeinlist]=='ножницы') or (gamer=='ножницы' and list_move_pc[numbeinlist]=='камень')or (gamer=='камень' and list_move_pc[numbeinlist]=='бумага'):
    print('А у меня ' + list_move_pc[numbeinlist] + ", значит я победил. Спасибо за игру!")
elif (gamer=='бумага' and list_move_pc[numbeinlist]=='камень') or (gamer=='ножницы' and list_move_pc[numbeinlist]=='бумага')or (gamer=='камень' and list_move_pc[numbeinlist]=='ножницы'):
    print('А у меня ' + list_move_pc[numbeinlist] + ", значит вы победили. Спасибо за игру!")
else:
    print(list_move_pc[numbeinlist] + ", но вы загадали что-то другое так что этот матч не считается. Нужно было загадать 'бумага', 'камень' или 'ножницы'. Попробуем в другой раз!")

