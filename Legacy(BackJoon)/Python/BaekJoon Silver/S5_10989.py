import sys
ip = sys.stdin.readline

N = int(ip())
L = [0 for i in range(10000)]

for i in range(N):
    a = int(ip())-1
    L[a]+=1

for i in range(10000):
    for j in range(L[i]):print(i+1)

'''
N개의 수가 주어졌을 때 오름차순?
아마 자바에서는 배열 길이 떄문에 이슈 생기는듯

1트 --
N = int(ip())
L = []
for i in range(N): L.append(int(ip()))
L.sort()
for i in range(N): print(L[i])
---
파이썬에서도 그냥 append로 하면 메모리 이슈가 생긴다.
'메모리'이슈, 그리고 메모리 제한 8MB. 
그냥 얘도 11723처럼 미리 배열을 만들어 놓는게 낫다.
입력되는 수가 10000보다 작거나 같은 자연수니까.
'''