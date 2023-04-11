import sys
ip = sys.stdin.readline

def matprint(arr):
    for i in range(len(arr)):
        print(arr[i], end="\n")

### 입력 및 초기화


### 알고리즘

''' 사탕꺼내기
원형 통이 있고 0번부터 사탕이 있는데, 원형통의 입구 부분에서만 사탕을 꺼낼 수 있다.
총 사탕 개수 N, 꺼낼 사탕의 개수와 번호가 주어짐.
첫 위치의 사탕을 꺼내는 것은 회전에 포함하지 않음. 
사탕을 꺼낸 후에는 왼쪽으로 굴러온다는데, 첫 인덱스 팝이라고 생각하면 됨.
"
금고 회전 수 문제.
좌회전, 우회전을 지원하는 큐가 있고, 큐의 첫 원소만 꺼낼 수 있다.

12345

2345

3452 1

452

245 2

45

54 3




'''