import os

file = os.path.join(os.path.dirname(__file__), '5.in')
input = open(file).read().strip()

ruleSection, updatesSection = input.split('\n\n')

rules = []
for rule in ruleSection.split('\n'):
    x, y = rule.split('|')
    rules.append((int(x), int(y)))

updates = []
for update in updatesSection.split('\n'):
    updates.append(list(map(int, update.split(','))))

def is_update_valid(update, rules):
    update_indices = {page: i for i, page in enumerate(update)}
    for x, y in rules:
        if x in update_indices and y in update_indices:
            if update_indices[x] > update_indices[y]:
                return False
    return True

sum = 0
for update in updates:
    if is_update_valid(update, rules):
        sum += update[len(update) // 2]
print(sum)

def fix(update, rules):
    fixed = update[:]
    changed = True
    while changed:
        changed = False
        for x, y in rules:
            if x in fixed and y in fixed:
                xIndex = fixed.index(x)
                yIndex = fixed.index(y)
                if xIndex > yIndex:
                    fixed[xIndex], fixed[yIndex] = fixed[yIndex], fixed[xIndex]
                    changed = True
    return fixed

sum = 0
for update in updates:
    if not is_update_valid(update, rules):
        fixed = fix(update, rules)
        sum += fixed[len(fixed) // 2]
print(sum)