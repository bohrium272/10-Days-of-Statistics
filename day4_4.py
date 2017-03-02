def geometric(n, p, q):
    answer = q ** (n - 1)
    answer *= p
    return answer


p = [int(e) for e in input().split()]
p = p[0] / p[1]
n = int(input())

probability = 0
for i in range(1, n + 1):
    probability += geometric(i, p, 1 - p)

print(round(probability, 3))
