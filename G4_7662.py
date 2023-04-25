import sys
ip = sys.stdin.readline

t = int(ip())

def is_a_smaller_then_b(a,b): return a[0] < b[0]
def is_a_bigger_then_b(a,b): return a[0] > b[0]

def pop_heap(order:str, heap:list, h_length):
    val, id = heap[1]
    heap[1] = heap[h_length]
    heap.pop()
    h_length -= 1

    cur = 1
    while cur*2 <= h_length:

        l_child = cur*2
        r_child = cur*2+1

        if r_child > h_length:
            prior = l_child
        else:
            if order == "min":
                if is_a_smaller_then_b(heap[l_child], heap[r_child]):
                    prior = l_child
                else:
                    prior = r_child
            else:
                if is_a_bigger_then_b(heap[l_child], heap[r_child]):
                    prior = l_child
                else:
                    prior = r_child

        if order == "min":
            condition = is_a_smaller_then_b(heap[prior], heap[cur])
        else:
            condition = is_a_bigger_then_b(heap[prior], heap[cur])
        if condition:
            temp = heap[prior]
            heap[prior] = heap[cur]
            heap[cur] = temp
            cur = prior
        else:
            break

    return val, id
      


def pop_min_heap():
    pass

for _ in range(t):

    k = int(ip())
    min_heap = [None]
    max_heap = [None]
    h_length = 0
    
    id = 1
    visited = []

    # TC별 연산 입력 #
    for _ in range(k):
        order, n = ip().strip().split()
        n = int(n)

        #삽입
        if order == "I":    
            h_length += 1
            min_heap.append((n, id))
            max_heap.append((n, id))
            id += 1

            # min힙 재정렬
            cur = len(min_heap)-1
            while cur > 1:
                parrent = cur//2
                if is_a_smaller_then_b(min_heap[cur], min_heap[parrent]):
                    temp = min_heap[parrent]
                    min_heap[parrent] = min_heap[cur]
                    min_heap[cur] = temp
                    cur = parrent
                else:
                    break

            # max힙 재정렬
            cur = len(max_heap)-1
            while cur > 1:
                parrent = cur//2
                if is_a_bigger_then_b(max_heap[cur], max_heap[parrent]):
                    temp = max_heap[parrent]
                    max_heap[parrent] = max_heap[cur]
                    max_heap[cur] = temp
                    cur = parrent
                else:
                    break        

        #삭제   
        else:               
            if h_length:   # 큐에 값이 있는 경우에만 연산 진행 
                
                if n == 1:  #최댓값 삭제인 경우
                    o = "max"
                    heap = max_heap
                else:       #최솟값 삭제인 경우
                    o = "min"
                    heap = min_heap
                
                _, top = pop_heap(o, heap, len(heap)-1)
                h_length -= 1

                while top in visited:
                    _, top = pop_heap(o, heap, len(heap)-1)
                else:
                    visited.append(top)
                                    
    # TC별 동기화 및 최종출력 #
    if h_length:
        _, top = max_heap[1]
        while top in visited: 
            pop_heap("max", max_heap, len(max_heap)-1)

        _, top = min_heap[1]
        while top in visited: 
            pop_heap("min", min_heap, len(min_heap)-1)

        print(max_heap[1][0], min_heap[1][0])

    else:
        print("EMPTY")

''' 이중 우선순위 큐
큐인데, 선입선출이 아니고 우선순위에 따라서 팝하는거.
두 가지 연산이 사용되는데, 하나는 삽입, 다른 사나는 삭제
그리고 삭제는 가장 높은걸 삭제할지 가장 낮은걸 삭제할지 정할 수 있다.

정수만 저장하는 이중 우선순위 큐 Q가 있고, 각 정수값들 자체가 우선순위임.
Q에 적용될 연산이 주어질 때 이를 처리한 후 최종적으로 Q에 저장된 데이터 중 최댓값과 최솟값을 출력하세요.

- 입력 -
T개의 TC, 첫 줄에 입력 데이터의 수를 자타내는 T가 주어짐 (T가 한 입력 묶음의 개수라는 뜻)
각 TC의 첫 줄에는 입력 개수 k가 주어짐 (T번쨰 TC의 k번째 입력)
각 k줄에 D또는 I + 정수가 입력됨
I k는 정수 k를 입력
D 1은 최댓값삭제, D -1은 최솟값 삭제, 큐가 비어있는데 D가 들어오면 연산 무시

각 TC가 끝날 때 큐에 남아있는 값 중 최댓값과 최솟값을 출력
두 값은 한 줄에 출력하되 하나의 공백. 큐가 비어있으면 EMPTY 출력

시간 6초 메모리 256MB

--2트--: 정신 나갈거같애
최소한 힙 구현은 해야지
양쪽 힙 동기화하는게 문제임. 
원소를 넣을 때 튜플 형태로 id를 같이 넣으라고 한다 오오 천재
진짜 개천잰가???

삭제를 각각 따로 해도 됨. 다만, id를 통해서 상대쪽에서 이미 삭제된 노드였다면 유효하지 않은 노드가 되는 셈이다 키야

--1트--: 될리가 있냐?
시간이 굉장히 널널합니다
우선순위 큐는 힙으로 구현하는걸로 알고 있는데, 이중이면?
min heap, max heap 두개 다 쓰는게 가장 간단해 보이긴 함.
문제는 한 쪽에서 팝 할때 다른 쪽에서 어떻게 처리해주느냐.
웬만하면 리프쪽에서 제거가 될거라서 크게 문제는 없을 것 같긴 해.
인덱스를 어떻게 정리하느냐가 문제지.
근데 반대쪽에서 제거하는게 결국엔 탐색 들어가야돼서 그다지 효과적이지 않을 것 같은데?

그냥 deque랑 정렬로 날먹해봐? 시간도 널널한데
아니 그냥 max랑 min 뽑으면 안됨?
이게 되면 개날먹인데 ㅋㅋ
'''