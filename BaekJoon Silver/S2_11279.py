import sys
ip = sys.stdin.readline

import heapq

arr = []
for _ in range(int(ip())):
    x = int(ip())
    if x:
        heapq.heappush(arr, -x)
    else:
        if arr:
            print(-heapq.heappop(arr))
        else:
            print(0)



''' 최대힙
시간 1초 메모리 256MB

최대힙임 ㅅㄱ

- 입력 -
첫줄에 연산 개수 N개 1이상 10만 이하
다음부터 N개 동안 정수 x 입력. 0이면 pop 아니면 push
x는 int 범위의 자연수

--1트--: 결과
heapq는 신이야
'''