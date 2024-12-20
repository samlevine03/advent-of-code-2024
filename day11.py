from collections import deque
from functools import lru_cache

with open('inputs/day11.txt') as f:
    nums = list(map(int, f.readline().split()))

stones = nums
stones = [125,17]

def blink(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        return [int(str(stone)[0:len(str(stone))//2]), int(str(stone)[len(str(stone))//2::])]
    else:
        return [stone * 2024]
    
res = 0 

for b in range(25):
    next_stones = []
    for i in range(len(stones)):
        blinked = blink(stones[i])
        next_stones.extend(blinked)
    stones = next_stones
        
print(len(stones))
stones = nums

@lru_cache(None)
def blink_stones(stone, num_blinks):
    if num_blinks == 0:
        return 1
    blinked = blink(stone)
    if len(blinked) == 1:
        return blink_stones(blinked[0], num_blinks - 1)
    else:
        return sum(blink_stones(s, num_blinks - 1) for s in blinked)
    
result = sum(blink_stones(s, 75) for s in stones)
print(result)