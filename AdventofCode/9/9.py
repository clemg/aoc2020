from itertools import combinations

with open("input") as fi:
    file = list(map(int, fi.readlines()))

# Part 1
p1 = 0
for line in range(25, len(file)):
    if not any(a + b == file[line] for a, b in combinations(file[line-25:line], 2)):
        p1 = file[line]

# Part 2
p2 = 0
for line in range(len(file)):
    for num in range(line + 2, len(file)):
        total = sum(file[line:num])
        if total > p1:
            break
        elif total == p1:
            p2 = min(file[line:num]) + max(file[line:num])

print(p1, p2)
