with open('inputs/day10.txt') as f:
    m = [list(map(int, list(row.strip()))) for row in f.readlines()]
    # m = []
    # for row in f.readlines():
    #     row = list(row.strip())
    #     for i in range(len(row)):
    #         if row[i] != '.':
    #             row[i] = int(row[i])
    #     m.append(row)

# print(m)
rows = len(m)
cols = len(m[0])

dirs = [(0,1), (0,-1), (1,0), (-1,0)]

def dfs(r, c, num, reached, trails):
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if nr not in range(rows) or nc not in range(cols):
            continue
        if m[nr][nc] == 9 and num == 8:
            trails.append((nr, nc))
            reached.add((nr, nc))
        elif m[nr][nc] == num + 1:
            dfs(nr, nc, num + 1, reached, trails)
    # print(reached)
    return len(reached), len(trails)
    # return reached

res = 0
res2 = 0
for r, row in enumerate(m):
    for c, char in enumerate(row):
        if char == 0:
            v1, v2 = dfs(r, c, 0, set(), [])
            res, res2 = res + v1, res2 + v2

print(res)
print(res2)