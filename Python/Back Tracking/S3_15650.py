import sys
ip = sys.stdin.readline

N, M = map(int, ip().split())

def DFS(seq: list):
    if len(seq) == M:
        print(*seq)
        return
    
    for i in range(1, N+1):
        if (i not in seq) and ((len(seq) == 0) or (seq[-1] < i)):
            seq.append(i)
            DFS(seq)
            seq.pop()

DFS([])

''' N과 M(2)
시간 1초 메모리 512MB

N과 M을 준다.
1부터 N까지 중복없이 M개를 오름차순으로 고른 수열을
오름차순으로 출력하세요

- 입력 -
첫 줄에 N M

- 출력-
한 줄에 수열 하나씩 출력. 수열의 수는 공백 하나로 구분

--1트--: 공부함
모든 경우의 수를 전부 고려한다는 점에서 BF랑 비슷하다. 자료구조를 트리로 나타낼 수 있을 때 적합하대.
기본적으로 탐색 알고리즘의 응용이다. BFS를 써도 되고 DFS를 써도 된다. 생각없이 짤 수 있다는데?

모든 경우의 수를 전부 다 고려해야하면 DFS가 낫다고 합니다. BFS로 하면 큐가 너무 커지는데 속도는 똑같대요.
단, 트리의 깊이가 무한대라면(루프가 발생하는 미로라든지) DFS로 해결이 불가능하니까 BFS를 써야 함

결론은 그냥 DFS를 쓰되, 재귀로 해결하면 된다는 얘기.

'''