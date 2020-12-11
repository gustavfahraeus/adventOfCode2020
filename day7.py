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
<<<<<<< HEAD
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
=======
     
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



>>>>>>> e7045133d26797f1157e43ae7c2b569b9b03c3cc





      
    


     

        





