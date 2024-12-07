from itertools import product
import os

file = os.path.join(os.path.dirname(__file__), '7.in')
input = open(file).read().strip()

lines = input.split('\n')

def operate(nums, ops):
    result = nums[0]
    for i in range(len(ops)):
        if ops[i] == '+':
            result += nums[i + 1]
        elif ops[i] == '*':
            result *= nums[i + 1]
        elif ops[i] == '||':
            result = int(str(result) + str(nums[i + 1]))
    return result


def try1(target, numbers):
    n = len(numbers)
    if n == 1:
        return numbers[0] == target
    for operators in product(['+', '*'], repeat=n - 1):
        if operate(numbers, operators) == target:
            return True
    return False

def try2(target, numbers):
    n = len(numbers)
    if n == 1:
        return numbers[0] == target
    for operators in product(['+', '*', '||'], repeat=n - 1):
        if operate(numbers, operators) == target:
            return True
    return False

sum1 = 0
sum2 = 0

for line in lines:
    target, numbers = line.split(":")
    target = int(target.strip())
    numbers = list(map(int, numbers.strip().split()))
    if try1(target, numbers):
        sum1 += target
    if try2(target, numbers):
        sum2 += target

print(sum1)
print(sum2)