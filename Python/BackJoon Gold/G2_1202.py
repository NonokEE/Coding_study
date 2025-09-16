## G2 1202 보석 도둑
import sys
ip = sys.stdin.readline

## 입력
import heapq
N, K = map(int, ip().split())
jewels = sorted([tuple(map(int, ip().split())) for _ in range(N)])
bags = []
for _ in range(K): heapq.heappush(bags, int(ip()))

## 그리디
res = 0
candidate = []

jewel_index = 0
while bags:
    bag = heapq.heappop(bags)
    while (jewel_index < N) and (jewels[jewel_index][0] <= bag):
        heapq.heappush(candidate, -jewels[jewel_index][1])
        jewel_index += 1
    if candidate: res -= heapq.heappop(candidate)

print(res)