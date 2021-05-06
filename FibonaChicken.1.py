'''
Fibonacci Sequence and Golden Ratio
'''

from math import sqrt

def FibonacciSequence(n):
    F = [0, 1]
    for i in range(2, n + 1):
        F.append(F[i - 1] + F[i - 2])
    return F

n = 50
F = FibonacciSequence(n)
for i in range(1, len(F) - 1):
    print(i, ":", F[i], F[i+1]/F[i], F[i]/F[i+1])

phi = (1 + sqrt(5)) / 2
phi_ = 1 - phi
print(phi)
print(-phi_)
