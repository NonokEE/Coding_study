import sys
ip = sys.stdin.readline

N = int(ip())
nazibo = []
rank = {}

for i in range(N): 
    nazibo.append([i] + list(map(int, ip().split())))
    rank[i] = 1

nazibo.sort(key = lambda x: x[1])

for i in range(N-1):
    for j in range(i+1, N):
        if nazibo[i][2] < nazibo[j][2]: rank[nazibo[i][0]] += 1

for i in range(N): print(rank[i], end=" ")


''' 덩치
몸무게 x, 키 y라면 (x,y)로 표현.
몸무게 키 둘다 크면 확실히 덩치가 큰건데, 뭐 하나만 크면 애매함.
덩치 등수는 자신보다 더 큰 덩치의 사람+1

첫 줄에 사람 수 N
x y 들어옴.

나열된 순으로 등수를 표시.

--1트-- : 결과
그냥 for 돌리면 시간 걸리려나?
일단 몸무게 순으로 정렬하고, 몸무게 작은 사람이 키까지 작으면 +1 해주기
'''