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
        if restriction.split(" ", 1)[0] == "no": continue
        else: ruleBook[typeOfBag] = {restriction.split(" ", 1)[1]: int(restriction.split(" ", 1)[0])}
           

visited = []
sum = 0
def bagPresent(inputBag):
    sum = 0
    for outerBag, innerBags in ruleBook.items():
        for bag in innerBags:
            if bag == inputBag and not (outerBag in visited):
                visited.append(outerBag)
                sum += 1 + bagPresent(outerBag) 
                    
    return sum

            
print(bagPresent("shiny gold bag"))





      
    


     

        





