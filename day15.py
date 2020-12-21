input = [7,12,1,0,16,2]
turnTracker = {}

for i, n in enumerate(input):
    if i != len(input)-1:
        turnTracker[n] = i

while len(input) < 30000000:
    spoken = input[-1]
    lastSpoken = turnTracker.get(spoken, -1)
    turnTracker[spoken] = len(input)-1
    
    if lastSpoken == -1:
        nextNr = 0
    else:
        nextNr = len(input) - 1 - lastSpoken
        
    input.append(nextNr)
    if len(input) == 2020:
        print(nextNr)
print(input[-1])