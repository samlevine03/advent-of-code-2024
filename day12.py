from collections import Counter

with open('inputs/day12.txt') as f:
    m = [list(list(row.strip())) for row in f.readlines()]

seen = set()
regions = []
ROWS = len(m)
COLS = len(m[0])

dirs = [(0,1),(0,-1),(1,0),(-1,0)]

def dfs(r, c, region, p):
    region.add((r,c))
    seen.add((r,c))
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if (nr,nc) not in region:
            p.append((nr,nc))
        if nr not in range(ROWS) or nc not in range(COLS) or (nr,nc) in seen:
            continue
        if m[r][c] == m[nr][nc]:
            dfs(nr, nc, region, p)
    for point in region:
        while point in p:
            p.remove(point)
    return region, p

for r, row in enumerate(m):
    for c, char in enumerate(m):
        if ((r,c)) in seen:
            continue
        regions.append(dfs(r,c,set(),[]))

res = 0
for r,p in regions:
    res += len(r) * len(p)

print(res)


#############

def count_corners(r,p):
    corner_list = []


    outer_corners = 0
    for rx,ry in r:
        adj_blanks = []
        for dx,dy in dirs:
            nx,ny = rx+dx,ry+dy
            if (nx,ny) not in r:
                adj_blanks.append((nx,ny))
        
        # print(adj_blanks)

        if len(adj_blanks) == 4:
            # print(f"+4 @ {rx,ry}")
            outer_corners += 4
            for _ in range(4):
                corner_list.append((rx,ry))
        elif len(adj_blanks) == 3:
            # print(f"+2 @ {rx,ry}")
            outer_corners += 2
            for _ in range(2):
                corner_list.append((rx,ry))
        elif len(adj_blanks) == 2:
            if adj_blanks[0][0] == adj_blanks[1][0] or adj_blanks[0][1] == adj_blanks[1][1]:
                continue
            # print(f"+1 @ {rx,ry}")
            outer_corners += 1
            corner_list.append((rx,ry))

    # print(len(p) - len(set(p)))
    # print("out", outer_corners)
    # print(len(corner_list))
    # print(corner_list)
    # print(p)
    # print(r)

    inner_corners = 0
    zones = [
        [(-1,-1),(-1,0),(0,-1)],
        [(-1,0),(-1,1),(0,1)],
        [(0,1),(1,1),(1,0)],
        [(0,-1),(1,-1),(1,0)]
    ]
    for rx,ry in set(p):
        for zone in zones:
            num_r = 0
            for dx,dy in zone:
                nx,ny = rx+dx,ry+dy
                if (nx,ny) in r:
                    num_r += 1
            if num_r == 3:
                # print(f"+1 @ {rx,ry}")
                inner_corners += 1

    return outer_corners + inner_corners

res = 0
for r,p in regions:
    res += len(r) * count_corners(r,p)
    
print(res)