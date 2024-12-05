import os

file = os.path.join(os.path.dirname(__file__), '1.in')
input = open(file).read().strip()

lines = input.split('\n')

arr1 = []
arr2 = []
sum = 0

for line in lines:
    x, y = line.split()
    x, y = int(x), int(y)
    arr1.append(x)
    arr2.append(y)

arr1.sort()
arr2.sort()

for i, item in enumerate(arr1):
    sum += abs(item - arr2[i])
print(sum)

sum = 0
for i, item in enumerate(arr1):
    count = arr2.count(item)
    sum += item * count
print(sum)