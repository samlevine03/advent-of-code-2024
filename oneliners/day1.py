from collections import Counter

llist, rlist = zip(*((int(line.split()[0]), int(line.split()[1])) for line in open("../inputs/day1.txt").readlines()))
rmap = Counter(rlist)

ans1 = sum(abs(l - r) for l, r in zip(sorted(llist), sorted(rlist)))
ans2 = sum(num * rmap.get(num, 0) for num in llist)

print(f"{ans1}\n{ans2}")