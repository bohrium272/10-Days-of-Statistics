from math import factorial
from math import e


def poisson(lam, n):
    return ((lam ** n) * (e ** (-lam)) / factorial(n))


avg = float(input())
n = float(input())

print(round(poisson(avg, n), 3))
