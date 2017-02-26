def mean(arr):
    return float(sum(arr) / len(arr))


def median(arr):
    arr = sorted(arr)
    if len(arr) % 2 == 0:
        temp = arr[(len(arr) // 2) - 1]
        return (temp + arr[(len(arr) // 2)]) / 2


def mode(arr):
    from collections import Counter
    count = dict(Counter(arr))
    max_count = max(count.values())
    return min([k for k, v in count.items() if v == max_count])


int(input())
arr = [int(e) for e in input().split()]
print(round(mean(arr), 1))
print(round(median(arr), 1))
print(round(mode(arr), 1))
