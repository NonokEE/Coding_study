import sys
ip = sys.stdin.readline

N = int(ip())
tree = {}         # tree[n] = n의 부모
parent = set([1]) # 누군가의 부모인 노드들. 1이 루트니까 무조건 넣고 시작
child = set([])   # 누군가의 자식인 노드들.

for _ in range(N-1):
    n1, n2 = map(int, ip().split())

    if n1 in parent: #n1이 부모인 경우
        tree[n2] = n1
        parent.add(n1)
        child.add(n2)
    elif n2 in parent: #n2가 부모인 경우
        tree[n1] = n2
        parent.add(n2)
        child.add(n1)
    else: #어느 쪽도 부모가 아닌 경우, 누군가의 자식인 쪽이 부모가 됨
        if n1 in child:# n1이 부모
            tree[n2] = n1
            parent.add(n1)
            child.add(n2)
        else:# n1이 부모
            tree[n1] = n2
            parent.add(n2)
            child.add(n1)

for i in range(2, N+1):
    print(tree[i])


''' 트리의 부모 찾기
시간 1초 메모리 256MB

루트없는 트리를 줄거에요. 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하세요.

- 입력 -
첫 줄에 노드 개수 N
둘째 줄 부터 연결 구조

- 출력-
2번노드부터 끝 노드까지 부모 출력
(1번은 루트니까 출력 없습니다)

--2트--:
키 에러가 났다는건 상정 못한 경우가 있다는건데 그게 가능해?

--1트--: 키 에러
간단하게 딕셔너리로 안되려나?
되기야는 하는데, 입력에서 어느쪽이 부모고 자식인지 알 수 없음.

새로 추가되는거니까, 무조건 한 쪽은 이미 있는거고 한 쪽은 없는거임!
없는 쪽이 자식노드다.
가 아닐 수도 있다.

한쪽이 확실히 부모면 상관없는데, 아직 부모자식이 확실하지 않은 경우가 있다.
둘 다 부모가 아닌 경우면 무조건 한쪽은 새로운 노드고 한쪽은 기존에 있던 노드다.
누군가의 자식인 쪽이 부모가 되면 됨

'''