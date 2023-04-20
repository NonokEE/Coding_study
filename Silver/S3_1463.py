import sys
ip = sys.stdin.readline

N = int(ip())
count = 3
table = [0, 0, 1, 1]

while count < N:
    count += 1
    candidate = [table[count-1]]
    if count % 3 == 0: candidate.append(table[int(count/3)])
    if count % 2 == 0: candidate.append(table[int(count/2)])
    table.append(min(candidate)+1)
    
print(table[N])

'''
(python 3는 1.5초 준대) (숫자 조건 없음)
정수 X에 대하여
1. X가 3으로 나눠떨어지면 3으로 나눈다.
2. X가 2로 나눠떨어지면 2로 나눈다.
3. 1을 뺀다
N이 주어졌을 때, 세 연산을 사용해서 1을 만든다. 이 때 최소 연산 횟수는?
---
DP인가?
table[n]이 n을 만드는데 필요한 최소 연산임
이걸로 다음 다음 다음 해서 N 구할때 까지 하면 됨
이게 DP였던걸로 기억

경우의 수:
N이 2로 나누어 떨어지면, table[N/2] + 1
N이 3으로 나누어 떨어지면, table[N/3] + 1
둘 다 아니면 비교해야 함
---
ㄴㄴ 매 순간마다 비교해야 함
3가지 경우 중 가능한 것들을 모두 후보로 삼고, 그 중에서 가장 작은걸 뽑으면 됨.
'''