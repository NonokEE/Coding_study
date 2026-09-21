import sys
ip = sys.stdin.readline

N, M = map(int, ip().split())
field = [list(map(int, ip().split())) for _ in range(N)]

#누적합 표 초기화
#prefix[x][y] = 0,0 ~ x,y의 합
prefix = [[0]*N for _ in range(N)]
for x in range(N):
    for y in range(N):
        prefix[x][y] = field[x][y]

for line in prefix:
    for y in range(1,N):
        line[y] += line[y-1]

for x in range(1,N):
    for y in range(N):
        prefix[x][y] += prefix[x-1][y]

for _ in range(M):
    x1, y1, x2, y2 = map(int, ip().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1

    res = prefix[x2][y2]
    flag = 0

    if x1 > 0:
        res -= prefix[x1-1][y2]
        flag += 1
    if y1 > 0:
        res -= prefix[x2][y1-1]
        flag += 1
    if flag == 2:
        res += prefix[x1-1][y1-1]

    print(res)


''' 구간 합 구하기 5
시간 1초 메모리 256MB

N짜리 정사각형 표가 있다. x1y1부터 x2y2까지 합을 구하는 프로그램을 작성하시오.
(x1y1과 x2y2를 양 끝으로하는 직사각형 범위의 합을 구하라는 문제임.)

- 입력 -
첫줄에 표 크기N, 합을 구해야하는 횟수 M (N은 1이상 1024이하, M은 1이상 100,000이하)
그 다음 N개동안 표 내용 (표 안의 수는 1,000이하 자연수)
그 다음 M개동안 x1 y1 x2 y2

- 출력-
각 회차별 답 출력

--1트--: 결과
DP, 누적합 문제
행별로 누적합? 그거만으로 될 정도로 간단?
누적합표의 정의를 00부터 그 칸까지의 답으로 정해둔다.
식 어떻게든 나옴.

'''