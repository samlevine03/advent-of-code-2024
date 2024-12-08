from itertools import combinations

with open('inputs/day8.txt') as f:
    m = [list(row.strip()) for row in f.readlines()]

nodes = {}
all_nodes = set()

for r, row in enumerate(m):
    for c, n in enumerate(row):
        if n != '.':
            all_nodes.add((r,c))
            if n in nodes:
                nodes[n].add((r,c))
            else:
                nodes[n] = {(r,c)}

antinodes = set()
for node, points in nodes.items():
    for p0, p1 in combinations(points, 2):
        dy, dx = p1[1] - p0[1], p1[0] - p0[0]
        p2 = (p1[0] + dx, p1[1] + dy)
        p3 = (p0[0] - dx, p0[1] - dy)
        if p2[0] in range(len(m[0])) and p2[1] in range(len(m)):
            antinodes.add(p2)
        if p3[0] in range(len(m[0])) and p3[1] in range(len(m)):
            antinodes.add(p3)

print(len(antinodes))

for r in m:
    print("".join(r))

antinodes = set()
for node, points in nodes.items():
    for p0, p1 in combinations(points, 2):
        antinodes.add(p0)
        antinodes.add(p1)
        dy, dx = p1[1] - p0[1], p1[0] - p0[0]
        p2 = (p1[0] + dx, p1[1] + dy)
        p3 = (p0[0] - dx, p0[1] - dy)
        while p2[0] in range(len(m[0])) and p2[1] in range(len(m)):
            antinodes.add(p2)
            p2 = (p2[0] + dx, p2[1] + dy)
        while p3[0] in range(len(m[0])) and p3[1] in range(len(m)):
            antinodes.add(p3)
            p3 = (p3[0] - dx, p3[1] - dy)

print(len(antinodes))