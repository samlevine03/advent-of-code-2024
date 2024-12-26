import re

with open('inputs/day14.txt') as f:
    lines = [line.strip() for line in f.readlines()]

robots = []
for line in lines:
    nums = re.findall(r"p=(-?\d+),(-?\d+).+v=(-?\d+),(-?\d+)", line)[0]
    nums = [int(num) for num in nums]
    robots.append(nums)

width = 101
height = 103
midpoint_x = width // 2
midpoint_y = height // 2

counts = [0] * 4

for bot in robots:
    x,y = bot[0],bot[1]
    vx,vy = bot[2],bot[3]
    
    x = (x + 100 * vx) % width
    y = (y + 100 * vy) % height

    if x == midpoint_x or y == midpoint_y:
        continue

    if x < midpoint_x and y < midpoint_y:
        counts[0] += 1
    elif x > midpoint_x and y < midpoint_y:
        counts[1] += 1
    elif x < midpoint_x and y > midpoint_y:
        counts[2] += 1
    elif x > midpoint_x and y > midpoint_y:
        counts[3] += 1

print(counts)
res = 1
for c in counts:
    res *= c
print(res)

########

m = [['.'] * width for _ in range(height)]

def printm(m):
    for r in m:
        print(''.join(r))
    print()

# printm(m)

def move_bots(seconds):
    for i in range(height):
        for j in range(width):
            m[i][j] = '.'

    for bot in robots:
        x,y = bot[0],bot[1]
        vx,vy = bot[2],bot[3]        
        x = (x + seconds * vx) % width
        y = (y + seconds * vy) % height
        m[y][x] = '#'

# move_bots(1)
# printm(m)

s = 0
while True:
    move_bots(s)
    for r in m:
        # PLEASE WORK LOL
        if '##########' in ''.join(r):
            printm(m)
            print(s)

    s += 1

    if s > 10000:
        break