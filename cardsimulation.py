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

x = 0    
while(x  < 1500000):
    with open('results.txt','a') as res:
        cards =randomcard()
        res.write(str(cards)+'\n')
    res.close()
    x = x+1

        