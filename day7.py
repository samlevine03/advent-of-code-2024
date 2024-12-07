import itertools

example = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

with open('inputs/day7.txt') as f:
    input = f.read().split('\n')
    

# for r in input:
    # print(r)

# input = example.split('\n')

def eval(nums, ops):
    res = nums[0]
    for (num, op) in zip(nums[1::], ops):
        # print(num, op)
        if op == 0:
            res += num
        elif op == 1:
            res *= num
        elif op == 2:
            str_res = str(res)
            str_num = str(num)
            res = int(str_res + str_num)
    # print(nums, ops, res)
    return res

part1 = 0
for r in input:
    val, nums = r.split(': ')
    val = int(val)
    nums = [int(num) for num in nums.split(' ')]

    for c in itertools.product([0, 1], repeat=len(nums) - 1):
        if val == eval(nums, c):
            part1 += val
            break

print(part1)
part2 = 0
for r in input:
    val, nums = r.split(': ')
    val = int(val)
    nums = [int(num) for num in nums.split(' ')]

    for c in itertools.product([0, 1, 2], repeat=len(nums) - 1):
        if val == eval(nums, c):
            part2 += val
            break

print(part2)
