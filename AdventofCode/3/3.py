from math import prod

with open("input", "r") as fi:
    file = fi.read().splitlines()

def get_trees(x: int, y: int) -> int:
    trees = 0
    offset = 0

    for line in range(0, len(file), y):
        if file[line][offset] == "#":
            trees += 1
        offset = (offset + x) % len(file[0])

    return trees

# Part 1
print(get_trees(3, 1))

# Part 2
print(prod((
    get_trees(1, 1),
    get_trees(3, 1),
    get_trees(5, 1),
    get_trees(7, 1),
    get_trees(1, 2))))
