from collections import defaultdict

with open('inputs/day15.txt') as f:
    lines = [line.strip() for line in f.readlines()]

m = []
inst = ''
for line in lines:
    if '#' in line:
        m.append(list(line))
    else:
        inst += line

def printm(m, showidx=False):
    m_ = m.copy()
    if showidx:
        idxs = [str(int(idx) % 10) for idx in list(range(len(m[0])))]
        # print(idxs)
        print(f"  {''.join(idxs)}")
    x,y = ROBOT
    m_[x][y] = '@'
    for i,r in enumerate(m_):
        if showidx:
            print(f"{i} {''.join(r)}")
        else:
            print(''.join(r))
    print()
    m_[x][y] = '.'

# printm(m)
# print(inst)

sx,sy = -1,-1
for r in range(len(m)):
    for c in range(len(m[0])):
        if m[r][c] == '@':
            sx,sy = r,c
# print(sx,sy)

dirs = {
    'v': (1, 0),
    '>': (0, 1),
    '^': (-1, 0),
    '<': (0, -1)
}

LOGS = False

if LOGS:
    print(f"Initial state:")
    printm(m)

for i in inst:
    if LOGS:
        print(f"Move {i}:")
    # check if can move
    dx,dy = dirs[i]
    nx,ny = sx+dx,sy+dy

    # if it's a free space
    if m[nx][ny] == '.':
        m[sx][sy] = '.'
        m[nx][ny] = '@'
        sx,sy=nx,ny
        if LOGS:
            printm(m)
        continue

    # we can't move
    elif m[nx][ny] == '#':
        if LOGS:
            printm(m)
        continue

    # it's an O
    else:
        push = []
        checkx,checky = nx,ny
        while m[checkx][checky] == 'O':
            checkx += dx
            checky += dy
            push.append((checkx,checky))
        if m[checkx][checky] == '#':
            # we can't move
            if LOGS:
                printm(m)
            continue
        else:
            # print(checkx,checky)
            if LOGS:
                print(push)
            # move
            m[sx][sy] = '.'
            m[nx][ny] = '@'
            sx,sy=nx,ny

            # push
            for px,py in push:
                m[px][py] = 'O'

    if LOGS:
        printm(m)

    # break

# return sum of all boxes GPS coords
# printm(m)

sum = 0
for r in range(len(m)):
    for c in range(len(m[0])):
        if m[r][c] != 'O':
            continue
        sum += 100 * r + c

print(sum)

####################

m = []
inst = ''
for line in lines:
    row = []
    if '#' in line:
        for char in line:
            if char == '#':
                row.append('#')
                row.append('#')
            elif char == '.':
                row.append('.')
                row.append('.')
            elif char == '@':
                row.append('@')
                row.append('.')
            elif char == 'O':
                row.append('[')
                row.append(']')
            else:
                print('err')
        m.append(row)
    else:
        inst += line

for r in range(len(m)):
    for c in range(len(m[0])):
        if m[r][c] == '@':
            ROBOT = (r,c)
            m[r][c] = '.'
            break
printm(m)

for direction in inst:
    i, j = ROBOT
    # printm(m)

    if direction in '<>':
        dir = -1 if direction == '<' else 1
        target_bracket = ']' if direction == '<' else '['
        update_idx = j + dir
        while m[i][update_idx] == target_bracket:
            update_idx += dir * 2
        if m[i][update_idx] == '.':
            for l in range(update_idx, j, -dir):
                m[i][l] = m[i][l - dir]
            ROBOT = (i, j + dir)

    elif direction in '^v':
        dir = -1 if direction == '^' else 1
        queue = {(i + dir, j)}
        rows = defaultdict(set)
        while queue:
            x, y = queue.pop()
            match m[x][y]:
                case '#':
                    break
                case ']':
                    rows[x] |= {y - 1, y}
                    queue |= {(x + dir, y), (x + dir, y - 1)}
                case '[':
                    rows[x] |= {y, y + 1}
                    queue |= {(x + dir, y), (x + dir, y + 1)}
                case '.':
                    rows[x].add(y)
        else:
            for x in sorted(rows, reverse=(direction == 'v')):  # reverse for v
                for y in rows[x]:
                    m[x][y] = m[x - dir][y] if y in rows[x - dir] else '.'
            ROBOT = (i + dir, j)

res = 0
for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] == '[':
            res += 100*i + j


print(res)