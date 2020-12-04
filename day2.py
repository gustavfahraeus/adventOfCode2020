file = open('day2input.txt', 'r')
input = file.read().split("\n")

def partOne():
    listOfEntries = list(map(
    lambda rawEntry: (
        entry := {
                    'interval': list(map(int, rawEntry.split()[0].split("-"))),
                    'letter': rawEntry.split()[1][0],
                    'password': rawEntry.split()[2]}
    ),input))

    partOne = 0
    for entry in listOfEntries:
        matches = list(filter(lambda char: char == entry['letter'], entry['password']))
        if len(matches) >= entry['interval'][0] and len(matches) <= entry['interval'][1]:
            partOne += 1

    print(partOne)


def partTwo():
    listOfEntries = list(map(
    lambda rawEntry: (
        entry := {
                    'interval': list(map(lambda s: s-1, list(map(int, rawEntry.split()[0].split("-"))))),
                    'letter': rawEntry.split()[1][0],
                    'password': rawEntry.split()[2]}
    ),input))

    partTwo = 0
    for entry in listOfEntries:
        if entry['password'][entry['interval'][0]] == entry['letter'] and entry['password'][entry['interval'][1]] != entry['letter']:
            partTwo += 1
        elif entry['password'][entry['interval'][0]] != entry['letter'] and entry['password'][entry['interval'][1]] == entry['letter']:
            partTwo += 1
        
    print(partTwo)


partOne()
partTwo()

    

