def formatted_input():
    with open("input.txt", "r") as f:
        lines = f.readlines()

        for i in range(len(lines)):
            lines[i] = list(map(int, lines[i].strip()))
            lines[i].append(9)
            lines[i].insert(0, 9)

    lines.insert(0, [9 for _ in range(len(lines[0]))])
    lines.append([9 for _ in range(len(lines[0]))])

    return lines


def search_cave(cave):
    for row in range(1, len(cave) - 1):
        for col in range(1, len(cave[row]) - 1):
            if cave[row][col] != 9:
                return row, col
    raise Exception()


def flood_basin(cave, row, col):
    cave[row][col] = 9

    size = 1

    if cave[row + 1][col] != 9:
        size += flood_basin(cave, row + 1, col)

    if cave[row - 1][col] != 9:
        size += flood_basin(cave, row - 1, col)

    if cave[row][col + 1] != 9:
        size += flood_basin(cave, row, col + 1)

    if cave[row][col - 1] != 9:
        size += flood_basin(cave, row, col - 1)

    return size


def greatest_basin(size, saved_basins):
    for i in range(len(saved_basins)):
        if size > saved_basins[i]:
            saved_basins[i] = size
            break


cave = formatted_input()
saved_basins = [0, 0, 0]

size = 1

while True:
    try:
        row, col = search_cave(cave)
    except:
        break

    greatest_basin(flood_basin(cave, row, col), saved_basins)

for num in saved_basins:
    size *= num

print(size)
