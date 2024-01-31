## G5 2467 용액
import sys
ip = sys.stdin.readline
##

N = int(ip())
arr = list(map(int, ip().split()))

minimum = sys.maxsize
res = [0,0]

s = 0
e = N-1

while (s < e):
    mixed = arr[s] + arr[e]
    
    if abs(mixed) < minimum:
        res[0] = s
        res[1] = e
        minimum = abs(mixed)

    if mixed == 0: break
    elif mixed > 0 : e -= 1
    elif mixed < 0 : s += 1

print(arr[res[0]], arr[res[1]])