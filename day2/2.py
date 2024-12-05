import os

file = os.path.join(os.path.dirname(__file__), '2.in')
input = open(file).read().strip()

lines = input.split('\n')
counter = 0

def isSafe(report):
    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]
    
    if all(-3 <= diff <= -1 for diff in differences) or all(1 <= diff <= 3 for diff in differences):
        return True
    return False

for line in lines:
    levels = list(map(int, line.split()))

    if isSafe(levels):
        counter += 1
print(counter)

counter = 0
for line in lines:
    levels = list(map(int, line.split()))

    for i in range(len(levels)):
        modified_report = levels[:i] + levels[i+1:]
        if isSafe(modified_report):
            counter += 1
            break
print(counter)