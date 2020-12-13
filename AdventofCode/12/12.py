with open("input", "r") as fi:
    file = [line.strip() for line in fi.readlines()]

# Part 1
pos = [0, 0]
direction = [1, 0]

for line in file:
    num = int(line[1:])

    if line[0] == "N":
        pos[1] += num
    elif line[0] == "S":
        pos[1] -= num
    elif line[0] == "E":
        pos[0] += num
    elif line[0] == "W":
        pos[0] -= num

    elif line[0] == "L":
        num %= 360
        while num > 0:
            direction = [-direction[1], direction[0]]
            num -= 90
    elif line[0] == "R":
        num %= 360
        num = 360 - num
        while num > 0:
            direction = [-direction[1], direction[0]]
            num -= 90

    elif line[0] == "F":
        pos = [pos[0] + direction[0] * num, pos[1] + direction[1] * num]

p1 = abs(pos[0]) + abs(pos[1])

# Part 2
waypoint_pos = [10, 1]
pos = [0, 0]

for line in file:
    num = int(line[1:])

    if line[0] == "N":
        waypoint_pos[1] += num
    elif line[0] == "S":
        waypoint_pos[1] -= num
    elif line[0] == "E":
        waypoint_pos[0] += num
    elif line[0] == "W":
        waypoint_pos[0] -= num

    elif line[0] == "L":
        num %= 360
        while num > 0:
            waypoint_pos = [-waypoint_pos[1], waypoint_pos[0]]
            num -= 90
    elif line[0] == "R":
        num %= 360
        num = 360 - num
        while num > 0:
            waypoint_pos = [-waypoint_pos[1], waypoint_pos[0]]
            num -= 90

    elif line[0] == "F":
        pos = [pos[0] + waypoint_pos[0] * num, pos[1] + waypoint_pos[1] * num]

p2 = abs(pos[0]) + abs(pos[1])

print(p1, p2)
