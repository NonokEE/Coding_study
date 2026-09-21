import sys
ip = sys.stdin.readline

N, M = map(int, ip().split())
nums = sorted(list(map(int, ip().split())))
visited = set([])

def DFS(seq: list):
    if len(seq) == M:
        temp = tuple(seq)
        if temp not in visited:
            print(*temp)
            visited.add(temp)
        return

    for i in nums:
        if (len(seq) == 0) or (seq[-1] <= i):
            seq.append(i)
            DFS(seq)
            seq.pop()
DFS([])

''' N과 M(12)
시간 2초 메모리 512MB

N개중에 M개 고른 수열
같은 수 여러번 골라도 됨
비내림차순

- 입력 -
똑같음

- 출력-
중복 허용안하는거만 빼면 똑같음

--1트--: 결과
1트 시도 내용 및 메모
'''