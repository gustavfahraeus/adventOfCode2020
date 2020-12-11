import copy

file = open('input.txt', 'r')

# Array of arrays of size 2. ['Instr', 'Amount']
instructions = list(map(lambda str: str.split(' '), file.read().splitlines()))

# Convert second index to int.
instructions = list(map(lambda arr: [arr[0],int(arr[1])], instructions))



def runProgram(listOfInstructions):
    accumulator = 0
    visited = []
    i = 0

    while(True):
        if i == len(listOfInstructions) - 1:
            break
        if i in visited:
            break
    
        if listOfInstructions[i][0] == "nop":
            visited.append(i)
            i += 1
            continue
    
        if listOfInstructions[i][0] == "acc":
            visited.append(i)
            accumulator += listOfInstructions[i][1]
            i += 1
            continue
        
        if listOfInstructions[i][0] == "jmp":
            visited.append(i)
            i += listOfInstructions[i][1]
            continue

    return [accumulator, i]

for i in range(0, len(instructions)):
    
    if instructions[i][0] == "nop":
        newInstructions = copy.deepcopy(instructions)
        newInstructions[i][0] = "jmp"
        if runProgram(newInstructions)[1] == len(newInstructions) -1: print("wtf")
    if instructions[i][0] == "jmp":
        newInstructions = copy.deepcopy(instructions)
        newInstructions[i][0] = "nop"
        runProgram(newInstructions)
        if runProgram(newInstructions)[1] == len(newInstructions) -1: print(runProgram(newInstructions)[0])