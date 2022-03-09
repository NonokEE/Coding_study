import sys
ip = sys.stdin.readline

N, M = map(int, ip().split())
listenman = []
listenlook = []

def quicksort(l):
    if len(l) <= 1: return l
    pivot = l[len(l)//2]
    lt, gt = [], []
    for item in l:
        if   item < pivot: lt.append(item)
        elif item > pivot: gt.append(item)
    return quicksort(lt) + [pivot] + quicksort(gt)

def binsearch(t, l, s, e):
    if s > e: return None
    m = (s+e)//2
    if t == l[m]: return m
    if t > l[m]: return binsearch(t, l, m+1, e)
    elif t < l[m]: return binsearch(t, l, s, m-1)

for i in range(N): listenman.append(str(ip().strip()))
listenman = quicksort(listenman)

for i in range(M):
    lookman = str(ip().strip())
    if lookman in listenman: listenlook.append(lookman)

listenlook = quicksort(listenlook)
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
방법2. N을 사전순으로 정렬하고, 이진 탐색 구현해서 해보기

일단 귀찮으니까 방법 1부터 시도.

--2트--
네 당연히 시간 제한 걸리구연
이진 탐색 구현해서 합시다.
만약 이거 안되면 소트도 퀵소트로. 근데 파이썬 소트도 괜찮지 않나?

--3트--
이게 시간 초과하네
퀵소트까지 해보고 안되면 방법적인 문제.

'''