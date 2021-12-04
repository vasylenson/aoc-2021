with open('input/2.in', 'r') as in_file:
    commands = list(in_file.readlines())

depth = 0
dist = 0
aim = 0

for command_str in commands:
    direction, step = command_str.split(' ')
    step = int(step)

    if direction == 'forward':
        dist += step
        depth += aim * step
    elif direction == 'down':
        aim += step
    elif direction == 'up':
        aim -= step
    else:
        print(direction, 'that is weird')

print(f'Part A: {aim * depth}')
print(f'Part B: {dist * depth}')