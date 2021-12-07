with open('input/7.in', 'r') as in_file:
    lines = list(map(str.strip, in_file.readlines()))
    crabs = list(map(int, lines[0].split(',')))

def cost(fr, to):
    dist = abs(fr - to)
    return dist * (dist + 1) // 2


assert cost(16, 5) == 66
assert cost(1, 5) == 10

dists = [sum(cost(crab, pos) for crab in crabs) for pos in range(max(crabs))]

print(min(dists))