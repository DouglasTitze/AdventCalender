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
        dic[num] = dic.get(num,0) + 1

    return dic



initialState = parseFile()
fishTimers = createDic(initialState)