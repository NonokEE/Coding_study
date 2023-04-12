import sys
ip = sys.stdin.readline

N, K = map(int, input().split())

## 초기화 ##
next_node = [N]
loop = 0

## 스텝 ##
while K not in next_node:
    temp = []
    for i in range(len(next_node)):
        temp.append(next_node[i]-1)
        temp.append(next_node[i]+1)
        temp.append(next_node[i]*2)
    next_node = list(set(temp))
    loop += 1   

print(loop)