from collections import defaultdict
from itertools import combinations
from math import gcd

m = [list(row.strip()) for row in open('../inputs/day8.txt').readlines()]

nodes = defaultdict(set)
[[nodes[n].add((r, c)) for c, n in enumerate(row) if n != '.'] for r, row in enumerate(m)]

antinodes = {
    p2 for points in nodes.values() for p0, p1 in combinations(points, 2)
    for dx, dy in [(p1[0] - p0[0], p1[1] - p0[1])]
    for p2 in [(p1[0] + dx, p1[1] + dy), (p0[0] - dx, p0[1] - dy)]
    if 0 <= p2[0] < len(m) and 0 <= p2[1] < len(m[0])
}
print(len(antinodes))

antinodes = {
    p for points in nodes.values() for p0, p1 in combinations(points, 2)
    for p in [p0, p1] + [
        (p0[0] + k * (p1[0] - p0[0]), p0[1] + k * (p1[1] - p0[1]))
        for k in range(-max(len(m), len(m[0])), max(len(m), len(m[0])) + 1)
    ]
    if 0 <= p[0] < len(m) and 0 <= p[1] < len(m[0])
}
print(len(antinodes))