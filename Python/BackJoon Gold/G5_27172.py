## G5 27172 수 나누기 게임
import sys
ip = sys.stdin.readline

## 입력
N = int(ip())
cards = list(map(int, ip().split()))


## 초기화
res = {card:0 for card in cards}
cards.sort()
maxnum = cards[-1]

## 리그 진행
for c in cards:
    for t in range(c * 2, maxnum+1, c):
        if t in res:
            res[c] += 1
            res[t] -= 1

## 결과 출력
print(*res.values())