with open("input.txt", "r") as f:
    lines = f.readlines()

num_row = 0
num_col = 0
most_com = []
last_column = len(lines[0])
last_row = len(lines)

while num_col < last_column:
    num_row = 0
    tmp = 0
    while num_row < last_row:
        if lines[num_row][num_col] == "1":
            tmp += 1
        num_row += 1

    if tmp > last_row // 2:
        most_com.append("1")
    else:
        most_com.append("0")

    num_col += 1

most_com.pop()
most_com = "".join(most_com)

print(int(most_com,2) * int(most_com[::-1],2))