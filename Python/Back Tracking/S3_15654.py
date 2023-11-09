import sys
ip = sys.stdin.readline

N, M = map(int, ip().split())
nums = sorted(list(map(int, ip().split())))

from itertools import permutations

for line in permutations(nums, M):
    print(*line)

''' N과 M(5)
시간 1초 메모리 512MB

N과 M을 줄건데요,
N개의 자연수 중에서 M개를 고른 수열을 출력하세요.

- 입력 -
첫줄에 N, M
둘째줄에 N개의 자연수

- 출력-
순열 출력하되 오름차순으로

--1트--: 결과
이건 사실 백트래킹으로도 할 수야는 있지만 순열에 더 가까운 것 같긴 하다.
한번 써보지 뭐.

itertools에 들어있는 permutations랑 combinations는 (뽑을 조합, 뽑을 개수) 받아서 이터레이션으로 반환한다.
내용물들은 튜플
'''