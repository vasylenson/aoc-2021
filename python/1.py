with open('input/1.in', 'r') as in_file:
    depths = list(map(int, in_file.readlines()))

count = sum(1 for prev, curr in zip(depths, depths[1:]) if curr > prev)
print(f"Part A: {count}")
window_count = sum(1 for prev, curr in zip(depths, depths[3:]) if curr > prev)
print(f"Part B: {window_count}")