import re

file = open("input.txt", 'r')

input = file.read().splitlines()








ruleBook = {}
for rule in input:
    typeOfBag = rule.split(' contain ')[0].replace('bags', 'bag')
    bagRestrictions = rule.split(' contain ')[1].split(", ")
    bagRestrictions[-1] = bagRestrictions[-1].replace('.', '')
    bagRestrictions = list(map(lambda string: string.replace('bags', 'bag'), bagRestrictions))
    
    for restriction in bagRestrictions:
        if restriction.split(" ", 1)[0] == "no": ruleBook[typeOfBag] = 0
        else: ruleBook[typeOfBag] = {restriction.split(" ", 1)[1]: int(restriction.split(" ", 1)[0])}



print(ruleBook)








      
    


     

        





