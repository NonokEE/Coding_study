import sys
ip = sys.stdin.readline

n = int(ip())

#a의 우선순위가 b보다 높으면 1을 반환, 아니면 0을 반환
#a가 b보다 우선이 되어야 해? a를 b보다 올릴까?
def condition(a, b):    
    if abs(a) < abs(b):
        return 1
    elif abs(a) == abs(b):
        if a < b:
            return 1
        else:
            return 0
    else: 
        return 0

heap = [None]  # 빈 힙이지만 인덱스 이쁘게 해주기 위해서 0번을 None으로 넣음. 
h_length = 0

for _ in range(n):
    x = int(ip())

    # 삽입
    if x: 
        h_length += 1
        heap.append(x)

        # 힙 재정렬
        current = h_length
        while current > 1:
            parent = current//2
            if condition(heap[current], heap[parent]):
                temp = heap[parent]
                heap[parent] = heap[current]
                heap[current] = temp
                current = parent
            else:
                break

    # pop        
    else:
        # 힙이 남아있다면
        if h_length: 
            print(heap[1])
            heap[1] = heap[h_length]
            heap.pop()
            h_length -= 1

            # 힙 재정렬
            current = 1
            while current*2 <= h_length: # 좌자식이 존재할 수 있는 조건. 존재하지 않는다면 리프노드이므로 루프 끝

                # 자식 노드 배치
                l_child = current*2
                r_child = current*2+1

                # 자식 비교
                if r_child > h_length: # 우자식이 없는 경우 좌자식과 비교
                    greater = l_child
                else:
                    if condition(heap[l_child], heap[r_child]):
                        greater = l_child
                    else:
                        greater = r_child

                # 부모 자식 비교
                if condition(heap[greater], heap[current]):
                    temp = heap[greater]
                    heap[greater] = heap[current]
                    heap[current] = temp
                    current = greater
                else:
                    break

        # 힙이 비어있다면
        else: 
            print(0)   

''' 절댓값 힙
절댓값 힙이란?
1. 배열에 0이 아닌 정수를 넣는다.
2. 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
   절댓값이 가장 작은 값이 여러 개인 경우, 가장 작은 수를 출력하고 배열에서 제거한다. (-9랑 9면 -9가 선택된다는 얘기)

프로그램은 비어있는 배열에서 시작한다.

- 입력 -
연산의 개수 N이 주어짐. (1 이상 100,000 이하)
다음 N개의 줄에 연산에 대한 정보를 나타내는 정수 x.
x가 0이 아니라면 배열에 x를 넣는다. x가 0이라면 배열에서 절댓값이 가장 작은 값을 출력하고 배열에서 제거한다.
정수는 int 범위 내에서 전부 입력됨.

만약 배열이 비어있는데 0이 들어오면 그냥 0을 출력한다.

시간 1초(추가없음) 메모리 256MB

--1트--: 결과
절댓값 힙이라니까 힙을 구현하면 되겠네요. 중복 정수 입력도 들어오나? 딱히 상관 없을 것 같긴 함
절댓값순으로, 그리고 같으면 작은 순으로 min힙 구현합시다.

배열 인덱스 말고 자연스 인덱스로 생각할 때,
부모 = 자식의 인덱스 // 2
왼쪽 자식 = 부모의 인덱스 * 2
오른쪽 자식 = 부모의 인덱스 * 2 + 1

0 1 2 3 4 5

만약 파이썬이라서 느리면, deque사용
'''