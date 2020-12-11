file = open('input.txt', 'r')


listOfNumbers = list(map(lambda nr: int(nr), file.read().splitlines()))

def twoSum(target, listOfIntegers):
    numbers = {}
    for i in range(0,len(listOfIntegers)):
        numbers[listOfIntegers[i]] = i

    for i in range(0,len(listOfIntegers)):
        if target - listOfIntegers[i] in numbers and numbers[target - listOfIntegers[i]] != i: return True

    return False

target = 1124361034
for i in  range(len(listOfNumbers)):
    for j in range(i+2, len(listOfNumbers)):
        interval = listOfNumbers[i:j]
        if sum(interval) == target:
            print(min(interval) + max(interval))
            break
  




