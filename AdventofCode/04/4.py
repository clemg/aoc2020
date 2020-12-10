with open("input", "r") as fi:
    file = fi.read()

# Part 1
p1 = 0
lines = file.split("\n\n")
lines = [elem.split() for elem in lines]

for line in lines:
    props = {}

    for prop in line:
        props[prop.split(":")[0]] = prop.split(":")[1]

    required_props = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    if not all(prop in props for prop in required_props):
        continue

    p1 += 1

# Part 2
p2 = 0
lines = file.split("\n\n")
lines = [elem.split() for elem in lines]

for line in lines:
    props = {}

    for prop in line:
        props[prop.split(":")[0]] = prop.split(":")[1]

    required_props = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    if not all(prop in props for prop in required_props):
        continue

    if not len(props["byr"]) == 4 or not props["byr"].isdigit() or not (1920 <= int(props["byr"]) <= 2002):
        continue
    if not len(props["iyr"]) == 4 or not props["iyr"].isdigit() or not (2010 <= int(props["iyr"]) <= 2020):
        continue
    if not len(props["eyr"]) == 4 or not props["eyr"].isdigit() or not (2020 <= int(props["eyr"]) <= 2030):
        continue
    if props["hgt"][-2:] not in ["cm", "in"] or not props["hgt"][:-2].isdigit():
        continue
    if props["hgt"].endswith("cm") and not (150 <= int(props["hgt"][:-2]) <= 193):
        continue
    if props["hgt"].endswith("in") and not (59 <= int(props["hgt"][:-2]) <= 76):
        continue
    if not props["hcl"].startswith("#") or not len(props["hcl"]) == 7 or not [letter in "0123456789abcdef" for letter in props["hcl"][:1]]:
        continue
    if not props["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        continue
    if not props["pid"].isdigit() or not len(props["pid"]) == 9:
        continue

    p2 += 1

print(p1, p2)
