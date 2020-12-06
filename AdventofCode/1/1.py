from itertools import combinations
from math import prod

with open("input", "r") as fi:
    numbers = [int(line) for line in fi.read().splitlines()]

# Part 1
for combi in combinations(numbers, 2):
    if sum(combi) == 2020:
        print(prod(combi))

# Part 2
for combi in combinations(numbers, 3):
    if sum(combi) == 2020:
        print(prod(combi))
