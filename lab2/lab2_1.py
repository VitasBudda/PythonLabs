import numpy as np

def input_int(name):
    print(f'Enter {name}:', end=' ')
    return int(input())

n = input_int('n')
X = np.array([[input_int(f'X[{i}][{j}]') for j in range(n)] for i in range(n)])
X2 = np.dot(X, X)

print(X)
print(sum(X.diagonal()))

print(X2)
print(sum(X2.diagonal()))