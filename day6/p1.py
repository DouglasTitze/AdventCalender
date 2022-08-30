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

def dayPass(dic, numDays):
    for _ in range(numDays):
        for i in range(8,-1,-1):
            tmpDic = {}
            match i:
                case 0:
                    tmpDic[0] = dic[1]
                case 1:
                    print("hello")
                case 2:
                    print("hello")
                case 3:
                    print("hello")
                case 4:
                    print("hello")
                case 5:
                    print("hello")
                case 6:
                    print("hello")
                case 7:
                    print("hello")
                case 8:
                    print("hello")
                case _:
                    print("error")



            dic = tmpDic


initialState = parseFile()
fishTimers = createDic(initialState)
dayPass(fishTimers,18)
