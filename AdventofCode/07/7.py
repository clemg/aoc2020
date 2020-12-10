from parse import findall, search

def parse(file):
    return (search('{} bag', file)[0], [*findall('{:d} {} bag', file)])

with open("input", "r") as fi:
    file = dict(map(parse, fi.readlines()))

# Part 1
def part1(line):
    return any(value == "shiny gold" or part1(value) for _, value in file[line])

# Part 2
def part2(line):
    return sum(key + key * part2(value) for key, value in file[line])

print(sum(map(part1, file)), part2("shiny gold"))
