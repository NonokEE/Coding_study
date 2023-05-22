import sys
ip = sys.stdin.readline

N = int(ip())
tree = {}

for _ in range(N):
    head, l, r = ip().split()
    tree[head] = [l, r]

def prefix(head):
    if head == '.':
        return

    print(head, end="")
    prefix(tree[head][0])
    prefix(tree[head][1])

def infix(head):
    if head == '.':
        return

    infix(tree[head][0])
    print(head, end="")
    infix(tree[head][1])

def postfix(head):
    if head == '.':
        return

    postfix(tree[head][0])
    postfix(tree[head][1])
    print(head, end="")

prefix('A')
print()
infix('A')
print()
postfix('A')


''' 트리 순회
시간 2초 메모리 128MB

이진트리 줄테니까 전위 중위 후위 출력하세요

- 입력 -
첫 줄에 노드 개수 N. 1이상 26이하
둘째줄부터 자신 왼쪽 오른쪽
이름은 항상 ABCD순으로. 자식이 없으면 .

- 출력-

--1트--: 결과
파이썬에서는 간단하게 딕셔너리로 트리 정보를 저장할 수 있답니다 오옹 나이스

'''