import re

input = re.sub(r"\n", "", open("../inputs/day3.txt").read())
enabled_input = re.sub(r"don't\(\).*?(do\(\)|$)", "", input)

ans1 = sum(int(x) * int(y) for x, y in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", input))
ans2 = sum(
    int(x) * int(y) for x, y in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", enabled_input)
)

print(f"{ans1}\n{ans2}")