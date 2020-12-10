with open("input", "r") as fi:
    file = fi.read().split("\n\n")
    file = [group.splitlines() for group in file]

# Part 1
p1 = 0
for group in file:
    base = set(group[0])

    for person in group[1:]:
        base = base.union(set(person))

    p1 += len(base)

# Part 2
p2 = 0
for group in file:
    base = set(group[0])

    for person in group[1:]:
        base = base.intersection(set(person))

    p2 += len(base)

print(p1, p2)
