
def quads_n_triples(file):
    choices = ['A' , '2', '3', '4' , '5' , '6' , '7', '8','9','10','J','Q','K']
    with open(f'{file}.txt') as x:
        res = x.readlines()
        counter = 0
        quad_counter = 0
        triple_counter = 0
        for lines in res: 
            for y in choices: 
                if lines.count(y) == 4: 
                   quad_counter += 1 
            if quad_counter == 1:
                for y in choices: 
                    if lines.count(y) == 3:
                        triple_counter += 1 
            if quad_counter == 1 and triple_counter == 2:
                counter += 1
            quad_counter = 0
            triple_counter = 0
        print("The number of hands with 1 quadruple and 2 triples is: " + str(counter))                  
    x.close()

def straight(file): 
    suites = ['C', 'S', 'D', 'H']
    list_in_list = [['C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'CJ'],['C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'CJ'], ['C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'CJ', 'CQ'], ['C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'CJ', 'CQ', 'CK'], ['SA', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10'],['S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ'], ['S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ'],
     ['S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK'],['HA', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10'],  ['H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'HJ'],
      ['H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'HJ', 'HQ'],['H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'HJ', 'HQ', 'HK'], ['DA', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10'],
      ['D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'DJ'],['D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'DJ', 'DQ'],  ['D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'DJ', 'DQ', 'DK']]
    suite_counter = 0
    counter2 = 0
    incounter = 0
    with open(f'{file}.txt') as x: 
        res = x.readlines()
        for lines in res: 
            for y in suites: 
                if lines.count(y) >= 10:
                    suite_counter += 1
            if suite_counter == 1: 
                for z in list_in_list:
                    for a in z: 
                        if lines.count(a) == 1:
                            incounter +=1
                        
                    if incounter == 10: 
                        counter2 += 1
                    incounter = 0
            suite_counter = 0
        print("The number of hands with a straight flush that has 10 consecutive numbers is: " + str(counter2))
    x.close()                                    


name = input("which file is being tested? ")

quads_n_triples(name)
straight(name)