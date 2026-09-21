import sys
ip = sys.stdin.readline

N, M = map(int, ip().split())
nums = sorted(list(map(int, ip().split())))

visited = set([])
from itertools import permutations

for line in permutations(nums, M):
    if line not in visited:
        print(*line)
        visited.add(line)

''' N과 M(9)
시간 1초 메모리 512MB

N개의 자연수 중에서 M개를 고른 수열

- 입력 -
첫 줄에 N M
둘째줄에 N개의 자연수

- 출력-
오름차순 출력, 중복 출력은 안돼요

--1트--: 클
숫자 중복이 있다. 숫자를 여러번 쓰는건 되는데, 중복 출력은 하면 안된다. 쪼끔 까다롭긴 했나봐?
permutations로 해결 안되나? 않돼내

수열 자체의 중복을 검사해야하는데, set으로 해결하면 되는 일 아닌지? O(1)이라매.
오 확실히 list로 하면 안되네 키야
'''