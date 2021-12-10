with open('input/10.in', 'r') as in_file:
    lines = list(map(str.strip, in_file.readlines()))
    chars = [[ch for ch in line] for line in lines]

openclose = {'(': ')', '[': ']', '{': '}', '<': '>'}

corrscore = {')': 1, ']': 2, '}': 3, '>': 4}

errscore = {')': 3, ']': 57, '}': 1197, '>': 25137}

incomplete = []

score = 0
for line in lines:
    stack = []
    valid = True
    for char in line:
        if char in openclose:
            stack.append(char)
        elif char != openclose[stack[-1]]:
            valid = False
            score += errscore[char]
            break
        elif char == openclose[stack[-1]]:
            stack.pop()
    if valid:
        incomplete.append(stack)

print('Part 1:', score)

scores = []
for stack in incomplete:
    stack.reverse()
    score = 0
    for ch in stack:
        corr = openclose[ch]
        score = score * 5 + corrscore[corr]
    scores.append(score)

scores.sort()
print('Part 2:', scores[len(scores) // 2])