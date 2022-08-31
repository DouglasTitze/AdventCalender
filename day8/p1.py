from ast import parse


def parseFile():
    with open("input.txt", "r") as f:
        for line in f:
            inp, out = line.strip().split(" | ")
            yield (inp.split(" "), out.split(" "))


print(sum(1 for (_, out) in parseFile() for num in out if len(num) in [2, 4, 3, 7]))
