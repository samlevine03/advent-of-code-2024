left_list = []
right_list = []

with open("day1.txt") as input_file:
    for line in input_file.readlines():
        left, right = line.split()
        left_list.append(int(left))
        right_list.append(int(right))

left_list.sort()
right_list.sort()

answer = 0
while left_list:
    distance = abs(left_list.pop() - right_list.pop())
    answer += distance

print(answer)