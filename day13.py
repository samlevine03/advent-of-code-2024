import re
from functools import lru_cache
from collections import deque
from math import gcd
# import numpy as np

with open('inputs/day13.txt') as f:
    lines = [line.strip() for line in f.readlines()]

# print(lines)

input = []
idx = 0

offset = 10000000000000

while idx < len(lines):
    a = lines[idx]
    b = lines[idx+1]
    p = lines[idx+2]
    idx += 4

    a_nums = re.findall(r"X\+(\d+).*?Y\+(\d+)", a)
    a_nums = (int(a_nums[0][0]), int(a_nums[0][1]))

    b_nums = re.findall(r"X\+(\d+).*?Y\+(\d+)", b)
    b_nums = (int(b_nums[0][0]), int(b_nums[0][1]))

    p_nums = re.findall(r"X\=(\d+).*?Y\=(\d+)", p)
    p_nums = (int(p_nums[0][0]), int(p_nums[0][1]))

    # print(a_nums,b_nums,p_nums)

    input.append([a_nums, b_nums, p_nums])

# 3 tokens to push A
# 1 token to push B

# @lru_cache(None)
def solve(a,b,p):
    ax,ay = a[0],a[1]
    bx,by = b[0],b[1]
    px,py = p[0],p[1]

    min_cost = float('inf')
    best = None

    for a_count in range(101):
        for b_count in range(101):
            x = a_count * ax + b_count * bx
            y = a_count * ay + b_count * by
            if x == px and y == py:
                cost = 3 * a_count + b_count
                if cost < min_cost:
                    min_cost = cost
                    best = (a_count, b_count)

    return min_cost if best else 0

    
total_cost = 0
prizes = 0

for machine in input:
    cost = solve(machine[0],machine[1],machine[2])

    if cost is not None:
        prizes += 1
        total_cost += cost


    # break
print(total_cost)

#########


def solve2(a, b, p):
    a1, a2 = a[0], a[1]
    b1, b2 = b[0], b[1]
    c1, c2 = p[0]+offset, p[1]+offset

    D = a1 * b2 - a2 * b1
    D_x = c1 * b2 - c2 * b1
    D_y = a1 * c2 - a2 * c1

    A = D_x / D
    B = D_y / D

    if A == int(A) and B == int(B):
        return A * 3 + B
    else:
        return 0
    
total_cost = 0

for machine in input:
    cost = solve2(machine[0],machine[1],machine[2])
    total_cost += cost

print(int(total_cost))