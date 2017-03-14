import numpy
from numpy.linalg import inv

m, n = [int(e) for e in input().split()]
X = []
Y = []
for i in range(n):
    temp = [1]
    temp1 = [float(e) for e in input().split()]
    X.append(temp + temp1[:m])
    Y.append(temp1[m])
X = numpy.array(X)
Y = numpy.reshape(numpy.array(Y), (n, 1))

B = inv(numpy.matmul(X.transpose(), X))
B = numpy.matmul(B, X.transpose())
B = numpy.matmul(B, Y)

q = int(input())
X1 = []
for i in range(q):
    X1.append([1] + [float(e) for e in input().split()])

X1 = numpy.array(X1)
answer = numpy.matmul(X1, B)

for e in answer:
    print(round(e[0], 2))
