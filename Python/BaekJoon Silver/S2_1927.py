import sys
ip = sys.stdin.readline
import heapq

heap = []
for _ in range(int(ip())):
    x = int(ip())
    if x:
        heapq.heappush(heap, x)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)


''' 최소힙
민힙 구현하는 문제
첫 줄에 연산 개수 N, 1이상 100,000이하
N개 줄 동안 연산 정보 x
x가 자연수라면 배열에 x 추가
0이라면 가장 작은 값 출력하고 제거(배열 비어있으면 0 출력)
x < 2^31
음수는 입력 안들어옴

- 입력 -

시간 1초 메모리 128MB

--1트--: heapq를 알려주셔서 감사합니다... 7662센세...
이걸 절댓값 힙보다 먼저 했어야됐네 ㅋㅋ
어차피 구현도 해봤고, 라이브러리도 있는거 아니까 그냥 라이브러리로 합시다. 라이브러리 연습도 할겸
'''