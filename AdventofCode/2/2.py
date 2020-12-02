correct_pass1 = correct_pass2 = 0

with open("input", "r") as fi:
    file = fi.readlines()
    
for line in file:
    count = 0

    # - 1 because the string starts at 1
    num1 = int(line.split("-")[0])-1
    num2 = int(line.split("-")[1][:2])-1
    # [0] to skip the ":"
    letter = line.split(" ")[1][0]
    password = line.split(" ")[2]

    # Part 1
    for l in password:
        if l == letter:
            count += 1
        
    if count >= num1+1 and count <= num2+1:
        correct_pass1 += 1
        
    # Part 2
    if((password[num1] == letter and password[num2] != letter) or (password[num2] == letter and password[num1] != letter)):
        correct_pass2 += 1

print(correct_pass1, correct_pass2)
