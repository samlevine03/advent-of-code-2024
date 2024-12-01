left_list = []
right_list = []

right_dict = {}

with open("day1.txt") as input_file:
    for line in input_file.readlines():
        left, right = line.split()
        left = int(left)
        right = int(right)
        left_list.append(left)
        right_list.append(right)
        right_dict[right] = right_dict.get(right, 0) + 1

left_nums = left_list.copy()

left_list.sort()
right_list.sort()

answer = 0
while left_list:
    distance = abs(left_list.pop() - right_list.pop())
    answer += distance

print(answer)

answer = 0
for num in left_nums:
    answer += right_dict.get(num, 0) * num

print(answer)