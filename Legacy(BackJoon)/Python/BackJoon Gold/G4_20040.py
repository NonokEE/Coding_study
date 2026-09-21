## G4 20040 사이클 게임
import sys
ip = sys.stdin.readline

##
n, m = map(int, ip().split())

parent = [i for i in range(n)]
rank = [1] * n

def find(x):
    origin = x
    while x != parent[x]:
        x = parent[x]
    parent[origin] = x
    return x

for turn in range(m):
    a, b = map(int, ip().split())

    loot_a = find(a)
    loot_b = find(b)

    if loot_a == loot_b:
        print(turn+1)
        break
    else:
        if parent[a] < parent[b]: parent[parent[a]] = parent[b]
        else                    : parent[parent[b]] = parent[a]
else:
    print(0)
