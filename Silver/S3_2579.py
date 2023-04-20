import sys
ip = sys.stdin.readline

N = int(ip())
score = [int(ip()) for _ in range(N)]
table = [[0, True], [score[0], True]]         # True인 경우 다음 계단 밟기 가능, False인 경우 다음 계단 밟기 불가능.
if N >= 2: table.append([score[0] + score[1], False])
level = 2

while level < N:
    level += 1
    candidate = [[table[level-3][0] + score[level-2] + score[level-1], False],
                 [table[level-2][0] + score[level-1], True]]

    if table[level-3][1]: candidate.append([table[level-3][0] + score[level-3] + score[level-1], True])

    table.append(max(candidate, key=lambda x:x[0]))

print(table[N][0])
'''
계단을 밟으면 그 계단에 쓰여 있는 점수를 얻게 된다.
계단 중간에 건너뛰면 점수 못 얻는다.

규칙
1. 계단은 한 번에 하나 혹은 두 개씩만 오를 수 있다.
2. 연속 세 개는 밟으면 안된다.
3. 마지막은 반드시 밟아야 한다.

각 계단의 점수가 주어질 때, 게임에서 얻을 수 있는 점수의 최댓값은?
--1트--
이것도 DP 문제.
DP의 기본 원리가 분할 정복임을 생각하자.
DP Table에 계단 0개 일때, 1개 일때 등등 최댓값을 입력하고
뒤에 점화식 넣어서 어캐어캐 한다.

1개 일 때는 0개일 때 + 내 점수
2개 일 때는? 1개일 때 + 내 점수 or 0개일 때 + 내 점수
3개 일 때는? 2개일 때 + 내 점수 or 1개일 때 + 내 점수

그런데 3개의 경우의 계산에서 2개 + 내 점수를 보자.
2개 최댓값의 경우가 연속 밟음일 때는 1개 + 내 점수를 선택할 수 없다.
연속 밟음 상태를 알 수 있도록 값이 저장되어야 한다.

--2트--
첫 계단 무조건 밟아야 한다고는 안했다. 
3
10
20
15
인 경우에는, 10 15 -> 25보다
첫 계단 건너뛰고 20 15 -> 35가 더 높다.

규칙을 다시 세워야 함.
max 뽑아내는 집합은?

n층 까지 가는 방법
1. n-3, n-1, n -> n-3 여부에 관계없이 가능. 이후 False
2.      n-2, n -> n-2 여부에 관계없이 가능. 이후 True
3. n-3, n-2, n -> n-3이 True 인 경우에만 가능. 이후 True

'''