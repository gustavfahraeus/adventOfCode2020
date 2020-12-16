file = open('input.txt', 'r')

input = file.read().splitlines()

timeStamp = int(input[0])
buses = [int(item) for item in input[1].split(',') if item != 'x']


def solveOne(earliestTime,listOfBuses):
    busDepartures = []
    for bus in listOfBuses:
        departureTime = 0
        nextDeparture = departureTime * bus
        
        while nextDeparture < earliestTime:
            departureTime += 1
            nextDeparture = bus * departureTime
            
        busDepartures.append([nextDeparture,bus])
        
    departureTimes = [pair[0] for pair in busDepartures]
    busIds = [pair[1] for pair in busDepartures]
    
    departureTime = min(departureTimes)
    waitingTime = departureTime - earliestTime
    
    return(waitingTime * busIds[departureTimes.index(departureTime)])
   
#print(solveOne(timeStamp,buses))

def solveTwo(listOfBuses):
    # We want to return the first timeStamp t
    # such that busIds[0] * someNr = t && busIds[1] * someNr = t+1 && someNr[2] * ... etc
    
    entryToOffset = {}
    
    for index, bus in enumerate(listOfBuses):
        if bus != 'x':
            entryToOffset[bus] = index
            
    relevantBuses = list(entryToOffset.keys())

    while True:
        timeStamp = 0
        for bus in relevantBuses:
            toggle = True
            if bus * timeStamp == relevantBuses[0] + entryToOffset[bus]:
                continue 
            else:
                toggle = False
                break
        if (toggle):
            return timeStamp
        else: timeStamp += 1
        
        
    
solveTwo(buses)
            
        


