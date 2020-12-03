from itertools import combinations
from math import prod

numbers = []
with open("input", "r") as fi:
    for line in fi:
        numbers.append(int(line))

# Part 1
for combi in combinations(numbers, 2):
    if sum(combi) == 2020:
        print(prod(combi))

# Part 2
for combi in combinations(numbers, 3):
    if sum(combi) == 2020:
        print(prod(combi))
