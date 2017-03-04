import math


def cdf(mean, sigma, x):
    res = (math.erf((x - mean) / (variance * math.sqrt(2))) + 1) / 2
    res = round(res, 4)
    return res


max_n = 9800
mean = 205
variance = 15
n = 49

mean = mean * n
variance = variance * math.sqrt(n)

print(round(cdf(mean, variance, max_n), 4))
