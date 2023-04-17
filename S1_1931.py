import sys
ip = sys.stdin.readline

n = int(ip())
meetings = [list(map(int, ip().split())) for _ in range(n)]

count = 0
latest_e = 0
meetings.sort(key=lambda x:(x[1], x[0]))


while meetings:
    cur_s, cur_e = meetings.pop(0)
    if latest_e > cur_s: continue
    else               : 
        count += 1
        latest_e = cur_e

print(count)

''' 회의실 배정
한 개의 회의실이 있고, 이를 사용하려는 N개의 회의에 대한 시간표를 만들거에요.
각 회의 I에 대해 끝나는 시간이 주어져있다. 각 회의가 겹치지 않게 회의실을 사용할 수 있느 회의의 최대 가수를 구하라.
회의는 중간에 중단될 수  없고, 한 회의가 끝나는 동시에 다음 회의를 시작할 수 있다.
시작하자 마자 끝나는 경우도 가능하다.

-입력-
첫 줄에 회의의 수 N
둘째 줄부터 회의의 정보 -> 시작시간 끝시간 (시작시간과 끝시간은 2^31보다 작거나 같은 자연수 또는 0)

--1트-- : 이게 왜 되지
시간 안겹치는 선에서 최대한 많이 쑤셔넣으라는 말인데,
어떤 것을 넣어주는게 좋을까?

1. 0초부터 되는대로 다 넣기(물론 가능한 짧은 것)
2. 가장 짧은 것부터 되는대로 넣기

DP로 할 문제는 아닌거같고, 단순 구현? 아니면 그리디?
예전에 가방에 물건 쑤셔넣는 문제 생각하면 그리디가 맞는 것 같음.
가방에 많이 넣어야되니까, 회의 진행 시간이 짧은 것, 빨리 끝나는 것들을 넣어주는게 맞다.
'''