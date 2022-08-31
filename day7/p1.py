from ast import parse
from unittest import TestProgram


def parseFile():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    lines = lines[0].strip().split(",")

    for i in range(len(lines)):
        lines[i] = int(lines[i])

    return lines


crabs = sorted(parseFile())
median = crabs[len(crabs) // 2]
sumFuel = 0

for crab in crabs:
    if crab == median:
        continue
    elif crab > median:
        sumFuel += crab - median
    else:
        sumFuel += median - crab

print(sumFuel)
