## G5 2166 다각형의 면적
import sys
ip = sys.stdin.readline
##
N = int(ip())
points = []

for _ in range(N): points.append(tuple(map(int,ip().split())))
points.append(points[0])

xval, yval = 0, 0
for i in range(N):
    xval += points[i][0] * points[i+1][1]
    yval += points[i][1] * points[i+1][0]

print(round(abs(xval - yval)/2, 1))