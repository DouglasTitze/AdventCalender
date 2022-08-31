from unittest import TestProgram


def parseFile():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    lines = lines[0].strip().split(",")

    for i in range(len(lines)):
        lines[i] = int(lines[i])

    return lines


def createDic(state):
    dic = {}

    for num in state:
        dic[num] = dic.get(num, 0) + 1

    return dic


def dayPass(dic, numDays):
    for _ in range(numDays):
        tmpDic = dic.copy()
        for i in range(9):
            numFish = dic.get(i, 0)
            match i:
                case 0:
                    tmpDic[6] = numFish
                    tmpDic[8] = numFish
                case 1:
                    tmpDic[0] = numFish
                case 2:
                    tmpDic[1] = numFish
                case 3:
                    tmpDic[2] = numFish
                case 4:
                    tmpDic[3] = numFish
                case 5:
                    tmpDic[4] = numFish
                case 6:
                    tmpDic[5] = numFish
                case 7:
                    tmpDic[6] += numFish
                case 8:
                    tmpDic[7] = numFish
                case _:
                    print("error")

        dic = tmpDic

    return dic


initialState = parseFile()
fishTimers = createDic(initialState)

fishTimers = dayPass(fishTimers, 80)

print(sum(fishTimers.values()))
