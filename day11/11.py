import os

file = os.path.join(os.path.dirname(__file__), '11.in')
input = open(file).read().strip()
input = [int(x) for x in input.split()]

dynamic = {}

def calc(x, n):
    if (x,n) in dynamic:
        return dynamic[(x,n)]
    
    if n == 0:
        next = 1
    elif x == 0:
        next = calc(1, n-1)
    elif len(str(x)) % 2 == 0:
        dstr = str(x)
        left = dstr[:len(dstr) // 2]
        right = dstr[len(dstr) // 2:]
        left, right = (int(left), int(right))
        next = calc(left, n - 1) + calc(right, n - 1)
    else:
        next = calc(x*2024, n-1)

    dynamic[(x,n)] = next
    return next

sum1 = sum(calc(x, 25) for x in input)
sum2 = sum(calc(x, 75) for x in input)
print(sum1)
print(sum2)