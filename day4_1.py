from math import factorial

def c(n, x):
    return (factorial(n) / (factorial(x) * factorial(n - x)))


def binomial(n, x, p, q):
    answer = c(n, x)
    answer *= (p ** x)
    answer *= (q ** (n - x))
    return answer

s = [float(e) for e in input().split()]
p = s[0] / (s[0] + s[1])
q = s[1] / (s[0] + s[1])

prob = 0
for i in range(3, 7):
    prob += binomial(6, i, p, q)

print(round(prob, 3))
