'''
Finding the index of Fibonacci Number using Inverse Function of Binet's Formula
https://www.wolframalpha.com/input/?i=inverse+of+y+%3D+%281.618033988749895%5Ex%29++%2F+sqrt%285%29
'''

from math import sqrt, log

phi = (1 + sqrt(5)) / 2

def inverse_fibonacci(N):
    return round(log(sqrt(5) * N) / log(phi))

def FibonacciSequence(n):
    F = [0, 1]
    for i in range(2, n + 1):
        F.append(F[i - 1] + F[i - 2])
    return F

n = 50
F = FibonacciSequence(n)
for i in range(1, len(F)):
    print(i, inverse_fibonacci(F[i]))

# n = 1000
# F = FibonacciSequence(n)
# for i in range(1, len(F)):
#     print(i, inverse_fibonacci(F[i]))
#     if i != inverse_fibonacci(F[i]):
#         print("Oops!", i, inverse_fibonacci(F[i]))
#         break

