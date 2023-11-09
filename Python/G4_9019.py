import sys
ip = sys.stdin.readline

from collections import deque

def funcD(e):
    return (e*2)%10000

def funcS(e):
    return (e-1)%10000

def funcL(e):
    head = e//1000
    body = e%1000
    return body*10 + head

def funcR(e):
    front = e//10
    tail = e%10
    return tail*1000 + front

func_name = ['D','S','L','R']

for _ in range(int(ip())):
    a, b = map(int, ip().split())
    visited = [False for _ in range(10000)] #False = 미개척지

    # BFS 초기화
    bfs_queue = deque([[a, ""]])
    visited[a] = True

    # BFS 시작
    while bfs_queue:
        cur, path = bfs_queue.popleft()
        arr = [funcD(cur), funcS(cur), funcL(cur), funcR(cur)]

        if cur == b:
            print(path)
            break

        for i in range(4):
            next = arr[i]
            func = func_name[i]

            if visited[next] == False: # 미개척지인 경우에만 갱신 진행
                visited[next] = True
                bfs_queue.append([next, path + func])
                 
                 
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

--6트--: 아니 내가 맞았어 이건 억까야
결과 횟수가 중요한게 아니고, 과정이 중요한 거니까 필드를 남기지 말라 이거지?
네... 
필드 없어도 되긴 하는구나. 필드 매번 초기화해주고 접근하느라 시간 남는 것 같기도.
사실 필드가 너무 넓어서 빈땅이 너무 많으니까 낭비긴 해. 그냥 빈 땅에 줄 그으면서 간다고 생각하는게 낫나보다.

! list에서 in은 O(n)인데, set에서 in은 O(1)이란다. 개신기하네. 딕셔너리로 구현되나?

--5트--: TO
너무 넓어... 어떻게 최적화하지
BFS가 아닌거 아니야? 아 설마 진짜로 LR때문에 문제가 생기는 거라고? 근데 그럴만 하긴 해..

--4트--: TO
함수 최적화의 문제가 아닌 것 같음.
완전 열린 필드라서 쓸데없는 수를 너무 많이 두는게 문제인데
경찰과 도둑이랑 비슷한 문제라고 봤는데..
뎁스 뭉탱이로 보자. 한 뎁스 안에서 중복되는 경우가 생겨서 비효율적인 수가 생길 수 있음.
큐를 안쓰고 loop 단위로 보면 됨

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