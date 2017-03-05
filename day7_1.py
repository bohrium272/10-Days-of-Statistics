def mean(arr):
    return float(sum(arr) / len(arr))


def sd(x):
    mu = mean(x)
    temp = round(float(sum([(e - mu) ** 2 for e in x])), 1)
    temp = temp / len(x)
    return round(temp ** 0.5, 1)


n = int(input())
x = [float(e) for e in input().split()]
y = [float(e) for e in input().split()]
mux = round(mean(x), 3)
muy = round(mean(y), 3)
sigx = round(sd(x), 3)
sigy = round(sd(y), 3)
rho = 0
for i in range(n):
    rho += ((x[i] - mux) * (y[i] - muy))
rho /= (n * sigx * sigy)

print(round(rho, 3))
