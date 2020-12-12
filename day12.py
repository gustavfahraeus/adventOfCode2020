file = open('input.txt', 'r')

input = file.read().splitlines()

facingDirection = {
    'current': 'E',
    'clock': ['N','E','S','W']
}

x = 0
y = 0 
for instruction in input:
    dir = instruction[0]
    amount = int(instruction[1:])
    if dir == 'F': dir = facingDirection.get('current')
    if dir == 'N': y += amount
    if dir == 'E': x += amount
    if dir == 'S': y -= amount
    if dir == 'W': x -= amount
    if dir == 'R':
        current = facingDirection['current']
        facingDirection['current'] = facingDirection['clock'][(facingDirection['clock'].index(current) + int(amount/90)) % 4]
    if dir == 'L':
        current = facingDirection['current']
        facingDirection['current'] = facingDirection['clock'][(facingDirection['clock'].index(current) - int(amount/90)) % 4]
        
print(abs(x) + abs(y))
    
directions = {"N": 0 + 1j, "E": 1 + 0j, "S": 0 - 1j, "W": -1 + 0j}
    
current_position = 0 + 0j
waypoint = 10 + 1j
current_heading = 1 + 0j

for instruction in input:
    dir = instruction[0]
    steps = int(instruction[1:])
    if dir == "F":
        current_position += steps * waypoint
    elif dir == "R":
        turns = int(steps / 90)
        for _ in range(turns):
            waypoint *= -1j
    elif dir == "L":
        turns = int(steps / 90)
        for _ in range(turns):
            waypoint *= 1j
    else:
        waypoint += directions[dir] * steps

print(abs(current_position.real) + abs(current_position.imag))
