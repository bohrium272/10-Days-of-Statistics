import math


mean = 500
std = 80
n = 100
z = 1.96
margin_of_error = z * ((std) / math.sqrt(n))


print(round(mean - margin_of_error, 2))
print(round(mean + margin_of_error, 2))
