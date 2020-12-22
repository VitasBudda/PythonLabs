import math

def func(a, x, k):
    return math.sin(x**k) / (a**(2*k) + math.factorial(2*k))

def input_float(name):
    print(f'Enter {name}:', end=' ')
    return float(input())

x = input_float('x')
a = input_float('a')
e = input_float('e')

res = func(a, x, 1)
res_prev, k = 0, 2

while res - res_prev >= e:
    res_prev = res
    res += func(a, x, k)
    k += 1

print(res)