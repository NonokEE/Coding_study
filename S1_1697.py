import sys
ip = sys.stdin.readline

N, K = map(int, input().split())

## 초기화 ##
INF = 99999999
field = [INF for _ in range(100001)]
field[N] = 0
loop = 0
visited = [N]

## 스텝 ##

while K not in visited:
    loop += 1
    temp = []
    for current in visited:
        if (current + 1 <= 100000) and (field[current+1] > loop): 
            field[current+1] = loop
            temp.append(current+1)

        if (current - 1 >= 0) and field[current-1] > loop: 
            field[current-1] = loop
            temp.append(current-1)

        if (current * 2 <= 100000) and field[current*2] > loop: 
            field[current*2] = loop
            temp.append(current*2)
    visited = list(set(temp))
print(loop)

''' 숨바꼭질
직선 안에서 숨바꼭질을 할거임.

1. 경찰은 N에서, 도둑은 K에서 시작
2. 경찰은 걷거나 순간이동을 할 수 있다. 경찰이 X에 있다고 가정할 때,
    - 걷는데 1초가 소모되고, X-1또는 X+1로 이동할 수 있다. 좌 또는 우로 한 칸 이동 가능하다는 뜻.
    - 순간이동 하는데 1초가 소모되고, 2*X로 이동하게 된다. 

첫 줄에 N과 K가 주어질 때 가장 적은 시간으로 도둑을 잡으려면 몇 초가 걸리는가

--1트-- : 메모리 초과
5 17의 예시에서,
5 10 9 18 17로 5번 이동해서 잡았다.

이게 왜 BFS 문제지?
아 설마 가능한 다음 모든 스텝을 전부 만드나..?
0초 -> N
1초 -> N-1 N+1 2N

다음 스텝으로 갈 때마다 브랜치가 3개씩 늘어나는데..? 이거 너무 무식하지 않나
근데 일단은 이게 가장 간단한 방법이니까 시도해본다.

-- 2트-- :
최적화도 아예 안해서 너무 무식하긴 했어
아무튼 이것도 최단 경로를 찾는 문제임. 시간이 넉넉하니까 플로이드 워셜이 가능할 것 같은데

모든 노드는 자기 번호 +- 1로 이동 가능
모든 노드는 자기 번호 * 2로 이동 가능

근데 플로이드 워셜 한다고 쳐도 0부터 100,000까지 다 돌려야되는데 과연 이게 효율적일까?

그냥 맵만 만들어놓고 거기서 갱신하게 하자.
이미 최적으로 들른 노드 다시 안 들르는 것 만으로도 상당히 효율적임

'''