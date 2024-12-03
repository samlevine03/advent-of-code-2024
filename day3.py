import re
res = 0
res_2 = 0

with open("day3.txt") as input_file:
    input = input_file.read()
    input = re.sub("\n", "", input)

    mults = re.findall(r"mul\(\d{1,3},\d{1,3}\)", input)
    for mult in mults:
        l, r = mult.split(',')
        l = l.split('(')[-1]
        r = r.split(')')[0]
        res += int(l) * int(r)

    input = re.sub(r"don't\(\).*?do\(\)", "", input)
    mults = re.findall(r"mul\(\d{1,3},\d{1,3}\)", input)
    for mult in mults:
        l, r = mult.split(',')
        l = l.split('(')[-1]
        r = r.split(')')[0]
        res_2 += int(l) * int(r)

print(res)
print(res_2)