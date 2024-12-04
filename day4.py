with open ('inputs/day4.txt') as f:
    input = f.read()

rows = input.split('\n')

matrix = []

for row in rows:
    l = []
    for c in row:
        l.append(c)
    matrix.append(row)


def dfs(r, c):
    count = 0
    dirs = [(0, 1), (0, -1),
            (1, 0), (-1, 0),
            (1, 1), (-1, -1),
            (1, -1), (-1, 1)]
    
    word = 'XMAS'
    
    for dr, dc in dirs:
        new_r, new_c = r + dr, c + dc
        char_idx = 1
        while 0 <= new_r < len(matrix) and 0 <= new_c < len(matrix[0]):
            if matrix[new_r][new_c] == word[char_idx]:
                if matrix[new_r][new_c] == 'S':
                    count += 1
                    break
                else:
                    new_r += dr
                    new_c += dc
                    char_idx += 1
            else:
                break

    return count
    

ans = 0
for r, row in enumerate(matrix):
    for c, char in enumerate(row):
        if char != 'X':
            continue
        else:
            num = dfs(r, c)
            ans += num

print(ans)

ans = 0
for r, row in enumerate(matrix):
    if r == 0 or r == len(matrix) - 1:
        continue
    for c, char in enumerate(row):
        if c == 0 or c == len(row) - 1:
            continue
        if char != 'A':
            continue
        else:
            freqs = {'S': 0, 'M': 0, 'A': 0, 'X': 0}
            freqs[matrix[r+1][c+1]] += 1
            freqs[matrix[r-1][c-1]] += 1
            freqs[matrix[r+1][c-1]] += 1
            freqs[matrix[r-1][c+1]] += 1
            if freqs == {'S': 2, 'M': 2, 'A': 0, 'X': 0}:
                if matrix[r-1][c-1] == matrix[r+1][c+1]:
                    continue
                ans += 1

print(ans)
