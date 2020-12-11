# Part 1
with open("input", "r") as fi:
    file = [list(line.rstrip()) for line in fi]

def compute_seat(data, line_no, index):
    count = 0

    for offset in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
        X, Y = line_no + offset[0], index + offset[1]        
        if 0 <= X < len(data) and 0 <= Y < len(data[0]) and data[X][Y] == "#":
            count += 1

    return count

def count(max_count):
    while True:
        brake = True
        file_copy = [line.copy() for line in file]

        for line_no, letter in enumerate(file_copy):
            for index, value in enumerate(letter):
                count = compute_seat(file_copy, line_no, index)

                if value == "L" and count == 0:
                    file[line_no][index] = "#"

                elif value == "#" and count >= max_count:
                    file[line_no][index] = "L"
                brake &= (value == file[line_no][index])

        if brake:
            break

    return sum(line.count("#") for line in file)

p1 = count(4)

# Part 2
with open("input", "r") as fi:
    file = [list(line.rstrip()) for line in fi]

def compute_seat(data, line_no, index):
    count = 0

    for offset in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
        X, Y = line_no + offset[0], index + offset[1]

        while 0 <= X < len(data) and 0 <= Y < len(data[0]):
            if data[X][Y] == "#":
                count += 1
                break
            elif data[X][Y] == "L":
                break
            X += offset[0]
            Y += offset[1]

    return count

def count(max_count):
    while True:
        brake = True
        file_copy = [line.copy() for line in file]

        for line_no, letter in enumerate(file_copy):
            for index, value in enumerate(letter):
                count = compute_seat(file_copy, line_no, index)

                    
                if value == "L" and count == 0:
                    file[line_no][index] = "#"

                elif value == "#" and count >= max_count:
                    file[line_no][index] = "L"
                brake &= (value == file[line_no][index])

        if brake:
            break

    return sum(line.count("#") for line in file)

p2 = count(5)

print(p1, p2)
