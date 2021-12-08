from collections import defaultdict

with open('input/8.in', 'r') as in_file:
    lines = list(map(str.strip, in_file.readlines()))
    notes = []
    for line in lines:
        p, v = line.split(' | ')
        patterns = p.split(' ')
        value = v.split(' ')
        notes += [(patterns, value)]

summ = []
for patterns, value in notes:
    poss = {k : list() for k in 'abcdefg'}
    # 0 _ 2 _ _ 5 6 _ _ 9
    # a   a a   a a a a a | 8 -
    # b       b b b   b b | 6 -
    # c c c c c     c c c | 8 -
    #     d d d d d   d d | 7 -
    # e   e       e   e   | 4 -
    # f f   f f f f f f f | 9 -
    # g   g g   g g   g g | 7 -

    # a is the one in 7 but not in 1
    # cf are in 1
    # f is the one apperaring in 9 out of 10 numbers, the other in c
    # e is the one apperaring in 4 out of 10 numbers
    # b is the one apperaring in 6 out of 10 numbers
    # d is in 4, while g is not

    one = None
    four = None
    seven = None
    eight = None
    freqs = defaultdict(int)
    trans = {}
    for pattern in patterns:
        if len(pattern) == 2:
            one = pattern
        elif len(pattern) == 4:
            four = pattern
        elif len(pattern) == 3:
            seven = pattern
        elif len(pattern) == 7:
            eight = pattern
        for letter in pattern:
            freqs[letter] += 1

    for letter, freq in freqs.items():
        if (letter in seven) and (letter not in one):
            trans[letter] = 'a'
        elif letter in one:
            if freq == 9:
                trans[letter] = 'f'
            else:
                trans[letter] = 'c'
        elif freq == 4:
            trans[letter] = 'e'
        elif freq == 6:
            trans[letter] = 'b'
        elif letter in four:
            trans[letter] = 'd'
        else:
            trans[letter] = 'g'

    '''
                   start
              b /         \ -b
         c/      \ -c   e/  \-e
       d/  \-d e/\-e    2  a/ \-a
     e/ \-e  0 6  5      d/\-d  1
     8 g/ \-g            3  7
       9   4
        
    '''
    number = 0
    for digit, order in zip(value, [1000, 100, 10, 1]):
        digit = [trans[l] for l in digit]
        if 'b' in digit:
            if 'c' in digit:
                if 'd' in digit:
                    if 'e' in digit:
                        number += 8 * order
                    else:
                        if 'g'in digit:
                            number += 9 * order
                        else:
                            number += 4 * order
                else:
                    number += 0 * order
            else:
                if 'e' in digit:
                    number += 6 * order
                else:
                    number += 5 * order
        else:
            if 'e' in digit:
                number += 2 * order
            else:
                if 'a' in digit:
                    if 'd' in digit:
                        number += 3 * order
                    else:
                        number += 7 * order
                else:
                    number += 1 * order
    summ += [number]

print(sum(summ))