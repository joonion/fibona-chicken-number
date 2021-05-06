'''
Binet Formula for Generating ith Fibonacci Number
'''

from math import sqrt, floor

phi = (1 + sqrt(5)) / 2
phi_ = 1 - phi

def Binet(i):
    return round((phi ** i - phi_ ** i) / sqrt(5))

# n = 50
# for i in range(n + 1):
#     print(i, Binet(i))

def FibonacciSequence(n):
    F = [0, 1]
    for i in range(2, n + 1):
        F.append(F[i - 1] + F[i - 2])
    return F

n = 1000
F = FibonacciSequence(n)
for i in range(n + 1):
    if F[i] != Binet(i):
        print("Oops!", i, F[i], Binet(i))
        break
