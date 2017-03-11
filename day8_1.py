def mean(arr):
    return float(sum(arr) / len(arr))


def sd(x):
    mu = mean(x)
    temp = round(float(sum([(e - mu) ** 2 for e in x])), 1)
    temp = temp / len(x)
    return round(temp ** 0.5, 1)


n = 5
x = [95, 85, 80, 70, 60]
y = [85, 95, 70, 65, 70]
mux = round(mean(x), 3)
muy = round(mean(y), 3)
sigx = round(sd(x), 3)
sigy = round(sd(y), 3)
rho = 0
for i in range(n):
    rho += ((x[i] - mux) * (y[i] - muy))
rho /= (n * sigx * sigy)


b = rho * (sigy / sigx)
a = muy - (b * mux)

answer = a + b * 80
print(round(answer, 2))
