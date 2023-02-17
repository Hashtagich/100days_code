import random
test_seed = int(input("vvod:\n"))
random.seed(test_seed)
podbros= random.randint(0,1) 
if podbros==1:
    print('Heads')
else:
    print('Tails')        
