with open("input.txt", "r") as f:
    lines = f.readlines()


dir_num = []

for line in lines:
    dir_num.append(line.split())

hor = 0
dep = 0
aim = 0

for command in dir_num:
    dir = command[0]
    num = int(command[1])

    if dir == "up":
        aim -= num
    elif dir == "down":
        aim += num
    else:
        hor += num
        dep += aim * num

print(hor * dep)