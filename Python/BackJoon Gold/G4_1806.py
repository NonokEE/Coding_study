## G4 1806 부분합
import sys
ip = sys.stdin.readline

## 입력
N, S = map(int, ip().split())
seq = list(map(int, ip().split()))

##
prefix = [0] * (N+1)
prefix[1] = seq[0]
for i in range(2, N+1): prefix[i] = prefix[i-1] + seq[i-1]

res = sys.maxsize
front, rear = 1, 0

while front < N+1:
    subtotal = prefix[front] - prefix[rear]

    if subtotal >= S:
        res = min(res, front - rear)
        rear += 1
    else:
        front += 1

## 출력
if res == sys.maxsize: res = 0
print(res)