import re
import time
res = 0
res_2 = 0

with open("day3.txt") as input_file:
    t0 = time.time()

    input = input_file.read()
    input = re.sub("\n", "", input)

    matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", input)

    def mult_match(match):
        return int(match[0]) * int(match[1])

    res1 = sum(map(mult_match, matches))
    print("res1", res1)

    input = re.sub(r"don't\(\).*?do\(\)", "", input)

    matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", input)
    res2 = sum(map(mult_match, matches))
    print("res2", res2)

    t1 = time.time()

print(t1 - t0)