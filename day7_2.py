n = int(input())
x = [float(e) for e in input().split()]
y = [float(e) for e in input().split()]


rank_x = dict((x1, i + 1) for i, x1 in enumerate(sorted(set(x))))
rank_y = dict((x1, i + 1) for i, x1 in enumerate(sorted(set(y))))

x_rank = [rank_x[e] for e in x]
y_rank = [rank_y[e] for e in y]

d = [(x_rank[i] - y_rank[i]) ** 2 for i in range(n)]
rxy = 1 - ((6) * sum(d)) / (n * (n * n - 1))

print(round(rxy, 3))
