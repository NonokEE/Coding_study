import sys
ip = sys.stdin.readline

from collections import deque

def funcD(e):
    return (e*2)%10000

def funcS(e):
    if e > 0 : 
        return e-1
    else: 
        return 9999

def int_to_deque(e):
    e = deque(str(e))
    while len(e) < 4:
        e.appendleft('0')
    return e

def funcL(e):
    e = int_to_deque(e)
    e.append(e.popleft())
    return int("".join(e))

def funcR(e):
    e = int_to_deque(e)
    e.appendleft(e.pop())
    return int("".join(e))

func_name = ['D','S','L','R']

for _ in range(int(ip())):
    a, b = map(int, ip().split())
    field = [False for _ in range(10000)] #False = 미개척지

    # BFS 초기화
    bfs_queue = deque([a])
    field[a] = ''

    # BFS 시작
    while field[b] == False:
        cur = bfs_queue.popleft()
        arr = [funcD(cur), funcS(cur), funcL(cur), funcR(cur)]

        for i in range(4):
            next = arr[i]
            func = func_name[i]

            if field[next] == False: # 미개척지인 경우에만 갱신 진행
                field[next] = field[cur] + func
                bfs_queue.append(next)
                 
    print(field[b])
''' DSLR
시간 6초 메모리 256MB

D S L R 커맨드가 있는 계산기가 있고, 레지스터는 하나임. 여기엔 0이상 10,000미만 십진수 저장 가능.
레지스터에 저장된 정수를 n이라고 할 때

D: n을 두배로. 9999초과시에는 10000으로 나눈 나머지. (2n mod 10000)
S: n-1. 0이라면 9999
L: 각 자릿수를 왼편으로 회전. 1234 -> 2341
R: 각 자릿수를 오른편으로 회전. 1234 -> 4123

서로 다른 A와 B에 대하여, A가 B가 될 수 있는 최소한의 명령어를 생성하라.
참고로 1000에서 L 하면 0001 -> 1이 되는 거임. R이었으면 0100 -> 100임

경로 여러개 있으면 아무거나 해도 됨.

- 입력 -
첫 줄에 tc개수 t
각 tc에 출발지 A랑 목적지 B

--4트--:
함수 최적화의 문제가 아닌 것 같음

--3트--: TO
BFS는 맞을텐데... 너무 무식하게 가는 감은 있음
어차피 이게 뎁스 단위로 뻗어가는거기 때문에 더 비효율적인 경우가 웬만해선 없음 -> ㄴㄴ 절대 없음. 
이미 값이 있으면 갱신할 필요가 없다 이말이다. BFS에 대한 이해도 부족이었음.
갱신 안하는 식으로 바꿔도 안되면 함수 LR에 덱 안쓰는 식으로 최적화 ㄱㄱ

--1트--: TO
그냥 내용이 복잡해서 그렇게 결국 이것도 BFS임.
일단 전처리는 전부 str로 해주는게 좋아보이고 -> 굳이?
필드 저장을 [값, 경로]로 저장하게 하자.
경로 초기값은 None이고, 커맨드를 배열로 추가하는 방식.
-> 굳이?

필드 인덱스가 곧 값인데 굳이 저럴 필요 없다.
시간 걸리면 도착지에 값 생길 때 까지만 진행.
이래도 걸리면..? 그냥 BFS가 아닌가? 시간 6초나 되는데 왜 걸리지

'''