file = open('input.txt', 'r')

input = [0] + sorted([int(x) for x in file.read().splitlines()])
input.append(input[-1] + 3)

routes = {}
routes[0] = 1

for joltage in input[1:]:
    routes[joltage] = routes.get(joltage-1, 0) + routes.get(joltage-2, 0) + routes.get(joltage-3, 0)

print(routes[max(routes.keys())])
