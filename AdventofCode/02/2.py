with open("input", "r") as fi:
    file = fi.readlines()

p1 = p2 = 0

for line in file:
    # - 1 because the string starts at 1
    num1 = int(line.split("-")[0])-1
    num2 = int(line.split("-")[1][:2])-1
    # [0] to skip the ":"
    letter = line.split(" ")[1][0]
    password = line.split(" ")[2]

    # Part 1
    if num1+1 <= password.count(letter) <= num2+1:
        p1 += 1

    # Part 2
    if((password[num1] == letter and password[num2] != letter) or (password[num2] == letter and password[num1] != letter)):
        p2 += 1

print(p1, p2)
