with open("input.txt", "r") as f:
    lines = f.readlines()


def diagnostic(lst, column, typ):

    l = len(lst)

    if l != 1:

        ones = []
        zeros = []
        for row in range(l):

            if lst[row][column] == "1":
                ones.append(lst[row])
            else:
                zeros.append(lst[row])

        len_one = len(ones)
        len_zer = len(zeros)

        if typ == "oxy":
            if len_one > len_zer:
                return ones
            elif len_zer > len_one:
                return zeros
            else:
                return ones
        else:
            if len_one < len_zer:
                return ones
            elif len_zer < len_one:
                return zeros
            else:
                return zeros
    else:
        return lst


oxy = []
c02 = []

for column in range(len(lines[0]) - 1):
    if column == 0:
        oxy = diagnostic(lines, column, "oxy")
        c02 = diagnostic(lines, column, "c02")
    else:
        oxy = diagnostic(oxy, column, "oxy")
        c02 = diagnostic(c02, column, "c02")


oxy = int("".join(oxy), 2)
c02 = int("".join(c02), 2)

print(oxy * c02)
