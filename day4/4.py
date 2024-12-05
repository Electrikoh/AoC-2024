import os

file = os.path.join(os.path.dirname(__file__), '4.in')
input = open(file).read().strip()

lines = input.split('\n')
counter1 = 0
counter2 = 0

R = len(lines)
C = len(lines[0])

# im sorry
for r in range(R):
    for c in range(C):
        if c+3<C and lines[r][c]=='X' and lines[r][c+1]=='M' and lines[r][c+2]=='A' and lines[r][c+3]=='S':
            counter1 += 1
        if r+3<R and lines[r][c]=='X' and lines[r+1][c]=='M' and lines[r+2][c]=='A' and lines[r+3][c]=='S':
            counter1 += 1
        if r+3<R and c+3<C and lines[r][c]=='X' and lines[r+1][c+1]=='M' and lines[r+2][c+2]=='A' and lines[r+3][c+3]=='S':
            counter1 += 1
        if c+3<C and lines[r][c]=='S' and lines[r][c+1]=='A' and lines[r][c+2]=='M' and lines[r][c+3]=='X':
            counter1 += 1
        if r+3<R and lines[r][c]=='S' and lines[r+1][c]=='A' and lines[r+2][c]=='M' and lines[r+3][c]=='X':
            counter1 += 1
        if r+3<R and c+3<C and lines[r][c]=='S' and lines[r+1][c+1]=='A' and lines[r+2][c+2]=='M' and lines[r+3][c+3]=='X':
            counter1 += 1
        if r-3>=0 and c+3<C and lines[r][c]=='S' and lines[r-1][c+1]=='A' and lines[r-2][c+2]=='M' and lines[r-3][c+3]=='X':
            counter1 += 1
        if r-3>=0 and c+3<C and lines[r][c]=='X' and lines[r-1][c+1]=='M' and lines[r-2][c+2]=='A' and lines[r-3][c+3]=='S':
            counter1 += 1

        if r+2<R and c+2<C and lines[r][c]=='M' and lines[r+1][c+1]=='A' and lines[r+2][c+2]=='S' and lines[r+2][c]=='M' and lines[r][c+2]=='S':
            counter2 += 1
        if r+2<R and c+2<C and lines[r][c]=='M' and lines[r+1][c+1]=='A' and lines[r+2][c+2]=='S' and lines[r+2][c]=='S' and lines[r][c+2]=='M':
            counter2 += 1
        if r+2<R and c+2<C and lines[r][c]=='S' and lines[r+1][c+1]=='A' and lines[r+2][c+2]=='M' and lines[r+2][c]=='M' and lines[r][c+2]=='S':
            counter2 += 1
        if r+2<R and c+2<C and lines[r][c]=='S' and lines[r+1][c+1]=='A' and lines[r+2][c+2]=='M' and lines[r+2][c]=='S' and lines[r][c+2]=='M':
            counter2 += 1

print(counter1)
print(counter2)