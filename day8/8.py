import os

file = os.path.join(os.path.dirname(__file__), '8.in')
input = open(file).read().strip()

lines = input.split('\n')
antenna_map = []
antennas = {}

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char not in ". ":
            antenna_map.append((char, x, y))
            if char not in antennas:
                antennas[char] = []
            antennas[char].append((x, y))

anti1 = set()
anti2 = set()

for freq, positions in antennas.items():
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            x1, y1 = positions[i]
            x2, y2 = positions[j]
            dx = x2 - x1
            dy = y2 - y1
            
            antinode1 = (x1 - dx, y1 - dy)
            antinode2 = (x2 + dx, y2 + dy)
            anti = [antinode1, antinode2]
                
            
            for ax, ay in anti:
                if 0 <= ax < len(lines[0]) and 0 <= ay < len(lines):
                    anti1.add((ax, ay))
            

rows = len(lines)
cols = len(lines[0])

for row in range(rows):
    for col in range(cols):
        for k,vs in antennas.items():
            for (r1,c1) in vs:
                for (r2,c2) in vs:
                    if (r1,c1) != (r2,c2):
                            d1 = abs(row-r1) + abs(col-c1)
                            d2 = abs(row-r2) + abs(col-c2)

                            dr1 = row-r1
                            dr2 = row-r2
                            dc1 = col-c1
                            dc2 = col-c2

                            if 0 <= row < rows and 0 <= col<cols and (dr1*dc2 == dc1*dr2):
                                anti2.add((row,col))


print(len(anti1))
print(len(anti2))