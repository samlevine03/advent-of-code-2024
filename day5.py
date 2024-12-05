import re
import random
from math import factorial

with open('inputs/day5.txt') as f:
    input = f.readlines()

rules = {}
updates = []

for line in input:
    line = re.sub('\n', '', line)
    if line == '':
        continue
    elif '|' in line:
        a, b = (int(x) for x in line.split('|'))
        if a in rules:
            rules[a].add(b)
        else:
            rules[a] = {b}
        
    else:
        update = [int(x) for x in line.split(',')]
        updates.append(update)

ans = 0
for update in updates:
    for i in range(len(update) - 1, - 1, -1):
        curr_must_be_before = rules.get(update[i], set())
        curr_is_after = set(update[0:i])
        if not curr_is_after.isdisjoint(curr_must_be_before):
            break
        elif i == 0:
            ans += update[len(update) // 2]

print(ans)

def is_correct(update):
    for i in range(len(update) - 1, - 1, -1):
        curr_must_be_before = rules.get(update[i], set())
        curr_is_after = set(update[0:i])
        if not curr_is_after.isdisjoint(curr_must_be_before):
            return False
        elif i == 0:
            return True


ans = 0
for ui, update in enumerate(updates):
    update_set = set(update)
    for i in range(len(update) - 1, - 1, -1):
        curr_must_be_before = rules.get(update[i], set())
        curr_is_after = set(update[0:i])
        if not curr_is_after.isdisjoint(curr_must_be_before):
            for n in update:
                if len(rules.get(n, set()).intersection(update_set)) == len(update) // 2:
                    ans += n
            break
        elif i == 0:
            continue

print(ans)