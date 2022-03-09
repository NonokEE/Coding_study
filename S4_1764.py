import sys
ip = sys.stdin.readline

N, M = map(int, ip().split())
listenman = []
listenlook = []

for i in range(N): listenman.append(str(ip().strip()))
for i in range(M):
    lookman = str(ip().strip())
    if lookman in listenman: listenlook.append(lookman)

listenlook.sort()
print(len(listenlook))
for i in range(len(listenlook)): print(listenlook[i])


'''
첫 줄에 듣도 못한 사람 N, 보도 못한 사람 M이 한번에 주어짐.
이름은 띄어쓰기 없이 알파벳 소문자, 길이 20 이하. N, M <= 500,000
N과 M 중에 중복 없음.

N과 M에 둘 다 들어가는 사람 수랑 명단을 사전순으로 출력.

--1트--
N은 그냥 받으면 되고, M 추가될 때 마다 N에서 탐색하면 되는 것 같다.
받는게 사전순이 아님에 유의

방법1. 그냥 in으로 찾아보기. 근데 시간 제한에 걸리겠지?
방법2. N을 사전순으로 정렬하고, 퀵소트 구현해서 해보기

일단 귀찮으니까 방법 1부터 시도.

'''