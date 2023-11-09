import sys
ip = sys.stdin.readline

k, n = map(int, ip().split())
cables = [int(ip()) for _ in range(k)]

def cut(cables:list, cm:int):
    count = 0
    for cable in cables: count+=cable//cm
    return count

start = 1
end = max(cables)

while start <= end: 
    mid = (start + end)//2
    count = cut(cables, mid)
    if   count >= n: start = mid+1
    elif count <  n: end   = mid-1

print(end)


''' 랜선 자르기
길이가 각각인 K개의 랜선이 있음.
모두 같은 길이의 N개의 랜선을 만들고 싶음 (N개 이상 만들어도 N개로 인정) <- 더 많이 잘라도 된다는 부분이 걸리는데...
N개의 랜선을 만들 수 있는 최대 길이를 구하셈.

첫줄에 가지고 있는 랜선 개수 K, 필요한 랜선 개수 N (K <=N )
다음 줄 부터 가지고 있던 랜선의 길이

--1트-- : 시간초과
다시 시도합니다 허허
이게 바이너리 서치라고요? 어떤 부분에서 바이너리 서치일까

일단 최소 K개니까, K개가 될 수 있는 가장 긴 길이(가지고 있던 랜선 중 가장 짧은 것의 길이)
~
필요한 N개의 랜선을 만들 수 있는 가장 작은 길이(이걸 알 수 있으면 고생 안했죠?)

개수를 하나 늘리는 가장 좋은 방법은 가장 긴걸 반토막내는 것.
그 다음 늘리려면 그 다음 긴걸 반토막(그러면 어차피 가장 긴 것도 반토막 이상은 난다) or 가장 길었던걸 3토막
이런식으로 점진적으로 토막 수 늘릴 수 있긴 해

방법1. 1 ~ 가장 짧은 것으로 이분탐색
방법2. 스마트하게 한토막 한토막

일단은 2번 방법 생각하기 귀찮으니까 1번으로 가보죠

--2트--: 

'''