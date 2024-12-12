import os
from collections import deque

file = os.path.join(os.path.dirname(__file__), '12.in')
input = open(file).read().strip()
grid = input.split('\n')

p1 = 0
p2 = 0
rows = len(grid)
cols = len(grid[0])

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

visited = set()

for start_row in range(rows):
    for start_col in range(cols):
        if (start_row, start_col) in visited:
            continue

        queue = deque([(start_row, start_col)])
        curArea = 0
        curPer = 0
        dirs = {}

        while queue:
            currow, curcol = queue.popleft()

            if (currow, curcol) in visited:
                continue

            visited.add((currow, curcol))
            curArea += 1

            for dr, dc in directions:
                next_row, next_col = currow + dr, curcol + dc
                if 0 <= next_row < rows and 0 <= next_col < cols and grid[next_row][next_col] == grid[currow][curcol]:
                    queue.append((next_row, next_col))
                else:
                    curPer += 1
                    if (dr, dc) not in dirs:
                        dirs[(dr, dc)] = set()
                    dirs[(dr, dc)].add((currow, curcol))

        borders = 0

        for direction, cells in dirs.items():
            seen = set()
            for cell in cells:
                if cell in seen:
                    continue
                borders += 1
                side_queue = deque([cell])

                while side_queue:
                    sr, sc = side_queue.popleft()

                    if (sr, sc) in seen:
                        continue

                    seen.add((sr, sc))

                    for dr, dc in directions:
                        adj_row, adj_col = sr + dr, sc + dc
                        if (adj_row, adj_col) in cells:
                            side_queue.append((adj_row, adj_col))

        p1 += curArea * curPer
        p2 += curArea * borders

print(p1)
print(p2)