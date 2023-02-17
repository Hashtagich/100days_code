print('Добро пожаловать в игру "Камень, ножницы, бумага"')
list=['камень', 'ножницы', 'бумага']
import random
question="yes"
while question=="да" or question=="Да" or question=="Yes" or question=="yes":
    step1 = input("Что выберешь? камень ножницы или бумагу\n")
    step2 = random.choice(list)
    print(step1)
    print(step2)
    if (step1 =="ножницы" and step2=="бумага") or (step1 =="камень" and step2=="ножницы") or (step1 =="бумага" and step2=="камень"):
        print('You win!')
    elif (step2 =="ножницы" and step1=="бумага") or (step2 =="камень" and step1=="ножницы") or (step2 =="бумага" and step1=="камень"):
        print('You lose!')
    elif (step2 == "ножницы" and step1 == "ножницы") or (step2 == "камень" and step1 == "камень") or (step2 == "бумага" and step1 == "бумага"):
        print('Ничья!')
    question = input("Желаете продолжинть 'да' или 'нет'?\n")
    if question=="нет" or question=="Нет" or question=="No" or question=="no":
        print("Goodbye!")