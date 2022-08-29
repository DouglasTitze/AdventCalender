import re


def createBoards():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    drawn_nums = lines.pop(0).strip().split(",")
    boards = []
    cur_borad = []

    for line in lines:
        line = line.strip()

        if not line:
            cur_borad = []
            boards.append(cur_borad)
            continue

        cur_borad.append(re.split(r"\s+", line))

    boards.append(cur_borad)

    return (drawn_nums, boards)


def winner(board):
    for row in board:
        if not any(row):
            return True

    for col in range(len(board[0])):
        if not any(board[row][col] for row in range(len(board))):
            return True

    return False


def checkBoard(board, num):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == str(num):
                board[row][col] = None


def calcScore(board, calledNum):
    return int(calledNum) * sum(int(x) for row in board for x in row if x)


drawn_nums, boards = createBoards()

prevWin = []
winNums = {}

for num in drawn_nums:
    for board in boards:
        if board in prevWin:
            continue

        checkBoard(board, num)
        if winner(board):
            prevWin.append(board)
            winNums[len(prevWin) - 1] = num

print(calcScore(prevWin[-1], winNums[len(prevWin) - 1]))