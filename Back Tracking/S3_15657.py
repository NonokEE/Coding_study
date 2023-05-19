import sys
ip = sys.stdin.readline

N, M = map(int, ip().split())
nums = sorted(list(map(int, ip().split())))

def DFS(seq: list):
    if len(seq) == M:
        print(*seq)
        return

    for i in nums:
        if (len(seq) == 0) or (seq[-1] <= i):
            seq.append(i)
            DFS(seq)
            seq.pop()
DFS([])

''' N과 M(8)
시간 1초 메모리 NNNMB

N개의 서로 다른 자연수 중 M개를 고른 수열
같은 수 여러 번 골라도 됨
비내림차순

- 입력 -
첫 줄에 N과 M
둘째줄에 N개의 수

- 출력-
늘 그렇듯

--1트--: 결과
똑같은데 중복 허용되고 무작위 수

'''