print('Добро пожаловать в счётчик чаевых')
total_bill = float(input('Какой итоговый счёт?:\n'))
num_people = int(input('Сколько человек будет оплачивать?:\n'))
tip_percent = int(input("Сколько процентов чаевых желаете оставить? 10, 12 или 15:\n"))
total_tip = (total_bill * (1 + tip_percent / 100)) / num_people
result = round(total_tip, 2)
print(f'Каждый должен заплатить {result}')
