def formatted_input():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = list(lines[i].strip())

    return lines

cave = formatted_input()
