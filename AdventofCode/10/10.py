with open("input", "r") as fi:
    file = sorted([int(line) for line in fi.readlines()])

# Part 1
ptr = 0
one, three = 0, 1

for i in file:
    if i == ptr+1:
        one += 1
        ptr = i
    elif i == ptr+2:
        ptr = i
    elif i == ptr+3:
        three += 1
        ptr = i

p1 = one * three

# Part 2
target = max(file) + 3
file.append(target)

explored = {}

def part2(n):
    if n in explored:
        return explored[n]
    if n == target:
        return 1
    else:
        total = 0
        if n+1 in file:
            total += part2(n+1)
        if n+2 in file:
            total += part2(n+2)
        if n+3 in file:
            total += part2(n+3)

        explored[n] = total
        return explored[n]

p2 = part2(0)

print(p1, p2)
