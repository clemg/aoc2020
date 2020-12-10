with open("input.txt", "r") as fi:
    file = fi.readlines()

def get_row_id(s):
    mini = 0
    maxi = 127
    to_add = 64

    for i in range(7):
        if s[i] == "B":
            mini += to_add
        else:
            maxi -= to_add
        to_add /= 2

    return int(mini)

def get_col_id(s):
    mini = 0
    maxi = 7
    to_add = 4

    for i in range(3):
        if s[i+7] == "R":
            mini += to_add
        else:
            maxi -= to_add
        to_add /= 2

    return int(mini)

# Part 1
p1 = 0
for line in file:
    p1 = max(p1, get_row_id(line) * 8 + get_col_id(line))

# Part 2
ids = []
for line in file:
    ids.append(get_row_id(line) * 8 + get_col_id(line))

for seat in sorted(ids):
    if seat + 1 not in ids and seat + 2 in ids:
        p2 = seat + 1

print(p1, p2)
