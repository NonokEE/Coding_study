import sys
ip = sys.stdin.readline

M = int(ip())
S = [0 for i in range(20)]

for i in range(M):
    op = ip()

    if "add" in op: 
        n = int(op.split()[1])-1
        S[n] = 1

    elif "remove" in op: 
        n = int(op.split()[1])-1
        S[n] = 0
        
    elif "check" in op: 
        n = int(op.split()[1])-1
        print(S[n])

    elif "toggle" in op: 
        n = int(op.split()[1])-1
        if S[n]: S[n] = 0
        else: S[n] = 1

    elif "all" in op: 
        for j in range(20): S[j] = 1

    elif "empty" in op: 
        for j in range(20): S[j] = 0

'''
공집합 S가 주어짐. 
add x: S에 x를 추가. 이미 있는 경우 무시.
remove x: S에서 x를 제거. 없는 경우 무시.
check x: S에 x가 있으면1, 없으면 0 출력
toggle x:S에 x가 있으면 제거, 없으면 추가.
all: S를 0~20의 숫자 배열로 바꿈
empty: S를 비움

첫 줄에 연산의 횟수 M 입력,
둘째 줄부터 연산 한 줄 씩 입력
---
범위를 잘 보는 습관을 들이자
x가 1이상 20이하 밖에 안되고, 각 셀의 데이터는 0 아님 1, 바이너리임.
그냥 20칸짜리 배열 만드는게 더 쉽다는 것.

이렇게 안하고 무식하게 하면 매 연산마다 소트 돌려야해서 시간이 오래 걸릴 것임.
'''