'''
Determination of Fibonacci Number
'''

from math import sqrt, floor

def is_perfect(n):
    rootn = floor(sqrt(n))
    return True if rootn * rootn == n else False

def is_fibonacci(N):
    x, y = 5 * N * N + 4, 5 * N * N - 4
    return is_perfect(x) or is_perfect(y)

N = 10000
# F = []
# for i in range(N + 1):
#     if is_fibonacci(i):
#         F.append(i)
# print(F)

def FibonacciSequence(n):
    F = [0, 1]
    for i in range(2, n + 1):
        F.append(F[i - 1] + F[i - 2])
    return F

N = 1000000
S = []
for i in range(1, N + 1):
    if is_fibonacci(i):
        S.append(i)

F = FibonacciSequence(len(S) + 2)[2:]
for i in range(len(S)):
    if F[i] != S[i]:
        print("Oops!", i, F[i], S[i])
        break
