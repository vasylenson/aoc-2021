with open('input/5.in', 'r') as in_file:
    inputs = list(map(str.strip, in_file.readlines()))
    lines = []
    maxx, maxy = 0, 0
    for i in inputs:
        fr, to = i.split(' -> ')
        x1, y1 = list(map(int, fr.split(',')))
        x2, y2 = list(map(int, to.split(',')))
        maxx = max([maxx, x1, x2])
        maxy = max([maxy, y1, y2])
        lines.append((x1, y1, x2, y2))

print(maxx, maxy)
grid = [0] * ((maxx + 1) * (maxy + 1))

for x1, y1, x2, y2 in lines:
    if x1 == x2:
        start = min(y1, y2)
        end = max(y1, y2) + 1
        for pos in range(start, end):
            grid[x1 + pos * maxx] += 1
    elif y1 == y2:
        start = min(x1, x2)
        end = max(x1, x2) + 1
        for pos in range(start, end):
            grid[pos + y1 * maxx] += 1
    elif x1 - x2 == y1 - y2:
        startx = min(x1, x2)
        starty = min(y1, y2)
        endx = max(x1, x2) + 1
        endy = max(y1, y2) + 1
        for x, y in zip(range(startx, endx), range(starty, endy)):
            print(x, y)

            grid[x + y * maxx] += 1
            x += 1
    elif x1 - x2 == y2 - y1:
        startx = min(x1, x2)
        starty = max(y1, y2)
        endx = max(x1, x2) + 1
        endy = min(y1, y2) - 1
        for x, y in zip(range(startx, endx), range(starty, endy, -1)):
            print(x, y)

            grid[x + y * maxx] += 1
            x += 1
    else:
        print('wrong stuff')

print(sum(1 for x in grid if x >= 2))