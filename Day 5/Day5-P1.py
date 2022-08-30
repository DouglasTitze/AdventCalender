def parseFile():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    i = 0
    for i in range(len(lines)):
        tmp = []
        lines[i] = lines[i].split()
        tmp += lines[i][0].split(",")
        tmp += lines[i][2].split(",")

        for j in range(len(tmp)):
            tmp[j] = int(tmp[j])

        lines[i] = tmp
    return lines


def createFloor():
    len_and_height = 1000
    ar = [[0] * len_and_height for i in range(len_and_height)]
    return ar


def iteratorNum(num1, num2):
    if num1 < num2:
        return 1
    else:
        return -1


def placePoint(line, floor):
    x1 = line[0]
    x2 = line[2]
    y1 = line[1]
    y2 = line[3]

    if x1 == x2:

        iterator = iteratorNum(y1, y2)

        while y1 != y2:
            floor[y1][x1] += 1
            y1 += iterator

    elif y1 == y2:

        iterator = iteratorNum(x1, x2)

        while x1 != x2:
            floor[y1][x1] += 1
            x1 += iterator

    else:
        return False


def createTxt(floor):
    for i in range(len(floor)):
        for j in range(len(floor[i])):
            floor[i][j] = str(floor[i][j])

        floor[i] = "".join(floor[i])

    f = open("floor.txt", "w+")
    f.write("\n".join(floor))
    f.close()


lineSegments = parseFile()
floor = createFloor()

for line in lineSegments:
    placePoint(line, floor)

overlap = 0

for line in floor:
    for point in line:
        if point >= 2:
            overlap += 1

print(overlap)
createTxt(floor)
