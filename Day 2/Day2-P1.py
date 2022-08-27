import numpy as np

with open("input.txt", "r") as f:
    lines = f.readlines()


dir_num = []

for line in lines:
    dir_num.append(line.split())

hor = 0
dep = 0

for command in dir_num:
    dir = command[0]
    num = int(command[1])

    if dir == "up":
        dep -= num
    elif dir == "down":
        dep += num
    else:
        hor += num

print(hor * dep)