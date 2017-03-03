import math


avg, sigma = [70, 10]


def cdf(u, d, x):
    return (math.erf((x - u) / (d * math.sqrt(2))) + 1) / 2
# cdf = lambda x: 0.5 * (1 + math.erf((x - avg) / (sigma * (2 ** 0.5))))


print(100 * round((cdf(avg, sigma, 100) - cdf(avg, sigma, 80)), 4))
print(100 * round((cdf(avg, sigma, 100) - cdf(avg, sigma, 60)), 4))
print(100 * round((cdf(avg, sigma, 60) - cdf(avg, sigma, 0)), 4))
