import sys
ip = sys.stdin.readline

N = int(ip())
paper = [list(map(int, ip().split())) for _ in range(N)]

def chk(sx, sy, ex,ey):
    factor = paper[sx][sy]
    flag = True
    for x in range(sx, ex):
        for y in range(sy, ey):
            if paper[x][y] != factor:
                flag = False
                break
        if not flag:
            break
    if flag:
        return factor
    else:
        return "No"

ans = {-1:0, 0:0, 1:0}

def recursion(sx, sy, ex, ey):
    l = ex - sx
    if l == 1:
        ans[paper[sx][sy]] += 1
        return
    else:
        c = chk(sx, sy, ex ,ey)
        if type(c) == type(0):
            ans[c] += 1
        else:
            t = [0, l//3, 2*l//3, l]

            for i in range(3):
                for j in range(3):
                    recursion(t[i]+sx, t[j]+sy, t[i+1]+sx, t[j+1]+sy)

e = len(paper)
recursion(0,0, e,e)
for e in ans.values(): 
    print(e)


''' 종이의 개수
시간 2초 메모리 256MB

N짜리 정사각형 종이가 있다. 각 칸에는 -1 0 1중 하나가 있음.

1. 모두 같은 수라면 그대로 사용
2. 아니라면 9등분해서 반복

- 입력 -
첫줄에 N. (1이상 3^7이하, 3^k 꼴)
다음에 종이 정보

- 출력-
-1 개수
0 개수
1 개수

--1트--: 결과
그냥 재귀 문제. 자르기가 귀찮네요.
'''