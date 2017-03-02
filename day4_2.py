from math import factorial


def c(n, x):
    return (factorial(n) / (factorial(x) * factorial(n - x)))


def binomial(n, x, p, q):
    answer = c(n, x)
    answer *= (p ** x)
    answer *= (q ** (n - x))
    return answer


p, n = [int(e) for e in input().split()]
p = p / 100
probability = 0

for i in range(0, 3):
    probability += binomial(10, i, p, 1 - p)

print(round(probability, 3))
probability = 0
for i in range(2, 11):
    probability += binomial(10, i, p, 1 - p)

print(round(probability, 3))
