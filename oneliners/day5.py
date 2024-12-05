from collections import defaultdict

input = [line.strip() for line in open('../inputs/day5.txt') if line.strip()]

rules = defaultdict(set)
for line in input:
    if '|' in line:
        a, b = map(int, line.split('|'))
        rules[a].add(b)

updates = [list(map(int, line.split(','))) for line in input if ',' in line]

is_correct = lambda u: all(not (set(u[:i]) & rules[u[i]]) for i in range(len(u)))

ans1 = sum(u[len(u) // 2] for u in updates if is_correct(u))

ans2 = sum(next(n for n in update if len(rules[n] & set(update)) == len(update) // 2)
                for update in updates if not is_correct(update))

print(f"{ans1}\n{ans2}")