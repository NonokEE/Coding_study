import sys
ip = sys.stdin.readline

# 입력 #
n, m = map(int, ip().split())
ladder = {}     # 뱀이든 사다리든 사실 상관 없음
for _ in range(n):
    x, y = map(int, ip().split())
    ladder[x-1] = y-1

for _ in range(m):
    u, v = map(int, ip().split())
    ladder[u-1] = v-1

# 초기화 #
INF = 99999999
field = [INF for _ in range(100)]
field[0] = 0

roll = 0
current_chamber = [0]

# BFS #
while field[99] == INF:
    roll += 1
    
    # 이번 스탭에서 가능한 다음 스탭들 찾기
    next_step = []
    for cur in current_chamber:
        for i in range(1, 7):
            if cur+i < 100: next_step.append(cur+i)
    next_step = list(set(next_step)) #중복 제거

    # 사다리타기
    temp = []
    for i in next_step:
        try:
            temp.append(ladder[i])
        except:
            temp.append(i)
    next_step = temp

    # 스탭 진행
    cand = []
    for i in next_step:
        if field[i] > roll: 
            field[i] = roll
            cand.append(i)

    current_chamber = cand

print(field[99])
    

''' 뱀사겜(뱀과 사다리 게임ㅎ)
주사위 눈을 조작할 수 있다면 최소 몇 번만에 도착할 수 있을까?
주사위는 1~6. 게임판은 10*10이고 1부터 100까지 적혀있음.

플레이어는 주사위 눈 만큼 이동, 도착번호가 100을 넘기면 도착할 수 없음. (명예로운 일격 하라는 뜻)
도착한 칸이 사다리면 타고 올라가고, 뱀이면 따라 내려감.
게임판의 상태가 주어졌을 때, 100번째 칸에 도착하기 위한 최소 횟수

- 입력 -
사다리 n과 뱀 m이 주어짐. 둘 다 1이상 15이하
n개 줄 동안 x,y 사다리
m개 줄 동안 u,v 뱀
사다리랑 뱀은 1번이랑 100번칸에 연결 안돼있음.
모든 칸은 최대 하나의 사다리나 뱀을 가질 수 있음. 사다리든 뱀이든 무조건 최대 하나만

시간 1초 메모리 512MB

--1트--: ezpz lemon sqz
BFS아니면 플로이드 워셜을 사용할 수 있을 것으로 보이는데, 맵을 어떻게 짜느냐가 중요하겠네요.
일단 1차원 맵

0. [0]을 큐에 넣고, 카운트 = 0
1. 팝 하고 카운트 += 1
   +1 ~ +6을 칸의 숫자를 확인 (이 때 사다리나 뱀이 있는지 딕셔너리로 확인)
   그 칸의 숫자들이 더 크다면 카운트로 갱신, 더 작다면 후보에서 제외
   갱신이 이루어진 칸들을 리스트로 만들어서 큐에 push

카운트를 리스트 단위로 올려야 하니까 저번에 그 경찰과 도둑이랑 유사함.

'''