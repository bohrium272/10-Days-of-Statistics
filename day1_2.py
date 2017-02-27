def median(arr):
    if len(arr) % 2 == 0:
        temp = arr[(len(arr) // 2) - 1]
        return (temp + arr[(len(arr) // 2)]) / 2
    return arr[(len(arr) // 2)]


n = int(input())
temp = [int(e) for e in input().split()]
f = [int(e) for e in input().split()]
x = []
for i in range(n):
    x += ([temp[i]] * f[i])
x = sorted(x)
n = sum(f)
q = round((median(x[:(n // 2)])), 1)
if n % 2 == 0:
    q -= round(median(x[(n // 2):]), 1)
else:
    global q3
    q -= round(median(x[(n // 2) + 1:]), 1)
print(round(float(-q), 1))
