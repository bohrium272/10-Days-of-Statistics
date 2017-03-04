import math


def cdf(mean, sigma, x):
    res = (math.erf((x - mean) / (variance * math.sqrt(2))) + 1) / 2
    res = round(res, 4)
    return res


max_n = 250
mean = 2.4
variance = 2.0
n = 100

mean = mean * n
variance = variance * math.sqrt(n)

print(round(cdf(mean, variance, max_n), 4))
