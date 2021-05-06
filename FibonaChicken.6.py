'''
Applying Zeckendorf's Decomposition for a Number Which is NOT a Fibonacci Number.
'''

from math import sqrt, log, floor

phi = (1 + sqrt(5)) / 2
phi_ = 1 - phi

def Binet(i):
    return round((phi ** i - phi_ ** i) / sqrt(5))

def inverse_fibonacci(N):
    return round(log(sqrt(5) * N) / log(phi))

def is_perfect(n):
    rootn = floor(sqrt(n))
    return True if rootn * rootn == n else False

def is_fibonacci(N):
    x, y = 5 * N * N + 4, 5 * N * N - 4
    return is_perfect(x) or is_perfect(y)

def FibonaChicken(N):
    if N <= 2:
        return 1
    i = inverse_fibonacci(N)
    if is_fibonacci(N):
        return Binet(i - 1)
    else:
        while N > Binet(i):
            i += 1
        return Binet(i - 2) + FibonaChicken(N - Binet(i - 1))

for N in range(15, 65):
    print(N, FibonaChicken(N))

