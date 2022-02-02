import random

def randomcard():
    with open('cards.txt') as x:
        cards = x.readlines()
        i = 0 
        choice = []
        while(i < 12):
            y = random.choice(cards)
            if (y not in choice ):
                choice.append(y)
                i = i+1
    x.close()
    return choice

name = input("what would you like the file name to be? ")

number = input("how many hands would you like to have? ")

x = 0    
while(x  < int(number)):
    with open(f'{name}.txt','a') as res:
        cards =randomcard()
        res.write(str(cards)+'\n')
    res.close()
    x = x+1

        