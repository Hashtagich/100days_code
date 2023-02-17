row1 = ['_', '_', '_']
row2 = ['_', '_', '_']
row3 = ['_', '_', '_']
maps = [row1, row2, row3]
print(f'{row1}\n{row2}\n{row3}')
position = int(input("Where do you want to put the treasure?\nКуда ты хочешь спрятать сокровище?\n"))  #
# первое число столбец, второе ряд
if int(position) % 10 == 1:
    if position//10 == 1:
        row1[position//10-1] = "X"
    elif position//10 == 2:
        row1[position//10-1] = "X"
    elif position//10 == 3:
        row1[position//10-1] = "X"
elif int(position) % 10 == 2:
    if position//10 == 1:
        row2[position//10-1] = "X"
    elif position//10 == 2:
        row2[position//10-1] = "X"
    elif position//10 == 3:
        row2[position//10-1] = "X"
elif int(position)//10 == 3:
    if position//10 == 1:
        row3[position//10-1] = "X"
    elif position//10 == 2:
        row3[position//10-1] = "X"
    elif position//10 == 3:
        row3[position//10-1] = "X"
else:
    print("Fail")
print(f'{row1}\n{row2}\n{row3}')
