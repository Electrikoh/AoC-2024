import os

file = os.path.join(os.path.dirname(__file__), '6.in')
input = open(file).read().strip()

grid = input.split('\n')

directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
turnRight = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

def walk(grid):
    
    start = None
    facing = None
    for y, row in enumerate(grid):
        for x, field in enumerate(row):
            if field in directions:
                start = (y, x)
                facing = field
                break
        if start:
            break
    
    visited = set()
    y, x = start
    rows, cols = len(grid), len(grid[0])
    
    while 0 <= y < rows and 0 <= x < cols:
        visited.add((y, x))
        dy, dx = directions[facing]
        ny, nx = y + dy, x + dx
        
        if 0 <= ny < rows and 0 <= nx < cols and grid[ny][nx] == '#':
            facing = turnRight[facing] 
        else:
            y, x = ny, nx
    
    return len(visited)

def walkWithObstruction(grid, obstruction):
    
    start = None
    facing = None
    for y, row in enumerate(grid):
        for x, field in enumerate(row):
            if field in directions:
                start = (y, x)
                facing = field
                break
        if start:
            break
    
    yObs, xObs = obstruction
    grid[yObs] = grid[yObs][:xObs] + '#' + grid[yObs][xObs + 1:]
    
    visited = set()
    y, x = start
    rows, cols = len(grid), len(grid[0])
    
    state = (y, x, facing)
    while state not in visited:
        visited.add(state)
        dy, dx = directions[facing]
        ny, nx = y + dy, x + dx
        
        if 0 <= ny < rows and 0 <= nx < cols and grid[ny][nx] == '#':
            facing = turnRight[facing]
        else:
            y, x = ny, nx
        
        state = (y, x, facing)
        
        if not (0 <= y < rows and 0 <= x < cols):
            return False
    
    return True

# takes like 50 seconds, but works 🥴
def tryAllPositions(grid):
    counter = 0
    rows, cols = len(grid), len(grid[0])
    
    for y in range(rows):
        for x in range(cols):
            if grid[y][x] == '.':
                if walkWithObstruction([row[:] for row in grid], (y, x)):
                    counter += 1
                    print(counter)
    
    return counter

result1 = walk(grid)
result2 = tryAllPositions(grid)
print(f"p1: {result1}")
print(f"p2: {result2}")