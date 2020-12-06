import math

file = open('input.txt', 'r')

input = file.read().splitlines()

possSeats = list(range(0,879))
for seat in input:
    row = [1,1,1,1,1,1,1]
    col = [1,1,1]
    rowIndex = 0
    colIndex = 0
    for char in seat:
        if char == 'F': 
            row[rowIndex] = 0
            rowIndex += 1 
        if char == 'B': 
            rowIndex += 1
        if char == 'L': 
             col[colIndex] = 0
             colIndex += 1
        if char == 'R': 
             colIndex += 1
             
    rowNr = int("".join(str(x) for x in row), 2)  
    colNr = int("".join(str(x) for x in col), 2) 
    id = rowNr*8+colNr
    if id in possSeats: possSeats.remove(id)

    
print(possSeats)