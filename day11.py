from copy import deepcopy

file = open('input.txt', 'r')

defaultGrid = [list(line) for line in file.read().splitlines()]

rows = len(defaultGrid)
cols = len(defaultGrid[0])

def solve(grid):
    while True:
        gridCopy = deepcopy(grid)
        unChanged = False
        for r in range(rows): 
            for c in range(cols):
                occupied = 0
                for dr in [-1,0,1]:
                    for dc in [-1,0,1]:
                        if not (dr==0 and dc==0):
                            rr = r+dr
                            cc = c+dc
                       
                            # only part 2
                            while 0 <= rr < rows and 0 <= cc < cols and grid[rr][cc] == '.':
                                rr = rr+dr
                                cc = cc+dc

                            if 0 <= rr < rows and 0  <= cc < cols and grid[rr][cc]=='#':
                                occupied += 1

                if grid[r][c] == 'L':
                    if occupied == 0:
                        gridCopy[r][c] = '#'
                        unChanged = True
         
                # 4 for part 1
                elif grid[r][c] == '#' and occupied >= 5:
                    gridCopy[r][c] = 'L'
                    unChanged = True
        if not unChanged:
            break
        grid = deepcopy(gridCopy)

    ans = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '#':
                ans += 1
    return ans

print(solve(defaultGrid))



