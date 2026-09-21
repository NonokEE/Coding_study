import sys
ip = sys.stdin.readline

import itertools

for _ in range(int(ip())):
    N = int(ip())
    mbtis = ip().split()

    if N > 32: 
        print(0)

    else:
        minval = sys.maxsize
        for x,y,z in set(itertools.combinations(mbtis, 3)):
            score = 0
            for i in range(4):
                if x[i] != y[i]: score += 1
                if y[i] != z[i]: score += 1
                if z[i] != x[i]: score += 1

            minval = min(minval, score)

        print(minval)


''' 가장 가까운 세 사람의 심리적 거리
시간 2초 메모리 1536MB

알파벳 다른 개수만큼 1점.
사람 세명 있을 때, 세명 점수 합친게 세명의 심리적 거리.
최솟값 구하라

- 입력 -
첫 줄에 TC개수 T (1이상 50이하)
각 TC마다
학생수 N (3이상 100,000이하)
MBTI가 공백을 두고 주어짐.

- 출력-
TC별 답

--1트--: 결과
결국엔 무슨 정해진 알고리즘은 없는 문젠데, 전체를 브루트포스 하는건 진짜 개 멍청한 방법임.
최소점은 0점, 만점은 8점.

비둘기집?
N칸이 있고 N보다 많은 마리수가 있다면 2마리 이상 들어가는 칸이 하나 이상 있다.

이걸 시바 그냥 브루트포스 돌려야돼?
그냥 돌려도 되긴 한데, 비둘기집을 응용
칸이 16개니까, 사람이 16명보다 많으면 같은 mbti를 가진 사람이 2명인게 보장됨.
따라서 32명보다 많으면 같은 mbti를 가진 3명이 반드시 존재하므로 거리가 0인것도 보장됨.

'''