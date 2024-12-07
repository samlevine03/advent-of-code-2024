matrix = [list(row.strip()) for row in open('../inputs/day6.txt').readlines()]

# idk if i can improve this anymore..? it's clean but oneliner is a stretch

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
sx, sy = next((r, c) for r, row in enumerate(matrix) for c, char in enumerate(row) if char == '^')

def traverse(matrix, sx, sy, dirs, ox=None, oy=None) -> tuple[dict, bool]: # (visited, loops?)
    seen, visited = set(), set()
    x, y, d = sx, sy, 0
    is_in_bounds = lambda x, y: 0 <= x < len(matrix) and 0 <= y < len(matrix[0])

    while is_in_bounds(x, y):
        if (x, y, d) in seen:
            return visited, True

        visited.add((x, y))
        seen.add((x, y, d))
        nx, ny = x + dirs[d][0], y + dirs[d][1]

        if not is_in_bounds(nx, ny):
            break
        if matrix[nx][ny] == '#' or (nx == ox and ny == oy):
            d = (d + 1) % 4
            continue
        x, y = nx, ny
    return visited, False

visited, _ = traverse(matrix, sx, sy, dirs)
print(len(visited))
print(sum(
    traverse(matrix, sx, sy, dirs, ox, oy)[1] 
    for ox, oy in visited 
))