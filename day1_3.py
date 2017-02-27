def mean(arr):
    return float(sum(arr) / len(arr))


def sd(x):
    mu = mean(x)
    temp = round(float(sum([(e - mu) ** 2 for e in x])), 1)
    temp = temp / len(x)
    return round(temp ** 0.5, 1)


n = int(input())
x = [int(e) for e in input().split()]
print(sd(x))
