import re

part = 1
rules = {}
cache = {}
data = []

with open('input') as fi:
    file = [line.strip() for line in fi.readlines()]

for line in file:
    if len(line) == 0:
        part += 1
    elif part == 1:
        m = re.compile(r'^(\d+): "([ab])"$').match(line)
        if m:
            rules[int(m.group(1))] = m.group(2)
            continue
        m = re.compile(r'^(\d+): (\d+)( \d+)?( \| (\d+)( \d+)?)?$').match(line)
        if m:
            rules[int(m.group(1))] = [-1 if i is None else int(i) for i in m.group(2, 3, 5, 6)]
    elif part == 2:
        data.append(line)

def pattern(num):
    if num in cache:
        return cache[num]

    rule = rules[num]
    if type(rule) == str:
        cache[num] = rule
        return rule

    a = pattern(rule[0])
    cache[rule[0]] = a
    if rule[1] >= 0:
        b = pattern(rule[1])
        cache[rule[1]] = b
        a += b

    if rule[2] >= 0:
        c = pattern(rule[2])
        cache[rule[2]] = c
        if rule[3] >= 0:
            d = pattern(rule[3])
            cache[rule[3]] = d
            c += d
        a = '(?:' + a + '|' +  c + ')'

    cache[num] = a
    return a

# Part 1
p1 = sum([bool(re.fullmatch(pattern(0), message)) for message in data])

# Part 2
p2 = 0
for message in data:
    fm = re.fullmatch(f"(({cache[42]})+)(({cache[31]})+)", message)
    if fm:
        if len(fm.group(1)) // len(fm.group(2)) > len(fm.group(3)) // len(fm.group(4)):
            p2 += 1

print(p1, p2)
