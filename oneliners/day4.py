matrix = [list(row) for row in open('../inputs/day4.txt').read().split('\n')]

def count_xmas(r, c):
    xmas = 'XMAS'
    return sum(
        all(0 <= r + dr * i < len(matrix) and 0 <= c + dc * i < len(matrix[0]) and matrix[r + dr * i][c + dc * i] == xmas[i]
            for i in range(1, len(xmas))) for dr in [-1,0,1] for dc in [-1,0,1]
    )

ans1 = sum(count_xmas(r, c) for r in range(len(matrix)) for c in range(len(matrix[0])) if matrix[r][c] == 'X')

def count_x_mas(r, c):
    return int(matrix[r][c] == "A" and 
               {"M", "S"} == {matrix[r-1][c-1], matrix[r+1][c+1]} == {matrix[r-1][c+1], matrix[r+1][c-1]})

ans2 = sum(count_x_mas(r, c) for r in range(1, len(matrix) - 1) for c in range(1, len(matrix[0]) - 1))

print(f"{ans1}\n{ans2}")