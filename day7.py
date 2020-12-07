import re

file = open("input.txt", 'r')

input = file.read().splitlines()

ruleBook = {}
for rule in input:
    typeOfBag = rule.split(' contain ')[0].replace('bags', 'bag')
    bagRestrictions = rule.split(' contain ')[1].split(", ")
    bagRestrictions[-1] = bagRestrictions[-1].replace('.', '')
    bagRestrictions = list(map(lambda string: string.replace('bags', 'bag'), bagRestrictions))

    ruleBook[typeOfBag] = {}
    for restriction in bagRestrictions:
     
        if restriction.split(" ", 1)[0] == "no": ruleBook[typeOfBag] = {}
        else: 
            ruleBook[typeOfBag].update({**ruleBook[typeOfBag], restriction.split(" ", 1)[1]: int(restriction.split(" ", 1)[0])})



def containedIn(target):
    containsColor = []
    for outMostBag, innerBags in ruleBook.items():
        for innerBag in innerBags:
            if innerBag == target:
                containsColor.append(outMostBag)
                containsColor = containsColor + [*containedIn(outMostBag)]
                break
    return list(dict.fromkeys(containsColor))


def capacity(target):
    sum = 0
    for bag, amount in ruleBook[target].items():
    
        if ruleBook[bag] == 0: 
            sum += amount
        else: sum += amount + amount*capacity(bag)
    return  sum

print(len(containedIn("shiny gold bag")))
print(capacity("shiny gold bag"))








      
    


     

        





