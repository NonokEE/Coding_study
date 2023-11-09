import sys
ip = sys.stdin.readline

def matprint(arr):
    for i in range(len(arr)):
        print(arr[i], end="\n")

### 입력 및 초기화
N= int(ip())
field = []

for i in range(N):
    temp = (ip().strip())
    t = []
    for i in range(N):
        if temp[i] == "B": t.append(0)
        else: t.append(1)
    field.append(t)

transpose = [[0 for _ in range(N)] for _ in range(N)] 
for i in range(N):
    for j in range(N):
        transpose[j][i] = field[i][j]

### 알고리즘



''' 리버스 게임
1. 가위바위보
2. 승자는 양면이 검흰인 돌을 아무렇게나 꽉차게 깔아둠.
3. 패자는 바둑돌을 뒤집는데, 그 때마다 해당 열이나 행의 모든 바둑돌을 뒤집음. (열 '이나' 행. 둘 중 하나만 선택.)
4. 원하는 만큼 뒤집기를 해서, 흰 바둑돌이 최소가 되도록 해라.

길이 N의 정사각형 배열에 바둑돌 배치가 주어질 때, 
흰 바둑돌이 최소가 되도록 하면 몇 개 까지 될 수 있는가.
뒤집는 횟수 상관 x

"
일단 검은 돌은 0, 흰 돌은 1로 바꿈.

1이 0보다 많은 행을 뒤집으면 손해임. 
1이 0보다 적거나 같은 행을 뒤집어야 본전이거나 그 이상.

1. 1이 가장 많은 곳을 찾는다.
2. 더 많아질 것 같으면 안뒤집고, 그 다음으로 많은 곳을 뒤집는다. (마찬가지고 더 많으면 안뒤집는다.)
3. 한 줄을 뒤집었을 때, 새로 1이 생긴 직각 줄에 1이 추가된다면 안뒤집는다.

1. 1이 가장 많은 곳 중에서
    - 해당 줄의 1이 더 많아지지 않을 때
    - 뒤집은 이후 1이 새로 생긴곳의 수직 줄에 1이 이미 있을 때? 0이 더 많을 때?
    뒤집는다.

2. 위 조건을 반복한다. 모든 줄이 0이 더 많으면 종료.



'''