nums = [2,0,1,7,4,14,18]

def calc(target):
    i = 3
    last_spoken = {}

    for i, n in enumerate(nums):
        last_spoken[n] = i

    prev = nums[-1]

    for i in range(len(nums)-1, target):
        if prev in last_spoken:
            n = i - last_spoken[prev]

        else:
            n = 0

        last_spoken[prev] = i
        prev = n

        if (i == target - 2):
            return n

# Part 1 & 2
print(calc(2020), calc(30000000))
