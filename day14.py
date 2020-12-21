import re
from copy import deepcopy
file = open('input.txt', 'r')

lines = file.read().splitlines()

memPattern = re.compile(r"(?<=mem\[)\d+") # Matches memory position.
maskPattern = re.compile(r"(?<=mask = )\w+") # Matches mask.
valuePattern = re.compile(r"(?<== )\d+")

def solveOne():
    currentBitMask = ''
    maskedValues = {}
    for line in lines:
        
        # New bit mask?
        if maskPattern.findall(line):
            currentBitMask = maskPattern.findall(line)[0]
            continue
    
        memPosition = int(memPattern.findall(line)[0])
        binValue = bin(int((valuePattern.findall(line)[0])))[2:].zfill(36)
   
        maskedValue = ''
        for index, bit in enumerate(currentBitMask):
            if bit == 'X':
                maskedValue += binValue[index]
                continue
            if bit == "1":
                maskedValue += '1'
            if bit == '0':
                maskedValue += '0'
        maskedValues[memPosition] = int(maskedValue, 2)
    
    sum = 0
    for binValue in maskedValues.values():
        sum += binValue
    return sum


def solveTwo():
    currentBitMask = ''
    maskedValues = {}
    for line in lines:
        
        # New bit mask?
        if maskPattern.findall(line):
            currentBitMask = maskPattern.findall(line)[0]
            continue
            
        memPosition = bin(int((memPattern.findall(line)[0])))[2:].zfill(36)
        decValue = int((valuePattern.findall(line)[0]))
        
        maskedAdress = ''
        for index,bit in enumerate(currentBitMask):
            if bit == 'X':
                maskedAdress += 'X'
            elif bit == '1':
                maskedAdress += '1'
            elif bit == '0':
                maskedAdress += memPosition[index]
        
        combinations = ['']
        for bit in maskedAdress:
            if bit != 'X':
                combinations = [combination + bit for combination in combinations]
            else:
                copy = deepcopy(combinations)
                copy = [combination + '0' for combination in copy]
                combinations = [combination + '1' for combination in combinations]
                combinations = combinations + copy
        combinations = [int(combination, 2) for combination in combinations]
        for value in combinations:
            maskedValues[value] = decValue
    
    sum = 0
    for value in maskedValues.values():
        sum += value
    return sum
        
        
print(solveOne())
print(solveTwo())

