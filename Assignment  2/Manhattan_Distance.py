# Set A-4).Write a python program to compute sum of Manhattan distance between all pairs of points.

import sys
def MaxDist(A, N):
    maximum = - sys.maxsize
    for i in range(N):
        sum = 0
        for j in range(i + 1, N):
            Sum = (abs(A[i][0] - A[j][0]) + abs(A[i][1] - A[j][1]))
            maximum = max(maximum, Sum)
    print(maximum)
N = 3
A = [[1, 2], [2, 3], [3, 4]]
MaxDist(A, N)
