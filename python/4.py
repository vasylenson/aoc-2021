with open('input/4.in', 'r') as in_file:
    lines = list(map(str.strip, in_file.readlines()))
    moves = list(map(int, lines[0].split(',')))
    boards = []
    next_board = []
    for line in lines[1:]:
        if line == "":
            boards.append(next_board)
            next_board = []
        else:
            next_board += list(
                map(int, filter(lambda x: len(x) > 0, line.split(' '))))

winners = []

def printboard(board):
    for row in range(5):
        print('\t'.join(map(str, board[row * 5:(row + 1) * 5])))

def score(board, last_move):
    winscore = last_move * sum(n for n in board if n != None)
    winners.append((board, winscore))
    # print(winscore)
    # printboard(board)

for move in moves:
    for ib, board in enumerate(boards):
        if boards == None:
            continue
        for i, n in enumerate(board):
            if move != n:
                continue

            board[i] = None
            row = i // 5
            col = i % 5
            
            if any(num != None for num in board[row * 5 : (row + 1) * 5]):
                continue
            if any(num != None for num in board[col::5]):
                continue

            score(board, move)
            boards[ib] = None

first_board, first_score = winners[0]
last_board, last_score = winners[-1]
print(f'[First to win]\nScore: {first_score}\nBoard:')
printboard(first_board)
print()
print(f'[Last to win]\nScore: {last_score}\nBoard:')
printboard(last_board)