with open("input.txt", "r") as f:
    lines = f.readlines()

drawn_nums = lines.pop(0)
boards = []

for row in range(1, len(lines)):
    line = lines[row][:-1]
    if line != "":
        boards.append(line)


print(boards)