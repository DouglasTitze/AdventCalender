import numpy as np

with open("input.txt", "r") as f:
    lines = f.readlines()

lines = np.array(lines).astype(int)

count = 0

for i in range(1, len(lines)):
    if lines[i] > lines[i - 1]:
        count += 1


print(count)
