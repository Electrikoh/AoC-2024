import os
import re

file = os.path.join(os.path.dirname(__file__), '3.in')
input = open(file).read().strip()

sum = 0
matches = re.findall(r"mul\((\d+),(\d+)\)", input)

for match in matches:
    x, y = map(int, match)  # Convert the extracted strings to integers
    sum += x * y
print(sum)

sum = 0
matches = re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", input)
execute = True

for x, y, do, dont in matches:
    if do:
        execute = True
    if dont:
        execute = False
    if execute and x and y:
        sum += int(x) * int(y)
print(sum)