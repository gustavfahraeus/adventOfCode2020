file = open('input.txt', 'r')

input  = list(map(lambda str: str.replace('\n',','), file.read().split('\n\n')))
print(input)

sum = 0
for listOfChars in input:
    presentChars = {}
    count = 0
    people = 1
    for char in listOfChars:
        if char == ',':
            people += 1
            continue
        if char in presentChars:
            presentChars[char] += 1
        else: presentChars[char] = 1
    for value in iter(presentChars.values()):
        if value == people: sum += 1
        
print(sum)