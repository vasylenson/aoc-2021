with open('input/6.in', 'r') as in_file:
    lines = list(map(str.strip, in_file.readlines()))
    fish = list(map(int, lines[0].split(',')))

DAYZ = 256

def loop(fish, DAYZ):
    fishmap = [0] * 9
    for f in fish:
        fishmap[f] += 1

    assert len(fishmap) == 9

    count = 0
    for i in range(DAYZ):
        zerodays = fishmap.pop(0)
        fishmap.append(zerodays)
        fishmap[6] += zerodays
    return fishmap

fishmap = loop(fish, DAYZ)

print(sum(fishmap))
print(fishmap)
