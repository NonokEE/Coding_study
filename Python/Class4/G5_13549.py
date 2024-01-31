import sys
ip = sys.stdin.readline

from collections import deque

N, K = map(int, ip().split());

if N >= K: print(int(N-K))
else:
    INF = 100001
    field = [INF] * 100001
    field[N] = 0
    queue = deque([N])

    def IsInField(num):
        return 0 <= num < INF

    while queue:
        cur = queue.popleft()

        #chk
        if cur == K:
            print(field[K])
            quit()

        #teleport
        tele = cur * 2
        while IsInField(tele) and (field[tele] > field[cur]):            
            field[tele] = field[cur]
            queue.appendleft(tele)
            tele = tele * 2

        #step
        if IsInField(cur+1) and (field[cur+1] > field[cur]):
            field[cur+1] = field[cur] + 1
            queue.append(cur+1)

        if IsInField(cur-1) and (field[cur-1] > field[cur]):
            field[cur-1] = field[cur] + 1
            queue.append(cur-1)
