with open("input", "r") as fi:
    file = [line.strip(")\n") for line in fi.readlines()]

allergen_mapping = {}
safe_count = {}

for line in file:
    ingredients, allergens = line.split(" (contains ")
    for ingredient in ingredients.split():
        safe_count[ingredient] = safe_count.get(ingredient, 0) + 1

    for allergen in allergens.split(', '):
        if allergen not in allergen_mapping:
            allergen_mapping[allergen] = set(ingredients.split())
        else:
            allergen_mapping[allergen] = allergen_mapping[allergen].intersection(set(ingredients.split()))

# Part 1
for possible in (possible for allergen in allergen_mapping for possible in allergen_mapping[allergen]):
    if possible in safe_count:
        del safe_count[possible]

p1 = sum(safe_count.values())

# Part 2
while False in [len(x) == 1 for x in allergen_mapping.values()]:
    for a1 in [a for a in allergen_mapping if len(allergen_mapping[a]) == 1]:
        for a2 in [a for a in allergen_mapping if len(allergen_mapping[a]) > 1]:
            allergen_mapping[a2] = allergen_mapping[a2].difference(allergen_mapping[a1])

p2 = ','.join([list(allergen_mapping[allergen])[0] for allergen in sorted(allergen_mapping.keys())])

print(p1, p2)
