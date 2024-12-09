import os

file = os.path.join(os.path.dirname(__file__), '9.in')
input = open(file).read().strip()

def getlayout(input):
    layout = []
    fileId = 0
    for i, ch in enumerate(input):
        length = int(ch)
        if i % 2 == 0:
            layout.extend([str(fileId)] * length)
            fileId += 1
        else:
            layout.extend(["."] * length)
    return layout


files = []
layout = getlayout(input)

while True:
    try:
        gapI = layout.index(".")
    except ValueError:
        break

    right = any(ch != "." for ch in layout[gapI + 1 :])
    if not right:
        break

    for i in range(len(layout) - 1, -1, -1):
        if layout[i] != ".":
            layout[gapI], layout[i] = layout[i], "."
            break

checksum = 0
for i, ch in enumerate(layout):
    if ch != ".":
        checksum += i * int(ch)

print(checksum)

# part 2

layout = getlayout(input)
fileBlocks = {}
curId = None
count = 0

for i, ch in enumerate(layout):
    if ch != ".":
        fid = int(ch)
        if fid != curId:
            curId = fid
            count = 1
            fileBlocks[fid] = [i, 1]
        else:
            count += 1
            fileBlocks[fid][1] = count

def findFreeBlock(layout, startPos, length):
    if startPos == 0:
        return None
    curStart = None
    curCount = 0
    for i in range(startPos):
        if layout[i] == ".":
            if curStart is None:
                curStart = i
                curCount = 1
            else:
                curCount += 1
        else:
            if curCount >= length:
                return curStart
            curStart = None
            curCount = 0
    if curStart is not None and curCount >= length:
        return curStart
    return None


for fid in sorted(fileBlocks.keys(), reverse=True):
    startPos, length = fileBlocks[fid]
    spanStart = findFreeBlock(layout, startPos, length)
    if spanStart is not None:
        for i in range(startPos, startPos + length):
            layout[i] = "."
        for i in range(spanStart, spanStart + length):
            layout[i] = str(fid)
        fileBlocks[fid][0] = spanStart

checksum = 0
for i, ch in enumerate(layout):
    if ch != ".":
        checksum += i * int(ch)

print(checksum)