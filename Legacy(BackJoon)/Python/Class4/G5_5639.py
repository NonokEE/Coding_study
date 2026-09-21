import sys
ip = sys.stdin.readline
sys.setrecursionlimit(100000)

prefix = []
while True:
    try: prefix.append(int(ip()))
    except: break

def postfix(head, e):
    #재귀 종결 조건
    if head > e:
        return
    
    # 트리 분석 및 절단점 확인
    cut = e + 1 #일부러 종결조건으로 초기화, 아래 루프에서 절단점 못찾으면 재귀 종료
    for i in range(head+1, e+1):
        if prefix[head] < prefix[i]: #헤드보다 커지는 부분부터 r sub tree
            cut = i
            break

    # postfix순회
    postfix(head+1, cut-1) #l sub tree 순회
    postfix(cut, e)        #r sub tree 순회
    print(prefix[head])            #postfix출력

postfix(0, len(prefix)-1)

''' 이진 검색트리
시간 1초 메모리 256MB

이진 검색 트리란? 왼쪽은 작고 오른쪽은 커야 됨
프리픽스 줄테니까 포스트픽스로 출력하세요.

- 입력 -
개수 안정해주고, 프리픽스 순회 결과 입력

- 출력-
포스트 픽스 한 줄에 하나씩

--2트--:
재귀에러인가? 아 RecursionError 써져있구나 ㅎㅎ
노드 수가 만개 이하래니까 재귀 2만개는 해줘야됨

--1트--: 런타임 에러?
그래프 탐색이긴 한데 탐색 이론은 아니고 순회 방법임
재귀로 어떻게 하지 이거
'''