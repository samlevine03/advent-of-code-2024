import itertools

lines = [line for line in open('../inputs/day7.txt').read().splitlines() if line]

def eval_expression(nums, ops):
    res = nums[0]
    for num, op in zip(nums[1:], ops):
        res = res + num if op == 0 else res * num if op == 1 else int(f"{res}{num}")
    return res

def calculate(lines, ops):
    return sum(val for line in lines if any(
        (val := int(line.split(': ')[0])) == eval_expression(list(map(int, line.split(': ')[1].split())), ops)
        for ops in itertools.product(ops, repeat=len(line.split(': ')[1].split()) - 1)
    ))

print(calculate(lines, [0, 1]))
print(calculate(lines, [0, 1, 2]))