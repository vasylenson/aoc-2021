with open('input/11.in', 'r') as in_file:
    lines = list(map(str.strip, in_file.readlines()))
    octo = [[int(ch) for ch in line] for line in lines]
ROWS = len(lines)
COLS = len(lines[0])

flashes = 0

def inc(row, col, grid=octo):
    if row >= ROWS or col >= COLS or row < 0 or col < 0:
        return

    if grid[row][col] > 9:
        return

    grid[row][col] += 1
    if grid[row][col] > 9:
        inc(row + 1, col - 1)
        inc(row + 1, col)
        inc(row + 1, col + 1)
        inc(row, col - 1)
        inc(row, col + 1)
        inc(row - 1, col - 1)
        inc(row - 1, col)
        inc(row - 1, col + 1)


for n in range(1000):
    sync = True
    for row in range(len(octo)):
        for col in range(len(octo[row])):
            inc(row, col)
    for row in range(len(octo)):
        for col in range(len(octo[row])):
            if octo[row][col] > 9:
                flashes += 1
                octo[row][col] = 0
            else:
                sync = False
    if sync:
        print('sync', n + 1)
        break
print(flashes)