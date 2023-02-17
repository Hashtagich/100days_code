print('Welcome to programme "Pizza time"')
size = input('What pizza do you want? S, M or L')
add_pepperoni = input('Do you want pepperoni? Y or N')
extra_cheese = input('Do you want extra cheese? Y or N')
total = 0
# основные расценки пиццы (условия):
# 1 Стоимость пицц в долларах по размеру S=15 M=20 L=25
# 2 Стоимость пепперони для S пиццы в долларах +2
# 3 Стоимость пепперони для M и L пиццы в долларах +3
# 4 Стоимость экстра сыра для всех + 1 доллар
if size == 'S':
    total += 15
    if add_pepperoni == 'Y':
        total += 2
    else:
        total += 0
elif size == 'M':
    total += 20
    if add_pepperoni == 'Y':
        total += 3
    else:
        total += 0
else:
    total += 25
    if add_pepperoni == 'Y':
        total += 2
    else:
        total += 0
if extra_cheese == 'Y':
    total += 1
else:
    total += 0
print('Your pizza send ' + str(total) + " $")
