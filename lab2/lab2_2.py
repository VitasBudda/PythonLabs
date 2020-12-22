import math

def rec(n, i = 1):
    if n == 0: return 1/3
    if i == n: return 1/3 * math.sqrt(1/math.factorial(n))
    return 1/3 * math.sqrt(1/math.factorial(i) + rec(n, i + 1))

n = int(input('n = '))
m = int(input('m = '))

print(math.pow(2, m) / rec(n))
