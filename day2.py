reports = []

with open("inputs/day2.txt") as input_file:
    for line in input_file.readlines():
        report = [int(x) for x in line.split()]
        reports.append(report)

def report_is_valid(report: list[int]) -> bool:
    if report[0] < report[1]:
        increasing = True
    elif report[0] > report[1]:
        increasing = False
    else:
        return False
    
    for i, level in enumerate(report):
        if i == 0:
            continue
        if abs(level - report[i - 1]) > 3:
            return False
        if level > report[i - 1] and not increasing:
            return False
        if level < report[i - 1] and increasing:
            return False
        if level == report[i - 1]:
            return False
        
    return True

ans = 0
for report in reports:
    if report_is_valid(report):
        ans += 1
        
print(ans)

ans = 0

for report in reports:
    if report_is_valid(report):
        ans += 1
        continue

    else:
        # just test every version
        for i, _ in enumerate(report):
            test_report = report.copy()
            test_report.pop(i)
            if report_is_valid(test_report):
                ans += 1
                break

print(ans)