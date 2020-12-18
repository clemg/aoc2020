with open("input", "r") as fi:
    file = fi.read().strip().split("\n\n")

rules = file[0].split("\n")
ticket = file[1].split("\n")
nearby = [line.split(",") for line in file[2].split("\n")[1:]]

valid_nums = {}
for rule in rules:
    rule = rule.split(": ")
    ranges = rule[1].split(" or ")
    r1 = [int(x) for x in ranges[0].split('-')]
    r2 = [int(x) for x in ranges[1].split('-')]
    valid_nums[rule[0]] = list(range(r1[0], r1[1]+1)) + list(range(r2[0], r2[1]+1))

# Part 1
p1 = 0

invalid = []
valid = [item for sublist in [valid_nums[key] for key in valid_nums] for item in sublist]

for i, tick in enumerate(nearby):
    for num in tick:
        num = int(num)
        if num not in valid:
            p1 += num
            invalid.append(i)

# Part 2
p2 = 1
assign = {}

while len(assign) < len(rules):
    for value in range(len(nearby[0])):
        valid_fields = [key for key in valid_nums if key not in assign]

        for num in range(len(nearby)):
            if num in invalid:
                continue

            val = int(nearby[num][value])
            for valid in valid_fields:
                if val not in valid_nums[valid]:
                    valid_fields.remove(valid)
        if len(valid_fields) == 1:
            assign[valid_fields[0]] = value

my_ticket = [int(x) for x in ticket[1].split(',')]

for key in assign:
    if key.startswith("departure"):
        p2 *= my_ticket[assign[key]]

print(p1, p2)
