with open("input", "r") as fi:
    file = [line.strip() for line in fi.readlines()]

def calc(expression, is_part2):
    while "(" in expression:
        start, end = 0, 0

        for pos, char in enumerate(expression):
            if char == "(":
                start = pos
            elif char == ")":
                end = pos
                break

        to_eval = expression[start+1:end]
        result = str(calc(to_eval, is_part2))
        expression = expression.replace("(" + to_eval + ")", result)

    result = 0
    op = ""
    buffer = []

    for pos in [pos for pos in expression.split() if pos != " "]:
        if pos == "+" or pos == "*":
            op = pos
        else:
            if len(op) > 0:
                if op == "+":
                    result += int(pos)
                else:
                    if is_part2:
                        buffer.append(result)
                        result = int(pos)
                    else:
                        result *= int(pos)
                op = ""
            else:
                result = int(pos)

    if is_part2:
        for num in buffer:
            result *= num

    return result

# Part 1 & 2
p1, p2 = 0, 0

for line in file:
    p1 += calc(line, False)
    p2 += calc(line, True)

print(p1, p2)

