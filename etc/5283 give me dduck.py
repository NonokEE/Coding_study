import sys
ip = sys.stdin.readline

def matprint(arr):
    for i in range(len(arr)):
        print(arr[i], end="\n")

### 입력 및 초기화
N= int(ip())
field = []

for i in range(N):
    field.append(list(map(int, ip().split())))


''' 떡내놔
집 가는 길은 길이 N의 정사각형 맵, 모든 칸에는 호랑이가 한마리 있다.
엄마는 제일 왼쪽 위 0행0열에서 출발, 제일 오른쪽 아래로 가야한다. 상하좌우 한칸씩만 이동 가능
집 가는 길에 만나는 모든 호랑이에게 반드시 원하는 만큼의 떡을 줘야하고, 스타트 지점도 포함한다.

"
그리디냐 DP냐 서치냐
당장 예제만 가지고 그리디로 하면 정답이 나오긴 하는데, 

0   2 0 0
0   2 0 0
0  90 0 0
90  0 0 0

이런 식이면 그리디로 못 푼다. 
DP로 접근을 해보자





'''