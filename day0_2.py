def weighted_mean(x, w):
    arr = zip(x, w)
    return sum([e[0] * e[1] for e in arr]) / sum(w)


int(input())
x = [int(e) for e in input().split()]
w = [int(e) for e in input().split()]
print(round(weighted_mean(x, w), 1))
