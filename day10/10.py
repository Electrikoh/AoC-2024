import os
from collections import deque

file = os.path.join(os.path.dirname(__file__), '10.in')
input = open(file).read().strip()
lines = input.split('\n')

tmap = [list(map(int, line)) for line in lines]
rows, cols = len(tmap), len(tmap[0])

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def calcScore(startRow, startCol):
    queue = deque([(startRow, startCol)])
    visited = set([(startRow, startCol)])
    reachable = set()

    while queue:
        r, c = queue.popleft()
        curHeight = tmap[r][c]
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                if tmap[nr][nc] == curHeight + 1:
                    visited.add((nr, nc))
                    queue.append((nr, nc))
                    if tmap[nr][nc] == 9:
                        reachable.add((nr, nc))
    
    return len(reachable)

def dfs(row, col, visited):
    if tmap[row][col] == 9:
        return 1
    
    visited.add((row, col))
    counter = 0
    curHeight = tmap[row][col]
    
    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if (
            0 <= nr < rows and 0 <= nc < cols
            and (nr, nc) not in visited
            and tmap[nr][nc] == curHeight + 1
        ):
            counter += dfs(nr, nc, visited)
    
    visited.remove((row, col))
    return counter

sum = 0
sum2 = 0
for row in range(rows):
    for col in range(cols):
        if tmap[row][col] == 0:
            sum += calcScore(row, col)
            sum2 += dfs(row, col, set())

print(sum)
print(sum2)