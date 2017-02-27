def median(arr):
    if len(arr) % 2 == 0:
        temp = arr[(len(arr) // 2) - 1]
        return (temp + arr[(len(arr) // 2)]) / 2
    return arr[(len(arr) // 2)]


n = int(input())
x = [int(e) for e in input().split()]
x = sorted(x)
print(int(median(x[:(n // 2)])))
print(int(median(x)))
if n % 2 == 0:
    print(int(median(x[(n // 2):])))
else:
    print(int(median(x[(n // 2) + 1:])))
