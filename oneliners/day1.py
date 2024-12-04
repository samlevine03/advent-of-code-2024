llist = []
rlist = []
rmap = {}

with open("../inputs/day1.txt") as f:
    for line in f:
        l, r = map(int, line.split())
        llist.append(l)
        rlist.append(r)
        rmap[r] = rmap.get(r, 0) + 1

ans1 = sum(abs(l - r) for l, r in zip(sorted(llist), sorted(rlist)))
ans2 = sum(num * rmap.get(num, 0) for num in llist)

print(f"{ans1}\n{ans2}")