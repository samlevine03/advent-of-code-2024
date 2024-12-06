with open('inputs/day6.txt') as f:
    matrix = [list(row.strip()) for row in f.readlines()]

def printm(matrix):
    for r in matrix:
        print(r,'')

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for r, row in enumerate(matrix):
    for c, char in enumerate(row):
        if char != '^':
            continue
        else:
            sx, sy = r, c
            break

visited = set()
d = 0
x, y = sx, sy
while 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):
    visited.add((x,y))
    # matrix[x][y] = 'X'

    dx, dy = dirs[d]
    nx, ny = x + dx, y + dy

    if nx in range(len(matrix)) and ny in range(len(matrix[0])):
        if matrix[nx][ny] == '#':
            d = (d + 1) % 4
            continue
        else:
            x, y = nx, ny
    else:
        break


print(len(visited))

visited = list(visited)

obs = set()
for i, (rr, cc) in enumerate(visited):
    print(f"{i}/{len(visited)}")
    if (rr, cc) != (sx, sy) and matrix[rr][cc] == '.':
        tmp = matrix[rr][cc]
        matrix[rr][cc] = '#'
        x, y = sx, sy
        d = 0
        seen = set()
        while 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):
            state = (x, y, d)
            if state in seen:
                matrix[rr][cc] = tmp
                obs.add((rr, cc))
                break
            seen.add(state)
            dx, dy = dirs[d]
            nx, ny = x + dx, y + dy
            if nx in range(len(matrix)) and ny in range(len(matrix[0])):
                if matrix[nx][ny] == '#':
                    d = (d + 1) % 4
                else:
                    x, y = nx, ny
            else:
                break
        matrix[rr][cc] = tmp

print(len(obs))