import re

file = open('input.txt', 'r')
input = file.read().split('\n\n')




byrRegEx = re.compile('byr:\d{4}(\D|$)')
iyrRegEx = re.compile('iyr:\d{4}(\D|$)')
eyrRegex = re.compile('eyr:\d{4}(\D|$)')
hgtRegEx = re.compile('hgt:(\d\d|\d\d\d)(in|cm)')
hclRegEx = re.compile('hcl:#[0-9|a-f]{6}(\D|$)')
eclRegEx = re.compile('ecl:(amb|blu|brn|gry|grn|hzl|oth)')
pidRegEx = re.compile('pid:\d{9}(\W|$)(\D|$)')


regExArray = [eclRegEx, pidRegEx, eyrRegex, hclRegEx, byrRegEx, iyrRegEx, hgtRegEx]

ans = 0
for line in input:

    count = 0
    for regEx in regExArray:
        if regEx.search(line):
            value = regEx.search(line).group(0).split(':')[1]
            if regEx == byrRegEx and int(value) in list(range(1920,2021)): count += 1  
            elif regEx == iyrRegEx and int(value) in list(range(2010,2021)): count += 1
            elif regEx == eyrRegex and int(value) in list(range(2020,2031)): count += 1 
            elif regEx == hgtRegEx:
                reversedArray = value[::-1]
                actualValue = ''.join(list(filter(lambda x: x.isdigit(), value)))
                if (reversedArray[1] + reversedArray[0]) == 'cm' and int(actualValue) in list(range(150,194)): 
                    count += 1
                
                elif (reversedArray[1] + reversedArray[0]) == 'in' and int(actualValue) in list(range(59,77)): count += 1
            elif regEx in [hclRegEx,eclRegEx,pidRegEx]: count += 1
    
    if count == 7: 
        ans += 1
        print(' '.join(line.split('\n')))
        

print(ans)
    

             
        