import sys
ip = sys.stdin.readline

N, M = map(int, ip().split())

def DFS(seq: list):
    if len(seq) == M:
        print(*seq)
        return

    for i in range(1, N+1):
        if (len(seq) == 0) or (seq[-1] <= i):
            seq.append(i)
            DFS(seq)
            seq.pop()
DFS([])

''' N과 M (4)
시간 1초 메모리 512MB

자연수 N과 M 줄게
* 1부터 N까지 M개를 고른 수열
* 같은 수 여러번 골라도 됨
* 수열은 비내림차순이어야 함
    + A1 <= A2 <= A3 <= ... <= AK
    + 숫자가 작아지지만 않으면 된다.

- 입력 -
첫 줄에 N, M
N >= M이고 둘 다 1이상 8이하

- 출력-
한 줄에 수열 하나씩 출력. 수열의 수는 공백 하나로 구분

--1트--: 결과
그냥 똑같은 문제 아님 거의? 이번엔 직접 해봅시다.
'''