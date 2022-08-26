import numpy as np

with open("input.txt", "r") as f:
    lines = f.readlines()

lines = np.array(lines).astype(int)

end = 4
prev = sum(lines[0:3])
count = 0

while end <= len(lines):
    start = end - 3
    cur = sum(lines[start:end])
    if cur > prev:
        count += 1

    prev = cur
    start += 1
    end += 1

print(count)
