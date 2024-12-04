reports = [[int(x) for x in line.split()] for line in open('../inputs/day2.txt')]

def is_valid(r):
    return all(0 < abs(r[i] - r[i-1]) <= 3 and (r[i] > r[i-1]) == (r[0] < r[1]) for i in range(1, len(r)))

ans1 = sum(is_valid(r) for r in reports)
ans2 = sum(is_valid(r) or any(is_valid(r[:i] + r[i+1:]) for i in range(len(r))) for r in reports)

print(f"{ans1}\n{ans2}")