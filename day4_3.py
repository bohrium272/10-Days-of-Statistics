def geometric(n, p, q):
    answer = q ** (n - 1)
    answer *= p
    return answer


p = [int(e) for e in input().split()]
p = p[0] / p[1]
n = int(input())
print(round(geometric(n, p, 1 - p), 3))
