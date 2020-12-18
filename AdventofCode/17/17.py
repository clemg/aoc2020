from itertools import product, chain
from collections import Counter

with open("input", "r") as fi:
    file = [line.strip() for line in fi]

def solve_dim(n):
    diffs = list(product((1, 0, -1), repeat=n))
    diffs.remove((0,) * n)

    current_state = set()

    for y, line in enumerate(file):
        for x, val in enumerate(line):
            if val == "#":
                current_state.add((x, y) + (0,) * (n - 2))

    get_neighbors = lambda pos: [tuple([pos[i] + diff[i] for i in range(n)]) for diff in diffs]

    for _ in range(6):
        counter = Counter(chain.from_iterable(get_neighbors(pos) for pos in current_state))

        stay_on = set(x for x in current_state if counter[x] in (2, 3))
        become_on = set(x for x, cnt in counter.items() if cnt == 3 and x not in current_state)

        current_state = stay_on.union(become_on)

    return len(current_state)

print(solve_dim(3), solve_dim(4))
