import sys
ip = sys.stdin.readline

A, B = map(int, ip().split())

from collections import deque
def BFS(a,b):
    q = deque([(A, 0)])

    while q:
        cur, count = q.popleft()

        if cur == b:
            return count + 1

        # *2
        num = cur*2
        if num <= b:
            q.append((num, count+1))

        # append1
        num = int(str(cur) + "1")
        if num <= b:
            q.append((num, count+1))
    
    return -1

print(BFS(A,B))

''' A -> B
시간 2초 메모리 512MB

정수 A를 B로 바꿀거다.
2를 곱하거나, 가장 오른쪽에 1을 추가할 수 있다.

- 입력 -
첫 줄에 A, B (1이상 10^9이하, A는 반드시 B보다 작다.)

- 출력-
필요한 연산의 최솟값에 1을 더한 값을 출력.
만들 수 없으면 -1 출력

--1트--: 결과
BFS긴 한데 작아지는 경우는 생각 안해줘도 됨.
'''