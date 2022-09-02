def formatted_input():
    with open("input.txt", "r") as f:
        lines = f.readlines()

        for i in range(len(lines)):
            lines[i] = list(map(int, lines[i].strip()))
            lines[i].append(float("inf"))
            lines[i].insert(0, float("inf"))

    lines.insert(0, [float("inf") for _ in range(len(lines[0]))])
    lines.append([float("inf") for _ in range(len(lines[0]))])

    return lines


def search_cave(cave):
    return sum(
        cave[row][col] + 1
        for row in range(1, len(cave) - 1)
        for col in range(1, len(cave[row]) - 1)
        if check_low(cave, row, col)
    )


def check_low(cave, row, col):
    cur_point = cave[row][col]
    return (
        cur_point < cave[row - 1][col]
        and cur_point < cave[row + 1][col]
        and cur_point < cave[row][col + 1]
        and cur_point < cave[row][col - 1]
    )


cave = formatted_input()
print(search_cave(cave))
