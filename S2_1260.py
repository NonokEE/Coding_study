import sys
ip = sys.stdin.readline

N, M, V = map(int, ip().split())
adj_list = {}
for i in range(N): adj_list[i+1] = []

for _ in range(M):
    s, e = map(int, ip().split())
    adj_list[s].append(e)
    adj_list[e].append(s)

for key in adj_list: adj_list[key] = list(set(adj_list[key]))

#DFS
visited = []
stk = [V]

while stk:
    cur = stk.pop()
    visited.append(cur)
    
    for vertex in adj_list[cur]:
        if vertex not in visited + stk: 
            stk.append(vertex)
            break
        
for i in range(len(visited)-1): print(visited[i], end=" ")
print()

#BFS
visited = []
q = [V]

while q:
    cur = q.pop(0)
    visited.append(cur)

    for vertex in adj_list[cur]:
        if vertex not in visited + q:
            q.append(vertex)

for i in range(len(visited)-1): print(visited[i], end=" ")



''' DFS와 BFS
그래프 줄 테니까 DFS랑 BFS순으로 탐색한 것을 출력해라.
방문할 수 있는 vertex가 여러 개인 경우, 번호가 작은 것을 먼저 방문한다.

첫째 줄에 정점 개수 N(1<=N<=1,000), 간선의 개수 M(1<=M<=10,000), 탐색을 시작하는 정점의 번호 V 주어짐.
다음 M개줄에 엣지 정보.
두 정점 사이에 여러 edge가 있을 수 있고, 입력되는 간선은 양방향이다.

첫째 줄에 DFS 순서대로 출력, 둘째 줄에 BFS 순서대로 출력.

--1트-- : 틀림
인접 리스트(딕셔너리)를 만들자. 이 때 양방향 추가, 중복 제거, 결과배열 정렬 해줘야 함. -> set으로 해결.
재귀 돌리면 터진다는걸 알았으니까

DFS -> 스택
BFS -> 큐
로 구현.

!! 파이썬에 set이라는게 있다. 중복 허용 안하고, [순서가 없기 떄문에 = index가 없기 때문에] 기본적으로 정렬된 상태. 
   집합 연산할 때 쓰는 것. &(.intersection), |(.union), -(.difference)같은 연산을 지원함.
   add, update로 추가하고, remove로 제거.
   인덱싱이 안되기 때문에 다시 리스트로 바꿔서 써야 한다.
   리스트에서 중복 제거 및 정렬을 하고 싶으면 set으로 바꿨다가 다시 list로 바꿔주면 굿.

--2트-- : 틀림
구현이 잘못됨.

--3트-- : 
졸려
'''