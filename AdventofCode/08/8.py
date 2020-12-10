with open("input", "r") as fi:
    file = [line.strip() for line in fi]

# Part 1
def part1():
    ptr = 0
    acc = 0
    already_done = []

    while True:
        if ptr not in already_done:
            already_done.append(ptr)
            
            value = int(file[ptr].split(" ")[1])
            if file[ptr].startswith("nop"):
                ptr += 1
            elif file[ptr].startswith("acc"):
                acc += value
                ptr+=1
            elif file[ptr].startswith("jmp"):
                ptr += value
        else:
            break

    return acc

# Part 2
def part2():
    potentials = []

    for instruction in range(len(file)):
        if not file[instruction].startswith("acc"):
            potentials.append(instruction)

    for potential in potentials:
        ptr = 0
        acc = 0
        already_done = []

        while True:
            if ptr in already_done:
                break

            already_done.append(ptr)
            value = int(file[ptr].split(" ")[1])

            if file[ptr].startswith("nop"):
                if ptr != potential:
                    ptr += 1
                else:
                    ptr += value
            elif file[ptr].startswith("acc"):
                    acc += value
                    ptr += 1
            elif file[ptr].startswith("jmp"):
                if ptr == potential:
                    ptr += 1
                else:
                    ptr += value

            if ptr == len(file):
                return acc


print(part1(), part2())
