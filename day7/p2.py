def parseFile():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    lines = lines[0].strip().split(",")

    for i in range(len(lines)):
        lines[i] = int(lines[i])

    return lines


def fuelCost(crabs, val):
    sumFuel = 0

    for crab in crabs:
        if crab == val:
            continue

        elif crab > val:
            n = crab - val

        else:
            n = val - crab

        while n:
            sumFuel += n
            n -= 1

    return sumFuel


crabs = parseFile()
fuel = 99999999999

for pos in range(min(crabs), max(crabs)):
    newFuel = fuelCost(crabs, pos)
    if newFuel < fuel:
        fuel = newFuel

print(fuel)
