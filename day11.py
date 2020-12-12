file = open('input.txt', 'r')

input = file.read().splitlines()

rows = len(input)
cols = len(input[0])

dotInput = ['.' + line + '.' for line in input]

dotLine = '.' * len(dotInput[0])
dotInput.insert(0,dotLine)
dotInput.append(dotLine)
