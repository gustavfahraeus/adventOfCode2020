file = open('input.txt', 'r')

input = file.read().splitlines()

def partOne():
    x, y = 0, 0
    delx, dely = 3, 1

    ans = 0
    for line in input:
        if input[y][x] == '#':
            ans += 1
        x += delx
        x %= len(line)
        y += dely

    print(ans)


slopes = [[1,1,0], [3,1,0], [5,1,0], [7,1,0], [1,2,0]]



for slope in slopes:
    print(slope)
    x, y = 0, 0
    delx = slope[0]
    dely = slope[1]
    
    for line in input:
        if input[y][x] == '#':
            slope[2] += 1
        x += delx
        x %= len(line)
        y += dely
        print(slopes)


