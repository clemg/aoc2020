with open("input", "r") as fi:
    file = fi.read().splitlines()

# Part 1
memory = {}

for line in file:
    line = line.split()

    if line[0] == "mask":
        mask = line[2]
    else:
        result = []
        ind, val = int(line[0][4:-1]), format(int(line[2]), "036b")

        for index, bit in enumerate(mask):
            if bit != "X":
                result.append(bit)
            else:
                result.append(val[index])

        memory[ind] = int(''.join(result), 2)

p1 = sum(memory.values())

# Part 2
memory = {}

for line in file:
    line = line.split()

    if line[0] == "mask":
        mask = line[2]

    else:
        result = []
        ind, value = format(int(line[0][4:-1]), '036b'), int(line[2])

        for index, bit in enumerate(mask):
            if bit == "0":
                result.append(ind[index])
            else:
                result.append(bit)
                
        possible = []

        index = [index for index, bit in enumerate(result) if bit == "X"]

        for num in range(2**len(index)):
            tmp = result.copy()

            for idx, val in enumerate(format(num, f"0{len(index)}b")):
                tmp[index[idx]] = val

            possible.append(''.join(tmp))

        for possibility in possible:
            memory[int(possibility, 2)] = value

p2 = sum(memory.values())

print(p1, p2)
