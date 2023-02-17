print ("Welcome to the Love calculator!")
name1 = input('What is your name?\n')
name2 = input('What is their name?\n')
comboname = name1+name2
comboname.lower()
firstnumber = comboname.count('t') + comboname.count('r') + comboname.count('u') + comboname.count('e')
secondnumber = comboname.count('l') + comboname.count('o') + comboname.count('v') + comboname.count('e')
total_ball=str(firstnumber)+str(secondnumber)
total_ball = int(total_ball)
if total_ball >=90 or total_ball <= 10:
    print ('Ваш коэффициент равен ' + str(total_ball) + ' вы подходите друг другу как ментос и кола')
elif 40 <= total_ball <=50:
    print ('Ваш коэффициент равен ' + str(total_ball) + ' вы подходите друг другу')
else:
    print('Ваш коэффициент равен ' + str(total_ball))
