## G4 9663 N-Quuen
import sys
ip = sys.stdin.readline

N = int(ip())
row = [0] * N
res = 0

def chk(num):
    for ind in range(num):
        if (row[num] == row[ind]) or (abs(row[num] - row[ind]) == num-ind):
            return False
    return True

def dfs(next):
    global res

    if next == N: 
        res += 1
    else:
        for i in range(N):
            row[next] = i
            if chk(next): dfs(next+1)

dfs(0)
print(res)