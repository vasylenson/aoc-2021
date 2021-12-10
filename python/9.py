with open('input/9.in', 'r') as in_file:
    lines = list(map(str.strip, in_file.readlines()))
    high = [[int(ch) for ch in line] for line in lines]

score = 0
lows = []
connections = []
for y in range(len(high)):
    row = []
    for x in range(len(high[0])):
        val = high[y][x]
        up = high[y - 1][x] if y > 0 else None
        down = high[y + 1][x] if y < len(high) - 1 else None
        right = high[y][x + 1] if x < len(high[0]) - 1 else None
        left = high[y][x - 1] if x > 0 else None

        connected = [
            None if up == None else val < up,
            None if down == None else val < down,
            None if right == None else val < right,
            None if left == None else val < left
        ]

        row.append([False, (x, y), connected])

        low = all(c for c in connected if c != None)
        if low:
            lows += [(x, y)]
            score += val + 1
    connections.append(row)

def count(x, y):
    visited, _, (up, down, right, left) = connections[y][x]

    if visited or high[y][x] == 9:
        return 0

    connections[y][x][0] = True
    summ = 1

    if up:
        summ += count(x, y - 1)

    if down:
        summ += count(x, y + 1)

    if right:
        summ += count(x + 1, y)

    if left:
        summ += count(x - 1, y)

    return summ

boids = [count(x, y) for x, y in lows]
boids.sort(reverse=True)

print(score)
print(boids)
print(boids[0] * boids[1] * boids[2])